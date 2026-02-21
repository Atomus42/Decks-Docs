#!/usr/bin/env python3
"""
Hybrid / Composite Strategy Variants – Optimized for 1H BTC/USD Data
Tests 8 composite strategies that combine multiple technical indicators.
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
# Helper functions
# ---------------------------------------------------------------------------

def ema(series: pd.Series, span: int) -> pd.Series:
    """Exponential moving average."""
    return series.ewm(span=span, adjust=False).mean()


def rsi(series: pd.Series, period: int) -> pd.Series:
    """Relative Strength Index."""
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    """Average True Range."""
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.ewm(span=period, adjust=False).mean()


def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal_period: int = 9):
    """MACD line, signal line, and histogram."""
    ema_fast = ema(series, fast)
    ema_slow = ema(series, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, signal_period)
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram


def bollinger_bands(series: pd.Series, period: int = 20, num_std: float = 2.0):
    """Bollinger Bands: upper, middle, lower."""
    middle = series.rolling(period).mean()
    std = series.rolling(period).std()
    upper = middle + num_std * std
    lower = middle - num_std * std
    return upper, middle, lower


def highest(series: pd.Series, period: int) -> pd.Series:
    """Rolling highest value."""
    return series.rolling(period).max()


def lowest(series: pd.Series, period: int) -> pd.Series:
    """Rolling lowest value."""
    return series.rolling(period).min()


# ---------------------------------------------------------------------------
# Strategy 1: Triple Confirmation 1H
# Enter when EMA(13) > EMA(34) AND RSI(14) > 50 AND MACD histogram > 0
# Exit when any 2 of 3 conditions turn bearish
# ---------------------------------------------------------------------------

def signals_triple_confirmation(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    n = len(close)
    warmup = 40

    ema13 = ema(close, 13)
    ema34 = ema(close, 34)
    rsi14 = rsi(close, 14)
    _, _, macd_hist = macd(close, 12, 26, 9)

    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(warmup, n):
        cond_ema = ema13.iloc[i] > ema34.iloc[i]
        cond_rsi = rsi14.iloc[i] > 50
        cond_macd = macd_hist.iloc[i] > 0

        if not in_position:
            # Enter when all 3 bullish
            if cond_ema and cond_rsi and cond_macd:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Count bearish conditions
            bearish_count = sum([not cond_ema, not cond_rsi, not cond_macd])
            if bearish_count >= 2:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 2: EMA(9/21) + Volume Spike
# Enter on EMA crossover only when volume > 2x rolling 20-bar avg
# Exit on EMA crossunder
# ---------------------------------------------------------------------------

def signals_ema_volume_spike(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    volume = df["Volume"]
    n = len(close)
    warmup = 25

    ema9 = ema(close, 9)
    ema21 = ema(close, 21)
    vol_avg20 = volume.rolling(20).mean()

    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(warmup, n):
        fast_above_slow = ema9.iloc[i] > ema21.iloc[i]
        fast_prev_below = ema9.iloc[i - 1] <= ema21.iloc[i - 1]
        volume_spike = volume.iloc[i] > 2.0 * vol_avg20.iloc[i]

        if not in_position:
            # Enter on crossover with volume confirmation
            if fast_above_slow and fast_prev_below and volume_spike:
                in_position = True
                sig.iloc[i] = 1
            # Also enter if crossover already happened with volume
            elif fast_above_slow and volume_spike:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Exit on EMA crossunder
            if not fast_above_slow:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 3: Ichimoku-like
# Tenkan = (highest(9) + lowest(9)) / 2
# Kijun  = (highest(26) + lowest(26)) / 2
# Buy when close > tenkan AND tenkan > kijun AND close > kijun
# Sell when close < kijun
# ---------------------------------------------------------------------------

def signals_ichimoku_like(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    n = len(close)
    warmup = 30

    tenkan = (highest(high, 9) + lowest(low, 9)) / 2
    kijun = (highest(high, 26) + lowest(low, 26)) / 2

    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(warmup, n):
        c = close.iloc[i]
        t = tenkan.iloc[i]
        k = kijun.iloc[i]

        if not in_position:
            if c > t and t > k and c > k:
                in_position = True
                sig.iloc[i] = 1
        else:
            if c < k:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 4: Momentum + Mean Reversion
# Use EMA(100) as trend filter.
# Above EMA100: use EMA(9/21) crossover (momentum)
# Below EMA100: use RSI(14) < 25 buy / > 65 sell (mean reversion)
# ---------------------------------------------------------------------------

def signals_momentum_mean_reversion(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    n = len(close)
    warmup = 105

    ema100 = ema(close, 100)
    ema9 = ema(close, 9)
    ema21 = ema(close, 21)
    rsi14 = rsi(close, 14)

    sig = pd.Series(0, index=close.index)
    in_position = False
    mode = None  # "momentum" or "reversion"

    for i in range(warmup, n):
        c = close.iloc[i]
        above_trend = c > ema100.iloc[i]

        if not in_position:
            if above_trend:
                # Momentum mode: EMA crossover
                if ema9.iloc[i] > ema21.iloc[i] and ema9.iloc[i - 1] <= ema21.iloc[i - 1]:
                    in_position = True
                    mode = "momentum"
                    sig.iloc[i] = 1
            else:
                # Mean reversion mode: RSI oversold
                if rsi14.iloc[i] < 25:
                    in_position = True
                    mode = "reversion"
                    sig.iloc[i] = 1
        else:
            if mode == "momentum":
                # Exit on EMA crossunder
                if ema9.iloc[i] < ema21.iloc[i]:
                    in_position = False
                    mode = None
                    sig.iloc[i] = 0
                else:
                    sig.iloc[i] = 1
            elif mode == "reversion":
                # Exit when RSI > 65
                if rsi14.iloc[i] > 65:
                    in_position = False
                    mode = None
                    sig.iloc[i] = 0
                else:
                    sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 5: Session Filter + EMA
# Only trade during 13:00-21:00 UTC (US session overlap)
# Use EMA(9/21) crossover during these hours, forced exit at 21:00
# ---------------------------------------------------------------------------

def signals_session_filter_ema(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    n = len(close)
    warmup = 25

    ema9 = ema(close, 9)
    ema21 = ema(close, 21)

    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(warmup, n):
        hour = df.index[i].hour
        in_session = 13 <= hour < 21

        if not in_session:
            # Force exit outside session
            if in_position:
                in_position = False
            sig.iloc[i] = 0
            continue

        fast_above = ema9.iloc[i] > ema21.iloc[i]

        if not in_position:
            # Enter on crossover within session
            if fast_above and ema9.iloc[i - 1] <= ema21.iloc[i - 1]:
                in_position = True
                sig.iloc[i] = 1
        else:
            if not fast_above:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 6: Multi-Timeframe (EMA50 as daily trend proxy)
# Only take EMA(9/21) hourly entries when price > EMA(50) (trend aligned)
# Exit on EMA crossunder
# ---------------------------------------------------------------------------

def signals_multi_timeframe(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    n = len(close)
    warmup = 55

    ema50 = ema(close, 50)
    ema9 = ema(close, 9)
    ema21 = ema(close, 21)

    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(warmup, n):
        trend_up = close.iloc[i] > ema50.iloc[i]
        fast_above = ema9.iloc[i] > ema21.iloc[i]
        fast_prev_below = ema9.iloc[i - 1] <= ema21.iloc[i - 1]

        if not in_position:
            if trend_up and fast_above and fast_prev_below:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Exit on EMA crossunder
            if not fast_above:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 7: Volatility Breakout
# Buy when close > close.shift(1) + 1.5*ATR AND close > EMA(50)
# Sell when close < close.shift(1) - 1.0*ATR OR close < EMA(50)
# ---------------------------------------------------------------------------

def signals_volatility_breakout(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    n = len(close)
    warmup = 55

    atr14 = atr(high, low, close, 14)
    ema50 = ema(close, 50)

    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(warmup, n):
        c = close.iloc[i]
        prev_c = close.iloc[i - 1]
        a = atr14.iloc[i]
        e50 = ema50.iloc[i]

        if not in_position:
            # Buy on upside breakout with trend confirmation
            if c > prev_c + 1.5 * a and c > e50:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Sell on downside move or losing trend
            if c < prev_c - 1.0 * a or c < e50:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 8: MACD + RSI + Bollinger Bands Composite
# Enter when MACD > signal AND RSI(14) between 40-65 AND close > BB lower
# Exit when RSI > 80 OR close < BB lower OR MACD < signal
# ---------------------------------------------------------------------------

def signals_macd_rsi_bb(df: pd.DataFrame) -> pd.Series:
    close = df["Close"]
    n = len(close)
    warmup = 35

    macd_line, signal_line, _ = macd(close, 12, 26, 9)
    rsi14 = rsi(close, 14)
    bb_upper, bb_middle, bb_lower = bollinger_bands(close, 20, 2.0)

    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(warmup, n):
        c = close.iloc[i]
        m = macd_line.iloc[i]
        s = signal_line.iloc[i]
        r = rsi14.iloc[i]
        bbl = bb_lower.iloc[i]

        if not in_position:
            # Enter: MACD bullish, RSI neutral, above lower band
            if m > s and 40 <= r <= 65 and c > bbl:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Exit on overbought, BB breakdown, or MACD bearish
            if r > 80 or c < bbl or m < s:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Main: run all strategies
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("HYBRID / COMPOSITE STRATEGY VARIANTS - 1H BTC/USD BACKTEST")
    print("=" * 70)
    print()

    df = backtest_engine.load_data()
    print(f"Loaded {len(df)} hourly bars from {df.index[0]} to {df.index[-1]}")
    print(f"Initial capital: ${backtest_engine.INITIAL_CAPITAL:,.0f}")
    print()

    results = []

    # Strategy definitions: (name, signal_func, params_dict)
    strategies = [
        (
            "Triple Confirmation 1H",
            signals_triple_confirmation,
            {"ema_fast": 13, "ema_slow": 34, "rsi_period": 14,
             "macd": "12/26/9", "exit": "2 of 3 bearish"},
        ),
        (
            "EMA(9/21) + Volume Spike",
            signals_ema_volume_spike,
            {"ema_fast": 9, "ema_slow": 21, "volume_mult": 2.0,
             "vol_avg_period": 20},
        ),
        (
            "Ichimoku-like 1H",
            signals_ichimoku_like,
            {"tenkan_period": 9, "kijun_period": 26,
             "buy": "close>tenkan>kijun", "sell": "close<kijun"},
        ),
        (
            "Momentum + Mean Reversion",
            signals_momentum_mean_reversion,
            {"trend_ema": 100, "mom_ema": "9/21",
             "mr_rsi_buy": 25, "mr_rsi_sell": 65},
        ),
        (
            "Session Filter + EMA(9/21)",
            signals_session_filter_ema,
            {"ema_fast": 9, "ema_slow": 21,
             "session_utc": "13:00-21:00"},
        ),
        (
            "Multi-Timeframe EMA(50)+EMA(9/21)",
            signals_multi_timeframe,
            {"trend_ema": 50, "entry_ema": "9/21",
             "exit": "EMA crossunder"},
        ),
        (
            "Volatility Breakout (ATR)",
            signals_volatility_breakout,
            {"atr_period": 14, "entry_mult": 1.5,
             "exit_mult": 1.0, "trend_ema": 50},
        ),
        (
            "MACD + RSI + BB Composite",
            signals_macd_rsi_bb,
            {"macd": "12/26/9", "rsi_period": 14,
             "rsi_entry": "40-65", "rsi_exit": ">80",
             "bb_period": 20, "bb_std": 2.0},
        ),
    ]

    for name, signal_func, params in strategies:
        print(f"  Running: {name} ...")
        signals = signal_func(df)
        result = backtest_engine.run_backtest(df, signals, name, params)
        results.append(result)

        # Inline summary
        ret = result["total_return_pct"]
        sharpe = result["sharpe_ratio"]
        dd = result["max_drawdown_pct"]
        nt = result["num_trades"]
        wr = result["win_rate_pct"]
        pf = result["profit_factor"]
        print(f"    Return: {ret:+.2f}%  |  Sharpe: {sharpe:.2f}  |  "
              f"MaxDD: {dd:.2f}%  |  Trades: {nt}  |  "
              f"WinRate: {wr:.1f}%  |  PF: {pf:.2f}")

    # Save results
    output_path = os.path.join(STRATEGY_DIR, "results_1h_hybrid.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print()
    print(f"Results saved to {output_path}")

    # ---------- Summary table ----------
    print()
    print("=" * 70)
    print("SUMMARY - HYBRID / COMPOSITE STRATEGIES (1H BTC/USD)")
    print("=" * 70)
    print()
    header = (f"{'Strategy':<40} {'Return%':>8} {'AnnRet%':>8} "
              f"{'Sharpe':>7} {'MaxDD%':>8} {'Trades':>7} "
              f"{'WinR%':>6} {'PF':>6} {'Excess%':>8}")
    print(header)
    print("-" * len(header))

    for r in results:
        print(f"{r['strategy']:<40} "
              f"{r['total_return_pct']:>+8.2f} "
              f"{r['annualized_return_pct']:>+8.2f} "
              f"{r['sharpe_ratio']:>7.2f} "
              f"{r['max_drawdown_pct']:>8.2f} "
              f"{r['num_trades']:>7d} "
              f"{r['win_rate_pct']:>6.1f} "
              f"{r['profit_factor']:>6.2f} "
              f"{r['excess_vs_buyhold_pct']:>+8.2f}")

    print("-" * len(header))
    bh = results[0]["buy_hold_return_pct"]
    print(f"{'Buy & Hold Benchmark':<40} {bh:>+8.2f}")
    print()

    # Best strategy by Sharpe
    best_sharpe = max(results, key=lambda x: x["sharpe_ratio"])
    best_ret = max(results, key=lambda x: x["total_return_pct"])
    best_pf = max(results, key=lambda x: x["profit_factor"])
    print(f"Best Sharpe Ratio:   {best_sharpe['strategy']} "
          f"(Sharpe={best_sharpe['sharpe_ratio']:.2f})")
    print(f"Best Total Return:   {best_ret['strategy']} "
          f"(Return={best_ret['total_return_pct']:+.2f}%)")
    print(f"Best Profit Factor:  {best_pf['strategy']} "
          f"(PF={best_pf['profit_factor']:.2f})")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
