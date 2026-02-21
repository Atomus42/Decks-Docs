"""
MACD-based strategy variants optimized for 1H BTC/USD data.
Tests 8 MACD variants and saves results to JSON.
"""
import sys
import json
import numpy as np
import pandas as pd

# Add strategy_output to path so we can import the 1H backtest engine
sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine_1h as backtest_engine

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ema(series, span):
    """Compute exponential moving average."""
    return series.ewm(span=span, adjust=False).mean()


def compute_macd(close, fast=12, slow=26, signal=9):
    """Return macd_line, signal_line, histogram."""
    ema_fast = ema(close, fast)
    ema_slow = ema(close, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, signal)
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram


# ---------------------------------------------------------------------------
# Strategy 1: MACD(12,26,9) Classic Signal Crossover
#   Buy when MACD > signal, sell when MACD < signal
# ---------------------------------------------------------------------------

def strategy_macd_classic_crossover(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 12, 26, 9)

    signals = pd.Series(0, index=df.index)
    above = macd_line > signal_line

    position = 0
    for i in range(len(df)):
        if above.iloc[i]:
            position = 1
        else:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 2: MACD(12,26,9) Zero-Line
#   Buy when MACD > 0, sell when MACD < 0
# ---------------------------------------------------------------------------

def strategy_macd_zeroline(df):
    close = df["Close"]
    macd_line, _, _ = compute_macd(close, 12, 26, 9)

    signals = pd.Series(0, index=df.index)

    position = 0
    for i in range(len(df)):
        if macd_line.iloc[i] > 0:
            position = 1
        elif macd_line.iloc[i] < 0:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 3: MACD(12,26,9) Histogram Momentum
#   Buy when histogram > 0 AND increasing (hist > hist.shift(1))
#   Sell when histogram < 0
# ---------------------------------------------------------------------------

def strategy_macd_histogram_momentum(df):
    close = df["Close"]
    _, _, histogram = compute_macd(close, 12, 26, 9)

    hist_prev = histogram.shift(1)
    signals = pd.Series(0, index=df.index)

    position = 0
    for i in range(len(df)):
        h = histogram.iloc[i]
        h_prev = hist_prev.iloc[i] if i > 0 else 0.0
        if pd.isna(h_prev):
            h_prev = 0.0

        # Buy: histogram > 0 AND increasing
        if h > 0 and h > h_prev and position == 0:
            position = 1
        # Sell: histogram < 0
        elif h < 0 and position == 1:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 4: MACD(8,21,5) Fast Signal Crossover
#   Buy on signal crossover, sell on crossunder
# ---------------------------------------------------------------------------

def strategy_macd_fast(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 8, 21, 5)

    signals = pd.Series(0, index=df.index)
    above = macd_line > signal_line
    cross_above = above & (~above.shift(1).fillna(False))
    cross_below = (~above) & above.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        if cross_above.iloc[i]:
            position = 1
        elif cross_below.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 5: MACD(5,13,4) Scalp (Ultra Fast)
#   Buy on signal crossover, sell on crossunder
# ---------------------------------------------------------------------------

def strategy_macd_scalp(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 5, 13, 4)

    signals = pd.Series(0, index=df.index)
    above = macd_line > signal_line
    cross_above = above & (~above.shift(1).fillna(False))
    cross_below = (~above) & above.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        if cross_above.iloc[i]:
            position = 1
        elif cross_below.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 6: MACD(12,26,9) + EMA(200) Trend Filter
#   Only take MACD buy signals when price > EMA(200)
# ---------------------------------------------------------------------------

def strategy_macd_ema200_filter(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 12, 26, 9)
    ema200 = ema(close, 200)

    signals = pd.Series(0, index=df.index)
    above = macd_line > signal_line
    cross_above = above & (~above.shift(1).fillna(False))
    cross_below = (~above) & above.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        # Enter long only when price is above EMA(200) and MACD crosses above signal
        if cross_above.iloc[i] and close.iloc[i] > ema200.iloc[i]:
            position = 1
        elif cross_below.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 7: MACD(12,26,9) + Volume Confirmation
#   Buy when MACD > signal AND volume > volume.rolling(20).mean() * 1.5
#   Sell when MACD < signal
# ---------------------------------------------------------------------------

def strategy_macd_volume_confirm(df):
    close = df["Close"]
    volume = df["Volume"]
    macd_line, signal_line, _ = compute_macd(close, 12, 26, 9)

    vol_avg = volume.rolling(20).mean()
    vol_spike = volume > (vol_avg * 1.5)

    signals = pd.Series(0, index=df.index)
    above = macd_line > signal_line
    cross_above = above & (~above.shift(1).fillna(False))
    cross_below = (~above) & above.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        # Enter long when MACD crosses above signal AND volume spike
        if cross_above.iloc[i] and vol_spike.iloc[i]:
            position = 1
        elif cross_below.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 8: MACD(12,26,9) Histogram Divergence
#   Buy when histogram turns from negative to positive
#   (hist > 0 and hist.shift(1) < 0)
#   Sell when histogram turns negative
# ---------------------------------------------------------------------------

def strategy_macd_histogram_divergence(df):
    close = df["Close"]
    _, _, histogram = compute_macd(close, 12, 26, 9)

    hist_prev = histogram.shift(1)
    signals = pd.Series(0, index=df.index)

    position = 0
    for i in range(len(df)):
        h = histogram.iloc[i]
        h_prev = hist_prev.iloc[i] if i > 0 else np.nan
        if pd.isna(h_prev):
            signals.iloc[i] = 0
            continue

        # Buy: histogram turns from negative to positive
        if h > 0 and h_prev < 0 and position == 0:
            position = 1
        # Sell: histogram turns negative
        elif h < 0 and position == 1:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("MACD Strategy Variants (1H) - BTC/USD Backtest")
    print("=" * 78)

    df = backtest_engine.load_data()
    print(f"Data loaded: {len(df)} bars from {df.index[0]} to {df.index[-1]}")
    print(f"Timeframe: 1H | Initial capital: $100,000 | Fee rate: 0.15%")
    print()

    strategies = [
        {
            "name": "MACD(12,26,9) Classic Signal Crossover",
            "func": strategy_macd_classic_crossover,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "signal_crossover"},
        },
        {
            "name": "MACD(12,26,9) Zero-Line",
            "func": strategy_macd_zeroline,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "zero_line"},
        },
        {
            "name": "MACD(12,26,9) Histogram Momentum",
            "func": strategy_macd_histogram_momentum,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "histogram_momentum"},
        },
        {
            "name": "MACD(8,21,5) Fast Crossover",
            "func": strategy_macd_fast,
            "params": {"fast": 8, "slow": 21, "signal": 5, "type": "fast_crossover"},
        },
        {
            "name": "MACD(5,13,4) Scalp (Ultra Fast)",
            "func": strategy_macd_scalp,
            "params": {"fast": 5, "slow": 13, "signal": 4, "type": "scalp_crossover"},
        },
        {
            "name": "MACD(12,26,9) + EMA200 Trend Filter",
            "func": strategy_macd_ema200_filter,
            "params": {"fast": 12, "slow": 26, "signal": 9, "trend_filter": "EMA200"},
        },
        {
            "name": "MACD(12,26,9) + Volume Confirmation",
            "func": strategy_macd_volume_confirm,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "volume_confirm",
                       "vol_window": 20, "vol_mult": 1.5},
        },
        {
            "name": "MACD(12,26,9) Histogram Divergence",
            "func": strategy_macd_histogram_divergence,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "histogram_divergence"},
        },
    ]

    all_results = []

    for strat in strategies:
        print(f"Running: {strat['name']} ...")
        signals = strat["func"](df)
        result = backtest_engine.run_backtest(df, signals, strat["name"], strat["params"])
        all_results.append(result)
        print(f"  Return: {result['total_return_pct']:+.2f}%  |  "
              f"Sharpe: {result['sharpe_ratio']:.2f}  |  "
              f"MaxDD: {result['max_drawdown_pct']:.2f}%  |  "
              f"Trades: {result['num_trades']}  |  "
              f"Win Rate: {result['win_rate_pct']:.1f}%")

    # Save results to JSON
    output_path = "/home/user/repo/strategy_output/results_1h_macd.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # Print summary table
    print("\n" + "=" * 78)
    print("SUMMARY - MACD Strategy Variants (1H BTC/USD)")
    print("=" * 78)
    header = (f"{'Strategy':<44} {'Return%':>9} {'AnnRet%':>9} {'Sharpe':>7} "
              f"{'MaxDD%':>8} {'Trades':>7} {'WinR%':>7} {'PF':>7}")
    print(header)
    print("-" * len(header))

    for r in all_results:
        name = r["strategy"][:42]
        print(f"{name:<44} {r['total_return_pct']:>+8.2f}% {r['annualized_return_pct']:>+8.2f}% "
              f"{r['sharpe_ratio']:>7.2f} {r['max_drawdown_pct']:>7.2f}% "
              f"{r['num_trades']:>7d} {r['win_rate_pct']:>6.1f}% "
              f"{r['profit_factor']:>7.2f}")

    # Buy & hold reference
    bh = all_results[0]["buy_hold_return_pct"]
    print("-" * len(header))
    print(f"{'Buy & Hold (benchmark)':<44} {bh:>+8.2f}%")
    print()

    # Best by Sharpe
    best_sharpe = max(all_results, key=lambda x: x["sharpe_ratio"])
    print(f"Best risk-adjusted (Sharpe): {best_sharpe['strategy']}")
    print(f"  Sharpe={best_sharpe['sharpe_ratio']:.2f}, "
          f"Return={best_sharpe['total_return_pct']:+.2f}%, "
          f"MaxDD={best_sharpe['max_drawdown_pct']:.2f}%")

    # Best by total return
    best_return = max(all_results, key=lambda x: x["total_return_pct"])
    print(f"\nBest total return: {best_return['strategy']}")
    print(f"  Return={best_return['total_return_pct']:+.2f}%, "
          f"Sharpe={best_return['sharpe_ratio']:.2f}, "
          f"MaxDD={best_return['max_drawdown_pct']:.2f}%")

    # Best by profit factor
    best_pf = max(all_results, key=lambda x: x["profit_factor"])
    print(f"\nBest profit factor: {best_pf['strategy']}")
    print(f"  PF={best_pf['profit_factor']:.2f}, "
          f"Win Rate={best_pf['win_rate_pct']:.1f}%, "
          f"Trades={best_pf['num_trades']}")

    # Excess vs buy & hold
    print(f"\nStrategies beating buy & hold ({bh:+.2f}%):")
    beaters = [r for r in all_results if r["total_return_pct"] > bh]
    if beaters:
        for r in sorted(beaters, key=lambda x: x["excess_vs_buyhold_pct"], reverse=True):
            print(f"  {r['strategy']}: {r['total_return_pct']:+.2f}% "
                  f"(excess: {r['excess_vs_buyhold_pct']:+.2f}%)")
    else:
        print("  None")


if __name__ == "__main__":
    main()
