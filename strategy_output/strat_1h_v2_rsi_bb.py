"""
RSI-as-Trend + Bollinger Band strategies for 1H BTC/USD.
Design goal: MAX RETURNS using RSI as a TREND tool (not mean-reversion),
combined with slow Bollinger Band breakouts. Fewer, higher-conviction trades.
"""
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine_1h_v2 as backtest_engine

# ── helpers ──────────────────────────────────────────────────────────────────

def compute_rsi(close, period=14):
    """Manual RSI using exponential weighted moving average."""
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - 100 / (1 + rs)
    return rsi


def compute_ema(close, span):
    return close.ewm(span=span, adjust=False).mean()


def compute_bb(close, period, num_std):
    """Bollinger Bands: middle = SMA, upper/lower = middle +/- num_std * std."""
    middle = close.rolling(window=period).mean()
    std = close.rolling(window=period).std()
    upper = middle + num_std * std
    lower = middle - num_std * std
    return middle, upper, lower


# ── load data ────────────────────────────────────────────────────────────────

df = backtest_engine.load_data()
close = df["Close"]

# ── pre-compute indicators ───────────────────────────────────────────────────

rsi_14 = compute_rsi(close, 14)
rsi_24 = compute_rsi(close, 24)
rsi_48 = compute_rsi(close, 48)

ema_200 = compute_ema(close, 200)

bb100_mid, bb100_upper, bb100_lower = compute_bb(close, 100, 2.0)
bb200_mid, bb200_upper, bb200_lower = compute_bb(close, 200, 1.5)

# ── strategies ───────────────────────────────────────────────────────────────

results = []

# (a) RSI(24) trend: long when RSI > 50, flat when RSI < 50
signals_a = (rsi_24 > 50).astype(int)
res = backtest_engine.run_backtest(df, signals_a, "RSI(24) Trend",
                                   {"period": 24, "threshold": 50})
results.append(res)

# (b) RSI(48) trend: even slower, long when > 50, flat when < 50
signals_b = (rsi_48 > 50).astype(int)
res = backtest_engine.run_backtest(df, signals_b, "RSI(48) Trend",
                                   {"period": 48, "threshold": 50})
results.append(res)

# (c) RSI(24) + EMA(200) filter: long when RSI(24) > 50 AND close > EMA200.
#     Exit only when BOTH conditions fail.
enter_c = (rsi_24 > 50) & (close > ema_200)
exit_c = (rsi_24 < 50) & (close < ema_200)
signals_c = pd.Series(0, index=df.index)
pos = 0
for i in range(len(df)):
    if pos == 0 and enter_c.iloc[i]:
        pos = 1
    elif pos == 1 and exit_c.iloc[i]:
        pos = 0
    signals_c.iloc[i] = pos
res = backtest_engine.run_backtest(df, signals_c, "RSI(24) + EMA(200) Filter",
                                   {"rsi_period": 24, "ema_span": 200,
                                    "enter": "RSI>50 & close>EMA200",
                                    "exit": "RSI<50 & close<EMA200"})
results.append(res)

# (d) RSI(14) momentum band: long when RSI > 55, exit when RSI < 40
signals_d = pd.Series(0, index=df.index)
pos = 0
for i in range(len(df)):
    if pos == 0 and rsi_14.iloc[i] > 55:
        pos = 1
    elif pos == 1 and rsi_14.iloc[i] < 40:
        pos = 0
    signals_d.iloc[i] = pos
res = backtest_engine.run_backtest(df, signals_d, "RSI(14) Momentum Band",
                                   {"period": 14, "entry_threshold": 55,
                                    "exit_threshold": 40})
results.append(res)

# (e) RSI(14) momentum + EMA(200): same as (d) but only enter when close > EMA200
signals_e = pd.Series(0, index=df.index)
pos = 0
for i in range(len(df)):
    if pos == 0 and rsi_14.iloc[i] > 55 and close.iloc[i] > ema_200.iloc[i]:
        pos = 1
    elif pos == 1 and rsi_14.iloc[i] < 40:
        pos = 0
    signals_e.iloc[i] = pos
res = backtest_engine.run_backtest(df, signals_e, "RSI(14) Momentum + EMA(200)",
                                   {"rsi_period": 14, "entry_threshold": 55,
                                    "exit_threshold": 40, "ema_span": 200})
results.append(res)

# (f) BB(100,2) slow breakout: long when close > upper band, exit when close < middle
signals_f = pd.Series(0, index=df.index)
pos = 0
for i in range(len(df)):
    if pd.isna(bb100_upper.iloc[i]):
        signals_f.iloc[i] = 0
        continue
    if pos == 0 and close.iloc[i] > bb100_upper.iloc[i]:
        pos = 1
    elif pos == 1 and close.iloc[i] < bb100_mid.iloc[i]:
        pos = 0
    signals_f.iloc[i] = pos
res = backtest_engine.run_backtest(df, signals_f, "BB(100,2) Slow Breakout",
                                   {"bb_period": 100, "bb_std": 2.0,
                                    "enter": "close > upper", "exit": "close < middle"})
results.append(res)

# (g) BB(200,1.5) ultra-slow + trend: long when close > upper AND close > EMA200,
#     exit when close < middle band
signals_g = pd.Series(0, index=df.index)
pos = 0
for i in range(len(df)):
    if pd.isna(bb200_upper.iloc[i]):
        signals_g.iloc[i] = 0
        continue
    if pos == 0 and close.iloc[i] > bb200_upper.iloc[i] and close.iloc[i] > ema_200.iloc[i]:
        pos = 1
    elif pos == 1 and close.iloc[i] < bb200_mid.iloc[i]:
        pos = 0
    signals_g.iloc[i] = pos
res = backtest_engine.run_backtest(df, signals_g, "BB(200,1.5) Ultra-Slow + Trend",
                                   {"bb_period": 200, "bb_std": 1.5, "ema_span": 200,
                                    "enter": "close > BB_upper & close > EMA200",
                                    "exit": "close < BB_middle"})
results.append(res)

# (h) RSI(24) + BB(100,2) combo: long when RSI(24) > 50 AND close > BB middle.
#     Exit when RSI < 45 OR close < BB lower band.
signals_h = pd.Series(0, index=df.index)
pos = 0
for i in range(len(df)):
    if pd.isna(bb100_mid.iloc[i]):
        signals_h.iloc[i] = 0
        continue
    if pos == 0 and rsi_24.iloc[i] > 50 and close.iloc[i] > bb100_mid.iloc[i]:
        pos = 1
    elif pos == 1 and (rsi_24.iloc[i] < 45 or close.iloc[i] < bb100_lower.iloc[i]):
        pos = 0
    signals_h.iloc[i] = pos
res = backtest_engine.run_backtest(df, signals_h, "RSI(24) + BB(100,2) Combo",
                                   {"rsi_period": 24, "bb_period": 100, "bb_std": 2.0,
                                    "enter": "RSI>50 & close>BB_mid",
                                    "exit": "RSI<45 | close<BB_lower"})
results.append(res)

# ── save results ─────────────────────────────────────────────────────────────

output_path = "/home/user/repo/strategy_output/results_1h_v2_rsi_bb.json"
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

# ── print summary ────────────────────────────────────────────────────────────

print("=" * 110)
print(f"{'Strategy':<38} {'Return%':>9} {'Ann%':>8} {'Sharpe':>7} {'MaxDD%':>8} "
      f"{'Trades':>7} {'WinR%':>7} {'PF':>7} {'vsB&H%':>8}")
print("-" * 110)

for r in sorted(results, key=lambda x: x["total_return_pct"], reverse=True):
    print(f"{r['strategy']:<38} {r['total_return_pct']:>9.2f} {r['annualized_return_pct']:>8.2f} "
          f"{r['sharpe_ratio']:>7.2f} {r['max_drawdown_pct']:>8.2f} "
          f"{r['num_trades']:>7} {r['win_rate_pct']:>7.2f} {r['profit_factor']:>7.2f} "
          f"{r['excess_vs_buyhold_pct']:>8.2f}")

print("=" * 110)
print(f"\nBuy & Hold return: {results[0]['buy_hold_return_pct']:.2f}%")
print(f"Results saved to: {output_path}")
best = max(results, key=lambda x: x["total_return_pct"])
print(f"\nBest strategy: {best['strategy']} -- {best['total_return_pct']:.2f}% total return, "
      f"Sharpe {best['sharpe_ratio']:.2f}, {best['num_trades']} trades")
