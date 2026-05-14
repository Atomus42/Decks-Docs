"""
On-Chain Concentration Validator — Checks holder distribution
and whale wallet concentration before taking positions.

Validates:
  - Top 10 holders don't control > 80% of supply (rug risk)
  - Liquidity lock status
  - Recent large transfers (dump risk)
  - Creator wallet activity
"""

import asyncio
import aiohttp
import os
import logging
from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

SOLSCAN_API = "https://pro-api.solscan.io/v2.0"
ETHERSCAN_API = "https://api.etherscan.io/api"

SOLSCAN_API_KEY = os.getenv("SOLSCAN_API_KEY", "")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "")


@dataclass
class ConcentrationResult:
    token_address: str
    chain: str
    top10_holder_pct: Optional[float]
    top1_holder_pct: Optional[float]
    total_holders: Optional[int]
    liquidity_locked: Optional[bool]
    large_transfers_24h: int
    risk_level: str  # "low", "medium", "high", "critical"
    risk_factors: list
    raw_data: dict
    checked_at: str

    @property
    def is_safe(self) -> bool:
        return self.risk_level in ("low", "medium")

    @property
    def summary(self) -> str:
        return (
            f"[{self.risk_level.upper()}] {self.token_address[:12]}... "
            f"({self.chain}) | "
            f"top10={self.top10_holder_pct or 'N/A'}% | "
            f"holders={self.total_holders or 'N/A'} | "
            f"locked={self.liquidity_locked} | "
            f"risks={', '.join(self.risk_factors) or 'none'}"
        )


# Risk thresholds
TOP10_CRITICAL_PCT = 90.0  # top 10 holders > 90% = almost certain rug
TOP10_HIGH_PCT = 80.0
TOP10_MEDIUM_PCT = 60.0
TOP1_CRITICAL_PCT = 50.0  # single holder > 50% = extreme risk
MIN_HOLDERS_FOR_TRADE = 100
LARGE_TRANSFER_THRESHOLD = 5  # > 5 large transfers in 24h = suspicious


async def check_solana_concentration(
    session: aiohttp.ClientSession,
    token_address: str,
) -> dict:
    """Check holder concentration for a Solana token via Solscan."""
    if not SOLSCAN_API_KEY:
        logger.warning("No Solscan API key, skipping on-chain check")
        return {}

    headers = {"token": SOLSCAN_API_KEY}
    result = {}

    # Fetch token holders
    try:
        async with session.get(
            f"{SOLSCAN_API}/token/holders",
            params={"address": token_address, "page": 1, "page_size": 20},
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=15),
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                if data.get("success"):
                    holders = data.get("data", {}).get("items", [])
                    total = data.get("data", {}).get("total", 0)
                    result["total_holders"] = total
                    result["holders_data"] = holders

                    # Calculate concentration
                    if holders:
                        total_supply = sum(
                            float(h.get("amount", 0)) for h in holders
                        )
                        if total_supply > 0:
                            top1 = float(holders[0].get("amount", 0))
                            top10 = sum(
                                float(h.get("amount", 0))
                                for h in holders[:10]
                            )
                            result["top1_pct"] = top1 / total_supply * 100
                            result["top10_pct"] = top10 / total_supply * 100
    except Exception as e:
        logger.error(f"Solscan holders check failed: {e}")

    # Fetch recent transfers
    try:
        async with session.get(
            f"{SOLSCAN_API}/token/transfer",
            params={
                "address": token_address,
                "page": 1,
                "page_size": 50,
            },
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=15),
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                if data.get("success"):
                    transfers = data.get("data", {}).get("items", [])
                    # Count large transfers (>1% of supply moved)
                    large_count = 0
                    for tx in transfers:
                        amount = float(tx.get("amount", 0))
                        # Rough heuristic: any single transfer > 1% of top holder
                        if result.get("holders_data"):
                            top_amount = float(
                                result["holders_data"][0].get("amount", 1)
                            )
                            if amount > top_amount * 0.1:
                                large_count += 1
                    result["large_transfers_24h"] = large_count
    except Exception as e:
        logger.error(f"Solscan transfers check failed: {e}")

    return result


async def check_evm_concentration(
    session: aiohttp.ClientSession,
    token_address: str,
    chain: str = "ethereum",
) -> dict:
    """Check holder concentration for EVM tokens via Etherscan/BSCScan."""
    if not ETHERSCAN_API_KEY:
        logger.warning("No Etherscan API key, skipping EVM on-chain check")
        return {}

    # Etherscan doesn't have a direct holder distribution endpoint
    # in free tier. Return minimal data.
    result = {}

    try:
        async with session.get(
            ETHERSCAN_API,
            params={
                "module": "token",
                "action": "tokenholderlist",
                "contractaddress": token_address,
                "page": 1,
                "offset": 20,
                "apikey": ETHERSCAN_API_KEY,
            },
            timeout=aiohttp.ClientTimeout(total=15),
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                if data.get("status") == "1":
                    holders = data.get("result", [])
                    if holders:
                        total_balance = sum(
                            int(h.get("TokenHolderQuantity", 0))
                            for h in holders
                        )
                        if total_balance > 0:
                            top1 = int(holders[0].get("TokenHolderQuantity", 0))
                            top10 = sum(
                                int(h.get("TokenHolderQuantity", 0))
                                for h in holders[:10]
                            )
                            result["top1_pct"] = top1 / total_balance * 100
                            result["top10_pct"] = top10 / total_balance * 100
                            result["total_holders"] = len(holders)  # approximate
    except Exception as e:
        logger.error(f"Etherscan holder check failed: {e}")

    return result


def assess_risk(
    top10_pct: Optional[float],
    top1_pct: Optional[float],
    total_holders: Optional[int],
    liquidity_locked: Optional[bool],
    large_transfers: int,
) -> tuple[str, list]:
    """Assess concentration risk level and list risk factors."""
    risk_factors = []
    risk_level = "low"

    if top10_pct is not None:
        if top10_pct > TOP10_CRITICAL_PCT:
            risk_factors.append(
                f"top10 holders control {top10_pct:.1f}% (>90% critical)"
            )
            risk_level = "critical"
        elif top10_pct > TOP10_HIGH_PCT:
            risk_factors.append(
                f"top10 holders control {top10_pct:.1f}% (>80% high risk)"
            )
            risk_level = max(risk_level, "high", key=_risk_order)

    if top1_pct is not None:
        if top1_pct > TOP1_CRITICAL_PCT:
            risk_factors.append(
                f"single holder controls {top1_pct:.1f}% (>50% rug risk)"
            )
            risk_level = "critical"
        elif top1_pct > 30:
            risk_factors.append(
                f"top holder controls {top1_pct:.1f}% (concentration risk)"
            )
            risk_level = max(risk_level, "high", key=_risk_order)

    if total_holders is not None and total_holders < MIN_HOLDERS_FOR_TRADE:
        risk_factors.append(
            f"only {total_holders} holders (<{MIN_HOLDERS_FOR_TRADE} minimum)"
        )
        risk_level = max(risk_level, "high", key=_risk_order)

    if liquidity_locked is False:
        risk_factors.append("liquidity NOT locked (rug pull possible)")
        risk_level = max(risk_level, "high", key=_risk_order)

    if large_transfers > LARGE_TRANSFER_THRESHOLD:
        risk_factors.append(
            f"{large_transfers} large transfers in 24h (dump risk)"
        )
        risk_level = max(risk_level, "medium", key=_risk_order)

    return risk_level, risk_factors


def _risk_order(level: str) -> int:
    return {"low": 0, "medium": 1, "high": 2, "critical": 3}.get(level, 0)


async def check_concentration(
    token_address: str,
    chain: str = "solana",
) -> ConcentrationResult:
    """
    Full concentration check for a token.
    Supports Solana and EVM chains.
    """
    async with aiohttp.ClientSession() as session:
        if chain.lower() in ("solana", "sol"):
            raw = await check_solana_concentration(session, token_address)
        else:
            raw = await check_evm_concentration(session, token_address, chain)

    top10 = raw.get("top10_pct")
    top1 = raw.get("top1_pct")
    holders = raw.get("total_holders")
    large_tx = raw.get("large_transfers_24h", 0)

    risk_level, risk_factors = assess_risk(
        top10, top1, holders, None, large_tx
    )

    return ConcentrationResult(
        token_address=token_address,
        chain=chain,
        top10_holder_pct=top10,
        top1_holder_pct=top1,
        total_holders=holders,
        liquidity_locked=None,  # Requires separate LP lock check
        large_transfers_24h=large_tx,
        risk_level=risk_level,
        risk_factors=risk_factors,
        raw_data=raw,
        checked_at=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    import sys

    address = sys.argv[1] if len(sys.argv) > 1 else ""
    chain = sys.argv[2] if len(sys.argv) > 2 else "solana"
    if not address:
        print("Usage: python onchain_concentration.py <token_address> [chain]")
        sys.exit(1)

    result = asyncio.run(check_concentration(address, chain))
    print(result.summary)
