"""
Centralized settings for the DEX pump agent system.
All secrets come from environment variables — never hardcoded.
"""

import os
from pathlib import Path


# === PATHS ===
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = Path(os.getenv("DATA_DIR", str(PROJECT_ROOT / "data")))
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
LOGS_DIR = DATA_DIR / "logs"

# === TELEGRAM ===
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
TELEGRAM_CRITICAL_CHAT_ID = os.getenv("TELEGRAM_CRITICAL_CHAT_ID", "")

# === CLAUDE API ===
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")

# === DATA APIS ===
COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY", "")
SOLSCAN_API_KEY = os.getenv("SOLSCAN_API_KEY", "")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "")

# === EXCHANGES ===
BINANCE_FR_API_KEY = os.getenv("BINANCE_FR_API_KEY", "")
BINANCE_FR_API_SECRET = os.getenv("BINANCE_FR_API_SECRET", "")
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY", "")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET", "")
MEXC_API_KEY = os.getenv("MEXC_API_KEY", "")
MEXC_API_SECRET = os.getenv("MEXC_API_SECRET", "")

# === RISK LIMITS ===
MAX_POSITIONS_OPEN = int(os.getenv("MAX_POSITIONS_OPEN", "5"))
MAX_DAILY_TRADES = int(os.getenv("MAX_DAILY_TRADES", "3"))
MAX_POSITION_SIZE_EUR = float(os.getenv("MAX_POSITION_SIZE_EUR", "2000"))
MAX_TOTAL_EXPOSURE_EUR = float(os.getenv("MAX_TOTAL_EXPOSURE_EUR", "10000"))
KILL_SWITCH_DRAWDOWN_PCT = float(os.getenv("KILL_SWITCH_DRAWDOWN_PCT", "20"))
PAPER_TRADING_MODE = os.getenv("PAPER_TRADING_MODE", "true").lower() == "true"

# === KELLY CRITERION SIZING ===
# Optimal Kelly fraction f* = (p*b - q) / b
# With p=0.03 (3% hit rate), b=7 (net x7 after frictions), q=0.97:
#   f* = (0.03*7 - 0.97)/7 = -0.076 => negative EV at naive scale
# With p=0.10 (filtered 10%), b=7: f* = (0.10*7 - 0.90)/7 = -0.029
# With p=0.17 (real events only), b=7: f* = (0.17*7 - 0.83)/7 = 0.05 = 5%
# => Only profitable with aggressive filtering to real events only
KELLY_FRACTION = float(os.getenv("KELLY_FRACTION", "0.05"))  # 5% of capital per trade
MAX_PER_TRADE_PCT = float(os.getenv("MAX_PER_TRADE_PCT", "5.0"))  # hard cap at Kelly optimal

# === REALISTIC FRICTION MODEL ===
# From EV analysis: honeypots 5-15%, rug pulls 40-60% on fresh launches,
# sell tax 1-50%, MEV sandwich 1-5% per swap
FRICTION_HONEYPOT_RATE = 0.10  # 10% of fresh-launch trades are honeypots
FRICTION_RUG_RATE = 0.35  # 35% of unscreened fresh launches rug
FRICTION_SELL_TAX_AVG_PCT = 3.0  # average sell tax on non-scam tokens
FRICTION_MEV_PER_SWAP_PCT = 2.0  # average MEV + sandwich cost per swap
FRICTION_SLIPPAGE_ENTRY_PCT = 1.5  # entry slippage on thin books
FRICTION_SLIPPAGE_EXIT_PCT = 2.0  # exit slippage (worse, less liquidity post-pump)
FRICTION_TOTAL_ROUND_TRIP_PCT = 8.5  # sum of above for non-rug trades

# === RUIN PROBABILITY PARAMETERS ===
# P(zero x10 in N trades) = 0.9^N at 10% hit rate
# N=10: 35%, N=15: 21%, N=20: 12%
# System must survive 20+ losing trades before first big win
MIN_CAPITAL_SURVIVAL_TRADES = 20  # must be able to sustain this many losses

# === AUTO EXECUTION (Option B) ===
AUTO_EXEC_ENABLED = os.getenv("AUTO_EXEC_ENABLED", "false").lower() == "true"
AUTO_EXEC_MIN_CONVICTION = int(os.getenv("AUTO_EXEC_MIN_CONVICTION", "85"))
AUTO_EXEC_FIXED_SIZE_EUR = float(os.getenv("AUTO_EXEC_FIXED_SIZE_EUR", "125"))  # Kelly: 5% of 2500
AUTO_EXEC_MAX_DAILY = int(os.getenv("AUTO_EXEC_MAX_DAILY", "3"))

# === SCRAPER INTERVALS ===
DEX_POLL_INTERVAL = int(os.getenv("DEX_POLL_INTERVAL", "300"))  # 5 min
RSS_POLL_INTERVAL = int(os.getenv("RSS_POLL_INTERVAL", "180"))  # 3 min

# === SHORT STRATEGY PARAMETERS ===
SHORT_ENTRY_DELAY_HOURS = 72
SHORT_MAX_HOLD_DAYS = 14
SHORT_LEVERAGE = 2.0
SHORT_STOP_LOSS_PCT = -25.0  # capital %
SHORT_TP1_PCT = 40.0  # capital %
SHORT_TP2_PCT = 80.0  # capital %

# === GATING THRESHOLDS ===
FUNDING_RATE_MAX = 0.0  # must be negative for short entry
LONG_SHORT_RATIO_MIN = 0.8
SHORT_OI_MAX_PCT = 55.0
SHORT_LIQUIDATION_MAX_PCT = 2.0

# === SIGNAL SCORING ===
# Tightened: only top 5-10% of alerts should pass (quality over volume)
DEXSCREENER_ALERT_THRESHOLD = 75  # was 60 — raised to filter false positives
RSS_ALERT_THRESHOLD = 65  # was 50 — raised
PINE_HIGH_CONVICTION = 70
PINE_MEDIUM_CONVICTION = 40

# === ANTI-RUG PRE-TRADE GATES (mandatory for long pre-event) ===
ANTIRUG_LP_LOCK_MIN_MONTHS = 6  # LP must be locked >= 6 months
ANTIRUG_MINT_FUNCTION_BLOCKED = True  # contract must not have active mint ownership
ANTIRUG_SELL_SIMULATION_REQUIRED = True  # eth_call sell simulation must succeed
ANTIRUG_TOP10_HOLDERS_MAX_PCT = 30.0  # top 10 holders < 30% of supply (was 80%)
ANTIRUG_MIN_HOLDERS = 200  # minimum holder count (was 100)
ANTIRUG_MAX_SELL_TAX_PCT = 5.0  # reject tokens with sell tax > 5%


def validate_config():
    """Check that critical env vars are set. Call at startup."""
    warnings = []
    if not TELEGRAM_BOT_TOKEN:
        warnings.append("TELEGRAM_BOT_TOKEN not set — alerts disabled")
    if not ANTHROPIC_API_KEY:
        warnings.append("ANTHROPIC_API_KEY not set — Claude agents disabled")
    if PAPER_TRADING_MODE:
        warnings.append("PAPER_TRADING_MODE=true — no real trades will execute")
    if AUTO_EXEC_ENABLED:
        warnings.append(
            f"AUTO_EXEC_ENABLED=true — auto-execution active "
            f"(min_conviction={AUTO_EXEC_MIN_CONVICTION}, "
            f"max_daily={AUTO_EXEC_MAX_DAILY}, "
            f"size={AUTO_EXEC_FIXED_SIZE_EUR}EUR)"
        )
    return warnings
