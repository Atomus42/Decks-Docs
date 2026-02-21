"""
MACD-based strategy variants for BTC/USD backtesting.
Tests 6 MACD variants and saves results to JSON.
"""
import sys
import json
import numpy as np
import pandas as pd

# Add strategy_output to path so we can import backtest_engine
sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine

# ---------------------------------------------------------------------------
# Helper: EMA calculation
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
# Strategy 1: MACD(12,26,9) classic crossover
# ---------------------------------------------------------------------------

def strategy_macd_classic(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 12, 26, 9)

    # Buy when MACD crosses above signal, sell when crosses below
    signals = pd.Series(0, index=df.index)
    above = macd_line > signal_line
    cross_above = above & (~above.shift(1).fillna(False))
    cross_below = (~above) & above.shift(1).fillna(False)

    # Forward-fill: 1 from cross_above until cross_below
    position = 0
    for i in range(len(df)):
        if cross_above.iloc[i]:
            position = 1
        elif cross_below.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 2: MACD(12,26,9) zero-line crossover
# ---------------------------------------------------------------------------

def strategy_macd_zeroline(df):
    close = df["Close"]
    macd_line, _, _ = compute_macd(close, 12, 26, 9)

    signals = pd.Series(0, index=df.index)
    above_zero = macd_line > 0
    cross_above = above_zero & (~above_zero.shift(1).fillna(False))
    cross_below = (~above_zero) & above_zero.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        if cross_above.iloc[i]:
            position = 1
        elif cross_below.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 3: MACD(12,26,9) histogram reversal
# ---------------------------------------------------------------------------

def strategy_macd_histogram(df):
    close = df["Close"]
    _, _, histogram = compute_macd(close, 12, 26, 9)

    signals = pd.Series(0, index=df.index)
    hist_positive = histogram > 0
    turns_positive = hist_positive & (~hist_positive.shift(1).fillna(False))
    turns_negative = (~hist_positive) & hist_positive.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        if turns_positive.iloc[i]:
            position = 1
        elif turns_negative.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 4: MACD(8,21,5) fast crossover
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
# Strategy 5: MACD(12,26,9) + EMA(200) trend filter
# ---------------------------------------------------------------------------

def strategy_macd_trend_filter(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 12, 26, 9)
    ema200 = ema(close, 200)

    signals = pd.Series(0, index=df.index)
    above_signal = macd_line > signal_line
    cross_above = above_signal & (~above_signal.shift(1).fillna(False))
    cross_below = (~above_signal) & above_signal.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        # Only enter long when price is above EMA(200)
        if cross_above.iloc[i] and close.iloc[i] > ema200.iloc[i]:
            position = 1
        elif cross_below.iloc[i]:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Strategy 6: MACD(12,26,9) divergence proxy
# ---------------------------------------------------------------------------

def strategy_macd_divergence(df):
    close = df["Close"]
    macd_line, signal_line, histogram = compute_macd(close, 12, 26, 9)

    signals = pd.Series(0, index=df.index)

    # Divergence proxy: price makes lower low but histogram makes higher low
    # Condition: price < price[5] AND histogram > histogram[5] AND histogram < 0
    price_lower = close < close.shift(5)
    hist_higher = histogram > histogram.shift(5)
    hist_negative = histogram < 0

    buy_signal = price_lower & hist_higher & hist_negative

    # Sell when MACD crosses below signal
    above_signal = macd_line > signal_line
    sell_signal = (~above_signal) & above_signal.shift(1).fillna(False)

    position = 0
    for i in range(len(df)):
        if buy_signal.iloc[i] and position == 0:
            position = 1
        elif sell_signal.iloc[i] and position == 1:
            position = 0
        signals.iloc[i] = position

    return signals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("MACD Strategy Variants - BTC/USD Backtest")
    print("=" * 70)

    df = backtest_engine.load_data()
    print(f"Data loaded: {len(df)} rows from {df.index[0].date()} to {df.index[-1].date()}")
    print()

    strategies = [
        {
            "name": "MACD(12,26,9) Classic Crossover",
            "func": strategy_macd_classic,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "signal_crossover"},
        },
        {
            "name": "MACD(12,26,9) Zero-Line Crossover",
            "func": strategy_macd_zeroline,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "zero_line"},
        },
        {
            "name": "MACD(12,26,9) Histogram Reversal",
            "func": strategy_macd_histogram,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "histogram_reversal"},
        },
        {
            "name": "MACD(8,21,5) Fast Crossover",
            "func": strategy_macd_fast,
            "params": {"fast": 8, "slow": 21, "signal": 5, "type": "fast_crossover"},
        },
        {
            "name": "MACD(12,26,9) + EMA200 Trend Filter",
            "func": strategy_macd_trend_filter,
            "params": {"fast": 12, "slow": 26, "signal": 9, "trend_filter": "EMA200"},
        },
        {
            "name": "MACD(12,26,9) Divergence Proxy",
            "func": strategy_macd_divergence,
            "params": {"fast": 12, "slow": 26, "signal": 9, "type": "divergence_proxy", "lookback": 5},
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
    output_path = "/home/user/repo/strategy_output/results_macd.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # Print summary table
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    header = f"{'Strategy':<42} {'Return%':>9} {'AnnRet%':>9} {'Sharpe':>7} {'MaxDD%':>8} {'Trades':>7} {'WinR%':>7} {'PF':>7}"
    print(header)
    print("-" * len(header))

    for r in all_results:
        name = r["strategy"][:40]
        print(f"{name:<42} {r['total_return_pct']:>+8.2f}% {r['annualized_return_pct']:>+8.2f}% "
              f"{r['sharpe_ratio']:>7.2f} {r['max_drawdown_pct']:>7.2f}% "
              f"{r['num_trades']:>7d} {r['win_rate_pct']:>6.1f}% "
              f"{r['profit_factor']:>7.2f}")

    # Buy & hold reference
    bh = all_results[0]["buy_hold_return_pct"]
    print("-" * len(header))
    print(f"{'Buy & Hold (benchmark)':<42} {bh:>+8.2f}%")
    print()

    # Best strategy
    best = max(all_results, key=lambda x: x["sharpe_ratio"])
    print(f"Best risk-adjusted (Sharpe): {best['strategy']}")
    print(f"  Sharpe={best['sharpe_ratio']:.2f}, Return={best['total_return_pct']:+.2f}%, MaxDD={best['max_drawdown_pct']:.2f}%")


if __name__ == "__main__":
    main()
