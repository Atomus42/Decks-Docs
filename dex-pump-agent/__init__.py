"""
DEX Pump Agent — Multi-strategy system for detecting and trading
memecoin pumps triggered by public figures.

Strategies:
  1. Long pre-event: detect accumulation, enter before pump, exit during pump
  2. Short post-pump (gated): short T+72h, x2 lever, hold max 14d, gated by funding/OI
  3. Vol selling: short straddle on DOGE/PEPE options pre-event (Deribit)

Architecture:
  - scrapers/     Layer 1: DexScreener, RSS feeds
  - pine/         TradingView Pine Script v6 indicators
  - agents/       Claude analysis agents (signal interpreter, compliance, R&D)
  - validators/   Layer 3: funding rate gates, on-chain concentration
  - backtester/   Walk-forward backtester on 24 months of events
  - config/       Settings, MCP agent configs
  - data/         Historical events, watchlists, signal logs
"""
