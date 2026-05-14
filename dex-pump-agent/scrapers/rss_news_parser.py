"""
RSS News Parser — Monitors crypto news feeds for personality mentions.
Detects early mentions of Musk/Trump/etc. in crypto press before the
pump reaches DexScreener trending. Complements DexScreener watcher.
"""

import asyncio
import aiohttp
import json
import os
import re
import hashlib
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict

try:
    import feedparser
except ImportError:
    feedparser = None

# === CONFIG ===
POLL_INTERVAL_SECONDS = int(os.getenv("RSS_POLL_INTERVAL", 180))  # 3 minutes

RSS_FEEDS = [
    # Tier 1: Fast crypto news
    "https://cointelegraph.com/rss",
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cryptonews.com/news/feed/",
    "https://decrypt.co/feed",
    "https://thedefiant.io/feed",
    # Tier 2: Social/meme-focused
    "https://bitcoinist.com/feed/",
    "https://u.today/rss",
    "https://ambcrypto.com/feed/",
]

PERSONALITY_PATTERNS = {
    "musk": [
        r"\belon\s*musk\b", r"\bmusk\b", r"\bgrok\b", r"\bkekius\b",
        r"\bfloki\b", r"\bdogecoin\b", r"\bdoge\b", r"\bstarlink\b",
        r"\bspacex\b", r"\btesla\b.*crypto", r"\bxai\b",
    ],
    "trump": [
        r"\btrump\b", r"\bmaga\b", r"\bmelania\b", r"\bwlfi\b",
        r"\bworld liberty\b", r"\bofficial trump\b",
    ],
    "vance": [r"\bjd\s*vance\b", r"\bvance\b.*crypto"],
    "milei": [r"\bmilei\b", r"\bargentina\b.*crypto"],
}

# Action keywords that boost signal relevance
ACTION_KEYWORDS = [
    r"\bpump\b", r"\bsurge[sd]?\b", r"\bsoar\b", r"\brall(?:y|ied|ies)\b",
    r"\bskyrocket\b", r"\bmoon\b", r"\b100[x%]\b", r"\btweet\b",
    r"\bpost(?:ed|s)?\b", r"\bname\s*change\b", r"\bprofile\b",
    r"\bmemecoin\b", r"\btoken\b.*launch", r"\bnew\s*coin\b",
]

DATA_DIR = Path(os.getenv("DATA_DIR", str(Path(__file__).parent.parent / "data")))
SEEN_ARTICLES_FILE = DATA_DIR / "seen_rss_articles.json"
SIGNALS_OUTPUT_FILE = DATA_DIR / "rss_signals.json"
LOG_FILE = DATA_DIR / "logs" / "rss_news_parser.log"

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class NewsSignal:
    article_id: str
    title: str
    link: str
    published: str
    source_feed: str
    matched_personality: str
    matched_patterns: list
    action_keywords_found: list
    relevance_score: int
    detected_at: str
    summary: str

    def to_alert_message(self) -> str:
        return (
            f"*RSS SIGNAL* -- {self.matched_personality.upper()}\n"
            f"Title: {self.title}\n"
            f"Source: {self.source_feed}\n"
            f"Published: {self.published}\n"
            f"Actions: {', '.join(self.action_keywords_found) or 'none'}\n"
            f"Relevance: {self.relevance_score}/100\n"
            f"Link: {self.link}"
        )


def load_seen_articles() -> dict:
    if not SEEN_ARTICLES_FILE.exists():
        return {}
    try:
        with open(SEEN_ARTICLES_FILE) as f:
            data = json.load(f)
        cutoff = datetime.now(timezone.utc) - timedelta(days=7)
        return {
            k: v for k, v in data.items()
            if datetime.fromisoformat(v) > cutoff
        }
    except Exception:
        return {}


def save_seen_articles(seen: dict):
    SEEN_ARTICLES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SEEN_ARTICLES_FILE, 'w') as f:
        json.dump(seen, f)


def article_id(entry: dict) -> str:
    raw = entry.get('id', entry.get('link', entry.get('title', '')))
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def match_article(title: str, summary: str) -> tuple[Optional[str], list, list]:
    text = f"{title} {summary}".lower()

    best_personality = None
    best_patterns = []

    for personality, patterns in PERSONALITY_PATTERNS.items():
        matched = [p for p in patterns if re.search(p, text, re.IGNORECASE)]
        if len(matched) > len(best_patterns):
            best_personality = personality
            best_patterns = matched

    action_found = [
        kw for kw in ACTION_KEYWORDS
        if re.search(kw, text, re.IGNORECASE)
    ]

    return best_personality, best_patterns, action_found


def calculate_news_relevance(
    matched_patterns: list,
    action_keywords: list,
    age_minutes: float
) -> int:
    score = 0

    # Pattern match strength (max 30)
    score += min(len(matched_patterns) * 15, 30)

    # Action keywords (max 30)
    score += min(len(action_keywords) * 10, 30)

    # Freshness (max 25)
    if age_minutes < 15:
        score += 25
    elif age_minutes < 60:
        score += 20
    elif age_minutes < 180:
        score += 10
    elif age_minutes < 720:
        score += 5

    # Multiple action keywords = convergence bonus (max 15)
    if len(action_keywords) >= 3:
        score += 15
    elif len(action_keywords) >= 2:
        score += 8

    return min(score, 100)


def save_signal(signal: NewsSignal):
    SIGNALS_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    signals = []
    if SIGNALS_OUTPUT_FILE.exists():
        try:
            with open(SIGNALS_OUTPUT_FILE) as f:
                signals = json.load(f)
        except Exception:
            pass

    signals.append(asdict(signal))

    # Keep last 200 signals
    signals = signals[-200:]
    with open(SIGNALS_OUTPUT_FILE, 'w') as f:
        json.dump(signals, f, indent=2)


async def fetch_feed(session: aiohttp.ClientSession, url: str) -> list:
    if feedparser is None:
        logger.error("feedparser not installed, run: pip install feedparser")
        return []
    try:
        async with session.get(
            url, timeout=aiohttp.ClientTimeout(total=15)
        ) as resp:
            if resp.status != 200:
                logger.warning(f"RSS {resp.status} for {url}")
                return []
            text = await resp.text()
            feed = feedparser.parse(text)
            return feed.entries
    except Exception as e:
        logger.error(f"RSS fetch error for {url}: {e}")
        return []


async def send_telegram_alert(session: aiohttp.ClientSession, message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        async with session.post(url, json={
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown',
            'disable_web_page_preview': True,
        }, timeout=aiohttp.ClientTimeout(total=10)) as resp:
            if resp.status != 200:
                logger.warning(f"Telegram {resp.status}")
    except Exception as e:
        logger.error(f"Telegram failed: {e}")


async def scan_cycle(session: aiohttp.ClientSession, seen: dict):
    logger.info("RSS scan starting")
    tasks = [fetch_feed(session, url) for url in RSS_FEEDS]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    new_signals = 0
    now = datetime.now(timezone.utc)

    for feed_url, entries in zip(RSS_FEEDS, results):
        if isinstance(entries, Exception):
            logger.error(f"Feed {feed_url} failed: {entries}")
            continue

        for entry in entries:
            aid = article_id(entry)
            if aid in seen:
                continue

            title = entry.get('title', '')
            summary = entry.get('summary', entry.get('description', ''))
            personality, patterns, actions = match_article(title, summary)

            if not personality:
                seen[aid] = now.isoformat()
                continue

            # Calculate age
            published = entry.get('published_parsed')
            if published:
                import calendar
                pub_ts = calendar.timegm(published)
                age_minutes = (now.timestamp() - pub_ts) / 60
            else:
                age_minutes = 30  # assume moderate freshness

            relevance = calculate_news_relevance(patterns, actions, age_minutes)

            signal = NewsSignal(
                article_id=aid,
                title=title,
                link=entry.get('link', ''),
                published=entry.get('published', ''),
                source_feed=feed_url.split('/')[2],
                matched_personality=personality,
                matched_patterns=patterns,
                action_keywords_found=actions,
                relevance_score=relevance,
                detected_at=now.isoformat(),
                summary=summary[:500],
            )

            save_signal(signal)
            seen[aid] = now.isoformat()
            new_signals += 1

            if relevance >= 50:
                await send_telegram_alert(session, signal.to_alert_message())
                logger.info(f"HIGH RSS: {title[:60]} score={relevance}")
            else:
                logger.info(f"Low RSS: {title[:60]} score={relevance}")

    save_seen_articles(seen)
    logger.info(f"RSS scan done: {new_signals} new signals")


async def main():
    logger.info("RSS news parser started")
    seen = load_seen_articles()

    async with aiohttp.ClientSession(
        headers={'User-Agent': 'atomus-newsbot/1.0'}
    ) as session:
        while True:
            try:
                await scan_cycle(session, seen)
            except Exception as e:
                logger.error(f"RSS cycle failed: {e}", exc_info=True)

            await asyncio.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    asyncio.run(main())
