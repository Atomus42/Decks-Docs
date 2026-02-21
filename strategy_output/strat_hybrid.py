#!/usr/bin/env python3
"""
Hybrid / Composite Strategy Variants – BTC/USD Backtest
Tests 6 multi-indicator composite strategies and saves results to JSON.
"""

import sys
import os
import json
from datetime import timedelta

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Make backtest_engine importable
# ---------------------------------------------------------------------------
STRATEGY_DIR = "/home/user/repo/strategy_output"
sys.path.insert(0, STRATEGY_DIR)
import backtest_engine

# ---------------------------------------------------------------------------
# Indicator helpers
# ---------------------------------------------------------------------------

def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def sma(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window).mean()


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    """Returns (macd_line, signal_line, histogram)."""
    ema_fast = ema(series, fast)
    ema_slow = ema(series, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, signal)
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram


def bollinger_bands(series: pd.Series, window: int = 20, num_std: float = 2.0):
    """Returns (upper_band, middle_band, lower_band)."""
    middle = sma(series, window)
    std = series.rolling(window=window).std()
    upper = middle + num_std * std
    lower = middle - num_std * std
    return upper, middle, lower


def realized_vol(series: pd.Series, window: int = 20) -> pd.Series:
    """20-day rolling annualized realized volatility from log returns."""
    log_ret = np.log(series / series.shift(1))
    return log_ret.rolling(window=window).std() * np.sqrt(365)


# ---------------------------------------------------------------------------
# Strategy 1: EMA(21/55) + RSI(14) Filter
# ---------------------------------------------------------------------------
def signals_ema_rsi(close: pd.Series) -> pd.Series:
    """
    Enter on EMA 21/55 cross up only if RSI(14) < 70 (not overbought).
    Exit on EMA cross down OR RSI > 80.
    """
    ema_fast = ema(close, 21)
    ema_slow = ema(close, 55)
    rsi_val = rsi(close, 14)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False

    for i in range(55, n):
        if not in_position:
            # Cross up: fast > slow now AND fast <= slow yesterday
            cross_up = (ema_fast.iloc[i] > ema_slow.iloc[i]) and (ema_fast.iloc[i - 1] <= ema_slow.iloc[i - 1])
            # Also allow entering if fast already above slow (trend continuation)
            # but only on the crossover day to avoid re-entering immediately after exit
            if cross_up and rsi_val.iloc[i] < 70:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Exit conditions
            cross_down = ema_fast.iloc[i] < ema_slow.iloc[i]
            rsi_overbought = rsi_val.iloc[i] > 80
            if cross_down or rsi_overbought:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 2: MACD(12,26,9) + Bollinger Bands(20,2)
# ---------------------------------------------------------------------------
def signals_macd_bb(close: pd.Series) -> pd.Series:
    """
    Enter when MACD crosses above signal AND price < upper Bollinger Band.
    Exit when MACD crosses below signal.
    """
    macd_line, signal_line, _ = macd(close, 12, 26, 9)
    upper_bb, _, _ = bollinger_bands(close, 20, 2.0)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False

    warmup = 30  # enough for all indicators to stabilize

    for i in range(warmup, n):
        if not in_position:
            # MACD cross up: MACD > signal now, MACD <= signal yesterday
            macd_cross_up = (macd_line.iloc[i] > signal_line.iloc[i]) and \
                            (macd_line.iloc[i - 1] <= signal_line.iloc[i - 1])
            price_below_upper_bb = close.iloc[i] < upper_bb.iloc[i]
            if macd_cross_up and price_below_upper_bb:
                in_position = True
                sig.iloc[i] = 1
        else:
            # MACD cross down: MACD < signal now, MACD >= signal yesterday
            macd_cross_down = (macd_line.iloc[i] < signal_line.iloc[i]) and \
                              (macd_line.iloc[i - 1] >= signal_line.iloc[i - 1])
            if macd_cross_down:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 3: Triple Confirmation (EMA + RSI + MACD)
# ---------------------------------------------------------------------------
def signals_triple_confirmation(close: pd.Series) -> pd.Series:
    """
    Enter when ALL three are bullish:
        - EMA(21) > EMA(55)
        - RSI(14) > 50
        - MACD histogram > 0
    Exit when any 2 of 3 turn bearish.
    """
    ema21 = ema(close, 21)
    ema55 = ema(close, 55)
    rsi_val = rsi(close, 14)
    _, _, hist = macd(close, 12, 26, 9)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False
    warmup = 55

    for i in range(warmup, n):
        bull_ema = ema21.iloc[i] > ema55.iloc[i]
        bull_rsi = rsi_val.iloc[i] > 50
        bull_macd = hist.iloc[i] > 0

        bullish_count = int(bull_ema) + int(bull_rsi) + int(bull_macd)
        bearish_count = 3 - bullish_count

        if not in_position:
            if bullish_count == 3:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Exit when 2+ of 3 turn bearish
            if bearish_count >= 2:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 4: Volatility Regime Switch
# ---------------------------------------------------------------------------
def signals_vol_regime(close: pd.Series) -> pd.Series:
    """
    Compute 20-day realized vol. Split into LOW (<= median) and HIGH (> median).
    LOW vol  -> mean-reversion: RSI < 30 buy, RSI > 70 sell.
    HIGH vol -> trend-following: EMA 21/55 crossover.
    """
    rvol = realized_vol(close, 20)
    vol_median = rvol.median()

    rsi_val = rsi(close, 14)
    ema21 = ema(close, 21)
    ema55 = ema(close, 55)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False
    current_regime = None  # 'low' or 'high'

    warmup = 55

    for i in range(warmup, n):
        vol_now = rvol.iloc[i]
        if pd.isna(vol_now):
            sig.iloc[i] = 1 if in_position else 0
            continue

        regime = "low" if vol_now <= vol_median else "high"

        if not in_position:
            if regime == "low":
                # Mean-reversion: buy on oversold
                if rsi_val.iloc[i] < 30:
                    in_position = True
                    current_regime = regime
                    sig.iloc[i] = 1
            else:
                # Trend-following: EMA cross up
                if ema21.iloc[i] > ema55.iloc[i] and ema21.iloc[i - 1] <= ema55.iloc[i - 1]:
                    in_position = True
                    current_regime = regime
                    sig.iloc[i] = 1
        else:
            # Use exit rule matching the regime we entered in
            if current_regime == "low":
                # Mean-reversion exit: RSI > 70
                if rsi_val.iloc[i] > 70:
                    in_position = False
                    sig.iloc[i] = 0
                else:
                    sig.iloc[i] = 1
            else:
                # Trend-following exit: EMA cross down
                if ema21.iloc[i] < ema55.iloc[i]:
                    in_position = False
                    sig.iloc[i] = 0
                else:
                    sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 5: Weekly Momentum + Daily Pullback Entry
# ---------------------------------------------------------------------------
def signals_weekly_momentum_daily_entry(close: pd.Series) -> pd.Series:
    """
    Weekly momentum: close > close[5 days ago] AND close > 20-day SMA.
    Daily entry: when weekly momentum is bullish, enter on RSI(7) < 55 (pullback
    within uptrend -- since RSI(7) rarely drops below 50 during sustained bullish
    momentum, 55 captures meaningful intra-trend dips).
    Exit: RSI(7) > 75.
    """
    close_5ago = close.shift(5)
    sma20 = sma(close, 20)
    rsi7 = rsi(close, 7)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False
    warmup = 25

    for i in range(warmup, n):
        weekly_bull = (close.iloc[i] > close_5ago.iloc[i]) and (close.iloc[i] > sma20.iloc[i])

        if not in_position:
            # Need weekly momentum bullish AND daily pullback (RSI7 < 55)
            if weekly_bull and rsi7.iloc[i] < 55:
                in_position = True
                sig.iloc[i] = 1
        else:
            # Exit on RSI(7) > 75 or weekly momentum turns bearish
            weekly_bear = not ((close.iloc[i] > close_5ago.iloc[i]) and (close.iloc[i] > sma20.iloc[i]))
            if rsi7.iloc[i] > 75 or weekly_bear:
                in_position = False
                sig.iloc[i] = 0
            else:
                sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy 6: CB Avoidance + EMA(21/55)
# ---------------------------------------------------------------------------
FOMC_DATES = [
    "2023-02-01", "2023-03-22", "2023-05-03", "2023-06-14", "2023-07-26",
    "2023-09-20", "2023-11-01", "2023-12-13",
    "2024-01-31", "2024-03-20", "2024-05-01", "2024-06-12", "2024-07-31",
    "2024-09-18", "2024-11-07", "2024-12-18",
    "2025-01-29", "2025-03-19", "2025-05-07", "2025-06-18", "2025-07-30",
    "2025-09-17", "2025-10-29", "2025-12-17",
]


def _build_cb_blackout_set(dates_list: list) -> set:
    """Build a set of dates representing T-1 to T+1 around each CB date."""
    blackout = set()
    for d_str in dates_list:
        d = pd.Timestamp(d_str)
        for offset in range(-1, 2):  # T-1, T, T+1
            blackout.add((d + timedelta(days=offset)).normalize())
    return blackout


def signals_cb_avoidance_ema(close: pd.Series) -> pd.Series:
    """
    EMA 21/55 crossover, but flatten positions during central bank windows
    (T-1 to T+1 around FOMC dates).
    """
    ema21 = ema(close, 21)
    ema55 = ema(close, 55)

    blackout = _build_cb_blackout_set(FOMC_DATES)

    n = len(close)
    sig = pd.Series(0, index=close.index)
    in_position = False
    warmup = 55

    for i in range(warmup, n):
        date = close.index[i]
        in_blackout = date.normalize() in blackout

        ema_bull = ema21.iloc[i] > ema55.iloc[i]

        if in_blackout:
            # Force flat during CB windows
            if in_position:
                in_position = False
            sig.iloc[i] = 0
        else:
            if not in_position:
                # Enter on EMA cross up (or re-enter after blackout if trend still bullish)
                cross_up = ema_bull and (ema21.iloc[i - 1] <= ema55.iloc[i - 1])
                # Also re-enter after a blackout if the trend is still intact
                was_blackout_yesterday = close.index[i - 1].normalize() in blackout
                re_enter = ema_bull and was_blackout_yesterday
                if cross_up or re_enter:
                    in_position = True
                    sig.iloc[i] = 1
            else:
                if not ema_bull:
                    in_position = False
                    sig.iloc[i] = 0
                else:
                    sig.iloc[i] = 1

    return sig


# ---------------------------------------------------------------------------
# Strategy registry
# ---------------------------------------------------------------------------
STRATEGIES = [
    {
        "name": "EMA(21/55) + RSI(14) Filter",
        "params": {"ema_fast": 21, "ema_slow": 55, "rsi_period": 14,
                   "rsi_entry_max": 70, "rsi_exit": 80},
        "signal_fn": lambda close: signals_ema_rsi(close),
    },
    {
        "name": "MACD(12,26,9) + BB(20,2)",
        "params": {"macd_fast": 12, "macd_slow": 26, "macd_signal": 9,
                   "bb_window": 20, "bb_std": 2.0},
        "signal_fn": lambda close: signals_macd_bb(close),
    },
    {
        "name": "Triple Confirmation (EMA+RSI+MACD)",
        "params": {"ema_fast": 21, "ema_slow": 55, "rsi_period": 14,
                   "macd": "12/26/9"},
        "signal_fn": lambda close: signals_triple_confirmation(close),
    },
    {
        "name": "Volatility Regime Switch",
        "params": {"vol_window": 20, "rsi_period": 14,
                   "ema_fast": 21, "ema_slow": 55,
                   "low_vol_rsi_buy": 30, "low_vol_rsi_sell": 70},
        "signal_fn": lambda close: signals_vol_regime(close),
    },
    {
        "name": "Weekly Momentum + Daily Pullback",
        "params": {"momentum_lookback": 5, "sma_period": 20,
                   "rsi_period": 7, "rsi_entry": 55, "rsi_exit": 75,
                   "note": "RSI<55 = pullback within uptrend"},
        "signal_fn": lambda close: signals_weekly_momentum_daily_entry(close),
    },
    {
        "name": "CB Avoidance + EMA(21/55)",
        "params": {"ema_fast": 21, "ema_slow": 55,
                   "cb_window": "T-1 to T+1", "cb_dates": "FOMC 2023-2025"},
        "signal_fn": lambda close: signals_cb_avoidance_ema(close),
    },
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 100)
    print("HYBRID / COMPOSITE STRATEGY VARIANTS – BTC/USD BACKTEST")
    print("=" * 100)

    # Load data
    df = backtest_engine.load_data()
    close = df["Close"]
    print(f"\nData range : {df.index[0].date()} -> {df.index[-1].date()}  ({len(df)} bars)")
    print(f"Initial cap: ${backtest_engine.INITIAL_CAPITAL:,.0f}")
    print(f"Fee rate   : {backtest_engine.FEE_RATE * 100:.2f}%\n")

    results = []

    for strat in STRATEGIES:
        name = strat["name"]
        params = strat["params"]
        sig = strat["signal_fn"](close)
        res = backtest_engine.run_backtest(df, sig, name, params)
        results.append(res)
        print(f"  [done] {name}")

    # ------------------------------------------------------------------
    # Save JSON
    # ------------------------------------------------------------------
    out_path = os.path.join(STRATEGY_DIR, "results_hybrid.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved -> {out_path}")

    # ------------------------------------------------------------------
    # Summary table
    # ------------------------------------------------------------------
    print("\n" + "=" * 130)
    print(f"{'Strategy':<42} {'Return%':>9} {'Ann.Ret%':>9} {'Sharpe':>7} {'MaxDD%':>8} "
          f"{'Trades':>7} {'WinR%':>7} {'PF':>7} {'AvgW%':>7} {'AvgL%':>7} {'vs B&H%':>9}")
    print("-" * 130)

    for r in results:
        print(f"{r['strategy']:<42} "
              f"{r['total_return_pct']:>9.2f} "
              f"{r['annualized_return_pct']:>9.2f} "
              f"{r['sharpe_ratio']:>7.2f} "
              f"{r['max_drawdown_pct']:>8.2f} "
              f"{r['num_trades']:>7d} "
              f"{r['win_rate_pct']:>7.2f} "
              f"{r['profit_factor']:>7.2f} "
              f"{r['avg_win_pct']:>7.2f} "
              f"{r['avg_loss_pct']:>7.2f} "
              f"{r['excess_vs_buyhold_pct']:>9.2f}")

    print("-" * 130)
    bh = results[0]["buy_hold_return_pct"]
    print(f"{'Buy & Hold (benchmark)':<42} {bh:>9.2f}")
    print("=" * 130)

    # Best by various metrics
    best_sharpe = max(results, key=lambda x: x["sharpe_ratio"])
    best_return = max(results, key=lambda x: x["total_return_pct"])
    best_dd = max(results, key=lambda x: x["max_drawdown_pct"])  # least negative = best

    print(f"\nBest by Sharpe     : {best_sharpe['strategy']}  "
          f"(Sharpe={best_sharpe['sharpe_ratio']:.2f}, "
          f"Return={best_sharpe['total_return_pct']:.2f}%, "
          f"MaxDD={best_sharpe['max_drawdown_pct']:.2f}%)")
    print(f"Best by Return     : {best_return['strategy']}  "
          f"(Return={best_return['total_return_pct']:.2f}%, "
          f"Sharpe={best_return['sharpe_ratio']:.2f})")
    print(f"Smallest Drawdown  : {best_dd['strategy']}  "
          f"(MaxDD={best_dd['max_drawdown_pct']:.2f}%, "
          f"Return={best_dd['total_return_pct']:.2f}%)")


if __name__ == "__main__":
    main()
