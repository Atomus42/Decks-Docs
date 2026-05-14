"""
DexScreener Watcher — Polls DexScreener trending feed and identifies
coins matching personality patterns (Musk, Trump, etc.).
Outputs: hot_watchlist updates + alerts on high-relevance new entries.
"""

import asyncio
import aiohttp
import json
import time
import re
import os
import logging
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# === CONFIG ===
POLL_INTERVAL_SECONDS = int(os.getenv("DEX_POLL_INTERVAL", 300))
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/search"
TRENDING_API = "https://api.dexscreener.com/token-boosts/top/v1"

PERSONALITY_KEYWORDS = {
    "musk": [
        "musk", "elon", "gork", "grok", "kekius", "harrybolz", "harry bolz",
        "dogefather", "dogeson", "asteroid", "floki", "shiba", "starlink",
        "tesla", "spacex", "xai", "neuralink", "boring", "doge",
        "gorklon", "rust", "pepe", "mars",
    ],
    "trump": [
        "trump", "donald", "maga", "patriot", "melania", "barron",
        "ivanka", "eric trump", "trump jr", "wlfi", "world liberty",
        "official trump", "47", "fight",
    ],
    "vance": ["vance", "jd vance"],
    "milei": ["milei", "libra", "argentina"],
    "cz": ["cz", "changpeng", "binance"],
    "vitalik": ["vitalik", "buterin"],
    "trump_jr": ["don jr", "donald jr"],
    "eric_trump": ["eric trump"],
}

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

DATA_DIR = Path(os.getenv("DATA_DIR", str(Path(__file__).parent.parent / "data")))
HOT_WATCHLIST_FILE = DATA_DIR / "hot_watchlist.json"
SEEN_TOKENS_FILE = DATA_DIR / "seen_dexscreener.json"
LOG_FILE = DATA_DIR / "logs" / "dexscreener_watcher.log"

MIN_LIQUIDITY_USD = 10_000
MIN_VOLUME_24H_USD = 50_000
MIN_AGE_HOURS = 0.5

# === LOGGING ===
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)


# === DATA STRUCTURES ===
@dataclass
class TokenSignal:
    address: str
    chain: str
    symbol: str
    name: str
    matched_personality: str
    matched_keywords: list
    price_usd: float
    liquidity_usd: float
    volume_24h_usd: float
    price_change_24h_pct: float
    market_cap: Optional[float]
    pair_age_hours: float
    holders: Optional[int]
    detected_at: str
    dexscreener_url: str
    relevance_score: int

    def to_alert_message(self) -> str:
        return (
            f"*NEW DEX SIGNAL* -- {self.symbol}\n"
            f"Chain: {self.chain}\n"
            f"Personality: {self.matched_personality}\n"
            f"Keywords matched: {', '.join(self.matched_keywords)}\n"
            f"Price: ${self.price_usd:.8f}\n"
            f"Liquidity: ${self.liquidity_usd:,.0f}\n"
            f"24h Volume: ${self.volume_24h_usd:,.0f}\n"
            f"24h Change: {self.price_change_24h_pct:+.1f}%\n"
            f"Age: {self.pair_age_hours:.1f}h\n"
            f"Relevance score: {self.relevance_score}/100\n"
            f"Chart: {self.dexscreener_url}"
        )


# === STATE MANAGEMENT ===
def load_seen_tokens() -> set:
    if not SEEN_TOKENS_FILE.exists():
        return set()
    try:
        with open(SEEN_TOKENS_FILE) as f:
            data = json.load(f)
        cutoff = time.time() - 7 * 24 * 3600
        return {addr for addr, ts in data.items() if ts > cutoff}
    except Exception as e:
        logger.error(f"Failed to load seen tokens: {e}")
        return set()


def save_seen_tokens(seen: set):
    SEEN_TOKENS_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = {addr: time.time() for addr in seen}
    with open(SEEN_TOKENS_FILE, 'w') as f:
        json.dump(data, f)


def load_hot_watchlist() -> dict:
    if not HOT_WATCHLIST_FILE.exists():
        return {}
    try:
        with open(HOT_WATCHLIST_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def update_hot_watchlist(signal: TokenSignal):
    HOT_WATCHLIST_FILE.parent.mkdir(parents=True, exist_ok=True)
    watchlist = load_hot_watchlist()
    watchlist[signal.address] = asdict(signal)

    cutoff = time.time() - 7 * 24 * 3600
    watchlist = {
        addr: data for addr, data in watchlist.items()
        if datetime.fromisoformat(data['detected_at']).timestamp() > cutoff
    }
    if len(watchlist) > 50:
        sorted_items = sorted(
            watchlist.items(),
            key=lambda x: x[1]['relevance_score'],
            reverse=True
        )[:50]
        watchlist = dict(sorted_items)

    with open(HOT_WATCHLIST_FILE, 'w') as f:
        json.dump(watchlist, f, indent=2)


# === CORE LOGIC ===
def match_personality(name: str, symbol: str) -> tuple[Optional[str], list]:
    text = f"{name} {symbol}".lower()
    text = re.sub(r'[^a-z0-9 ]', ' ', text)

    best_match = None
    best_keywords = []

    for personality, keywords in PERSONALITY_KEYWORDS.items():
        matched = [kw for kw in keywords if kw in text]
        if len(matched) > len(best_keywords):
            best_match = personality
            best_keywords = matched

    return best_match, best_keywords


def calculate_relevance_score(pair: dict, matched_keywords: list) -> int:
    score = 0

    # Keyword strength (max 30)
    score += min(len(matched_keywords) * 15, 30)

    # Liquidity (max 20)
    liq = float(pair.get('liquidity', {}).get('usd', 0) or 0)
    if liq > 1_000_000:
        score += 20
    elif liq > 100_000:
        score += 15
    elif liq > 10_000:
        score += 8

    # Volume momentum (max 25)
    vol_24h = float(pair.get('volume', {}).get('h24', 0) or 0)
    vol_1h = float(pair.get('volume', {}).get('h1', 0) or 0)
    if vol_24h > 0:
        avg_hourly = vol_24h / 24
        if vol_1h > avg_hourly * 5:
            score += 25
        elif vol_1h > avg_hourly * 2:
            score += 15
        elif vol_1h > avg_hourly:
            score += 8

    # Price momentum (max 15)
    change_1h = float(pair.get('priceChange', {}).get('h1', 0) or 0)
    if change_1h > 30:
        score += 15
    elif change_1h > 10:
        score += 10
    elif change_1h > 3:
        score += 5

    # Pair age (max 10)
    pair_age_ms = pair.get('pairCreatedAt', 0)
    if pair_age_ms:
        age_hours = (time.time() * 1000 - pair_age_ms) / (1000 * 3600)
        if age_hours < 24:
            score += 10
        elif age_hours < 72:
            score += 6
        elif age_hours < 168:
            score += 3

    return min(score, 100)


def passes_filters(pair: dict) -> bool:
    liq = float(pair.get('liquidity', {}).get('usd', 0) or 0)
    if liq < MIN_LIQUIDITY_USD:
        return False

    vol_24h = float(pair.get('volume', {}).get('h24', 0) or 0)
    if vol_24h < MIN_VOLUME_24H_USD:
        return False

    pair_age_ms = pair.get('pairCreatedAt', 0)
    if pair_age_ms:
        age_hours = (time.time() * 1000 - pair_age_ms) / (1000 * 3600)
        if age_hours < MIN_AGE_HOURS:
            return False

    return True


def build_signal(pair: dict, personality: str, keywords: list) -> TokenSignal:
    base_token = pair.get('baseToken', {})
    pair_age_ms = pair.get('pairCreatedAt', 0)
    age_hours = (time.time() * 1000 - pair_age_ms) / (1000 * 3600) if pair_age_ms else 0

    return TokenSignal(
        address=base_token.get('address', ''),
        chain=pair.get('chainId', 'unknown'),
        symbol=base_token.get('symbol', ''),
        name=base_token.get('name', ''),
        matched_personality=personality,
        matched_keywords=keywords,
        price_usd=float(pair.get('priceUsd', 0) or 0),
        liquidity_usd=float(pair.get('liquidity', {}).get('usd', 0) or 0),
        volume_24h_usd=float(pair.get('volume', {}).get('h24', 0) or 0),
        price_change_24h_pct=float(pair.get('priceChange', {}).get('h24', 0) or 0),
        market_cap=pair.get('marketCap'),
        pair_age_hours=age_hours,
        holders=None,
        detected_at=datetime.now(timezone.utc).isoformat(),
        dexscreener_url=pair.get('url', ''),
        relevance_score=calculate_relevance_score(pair, keywords),
    )


# === DEXSCREENER QUERIES ===
async def fetch_search(session, query: str) -> list:
    try:
        async with session.get(
            DEXSCREENER_API,
            params={'q': query},
            timeout=aiohttp.ClientTimeout(total=10)
        ) as resp:
            if resp.status != 200:
                logger.warning(f"DexScreener {resp.status} for query={query}")
                return []
            data = await resp.json()
            return data.get('pairs', []) or []
    except Exception as e:
        logger.error(f"Fetch error for {query}: {e}")
        return []


async def fetch_all_personalities(session) -> list:
    all_pairs = []
    primary_keywords = [
        "musk", "elon", "trump", "gork", "kekius",
        "harrybolz", "asteroid", "doge", "pepe", "milei",
    ]

    tasks = [fetch_search(session, kw) for kw in primary_keywords]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for r in results:
        if isinstance(r, list):
            all_pairs.extend(r)

    seen_addrs = set()
    deduped = []
    for pair in all_pairs:
        addr = pair.get('baseToken', {}).get('address')
        if addr and addr not in seen_addrs:
            seen_addrs.add(addr)
            deduped.append(pair)

    return deduped


# === TELEGRAM ===
async def send_telegram_alert(session, message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logger.info(f"Telegram disabled, would send: {message[:100]}...")
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
                logger.warning(f"Telegram {resp.status}: {await resp.text()}")
    except Exception as e:
        logger.error(f"Telegram send failed: {e}")


# === MAIN LOOP ===
async def watch_cycle(session, seen_tokens: set):
    logger.info("Starting cycle")
    pairs = await fetch_all_personalities(session)
    logger.info(f"Fetched {len(pairs)} unique pairs")

    new_signals = 0
    high_priority_signals = 0

    for pair in pairs:
        base_token = pair.get('baseToken', {})
        addr = base_token.get('address')
        if not addr or addr in seen_tokens:
            continue

        if not passes_filters(pair):
            continue

        name = base_token.get('name', '')
        symbol = base_token.get('symbol', '')
        personality, keywords = match_personality(name, symbol)

        if not personality:
            continue

        signal = build_signal(pair, personality, keywords)
        seen_tokens.add(addr)
        new_signals += 1

        update_hot_watchlist(signal)

        if signal.relevance_score >= 60:
            high_priority_signals += 1
            await send_telegram_alert(session, signal.to_alert_message())
            logger.info(f"HIGH alert: {signal.symbol} score={signal.relevance_score}")
        else:
            logger.info(f"Low-priority: {signal.symbol} score={signal.relevance_score}")

    save_seen_tokens(seen_tokens)
    logger.info(f"Cycle done: {new_signals} new, {high_priority_signals} high-priority")


async def main():
    logger.info("DexScreener watcher started")
    seen_tokens = load_seen_tokens()

    async with aiohttp.ClientSession(
        headers={'User-Agent': 'atomus-bot/1.0'}
    ) as session:
        while True:
            try:
                await watch_cycle(session, seen_tokens)
            except Exception as e:
                logger.error(f"Cycle failed: {e}", exc_info=True)

            await asyncio.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    asyncio.run(main())
