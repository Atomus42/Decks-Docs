#!/usr/bin/env python3
"""
Momentum & Market-Structure Strategy Variants – Optimized for 1H BTC/USD Data
Tests 8 momentum / structure-based strategies on hourly bars.
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
# Helpers
# ---------------------------------------------------------------------------

def ema(series: pd.Series, span: int) -> pd.Series:
    """Exponential moving average."""
    return series.ewm(span=span, adjust=False).mean()


def true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Compute True Range."""
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)


def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    """Average True Range via EMA smoothing."""
    tr = true_range(high, low, close)
    return tr.ewm(span=period, adjust=False).mean()


# ---------------------------------------------------------------------------
# 1. Donchian Channel (24)
# ---------------------------------------------------------------------------
def signals_donchian(close: pd.Series, high: pd.Series, low: pd.Series,
                     entry_period: int, exit_period: int) -> pd.Series:
    """
    Buy: close > highest high of last N bars.
    Sell: close < lowest low of last N/2 bars.
    """
    upper = high.rolling(entry_period).max().shift(1)
    lower = low.rolling(exit_period).min().shift(1)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_pos = False
    warmup = entry_period + 1

    for i in range(warmup, n):
        if not in_pos:
            if close.iloc[i] > upper.iloc[i]:
                in_pos = True
                sig.iloc[i] = 1
        else:
            if close.iloc[i] < lower.iloc[i]:
                in_pos = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1
    return sig


# ---------------------------------------------------------------------------
# 3. ROC(24) Momentum
# ---------------------------------------------------------------------------
def signals_roc_momentum(close: pd.Series, period: int) -> pd.Series:
    """
    Buy when ROC > 0 AND ROC is increasing (ROC > prev ROC).
    Sell when ROC < 0.
    """
    roc = close.pct_change(period) * 100
    roc_prev = roc.shift(1)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_pos = False
    warmup = period + 2

    for i in range(warmup, n):
        if not in_pos:
            if roc.iloc[i] > 0 and roc.iloc[i] > roc_prev.iloc[i]:
                in_pos = True
                sig.iloc[i] = 1
        else:
            if roc.iloc[i] < 0:
                in_pos = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1
    return sig


# ---------------------------------------------------------------------------
# 4. ADX(14) Trend
# ---------------------------------------------------------------------------
def signals_adx_trend(high: pd.Series, low: pd.Series, close: pd.Series,
                      period: int) -> pd.Series:
    """
    Compute +DI, -DI, ADX manually.
    Buy: ADX > 25 AND +DI > -DI.
    Sell: +DI < -DI OR ADX < 20.
    """
    tr = true_range(high, low, close)

    # Directional Movement
    up_move = high - high.shift(1)
    down_move = low.shift(1) - low

    plus_dm = pd.Series(0.0, index=close.index)
    minus_dm = pd.Series(0.0, index=close.index)

    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)

    plus_dm = pd.Series(plus_dm, index=close.index)
    minus_dm = pd.Series(minus_dm, index=close.index)

    # Smooth with EMA
    atr_smooth = tr.ewm(span=period, adjust=False).mean()
    plus_dm_smooth = plus_dm.ewm(span=period, adjust=False).mean()
    minus_dm_smooth = minus_dm.ewm(span=period, adjust=False).mean()

    # Directional Indicators
    plus_di = 100 * plus_dm_smooth / atr_smooth
    minus_di = 100 * minus_dm_smooth / atr_smooth

    # ADX
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
    dx = dx.replace([np.inf, -np.inf], 0).fillna(0)
    adx_line = dx.ewm(span=period, adjust=False).mean()

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_pos = False
    warmup = period * 3  # enough for ADX to stabilize

    for i in range(warmup, n):
        if not in_pos:
            if adx_line.iloc[i] > 25 and plus_di.iloc[i] > minus_di.iloc[i]:
                in_pos = True
                sig.iloc[i] = 1
        else:
            if plus_di.iloc[i] < minus_di.iloc[i] or adx_line.iloc[i] < 20:
                in_pos = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1
    return sig


# ---------------------------------------------------------------------------
# 5. VWAP Reversion (24-bar rolling)
# ---------------------------------------------------------------------------
def signals_vwap_reversion(close: pd.Series, volume: pd.Series,
                           window: int) -> pd.Series:
    """
    Rolling VWAP over 24-bar windows using expanding cumsum within each window.
    Buy when close < VWAP * 0.99 (1% below).
    Sell when close > VWAP * 1.01 (1% above).
    """
    # Replace zero volume with 1 to avoid division issues
    vol = volume.copy()
    vol = vol.replace(0, 1)

    # Rolling VWAP: cumsum(close*volume) / cumsum(volume) within each 24-bar window
    pv = close * vol

    # Use rolling window with expanding-like behaviour:
    # sum of (close * volume) over last 'window' bars / sum of volume over last 'window' bars
    rolling_pv = pv.rolling(window, min_periods=1).sum()
    rolling_vol = vol.rolling(window, min_periods=1).sum()
    vwap = rolling_pv / rolling_vol

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_pos = False
    warmup = window

    for i in range(warmup, n):
        if not in_pos:
            if close.iloc[i] < vwap.iloc[i] * 0.99:
                in_pos = True
                sig.iloc[i] = 1
        else:
            if close.iloc[i] > vwap.iloc[i] * 1.01:
                in_pos = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1
    return sig


# ---------------------------------------------------------------------------
# 6. Supertrend (10, 3)
# ---------------------------------------------------------------------------
def signals_supertrend(high: pd.Series, low: pd.Series, close: pd.Series,
                       atr_period: int, multiplier: float) -> pd.Series:
    """
    Supertrend indicator.
    upper_band = (H+L)/2 + multiplier * ATR
    lower_band = (H+L)/2 - multiplier * ATR
    Trend flips when close crosses bands.
    Buy on uptrend, sell on downtrend.
    """
    atr_val = atr(high, low, close, atr_period)
    hl2 = (high + low) / 2

    upper_basic = hl2 + multiplier * atr_val
    lower_basic = hl2 - multiplier * atr_val

    n = len(close)
    upper_band = upper_basic.copy()
    lower_band = lower_basic.copy()
    supertrend = pd.Series(0.0, index=close.index)
    direction = pd.Series(1, index=close.index)  # 1 = up, -1 = down

    for i in range(1, n):
        # Adjust bands: band can only tighten, not widen against trend
        if lower_basic.iloc[i] > lower_band.iloc[i - 1] or close.iloc[i - 1] < lower_band.iloc[i - 1]:
            lower_band.iloc[i] = lower_basic.iloc[i]
        else:
            lower_band.iloc[i] = lower_band.iloc[i - 1]

        if upper_basic.iloc[i] < upper_band.iloc[i - 1] or close.iloc[i - 1] > upper_band.iloc[i - 1]:
            upper_band.iloc[i] = upper_basic.iloc[i]
        else:
            upper_band.iloc[i] = upper_band.iloc[i - 1]

        # Determine direction
        if direction.iloc[i - 1] == 1:
            # Currently uptrend
            if close.iloc[i] < lower_band.iloc[i]:
                direction.iloc[i] = -1
                supertrend.iloc[i] = upper_band.iloc[i]
            else:
                direction.iloc[i] = 1
                supertrend.iloc[i] = lower_band.iloc[i]
        else:
            # Currently downtrend
            if close.iloc[i] > upper_band.iloc[i]:
                direction.iloc[i] = 1
                supertrend.iloc[i] = lower_band.iloc[i]
            else:
                direction.iloc[i] = -1
                supertrend.iloc[i] = upper_band.iloc[i]

    # Signal: 1 when uptrend, 0 when downtrend
    sig = (direction == 1).astype(int)
    sig.iloc[:atr_period] = 0  # warmup
    return sig


# ---------------------------------------------------------------------------
# 7. Keltner Channel (20, 2x ATR(14))
# ---------------------------------------------------------------------------
def signals_keltner(close: pd.Series, high: pd.Series, low: pd.Series,
                    ema_period: int, atr_period: int,
                    atr_mult: float) -> pd.Series:
    """
    Keltner Channel:
      Upper = EMA(20) + 2 * ATR(14)
      Lower = EMA(20) - 2 * ATR(14)  (not used for exit)
    Buy: close > upper band.
    Sell: close < EMA(20).
    """
    ema_line = ema(close, ema_period)
    atr_val = atr(high, low, close, atr_period)
    upper = ema_line + atr_mult * atr_val

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_pos = False
    warmup = max(ema_period, atr_period) + 1

    for i in range(warmup, n):
        if not in_pos:
            if close.iloc[i] > upper.iloc[i]:
                in_pos = True
                sig.iloc[i] = 1
        else:
            if close.iloc[i] < ema_line.iloc[i]:
                in_pos = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1
    return sig


# ---------------------------------------------------------------------------
# 8. Heikin Ashi Trend
# ---------------------------------------------------------------------------
def signals_heikin_ashi(open_: pd.Series, high: pd.Series,
                        low: pd.Series, close: pd.Series,
                        entry_green: int, exit_red: int) -> pd.Series:
    """
    Heikin Ashi candles:
      ha_close = (O + H + L + C) / 4
      ha_open  = (prev_ha_open + prev_ha_close) / 2  (seed with (O+C)/2)
    Long when 'entry_green' consecutive HA green candles (ha_close > ha_open).
    Exit when 'exit_red' consecutive HA red candles.
    """
    n = len(close)
    ha_close = (open_ + high + low + close) / 4
    ha_open = pd.Series(0.0, index=close.index)

    # Seed first HA open
    ha_open.iloc[0] = (open_.iloc[0] + close.iloc[0]) / 2
    for i in range(1, n):
        ha_open.iloc[i] = (ha_open.iloc[i - 1] + ha_close.iloc[i - 1]) / 2

    # Green / red
    is_green = (ha_close > ha_open).astype(int)
    is_red = (ha_close <= ha_open).astype(int)

    # Count consecutive
    green_streak = pd.Series(0, index=close.index)
    red_streak = pd.Series(0, index=close.index)

    for i in range(1, n):
        green_streak.iloc[i] = (green_streak.iloc[i - 1] + 1) if is_green.iloc[i] else 0
        red_streak.iloc[i] = (red_streak.iloc[i - 1] + 1) if is_red.iloc[i] else 0

    sig = pd.Series(0, index=close.index)
    in_pos = False

    for i in range(entry_green, n):
        if not in_pos:
            if green_streak.iloc[i] >= entry_green:
                in_pos = True
                sig.iloc[i] = 1
        else:
            if red_streak.iloc[i] >= exit_red:
                in_pos = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1
    return sig


# ---------------------------------------------------------------------------
# Define all variants
# ---------------------------------------------------------------------------
VARIANTS = [
    {
        "name": "Donchian Channel(24/12)",
        "params": {"entry_period": 24, "exit_period": 12},
        "signal_fn": lambda df, p: signals_donchian(
            df["Close"], df["High"], df["Low"], p["entry_period"], p["exit_period"]),
    },
    {
        "name": "Donchian Channel(48/24)",
        "params": {"entry_period": 48, "exit_period": 24},
        "signal_fn": lambda df, p: signals_donchian(
            df["Close"], df["High"], df["Low"], p["entry_period"], p["exit_period"]),
    },
    {
        "name": "ROC(24) Momentum",
        "params": {"period": 24},
        "signal_fn": lambda df, p: signals_roc_momentum(df["Close"], p["period"]),
    },
    {
        "name": "ADX(14) Trend Filter",
        "params": {"period": 14, "adx_entry": 25, "adx_exit": 20},
        "signal_fn": lambda df, p: signals_adx_trend(
            df["High"], df["Low"], df["Close"], p["period"]),
    },
    {
        "name": "VWAP Reversion(24)",
        "params": {"window": 24, "entry_pct": 0.99, "exit_pct": 1.01},
        "signal_fn": lambda df, p: signals_vwap_reversion(
            df["Close"], df["Volume"], p["window"]),
    },
    {
        "name": "Supertrend(10, 3.0)",
        "params": {"atr_period": 10, "multiplier": 3.0},
        "signal_fn": lambda df, p: signals_supertrend(
            df["High"], df["Low"], df["Close"], p["atr_period"], p["multiplier"]),
    },
    {
        "name": "Keltner Channel(20, 2xATR14)",
        "params": {"ema_period": 20, "atr_period": 14, "atr_mult": 2.0},
        "signal_fn": lambda df, p: signals_keltner(
            df["Close"], df["High"], df["Low"],
            p["ema_period"], p["atr_period"], p["atr_mult"]),
    },
    {
        "name": "Heikin Ashi Trend(3g/2r)",
        "params": {"entry_green": 3, "exit_red": 2},
        "signal_fn": lambda df, p: signals_heikin_ashi(
            df["Open"], df["High"], df["Low"], df["Close"],
            p["entry_green"], p["exit_red"]),
    },
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 80)
    print("MOMENTUM & MARKET-STRUCTURE STRATEGY VARIANTS – 1H BTC/USD BACKTEST")
    print("=" * 80)

    # Load data
    df = backtest_engine.load_data()
    print(f"\nData range : {df.index[0]} -> {df.index[-1]}  ({len(df)} bars)")
    print(f"Timeframe  : 1H")
    print(f"Initial cap: ${backtest_engine.INITIAL_CAPITAL:,.0f}")
    print(f"Fee rate   : {backtest_engine.FEE_RATE * 100:.2f}%\n")

    results = []

    for v in VARIANTS:
        name = v["name"]
        params = v["params"]
        sig = v["signal_fn"](df, params)
        res = backtest_engine.run_backtest(df, sig, name, params)
        results.append(res)
        print(f"  [done] {name}")

    # ------------------------------------------------------------------
    # Save JSON
    # ------------------------------------------------------------------
    out_path = os.path.join(STRATEGY_DIR, "results_1h_momentum.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved -> {out_path}")

    # ------------------------------------------------------------------
    # Summary table
    # ------------------------------------------------------------------
    print("\n" + "=" * 140)
    print(f"{'Strategy':<32} {'Return%':>9} {'Ann.Ret%':>9} {'Sharpe':>7} {'MaxDD%':>8} "
          f"{'Trades':>7} {'WinR%':>7} {'PF':>7} {'AvgW%':>7} {'AvgL%':>7} {'FinalEq':>12} {'vs B&H%':>9}")
    print("-" * 140)

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

    print("-" * 140)
    print(f"{'Buy & Hold (benchmark)':<32} {results[0]['buy_hold_return_pct']:>9.2f}")
    print("=" * 140)

    # Best variant highlights
    best_sharpe = max(results, key=lambda x: x["sharpe_ratio"])
    best_return = max(results, key=lambda x: x["total_return_pct"])
    best_dd     = max(results, key=lambda x: x["max_drawdown_pct"])  # least negative

    print(f"\n--- Top Picks ---")
    print(f"  Best Sharpe : {best_sharpe['strategy']}  "
          f"(Sharpe={best_sharpe['sharpe_ratio']:.2f}, Return={best_sharpe['total_return_pct']:.2f}%)")
    print(f"  Best Return : {best_return['strategy']}  "
          f"(Return={best_return['total_return_pct']:.2f}%, Sharpe={best_return['sharpe_ratio']:.2f})")
    print(f"  Lowest DD   : {best_dd['strategy']}  "
          f"(MaxDD={best_dd['max_drawdown_pct']:.2f}%, Return={best_dd['total_return_pct']:.2f}%)")


if __name__ == "__main__":
    main()
