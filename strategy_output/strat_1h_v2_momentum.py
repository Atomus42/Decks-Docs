"""
1H BTC/USD Momentum Strategy Variants — V2 Engine
Designed for MAX RETURNS with fewer trades (hold days/weeks).
Tests 8 momentum-based strategies.
"""
import sys
sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine_1h_v2 as backtest_engine

import numpy as np
import pandas as pd
import json

OUTPUT_PATH = "/home/user/repo/strategy_output/results_1h_v2_momentum.json"


def compute_atr(df, period):
    """Average True Range."""
    high = df["High"]
    low = df["Low"]
    close = df["Close"]
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(period).mean()


def compute_supertrend(df, atr_period, multiplier):
    """
    Classic Supertrend indicator.
    Returns a signal series: 1 = uptrend (long), 0 = downtrend (flat).
    """
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    atr = compute_atr(df, atr_period)
    hl2 = (high + low) / 2

    upper_band = hl2 + multiplier * atr
    lower_band = hl2 - multiplier * atr

    n = len(df)
    final_upper = upper_band.copy()
    final_lower = lower_band.copy()
    supertrend = pd.Series(np.nan, index=df.index)
    direction = pd.Series(1, index=df.index)  # 1 = up, -1 = down

    for i in range(1, n):
        # Ratchet lower band up (support)
        if lower_band.iloc[i] > final_lower.iloc[i - 1] or close.iloc[i - 1] < final_lower.iloc[i - 1]:
            final_lower.iloc[i] = lower_band.iloc[i]
        else:
            final_lower.iloc[i] = final_lower.iloc[i - 1]

        # Ratchet upper band down (resistance)
        if upper_band.iloc[i] < final_upper.iloc[i - 1] or close.iloc[i - 1] > final_upper.iloc[i - 1]:
            final_upper.iloc[i] = upper_band.iloc[i]
        else:
            final_upper.iloc[i] = final_upper.iloc[i - 1]

        # Direction logic
        if direction.iloc[i - 1] == 1:
            if close.iloc[i] < final_lower.iloc[i]:
                direction.iloc[i] = -1
            else:
                direction.iloc[i] = 1
        else:
            if close.iloc[i] > final_upper.iloc[i]:
                direction.iloc[i] = 1
            else:
                direction.iloc[i] = -1

    signals = (direction == 1).astype(int)
    return signals


def donchian_strategy(df, entry_period, exit_period):
    """
    Donchian breakout: buy when close > highest high over entry_period,
    sell when close < lowest low over exit_period.
    """
    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    upper_channel = high.rolling(entry_period).max()
    lower_channel = low.rolling(exit_period).min()

    signals = pd.Series(0, index=df.index)
    in_position = False

    for i in range(max(entry_period, exit_period), len(df)):
        if not in_position:
            if close.iloc[i] > upper_channel.iloc[i - 1]:
                in_position = True
                signals.iloc[i] = 1
            else:
                signals.iloc[i] = 0
        else:
            if close.iloc[i] < lower_channel.iloc[i - 1]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    return signals


def sma_trend_strategy(df, sma_period):
    """Long when close > SMA(period), flat when below."""
    close = df["Close"]
    sma = close.rolling(sma_period).mean()
    signals = (close > sma).astype(int)
    signals.iloc[:sma_period] = 0
    return signals


def momentum_roc_strategy(df, lookback, entry_threshold, exit_threshold):
    """
    ROC-based momentum: long when ROC(lookback) > entry_threshold,
    exit when ROC < exit_threshold.
    """
    close = df["Close"]
    roc = (close / close.shift(lookback) - 1) * 100  # percentage

    signals = pd.Series(0, index=df.index)
    in_position = False

    for i in range(lookback, len(df)):
        if not in_position:
            if roc.iloc[i] > entry_threshold:
                in_position = True
                signals.iloc[i] = 1
        else:
            if roc.iloc[i] < exit_threshold:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    return signals


def dual_momentum_strategy(df, short_lookback, long_lookback):
    """
    Dual momentum: long when close > close[short_lookback] AND close > close[long_lookback].
    Exit when close < close[short_lookback].
    """
    close = df["Close"]
    short_mom = close > close.shift(short_lookback)
    long_mom = close > close.shift(long_lookback)

    signals = pd.Series(0, index=df.index)
    in_position = False

    for i in range(long_lookback, len(df)):
        if not in_position:
            if short_mom.iloc[i] and long_mom.iloc[i]:
                in_position = True
                signals.iloc[i] = 1
        else:
            if not short_mom.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    return signals


def main():
    df = backtest_engine.load_data()
    print(f"Loaded {len(df)} rows of 1H BTC data")
    print(f"Date range: {df.index[0]} to {df.index[-1]}")
    print(f"Price range: ${df['Close'].min():,.0f} - ${df['Close'].max():,.0f}")
    print("=" * 90)

    results = []

    # (a) Donchian(168/72) — 1-week breakout / 3-day exit
    print("\n[1/8] Donchian(168/72) — 1-week breakout / 3-day exit ...")
    sig = donchian_strategy(df, 168, 72)
    r = backtest_engine.run_backtest(df, sig, "Donchian Breakout",
                                     {"entry_period": 168, "exit_period": 72})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # (b) Donchian(336/168) — 2-week breakout / 1-week exit
    print("[2/8] Donchian(336/168) — 2-week breakout / 1-week exit ...")
    sig = donchian_strategy(df, 336, 168)
    r = backtest_engine.run_backtest(df, sig, "Donchian Breakout Slow",
                                     {"entry_period": 336, "exit_period": 168})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # (c) Supertrend(50, 3.0)
    print("[3/8] Supertrend(50, 3.0) ...")
    sig = compute_supertrend(df, 50, 3.0)
    r = backtest_engine.run_backtest(df, sig, "Supertrend",
                                     {"atr_period": 50, "multiplier": 3.0})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # (d) Supertrend(100, 2.5)
    print("[4/8] Supertrend(100, 2.5) ...")
    sig = compute_supertrend(df, 100, 2.5)
    r = backtest_engine.run_backtest(df, sig, "Supertrend Slow",
                                     {"atr_period": 100, "multiplier": 2.5})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # (e) Price vs 200-bar SMA
    print("[5/8] Price vs SMA(200) ...")
    sig = sma_trend_strategy(df, 200)
    r = backtest_engine.run_backtest(df, sig, "SMA Trend",
                                     {"sma_period": 200})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # (f) Price vs 500-bar SMA
    print("[6/8] Price vs SMA(500) ...")
    sig = sma_trend_strategy(df, 500)
    r = backtest_engine.run_backtest(df, sig, "SMA Trend Slow",
                                     {"sma_period": 500})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # (g) Momentum score — ROC(168) with +2%/-2% thresholds
    print("[7/8] Momentum ROC(168) — entry >2%, exit <-2% ...")
    sig = momentum_roc_strategy(df, 168, 2.0, -2.0)
    r = backtest_engine.run_backtest(df, sig, "Momentum ROC",
                                     {"lookback": 168, "entry_pct": 2.0, "exit_pct": -2.0})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # (h) Dual momentum — close > close[168] AND close > close[504]
    print("[8/8] Dual Momentum(168/504) ...")
    sig = dual_momentum_strategy(df, 168, 504)
    r = backtest_engine.run_backtest(df, sig, "Dual Momentum",
                                     {"short_lookback": 168, "long_lookback": 504})
    results.append(r)
    print(f"  Return: {r['total_return_pct']:+.2f}% | Trades: {r['num_trades']} | "
          f"Sharpe: {r['sharpe_ratio']:.2f} | MaxDD: {r['max_drawdown_pct']:.2f}%")

    # Save results
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Print ranked summary
    print("\n" + "=" * 90)
    print("MOMENTUM STRATEGY RANKINGS — SORTED BY TOTAL RETURN")
    print("=" * 90)
    ranked = sorted(results, key=lambda x: x["total_return_pct"], reverse=True)
    print(f"{'Rank':<5} {'Strategy':<25} {'Return%':>10} {'Ann.Ret%':>10} {'Sharpe':>8} "
          f"{'MaxDD%':>9} {'Trades':>7} {'WinR%':>7} {'PF':>7} {'vs B&H':>9}")
    print("-" * 90)
    for i, r in enumerate(ranked, 1):
        print(f"{i:<5} {r['strategy']:<25} {r['total_return_pct']:>+10.2f} "
              f"{r['annualized_return_pct']:>+10.2f} {r['sharpe_ratio']:>8.2f} "
              f"{r['max_drawdown_pct']:>9.2f} {r['num_trades']:>7} "
              f"{r['win_rate_pct']:>7.1f} {r['profit_factor']:>7.2f} "
              f"{r['excess_vs_buyhold_pct']:>+9.2f}")

    print(f"\nBuy & Hold return: {results[0]['buy_hold_return_pct']:+.2f}%")
    best = ranked[0]
    print(f"BEST: {best['strategy']} with {best['total_return_pct']:+.2f}% return, "
          f"{best['num_trades']} trades, Sharpe {best['sharpe_ratio']:.2f}")


if __name__ == "__main__":
    main()
