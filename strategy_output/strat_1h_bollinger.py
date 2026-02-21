"""
Bollinger Band strategy variants optimized for 1H BTC/USD data.
Tests 8 BB configurations: mean reversion, breakout, squeeze, RSI-filtered,
bounce, and Keltner+BB combo.
"""
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine_1h as backtest_engine


# ---------------------------------------------------------------------------
# Indicator helpers
# ---------------------------------------------------------------------------

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


def compute_atr(df, period=14):
    """Compute Average True Range."""
    high = df["High"]
    low = df["Low"]
    close = df["Close"]
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.rolling(window=period, min_periods=period).mean()
    return atr


def compute_ema(series, period):
    """Compute Exponential Moving Average."""
    return series.ewm(span=period, adjust=False).mean()


def compute_keltner(df, period=20, atr_period=14, atr_mult=1.5):
    """Compute Keltner Channel: EMA +/- mult * ATR."""
    ema = compute_ema(df["Close"], period)
    atr = compute_atr(df, atr_period)
    upper = ema + atr_mult * atr
    lower = ema - atr_mult * atr
    return ema, upper, lower


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


def signals_bb_tight_mean_reversion(df):
    """BB(20,1.5) tight mean reversion: buy close < lower, sell close > upper."""
    return signals_bb_mean_reversion(df, period=20, mult=1.5)


def signals_bb_slow_mean_reversion(df):
    """BB(50,2) slow: buy close < lower, sell close > upper."""
    return signals_bb_mean_reversion(df, period=50, mult=2.0)


def signals_bb_squeeze_breakout(df, period=20, mult=2.0, lookback=120):
    """Squeeze breakout: bandwidth = (upper-lower)/sma;
    in_squeeze = bandwidth < bandwidth.rolling(120).quantile(0.2);
    buy when in_squeeze shifts to not in_squeeze AND close > upper;
    sell when close < sma."""
    close = df["Close"]
    sma, upper, lower = compute_bollinger(df, period, mult)
    bandwidth = (upper - lower) / sma
    bw_quantile = bandwidth.rolling(window=lookback, min_periods=period).quantile(0.2)
    in_squeeze = bandwidth < bw_quantile

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if pd.isna(upper.iloc[i]) or pd.isna(bw_quantile.iloc[i]):
            signals.iloc[i] = 0
            continue
        if position == 0:
            # Squeeze just released: was in squeeze on prior bar, not in squeeze now
            if i > 0 and in_squeeze.iloc[i - 1] and not in_squeeze.iloc[i]:
                if close.iloc[i] > upper.iloc[i]:
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


def signals_bb_bounce(df, period=20, mult=2.0, max_hold_bars=24):
    """Bounce off lower band: buy when close > lower AND previous close <= previous lower
    (price bounces off lower band). Sell when close > upper or after 24 bars."""
    close = df["Close"]
    sma, upper, lower = compute_bollinger(df, period, mult)

    signals = pd.Series(0, index=df.index)
    position = 0
    bars_held = 0
    for i in range(len(df)):
        if pd.isna(lower.iloc[i]) or i == 0:
            signals.iloc[i] = 0
            continue
        if position == 0:
            # Bounce: current close above lower, previous close at or below previous lower
            if (close.iloc[i] > lower.iloc[i]
                    and close.iloc[i - 1] <= lower.iloc[i - 1]):
                position = 1
                bars_held = 0
        elif position == 1:
            bars_held += 1
            if close.iloc[i] > upper.iloc[i] or bars_held >= max_hold_bars:
                position = 0
                bars_held = 0
        signals.iloc[i] = position
    return signals


def signals_keltner_bb_combo(df, bb_period=20, bb_mult=2.0,
                              kc_period=20, kc_atr_period=14, kc_atr_mult=1.5):
    """Keltner + BB combo: BB inside Keltner = squeeze.
    Buy when squeeze releases AND close > BB upper. Sell when close < EMA(20)."""
    close = df["Close"]
    bb_sma, bb_upper, bb_lower = compute_bollinger(df, bb_period, bb_mult)
    kc_ema, kc_upper, kc_lower = compute_keltner(df, kc_period, kc_atr_period, kc_atr_mult)
    ema20 = compute_ema(close, 20)

    # Squeeze: BB bands are inside Keltner Channel
    in_squeeze = (bb_lower > kc_lower) & (bb_upper < kc_upper)

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if pd.isna(bb_upper.iloc[i]) or pd.isna(kc_upper.iloc[i]):
            signals.iloc[i] = 0
            continue
        if position == 0:
            # Squeeze release: was in squeeze on prior bar, no longer in squeeze
            if i > 0 and in_squeeze.iloc[i - 1] and not in_squeeze.iloc[i]:
                if close.iloc[i] > bb_upper.iloc[i]:
                    position = 1
        elif position == 1:
            if close.iloc[i] < ema20.iloc[i]:
                position = 0
        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("BOLLINGER BAND STRATEGY VARIANTS (1H)  -  BTC/USD BACKTEST")
    print("=" * 78)

    df = backtest_engine.load_data()
    print(f"Data loaded: {len(df)} bars from {df.index[0].date()} to {df.index[-1].date()}\n")

    results = []

    # --- Variant 1: BB(20,2) mean reversion ---
    name = "BB(20,2) Mean Reversion"
    print(f"  Running {name}...")
    sigs = signals_bb_mean_reversion(df, period=20, mult=2.0)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"period": 20, "mult": 2.0, "type": "mean_reversion"})
    results.append(res)

    # --- Variant 2: BB(20,2) breakout ---
    name = "BB(20,2) Breakout"
    print(f"  Running {name}...")
    sigs = signals_bb_breakout(df, period=20, mult=2.0)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"period": 20, "mult": 2.0, "type": "breakout"})
    results.append(res)

    # --- Variant 3: BB(20,1.5) tight bands mean reversion ---
    name = "BB(20,1.5) Tight Mean Reversion"
    print(f"  Running {name}...")
    sigs = signals_bb_tight_mean_reversion(df)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"period": 20, "mult": 1.5, "type": "mean_reversion"})
    results.append(res)

    # --- Variant 4: BB(50,2) slow mean reversion ---
    name = "BB(50,2) Slow Mean Reversion"
    print(f"  Running {name}...")
    sigs = signals_bb_slow_mean_reversion(df)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"period": 50, "mult": 2.0, "type": "mean_reversion"})
    results.append(res)

    # --- Variant 5: BB(20,2) squeeze breakout ---
    name = "BB(20,2) Squeeze Breakout"
    print(f"  Running {name}...")
    sigs = signals_bb_squeeze_breakout(df, period=20, mult=2.0, lookback=120)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"period": 20, "mult": 2.0, "lookback": 120, "type": "squeeze_breakout"})
    results.append(res)

    # --- Variant 6: BB(20,2) + RSI(14) filter ---
    name = "BB(20,2) + RSI(14) Filter"
    print(f"  Running {name}...")
    sigs = signals_bb_rsi_filter(df, period=20, mult=2.0, rsi_period=14)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"period": 20, "mult": 2.0, "rsi_period": 14, "type": "mean_reversion_rsi"})
    results.append(res)

    # --- Variant 7: BB(20,2) bounce ---
    name = "BB(20,2) Bounce"
    print(f"  Running {name}...")
    sigs = signals_bb_bounce(df, period=20, mult=2.0, max_hold_bars=24)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"period": 20, "mult": 2.0, "max_hold_bars": 24, "type": "bounce"})
    results.append(res)

    # --- Variant 8: Keltner + BB combo ---
    name = "Keltner+BB Squeeze Combo"
    print(f"  Running {name}...")
    sigs = signals_keltner_bb_combo(df, bb_period=20, bb_mult=2.0,
                                     kc_period=20, kc_atr_period=14, kc_atr_mult=1.5)
    res = backtest_engine.run_backtest(df, sigs, name,
          {"bb_period": 20, "bb_mult": 2.0, "kc_period": 20,
           "kc_atr_period": 14, "kc_atr_mult": 1.5, "type": "keltner_bb_squeeze"})
    results.append(res)

    # --- Save results ---
    output_path = "/home/user/repo/strategy_output/results_1h_bollinger.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}\n")

    # --- Print summary table ---
    print("=" * 100)
    print(f"{'Strategy':<32} {'Return%':>9} {'Ann.Ret%':>9} {'Sharpe':>7} "
          f"{'MaxDD%':>8} {'Trades':>7} {'WinR%':>7} {'PF':>7} {'Excess%':>9}")
    print("-" * 100)
    for r in results:
        print(f"{r['strategy']:<32} {r['total_return_pct']:>9.2f} "
              f"{r['annualized_return_pct']:>9.2f} {r['sharpe_ratio']:>7.2f} "
              f"{r['max_drawdown_pct']:>8.2f} {r['num_trades']:>7d} "
              f"{r['win_rate_pct']:>7.2f} {r['profit_factor']:>7.2f} "
              f"{r['excess_vs_buyhold_pct']:>9.2f}")
    print("-" * 100)
    print(f"{'Buy & Hold BTC':.<32} {results[0]['buy_hold_return_pct']:>9.2f}")
    print("=" * 100)

    # Highlight best strategy by Sharpe
    best_sharpe = max(results, key=lambda r: r["sharpe_ratio"])
    print(f"\nBest Sharpe:  {best_sharpe['strategy']}  "
          f"(Sharpe={best_sharpe['sharpe_ratio']:.2f}, "
          f"Return={best_sharpe['total_return_pct']:.2f}%, "
          f"MaxDD={best_sharpe['max_drawdown_pct']:.2f}%)")

    best_return = max(results, key=lambda r: r["total_return_pct"])
    print(f"Best Return:  {best_return['strategy']}  "
          f"(Return={best_return['total_return_pct']:.2f}%, "
          f"Sharpe={best_return['sharpe_ratio']:.2f}, "
          f"MaxDD={best_return['max_drawdown_pct']:.2f}%)")

    best_pf = max(results, key=lambda r: r["profit_factor"])
    print(f"Best PF:      {best_pf['strategy']}  "
          f"(PF={best_pf['profit_factor']:.2f}, "
          f"WinRate={best_pf['win_rate_pct']:.2f}%, "
          f"Trades={best_pf['num_trades']})")


if __name__ == "__main__":
    main()
