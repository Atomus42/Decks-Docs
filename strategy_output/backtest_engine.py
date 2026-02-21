"""
Shared backtesting engine for multi-strategy analysis.
Each strategy module imports this and calls run_backtest() with its signal function.
"""
import numpy as np
import pandas as pd
import json
import sys

DATA_PATH = "/home/user/repo/strategy_output/btc_3yr_candles.csv"
INITIAL_CAPITAL = 100_000.0
FEE_RATE = 0.0015  # 0.10% commission + 0.05% slippage

def load_data():
    df = pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)
    df.index.name = "Date"
    return df

def run_backtest(df, signals, strategy_name, params_dict=None):
    """
    Run a vectorized long-only backtest.

    Parameters:
        df: DataFrame with OHLCV data
        signals: Series aligned to df.index with values:
            1  = go long / hold long
            0  = flat / no position
            -1 = go short (treated as flat for long-only)
        strategy_name: string identifier
        params_dict: optional dict of parameters for logging

    Returns a dict with performance metrics.
    """
    signals = signals.reindex(df.index).fillna(0).astype(int)
    signals = signals.clip(lower=0, upper=1)  # long-only

    close = df["Close"].copy()
    n = len(close)

    # Detect position changes
    prev_signals = signals.shift(1).fillna(0).astype(int)
    entries = (signals == 1) & (prev_signals == 0)
    exits   = (signals == 0) & (prev_signals == 1)

    # Walk through trades
    equity = INITIAL_CAPITAL
    peak_equity = equity
    position = 0.0
    entry_price = 0.0
    trades = []
    equity_curve = []

    for i in range(n):
        date = df.index[i]
        price = close.iloc[i]
        sig = signals.iloc[i]
        prev_sig = prev_signals.iloc[i] if i > 0 else 0

        # Exit
        if prev_sig == 1 and sig == 0 and position > 0:
            exit_cost = price * position * FEE_RATE
            pnl = (price - entry_price) * position - exit_cost
            equity += pnl
            trades.append({"pnl": pnl, "entry": entry_price, "exit": price,
                          "ret_pct": (price / entry_price - 1) * 100})
            position = 0.0

        # Entry
        if prev_sig == 0 and sig == 1 and position == 0:
            entry_cost = price * FEE_RATE
            position = (equity * 0.95) / price  # use 95% of equity
            entry_price = price
            equity -= price * position * FEE_RATE

        # Mark to market
        unrealized = (price - entry_price) * position if position > 0 else 0
        total_eq = equity + unrealized
        peak_equity = max(peak_equity, total_eq)
        equity_curve.append(total_eq)

    # Close any open position at end
    if position > 0:
        price = close.iloc[-1]
        exit_cost = price * position * FEE_RATE
        pnl = (price - entry_price) * position - exit_cost
        equity += pnl
        trades.append({"pnl": pnl, "entry": entry_price, "exit": price,
                      "ret_pct": (price / entry_price - 1) * 100})
        equity_curve[-1] = equity

    # Compute metrics
    eq_series = pd.Series(equity_curve, index=df.index)
    daily_ret = eq_series.pct_change().dropna()

    total_return_pct = (eq_series.iloc[-1] / INITIAL_CAPITAL - 1) * 100
    days = (df.index[-1] - df.index[0]).days
    years = days / 365.25
    ann_return = ((1 + total_return_pct / 100) ** (1 / years) - 1) * 100 if years > 0 else 0

    sharpe = (daily_ret.mean() / daily_ret.std()) * np.sqrt(365) if daily_ret.std() > 0 else 0

    running_max = eq_series.cummax()
    drawdown = (eq_series - running_max) / running_max
    max_dd = drawdown.min() * 100

    n_trades = len(trades)
    wins = [t for t in trades if t["pnl"] > 0]
    losses = [t for t in trades if t["pnl"] <= 0]
    win_rate = len(wins) / n_trades * 100 if n_trades > 0 else 0

    gross_profit = sum(t["pnl"] for t in wins) if wins else 0
    gross_loss = abs(sum(t["pnl"] for t in losses)) if losses else 0
    profit_factor = gross_profit / gross_loss if gross_loss > 0 else float("inf")

    avg_win_pct = np.mean([t["ret_pct"] for t in wins]) if wins else 0
    avg_loss_pct = np.mean([t["ret_pct"] for t in losses]) if losses else 0

    # Buy & hold benchmark
    bh_return = (close.iloc[-1] / close.iloc[0] - 1) * 100

    result = {
        "strategy": strategy_name,
        "params": params_dict or {},
        "total_return_pct": round(total_return_pct, 2),
        "annualized_return_pct": round(ann_return, 2),
        "sharpe_ratio": round(sharpe, 2),
        "max_drawdown_pct": round(max_dd, 2),
        "num_trades": n_trades,
        "win_rate_pct": round(win_rate, 2),
        "profit_factor": round(profit_factor, 2) if profit_factor != float("inf") else 999.99,
        "avg_win_pct": round(avg_win_pct, 2),
        "avg_loss_pct": round(avg_loss_pct, 2),
        "final_equity": round(eq_series.iloc[-1], 2),
        "buy_hold_return_pct": round(bh_return, 2),
        "excess_vs_buyhold_pct": round(total_return_pct - bh_return, 2),
    }
    return result
