"""
RSI-based strategy variants backtested on BTC/USD 1-hour data.
Tests eight RSI configurations from classic mean-reversion to momentum and filtered approaches.
"""
import sys
import json
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Make sure the backtest engine is importable
# ---------------------------------------------------------------------------
sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine_1h as backtest_engine

# ---------------------------------------------------------------------------
# Indicator calculations
# ---------------------------------------------------------------------------

def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    """Wilder-style RSI using exponential smoothing."""
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - 100 / (1 + rs)
    return rsi


def compute_ema(close: pd.Series, period: int) -> pd.Series:
    """Exponential moving average."""
    return close.ewm(span=period, adjust=False).mean()


def compute_stoch_rsi(close: pd.Series, rsi_period: int = 14, stoch_period: int = 14) -> pd.Series:
    """Stochastic RSI: normalise RSI into 0-1 range over a rolling window."""
    rsi = compute_rsi(close, rsi_period)
    rsi_min = rsi.rolling(window=stoch_period).min()
    rsi_max = rsi.rolling(window=stoch_period).max()
    stoch_rsi = (rsi - rsi_min) / (rsi_max - rsi_min)
    return stoch_rsi


# ---------------------------------------------------------------------------
# Signal generators for each variant
# ---------------------------------------------------------------------------

def signals_rsi_mean_reversion(df, rsi_period=14, buy_thresh=30, sell_thresh=70):
    """Classic RSI mean-reversion: buy when oversold, sell when overbought."""
    rsi = compute_rsi(df["Close"], rsi_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        if not in_position and rsi.iloc[i] < buy_thresh:
            in_position = True
            signals.iloc[i] = 1
        elif in_position and rsi.iloc[i] > sell_thresh:
            in_position = False
            signals.iloc[i] = 0
        elif in_position:
            signals.iloc[i] = 1
    return signals


def signals_rsi_fast(df, rsi_period=7, buy_thresh=25, sell_thresh=75):
    """Fast RSI(7) mean-reversion with tighter thresholds."""
    rsi = compute_rsi(df["Close"], rsi_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        if not in_position and rsi.iloc[i] < buy_thresh:
            in_position = True
            signals.iloc[i] = 1
        elif in_position and rsi.iloc[i] > sell_thresh:
            in_position = False
            signals.iloc[i] = 0
        elif in_position:
            signals.iloc[i] = 1
    return signals


def signals_rsi_trend(df, rsi_period=14):
    """Trend-following: buy when RSI crosses above 50, sell when it crosses below 50."""
    rsi = compute_rsi(df["Close"], rsi_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(1, len(df)):
        prev_rsi = rsi.iloc[i - 1]
        curr_rsi = rsi.iloc[i]
        if not in_position and prev_rsi <= 50 and curr_rsi > 50:
            in_position = True
        elif in_position and prev_rsi >= 50 and curr_rsi < 50:
            in_position = False
        signals.iloc[i] = 1 if in_position else 0
    return signals


def signals_rsi_connors(df, rsi_period=2, buy_thresh=5, sell_thresh=95):
    """Connors RSI(2): extreme mean-reversion with very tight thresholds."""
    rsi = compute_rsi(df["Close"], rsi_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        if not in_position and rsi.iloc[i] < buy_thresh:
            in_position = True
            signals.iloc[i] = 1
        elif in_position and rsi.iloc[i] > sell_thresh:
            in_position = False
            signals.iloc[i] = 0
        elif in_position:
            signals.iloc[i] = 1
    return signals


def signals_rsi_ema50_filter(df, rsi_period=14, ema_period=50, buy_thresh=30, sell_thresh=70):
    """RSI mean-reversion with EMA(50) trend filter: buy RSI<30 only when price > EMA50."""
    rsi = compute_rsi(df["Close"], rsi_period)
    ema = compute_ema(df["Close"], ema_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        price = df["Close"].iloc[i]
        if not in_position and rsi.iloc[i] < buy_thresh and price > ema.iloc[i]:
            in_position = True
            signals.iloc[i] = 1
        elif in_position and rsi.iloc[i] > sell_thresh:
            in_position = False
            signals.iloc[i] = 0
        elif in_position:
            signals.iloc[i] = 1
    return signals


def signals_rsi_ema200_filter(df, rsi_period=14, ema_period=200, buy_thresh=30, sell_thresh=65):
    """RSI mean-reversion with EMA(200) trend filter: buy RSI<30 only when price > EMA200, sell RSI>65."""
    rsi = compute_rsi(df["Close"], rsi_period)
    ema = compute_ema(df["Close"], ema_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        price = df["Close"].iloc[i]
        if not in_position and rsi.iloc[i] < buy_thresh and price > ema.iloc[i]:
            in_position = True
            signals.iloc[i] = 1
        elif in_position and rsi.iloc[i] > sell_thresh:
            in_position = False
            signals.iloc[i] = 0
        elif in_position:
            signals.iloc[i] = 1
    return signals


def signals_stoch_rsi(df, rsi_period=14, stoch_period=14, buy_thresh=0.2, sell_thresh=0.8):
    """Stochastic RSI: buy when stochRSI < 0.2, sell when stochRSI > 0.8."""
    stoch_rsi = compute_stoch_rsi(df["Close"], rsi_period, stoch_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(len(df)):
        val = stoch_rsi.iloc[i]
        if pd.isna(val):
            continue
        if not in_position and val < buy_thresh:
            in_position = True
            signals.iloc[i] = 1
        elif in_position and val > sell_thresh:
            in_position = False
            signals.iloc[i] = 0
        elif in_position:
            signals.iloc[i] = 1
    return signals


def signals_rsi_momentum(df, rsi_period=6, buy_cross=60, sell_drop=40):
    """RSI(6) momentum ignition: buy when RSI crosses above 60, sell when it drops below 40."""
    rsi = compute_rsi(df["Close"], rsi_period)
    signals = pd.Series(0, index=df.index)
    in_position = False
    for i in range(1, len(df)):
        prev_rsi = rsi.iloc[i - 1]
        curr_rsi = rsi.iloc[i]
        if not in_position and prev_rsi <= buy_cross and curr_rsi > buy_cross:
            in_position = True
        elif in_position and curr_rsi < sell_drop:
            in_position = False
        signals.iloc[i] = 1 if in_position else 0
    return signals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 80)
    print("RSI Strategy Variant Backtest  --  BTC/USD 1-Hour Data")
    print("=" * 80)

    df = backtest_engine.load_data()
    print(f"Data loaded: {df.index[0]} to {df.index[-1]}  ({len(df)} bars)\n")

    # Define the eight strategy variants
    variants = [
        {
            "name": "RSI(14) Mean Reversion (30/70)",
            "params": {"rsi_period": 14, "buy_thresh": 30, "sell_thresh": 70},
            "gen": lambda d: signals_rsi_mean_reversion(d, 14, 30, 70),
        },
        {
            "name": "RSI(7) Fast (25/75)",
            "params": {"rsi_period": 7, "buy_thresh": 25, "sell_thresh": 75},
            "gen": lambda d: signals_rsi_fast(d, 7, 25, 75),
        },
        {
            "name": "RSI(14) Trend (50 crossover)",
            "params": {"rsi_period": 14, "crossover_level": 50},
            "gen": lambda d: signals_rsi_trend(d, 14),
        },
        {
            "name": "RSI(2) Connors (5/95)",
            "params": {"rsi_period": 2, "buy_thresh": 5, "sell_thresh": 95},
            "gen": lambda d: signals_rsi_connors(d, 2, 5, 95),
        },
        {
            "name": "RSI(14) + EMA(50) Filter (30/70)",
            "params": {"rsi_period": 14, "ema_period": 50,
                       "buy_thresh": 30, "sell_thresh": 70},
            "gen": lambda d: signals_rsi_ema50_filter(d, 14, 50, 30, 70),
        },
        {
            "name": "RSI(14) + EMA(200) Filter (30/65)",
            "params": {"rsi_period": 14, "ema_period": 200,
                       "buy_thresh": 30, "sell_thresh": 65},
            "gen": lambda d: signals_rsi_ema200_filter(d, 14, 200, 30, 65),
        },
        {
            "name": "Stoch RSI(14,14) (0.2/0.8)",
            "params": {"rsi_period": 14, "stoch_period": 14,
                       "buy_thresh": 0.2, "sell_thresh": 0.8},
            "gen": lambda d: signals_stoch_rsi(d, 14, 14, 0.2, 0.8),
        },
        {
            "name": "RSI(6) Momentum (60/40)",
            "params": {"rsi_period": 6, "buy_cross": 60, "sell_drop": 40},
            "gen": lambda d: signals_rsi_momentum(d, 6, 60, 40),
        },
    ]

    all_results = []

    for v in variants:
        print(f"  Testing: {v['name']} ...", end="", flush=True)
        sig = v["gen"](df)
        result = backtest_engine.run_backtest(df, sig, v["name"], v["params"])
        all_results.append(result)
        print(f"  {result['num_trades']} trades, "
              f"Return={result['total_return_pct']:.2f}%, "
              f"Sharpe={result['sharpe_ratio']:.2f}")

    # ------------------------------------------------------------------
    # Save results to JSON
    # ------------------------------------------------------------------
    output_path = "/home/user/repo/strategy_output/results_1h_rsi.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}\n")

    # ------------------------------------------------------------------
    # Print summary table
    # ------------------------------------------------------------------
    header = (f"{'Strategy':<38} {'Return%':>8} {'Ann%':>8} {'Sharpe':>7} "
              f"{'MaxDD%':>8} {'Trades':>7} {'WinR%':>7} {'PF':>7} "
              f"{'vs B&H%':>8}")
    print(header)
    print("-" * len(header))
    for r in all_results:
        print(f"{r['strategy']:<38} "
              f"{r['total_return_pct']:>8.2f} "
              f"{r['annualized_return_pct']:>8.2f} "
              f"{r['sharpe_ratio']:>7.2f} "
              f"{r['max_drawdown_pct']:>8.2f} "
              f"{r['num_trades']:>7d} "
              f"{r['win_rate_pct']:>7.2f} "
              f"{r['profit_factor']:>7.2f} "
              f"{r['excess_vs_buyhold_pct']:>8.2f}")
    print("-" * len(header))

    # Highlight best performers
    best_sharpe = max(all_results, key=lambda r: r["sharpe_ratio"])
    best_return = max(all_results, key=lambda r: r["total_return_pct"])
    best_winrate = max(all_results, key=lambda r: r["win_rate_pct"])
    least_dd = max(all_results, key=lambda r: r["max_drawdown_pct"])  # least negative

    print(f"\n  Best Sharpe:    {best_sharpe['strategy']:<38}  "
          f"Sharpe={best_sharpe['sharpe_ratio']:.2f}, "
          f"Return={best_sharpe['total_return_pct']:.2f}%")
    print(f"  Best Return:    {best_return['strategy']:<38}  "
          f"Return={best_return['total_return_pct']:.2f}%, "
          f"Sharpe={best_return['sharpe_ratio']:.2f}")
    print(f"  Best Win Rate:  {best_winrate['strategy']:<38}  "
          f"WinR={best_winrate['win_rate_pct']:.2f}%, "
          f"Trades={best_winrate['num_trades']}")
    print(f"  Least Drawdown: {least_dd['strategy']:<38}  "
          f"MaxDD={least_dd['max_drawdown_pct']:.2f}%")

    # Buy & hold reference
    bh = all_results[0]["buy_hold_return_pct"]
    print(f"\n  Buy & Hold return: {bh:.2f}%")
    beat_bh = [r for r in all_results if r["excess_vs_buyhold_pct"] > 0]
    print(f"  Strategies beating B&H: {len(beat_bh)} / {len(all_results)}")
    print("=" * 80)


if __name__ == "__main__":
    main()
