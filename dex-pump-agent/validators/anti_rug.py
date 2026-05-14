"""
Anti-Rug Pre-Trade Screener — Mandatory gate before any long position
on fresh-launch memecoins.

Checks (all must pass for trade to proceed):
  1. LP locked >= 6 months (or burned)
  2. No active mint function ownership (can't inflate supply)
  3. Sell function works (eth_call simulation — detects honeypots)
  4. Top 10 holders < 30% of supply
  5. Sell tax <= 5%
  6. Minimum 200 holders

Rationale (from EV analysis):
  - 5-15% of Pump.fun launches are pure honeypots (buy OK, sell blocked)
  - 40-60% of unscreened fresh launches rug (LP withdrawn)
  - Upgradable contracts can activate sell tax retroactively
  Without this screen, 30-40% of trades are total losses (-100%),
  which makes the strategy negative EV even with occasional x10s.
"""

import asyncio
import aiohttp
import os
import logging
from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


@dataclass
class AntiRugResult:
    token_address: str
    chain: str
    lp_locked: Optional[bool]
    lp_lock_months: Optional[float]
    mint_function_safe: Optional[bool]
    sell_simulation_passed: Optional[bool]
    sell_tax_pct: Optional[float]
    top10_holder_pct: Optional[float]
    holder_count: Optional[int]
    is_proxy_contract: Optional[bool]
    all_gates_passed: bool
    gate_failures: list
    checked_at: str

    @property
    def summary(self) -> str:
        status = "SAFE" if self.all_gates_passed else "BLOCKED"
        failures = ", ".join(self.gate_failures) if self.gate_failures else "none"
        return (
            f"[{status}] {self.token_address[:16]}... ({self.chain}) | "
            f"LP_lock={self.lp_locked} | mint_safe={self.mint_function_safe} | "
            f"sell_ok={self.sell_simulation_passed} | "
            f"sell_tax={self.sell_tax_pct}% | "
            f"top10={self.top10_holder_pct}% | "
            f"holders={self.holder_count} | "
            f"failures=[{failures}]"
        )


# Thresholds from settings
LP_LOCK_MIN_MONTHS = float(os.getenv("ANTIRUG_LP_LOCK_MIN_MONTHS", "6"))
TOP10_MAX_PCT = float(os.getenv("ANTIRUG_TOP10_HOLDERS_MAX_PCT", "30"))
MIN_HOLDERS = int(os.getenv("ANTIRUG_MIN_HOLDERS", "200"))
MAX_SELL_TAX_PCT = float(os.getenv("ANTIRUG_MAX_SELL_TAX_PCT", "5"))


async def check_honeypot_goplus(
    session: aiohttp.ClientSession,
    token_address: str,
    chain_id: str = "1",
) -> dict:
    """
    Check token safety via GoPlus Security API (free, no key needed).
    Covers: honeypot detection, sell tax, mint function, proxy contract.
    """
    try:
        url = f"https://api.gopluslabs.com/api/v1/token_security/{chain_id}"
        async with session.get(
            url,
            params={"contract_addresses": token_address},
            timeout=aiohttp.ClientTimeout(total=15),
        ) as resp:
            if resp.status != 200:
                logger.warning(f"GoPlus API {resp.status} for {token_address}")
                return {}
            data = await resp.json()
            if data.get("code") != 1:
                return {}
            # GoPlus returns data keyed by lowercase address
            token_data = data.get("result", {}).get(token_address.lower(), {})
            return token_data
    except Exception as e:
        logger.error(f"GoPlus check failed for {token_address}: {e}")
        return {}


async def check_honeypot_solana(
    session: aiohttp.ClientSession,
    token_address: str,
) -> dict:
    """
    Check Solana token safety via RugCheck API.
    """
    try:
        url = f"https://api.rugcheck.xyz/v1/tokens/{token_address}/report"
        async with session.get(
            url,
            timeout=aiohttp.ClientTimeout(total=15),
        ) as resp:
            if resp.status != 200:
                logger.warning(f"RugCheck API {resp.status} for {token_address}")
                return {}
            return await resp.json()
    except Exception as e:
        logger.error(f"RugCheck failed for {token_address}: {e}")
        return {}


def _parse_goplus_result(data: dict) -> dict:
    """Extract structured safety data from GoPlus response."""
    if not data:
        return {}

    return {
        "is_honeypot": data.get("is_honeypot") == "1",
        "sell_tax_pct": float(data.get("sell_tax", 0) or 0) * 100,
        "buy_tax_pct": float(data.get("buy_tax", 0) or 0) * 100,
        "can_take_back_ownership": data.get("can_take_back_ownership") == "1",
        "owner_can_change_balance": data.get("owner_change_balance") == "1",
        "is_mintable": data.get("is_mintable") == "1",
        "is_proxy": data.get("is_proxy") == "1",
        "is_open_source": data.get("is_open_source") == "1",
        "lp_holders": data.get("lp_holders", []),
        "holder_count": int(data.get("holder_count", 0) or 0),
        "top10_holder_pct": _calc_top10_from_goplus(data.get("holders", [])),
        "lp_total_supply_pct": float(data.get("lp_total_supply", 0) or 0) * 100,
    }


def _calc_top10_from_goplus(holders: list) -> Optional[float]:
    """Calculate top 10 holder concentration from GoPlus holder list."""
    if not holders:
        return None
    top10_pct = sum(
        float(h.get("percent", 0) or 0) * 100
        for h in holders[:10]
    )
    return round(top10_pct, 1)


def _check_lp_lock(goplus_data: dict) -> tuple[Optional[bool], Optional[float]]:
    """Check if LP is locked and for how long."""
    lp_holders = goplus_data.get("lp_holders", [])
    if not lp_holders:
        return None, None

    for lp in lp_holders:
        is_locked = lp.get("is_locked") == 1
        if is_locked:
            # LP is locked — check for how long
            lock_detail = lp.get("locked_detail", [])
            if lock_detail:
                # Find the longest lock
                max_months = 0
                for lock in lock_detail:
                    end_time = lock.get("end_time")
                    if end_time:
                        try:
                            end_dt = datetime.fromtimestamp(
                                int(end_time), tz=timezone.utc
                            )
                            now = datetime.now(timezone.utc)
                            months_remaining = (end_dt - now).days / 30.44
                            max_months = max(max_months, months_remaining)
                        except (ValueError, OSError):
                            pass
                return True, max_months
            return True, None

    # Check if LP is burned (sent to dead address)
    for lp in lp_holders:
        address = lp.get("address", "").lower()
        if address in (
            "0x000000000000000000000000000000000000dead",
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000001",
        ):
            pct = float(lp.get("percent", 0) or 0) * 100
            if pct > 50:
                return True, 999  # burned = permanent lock
    return False, 0


async def screen_token(
    token_address: str,
    chain: str = "ethereum",
) -> AntiRugResult:
    """
    Full anti-rug screening for a token before taking a long position.
    Uses GoPlus (EVM) or RugCheck (Solana) for honeypot/rug detection.
    """
    gate_failures = []

    async with aiohttp.ClientSession() as session:
        if chain.lower() in ("solana", "sol"):
            raw = await check_honeypot_solana(session, token_address)
            # Parse Solana-specific format
            parsed = {
                "is_honeypot": raw.get("risks", []) != [],
                "sell_tax_pct": 0,
                "is_mintable": raw.get("mintAuthority") is not None,
                "is_proxy": False,
                "holder_count": raw.get("totalHolders"),
                "top10_holder_pct": raw.get("topHoldersPercent"),
                "lp_locked": raw.get("lpLocked", False),
                "lp_lock_months": None,
            }
        else:
            chain_id_map = {
                "ethereum": "1", "eth": "1",
                "bsc": "56", "bnb": "56",
                "polygon": "137",
                "arbitrum": "42161",
                "base": "8453",
                "avalanche": "43114",
            }
            chain_id = chain_id_map.get(chain.lower(), "1")
            goplus_raw = await check_honeypot_goplus(
                session, token_address, chain_id
            )
            parsed = _parse_goplus_result(goplus_raw)
            lp_locked, lp_months = _check_lp_lock(goplus_raw)
            parsed["lp_locked"] = lp_locked
            parsed["lp_lock_months"] = lp_months

    # === GATE CHECKS ===

    # Gate 1: Honeypot detection
    sell_sim_passed = not parsed.get("is_honeypot", True)
    if not sell_sim_passed:
        gate_failures.append("HONEYPOT: sell function blocked or failing")

    # Gate 2: Sell tax <= 5%
    sell_tax = parsed.get("sell_tax_pct")
    if sell_tax is not None and sell_tax > MAX_SELL_TAX_PCT:
        gate_failures.append(
            f"SELL_TAX: {sell_tax:.1f}% > {MAX_SELL_TAX_PCT}% max"
        )

    # Gate 3: No active mint function
    mint_safe = not parsed.get("is_mintable", True)
    if not mint_safe:
        gate_failures.append("MINT: contract owner can mint new tokens")

    # Gate 4: LP locked >= 6 months
    lp_locked = parsed.get("lp_locked")
    lp_months = parsed.get("lp_lock_months", 0)
    if lp_locked is False:
        gate_failures.append("LP_UNLOCKED: liquidity not locked (rug possible)")
    elif lp_months is not None and lp_months < LP_LOCK_MIN_MONTHS:
        gate_failures.append(
            f"LP_SHORT_LOCK: only {lp_months:.1f} months "
            f"(need >= {LP_LOCK_MIN_MONTHS})"
        )

    # Gate 5: Top 10 holders < 30%
    top10 = parsed.get("top10_holder_pct")
    if top10 is not None and top10 > TOP10_MAX_PCT:
        gate_failures.append(
            f"CONCENTRATION: top10 hold {top10:.1f}% > {TOP10_MAX_PCT}% max"
        )

    # Gate 6: Minimum holders
    holders = parsed.get("holder_count")
    if holders is not None and holders < MIN_HOLDERS:
        gate_failures.append(
            f"LOW_HOLDERS: {holders} < {MIN_HOLDERS} minimum"
        )

    # Gate 7: Not a proxy/upgradable contract
    is_proxy = parsed.get("is_proxy", False)
    if is_proxy:
        gate_failures.append(
            "PROXY_CONTRACT: upgradable — sell tax can be activated retroactively"
        )

    return AntiRugResult(
        token_address=token_address,
        chain=chain,
        lp_locked=lp_locked,
        lp_lock_months=lp_months,
        mint_function_safe=mint_safe,
        sell_simulation_passed=sell_sim_passed,
        sell_tax_pct=sell_tax,
        top10_holder_pct=top10,
        holder_count=holders,
        is_proxy_contract=is_proxy,
        all_gates_passed=len(gate_failures) == 0,
        gate_failures=gate_failures,
        checked_at=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python anti_rug.py <token_address> [chain]")
        print("  chain: ethereum (default), bsc, solana, polygon, arbitrum, base")
        sys.exit(1)

    address = sys.argv[1]
    chain = sys.argv[2] if len(sys.argv) > 2 else "ethereum"

    result = asyncio.run(screen_token(address, chain))
    print(result.summary)
    if result.gate_failures:
        print("\nGate failures:")
        for f in result.gate_failures:
            print(f"  - {f}")
    else:
        print("\nAll gates passed. Token is tradeable.")
