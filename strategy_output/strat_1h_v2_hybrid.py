"""
Aggressive Hybrid/Composite Strategies — 1H BTC/USD Backtests
8 strategies designed for SLOW signals (hold days/weeks).
"""

import sys
sys.path.insert(0, "/home/user/repo/strategy_output")

import numpy as np
import pandas as pd
import json

from backtest_engine_1h_v2 import load_data, run_backtest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ema(series, span):
    return series.ewm(span=span, adjust=False).mean()


def rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def macd(series, fast=12, slow=26, signal=9):
    ema_fast = ema(series, fast)
    ema_slow = ema(series, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, signal)
    return macd_line, signal_line


def bollinger_bands(series, period=20, num_std=2.0):
    mid = series.rolling(period).mean()
    std = series.rolling(period).std()
    upper = mid + num_std * std
    lower = mid - num_std * std
    return upper, mid, lower


def atr(high, low, close, period=14):
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(period).mean()


def supertrend(high, low, close, period=50, multiplier=3.0):
    atr_val = atr(high, low, close, period)
    hl2 = (high + low) / 2
    upper_band = hl2 + multiplier * atr_val
    lower_band = hl2 - multiplier * atr_val

    n = len(close)
    trend = pd.Series(np.ones(n), index=close.index)  # 1 = up, -1 = down
    final_upper = upper_band.copy()
    final_lower = lower_band.copy()

    for i in range(1, n):
        # Tighten bands (standard supertrend logic)
        if lower_band.iloc[i] > final_lower.iloc[i-1] or close.iloc[i-1] < final_lower.iloc[i-1]:
            final_lower.iloc[i] = lower_band.iloc[i]
        else:
            final_lower.iloc[i] = final_lower.iloc[i-1]

        if upper_band.iloc[i] < final_upper.iloc[i-1] or close.iloc[i-1] > final_upper.iloc[i-1]:
            final_upper.iloc[i] = upper_band.iloc[i]
        else:
            final_upper.iloc[i] = final_upper.iloc[i-1]

        # Determine trend direction
        if trend.iloc[i-1] == 1:  # was up
            if close.iloc[i] < final_lower.iloc[i]:
                trend.iloc[i] = -1
            else:
                trend.iloc[i] = 1
        else:  # was down
            if close.iloc[i] > final_upper.iloc[i]:
                trend.iloc[i] = 1
            else:
                trend.iloc[i] = -1

    return trend  # 1 = bullish, -1 = bearish


def heikin_ashi(open_, high, low, close):
    ha_close = (open_ + high + low + close) / 4
    ha_open = pd.Series(np.nan, index=close.index)
    ha_open.iloc[0] = (open_.iloc[0] + close.iloc[0]) / 2
    for i in range(1, len(close)):
        ha_open.iloc[i] = (ha_open.iloc[i-1] + ha_close.iloc[i-1]) / 2
    return ha_open, ha_close


# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

def strategy_a(df):
    """A) EMA(50/200) + RSI(14)>50"""
    close = df["Close"]
    ema50 = ema(close, 50)
    ema200 = ema(close, 200)
    rsi14 = rsi(close, 14)
    signals = ((ema50 > ema200) & (rsi14 > 50)).astype(int)
    params = {"ema_fast": 50, "ema_slow": 200, "rsi_period": 14, "rsi_threshold": 50}
    return signals, "A) EMA(50/200) + RSI(14)>50", params


def strategy_b(df):
    """B) EMA(50/200) + Donchian(168)"""
    close = df["Close"]
    ema50 = ema(close, 50)
    ema200 = ema(close, 200)
    donchian_high = df["High"].rolling(168).max()
    golden_cross = ema50 > ema200
    above_donchian = close > donchian_high.shift(1)  # compare to previous bar's channel
    signals = (golden_cross & above_donchian).astype(int)
    params = {"ema_fast": 50, "ema_slow": 200, "donchian_period": 168}
    return signals, "B) EMA(50/200) + Donchian(168)", params


def strategy_c(df):
    """C) Ichimoku Cloud Mega (9/26/52 on hourly)"""
    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    # Tenkan-sen (conversion line): (9-period high + 9-period low) / 2
    tenkan = (high.rolling(9).max() + low.rolling(9).min()) / 2
    # Kijun-sen (base line): (26-period high + 26-period low) / 2
    kijun = (high.rolling(26).max() + low.rolling(26).min()) / 2
    # Senkou Span A: (tenkan + kijun) / 2 shifted forward 26
    senkou_a = ((tenkan + kijun) / 2).shift(26)
    # Senkou Span B: (52-period high + 52-period low) / 2 shifted forward 26
    senkou_b = ((high.rolling(52).max() + low.rolling(52).min()) / 2).shift(26)

    cloud_top = pd.concat([senkou_a, senkou_b], axis=1).max(axis=1)
    above_cloud = close > cloud_top
    conversion_above_base = tenkan > kijun

    signals = (above_cloud & conversion_above_base).astype(int)
    params = {"tenkan": 9, "kijun": 26, "senkou_b_period": 52}
    return signals, "C) Ichimoku Cloud Mega (9/26/52)", params


def strategy_d(df):
    """D) MACD(48,104,36) + EMA(200)"""
    close = df["Close"]
    macd_line, _ = macd(close, fast=48, slow=104, signal=36)
    ema200 = ema(close, 200)
    signals = ((macd_line > 0) & (close > ema200)).astype(int)
    params = {"macd_fast": 48, "macd_slow": 104, "macd_signal": 36, "ema": 200}
    return signals, "D) MACD(48/104/36) + EMA(200)", params


def strategy_e(df):
    """E) Supertrend(50,3) + EMA(200)"""
    close = df["Close"]
    st = supertrend(df["High"], df["Low"], close, period=50, multiplier=3.0)
    ema200 = ema(close, 200)
    signals = ((st == 1) & (close > ema200)).astype(int)
    params = {"supertrend_period": 50, "supertrend_mult": 3.0, "ema": 200}
    return signals, "E) Supertrend(50,3) + EMA(200)", params


def strategy_f(df):
    """F) Heikin Ashi(12G) + EMA(200)
    Long when 12 consecutive green HA bars AND close > EMA(200).
    Exit on 6 consecutive red HA bars OR close < EMA(200).
    """
    close = df["Close"]
    ha_open, ha_close = heikin_ashi(df["Open"], df["High"], df["Low"], close)
    ema200 = ema(close, 200)

    green = (ha_close > ha_open).astype(int)
    red = (ha_close <= ha_open).astype(int)

    # Count consecutive green/red bars
    n = len(close)
    consec_green = pd.Series(np.zeros(n), index=close.index)
    consec_red = pd.Series(np.zeros(n), index=close.index)

    for i in range(1, n):
        if green.iloc[i] == 1:
            consec_green.iloc[i] = consec_green.iloc[i-1] + 1
            consec_red.iloc[i] = 0
        else:
            consec_green.iloc[i] = 0
            consec_red.iloc[i] = consec_red.iloc[i-1] + 1

    # State machine: entry on 12 green + above EMA200, exit on 6 red or below EMA200
    signals = pd.Series(np.zeros(n, dtype=int), index=close.index)
    in_position = False
    for i in range(n):
        if not in_position:
            if consec_green.iloc[i] >= 12 and close.iloc[i] > ema200.iloc[i]:
                in_position = True
                signals.iloc[i] = 1
        else:
            if consec_red.iloc[i] >= 6 or close.iloc[i] < ema200.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    params = {"ha_green_entry": 12, "ha_red_exit": 6, "ema": 200}
    return signals, "F) Heikin Ashi(12G) + EMA(200)", params


def strategy_g(df):
    """G) BB(200,1.5) + MACD(48,104,36)
    Long when close > BB upper AND MACD > signal.
    Exit on close < BB middle.
    """
    close = df["Close"]
    bb_upper, bb_mid, _ = bollinger_bands(close, period=200, num_std=1.5)
    macd_line, signal_line = macd(close, fast=48, slow=104, signal=36)

    n = len(close)
    signals = pd.Series(np.zeros(n, dtype=int), index=close.index)
    in_position = False

    for i in range(n):
        if pd.isna(bb_upper.iloc[i]) or pd.isna(macd_line.iloc[i]):
            continue
        if not in_position:
            if close.iloc[i] > bb_upper.iloc[i] and macd_line.iloc[i] > signal_line.iloc[i]:
                in_position = True
                signals.iloc[i] = 1
        else:
            if close.iloc[i] < bb_mid.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
            else:
                signals.iloc[i] = 1

    params = {"bb_period": 200, "bb_std": 1.5, "macd_fast": 48, "macd_slow": 104, "macd_signal": 36}
    return signals, "G) BB(200,1.5) + MACD(48/104/36)", params


def strategy_h(df):
    """H) Multi-timeframe: Weekly trend (168h EMA cross 504h) + Daily pullback (24h RSI<55)
    Long when weekly trend bullish (EMA168 > EMA504), enter when 24h RSI dips below 55
    then recovers above 55. Exit when weekly trend turns bearish.
    """
    close = df["Close"]
    ema168 = ema(close, 168)
    ema504 = ema(close, 504)
    weekly_bull = ema168 > ema504

    # 24-bar RSI for "daily" pullback timing
    rsi24 = rsi(close, 24)

    n = len(close)
    signals = pd.Series(np.zeros(n, dtype=int), index=close.index)
    in_position = False
    rsi_dipped = False

    for i in range(1, n):
        if pd.isna(rsi24.iloc[i]) or pd.isna(ema504.iloc[i]):
            continue

        if not in_position:
            # Track if RSI has dipped below 55 during bullish weekly trend
            if weekly_bull.iloc[i]:
                if rsi24.iloc[i] < 55:
                    rsi_dipped = True
                if rsi_dipped and rsi24.iloc[i] > 55:
                    in_position = True
                    rsi_dipped = False
                    signals.iloc[i] = 1
            else:
                rsi_dipped = False
        else:
            if not weekly_bull.iloc[i]:
                in_position = False
                signals.iloc[i] = 0
                rsi_dipped = False
            else:
                signals.iloc[i] = 1

    params = {"weekly_ema_fast": 168, "weekly_ema_slow": 504, "daily_rsi_period": 24,
              "rsi_dip_threshold": 55}
    return signals, "H) Multi-TF: Weekly EMA + Daily RSI pullback", params


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 80)
    print("AGGRESSIVE HYBRID/COMPOSITE STRATEGIES — 1H BTC/USD BACKTEST")
    print("=" * 80)

    df = load_data()
    print(f"\nData: {len(df)} bars  |  {df.index[0]} -> {df.index[-1]}")
    print(f"BTC range: ${df['Close'].min():,.0f} — ${df['Close'].max():,.0f}\n")

    strategies = [
        strategy_a, strategy_b, strategy_c, strategy_d,
        strategy_e, strategy_f, strategy_g, strategy_h,
    ]

    all_results = []

    for strat_func in strategies:
        signals, name, params = strat_func(df)
        result = run_backtest(df, signals, name, params)
        all_results.append(result)

        exposure_pct = signals.sum() / len(signals) * 100
        print(f"  {name}")
        print(f"    Return: {result['total_return_pct']:>+10.2f}%  |  "
              f"Ann: {result['annualized_return_pct']:>+8.2f}%  |  "
              f"Sharpe: {result['sharpe_ratio']:>6.2f}  |  "
              f"MaxDD: {result['max_drawdown_pct']:>8.2f}%")
        print(f"    Trades: {result['num_trades']:>4d}  |  "
              f"WinRate: {result['win_rate_pct']:>6.2f}%  |  "
              f"PF: {result['profit_factor']:>7.2f}  |  "
              f"Exposure: {exposure_pct:>5.1f}%")
        print(f"    Final Equity: ${result['final_equity']:>12,.2f}  |  "
              f"B&H: {result['buy_hold_return_pct']:>+8.2f}%  |  "
              f"Excess: {result['excess_vs_buyhold_pct']:>+8.2f}%")
        print()

    # Sort by total return
    all_results.sort(key=lambda x: x["total_return_pct"], reverse=True)

    print("=" * 80)
    print("RANKING BY TOTAL RETURN")
    print("=" * 80)
    for i, r in enumerate(all_results, 1):
        print(f"  {i}. {r['strategy']:<45s}  {r['total_return_pct']:>+10.2f}%  "
              f"Sharpe={r['sharpe_ratio']:.2f}  MaxDD={r['max_drawdown_pct']:.2f}%")

    # Save results
    output_path = "/home/user/repo/strategy_output/results_1h_v2_hybrid.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
