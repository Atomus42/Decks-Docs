#!/usr/bin/env python3
"""
EMA Crossover Strategy Variants – Optimized for 1H BTC/USD Data
Tests 8 EMA crossover variants with periods adjusted for hourly bars.
"""

import sys
import os
import json

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Make backtest_engine_1h importable
# ---------------------------------------------------------------------------
STRATEGY_DIR = "/home/user/repo/strategy_output"
sys.path.insert(0, STRATEGY_DIR)
import backtest_engine_1h as backtest_engine

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
    Triple EMA (5/13/34 on 1H):
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


def signals_ema_slope_filter(close: pd.Series, fast: int, slow: int, slope_bars: int) -> pd.Series:
    """
    EMA 8/21 with slope filter:
      Enter long when fast EMA > slow EMA AND slow EMA is rising
      (slow EMA > slow EMA shifted by slope_bars).
      Exit when fast EMA < slow EMA.
    """
    ema_fast = ema(close, fast)
    ema_slow = ema(close, slow)

    crossover = (ema_fast > ema_slow).astype(int)
    slope_ok = (ema_slow > ema_slow.shift(slope_bars)).astype(int)

    # State machine: enter only when crossover AND slope are both true,
    # exit when crossover fails
    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False
    warmup = max(slow, slope_bars)

    for i in range(warmup, n):
        if not in_position:
            if crossover.iloc[i] == 1 and slope_ok.iloc[i] == 1:
                in_position = True
                sig.iloc[i] = 1
        else:
            if crossover.iloc[i] == 0:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Define strategy variants (periods adjusted for 1H timeframe)
# ---------------------------------------------------------------------------
VARIANTS = [
    {
        "name": "EMA 9/21 (Ultra Fast ~1d)",
        "params": {"fast": 9, "slow": 21},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 12/26 (Classic Intraday)",
        "params": {"fast": 12, "slow": 26},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 21/55 (Multi-Day Swing)",
        "params": {"fast": 21, "slow": 55},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 50/100 (Medium Trend)",
        "params": {"fast": 50, "slow": 100},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "EMA 50/200 (Slow Trend 1H)",
        "params": {"fast": 50, "slow": 200},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
    {
        "name": "Triple EMA 5/13/34 (Fast 1H)",
        "params": {"fast": 5, "mid": 13, "slow": 34},
        "signal_fn": lambda close, p: signals_triple_ema(close, p["fast"], p["mid"], p["slow"]),
    },
    {
        "name": "EMA 8/21 + Slope Filter",
        "params": {"fast": 8, "slow": 21, "slope_bars": 5},
        "signal_fn": lambda close, p: signals_ema_slope_filter(
            close, p["fast"], p["slow"], p["slope_bars"]
        ),
    },
    {
        "name": "EMA 13/48 (Fibonacci-Based)",
        "params": {"fast": 13, "slow": 48},
        "signal_fn": lambda close, p: signals_dual_ema(close, p["fast"], p["slow"]),
    },
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 80)
    print("EMA CROSSOVER STRATEGY VARIANTS – 1H BTC/USD BACKTEST")
    print("=" * 80)

    # Load data
    df = backtest_engine.load_data()
    close = df["Close"]
    print(f"\nData range : {df.index[0]} -> {df.index[-1]}  ({len(df)} bars)")
    print(f"Timeframe  : 1H")
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
    out_path = os.path.join(STRATEGY_DIR, "results_1h_ema.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved -> {out_path}")

    # ------------------------------------------------------------------
    # Summary table
    # ------------------------------------------------------------------
    print("\n" + "=" * 130)
    print(f"{'Strategy':<32} {'Return%':>9} {'Ann.Ret%':>9} {'Sharpe':>7} {'MaxDD%':>8} "
          f"{'Trades':>7} {'WinR%':>7} {'PF':>7} {'AvgW%':>7} {'AvgL%':>7} {'FinalEq':>12} {'vs B&H%':>9}")
    print("-" * 130)

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
              f"{r['final_equity']:>12,.2f} "
              f"{r['excess_vs_buyhold_pct']:>9.2f}")

    print("-" * 130)
    print(f"{'Buy & Hold (benchmark)':<32} {results[0]['buy_hold_return_pct']:>9.2f}")
    print("=" * 130)

    # Best variant by Sharpe
    best_sharpe = max(results, key=lambda x: x["sharpe_ratio"])
    best_return = max(results, key=lambda x: x["total_return_pct"])
    best_dd     = max(results, key=lambda x: x["max_drawdown_pct"])  # least negative = best

    print(f"\n--- Top Picks ---")
    print(f"  Best Sharpe : {best_sharpe['strategy']}  "
          f"(Sharpe={best_sharpe['sharpe_ratio']:.2f}, Return={best_sharpe['total_return_pct']:.2f}%)")
    print(f"  Best Return : {best_return['strategy']}  "
          f"(Return={best_return['total_return_pct']:.2f}%, Sharpe={best_return['sharpe_ratio']:.2f})")
    print(f"  Lowest DD   : {best_dd['strategy']}  "
          f"(MaxDD={best_dd['max_drawdown_pct']:.2f}%, Return={best_dd['total_return_pct']:.2f}%)")


if __name__ == "__main__":
    main()
