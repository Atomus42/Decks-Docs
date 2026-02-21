#!/usr/bin/env python3
"""
BTC/USD Trading Strategy with Central Bank Announcement Avoidance
=================================================================

A data-driven trend-following strategy that systematically exits positions
during major central bank events (FOMC, ECB, BOE, BOJ) to avoid
unpredictable volatility injections.

Strategy rationale:
- BTC exhibits strong momentum/trend behavior due to reflexive retail flows
  and narrative-driven positioning. Trend-following captures this well.
- We use a dual moving average crossover (fast EMA / slow EMA) as the core
  signal. EMAs weight recent prices more heavily, making them responsive to
  BTC's fast regime changes while filtering daily noise.
- ATR-based stop-losses adapt to BTC's highly variable volatility regimes
  (e.g., 2% daily moves in quiet periods vs 10%+ in crisis periods).
- A max-drawdown circuit breaker halts trading after catastrophic losses,
  protecting capital during black-swan events.
- The central bank exclusion window flattens positions around announcements,
  avoiding the binary-event gamma that crypto markets increasingly absorb
  from macro traders.

Author: Claude
Date: 2026-02-21
"""

import warnings
warnings.filterwarnings("ignore")

import os
import sys
import datetime as dt
from typing import Optional

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for server environments
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

# ============================================================================
# TUNABLE PARAMETERS — edit these to configure the strategy
# ============================================================================

PARAMS = {
    # --- Data ---
    "ticker":           "BTC-USD",
    "start_date":       "2022-01-01",       # backtest start (YYYY-MM-DD)
    "end_date":         "2025-12-31",       # backtest end   (YYYY-MM-DD)

    # --- Trend signal ---
    "fast_ema_period":  21,                 # fast EMA lookback (days)
    "slow_ema_period":  55,                 # slow EMA lookback (days)
    # Why 21/55: BTC trends persist on ~monthly cycles. 21 ≈ 1 trading month,
    # 55 ≈ 1 quarter. This pair balances responsiveness vs whipsaw filtering.

    # --- Risk management ---
    "atr_period":       14,                 # ATR lookback for stop-loss
    "atr_stop_mult":    2.5,               # stop-loss = entry - ATR * mult
    # Why 2.5x ATR: BTC daily ranges are wide; tighter stops get stopped out
    # by noise. 2.5x gives room for normal pullbacks while cutting real losses.
    "risk_per_trade":   0.02,              # risk 2% of equity per trade
    "max_drawdown_pct": 0.20,             # halt trading after 20% peak DD
    "trailing_stop":    True,              # use trailing stop (vs fixed)

    # --- Central bank exclusion ---
    "cb_exclusion_enabled": True,          # toggle the CB filter on/off
    "cb_window_before": 1,                 # flatten positions T-N days before
    "cb_window_after":  1,                 # stay flat T+N days after
    # Covers the pre-announcement positioning unwind and post-announcement
    # volatility spike. T-1 to T+1 is the minimum effective window.

    # --- Execution ---
    "trading_fee_pct":  0.001,             # 0.10% per trade (taker fee)
    "slippage_pct":     0.0005,            # 0.05% slippage estimate

    # --- Output ---
    "output_dir":       "strategy_output", # directory for CSVs and charts
}


# ============================================================================
# CENTRAL BANK CALENDAR
# ============================================================================

def build_central_bank_calendar() -> pd.DatetimeIndex:
    """
    Returns a DatetimeIndex of major central bank rate decision dates.
    Covers FOMC, ECB, BOE, and BOJ from 2022 through 2025.

    Sources: Federal Reserve, ECB, Bank of England, Bank of Japan published
    meeting schedules. These are the announcement/decision dates.
    """

    # --- FOMC (Fed) scheduled rate decisions ---
    fomc = [
        # 2022
        "2022-01-26", "2022-03-16", "2022-05-04", "2022-06-15",
        "2022-07-27", "2022-09-21", "2022-11-02", "2022-12-14",
        # 2023
        "2023-02-01", "2023-03-22", "2023-05-03", "2023-06-14",
        "2023-07-26", "2023-09-20", "2023-11-01", "2023-12-13",
        # 2024
        "2024-01-31", "2024-03-20", "2024-05-01", "2024-06-12",
        "2024-07-31", "2024-09-18", "2024-11-07", "2024-12-18",
        # 2025
        "2025-01-29", "2025-03-19", "2025-05-07", "2025-06-18",
        "2025-07-30", "2025-09-17", "2025-10-29", "2025-12-17",
    ]

    # --- ECB rate decisions ---
    ecb = [
        # 2022
        "2022-02-03", "2022-03-10", "2022-04-14", "2022-06-09",
        "2022-07-21", "2022-09-08", "2022-10-27", "2022-12-15",
        # 2023
        "2023-02-02", "2023-03-16", "2023-05-04", "2023-06-15",
        "2023-07-27", "2023-09-14", "2023-10-26", "2023-12-14",
        # 2024
        "2024-01-25", "2024-03-07", "2024-04-11", "2024-06-06",
        "2024-07-18", "2024-09-12", "2024-10-17", "2024-12-12",
        # 2025
        "2025-01-30", "2025-03-06", "2025-04-17", "2025-06-05",
        "2025-07-24", "2025-09-11", "2025-10-30", "2025-12-18",
    ]

    # --- Bank of England rate decisions ---
    boe = [
        # 2022
        "2022-02-03", "2022-03-17", "2022-05-05", "2022-06-16",
        "2022-08-04", "2022-09-22", "2022-11-03", "2022-12-15",
        # 2023
        "2023-02-02", "2023-03-23", "2023-05-11", "2023-06-22",
        "2023-08-03", "2023-09-21", "2023-11-02", "2023-12-14",
        # 2024
        "2024-02-01", "2024-03-21", "2024-05-09", "2024-06-20",
        "2024-08-01", "2024-09-19", "2024-11-07", "2024-12-19",
        # 2025
        "2025-02-06", "2025-03-20", "2025-05-08", "2025-06-19",
        "2025-08-07", "2025-09-18", "2025-11-06", "2025-12-18",
    ]

    # --- Bank of Japan rate decisions ---
    boj = [
        # 2022
        "2022-01-18", "2022-03-18", "2022-04-28", "2022-06-17",
        "2022-07-21", "2022-09-22", "2022-10-28", "2022-12-20",
        # 2023
        "2023-01-18", "2023-03-10", "2023-04-28", "2023-06-16",
        "2023-07-28", "2023-09-22", "2023-10-31", "2023-12-19",
        # 2024
        "2024-01-23", "2024-03-19", "2024-04-26", "2024-06-14",
        "2024-07-31", "2024-09-20", "2024-10-31", "2024-12-19",
        # 2025
        "2025-01-24", "2025-03-14", "2025-05-01", "2025-06-17",
        "2025-07-31", "2025-09-19", "2025-10-30", "2025-12-19",
    ]

    all_dates = fomc + ecb + boe + boj
    parsed = pd.to_datetime(all_dates)
    return parsed.sort_values().unique()


def build_exclusion_mask(dates: pd.DatetimeIndex,
                         cb_dates: pd.DatetimeIndex,
                         window_before: int,
                         window_after: int) -> pd.Series:
    """
    Returns a boolean Series (index=dates) that is True on days that fall
    within the exclusion window around any central bank event.
    """
    mask = pd.Series(False, index=dates)
    for cb_date in cb_dates:
        start = cb_date - pd.Timedelta(days=window_before)
        end = cb_date + pd.Timedelta(days=window_after)
        mask |= (dates >= start) & (dates <= end)
    return mask


# ============================================================================
# DATA FETCHING
# ============================================================================

def fetch_btc_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch daily OHLCV data via yfinance.
    Falls back to sample data generation if yfinance is unavailable.
    """
    try:
        import yfinance as yf
        print(f"Fetching {ticker} data from {start} to {end} via yfinance...")
        # Add buffer for indicator warm-up
        warmup_start = (pd.Timestamp(start) - pd.Timedelta(days=120)).strftime("%Y-%m-%d")
        df = yf.download(ticker, start=warmup_start, end=end, auto_adjust=True, progress=False)
        if df.empty:
            raise ValueError("yfinance returned empty DataFrame")
        # Flatten multi-level columns if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df.index = pd.DatetimeIndex(df.index)
        df.index.name = "Date"
        print(f"  Loaded {len(df)} daily bars ({df.index[0].date()} to {df.index[-1].date()})")
        return df
    except Exception as e:
        print(f"yfinance fetch failed ({e}). Generating synthetic data for demonstration.")
        return _generate_synthetic_btc(start, end)


def _generate_synthetic_btc(start: str, end: str) -> pd.DataFrame:
    """Generate plausible synthetic BTC daily OHLCV for offline testing."""
    warmup_start = (pd.Timestamp(start) - pd.Timedelta(days=120)).strftime("%Y-%m-%d")
    dates = pd.bdate_range(warmup_start, end)
    np.random.seed(42)
    n = len(dates)
    # Geometric Brownian Motion with BTC-like params
    mu = 0.0003   # slight upward drift
    sigma = 0.035  # ~3.5% daily vol
    returns = np.random.normal(mu, sigma, n)
    price = 45000.0 * np.exp(np.cumsum(returns))
    high = price * (1 + np.abs(np.random.normal(0, 0.015, n)))
    low = price * (1 - np.abs(np.random.normal(0, 0.015, n)))
    open_ = low + (high - low) * np.random.uniform(0.3, 0.7, n)
    volume = np.random.lognormal(mean=23, sigma=0.5, size=n)
    df = pd.DataFrame({
        "Open": open_, "High": high, "Low": low, "Close": price, "Volume": volume
    }, index=dates)
    df.index.name = "Date"
    print(f"  Generated {len(df)} synthetic bars ({df.index[0].date()} to {df.index[-1].date()})")
    return df


# ============================================================================
# INDICATORS
# ============================================================================

def compute_indicators(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """Compute EMAs, ATR, and signal columns."""
    df = df.copy()

    # Exponential moving averages
    df["EMA_fast"] = df["Close"].ewm(span=params["fast_ema_period"], adjust=False).mean()
    df["EMA_slow"] = df["Close"].ewm(span=params["slow_ema_period"], adjust=False).mean()

    # Average True Range (Wilder's method)
    high = df["High"]
    low = df["Low"]
    prev_close = df["Close"].shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    df["ATR"] = tr.ewm(span=params["atr_period"], adjust=False).mean()

    # Trend signal: 1 = bullish (fast > slow), 0 = bearish
    df["signal"] = (df["EMA_fast"] > df["EMA_slow"]).astype(int)

    return df


# ============================================================================
# BACKTESTER
# ============================================================================

def backtest(df: pd.DataFrame, params: dict, use_cb_filter: bool) -> pd.DataFrame:
    """
    Event-driven backtest loop.

    Position sizing: each trade risks `risk_per_trade` fraction of current
    equity. The number of BTC units is sized so that if the stop-loss is hit,
    the loss equals that risk amount. This ensures consistent risk across
    varying volatility regimes.

    Returns a DataFrame of trade-level results plus an equity series.
    """
    # Trim to backtest period (indicators need warm-up bars before start_date)
    start_ts = pd.Timestamp(params["start_date"])
    mask = df.index >= start_ts
    if mask.sum() == 0:
        print("ERROR: no data in backtest range.")
        sys.exit(1)

    # Central bank filter
    cb_dates = build_central_bank_calendar()
    exclusion = build_exclusion_mask(
        df.index, cb_dates,
        params["cb_window_before"], params["cb_window_after"]
    )

    fee_rate = params["trading_fee_pct"] + params["slippage_pct"]
    risk_frac = params["risk_per_trade"]
    atr_mult = params["atr_stop_mult"]
    max_dd = params["max_drawdown_pct"]
    trailing = params["trailing_stop"]

    # State
    equity = 100_000.0  # starting capital in USD
    peak_equity = equity
    position = 0.0       # BTC units held (0 = flat, >0 = long)
    entry_price = 0.0
    entry_date = None     # date of current open trade
    stop_price = 0.0
    highest_since_entry = 0.0
    circuit_breaker_active = False

    # Records
    equity_curve = []
    trades = []          # completed trades only (entry+exit pairs)
    daily_log = []

    for i in range(len(df)):
        date = df.index[i]
        in_backtest = date >= start_ts
        close = df["Close"].iloc[i]
        high = df["High"].iloc[i]
        low = df["Low"].iloc[i]
        atr = df["ATR"].iloc[i]
        sig = df["signal"].iloc[i]
        is_excluded = exclusion.iloc[i] if use_cb_filter else False

        if not in_backtest:
            continue

        action = "hold"
        trade_pnl = 0.0

        # --- Circuit breaker check ---
        drawdown = (peak_equity - equity) / peak_equity if peak_equity > 0 else 0
        if drawdown >= max_dd and not circuit_breaker_active:
            circuit_breaker_active = True
            # Force close any open position
            if position > 0:
                exit_cost = close * position * fee_rate
                trade_pnl = (close - entry_price) * position - exit_cost
                equity += trade_pnl
                trades.append({
                    "entry_date": entry_date, "entry_price": entry_price,
                    "exit_date": date, "exit_price": close,
                    "size": position, "pnl": trade_pnl,
                    "reason": "circuit_breaker",
                })
                position = 0.0
                entry_date = None
                action = "cb_exit"

        if circuit_breaker_active:
            equity_curve.append({"Date": date, "equity": equity})
            daily_log.append({
                "Date": date, "Close": close, "signal": sig,
                "excluded": is_excluded, "position": position,
                "equity": equity, "action": "circuit_breaker_halt",
            })
            continue

        # --- Check stop-loss (intraday using Low) ---
        if position > 0 and low <= stop_price:
            # Stopped out — assume fill at stop price
            fill = stop_price
            exit_cost = fill * position * fee_rate
            trade_pnl = (fill - entry_price) * position - exit_cost
            equity += trade_pnl
            trades.append({
                "entry_date": entry_date, "entry_price": entry_price,
                "exit_date": date, "exit_price": fill,
                "size": position, "pnl": trade_pnl,
                "reason": "stop_loss",
            })
            position = 0.0
            entry_date = None
            action = "stop_exit"

        # --- Update trailing stop ---
        if position > 0 and trailing:
            if high > highest_since_entry:
                highest_since_entry = high
                new_stop = highest_since_entry - atr * atr_mult
                if new_stop > stop_price:
                    stop_price = new_stop

        # --- Exclusion window: flatten if in excluded zone ---
        if position > 0 and is_excluded and action == "hold":
            exit_cost = close * position * fee_rate
            trade_pnl = (close - entry_price) * position - exit_cost
            equity += trade_pnl
            trades.append({
                "entry_date": entry_date, "entry_price": entry_price,
                "exit_date": date, "exit_price": close,
                "size": position, "pnl": trade_pnl,
                "reason": "cb_exclusion",
            })
            position = 0.0
            entry_date = None
            action = "cb_flat"

        # --- Signal-based exits: trend reversal ---
        if position > 0 and sig == 0 and action == "hold":
            exit_cost = close * position * fee_rate
            trade_pnl = (close - entry_price) * position - exit_cost
            equity += trade_pnl
            trades.append({
                "entry_date": entry_date, "entry_price": entry_price,
                "exit_date": date, "exit_price": close,
                "size": position, "pnl": trade_pnl,
                "reason": "signal_exit",
            })
            position = 0.0
            entry_date = None
            action = "signal_exit"

        # --- Entries ---
        if position == 0 and sig == 1 and not is_excluded and action in ("hold", "stop_exit"):
            if atr > 0 and equity > 0:
                risk_amount = equity * risk_frac
                stop_dist = atr * atr_mult
                size = risk_amount / stop_dist  # BTC units
                cost = close * size * fee_rate
                if close * size + cost < equity:
                    entry_price = close
                    entry_date = date
                    stop_price = close - stop_dist
                    highest_since_entry = close
                    position = size
                    equity -= cost  # entry fee
                    action = "entry"

        # Update peak equity (including unrealized)
        unrealized = (close - entry_price) * position if position > 0 else 0
        total_equity = equity + unrealized
        peak_equity = max(peak_equity, total_equity)

        equity_curve.append({"Date": date, "equity": total_equity})
        daily_log.append({
            "Date": date, "Close": close, "signal": sig,
            "excluded": is_excluded, "position": position,
            "equity": total_equity, "action": action,
        })

    # Close any open position at end of backtest
    if position > 0:
        last_close = df["Close"].iloc[-1]
        exit_cost = last_close * position * fee_rate
        trade_pnl = (last_close - entry_price) * position - exit_cost
        equity += trade_pnl
        trades.append({
            "entry_date": entry_date, "entry_price": entry_price,
            "exit_date": df.index[-1], "exit_price": last_close,
            "size": position, "pnl": trade_pnl,
            "reason": "end_of_backtest",
        })

    eq_df = pd.DataFrame(equity_curve).set_index("Date")
    log_df = pd.DataFrame(daily_log).set_index("Date")
    trades_df = pd.DataFrame(trades)

    return eq_df, log_df, trades_df


# ============================================================================
# PERFORMANCE METRICS
# ============================================================================

def compute_metrics(eq_df: pd.DataFrame, trades_df: pd.DataFrame,
                    start_equity: float = 100_000.0) -> dict:
    """Compute standard strategy performance metrics."""
    if eq_df.empty:
        return {}

    final_equity = eq_df["equity"].iloc[-1]
    total_return = (final_equity / start_equity) - 1

    # Annualized return
    days = (eq_df.index[-1] - eq_df.index[0]).days
    years = days / 365.25
    ann_return = (1 + total_return) ** (1 / years) - 1 if years > 0 else 0

    # Daily returns for Sharpe
    daily_ret = eq_df["equity"].pct_change().dropna()
    sharpe = (daily_ret.mean() / daily_ret.std()) * np.sqrt(365) if daily_ret.std() > 0 else 0

    # Max drawdown
    running_max = eq_df["equity"].cummax()
    drawdown = (eq_df["equity"] - running_max) / running_max
    max_dd = drawdown.min()

    # Trade stats
    n_trades = len(trades_df)
    if n_trades > 0:
        wins = trades_df[trades_df["pnl"] > 0]
        losses = trades_df[trades_df["pnl"] <= 0]
        win_rate = len(wins) / n_trades
        gross_profit = wins["pnl"].sum() if len(wins) > 0 else 0
        gross_loss = abs(losses["pnl"].sum()) if len(losses) > 0 else 0
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else float("inf")
        avg_win = wins["pnl"].mean() if len(wins) > 0 else 0
        avg_loss = losses["pnl"].mean() if len(losses) > 0 else 0
    else:
        win_rate = profit_factor = avg_win = avg_loss = 0

    return {
        "Total Return":       f"{total_return:.2%}",
        "Annualized Return":  f"{ann_return:.2%}",
        "Sharpe Ratio":       f"{sharpe:.2f}",
        "Max Drawdown":       f"{max_dd:.2%}",
        "# Trades":           n_trades,
        "Win Rate":           f"{win_rate:.2%}",
        "Profit Factor":      f"{profit_factor:.2f}",
        "Avg Win":            f"${avg_win:,.2f}",
        "Avg Loss":           f"${avg_loss:,.2f}",
        "Final Equity":       f"${final_equity:,.2f}",
    }


# ============================================================================
# VISUALIZATION
# ============================================================================

def plot_results(df: pd.DataFrame, log_filtered: pd.DataFrame,
                 log_unfiltered: pd.DataFrame, eq_filtered: pd.DataFrame,
                 eq_unfiltered: pd.DataFrame, params: dict,
                 cb_dates: pd.DatetimeIndex, output_dir: str):
    """Generate all charts and save to output_dir."""

    start_ts = pd.Timestamp(params["start_date"])
    plot_df = df[df.index >= start_ts].copy()

    fig, axes = plt.subplots(4, 1, figsize=(18, 22), gridspec_kw={"height_ratios": [3, 1.2, 2, 1.5]})
    fig.suptitle("BTC/USD Strategy — Central Bank Avoidance Filter", fontsize=16, fontweight="bold")

    # ---- Chart 1: Price + signals + exclusion windows ----
    ax1 = axes[0]
    ax1.plot(plot_df.index, plot_df["Close"], color="#555555", linewidth=0.8, label="BTC/USD Close", zorder=2)

    if "EMA_fast" in plot_df.columns:
        ax1.plot(plot_df.index, plot_df["EMA_fast"], color="#2196F3", linewidth=0.7,
                 alpha=0.8, label=f"EMA {params['fast_ema_period']}")
        ax1.plot(plot_df.index, plot_df["EMA_slow"], color="#FF9800", linewidth=0.7,
                 alpha=0.8, label=f"EMA {params['slow_ema_period']}")

    # Entry/exit markers from filtered log
    entries = log_filtered[log_filtered["action"] == "entry"]
    exits = log_filtered[log_filtered["action"].isin(["signal_exit", "stop_exit", "cb_flat", "cb_exit"])]
    ax1.scatter(entries.index, entries["Close"], marker="^", color="#4CAF50", s=80,
                zorder=5, label="Entry", edgecolors="black", linewidths=0.5)
    ax1.scatter(exits.index, exits["Close"], marker="v", color="#F44336", s=80,
                zorder=5, label="Exit", edgecolors="black", linewidths=0.5)

    # Shade exclusion windows
    exclusion = build_exclusion_mask(
        plot_df.index, cb_dates,
        params["cb_window_before"], params["cb_window_after"]
    )
    _shade_exclusion(ax1, plot_df.index, exclusion)

    ax1.set_ylabel("Price (USD)", fontsize=11)
    ax1.legend(loc="upper left", fontsize=9)
    ax1.set_title("Price Chart with Entry/Exit Signals and CB Exclusion Windows", fontsize=12)
    ax1.grid(True, alpha=0.3)

    # ---- Chart 2: Position status (filtered) ----
    ax2 = axes[1]
    pos_series = log_filtered["position"].clip(lower=0)
    ax2.fill_between(log_filtered.index, 0, (pos_series > 0).astype(int),
                      color="#4CAF50", alpha=0.3, step="post", label="In Position")
    excl_series = log_filtered["excluded"].astype(int)
    ax2.fill_between(log_filtered.index, 0, excl_series,
                      color="#FF9800", alpha=0.3, step="post", label="CB Exclusion")
    ax2.set_ylabel("Status", fontsize=11)
    ax2.set_yticks([0, 1])
    ax2.set_yticklabels(["Flat", "Active"])
    ax2.legend(loc="upper left", fontsize=9)
    ax2.set_title("Position Status (Filtered Strategy)", fontsize=12)
    ax2.grid(True, alpha=0.3)

    # ---- Chart 3: Equity curves comparison ----
    ax3 = axes[2]
    ax3.plot(eq_filtered.index, eq_filtered["equity"], color="#2196F3",
             linewidth=1.5, label="With CB Filter")
    ax3.plot(eq_unfiltered.index, eq_unfiltered["equity"], color="#F44336",
             linewidth=1.5, alpha=0.7, label="Without CB Filter")
    ax3.axhline(y=100_000, color="gray", linestyle="--", alpha=0.5, label="Starting Capital")
    ax3.set_ylabel("Equity (USD)", fontsize=11)
    ax3.legend(loc="upper left", fontsize=9)
    ax3.set_title("Equity Curves — Filtered vs Unfiltered", fontsize=12)
    ax3.grid(True, alpha=0.3)

    # ---- Chart 4: Drawdown ----
    ax4 = axes[3]
    for label, eq, color in [("Filtered", eq_filtered, "#2196F3"),
                               ("Unfiltered", eq_unfiltered, "#F44336")]:
        running_max = eq["equity"].cummax()
        dd = (eq["equity"] - running_max) / running_max * 100
        ax4.fill_between(eq.index, dd, 0, alpha=0.3, color=color, label=label)
        ax4.plot(eq.index, dd, color=color, linewidth=0.8)

    ax4.axhline(y=-params["max_drawdown_pct"] * 100, color="black", linestyle="--",
                alpha=0.5, label=f"Circuit Breaker ({params['max_drawdown_pct']:.0%})")
    ax4.set_ylabel("Drawdown (%)", fontsize=11)
    ax4.set_xlabel("Date", fontsize=11)
    ax4.legend(loc="lower left", fontsize=9)
    ax4.set_title("Drawdown Comparison", fontsize=12)
    ax4.grid(True, alpha=0.3)

    for ax in axes:
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    chart_path = os.path.join(output_dir, "strategy_charts.png")
    fig.savefig(chart_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Charts saved to {chart_path}")
    return chart_path


def _shade_exclusion(ax, dates, mask):
    """Draw shaded rectangles on the chart for exclusion windows."""
    in_window = False
    start = None
    ymin, ymax = ax.get_ylim()
    for i, (date, excluded) in enumerate(zip(dates, mask)):
        if excluded and not in_window:
            start = date
            in_window = True
        elif not excluded and in_window:
            ax.axvspan(start, dates[i - 1], color="#FF9800", alpha=0.12, zorder=1)
            in_window = False
    if in_window and start is not None:
        ax.axvspan(start, dates[-1], color="#FF9800", alpha=0.12, zorder=1)


# ============================================================================
# MAIN
# ============================================================================

def main():
    params = PARAMS.copy()
    output_dir = params["output_dir"]
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 70)
    print("BTC/USD Strategy with Central Bank Avoidance Filter")
    print("=" * 70)

    # --- 1. Fetch data ---
    print("\n[1/5] Fetching data...")
    df = fetch_btc_data(params["ticker"], params["start_date"], params["end_date"])

    # --- 2. Compute indicators ---
    print("\n[2/5] Computing indicators...")
    df = compute_indicators(df, params)
    print(f"  Indicators computed: EMA({params['fast_ema_period']}), "
          f"EMA({params['slow_ema_period']}), ATR({params['atr_period']})")

    # --- 3. Backtest WITH CB filter ---
    print("\n[3/5] Running backtest WITH central bank filter...")
    eq_filtered, log_filtered, trades_filtered = backtest(df, params, use_cb_filter=True)
    metrics_filtered = compute_metrics(eq_filtered, trades_filtered)
    print("  Done.")

    # --- 4. Backtest WITHOUT CB filter ---
    print("\n[4/5] Running backtest WITHOUT central bank filter...")
    eq_unfiltered, log_unfiltered, trades_unfiltered = backtest(df, params, use_cb_filter=False)
    metrics_unfiltered = compute_metrics(eq_unfiltered, trades_unfiltered)
    print("  Done.")

    # --- 5. Results ---
    print("\n[5/5] Generating results...\n")

    # Summary table
    print("=" * 70)
    print(f"{'METRIC':<25} {'WITH CB FILTER':>20} {'WITHOUT CB FILTER':>20}")
    print("-" * 70)
    all_keys = list(metrics_filtered.keys())
    for key in all_keys:
        v1 = metrics_filtered.get(key, "N/A")
        v2 = metrics_unfiltered.get(key, "N/A")
        print(f"{key:<25} {str(v1):>20} {str(v2):>20}")
    print("=" * 70)

    # Central bank exclusion stats
    cb_dates = build_central_bank_calendar()
    start_ts = pd.Timestamp(params["start_date"])
    end_ts = pd.Timestamp(params["end_date"])
    cb_in_range = cb_dates[(cb_dates >= start_ts) & (cb_dates <= end_ts)]
    exclusion_mask = build_exclusion_mask(
        df[df.index >= start_ts].index, cb_dates,
        params["cb_window_before"], params["cb_window_after"]
    )
    print(f"\nCentral bank events in range:  {len(cb_in_range)}")
    print(f"Days excluded by CB filter:    {exclusion_mask.sum()}")
    print(f"Exclusion window:              T-{params['cb_window_before']} to T+{params['cb_window_after']}")

    # CB-forced exit stats
    if not trades_filtered.empty and "reason" in trades_filtered.columns:
        cb_exits = trades_filtered[trades_filtered["reason"] == "cb_exclusion"]
        print(f"Trades exited due to CB filter: {len(cb_exits)}")
        if len(cb_exits) > 0:
            print(f"  Total P&L from CB exits:     ${cb_exits['pnl'].sum():,.2f}")

    # Export trade logs
    for label, tdf in [("filtered", trades_filtered), ("unfiltered", trades_unfiltered)]:
        path = os.path.join(output_dir, f"trades_{label}.csv")
        if not tdf.empty:
            tdf.to_csv(path, index=False)
            print(f"\nTrade log saved: {path} ({len(tdf)} trades)")

    # Export daily equity
    for label, edf in [("filtered", eq_filtered), ("unfiltered", eq_unfiltered)]:
        path = os.path.join(output_dir, f"equity_{label}.csv")
        edf.to_csv(path)

    # Charts
    print("\nGenerating charts...")
    try:
        chart_path = plot_results(
            df, log_filtered, log_unfiltered,
            eq_filtered, eq_unfiltered, params,
            cb_dates, output_dir
        )
    except Exception as e:
        print(f"  Chart generation failed: {e}")
        chart_path = None

    # Parameters summary
    print("\n" + "=" * 70)
    print("STRATEGY PARAMETERS")
    print("-" * 70)
    for k, v in params.items():
        print(f"  {k:<25} = {v}")
    print("=" * 70)

    print(f"\nAll outputs saved to: {os.path.abspath(output_dir)}/")
    print("Done.")


if __name__ == "__main__":
    main()
