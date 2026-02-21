"""
Momentum / Trend-Following Strategy Variants for BTC/USD
Tests: Donchian Channel (20 & 55), Rate of Change, ADX, Keltner Channel, Simple Momentum
"""
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine

# ── Helpers ──────────────────────────────────────────────────────────────────

def ema(series, span):
    """Exponential moving average."""
    return series.ewm(span=span, adjust=False).mean()


def atr(df, period):
    """Average True Range."""
    high, low, close = df["High"], df["Low"], df["Close"]
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(period).mean()


# ── Strategy 1: Donchian Channel (20/10) – Turtle Trading ────────────────────

def donchian_signals(df, entry_period, exit_period):
    high = df["High"]
    low = df["Low"]
    close = df["Close"]

    upper = high.shift(1).rolling(entry_period).max()   # highest high of last N bars
    lower = low.shift(1).rolling(exit_period).min()      # lowest low of last M bars

    signals = pd.Series(0, index=df.index)
    pos = 0
    for i in range(max(entry_period, exit_period) + 1, len(df)):
        if pos == 0:
            if close.iloc[i] > upper.iloc[i]:
                pos = 1
        else:
            if close.iloc[i] < lower.iloc[i]:
                pos = 0
        signals.iloc[i] = pos
    return signals


# ── Strategy 2: Rate of Change (20) ─────────────────────────────────────────

def roc_signals(df, period):
    close = df["Close"]
    roc = (close - close.shift(period)) / close.shift(period) * 100
    roc_prev = roc.shift(1)

    signals = pd.Series(0, index=df.index)
    pos = 0
    for i in range(period + 2, len(df)):
        if pos == 0:
            # Buy when ROC > 0 and increasing
            if roc.iloc[i] > 0 and roc.iloc[i] > roc_prev.iloc[i]:
                pos = 1
        else:
            # Sell when ROC < 0
            if roc.iloc[i] < 0:
                pos = 0
        signals.iloc[i] = pos
    return signals


# ── Strategy 3: ADX(14) Trend ───────────────────────────────────────────────

def adx_signals(df, period=14):
    high = df["High"].values
    low = df["Low"].values
    close = df["Close"].values
    n = len(df)

    # Compute True Range, +DM, -DM
    tr_arr = np.zeros(n)
    plus_dm_arr = np.zeros(n)
    minus_dm_arr = np.zeros(n)

    for i in range(1, n):
        h_l = high[i] - low[i]
        h_pc = abs(high[i] - close[i - 1])
        l_pc = abs(low[i] - close[i - 1])
        tr_arr[i] = max(h_l, h_pc, l_pc)

        up_move = high[i] - high[i - 1]
        down_move = low[i - 1] - low[i]

        plus_dm_arr[i] = up_move if (up_move > down_move and up_move > 0) else 0.0
        minus_dm_arr[i] = down_move if (down_move > up_move and down_move > 0) else 0.0

    # Smooth with EMA
    tr_s = ema(pd.Series(tr_arr, index=df.index), period)
    plus_dm_s = ema(pd.Series(plus_dm_arr, index=df.index), period)
    minus_dm_s = ema(pd.Series(minus_dm_arr, index=df.index), period)

    # +DI, -DI
    plus_di = (plus_dm_s / tr_s) * 100
    minus_di = (minus_dm_s / tr_s) * 100

    # DX and ADX
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
    dx = dx.fillna(0)
    adx_line = ema(dx, period)

    signals = pd.Series(0, index=df.index)
    pos = 0
    start = period * 3  # allow indicators to warm up
    for i in range(start, n):
        if pos == 0:
            # Buy when ADX > 25 and +DI > -DI (strong uptrend)
            if adx_line.iloc[i] > 25 and plus_di.iloc[i] > minus_di.iloc[i]:
                pos = 1
        else:
            # Sell when +DI < -DI or ADX < 20
            if plus_di.iloc[i] < minus_di.iloc[i] or adx_line.iloc[i] < 20:
                pos = 0
        signals.iloc[i] = pos
    return signals


# ── Strategy 4: Keltner Channel (20, 2×ATR) ─────────────────────────────────

def keltner_signals(df, ema_period=20, atr_mult=2.0):
    close = df["Close"]
    mid = ema(close, ema_period)
    atr_val = atr(df, ema_period)
    upper = mid + atr_mult * atr_val

    signals = pd.Series(0, index=df.index)
    pos = 0
    start = ema_period + 1
    for i in range(start, len(df)):
        if pos == 0:
            # Buy when close breaks above upper channel
            if close.iloc[i] > upper.iloc[i]:
                pos = 1
        else:
            # Sell when close drops below middle line
            if close.iloc[i] < mid.iloc[i]:
                pos = 0
        signals.iloc[i] = pos
    return signals


# ── Strategy 5: Simple Dual Momentum (30/60 day) ────────────────────────────

def simple_momentum_signals(df, short_lb=30, long_lb=60):
    close = df["Close"]
    mom_short = close / close.shift(short_lb)   # 1-month momentum ratio
    mom_long = close / close.shift(long_lb)     # 2-month momentum ratio

    signals = pd.Series(0, index=df.index)
    pos = 0
    start = long_lb + 1
    for i in range(start, len(df)):
        if pos == 0:
            # Buy when close > close[30] AND close > close[60]
            if mom_short.iloc[i] > 1.0 and mom_long.iloc[i] > 1.0:
                pos = 1
        else:
            # Sell when close < close[30]
            if mom_short.iloc[i] < 1.0:
                pos = 0
        signals.iloc[i] = pos
    return signals


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    df = backtest_engine.load_data()
    print(f"Loaded {len(df)} bars from {df.index[0].date()} to {df.index[-1].date()}\n")

    strategies = [
        {
            "name": "Donchian Channel (20/10) - Turtle",
            "func": lambda d: donchian_signals(d, 20, 10),
            "params": {"entry_period": 20, "exit_period": 10},
        },
        {
            "name": "Donchian Channel (55/20)",
            "func": lambda d: donchian_signals(d, 55, 20),
            "params": {"entry_period": 55, "exit_period": 20},
        },
        {
            "name": "Rate of Change (20)",
            "func": lambda d: roc_signals(d, 20),
            "params": {"period": 20},
        },
        {
            "name": "ADX (14) Trend",
            "func": lambda d: adx_signals(d, 14),
            "params": {"period": 14, "adx_entry": 25, "adx_exit": 20},
        },
        {
            "name": "Keltner Channel (20, 2xATR)",
            "func": lambda d: keltner_signals(d, 20, 2.0),
            "params": {"ema_period": 20, "atr_mult": 2.0},
        },
        {
            "name": "Simple Momentum (30/60)",
            "func": lambda d: simple_momentum_signals(d, 30, 60),
            "params": {"short_lookback": 30, "long_lookback": 60},
        },
    ]

    results = []
    for strat in strategies:
        print(f"Running: {strat['name']} ... ", end="", flush=True)
        signals = strat["func"](df)
        result = backtest_engine.run_backtest(df, signals, strat["name"], strat["params"])
        results.append(result)
        print(f"Return: {result['total_return_pct']:+.2f}%  |  "
              f"Sharpe: {result['sharpe_ratio']:.2f}  |  "
              f"MaxDD: {result['max_drawdown_pct']:.2f}%  |  "
              f"Trades: {result['num_trades']}")

    # Save results
    output_path = "/home/user/repo/strategy_output/results_momentum.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # ── Summary Table ────────────────────────────────────────────────────────
    print("\n" + "=" * 100)
    print(f"{'Strategy':<35} {'Return%':>9} {'Ann.Ret%':>9} {'Sharpe':>8} "
          f"{'MaxDD%':>9} {'WinRate%':>9} {'PF':>8} {'Trades':>7} {'vsB&H%':>9}")
    print("-" * 100)
    for r in sorted(results, key=lambda x: x["total_return_pct"], reverse=True):
        print(f"{r['strategy']:<35} {r['total_return_pct']:>+9.2f} "
              f"{r['annualized_return_pct']:>+9.2f} {r['sharpe_ratio']:>8.2f} "
              f"{r['max_drawdown_pct']:>9.2f} {r['win_rate_pct']:>9.2f} "
              f"{r['profit_factor']:>8.2f} {r['num_trades']:>7d} "
              f"{r['excess_vs_buyhold_pct']:>+9.2f}")
    print("=" * 100)
    bh = results[0]["buy_hold_return_pct"]
    print(f"Buy & Hold BTC return over period: {bh:+.2f}%")
    best = max(results, key=lambda x: x["sharpe_ratio"])
    print(f"Best risk-adjusted (Sharpe): {best['strategy']} "
          f"(Sharpe={best['sharpe_ratio']:.2f}, Return={best['total_return_pct']:+.2f}%)")


if __name__ == "__main__":
    main()
