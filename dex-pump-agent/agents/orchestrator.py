"""
Orchestrator for Claude analysis agents.
- Subscribes to signals queue (event-driven signal interpreter)
- Cron jobs for daily compliance and weekly research
- Calls Claude API with structured prompts
- Persists analyses to filesystem (Markdown) + optional DB

Agents are READ-ONLY on operational data. They never modify code,
configs, or execute trades. They produce interpretations that inform
the human operator.
"""

import asyncio
import os
import json
import re
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

REPO_PATH = Path(os.getenv("REPO_PATH", str(Path(__file__).parent.parent)))
ANALYSIS_PATH = REPO_PATH / "analysis"

# Ensure analysis directories exist
for subdir in ("signals", "compliance", "research"):
    (ANALYSIS_PATH / subdir).mkdir(parents=True, exist_ok=True)


# ============================================================
# CLAUDE API CLIENT
# ============================================================

class ClaudeClient:
    """Wrapper around the Anthropic API for agent calls."""

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "")
        self._client = None

    async def _get_client(self):
        if self._client is None:
            try:
                from anthropic import AsyncAnthropic
                self._client = AsyncAnthropic(api_key=self.api_key)
            except ImportError:
                logger.error("anthropic package not installed")
                raise
        return self._client

    async def analyze(
        self,
        system_prompt: str,
        user_message: str,
        max_tokens: int = 4000,
        model: str = "claude-sonnet-4-20250514",
    ) -> str:
        """Send a message to Claude and return the response text."""
        if not self.api_key:
            logger.error("No ANTHROPIC_API_KEY set")
            return '{"error": "No API key configured"}'

        client = await self._get_client()
        try:
            response = await client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
            )
            return response.content[0].text
        except Exception as e:
            logger.error(f"Claude API error: {e}", exc_info=True)
            return f'{{"error": "{str(e)}"}}'


claude = ClaudeClient()


# ============================================================
# TELEGRAM ALERTS
# ============================================================

async def send_telegram(message: str, critical: bool = False):
    """Send a Telegram notification."""
    import aiohttp

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv(
        "TELEGRAM_CRITICAL_CHAT_ID" if critical else "TELEGRAM_CHAT_ID"
    )
    if not token or not chat_id:
        logger.info(f"Telegram disabled: {message[:80]}...")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(url, json={
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'Markdown',
            })
    except Exception as e:
        logger.error(f"Telegram failed: {e}")


# ============================================================
# DATA LOADING (filesystem-based, no DB dependency)
# ============================================================

def load_historical_events() -> list:
    """Load the historical events dataset for context."""
    events_path = REPO_PATH / "data" / "historical_events.json"
    if not events_path.exists():
        return []
    with open(events_path) as f:
        data = json.load(f)
    return data.get("events", [])


def load_hot_watchlist() -> dict:
    """Load the current hot watchlist from DexScreener watcher."""
    wl_path = REPO_PATH / "data" / "hot_watchlist.json"
    if not wl_path.exists():
        return {}
    try:
        with open(wl_path) as f:
            return json.load(f)
    except Exception:
        return {}


def load_rss_signals(hours: int = 24) -> list:
    """Load recent RSS signals."""
    sig_path = REPO_PATH / "data" / "rss_signals.json"
    if not sig_path.exists():
        return []
    try:
        with open(sig_path) as f:
            signals = json.load(f)
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        return [
            s for s in signals
            if datetime.fromisoformat(s["detected_at"]) > cutoff
        ]
    except Exception:
        return []


def load_recent_analyses(days: int = 7) -> list:
    """Load recent signal analyses from the analysis directory."""
    analyses = []
    signals_dir = ANALYSIS_PATH / "signals"
    if not signals_dir.exists():
        return []

    for month_dir in sorted(signals_dir.iterdir(), reverse=True):
        if not month_dir.is_dir():
            continue
        for f in sorted(month_dir.iterdir(), reverse=True):
            if f.suffix == ".md":
                try:
                    content = f.read_text(encoding="utf-8")
                    analyses.append({
                        "file": f.name,
                        "content": content[:2000],
                    })
                except Exception:
                    pass
            if len(analyses) >= 20:
                break
        if len(analyses) >= 20:
            break

    return analyses


# ============================================================
# AGENT 1 — SIGNAL INTERPRETER (event-driven)
# ============================================================

from .prompts import SIGNAL_INTERPRETER_PROMPT


async def interpret_signal(signal_data: dict):
    """
    Analyze a signal using Claude.
    signal_data should contain at minimum: ticker, source, score, raw_payload.
    """
    signal_id = signal_data.get("id", "unknown")
    ticker = signal_data.get("ticker", "unknown")

    # Build context
    historical = load_historical_events()
    similar = [
        e for e in historical
        if e.get("ticker", "").lower() == ticker.lower()
        or e.get("personality", "").lower() in signal_data.get("source", "").lower()
    ]

    watchlist = load_hot_watchlist()
    watchlist_entry = next(
        (v for v in watchlist.values() if v.get("symbol", "").lower() == ticker.lower()),
        None,
    )

    recent_rss = [
        s for s in load_rss_signals(72)
        if ticker.lower() in s.get("title", "").lower()
        or ticker.lower() in s.get("summary", "").lower()
    ]

    context = {
        "signal": signal_data,
        "similar_historical_events": similar[:5],
        "hot_watchlist_entry": watchlist_entry,
        "related_rss_signals": recent_rss[:5],
        "current_time": datetime.now(timezone.utc).isoformat(),
    }

    context_json = json.dumps(context, default=str, indent=2)

    result_text = await claude.analyze(
        system_prompt=SIGNAL_INTERPRETER_PROMPT,
        user_message=f"Analyze this signal in context:\n\n{context_json}",
        max_tokens=2000,
    )

    # Parse JSON response
    try:
        result = json.loads(result_text)
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', result_text, re.DOTALL)
        if match:
            try:
                result = json.loads(match.group())
            except json.JSONDecodeError:
                logger.error(f"Failed to parse response: {result_text[:500]}")
                return None
        else:
            logger.error(f"No JSON in response: {result_text[:500]}")
            return None

    # Save to filesystem
    date_dir = ANALYSIS_PATH / "signals" / datetime.now(timezone.utc).strftime("%Y-%m")
    date_dir.mkdir(parents=True, exist_ok=True)
    analysis_file = date_dir / f"signal_{signal_id}.md"
    with open(analysis_file, 'w', encoding='utf-8') as f:
        f.write(f"# Signal Analysis #{signal_id}\n\n")
        f.write(f"**Ticker**: {ticker}\n")
        f.write(f"**Source**: {signal_data.get('source', 'N/A')}\n")
        f.write(f"**Score**: {signal_data.get('score', 'N/A')}\n")
        f.write(f"**Analyzed**: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write(f"## Recommendation: {result.get('recommendation')}\n\n")
        f.write(f"**Conviction**: {result.get('conviction_score')}/100\n\n")
        f.write(f"## Interpretation\n\n{result.get('interpretation')}\n\n")
        if result.get('risk_factors'):
            f.write("## Risk Factors\n\n")
            for rf in result['risk_factors']:
                f.write(f"- {rf}\n")
            f.write("\n")
        if result.get('similar_historical_events'):
            f.write("## Similar Historical Events\n\n")
            for ev in result['similar_historical_events']:
                f.write(f"- {ev.get('date')} -- {ev.get('ticker')} -- {ev.get('outcome')}\n")
            f.write("\n")
        f.write(f"## Reasoning Summary\n\n{result.get('reasoning_summary')}\n")

    # Telegram alert for actionable recommendations
    if result.get('recommendation') in ('EXECUTE', 'INVESTIGATE'):
        await send_telegram(
            f"*Agent Analysis* -- Signal #{signal_id} ({ticker})\n"
            f"Recommendation: *{result.get('recommendation')}*\n"
            f"Conviction: {result.get('conviction_score')}/100\n\n"
            f"_{result.get('reasoning_summary', '')[:300]}_"
        )

    logger.info(f"Signal {signal_id} analyzed: {result.get('recommendation')}")
    return result


# ============================================================
# AGENT 2 — DAILY COMPLIANCE REVIEWER (cron 06:00 UTC)
# ============================================================

from .prompts import COMPLIANCE_PROMPT


async def daily_compliance_review():
    """Generate daily compliance and operational health report."""
    yesterday = datetime.now(timezone.utc).date() - timedelta(days=1)

    # Gather context from filesystem
    recent_analyses = load_recent_analyses(1)
    watchlist = load_hot_watchlist()
    rss_signals = load_rss_signals(24)
    historical = load_historical_events()

    # Load backtester results if available
    bt_results_path = REPO_PATH / "backtester" / "results" / "backtest_results.json"
    bt_results = {}
    if bt_results_path.exists():
        try:
            with open(bt_results_path) as f:
                bt_results = json.load(f)
        except Exception:
            pass

    context = {
        "report_date": yesterday.isoformat(),
        "signal_analyses_count": len(recent_analyses),
        "recent_analyses_summary": [
            a["content"][:500] for a in recent_analyses[:5]
        ],
        "hot_watchlist_count": len(watchlist),
        "rss_signals_24h": len(rss_signals),
        "rss_high_relevance": [
            s for s in rss_signals if s.get("relevance_score", 0) >= 50
        ],
        "backtest_stats": bt_results.get("combined_stats", {}),
        "total_historical_events": len(historical),
    }

    context_json = json.dumps(context, default=str, indent=2)

    report = await claude.analyze(
        system_prompt=COMPLIANCE_PROMPT,
        user_message=(
            f"Produce the daily compliance report for {yesterday}:\n\n"
            f"{context_json}"
        ),
        max_tokens=4000,
    )

    # Save report
    report_dir = ANALYSIS_PATH / "compliance"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"{yesterday.isoformat()}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    # Extract health score for Telegram
    health_match = re.search(r'OVERALL HEALTH[:\s]*(\d+)', report, re.IGNORECASE)
    health = health_match.group(1) if health_match else "N/A"

    await send_telegram(
        f"*Daily Compliance* -- {yesterday}\n"
        f"Overall health: {health}/100\n\n"
        f"Full report: `analysis/compliance/{yesterday}.md`"
    )

    logger.info(f"Daily compliance report generated for {yesterday}")


# ============================================================
# AGENT 3 — WEEKLY R&D ANALYST (cron Sunday 08:00 UTC)
# ============================================================

from .prompts import RD_PROMPT


async def weekly_research_review():
    """Generate weekly strategy R&D report."""
    week_num = datetime.now(timezone.utc).strftime("%Y-W%V")
    week_start = datetime.now(timezone.utc) - timedelta(days=7)

    # Gather data
    recent_analyses = load_recent_analyses(7)
    rss_signals = load_rss_signals(168)  # 7 days
    historical = load_historical_events()

    # Analyze which sources produced signals
    source_breakdown = {}
    for a in recent_analyses:
        content = a["content"]
        source_match = re.search(r'\*\*Source\*\*:\s*(\S+)', content)
        rec_match = re.search(r'## Recommendation:\s*(\S+)', content)
        if source_match:
            src = source_match.group(1)
            rec = rec_match.group(1) if rec_match else "unknown"
            if src not in source_breakdown:
                source_breakdown[src] = {"total": 0, "execute": 0, "watch": 0, "ignore": 0}
            source_breakdown[src]["total"] += 1
            source_breakdown[src][rec.lower()] = source_breakdown[src].get(rec.lower(), 0) + 1

    context = {
        "week": week_num,
        "analyses_count": len(recent_analyses),
        "source_breakdown": source_breakdown,
        "rss_signals_count": len(rss_signals),
        "rss_personality_breakdown": _count_by_key(rss_signals, "matched_personality"),
        "historical_event_count": len(historical),
        "sample_analyses": [a["content"][:1000] for a in recent_analyses[:10]],
    }

    context_json = json.dumps(context, default=str, indent=2)

    report = await claude.analyze(
        system_prompt=RD_PROMPT,
        user_message=f"Produce the weekly R&D report. Data:\n\n{context_json}",
        max_tokens=6000,
    )

    # Save
    report_dir = ANALYSIS_PATH / "research"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"{week_num}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    await send_telegram(
        f"*Weekly R&D Report* -- {week_num}\n\n"
        f"Available at: `analysis/research/{week_num}.md`\n\n"
        f"_Review and decide on proposed adjustments._"
    )

    logger.info(f"Weekly R&D report generated for {week_num}")


def _count_by_key(items: list, key: str) -> dict:
    counts = {}
    for item in items:
        val = item.get(key, "unknown")
        counts[val] = counts.get(val, 0) + 1
    return counts


# ============================================================
# SCHEDULER / MAIN
# ============================================================

async def run_scheduler():
    """
    Simple async scheduler that runs compliance daily at 06:00 UTC
    and research weekly on Sunday at 08:00 UTC.
    No external dependencies (no APScheduler needed).
    """
    logger.info("Scheduler started")

    last_compliance_date = None
    last_research_week = None

    while True:
        now = datetime.now(timezone.utc)

        # Daily compliance at 06:00 UTC
        if now.hour >= 6 and now.date() != last_compliance_date:
            try:
                await daily_compliance_review()
                last_compliance_date = now.date()
            except Exception as e:
                logger.error(f"Compliance review failed: {e}", exc_info=True)

        # Weekly research on Sunday at 08:00 UTC
        week_id = now.strftime("%Y-W%V")
        if now.weekday() == 6 and now.hour >= 8 and week_id != last_research_week:
            try:
                await weekly_research_review()
                last_research_week = week_id
            except Exception as e:
                logger.error(f"Research review failed: {e}", exc_info=True)

        await asyncio.sleep(300)  # Check every 5 minutes


async def main():
    """Main entry point: runs scheduler + optional signal queue consumer."""
    logger.info("Claude agents orchestrator starting")

    # Run scheduler
    await run_scheduler()


if __name__ == "__main__":
    asyncio.run(main())
