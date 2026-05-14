"""
Signal Interpreter Agent — Core evaluation engine for DEX pump detection.

This agent evaluates incoming signals from multiple sources (TradingView Pine Script,
DexScreener, RSS, Google Trends, on-chain data) and produces actionable recommendations:
- EXECUTE: High conviction, take the trade
- WATCH: Interesting but needs confirmation
- IGNORE: False positive
- INVESTIGATE: Unusual pattern needs manual review

It routes signals to the appropriate strategy:
1. Long Pre-Event (accumulation detected, pump imminent)
2. Short Post-Pump Gated (pump happened, mean reversion expected)
3. Vol Selling (sell straddle on options pre-event)
"""

import json
import os
import logging
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum
from pathlib import Path

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────────────
# ENUMS & DATA STRUCTURES
# ──────────────────────────────────────────────────────────────

class Recommendation(str, Enum):
    EXECUTE = "EXECUTE"
    WATCH = "WATCH"
    IGNORE = "IGNORE"
    INVESTIGATE = "INVESTIGATE"

class Strategy(str, Enum):
    LONG_PRE_EVENT = "long_pre_event"
    SHORT_POST_PUMP = "short_post_pump_gated"
    VOL_SELLING = "vol_selling"
    SECOND_REACTION = "second_reaction"

class SignalSource(str, Enum):
    TRADINGVIEW = "tradingview"
    DEXSCREENER = "dexscreener"
    RSS_NEWS = "rss_news"
    GOOGLE_TRENDS = "google_trends"
    POLYMARKET = "polymarket"
    ONCHAIN = "onchain"
    TWITTER = "twitter"
    COINGLASS = "coinglass"

@dataclass
class Signal:
    """Incoming signal from any source."""
    source: SignalSource
    ticker: str
    signal_type: str  # e.g. "accumulation", "distribution", "trending", "mention"
    score: float  # 0-100 from source
    timestamp: datetime
    raw_payload: dict = field(default_factory=dict)
    chain: Optional[str] = None
    matched_personality: Optional[str] = None
    contract_address: Optional[str] = None

@dataclass
class ValidationResult:
    """Result from Couche 3 validation checks."""
    funding_rate_ok: bool = True
    oi_ratio_ok: bool = True
    concentration_ok: bool = True
    liquidation_cluster_safe: bool = True
    stablecoin_flow_ok: bool = True
    details: dict = field(default_factory=dict)

    @property
    def all_gates_passed(self) -> bool:
        return all([
            self.funding_rate_ok,
            self.oi_ratio_ok,
            self.concentration_ok,
            self.liquidation_cluster_safe,
        ])

    @property
    def gate_score(self) -> float:
        """0-100 score based on how many gates pass."""
        gates = [
            self.funding_rate_ok,
            self.oi_ratio_ok,
            self.concentration_ok,
            self.liquidation_cluster_safe,
            self.stablecoin_flow_ok,
        ]
        return (sum(gates) / len(gates)) * 100

@dataclass
class SignalAnalysis:
    """Output of the Signal Interpreter agent."""
    signal_id: Optional[int]
    ticker: str
    recommendation: Recommendation
    strategy: Optional[Strategy]
    conviction_score: int  # 0-100
    risk_factors: list
    similar_events: list
    reasoning: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        d = asdict(self)
        d['recommendation'] = self.recommendation.value
        d['strategy'] = self.strategy.value if self.strategy else None
        d['timestamp'] = self.timestamp.isoformat()
        return d

    def to_telegram_message(self) -> str:
        emoji = {
            Recommendation.EXECUTE: "🟢",
            Recommendation.WATCH: "🟡",
            Recommendation.IGNORE: "⚪",
            Recommendation.INVESTIGATE: "🔵",
        }
        return (
            f"{emoji.get(self.recommendation, '❓')} *{self.recommendation.value}* — {self.ticker}\n"
            f"Strategy: {self.strategy.value if self.strategy else 'none'}\n"
            f"Conviction: {self.conviction_score}/100\n\n"
            f"_{self.reasoning[:300]}_\n\n"
            f"Risks: {', '.join(self.risk_factors[:3])}"
        )


# ──────────────────────────────────────────────────────────────
# HISTORICAL CONTEXT
# ──────────────────────────────────────────────────────────────

class HistoricalContext:
    """Loads and queries the historical events dataset for pattern matching."""

    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            data_path = str(Path(__file__).parent.parent / "data" / "historical_events.json")
        with open(data_path) as f:
            self._data = json.load(f)
        self.events = self._data["events"]
        self.profiles = self._data["personality_profiles"]
        self.strategy_params = self._data["strategy_parameters"]

    def find_similar_events(self, ticker: str, personality: Optional[str] = None,
                            pump_pct_range: tuple = None) -> list:
        """Find historically similar events for comparison."""
        matches = []
        for ev in self.events:
            score = 0
            if ev["ticker"].upper() == ticker.upper():
                score += 40
            if personality and ev["personality"] == personality:
                score += 30
            if pump_pct_range and ev["pump_pct"] is not None:
                lo, hi = pump_pct_range
                if lo <= ev["pump_pct"] <= hi:
                    score += 20
            if ev.get("pre_signals"):
                pre_sig_count = sum(1 for v in ev["pre_signals"].values() if v)
                score += pre_sig_count * 5
            if score > 20:
                matches.append({
                    "event_id": ev["id"],
                    "date": ev["date_utc"],
                    "ticker": ev["ticker"],
                    "personality": ev["personality"],
                    "pump_pct": ev["pump_pct"],
                    "short_drawdown_7d_pct": ev.get("short_drawdown_7d_pct"),
                    "similarity_score": score,
                    "outcome": f"+{ev['pump_pct']}% pump" if ev["pump_pct"] and ev["pump_pct"] > 0 else "failed"
                })
        return sorted(matches, key=lambda x: x["similarity_score"], reverse=True)[:5]

    def get_personality_profile(self, personality: str) -> Optional[dict]:
        return self.profiles.get(personality)

    def get_strategy_params(self, strategy: str) -> Optional[dict]:
        return self.strategy_params.get(strategy)

    def get_short_hit_rate(self, personality: Optional[str] = None) -> dict:
        """Calculate historical short hit rate."""
        shortable = [e for e in self.events if e["shortable"]]
        if personality:
            shortable = [e for e in shortable if e["personality"] == personality]
        if not shortable:
            return {"hit_rate": 0, "sample_size": 0}
        winners = [e for e in shortable
                    if e.get("short_drawdown_7d_pct") and e["short_drawdown_7d_pct"] < -5]
        return {
            "hit_rate": len(winners) / len(shortable),
            "sample_size": len(shortable),
            "avg_drawdown_pct": sum(e["short_drawdown_7d_pct"] for e in shortable) / len(shortable),
        }


# ──────────────────────────────────────────────────────────────
# SIGNAL INTERPRETER — CORE AGENT
# ──────────────────────────────────────────────────────────────

class SignalInterpreter:
    """
    Core evaluation agent. Receives signals from multiple sources,
    cross-references with historical patterns, applies gating conditions,
    and produces actionable recommendations.
    """

    # Weights for composite scoring across sources
    SOURCE_WEIGHTS = {
        SignalSource.TRADINGVIEW: 0.30,
        SignalSource.DEXSCREENER: 0.15,
        SignalSource.ONCHAIN: 0.20,
        SignalSource.GOOGLE_TRENDS: 0.10,
        SignalSource.TWITTER: 0.10,
        SignalSource.POLYMARKET: 0.05,
        SignalSource.RSS_NEWS: 0.05,
        SignalSource.COINGLASS: 0.05,
    }

    # Tier classification for coins
    TIER_1_COINS = {"DOGE", "PEPE", "FLOKI", "SHIB", "BONK"}
    TIER_2_COINS = {"WIF", "BRETT", "MOG", "GIGA", "BABYDOGE"}

    def __init__(self, history: Optional[HistoricalContext] = None):
        self.history = history or HistoricalContext()
        self._recent_signals: list[Signal] = []
        self._signal_buffer_hours = 72  # keep signals for cross-referencing

    def ingest_signal(self, signal: Signal):
        """Add a signal to the recent buffer."""
        self._recent_signals.append(signal)
        # Prune old signals
        cutoff = datetime.now(timezone.utc) - timedelta(hours=self._signal_buffer_hours)
        self._recent_signals = [s for s in self._recent_signals if s.timestamp > cutoff]

    def get_convergence_score(self, ticker: str) -> dict:
        """
        Calculate how many independent sources confirm a signal on the same ticker.
        Convergence is the strongest indicator of a real event.
        """
        cutoff = datetime.now(timezone.utc) - timedelta(hours=72)
        relevant = [s for s in self._recent_signals
                    if s.ticker.upper() == ticker.upper() and s.timestamp > cutoff]

        sources_seen = set()
        weighted_score = 0
        max_score_by_source = {}

        for sig in relevant:
            sources_seen.add(sig.source)
            weight = self.SOURCE_WEIGHTS.get(sig.source, 0.05)
            existing = max_score_by_source.get(sig.source, 0)
            max_score_by_source[sig.source] = max(existing, sig.score * weight)

        weighted_score = sum(max_score_by_source.values())
        convergence_count = len(sources_seen)

        # Convergence bonus: more sources = exponentially more conviction
        if convergence_count >= 4:
            convergence_multiplier = 1.5
        elif convergence_count >= 3:
            convergence_multiplier = 1.3
        elif convergence_count >= 2:
            convergence_multiplier = 1.1
        else:
            convergence_multiplier = 1.0

        return {
            "composite_score": min(weighted_score * convergence_multiplier, 100),
            "convergence_count": convergence_count,
            "sources": list(sources_seen),
            "max_scores": {k.value: v for k, v in max_score_by_source.items()},
        }

    def classify_signal_type(self, signal: Signal) -> Strategy:
        """Determine which strategy this signal maps to."""
        sig_type = signal.signal_type.lower()

        # Distribution signals → short
        if sig_type in ("distribution", "shooting_star", "cvd_divergence_bearish",
                        "volume_decreasing_rallies"):
            return Strategy.SHORT_POST_PUMP

        # Accumulation signals → long
        if sig_type in ("accumulation", "wyckoff_spring", "wyckoff_sos",
                        "volume_burst", "cvd_divergence_bullish",
                        "asian_accumulation", "round_number_absorption"):
            return Strategy.LONG_PRE_EVENT

        # Trending / news → depends on timing
        if sig_type in ("trending", "mention", "news_mention"):
            return Strategy.LONG_PRE_EVENT

        # Second touch pattern
        if sig_type in ("second_touch", "retweet_same_coin"):
            return Strategy.SECOND_REACTION

        # Default
        return Strategy.LONG_PRE_EVENT

    def get_coin_tier(self, ticker: str) -> int:
        t = ticker.upper()
        if t in self.TIER_1_COINS:
            return 1
        if t in self.TIER_2_COINS:
            return 2
        return 3

    def evaluate(self, signal: Signal,
                 validation: Optional[ValidationResult] = None) -> SignalAnalysis:
        """
        Main evaluation function. Takes a signal + optional validation results,
        produces a recommendation.

        This is the brain of the agent.
        """
        self.ingest_signal(signal)
        convergence = self.get_convergence_score(signal.ticker)
        strategy = self.classify_signal_type(signal)
        tier = self.get_coin_tier(signal.ticker)
        similar = self.history.find_similar_events(
            signal.ticker, signal.matched_personality
        )
        risk_factors = []
        conviction = convergence["composite_score"]

        # ── Strategy-specific evaluation ──

        if strategy == Strategy.SHORT_POST_PUMP:
            conviction = self._evaluate_short(signal, convergence, validation,
                                               risk_factors)
        elif strategy == Strategy.LONG_PRE_EVENT:
            conviction = self._evaluate_long(signal, convergence, validation,
                                              risk_factors)
        elif strategy == Strategy.SECOND_REACTION:
            conviction = self._evaluate_second_reaction(signal, convergence,
                                                         risk_factors)

        # ── Tier adjustments ──
        if tier == 3:
            risk_factors.append("Tier 3 niche coin — low liquidity, high slippage risk")
            conviction *= 0.85  # haircut for illiquidity
        elif tier == 1:
            conviction *= 1.05  # slight bonus for liquid coins

        # ── Validation gate adjustments ──
        if validation:
            if not validation.all_gates_passed:
                conviction *= 0.6
                risk_factors.append(
                    f"Validation gates failed: "
                    f"funding={'OK' if validation.funding_rate_ok else 'FAIL'}, "
                    f"OI={'OK' if validation.oi_ratio_ok else 'FAIL'}, "
                    f"concentration={'OK' if validation.concentration_ok else 'FAIL'}, "
                    f"liquidation={'OK' if validation.liquidation_cluster_safe else 'FAIL'}"
                )
            else:
                conviction *= 1.1  # bonus for clean validation

        # ── Failed event detection ──
        if signal.score < 30 and convergence["convergence_count"] < 2:
            # This looks like DOGEfather 19/3/26 — false event, correctly filtered
            conviction = min(conviction, 25)
            risk_factors.append("Low signal score with no convergence — likely false positive (cf. DOGEfather Mar 2026)")

        # ── Cap conviction ──
        conviction = max(0, min(100, int(conviction)))

        # ── Determine recommendation ──
        if conviction >= 75:
            recommendation = Recommendation.EXECUTE
        elif conviction >= 50:
            recommendation = Recommendation.WATCH
        elif conviction >= 30:
            recommendation = Recommendation.INVESTIGATE
        else:
            recommendation = Recommendation.IGNORE

        # ── Build reasoning ──
        reasoning = self._build_reasoning(signal, convergence, strategy,
                                           conviction, similar, risk_factors)

        return SignalAnalysis(
            signal_id=None,
            ticker=signal.ticker,
            recommendation=recommendation,
            strategy=strategy if recommendation in (Recommendation.EXECUTE, Recommendation.WATCH) else None,
            conviction_score=conviction,
            risk_factors=risk_factors,
            similar_events=similar[:3],
            reasoning=reasoning,
        )

    def _evaluate_short(self, signal: Signal, convergence: dict,
                        validation: Optional[ValidationResult],
                        risk_factors: list) -> float:
        """Evaluate a short post-pump signal."""
        conviction = convergence["composite_score"]
        params = self.history.get_strategy_params("short_post_pump_gated")

        # Check gating conditions
        if validation:
            gates = params["gates"] if params else {}
            if not validation.funding_rate_ok:
                risk_factors.append("Funding rate positive — shorts are paying, market may have turned")
                conviction *= 0.4
            if not validation.oi_ratio_ok:
                risk_factors.append("Short OI ratio >55% — overcrowded, squeeze risk elevated")
                conviction *= 0.5
            if not validation.liquidation_cluster_safe:
                risk_factors.append("Liquidation cluster above current price — stop hunt risk")
                conviction *= 0.7

        # Historical hit rate context
        hist = self.history.get_short_hit_rate(signal.matched_personality)
        if hist["hit_rate"] > 0.7:
            conviction *= 1.1
        elif hist["hit_rate"] < 0.5:
            risk_factors.append(f"Low historical short hit rate: {hist['hit_rate']:.0%}")
            conviction *= 0.8

        # Second-touch risk
        profile = self.history.get_personality_profile(signal.matched_personality or "")
        if profile and profile.get("second_touch_probability", 0) > 0.5:
            risk_factors.append(
                f"High second-touch probability ({profile['second_touch_probability']:.0%}) "
                f"— personality may re-mention coin within {profile.get('second_touch_window_hours', 72)}h"
            )
            conviction *= 0.9

        return conviction

    def _evaluate_long(self, signal: Signal, convergence: dict,
                       validation: Optional[ValidationResult],
                       risk_factors: list) -> float:
        """Evaluate a long pre-event signal."""
        conviction = convergence["composite_score"]

        # Multi-source convergence is critical for long pre-event
        if convergence["convergence_count"] >= 3:
            conviction *= 1.3
        elif convergence["convergence_count"] == 1:
            risk_factors.append("Single-source signal — high false positive risk")
            conviction *= 0.6

        # Pre-signal pattern matching
        if signal.raw_payload.get("wallet_cluster_detected"):
            conviction += 15
        if signal.raw_payload.get("google_trends_spike"):
            conviction += 10
        if signal.raw_payload.get("dormant_token_wake"):
            conviction += 15

        # Slippage risk on niche coins
        if signal.chain in ("solana", "ethereum") and self.get_coin_tier(signal.ticker) == 3:
            risk_factors.append("DEX-only coin — slippage 5-20% expected at entry")
            conviction *= 0.85

        return conviction

    def _evaluate_second_reaction(self, signal: Signal, convergence: dict,
                                   risk_factors: list) -> float:
        """Evaluate second-touch / re-mention pattern."""
        conviction = convergence["composite_score"]

        # Check if first touch already happened
        first_touch_signals = [
            s for s in self._recent_signals
            if s.ticker.upper() == signal.ticker.upper()
            and s.timestamp < signal.timestamp
        ]
        if first_touch_signals:
            conviction *= 1.2  # confirmed first touch exists
        else:
            risk_factors.append("No first-touch signal found — second reaction unconfirmed")
            conviction *= 0.5

        # Historical second-touch rate
        profile = self.history.get_personality_profile(signal.matched_personality or "")
        if profile and profile.get("second_touch_probability", 0) > 0.5:
            conviction *= 1.15

        return conviction

    def _build_reasoning(self, signal: Signal, convergence: dict,
                         strategy: Strategy, conviction: int,
                         similar: list, risk_factors: list) -> str:
        """Build human-readable reasoning string."""
        parts = []

        parts.append(
            f"Signal from {signal.source.value} on {signal.ticker} "
            f"(type: {signal.signal_type}, raw score: {signal.score:.0f})."
        )

        parts.append(
            f"Convergence: {convergence['convergence_count']} sources "
            f"({', '.join(s.value for s in convergence['sources'])}), "
            f"composite: {convergence['composite_score']:.0f}/100."
        )

        parts.append(f"Routed to strategy: {strategy.value}.")

        if similar:
            best = similar[0]
            parts.append(
                f"Most similar historical event: {best['event_id']} "
                f"({best['ticker']}, {best['date'][:10]}, {best['outcome']})."
            )

        if risk_factors:
            parts.append(f"Key risks: {'; '.join(risk_factors[:3])}.")

        parts.append(f"Final conviction: {conviction}/100.")

        return " ".join(parts)


# ──────────────────────────────────────────────────────────────
# SELL WINDOW DETECTOR
# ──────────────────────────────────────────────────────────────

class SellWindowDetector:
    """
    Specialized module for detecting the optimal sell window during a pump.
    Critical requirement: don't miss the sell window AND be able to actually sell.

    Uses distribution detection signals from Pine Script + volume analysis
    to identify when insiders are exiting.
    """

    def __init__(self):
        self.position_entry_price: Optional[float] = None
        self.position_entry_time: Optional[datetime] = None
        self.peak_price: float = 0
        self.trailing_stop_pct: float = 0.20  # 20% trailing from peak

    def update_price(self, current_price: float, volume: float,
                     cvd_delta: float, timestamp: datetime) -> dict:
        """
        Called on each price update. Returns sell signals.

        Returns dict with:
        - should_sell: bool
        - reason: str
        - urgency: "immediate" | "soon" | "monitor"
        """
        if self.position_entry_price is None:
            return {"should_sell": False, "reason": "no_position", "urgency": "monitor"}

        # Track peak
        if current_price > self.peak_price:
            self.peak_price = current_price

        pnl_pct = (current_price - self.position_entry_price) / self.position_entry_price * 100
        drawdown_from_peak_pct = (current_price - self.peak_price) / self.peak_price * 100

        signals = []

        # Signal 1: Trailing stop from peak
        if drawdown_from_peak_pct < -self.trailing_stop_pct * 100:
            signals.append({
                "type": "trailing_stop",
                "urgency": "immediate",
                "reason": f"Price dropped {drawdown_from_peak_pct:.1f}% from peak ${self.peak_price:.6f}"
            })

        # Signal 2: CVD divergence (price up but selling pressure)
        if pnl_pct > 20 and cvd_delta < 0:
            signals.append({
                "type": "cvd_divergence",
                "urgency": "soon",
                "reason": f"Price up {pnl_pct:.1f}% but CVD negative — distribution detected"
            })

        # Signal 3: Time-based exit (memecoin pumps rarely last >4h for niche)
        if self.position_entry_time:
            hours_held = (timestamp - self.position_entry_time).total_seconds() / 3600
            if hours_held > 4 and pnl_pct > 50:
                signals.append({
                    "type": "time_exit",
                    "urgency": "soon",
                    "reason": f"Held {hours_held:.1f}h with +{pnl_pct:.0f}% gain — memecoin pump window closing"
                })

        # Signal 4: Echeloned take-profit
        if pnl_pct >= 100:
            signals.append({
                "type": "take_profit_full",
                "urgency": "immediate",
                "reason": f"+{pnl_pct:.0f}% — take full profit (2x achieved)"
            })
        elif pnl_pct >= 50:
            signals.append({
                "type": "take_profit_half",
                "urgency": "soon",
                "reason": f"+{pnl_pct:.0f}% — consider selling 50% position"
            })

        if signals:
            most_urgent = min(signals, key=lambda s: {"immediate": 0, "soon": 1, "monitor": 2}[s["urgency"]])
            return {
                "should_sell": most_urgent["urgency"] == "immediate",
                "reason": most_urgent["reason"],
                "urgency": most_urgent["urgency"],
                "all_signals": signals,
                "pnl_pct": pnl_pct,
                "drawdown_from_peak_pct": drawdown_from_peak_pct,
            }

        return {"should_sell": False, "reason": "no_exit_signal", "urgency": "monitor",
                "pnl_pct": pnl_pct, "drawdown_from_peak_pct": drawdown_from_peak_pct}

    def open_position(self, entry_price: float, entry_time: datetime):
        self.position_entry_price = entry_price
        self.position_entry_time = entry_time
        self.peak_price = entry_price

    def close_position(self):
        self.position_entry_price = None
        self.position_entry_time = None
        self.peak_price = 0


# ──────────────────────────────────────────────────────────────
# SHORT POSITION MANAGER
# ──────────────────────────────────────────────────────────────

class ShortPositionManager:
    """
    Manages short positions post-pump with gated conditions.
    Implements the optimized parameters from backtest:
    - Entry T+72h
    - Hold max 14 days
    - Stop-loss -25% capital
    - TP echeloned: 50% at +40%, 50% at +80%
    - Leverage x2
    - Exit on re-tweet / squeeze signal
    """

    def __init__(self, leverage: float = 2.0):
        self.leverage = leverage
        self.entry_price: Optional[float] = None
        self.entry_time: Optional[datetime] = None
        self.position_size_eur: float = 0
        self.half_closed: bool = False

    def open_short(self, price: float, size_eur: float, timestamp: datetime):
        self.entry_price = price
        self.entry_time = timestamp
        self.position_size_eur = size_eur
        self.half_closed = False

    def check_exit(self, current_price: float, timestamp: datetime,
                   personality_retweeted: bool = False,
                   volume_spike_3sigma: bool = False,
                   short_liquidations_high: bool = False) -> dict:
        """
        Check all exit conditions for the short position.
        Returns exit instructions.
        """
        if self.entry_price is None:
            return {"should_exit": False, "reason": "no_position"}

        price_change_pct = (current_price - self.entry_price) / self.entry_price * 100
        capital_change_pct = price_change_pct * self.leverage * -1  # short = inverse
        days_held = (timestamp - self.entry_time).total_seconds() / 86400

        # Emergency exits
        if personality_retweeted:
            return {
                "should_exit": True,
                "exit_pct": 100,
                "reason": "EMERGENCY: Personality re-tweeted coin — exit immediately",
                "urgency": "immediate",
                "capital_change_pct": capital_change_pct,
            }
        if volume_spike_3sigma:
            return {
                "should_exit": True,
                "exit_pct": 100,
                "reason": "Volume spike >3σ without news — possible squeeze, exit defensively",
                "urgency": "immediate",
                "capital_change_pct": capital_change_pct,
            }
        if short_liquidations_high:
            return {
                "should_exit": True,
                "exit_pct": 50,
                "reason": "Short liquidations >2% of OI — reduce position 50%",
                "urgency": "soon",
                "capital_change_pct": capital_change_pct,
            }

        # Stop-loss: -25% capital
        if capital_change_pct <= -25:
            return {
                "should_exit": True,
                "exit_pct": 100,
                "reason": f"Stop-loss hit: capital at {capital_change_pct:+.1f}%",
                "urgency": "immediate",
                "capital_change_pct": capital_change_pct,
            }

        # Take-profit 1: +40% capital, close 50%
        if capital_change_pct >= 40 and not self.half_closed:
            self.half_closed = True
            return {
                "should_exit": True,
                "exit_pct": 50,
                "reason": f"TP1 reached: capital at {capital_change_pct:+.1f}%, closing 50%",
                "urgency": "soon",
                "capital_change_pct": capital_change_pct,
            }

        # Take-profit 2: +80% capital, close remaining
        if capital_change_pct >= 80:
            return {
                "should_exit": True,
                "exit_pct": 100,
                "reason": f"TP2 reached: capital at {capital_change_pct:+.1f}%, closing all",
                "urgency": "immediate",
                "capital_change_pct": capital_change_pct,
            }

        # Time-based exit: max 14 days
        if days_held >= 14:
            return {
                "should_exit": True,
                "exit_pct": 100,
                "reason": f"Max holding period (14d) reached, capital at {capital_change_pct:+.1f}%",
                "urgency": "soon",
                "capital_change_pct": capital_change_pct,
            }

        return {
            "should_exit": False,
            "reason": "holding",
            "days_held": days_held,
            "capital_change_pct": capital_change_pct,
        }


# ──────────────────────────────────────────────────────────────
# CONVENIENCE: Run evaluation from CLI
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    # Demo: evaluate a sample signal
    interpreter = SignalInterpreter()

    sample_signal = Signal(
        source=SignalSource.TRADINGVIEW,
        ticker="GORK",
        signal_type="accumulation",
        score=78,
        timestamp=datetime.now(timezone.utc),
        chain="solana",
        matched_personality="musk",
    )

    # Simulate convergence by adding signals from multiple sources
    interpreter.ingest_signal(Signal(
        source=SignalSource.DEXSCREENER,
        ticker="GORK",
        signal_type="trending",
        score=65,
        timestamp=datetime.now(timezone.utc) - timedelta(hours=2),
        matched_personality="musk",
    ))
    interpreter.ingest_signal(Signal(
        source=SignalSource.GOOGLE_TRENDS,
        ticker="GORK",
        signal_type="spike",
        score=70,
        timestamp=datetime.now(timezone.utc) - timedelta(hours=6),
    ))

    validation = ValidationResult(
        funding_rate_ok=True,
        oi_ratio_ok=True,
        concentration_ok=True,
        liquidation_cluster_safe=True,
    )

    analysis = interpreter.evaluate(sample_signal, validation)

    print("=" * 60)
    print("SIGNAL ANALYSIS RESULT")
    print("=" * 60)
    print(json.dumps(analysis.to_dict(), indent=2, default=str))
    print()
    print("Telegram message:")
    print(analysis.to_telegram_message())
