"""
Bollinger Band strategy variants for BTC/USD backtesting.
Tests multiple BB configurations: mean reversion, breakout, squeeze, and RSI-filtered.
"""
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine


def compute_bollinger(df, period=20, mult=2.0):
    """Compute Bollinger Bands: SMA +/- mult * rolling std."""
    close = df["Close"]
    sma = close.rolling(window=period).mean()
    std = close.rolling(window=period).std()
    upper = sma + mult * std
    lower = sma - mult * std
    return sma, upper, lower


def compute_rsi(series, period=14):
    """Compute RSI indicator."""
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi


# ---------------------------------------------------------------------------
# Strategy signal generators
# ---------------------------------------------------------------------------

def signals_bb_mean_reversion(df, period=20, mult=2.0):
    """Mean reversion: buy when close < lower band, sell when close > upper band."""
    close = df["Close"]
    sma, upper, lower = compute_bollinger(df, period, mult)
    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if pd.isna(lower.iloc[i]):
            signals.iloc[i] = 0
            continue
        if position == 0 and close.iloc[i] < lower.iloc[i]:
            position = 1
        elif position == 1 and close.iloc[i] > upper.iloc[i]:
            position = 0
        signals.iloc[i] = position
    return signals


def signals_bb_breakout(df, period=20, mult=2.0):
    """Breakout: buy when close > upper band, sell when close < SMA."""
    close = df["Close"]
    sma, upper, lower = compute_bollinger(df, period, mult)
    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if pd.isna(upper.iloc[i]):
            signals.iloc[i] = 0
            continue
        if position == 0 and close.iloc[i] > upper.iloc[i]:
            position = 1
        elif position == 1 and close.iloc[i] < sma.iloc[i]:
            position = 0
        signals.iloc[i] = position
    return signals


def signals_bb_squeeze_breakout(df, period=20, mult=2.0):
    """Squeeze + breakout: enter when bandwidth in bottom 20% and price > upper.
       Exit when price < SMA."""
    close = df["Close"]
    sma, upper, lower = compute_bollinger(df, period, mult)
    bandwidth = (upper - lower) / sma
    # Rolling percentile of bandwidth (use expanding for first values)
    bw_pctile = bandwidth.rolling(window=252, min_periods=period).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if pd.isna(upper.iloc[i]) or pd.isna(bw_pctile.iloc[i]):
            signals.iloc[i] = 0
            continue
        if position == 0:
            # Squeeze condition: bandwidth in bottom 20% AND price breaks above upper band
            if bw_pctile.iloc[i] <= 0.20 and close.iloc[i] > upper.iloc[i]:
                position = 1
        elif position == 1:
            if close.iloc[i] < sma.iloc[i]:
                position = 0
        signals.iloc[i] = position
    return signals


def signals_bb_rsi_filter(df, period=20, mult=2.0, rsi_period=14):
    """BB + RSI filter: buy when close < lower AND RSI < 30;
       sell when close > SMA or RSI > 70."""
    close = df["Close"]
    sma, upper, lower = compute_bollinger(df, period, mult)
    rsi = compute_rsi(close, rsi_period)

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if pd.isna(lower.iloc[i]) or pd.isna(rsi.iloc[i]):
            signals.iloc[i] = 0
            continue
        if position == 0:
            if close.iloc[i] < lower.iloc[i] and rsi.iloc[i] < 30:
                position = 1
        elif position == 1:
            if close.iloc[i] > sma.iloc[i] or rsi.iloc[i] > 70:
                position = 0
        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("BOLLINGER BAND STRATEGY VARIANTS  -  BTC/USD BACKTEST")
    print("=" * 72)

    df = backtest_engine.load_data()
    print(f"Data loaded: {len(df)} bars from {df.index[0].date()} to {df.index[-1].date()}\n")

    results = []

    # --- Variant 1: BB(20,2) mean reversion ---
    name = "BB(20,2) Mean Reversion"
    print(f"Running {name}...")
    sigs = signals_bb_mean_reversion(df, period=20, mult=2.0)
    res = backtest_engine.run_backtest(df, sigs, name, {"period": 20, "mult": 2.0, "type": "mean_reversion"})
    results.append(res)

    # --- Variant 2: BB(20,2) breakout ---
    name = "BB(20,2) Breakout"
    print(f"Running {name}...")
    sigs = signals_bb_breakout(df, period=20, mult=2.0)
    res = backtest_engine.run_backtest(df, sigs, name, {"period": 20, "mult": 2.0, "type": "breakout"})
    results.append(res)

    # --- Variant 3: BB(20,1.5) tight bands mean reversion ---
    name = "BB(20,1.5) Tight Mean Reversion"
    print(f"Running {name}...")
    sigs = signals_bb_mean_reversion(df, period=20, mult=1.5)
    res = backtest_engine.run_backtest(df, sigs, name, {"period": 20, "mult": 1.5, "type": "mean_reversion"})
    results.append(res)

    # --- Variant 4: BB(50,2) slow bands mean reversion ---
    name = "BB(50,2) Slow Mean Reversion"
    print(f"Running {name}...")
    sigs = signals_bb_mean_reversion(df, period=50, mult=2.0)
    res = backtest_engine.run_backtest(df, sigs, name, {"period": 50, "mult": 2.0, "type": "mean_reversion"})
    results.append(res)

    # --- Variant 5: BB(20,2) squeeze + breakout ---
    name = "BB(20,2) Squeeze Breakout"
    print(f"Running {name}...")
    sigs = signals_bb_squeeze_breakout(df, period=20, mult=2.0)
    res = backtest_engine.run_backtest(df, sigs, name, {"period": 20, "mult": 2.0, "type": "squeeze_breakout"})
    results.append(res)

    # --- Variant 6: BB(20,2) + RSI filter ---
    name = "BB(20,2) + RSI(14) Filter"
    print(f"Running {name}...")
    sigs = signals_bb_rsi_filter(df, period=20, mult=2.0, rsi_period=14)
    res = backtest_engine.run_backtest(df, sigs, name, {"period": 20, "mult": 2.0, "rsi_period": 14, "type": "mean_reversion_rsi"})
    results.append(res)

    # --- Save results ---
    output_path = "/home/user/repo/strategy_output/results_bollinger.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}\n")

    # --- Print summary table ---
    print("=" * 72)
    print(f"{'Strategy':<35} {'Return%':>9} {'Ann.Ret%':>9} {'Sharpe':>7} {'MaxDD%':>8} {'Trades':>7} {'WinR%':>7} {'PF':>7}")
    print("-" * 72)
    for r in results:
        print(f"{r['strategy']:<35} {r['total_return_pct']:>9.2f} {r['annualized_return_pct']:>9.2f} "
              f"{r['sharpe_ratio']:>7.2f} {r['max_drawdown_pct']:>8.2f} {r['num_trades']:>7d} "
              f"{r['win_rate_pct']:>7.2f} {r['profit_factor']:>7.2f}")
    print("-" * 72)
    print(f"{'Buy & Hold BTC':.<35} {results[0]['buy_hold_return_pct']:>9.2f}")
    print("=" * 72)

    # Highlight best strategy
    best = max(results, key=lambda r: r["sharpe_ratio"])
    print(f"\nBest Sharpe: {best['strategy']}  (Sharpe={best['sharpe_ratio']:.2f}, "
          f"Return={best['total_return_pct']:.2f}%, MaxDD={best['max_drawdown_pct']:.2f}%)")


if __name__ == "__main__":
    main()
