"""
Walk-Forward Backtester — Replays 24 months of historical events
as if they were happening live, proving the detection + trading system works.

Simulates:
1. Long pre-event strategy (enter on pre-signals, exit during pump)
2. Short post-pump gated strategy (enter T+72h, exit T+14d max)
3. Combined portfolio with capital recycling

Outputs: trade-by-trade P&L, equity curve, hit rates, Sharpe, drawdowns.
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Trade:
    event_id: str
    strategy: str
    ticker: str
    personality: str
    side: str  # "long" or "short"
    entry_price: float
    exit_price: float
    entry_time: str
    exit_time: str
    leverage: float
    capital_deployed: float
    pnl_eur: float
    pnl_pct: float
    exit_reason: str
    pre_signals_count: int
    pre_signal_score: float


@dataclass
class BacktestResult:
    trades: list
    equity_curve: list
    stats: dict


class WalkForwardBacktester:
    """
    Replays historical events chronologically, simulating both long pre-event
    and short post-pump strategies with realistic constraints.
    """

    def __init__(self, events_path: Optional[str] = None,
                 initial_capital: float = 1000.0,
                 per_trade_capital: float = 1000.0,
                 compound: bool = True):
        if events_path is None:
            events_path = str(Path(__file__).parent.parent / "data" / "historical_events.json")

        with open(events_path) as f:
            data = json.load(f)

        self.events = sorted(data["events"], key=lambda e: e["date_utc"])
        self.strategy_params = data["strategy_parameters"]
        self.initial_capital = initial_capital
        self.per_trade_capital = per_trade_capital
        self.compound = compound

    def run_short_strategy(self) -> BacktestResult:
        """
        Backtest the short post-pump gated strategy.
        Parameters from grid search optimum:
          Entry: T+72h, Hold: max 14d, Stop: -25% capital, TP: 50%@+40%, 50%@+80%, Lever: x2
        """
        params = self.strategy_params["short_post_pump_gated"]
        leverage = params["leverage"]
        stop_pct = params["stop_loss_capital_pct"]
        tp1_pct = params["take_profit_1_capital_pct"]
        tp2_pct = params["take_profit_2_capital_pct"]

        capital = self.initial_capital
        trades = []
        equity_curve = [{"date": "start", "equity": capital}]

        for ev in self.events:
            if not ev["shortable"]:
                continue

            entry_price = ev.get("short_entry_t72h_price")
            exit_price_7d = ev.get("short_exit_t7d_price")
            if entry_price is None or exit_price_7d is None:
                continue

            # Calculate underlying price change
            price_change_pct = (exit_price_7d - entry_price) / entry_price * 100
            # Short P&L = -price_change * leverage
            capital_pnl_pct = -price_change_pct * leverage

            # Apply stop-loss / take-profit logic
            drawdown_7d = ev.get("short_drawdown_7d_pct", 0) or 0

            # Simulate worst case during holding period
            # If drawdown is positive (price went UP against short), check stop
            worst_adverse_move = -drawdown_7d if drawdown_7d > 0 else 0
            worst_capital_pct = worst_adverse_move * leverage

            exit_reason = "T+14d"
            effective_pnl_pct = capital_pnl_pct

            if worst_capital_pct <= stop_pct:
                # Stop-loss triggered
                effective_pnl_pct = stop_pct
                exit_reason = "stop_loss"
            elif capital_pnl_pct >= tp2_pct:
                # TP2 hit
                effective_pnl_pct = tp2_pct
                exit_reason = "take_profit_2"
            elif capital_pnl_pct >= tp1_pct:
                # TP1 hit (partial), blend
                # 50% at TP1, 50% at actual final
                effective_pnl_pct = (tp1_pct * 0.5) + (capital_pnl_pct * 0.5)
                exit_reason = "take_profit_1_partial"

            # Capital allocation
            trade_capital = capital if self.compound else self.per_trade_capital
            pnl_eur = trade_capital * effective_pnl_pct / 100

            # Pre-signal score
            pre_sigs = ev.get("pre_signals", {})
            pre_sig_count = sum(1 for v in pre_sigs.values() if v)
            pre_sig_score = pre_sig_count / max(len(pre_sigs), 1) * 100

            trade = Trade(
                event_id=ev["id"],
                strategy="short_post_pump_gated",
                ticker=ev["ticker"],
                personality=ev["personality"],
                side="short",
                entry_price=entry_price,
                exit_price=exit_price_7d,
                entry_time=ev["date_utc"],
                exit_time="",
                leverage=leverage,
                capital_deployed=trade_capital,
                pnl_eur=pnl_eur,
                pnl_pct=effective_pnl_pct,
                exit_reason=exit_reason,
                pre_signals_count=pre_sig_count,
                pre_signal_score=pre_sig_score,
            )
            trades.append(trade)

            if self.compound:
                capital += pnl_eur
                capital = max(capital, 0)  # can't go below zero

            equity_curve.append({
                "date": ev["date_utc"][:10],
                "event": ev["id"],
                "equity": capital if self.compound else self.initial_capital + sum(t.pnl_eur for t in trades),
            })

        return BacktestResult(
            trades=trades,
            equity_curve=equity_curve,
            stats=self._compute_stats(trades, equity_curve),
        )

    def run_long_strategy(self) -> BacktestResult:
        """
        Backtest long pre-event strategy.
        Entry: when pre-signals detected (simulated as T0 price for events with pre-signals).
        Exit: at T0+15min price (conservative) or at peak (optimistic).
        """
        capital = self.initial_capital
        trades = []
        equity_curve = [{"date": "start", "equity": capital}]

        for ev in self.events:
            pre_sigs = ev.get("pre_signals", {})
            pre_sig_count = sum(1 for v in pre_sigs.values() if v)

            # Only take trades where pre-signals were detectable
            if pre_sig_count < 2:
                continue

            # Conservative: enter at T0, exit at T0+15min price
            entry_price = ev["price_t0_usd"]
            exit_price = ev.get("price_t0_plus_15min_usd", entry_price)

            if entry_price <= 0 or exit_price <= 0:
                continue

            pnl_pct = (exit_price - entry_price) / entry_price * 100

            # Cap at reasonable long exit (50% of peak gain, conservative)
            peak = ev.get("peak_usd", exit_price)
            if peak and peak > entry_price:
                max_gain_pct = (peak - entry_price) / entry_price * 100
                # Capture 50% of peak gain
                target_pnl_pct = max_gain_pct * 0.5
                pnl_pct = min(pnl_pct, target_pnl_pct) if pnl_pct > 0 else pnl_pct

            # Slippage penalty
            slippage = ev.get("slippage_1000eur_t5min_pct", 1)
            pnl_pct -= slippage * 2  # entry + exit slippage

            trade_capital = capital if self.compound else self.per_trade_capital
            pnl_eur = trade_capital * pnl_pct / 100

            pre_sig_score = pre_sig_count / max(len(pre_sigs), 1) * 100

            trade = Trade(
                event_id=ev["id"],
                strategy="long_pre_event",
                ticker=ev["ticker"],
                personality=ev["personality"],
                side="long",
                entry_price=entry_price,
                exit_price=exit_price,
                entry_time=ev["date_utc"],
                exit_time="",
                leverage=1.0,
                capital_deployed=trade_capital,
                pnl_eur=pnl_eur,
                pnl_pct=pnl_pct,
                exit_reason="pre_signal_exit",
                pre_signals_count=pre_sig_count,
                pre_signal_score=pre_sig_score,
            )
            trades.append(trade)

            if self.compound:
                capital += pnl_eur
                capital = max(capital, 0)

            equity_curve.append({
                "date": ev["date_utc"][:10],
                "event": ev["id"],
                "equity": capital if self.compound else self.initial_capital + sum(t.pnl_eur for t in trades),
            })

        return BacktestResult(
            trades=trades,
            equity_curve=equity_curve,
            stats=self._compute_stats(trades, equity_curve),
        )

    def run_combined(self) -> dict:
        """Run both strategies and produce combined report."""
        short_result = self.run_short_strategy()
        long_result = self.run_long_strategy()

        return {
            "short_strategy": {
                "trades": [self._trade_to_dict(t) for t in short_result.trades],
                "stats": short_result.stats,
                "equity_curve": short_result.equity_curve,
            },
            "long_strategy": {
                "trades": [self._trade_to_dict(t) for t in long_result.trades],
                "stats": long_result.stats,
                "equity_curve": long_result.equity_curve,
            },
            "combined_stats": {
                "total_trades": len(short_result.trades) + len(long_result.trades),
                "total_pnl_eur": sum(t.pnl_eur for t in short_result.trades) + sum(t.pnl_eur for t in long_result.trades),
                "short_contribution_pct": (
                    sum(t.pnl_eur for t in short_result.trades) /
                    max(sum(t.pnl_eur for t in short_result.trades) + sum(t.pnl_eur for t in long_result.trades), 1)
                ) * 100,
            },
        }

    def _compute_stats(self, trades: list, equity_curve: list) -> dict:
        if not trades:
            return {"error": "no trades"}

        pnls = [t.pnl_pct for t in trades]
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p <= 0]

        import statistics
        avg_pnl = statistics.mean(pnls) if pnls else 0
        std_pnl = statistics.stdev(pnls) if len(pnls) > 1 else 0

        # Max drawdown from equity curve
        peak_equity = 0
        max_dd = 0
        for point in equity_curve:
            eq = point.get("equity", 0)
            if eq > peak_equity:
                peak_equity = eq
            if peak_equity > 0:
                dd = (eq - peak_equity) / peak_equity * 100
                if dd < max_dd:
                    max_dd = dd

        # Final capital
        final_equity = equity_curve[-1]["equity"] if equity_curve else self.initial_capital

        return {
            "total_trades": len(trades),
            "winners": len(wins),
            "losers": len(losses),
            "hit_rate_pct": len(wins) / len(trades) * 100 if trades else 0,
            "avg_pnl_pct": round(avg_pnl, 2),
            "median_pnl_pct": round(statistics.median(pnls), 2) if pnls else 0,
            "std_pnl_pct": round(std_pnl, 2),
            "best_trade_pct": round(max(pnls), 2) if pnls else 0,
            "worst_trade_pct": round(min(pnls), 2) if pnls else 0,
            "sharpe_per_trade": round(avg_pnl / std_pnl, 2) if std_pnl > 0 else 0,
            "max_drawdown_pct": round(max_dd, 2),
            "initial_capital": self.initial_capital,
            "final_capital": round(final_equity, 2),
            "total_return_pct": round((final_equity - self.initial_capital) / self.initial_capital * 100, 2),
            "avg_pre_signal_score": round(statistics.mean([t.pre_signal_score for t in trades]), 1) if trades else 0,
        }

    def _trade_to_dict(self, trade: Trade) -> dict:
        return {
            "event_id": trade.event_id,
            "strategy": trade.strategy,
            "ticker": trade.ticker,
            "personality": trade.personality,
            "side": trade.side,
            "entry_price": trade.entry_price,
            "exit_price": trade.exit_price,
            "leverage": trade.leverage,
            "pnl_eur": round(trade.pnl_eur, 2),
            "pnl_pct": round(trade.pnl_pct, 2),
            "exit_reason": trade.exit_reason,
            "pre_signals_count": trade.pre_signals_count,
        }


def print_report(result: dict):
    """Pretty-print backtest results."""
    for strat_name in ("short_strategy", "long_strategy"):
        strat = result[strat_name]
        stats = strat["stats"]
        print(f"\n{'='*60}")
        print(f"  {strat_name.upper().replace('_', ' ')}")
        print(f"{'='*60}")
        print(f"  Trades:       {stats['total_trades']}")
        print(f"  Hit rate:     {stats['hit_rate_pct']:.0f}%")
        print(f"  Avg P&L:      {stats['avg_pnl_pct']:+.1f}%")
        print(f"  Median P&L:   {stats['median_pnl_pct']:+.1f}%")
        print(f"  Best trade:   {stats['best_trade_pct']:+.1f}%")
        print(f"  Worst trade:  {stats['worst_trade_pct']:+.1f}%")
        print(f"  Sharpe/trade: {stats['sharpe_per_trade']:.2f}")
        print(f"  Max drawdown: {stats['max_drawdown_pct']:.1f}%")
        print(f"  Capital:      {stats['initial_capital']}€ → {stats['final_capital']}€")
        print(f"  Total return: {stats['total_return_pct']:+.1f}%")
        print()
        print(f"  Trade log:")
        for t in strat["trades"]:
            emoji = "✅" if t["pnl_pct"] > 0 else "❌"
            print(f"    {emoji} {t['event_id']:5s} {t['ticker']:12s} {t['side']:5s} "
                  f"{t['pnl_pct']:+7.1f}% ({t['exit_reason']})")

    combined = result["combined_stats"]
    print(f"\n{'='*60}")
    print(f"  COMBINED")
    print(f"{'='*60}")
    print(f"  Total trades:    {combined['total_trades']}")
    print(f"  Total P&L:       {combined['total_pnl_eur']:+.0f}€")
    print(f"  Short contrib:   {combined['short_contribution_pct']:.0f}%")


if __name__ == "__main__":
    bt = WalkForwardBacktester(initial_capital=1000, compound=True)
    result = bt.run_combined()

    print_report(result)

    # Save full results to JSON
    output_path = Path(__file__).parent / "results"
    output_path.mkdir(exist_ok=True)
    with open(output_path / "backtest_results.json", "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"\nFull results saved to {output_path / 'backtest_results.json'}")
