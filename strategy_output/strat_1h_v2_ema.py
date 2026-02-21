"""
8 Aggressive EMA Crossover Strategies on 1H BTC/USD data.
Designed for SLOW signals — hold days/weeks, not hours.
"""

import sys
sys.path.insert(0, "/home/user/repo/strategy_output")

import json
import pandas as pd
import numpy as np
from backtest_engine_1h_v2 import load_data, run_backtest

OUTPUT_PATH = "/home/user/repo/strategy_output/results_1h_v2_ema.json"


def ema(series, span):
    return series.ewm(span=span, adjust=False).mean()


def strategy_a(df):
    """A) EMA 50/200 Golden Cross — Long when EMA(50) > EMA(200)"""
    ema50 = ema(df["Close"], 50)
    ema200 = ema(df["Close"], 200)
    signals = (ema50 > ema200).astype(int)
    params = {"fast_ema": 50, "slow_ema": 200}
    return signals, "EMA 50/200 Golden Cross", params


def strategy_b(df):
    """B) EMA 100/300 Ultra-Slow — Long when EMA(100) > EMA(300)"""
    ema100 = ema(df["Close"], 100)
    ema300 = ema(df["Close"], 300)
    signals = (ema100 > ema300).astype(int)
    params = {"fast_ema": 100, "slow_ema": 300}
    return signals, "EMA 100/300 Ultra-Slow", params


def strategy_c(df):
    """C) EMA 21/55 with 3-bar confirmation — Long when EMA(21) > EMA(55) for 3+ consecutive bars"""
    ema21 = ema(df["Close"], 21)
    ema55 = ema(df["Close"], 55)
    bullish = (ema21 > ema55).astype(int)
    # Require 3 consecutive bullish bars: rolling sum of last 3 must be 3
    confirmed = (bullish.rolling(window=3, min_periods=3).sum() == 3).astype(int)
    params = {"fast_ema": 21, "slow_ema": 55, "confirm_bars": 3}
    return confirmed, "EMA 21/55 + 3-Bar Confirm", params


def strategy_d(df):
    """D) EMA 50/200 + slope filter — Long when EMA(50) > EMA(200) AND EMA(200) is rising (current > 24 bars ago)"""
    ema50 = ema(df["Close"], 50)
    ema200 = ema(df["Close"], 200)
    cross = ema50 > ema200
    slope_rising = ema200 > ema200.shift(24)
    signals = (cross & slope_rising).astype(int)
    params = {"fast_ema": 50, "slow_ema": 200, "slope_lookback": 24}
    return signals, "EMA 50/200 + Slope Filter", params


def strategy_e(df):
    """E) Triple EMA (21/55/200) — Long when EMA(21) > EMA(55) > EMA(200)"""
    ema21 = ema(df["Close"], 21)
    ema55 = ema(df["Close"], 55)
    ema200 = ema(df["Close"], 200)
    signals = ((ema21 > ema55) & (ema55 > ema200)).astype(int)
    params = {"ema_fast": 21, "ema_mid": 55, "ema_slow": 200}
    return signals, "Triple EMA 21/55/200", params


def strategy_f(df):
    """F) EMA 50/200 + re-entry delay — Same as A but after exit, wait 48 bars before re-entry"""
    ema50 = ema(df["Close"], 50)
    ema200 = ema(df["Close"], 200)
    raw = (ema50 > ema200).astype(int)

    # Enforce 48-bar cooldown after each exit
    signals = pd.Series(0, index=df.index)
    in_position = False
    cooldown = 0

    for i in range(len(raw)):
        if cooldown > 0:
            cooldown -= 1
            signals.iloc[i] = 0
            continue

        if raw.iloc[i] == 1:
            if not in_position:
                in_position = True
            signals.iloc[i] = 1
        else:
            if in_position:
                in_position = False
                cooldown = 48  # start cooldown on exit
            signals.iloc[i] = 0

    params = {"fast_ema": 50, "slow_ema": 200, "reentry_delay_bars": 48}
    return signals, "EMA 50/200 + Re-entry Delay", params


def strategy_g(df):
    """G) EMA 100/400 Glacial — Long when EMA(100) > EMA(400)"""
    ema100 = ema(df["Close"], 100)
    ema400 = ema(df["Close"], 400)
    signals = (ema100 > ema400).astype(int)
    params = {"fast_ema": 100, "slow_ema": 400}
    return signals, "EMA 100/400 Glacial", params


def strategy_h(df):
    """H) EMA 50/200 + volume confirmation — Long when EMA(50) > EMA(200) AND volume > volume SMA(200)"""
    ema50 = ema(df["Close"], 50)
    ema200 = ema(df["Close"], 200)
    cross = ema50 > ema200
    vol_sma200 = df["Volume"].rolling(window=200, min_periods=1).mean()
    vol_confirm = df["Volume"] > vol_sma200
    signals = (cross & vol_confirm).astype(int)
    params = {"fast_ema": 50, "slow_ema": 200, "vol_sma": 200}
    return signals, "EMA 50/200 + Volume Confirm", params


def main():
    print("Loading 1H BTC/USD data...")
    df = load_data()
    print(f"  Loaded {len(df)} hourly bars: {df.index[0]} -> {df.index[-1]}\n")

    strategies = [
        strategy_a,
        strategy_b,
        strategy_c,
        strategy_d,
        strategy_e,
        strategy_f,
        strategy_g,
        strategy_h,
    ]

    all_results = []
    for strat_fn in strategies:
        signals, name, params = strat_fn(df)
        print(f"Running: {name} ...")
        result = run_backtest(df, signals, name, params)
        all_results.append(result)

        print(f"  Return: {result['total_return_pct']:+.2f}%  |  "
              f"Sharpe: {result['sharpe_ratio']:.2f}  |  "
              f"MaxDD: {result['max_drawdown_pct']:.2f}%  |  "
              f"Trades: {result['num_trades']}  |  "
              f"WinRate: {result['win_rate_pct']:.1f}%  |  "
              f"PF: {result['profit_factor']:.2f}  |  "
              f"vs B&H: {result['excess_vs_buyhold_pct']:+.2f}%")

    # Sort by total return descending
    all_results.sort(key=lambda x: x["total_return_pct"], reverse=True)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Summary table
    print("\n" + "=" * 110)
    print(f"{'Rank':<5} {'Strategy':<35} {'Return%':>10} {'AnnRet%':>10} {'Sharpe':>8} "
          f"{'MaxDD%':>9} {'Trades':>7} {'WinRate':>8} {'PF':>7} {'vsB&H%':>9}")
    print("=" * 110)
    for i, r in enumerate(all_results, 1):
        print(f"{i:<5} {r['strategy']:<35} {r['total_return_pct']:>+10.2f} "
              f"{r['annualized_return_pct']:>+10.2f} {r['sharpe_ratio']:>8.2f} "
              f"{r['max_drawdown_pct']:>9.2f} {r['num_trades']:>7} "
              f"{r['win_rate_pct']:>7.1f}% {r['profit_factor']:>7.2f} "
              f"{r['excess_vs_buyhold_pct']:>+9.2f}")
    print("=" * 110)
    print(f"Buy & Hold return: {all_results[0]['buy_hold_return_pct']:+.2f}%")


if __name__ == "__main__":
    main()
