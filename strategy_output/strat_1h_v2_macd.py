"""
MACD v2 strategy variants — slow parameters for MAX RETURNS on 1H BTC/USD.
Designed to minimize trades, hold for days, and ride major trends.
Tests 8 MACD variants using backtest_engine_1h_v2.
"""
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine_1h_v2 as backtest_engine

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


def compute_rsi(close, period=14):
    """Compute RSI."""
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


# ---------------------------------------------------------------------------
# Strategy A: MACD(24,52,18) Slow Signal Crossover
#   2x classic params — buy MACD > signal, sell MACD < signal
# ---------------------------------------------------------------------------

def strategy_a_macd_slow(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 24, 52, 18)

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if macd_line.iloc[i] > signal_line.iloc[i]:
            position = 1
        else:
            position = 0
        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Strategy B: MACD(48,104,36) Ultra-Slow Signal Crossover
#   4x classic params — same logic, even fewer trades
# ---------------------------------------------------------------------------

def strategy_b_macd_ultraslow(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 48, 104, 36)

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        if macd_line.iloc[i] > signal_line.iloc[i]:
            position = 1
        else:
            position = 0
        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Strategy C: MACD(24,52,18) Zero-Line Only
#   Buy when MACD > 0, sell when MACD < 0 — even fewer trades
# ---------------------------------------------------------------------------

def strategy_c_slow_zeroline(df):
    close = df["Close"]
    macd_line, _, _ = compute_macd(close, 24, 52, 18)

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
# Strategy D: MACD(48,104,36) Zero-Line
#   Ultra-slow zero-line — absolute minimum trades
# ---------------------------------------------------------------------------

def strategy_d_ultraslow_zeroline(df):
    close = df["Close"]
    macd_line, _, _ = compute_macd(close, 48, 104, 36)

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
# Strategy E: MACD(12,26,9) + Close > EMA(200) Mandatory Trend Filter
#   Buy when MACD > signal AND close > EMA200 (double confirmation entry).
#   Sell when MACD < signal AND close < EMA200 (double confirmation exit).
# ---------------------------------------------------------------------------

def strategy_e_ema200_double_confirm(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 12, 26, 9)
    ema200 = ema(close, 200)

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        macd_above = macd_line.iloc[i] > signal_line.iloc[i]
        price_above_ema = close.iloc[i] > ema200.iloc[i]

        if position == 0:
            # Entry requires BOTH conditions
            if macd_above and price_above_ema:
                position = 1
        else:
            # Exit requires BOTH bearish conditions (double confirmation to exit)
            macd_below = macd_line.iloc[i] < signal_line.iloc[i]
            price_below_ema = close.iloc[i] < ema200.iloc[i]
            if macd_below and price_below_ema:
                position = 0
        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Strategy F: MACD(24,52,18) + 6-Bar Confirmation
#   Require MACD > signal for 6 consecutive bars to enter.
#   Require MACD < signal for 6 consecutive bars to exit.
#   Eliminates whipsaw trades.
# ---------------------------------------------------------------------------

def strategy_f_6bar_confirmation(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 24, 52, 18)

    signals = pd.Series(0, index=df.index)
    position = 0
    bars_above = 0
    bars_below = 0
    confirm_bars = 6

    for i in range(len(df)):
        if macd_line.iloc[i] > signal_line.iloc[i]:
            bars_above += 1
            bars_below = 0
        else:
            bars_below += 1
            bars_above = 0

        if position == 0 and bars_above >= confirm_bars:
            position = 1
        elif position == 1 and bars_below >= confirm_bars:
            position = 0

        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Strategy G: MACD(12,26,9) Histogram Trend
#   Long when histogram > 0 AND histogram > histogram's own 24-bar EMA
#   (histogram trending up). Exit when histogram < 0.
# ---------------------------------------------------------------------------

def strategy_g_histogram_trend(df):
    close = df["Close"]
    _, _, histogram = compute_macd(close, 12, 26, 9)
    hist_ema24 = ema(histogram, 24)

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        h = histogram.iloc[i]
        he = hist_ema24.iloc[i]

        if position == 0:
            # Enter: histogram > 0 AND histogram trending up (above its own EMA)
            if h > 0 and h > he:
                position = 1
        else:
            # Exit: histogram < 0
            if h < 0:
                position = 0

        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Strategy H: MACD(24,52,18) + RSI(14) Filter
#   Enter when MACD > signal AND RSI > 45 AND RSI < 75
#   (momentum confirmed, not overbought). Exit when MACD < signal.
# ---------------------------------------------------------------------------

def strategy_h_macd_rsi_filter(df):
    close = df["Close"]
    macd_line, signal_line, _ = compute_macd(close, 24, 52, 18)
    rsi = compute_rsi(close, 14)

    signals = pd.Series(0, index=df.index)
    position = 0
    for i in range(len(df)):
        macd_above = macd_line.iloc[i] > signal_line.iloc[i]
        rsi_val = rsi.iloc[i]

        if position == 0:
            # Enter: MACD bullish AND RSI in sweet spot (45-75)
            if macd_above and rsi_val > 45 and rsi_val < 75:
                position = 1
        else:
            # Exit: MACD turns bearish
            if not macd_above:
                position = 0

        signals.iloc[i] = position
    return signals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 80)
    print("MACD v2 Strategy Variants (1H) — Slow Parameters for MAX RETURNS")
    print("=" * 80)

    df = backtest_engine.load_data()
    print(f"Data loaded: {len(df)} bars from {df.index[0]} to {df.index[-1]}")
    print(f"Timeframe: 1H | Initial capital: $100,000 | Fee rate: 0.075%")
    print()

    strategies = [
        {
            "name": "A) MACD(24,52,18) Slow Signal Crossover",
            "func": strategy_a_macd_slow,
            "params": {"fast": 24, "slow": 52, "signal": 18, "type": "slow_signal_crossover"},
        },
        {
            "name": "B) MACD(48,104,36) Ultra-Slow Signal Crossover",
            "func": strategy_b_macd_ultraslow,
            "params": {"fast": 48, "slow": 104, "signal": 36, "type": "ultraslow_signal_crossover"},
        },
        {
            "name": "C) MACD(24,52,18) Zero-Line Only",
            "func": strategy_c_slow_zeroline,
            "params": {"fast": 24, "slow": 52, "signal": 18, "type": "slow_zero_line"},
        },
        {
            "name": "D) MACD(48,104,36) Zero-Line",
            "func": strategy_d_ultraslow_zeroline,
            "params": {"fast": 48, "slow": 104, "signal": 36, "type": "ultraslow_zero_line"},
        },
        {
            "name": "E) MACD(12,26,9) + EMA200 Double Confirm",
            "func": strategy_e_ema200_double_confirm,
            "params": {"fast": 12, "slow": 26, "signal": 9, "trend_filter": "EMA200",
                       "type": "double_confirm_entry_exit"},
        },
        {
            "name": "F) MACD(24,52,18) + 6-Bar Confirmation",
            "func": strategy_f_6bar_confirmation,
            "params": {"fast": 24, "slow": 52, "signal": 18,
                       "confirm_bars": 6, "type": "bar_confirmation"},
        },
        {
            "name": "G) MACD(12,26,9) Histogram Trend",
            "func": strategy_g_histogram_trend,
            "params": {"fast": 12, "slow": 26, "signal": 9,
                       "hist_ema": 24, "type": "histogram_trend"},
        },
        {
            "name": "H) MACD(24,52,18) + RSI(14) Filter",
            "func": strategy_h_macd_rsi_filter,
            "params": {"fast": 24, "slow": 52, "signal": 18,
                       "rsi_period": 14, "rsi_low": 45, "rsi_high": 75,
                       "type": "macd_rsi_filter"},
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
              f"Win Rate: {result['win_rate_pct']:.1f}%  |  "
              f"PF: {result['profit_factor']:.2f}")

    # Save results to JSON
    output_path = "/home/user/repo/strategy_output/results_1h_v2_macd.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # ----- Summary Table -----
    print("\n" + "=" * 80)
    print("SUMMARY — MACD v2 Slow Variants (1H BTC/USD, MAX RETURNS Focus)")
    print("=" * 80)
    header = (f"{'Strategy':<50} {'Return%':>9} {'AnnRet%':>9} {'Sharpe':>7} "
              f"{'MaxDD%':>8} {'Trades':>7} {'WinR%':>7} {'PF':>7}")
    print(header)
    print("-" * len(header))

    for r in all_results:
        name = r["strategy"][:48]
        print(f"{name:<50} {r['total_return_pct']:>+8.2f}% {r['annualized_return_pct']:>+8.2f}% "
              f"{r['sharpe_ratio']:>7.2f} {r['max_drawdown_pct']:>7.2f}% "
              f"{r['num_trades']:>7d} {r['win_rate_pct']:>6.1f}% "
              f"{r['profit_factor']:>7.2f}")

    # Buy & hold reference
    bh = all_results[0]["buy_hold_return_pct"]
    print("-" * len(header))
    print(f"{'Buy & Hold (benchmark)':<50} {bh:>+8.2f}%")
    print()

    # ----- Best by category -----
    best_return = max(all_results, key=lambda x: x["total_return_pct"])
    print(f"BEST Total Return: {best_return['strategy']}")
    print(f"  Return={best_return['total_return_pct']:+.2f}%, "
          f"Sharpe={best_return['sharpe_ratio']:.2f}, "
          f"MaxDD={best_return['max_drawdown_pct']:.2f}%, "
          f"Trades={best_return['num_trades']}")

    best_sharpe = max(all_results, key=lambda x: x["sharpe_ratio"])
    print(f"\nBEST Risk-Adjusted (Sharpe): {best_sharpe['strategy']}")
    print(f"  Sharpe={best_sharpe['sharpe_ratio']:.2f}, "
          f"Return={best_sharpe['total_return_pct']:+.2f}%, "
          f"MaxDD={best_sharpe['max_drawdown_pct']:.2f}%")

    best_pf = max(all_results, key=lambda x: x["profit_factor"])
    print(f"\nBEST Profit Factor: {best_pf['strategy']}")
    print(f"  PF={best_pf['profit_factor']:.2f}, "
          f"Win Rate={best_pf['win_rate_pct']:.1f}%, "
          f"Trades={best_pf['num_trades']}")

    least_dd = max(all_results, key=lambda x: x["max_drawdown_pct"])  # least negative
    print(f"\nSMALLEST Max Drawdown: {least_dd['strategy']}")
    print(f"  MaxDD={least_dd['max_drawdown_pct']:.2f}%, "
          f"Return={least_dd['total_return_pct']:+.2f}%, "
          f"Trades={least_dd['num_trades']}")

    fewest_trades = min(all_results, key=lambda x: x["num_trades"])
    print(f"\nFEWEST Trades (hold longest): {fewest_trades['strategy']}")
    print(f"  Trades={fewest_trades['num_trades']}, "
          f"Return={fewest_trades['total_return_pct']:+.2f}%, "
          f"Sharpe={fewest_trades['sharpe_ratio']:.2f}")

    # ----- Excess vs buy & hold -----
    print(f"\nStrategies beating buy & hold ({bh:+.2f}%):")
    beaters = [r for r in all_results if r["total_return_pct"] > bh]
    if beaters:
        for r in sorted(beaters, key=lambda x: x["excess_vs_buyhold_pct"], reverse=True):
            print(f"  {r['strategy']}: {r['total_return_pct']:+.2f}% "
                  f"(excess: {r['excess_vs_buyhold_pct']:+.2f}%)")
    else:
        print("  None")

    print()


if __name__ == "__main__":
    main()
