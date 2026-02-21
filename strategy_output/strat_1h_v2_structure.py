#!/usr/bin/env python3
"""
Market Structure Strategies – Optimized for MAX RETURNS on 1H BTC/USD
Tests 8 market-structure strategies designed to ride the big move from $50K to $120K+.

Categories:
  a) Higher Highs (rolling 168-bar weekly high breakout)
  b) Volatility Regime (low-vol EMA, high-vol flat)
  c) Monthly Momentum (close vs 720-bar lookback)
  d) Bi-weekly Momentum (close vs 336-bar lookback + EMA200 filter)
  e) ATR Breakout Slow (SMA200 + 0.5*ATR168 breakout)
  f) Keltner Ultra-Wide (EMA200 + 2*ATR168 channel)
  g) Price Relative to ATH Proxy (expanding max proximity)
  h) Heikin Ashi Weekly (consecutive green/red HA candle counting)
"""

import sys
import os
import json

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Make backtest engine importable
# ---------------------------------------------------------------------------
STRATEGY_DIR = "/home/user/repo/strategy_output"
sys.path.insert(0, STRATEGY_DIR)
import backtest_engine_1h_v2 as backtest_engine

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def ema(series: pd.Series, span: int) -> pd.Series:
    """Exponential moving average."""
    return series.ewm(span=span, adjust=False).mean()


def sma(series: pd.Series, period: int) -> pd.Series:
    """Simple moving average."""
    return series.rolling(window=period).mean()


def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    """Average True Range."""
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.ewm(span=period, adjust=False).mean()


# ---------------------------------------------------------------------------
# Strategy definitions
# ---------------------------------------------------------------------------

def strategy_higher_highs(df: pd.DataFrame) -> dict:
    """
    a) Higher Highs: track rolling 168-bar (1 week) high.
    Long when current 168-bar high > previous 168-bar high (shifted 168 bars).
    Exit when current high < previous high.
    """
    close = df["Close"]
    high = df["High"]

    rolling_high = high.rolling(window=168).max()
    prev_rolling_high = rolling_high.shift(168)

    signals = pd.Series(0, index=df.index)
    signals[rolling_high > prev_rolling_high] = 1
    signals[rolling_high < prev_rolling_high] = 0

    params = {"rolling_window": 168, "shift": 168}
    return backtest_engine.run_backtest(df, signals, "Higher Highs (168-bar)", params)


def strategy_volatility_regime(df: pd.DataFrame) -> dict:
    """
    b) Volatility Regime: 20-bar realized vol = close.pct_change().rolling(480).std() * sqrt(8760).
    If vol < median vol → use EMA(50/200) crossover. If vol > median → stay flat.
    Median computed over the full dataset.
    """
    close = df["Close"]

    # Realized volatility (annualized)
    returns = close.pct_change()
    realized_vol = returns.rolling(window=480).std() * np.sqrt(8760)
    median_vol = realized_vol.median()

    # EMA crossover
    ema_50 = ema(close, 50)
    ema_200 = ema(close, 200)

    # Low-vol regime: use EMA crossover; high-vol: flat
    ema_signal = (ema_50 > ema_200).astype(int)
    low_vol_mask = (realized_vol < median_vol).astype(int)

    signals = ema_signal * low_vol_mask

    params = {
        "vol_window": 480,
        "annualization_factor": 8760,
        "ema_fast": 50,
        "ema_slow": 200,
        "median_vol": round(float(median_vol), 4) if pd.notna(median_vol) else None,
    }
    return backtest_engine.run_backtest(df, signals, "Vol Regime EMA(50/200)", params)


def strategy_monthly_momentum(df: pd.DataFrame) -> dict:
    """
    c) Monthly Momentum: long when close > close.shift(720) (~30 days of hourly bars).
    Exit when close < close.shift(720). Very slow.
    """
    close = df["Close"]

    prev_close = close.shift(720)
    signals = pd.Series(0, index=df.index)
    signals[close > prev_close] = 1
    signals[close <= prev_close] = 0

    params = {"lookback_bars": 720}
    return backtest_engine.run_backtest(df, signals, "Monthly Momentum (720-bar)", params)


def strategy_biweekly_momentum(df: pd.DataFrame) -> dict:
    """
    d) Bi-weekly Momentum: long when close > close.shift(336) AND close > EMA(200).
    Exit when close < close.shift(336).
    """
    close = df["Close"]

    prev_close = close.shift(336)
    ema_200 = ema(close, 200)

    entry_cond = (close > prev_close) & (close > ema_200)
    exit_cond = close < prev_close

    # State machine for proper entry/exit logic
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        if not in_position:
            if entry_cond.iloc[i]:
                in_position = True
                signals.iloc[i] = 1
            else:
                signals.iloc[i] = 0
        else:
            if exit_cond.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    params = {"lookback_bars": 336, "ema_period": 200}
    return backtest_engine.run_backtest(df, signals, "Bi-weekly Momentum (336-bar + EMA200)", params)


def strategy_atr_breakout_slow(df: pd.DataFrame) -> dict:
    """
    e) ATR Breakout Slow: long when close > SMA(200) + 0.5 * ATR(168).
    Exit when close < SMA(200).
    """
    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    sma_200 = sma(close, 200)
    atr_168 = atr(high, low, close, 168)

    upper_band = sma_200 + 0.5 * atr_168
    lower_band = sma_200

    # State machine: enter on breakout above upper, exit on drop below lower
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        price = close.iloc[i]
        if pd.isna(upper_band.iloc[i]) or pd.isna(lower_band.iloc[i]):
            signals.iloc[i] = 0
            continue
        if not in_position:
            if price > upper_band.iloc[i]:
                in_position = True
                signals.iloc[i] = 1
            else:
                signals.iloc[i] = 0
        else:
            if price < lower_band.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    params = {"sma_period": 200, "atr_period": 168, "atr_multiplier": 0.5}
    return backtest_engine.run_backtest(df, signals, "ATR Breakout Slow (SMA200 + 0.5*ATR168)", params)


def strategy_keltner_ultra_wide(df: pd.DataFrame) -> dict:
    """
    f) Keltner Ultra-Wide: upper = EMA(200) + 2*ATR(168), lower = EMA(200).
    Long when close > upper. Exit when close < EMA(200).
    """
    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    ema_200 = ema(close, 200)
    atr_168 = atr(high, low, close, 168)

    upper_band = ema_200 + 2.0 * atr_168
    lower_band = ema_200

    # State machine
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        price = close.iloc[i]
        if pd.isna(upper_band.iloc[i]) or pd.isna(lower_band.iloc[i]):
            signals.iloc[i] = 0
            continue
        if not in_position:
            if price > upper_band.iloc[i]:
                in_position = True
                signals.iloc[i] = 1
            else:
                signals.iloc[i] = 0
        else:
            if price < lower_band.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    params = {"ema_period": 200, "atr_period": 168, "atr_multiplier": 2.0}
    return backtest_engine.run_backtest(df, signals, "Keltner Ultra-Wide (EMA200 + 2*ATR168)", params)


def strategy_ath_proximity(df: pd.DataFrame) -> dict:
    """
    g) Price Relative to ATH Proxy: expanding max of close.
    Long when close > 0.85 * expanding_max (within 15% of ATH).
    Exit when close < 0.70 * expanding_max.
    """
    close = df["Close"]

    expanding_max = close.expanding().max()
    upper_threshold = 0.85 * expanding_max
    lower_threshold = 0.70 * expanding_max

    # State machine
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        price = close.iloc[i]
        if not in_position:
            if price > upper_threshold.iloc[i]:
                in_position = True
                signals.iloc[i] = 1
            else:
                signals.iloc[i] = 0
        else:
            if price < lower_threshold.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    params = {"entry_pct_of_ath": 0.85, "exit_pct_of_ath": 0.70}
    return backtest_engine.run_backtest(df, signals, "ATH Proximity (85%/70%)", params)


def strategy_heikin_ashi_weekly(df: pd.DataFrame) -> dict:
    """
    h) Heikin Ashi Weekly: compute HA candles, count consecutive green (ha_close > ha_open).
    Long when 12+ consecutive HA green candles. Exit when 6+ consecutive HA red.
    """
    close = df["Close"]
    open_ = df["Open"]
    high = df["High"]
    low = df["Low"]

    # Compute Heikin Ashi candles
    ha_close = (open_ + high + low + close) / 4.0

    ha_open = pd.Series(0.0, index=df.index)
    ha_open.iloc[0] = (open_.iloc[0] + close.iloc[0]) / 2.0
    for i in range(1, len(df)):
        ha_open.iloc[i] = (ha_open.iloc[i - 1] + ha_close.iloc[i - 1]) / 2.0

    ha_high = pd.concat([high, ha_open, ha_close], axis=1).max(axis=1)
    ha_low = pd.concat([low, ha_open, ha_close], axis=1).min(axis=1)

    # Count consecutive green/red candles
    is_green = (ha_close > ha_open).astype(int)
    is_red = (ha_close <= ha_open).astype(int)

    consec_green = pd.Series(0, index=df.index)
    consec_red = pd.Series(0, index=df.index)

    for i in range(len(df)):
        if is_green.iloc[i]:
            consec_green.iloc[i] = (consec_green.iloc[i - 1] + 1) if i > 0 else 1
            consec_red.iloc[i] = 0
        else:
            consec_red.iloc[i] = (consec_red.iloc[i - 1] + 1) if i > 0 else 1
            consec_green.iloc[i] = 0

    # State machine: enter after 12+ green, exit after 6+ red
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        if not in_position:
            if consec_green.iloc[i] >= 12:
                in_position = True
                signals.iloc[i] = 1
            else:
                signals.iloc[i] = 0
        else:
            if consec_red.iloc[i] >= 6:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    params = {"green_entry_threshold": 12, "red_exit_threshold": 6}
    return backtest_engine.run_backtest(df, signals, "Heikin Ashi Weekly (12G/6R)", params)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 80)
    print("MARKET STRUCTURE STRATEGIES — 1H BTC/USD (v2 Engine, MAX RETURNS)")
    print("=" * 80)

    df = backtest_engine.load_data()
    print(f"\nData loaded: {len(df)} bars from {df.index[0]} to {df.index[-1]}")
    print(f"Price range: ${df['Close'].min():,.2f} – ${df['Close'].max():,.2f}")
    print(f"Buy & Hold return: {(df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100:.2f}%")
    print()

    strategies = [
        ("a", strategy_higher_highs),
        ("b", strategy_volatility_regime),
        ("c", strategy_monthly_momentum),
        ("d", strategy_biweekly_momentum),
        ("e", strategy_atr_breakout_slow),
        ("f", strategy_keltner_ultra_wide),
        ("g", strategy_ath_proximity),
        ("h", strategy_heikin_ashi_weekly),
    ]

    results = []
    for label, func in strategies:
        print(f"  Running strategy ({label}): {func.__name__} ...")
        result = func(df)
        results.append(result)
        print(f"    -> {result['strategy']}: Return={result['total_return_pct']:.2f}%, "
              f"Sharpe={result['sharpe_ratio']:.2f}, MaxDD={result['max_drawdown_pct']:.2f}%, "
              f"Trades={result['num_trades']}, WinRate={result['win_rate_pct']:.1f}%")

    # Save results
    output_path = "/home/user/repo/strategy_output/results_1h_v2_structure.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # Summary table
    print("\n" + "=" * 80)
    print(f"{'Strategy':<45} {'Return%':>9} {'Sharpe':>7} {'MaxDD%':>8} {'Trades':>7} {'WR%':>6} {'PF':>7} {'FinalEq':>12}")
    print("-" * 80)

    results_sorted = sorted(results, key=lambda r: r["total_return_pct"], reverse=True)
    for r in results_sorted:
        pf_str = f"{r['profit_factor']:.2f}" if r['profit_factor'] < 999 else "INF"
        print(f"{r['strategy']:<45} {r['total_return_pct']:>8.2f}% {r['sharpe_ratio']:>7.2f} "
              f"{r['max_drawdown_pct']:>7.2f}% {r['num_trades']:>7} {r['win_rate_pct']:>5.1f}% "
              f"{pf_str:>7} ${r['final_equity']:>11,.2f}")

    print("-" * 80)
    bh = results[0]["buy_hold_return_pct"]
    print(f"{'Buy & Hold':<45} {bh:>8.2f}%")

    # Best strategy highlight
    best = results_sorted[0]
    print(f"\n*** BEST STRATEGY: {best['strategy']}")
    print(f"    Total Return: {best['total_return_pct']:.2f}% | "
          f"Ann. Return: {best['annualized_return_pct']:.2f}% | "
          f"Sharpe: {best['sharpe_ratio']:.2f}")
    print(f"    Max Drawdown: {best['max_drawdown_pct']:.2f}% | "
          f"Trades: {best['num_trades']} | "
          f"Win Rate: {best['win_rate_pct']:.1f}% | "
          f"Profit Factor: {best['profit_factor']:.2f}")
    print(f"    Final Equity: ${best['final_equity']:,.2f} | "
          f"Excess vs B&H: {best['excess_vs_buyhold_pct']:.2f}%")

    # Count strategies that beat buy & hold
    beaters = [r for r in results if r["total_return_pct"] > bh]
    print(f"\n    {len(beaters)}/{len(results)} strategies beat Buy & Hold ({bh:.2f}%)")
    print("=" * 80)


if __name__ == "__main__":
    main()
