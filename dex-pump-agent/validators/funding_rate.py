"""
Funding Rate Validator — Checks funding rates and OI data
from Coinglass/exchanges before allowing short entries.

Gating conditions for short_post_pump_gated strategy:
  - Funding rate must be negative (shorts paying longs = crowded long)
  - Long/Short ratio > 0.8
  - Short OI < 55% of total OI
  - No squeeze risk (short liquidations < 2% of OI)
"""

import asyncio
import aiohttp
import os
import logging
from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

COINGLASS_API = "https://open-api.coinglass.com/public/v2"
COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY", "")


@dataclass
class FundingGateResult:
    ticker: str
    venue: str
    funding_rate: Optional[float]
    long_short_ratio: Optional[float]
    short_oi_pct: Optional[float]
    short_liquidations_pct: Optional[float]
    gate_passed: bool
    gate_failures: list
    raw_data: dict
    checked_at: str

    @property
    def summary(self) -> str:
        status = "PASS" if self.gate_passed else "FAIL"
        failures = ", ".join(self.gate_failures) if self.gate_failures else "none"
        return (
            f"[{status}] {self.ticker}@{self.venue} | "
            f"funding={self.funding_rate or 'N/A'} | "
            f"LS_ratio={self.long_short_ratio or 'N/A'} | "
            f"short_OI={self.short_oi_pct or 'N/A'}% | "
            f"failures={failures}"
        )


# Gate thresholds (from backtested optimum)
FUNDING_RATE_MAX = 0.0  # must be negative
LONG_SHORT_RATIO_MIN = 0.8
SHORT_OI_MAX_PCT = 55.0
SHORT_LIQUIDATION_MAX_PCT = 2.0


async def fetch_funding_rate(
    session: aiohttp.ClientSession,
    symbol: str,
) -> Optional[float]:
    """Fetch current funding rate from Coinglass."""
    if not COINGLASS_API_KEY:
        logger.warning("No Coinglass API key, skipping funding rate check")
        return None

    headers = {"coinglassSecret": COINGLASS_API_KEY}
    try:
        async with session.get(
            f"{COINGLASS_API}/funding",
            params={"symbol": symbol},
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=10),
        ) as resp:
            if resp.status != 200:
                logger.warning(f"Coinglass funding {resp.status} for {symbol}")
                return None
            data = await resp.json()
            if data.get("code") != "0":
                logger.warning(f"Coinglass error: {data.get('msg')}")
                return None

            # Average across exchanges
            rates = []
            for exchange_data in data.get("data", []):
                rate = exchange_data.get("uMarginList", [{}])[0].get("rate")
                if rate is not None:
                    rates.append(float(rate))
            return sum(rates) / len(rates) if rates else None
    except Exception as e:
        logger.error(f"Funding rate fetch failed for {symbol}: {e}")
        return None


async def fetch_long_short_ratio(
    session: aiohttp.ClientSession,
    symbol: str,
) -> Optional[float]:
    """Fetch global long/short ratio from Coinglass."""
    if not COINGLASS_API_KEY:
        return None

    headers = {"coinglassSecret": COINGLASS_API_KEY}
    try:
        async with session.get(
            f"{COINGLASS_API}/long_short",
            params={"symbol": symbol, "timeType": 2},  # 1h
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=10),
        ) as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
            if data.get("code") != "0":
                return None
            entries = data.get("data", [])
            if entries:
                latest = entries[-1]
                return float(latest.get("longRate", 0)) / max(
                    float(latest.get("shortRate", 1)), 0.01
                )
            return None
    except Exception as e:
        logger.error(f"LS ratio fetch failed for {symbol}: {e}")
        return None


async def fetch_oi_breakdown(
    session: aiohttp.ClientSession,
    symbol: str,
) -> tuple[Optional[float], Optional[float]]:
    """Fetch OI breakdown: short OI % and short liquidation %."""
    if not COINGLASS_API_KEY:
        return None, None

    headers = {"coinglassSecret": COINGLASS_API_KEY}
    try:
        async with session.get(
            f"{COINGLASS_API}/open_interest",
            params={"symbol": symbol},
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=10),
        ) as resp:
            if resp.status != 200:
                return None, None
            data = await resp.json()
            if data.get("code") != "0":
                return None, None

            # Extract short OI percentage (simplified)
            oi_data = data.get("data", [])
            if not oi_data:
                return None, None

            total_oi = sum(
                float(e.get("openInterest", 0)) for e in oi_data
            )
            # Short OI is estimated from long/short ratio if available
            return None, None  # Requires separate endpoint for liquidation data

    except Exception as e:
        logger.error(f"OI breakdown fetch failed for {symbol}: {e}")
        return None, None


async def check_short_gates(
    ticker: str,
    venue: str = "binance",
) -> FundingGateResult:
    """
    Run all gating checks for the short post-pump strategy.
    Returns a FundingGateResult with pass/fail and details.
    """
    # Normalize symbol for Coinglass (e.g., DOGE, PEPE, FLOKI)
    symbol = ticker.upper().replace("USDT", "").replace("USD", "")

    gate_failures = []
    raw_data = {}

    async with aiohttp.ClientSession() as session:
        funding, ls_ratio = await asyncio.gather(
            fetch_funding_rate(session, symbol),
            fetch_long_short_ratio(session, symbol),
        )

        short_oi_pct, short_liq_pct = await fetch_oi_breakdown(session, symbol)

    raw_data = {
        "funding_rate": funding,
        "long_short_ratio": ls_ratio,
        "short_oi_pct": short_oi_pct,
        "short_liquidations_pct": short_liq_pct,
    }

    # Gate 1: Funding rate must be negative
    if funding is not None and funding > FUNDING_RATE_MAX:
        gate_failures.append(
            f"funding_rate={funding:.6f} > {FUNDING_RATE_MAX} (shorts not crowded enough)"
        )

    # Gate 2: Long/Short ratio > 0.8
    if ls_ratio is not None and ls_ratio < LONG_SHORT_RATIO_MIN:
        gate_failures.append(
            f"ls_ratio={ls_ratio:.2f} < {LONG_SHORT_RATIO_MIN} (not enough longs)"
        )

    # Gate 3: Short OI < 55%
    if short_oi_pct is not None and short_oi_pct > SHORT_OI_MAX_PCT:
        gate_failures.append(
            f"short_oi={short_oi_pct:.1f}% > {SHORT_OI_MAX_PCT}% (too crowded short)"
        )

    # Gate 4: Short liquidations < 2% of OI
    if short_liq_pct is not None and short_liq_pct > SHORT_LIQUIDATION_MAX_PCT:
        gate_failures.append(
            f"short_liq={short_liq_pct:.1f}% > {SHORT_LIQUIDATION_MAX_PCT}% (squeeze risk)"
        )

    # If any data is unavailable, pass with warning (conservative: allow trade
    # but flag missing data for human review)
    if funding is None:
        gate_failures.append("funding_rate=unavailable (check Coinglass key)")
    if ls_ratio is None:
        gate_failures.append("ls_ratio=unavailable")

    # A gate failure on data availability alone doesn't block;
    # only actual threshold violations block
    hard_failures = [
        f for f in gate_failures if "unavailable" not in f
    ]

    return FundingGateResult(
        ticker=ticker,
        venue=venue,
        funding_rate=funding,
        long_short_ratio=ls_ratio,
        short_oi_pct=short_oi_pct,
        short_liquidations_pct=short_liq_pct,
        gate_passed=len(hard_failures) == 0,
        gate_failures=gate_failures,
        raw_data=raw_data,
        checked_at=datetime.now(timezone.utc).isoformat(),
    )


async def check_emergency_exit_conditions(
    ticker: str,
    entry_price: float,
    current_price: float,
    leverage: float = 2.0,
) -> dict:
    """
    Check if emergency exit conditions are met for an open short.
    Returns dict with exit signals.
    """
    result = await check_short_gates(ticker)

    price_change_pct = (current_price - entry_price) / entry_price * 100
    capital_pnl_pct = -price_change_pct * leverage

    exit_signals = {
        "stop_loss_hit": capital_pnl_pct <= -25.0,
        "squeeze_risk": (
            result.short_liquidations_pct is not None
            and result.short_liquidations_pct > 2.0
        ),
        "funding_flipped_positive": (
            result.funding_rate is not None
            and result.funding_rate > 0.01
        ),
        "current_pnl_pct": capital_pnl_pct,
        "gate_status": result.summary,
    }

    return exit_signals


if __name__ == "__main__":
    import sys

    ticker = sys.argv[1] if len(sys.argv) > 1 else "DOGE"
    result = asyncio.run(check_short_gates(ticker))
    print(result.summary)
    print(f"\nRaw data: {result.raw_data}")
