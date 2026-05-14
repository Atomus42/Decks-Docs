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

# === AUTO EXECUTION (Option B) ===
AUTO_EXEC_ENABLED = os.getenv("AUTO_EXEC_ENABLED", "false").lower() == "true"
AUTO_EXEC_MIN_CONVICTION = int(os.getenv("AUTO_EXEC_MIN_CONVICTION", "85"))
AUTO_EXEC_FIXED_SIZE_EUR = float(os.getenv("AUTO_EXEC_FIXED_SIZE_EUR", "500"))
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
DEXSCREENER_ALERT_THRESHOLD = 60  # score out of 100
RSS_ALERT_THRESHOLD = 50
PINE_HIGH_CONVICTION = 70
PINE_MEDIUM_CONVICTION = 40


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
