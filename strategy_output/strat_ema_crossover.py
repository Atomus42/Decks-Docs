#!/usr/bin/env python3
"""
EMA Crossover Strategy Variants – BTC/USD Backtest
Tests 6 EMA crossover variants and saves results to JSON.
"""

import sys
import os
import json

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Make backtest_engine importable
# ---------------------------------------------------------------------------
STRATEGY_DIR = "/home/user/repo/strategy_output"
sys.path.insert(0, STRATEGY_DIR)
import backtest_engine

# ---------------------------------------------------------------------------
# Helper: compute EMA
# ---------------------------------------------------------------------------

def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()

# ---------------------------------------------------------------------------
# Signal generators
# ---------------------------------------------------------------------------

def signals_dual_ema(close: pd.Series, fast: int, slow: int) -> pd.Series:
    """1 when fast EMA > slow EMA, 0 otherwise."""
    ema_fast = ema(close, fast)
    ema_slow = ema(close, slow)
    sig = (ema_fast > ema_slow).astype(int)
    # Keep flat during warm-up period
    sig.iloc[:slow] = 0
    return sig


def signals_triple_ema(close: pd.Series, fast: int, mid: int, slow: int) -> pd.Series:
    """
    Triple EMA (8/21/55):
      Enter long when fast > mid > slow  (all aligned bullish).
      Exit when fast < mid.
    Uses a state machine so exits are sticky until next full alignment.
    """
    ema_fast = ema(close, fast)
    ema_mid  = ema(close, mid)
    ema_slow = ema(close, slow)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(slow, n):
        if not in_position:
            # Enter when all three aligned bullish
            if ema_fast.iloc[i] > ema_mid.iloc[i] > ema_slow.iloc[i]:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Stay in position until fast crosses below mid
            if ema_fast.iloc[i] < ema_mid.iloc[i]:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Define strategy variants
# ---------------------------------------------------------------------------
VARIANTS = [
    {
        "name": "EMA 9/21 (Fast Scalp)",
        "params": {"fast": 9, "slow": 21},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 12/26 (MACD-like)",
        "params": {"fast": 12, "slow": 26},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 21/55 (Medium Trend)",
        "params": {"fast": 21, "slow": 55},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 50/200 (Golden/Death Cross)",
        "params": {"fast": 50, "slow": 200},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 20/50 (Swing)",
        "params": {"fast": 20, "slow": 50},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "Triple EMA 8/21/55",
        "params": {"fast": 8, "mid": 21, "slow": 55},
        "signal_fn": lambda close, p: signals_triple_ema(close, p["fast"], p["mid"], p["slow"]),
    },
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 80)
    print("EMA CROSSOVER STRATEGY VARIANTS – BTC/USD BACKTEST")
    print("=" * 80)

    # Load data
    df = backtest_engine.load_data()
    close = df["Close"]
    print(f"\nData range : {df.index[0].date()} -> {df.index[-1].date()}  ({len(df)} bars)")
    print(f"Initial cap: ${backtest_engine.INITIAL_CAPITAL:,.0f}")
    print(f"Fee rate   : {backtest_engine.FEE_RATE * 100:.2f}%\n")

    results = []

    for v in VARIANTS:
        name = v["name"]
        params = v["params"]
        sig = v["signal_fn"](close, params)
        res = backtest_engine.run_backtest(df, sig, name, params)
        results.append(res)
        print(f"  [done] {name}")

    # ------------------------------------------------------------------
    # Save JSON
    # ------------------------------------------------------------------
    out_path = os.path.join(STRATEGY_DIR, "results_ema_crossover.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved -> {out_path}")

    # ------------------------------------------------------------------
    # Summary table
    # ------------------------------------------------------------------
    print("\n" + "=" * 120)
    print(f"{'Strategy':<32} {'Return%':>9} {'Ann.Ret%':>9} {'Sharpe':>7} {'MaxDD%':>8} "
          f"{'Trades':>7} {'WinR%':>7} {'PF':>7} {'AvgW%':>7} {'AvgL%':>7} {'vs B&H%':>9}")
    print("-" * 120)

    for r in results:
        print(f"{r['strategy']:<32} "
              f"{r['total_return_pct']:>9.2f} "
              f"{r['annualized_return_pct']:>9.2f} "
              f"{r['sharpe_ratio']:>7.2f} "
              f"{r['max_drawdown_pct']:>8.2f} "
              f"{r['num_trades']:>7d} "
              f"{r['win_rate_pct']:>7.2f} "
              f"{r['profit_factor']:>7.2f} "
              f"{r['avg_win_pct']:>7.2f} "
              f"{r['avg_loss_pct']:>7.2f} "
              f"{r['excess_vs_buyhold_pct']:>9.2f}")

    print("-" * 120)
    print(f"{'Buy & Hold (benchmark)':<32} {results[0]['buy_hold_return_pct']:>9.2f}")
    print("=" * 120)

    # Best variant by Sharpe
    best = max(results, key=lambda x: x["sharpe_ratio"])
    print(f"\nBest by Sharpe ratio: {best['strategy']}  (Sharpe={best['sharpe_ratio']:.2f}, "
          f"Return={best['total_return_pct']:.2f}%, MaxDD={best['max_drawdown_pct']:.2f}%)")


if __name__ == "__main__":
    main()
