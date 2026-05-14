"""
Claude analysis agents for the DEX pump trading system.

Three agents, all READ-ONLY on operational data:
  1. Signal Interpreter — event-driven, analyzes incoming signals
  2. Daily Compliance Reviewer — cron daily 06:00 UTC
  3. Weekly R&D Analyst — cron Sunday 08:00 UTC
"""
