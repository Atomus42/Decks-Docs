"""
RSI-based strategy variants backtested on BTC/USD daily data.
Tests six RSI configurations from classic mean-reversion to trend-following.
"""
import sys
import json
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Make sure the backtest engine is importable
# ---------------------------------------------------------------------------
sys.path.insert(0, "/home/user/repo/strategy_output")
import backtest_engine

# ---------------------------------------------------------------------------
# RSI calculation (Wilder-style exponential smoothing)
# ---------------------------------------------------------------------------
def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - 100 / (1 + rs)
    return rsi


def compute_ema(close: pd.Series, period: int) -> pd.Series:
    return close.ewm(span=period, adjust=False).mean()


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


def signals_rsi_trend_following(df, rsi_period=14):
    """Trend-following: buy when RSI crosses above 50, sell when crosses below."""
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


def signals_rsi_ema_filter(df, rsi_period=14, ema_period=50, buy_thresh=30, sell_thresh=70):
    """RSI mean-reversion with EMA trend filter: only buy when price > EMA."""
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("RSI Strategy Variant Backtest  --  BTC/USD Daily")
    print("=" * 72)

    df = backtest_engine.load_data()
    print(f"Data loaded: {df.index[0].date()} to {df.index[-1].date()}  "
          f"({len(df)} bars)\n")

    # Define the six strategy variants
    variants = [
        {
            "name": "RSI(14) Mean Reversion (30/70)",
            "params": {"rsi_period": 14, "buy_thresh": 30, "sell_thresh": 70},
            "gen": lambda d: signals_rsi_mean_reversion(d, 14, 30, 70),
        },
        {
            "name": "RSI(14) Mean Reversion Tight (25/75)",
            "params": {"rsi_period": 14, "buy_thresh": 25, "sell_thresh": 75},
            "gen": lambda d: signals_rsi_mean_reversion(d, 14, 25, 75),
        },
        {
            "name": "RSI(7) Fast Mean Reversion (20/80)",
            "params": {"rsi_period": 7, "buy_thresh": 20, "sell_thresh": 80},
            "gen": lambda d: signals_rsi_mean_reversion(d, 7, 20, 80),
        },
        {
            "name": "RSI(14) Trend Following (50 crossover)",
            "params": {"rsi_period": 14, "crossover_level": 50},
            "gen": lambda d: signals_rsi_trend_following(d, 14),
        },
        {
            "name": "RSI(14) + EMA(50) Filter (30/70)",
            "params": {"rsi_period": 14, "ema_period": 50,
                       "buy_thresh": 30, "sell_thresh": 70},
            "gen": lambda d: signals_rsi_ema_filter(d, 14, 50, 30, 70),
        },
        {
            "name": "RSI(2) Connors Style (10/90)",
            "params": {"rsi_period": 2, "buy_thresh": 10, "sell_thresh": 90},
            "gen": lambda d: signals_rsi_mean_reversion(d, 2, 10, 90),
        },
    ]

    all_results = []

    for v in variants:
        sig = v["gen"](df)
        result = backtest_engine.run_backtest(df, sig, v["name"], v["params"])
        all_results.append(result)

    # ------------------------------------------------------------------
    # Save results to JSON
    # ------------------------------------------------------------------
    output_path = "/home/user/repo/strategy_output/results_rsi.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"Results saved to {output_path}\n")

    # ------------------------------------------------------------------
    # Print summary table
    # ------------------------------------------------------------------
    header = (f"{'Strategy':<42} {'Return%':>8} {'Ann%':>7} {'Sharpe':>7} "
              f"{'MaxDD%':>8} {'Trades':>7} {'WinR%':>7} {'PF':>7} "
              f"{'vs B&H%':>8}")
    print(header)
    print("-" * len(header))
    for r in all_results:
        print(f"{r['strategy']:<42} "
              f"{r['total_return_pct']:>8.2f} "
              f"{r['annualized_return_pct']:>7.2f} "
              f"{r['sharpe_ratio']:>7.2f} "
              f"{r['max_drawdown_pct']:>8.2f} "
              f"{r['num_trades']:>7d} "
              f"{r['win_rate_pct']:>7.2f} "
              f"{r['profit_factor']:>7.2f} "
              f"{r['excess_vs_buyhold_pct']:>8.2f}")
    print("-" * len(header))

    # Highlight best by Sharpe
    best = max(all_results, key=lambda r: r["sharpe_ratio"])
    print(f"\nBest Sharpe: {best['strategy']}  "
          f"(Sharpe={best['sharpe_ratio']:.2f}, "
          f"Return={best['total_return_pct']:.2f}%)")

    # Buy & hold reference
    bh = all_results[0]["buy_hold_return_pct"]
    print(f"Buy & Hold return: {bh:.2f}%")
    print("=" * 72)


if __name__ == "__main__":
    main()
