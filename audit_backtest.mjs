// =============================================================================
// EXHAUSTIVE EXIT IMPROVEMENT RESEARCH ENGINE
// Tests 30+ exit variants against real BTCUSDT 1H data
// =============================================================================

const CONFIG_BASE = {
  rsiMomPeriod: 11, rsiMomEntry: 40, rsiMomExit: 30,
  emaFastLen: 12, emaSlowLen: 43,
  atrMomPeriod: 17, atrMomTrail: 6.5, momHardSLPct: 5.0,
  erPeriod: 50, erSmoothPer: 10, erTrendThresh: 0.06,
  bbPeriod: 20, bbStd: 2.0,
  rsiMrPeriod: 14, rsiMrBuy: 30, rsiMrSell: 65,
  mrProfitPct: 5.0, mrHardSLPct: 1.5,
  atrMrPeriod: 14, atrMrTrail: 4.0, mrMaxHold: 96,
  initialCapital: 100000, commissionPct: 0.04, slippage: 1,

  // === EXIT IMPROVEMENT FLAGS (all off = v3 baseline) ===

  // 1. Tiered profit lock-in
  useProfitLockIn: false,
  lockBETrigger: 2.0,   lockBELevel: 0.1,     // breakeven at +2%
  lockT1Trigger: 4.0,   lockT1Level: 2.0,     // lock +2% at +4%
  lockT2Trigger: 6.0,   lockT2Level: 4.0,     // lock +4% at +6%

  // 2. RSI suppression when profitable
  useRsiSuppression: false,
  momRsiSuppressAbovePnl: 3.0,  // don't fire MOM RSI exit if unrealized >= this
  mrRsiDynamicThresh: 75,        // raise MR RSI sell to this when profitable
  mrRsiDynamicAbovePnl: 3.0,

  // 3. Extended trail after big move
  useExtendedTrail: false,
  momExtTrailTrigger: 5.0,  momExtTrailMult: 8.0,
  mrExtTrailTrigger: 3.0,   mrExtTrailMult: 6.0,

  // 4. Remove MR profit target cap
  removeMrPTCap: false,

  // 5. Profit chandelier (MR)
  useProfitChandelier: false,
  chandelierATRMult: 1.5,
  chandelierActivatePnl: 3.0,

  // 6. Trailing percentage stop (instead of ATR trail)
  usePercentTrail: false,
  momPercentTrail: 3.0,   // trail by 3% from high
  mrPercentTrail: 2.0,

  // 7. Time-based trail tightening
  useTimeTighten: false,
  timeTightenBars: 48,     // after 48 bars, tighten trail
  timeTightenFactor: 0.6,  // multiply trail distance by this

  // 8. Parabolic acceleration trail
  useParabolicTrail: false,
  parabolicStart: 0.02,
  parabolicIncrement: 0.02,
  parabolicMax: 0.20,

  // 9. EMA crossover exit (fast < slow = exit MOM)
  useEmaCrossExit: false,

  // 10. Keltner channel exit for MOM (exit at upper keltner)
  useKeltnerExit: false,
  keltnerMult: 2.5,

  // 11. Volatility regime adaptive trail
  useVolAdaptiveTrail: false,
  volAdaptiveHighATRMult: 1.3,  // widen trail when ATR is high vs its SMA
  volAdaptiveLowATRMult: 0.7,

  // 12. RSI exit cooldown (don't exit on first RSI signal, wait N bars)
  useRsiCooldown: false,
  rsiCooldownBars: 3,

  // 13. Chandelier exit for MOM (classic: highest high - N * ATR)
  useChandelierMom: false,
  chandelierMomMult: 3.0,

  // 14. Dynamic MOM RSI exit threshold based on profit
  useDynamicMomRsi: false,
  // If PnL >= 3%, lower RSI exit threshold to 20 (harder to trigger)
  dynamicMomRsiProfitThresh: 3.0,
  dynamicMomRsiNewExit: 20,

  // 15. Breakeven-only stop (no tiers, just move SL to breakeven at X%)
  useBreakevenOnly: false,
  breakevenTrigger: 2.0,
  breakevenBuffer: 0.1,

  // 16. ATR-based dynamic profit target for MOM
  useMomATRProfitTarget: false,
  momATRPTMult: 4.0,  // exit at entry + 4x ATR

  // 17. Percentage-based profit target for MOM
  useMomPctPT: false,
  momPctPT: 8.0,

  // 18. Higher timeframe trend filter for exits (use longer EMA)
  useHTFTrendFilter: false,
  htfEmaLen: 100,

  // 19. Close > EMA required to stay in MOM (exit if close < emaFast)
  useEmaFloorExit: false,

  // 20. Minimum bars before RSI exit
  useMinBarsBeforeRsi: false,
  minBarsBeforeRsi: 10,

  // 21. Trailing from close (not from high)
  useTrailFromClose: false,
};

// =============================================================================
// DATA FETCHING
// =============================================================================
async function fetchKlines(symbol, interval, startTime, endTime) {
  const allCandles = [];
  let cursor = startTime;
  while (cursor < endTime) {
    const url = `https://api.binance.com/api/v3/klines?symbol=${symbol}&interval=${interval}&startTime=${cursor}&endTime=${endTime}&limit=1000`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Binance API ${res.status}: ${await res.text()}`);
    const data = await res.json();
    if (data.length === 0) break;
    for (const k of data) {
      allCandles.push({
        time: k[0], open: +k[1], high: +k[2], low: +k[3], close: +k[4], volume: +k[5]
      });
    }
    cursor = data[data.length - 1][0] + 1;
    await new Promise(r => setTimeout(r, 80));
  }
  return allCandles;
}

// =============================================================================
// INDICATORS
// =============================================================================
function calcRSI(closes, period) {
  const rsi = new Array(closes.length).fill(NaN);
  if (closes.length < period + 1) return rsi;
  let avgGain = 0, avgLoss = 0;
  for (let i = 1; i <= period; i++) {
    const d = closes[i] - closes[i - 1];
    if (d > 0) avgGain += d; else avgLoss -= d;
  }
  avgGain /= period; avgLoss /= period;
  rsi[period] = avgLoss === 0 ? 100 : 100 - 100 / (1 + avgGain / avgLoss);
  for (let i = period + 1; i < closes.length; i++) {
    const d = closes[i] - closes[i - 1];
    avgGain = (avgGain * (period - 1) + (d > 0 ? d : 0)) / period;
    avgLoss = (avgLoss * (period - 1) + (d < 0 ? -d : 0)) / period;
    rsi[i] = avgLoss === 0 ? 100 : 100 - 100 / (1 + avgGain / avgLoss);
  }
  return rsi;
}

function calcEMA(data, period) {
  const ema = new Array(data.length).fill(NaN);
  let sum = 0, count = 0;
  for (let i = 0; i < data.length; i++) {
    if (isNaN(data[i])) continue;
    sum += data[i]; count++;
    if (count === period) {
      ema[i] = sum / period;
      const k = 2 / (period + 1);
      for (let j = i + 1; j < data.length; j++) {
        if (isNaN(data[j])) { ema[j] = ema[j - 1]; continue; }
        ema[j] = data[j] * k + ema[j - 1] * (1 - k);
      }
      break;
    }
  }
  return ema;
}

function calcSMA(data, period) {
  const sma = new Array(data.length).fill(NaN);
  let sum = 0;
  for (let i = 0; i < data.length; i++) {
    sum += data[i];
    if (i >= period) sum -= data[i - period];
    if (i >= period - 1) sma[i] = sum / period;
  }
  return sma;
}

function calcStdev(data, period) {
  const sd = new Array(data.length).fill(NaN);
  for (let i = period - 1; i < data.length; i++) {
    let sum = 0, sum2 = 0;
    for (let j = i - period + 1; j <= i; j++) {
      sum += data[j]; sum2 += data[j] * data[j];
    }
    const mean = sum / period;
    sd[i] = Math.sqrt(sum2 / period - mean * mean);
  }
  return sd;
}

function calcATR(highs, lows, closes, period) {
  const tr = new Array(highs.length).fill(NaN);
  tr[0] = highs[0] - lows[0];
  for (let i = 1; i < highs.length; i++) {
    tr[i] = Math.max(highs[i] - lows[i], Math.abs(highs[i] - closes[i - 1]), Math.abs(lows[i] - closes[i - 1]));
  }
  const atr = new Array(highs.length).fill(NaN);
  let sum = 0;
  for (let i = 0; i < period; i++) sum += tr[i];
  atr[period - 1] = sum / period;
  for (let i = period; i < highs.length; i++) {
    atr[i] = (atr[i - 1] * (period - 1) + tr[i]) / period;
  }
  return atr;
}

function calcER(closes, erPeriod, smoothPer) {
  const erRaw = new Array(closes.length).fill(0);
  for (let i = erPeriod; i < closes.length; i++) {
    const direction = Math.abs(closes[i] - closes[i - erPeriod]);
    let volatility = 0;
    for (let j = i - erPeriod + 1; j <= i; j++) volatility += Math.abs(closes[j] - closes[j - 1]);
    erRaw[i] = volatility !== 0 ? direction / volatility : 0;
  }
  return calcEMA(erRaw, smoothPer);
}

// =============================================================================
// PRE-COMPUTE ALL INDICATORS (once, shared across all variants)
// =============================================================================
function precompute(candles) {
  const n = candles.length;
  const closes = candles.map(c => c.close);
  const highs = candles.map(c => c.high);
  const lows = candles.map(c => c.low);

  return {
    n, closes, highs, lows,
    rsiMom: calcRSI(closes, CONFIG_BASE.rsiMomPeriod),
    rsiMr: calcRSI(closes, CONFIG_BASE.rsiMrPeriod),
    emaFast: calcEMA(closes, CONFIG_BASE.emaFastLen),
    emaSlow: calcEMA(closes, CONFIG_BASE.emaSlowLen),
    ema100: calcEMA(closes, 100),
    atrMom: calcATR(highs, lows, closes, CONFIG_BASE.atrMomPeriod),
    atrMr: calcATR(highs, lows, closes, CONFIG_BASE.atrMrPeriod),
    atr14: calcATR(highs, lows, closes, 14),
    bbBasis: calcSMA(closes, CONFIG_BASE.bbPeriod),
    bbStdev: calcStdev(closes, CONFIG_BASE.bbPeriod),
    erSmoothed: calcER(closes, CONFIG_BASE.erPeriod, CONFIG_BASE.erSmoothPer),
    atrMomSMA: null, // computed below
  };
}

// =============================================================================
// BACKTEST ENGINE (parameterized)
// =============================================================================
function runBacktest(ind, cfg) {
  const { n, closes, highs, lows, rsiMom, rsiMr, emaFast, emaSlow, ema100, atrMom, atrMr, atr14, bbBasis, bbStdev, erSmoothed } = ind;

  // ATR SMA for volatility-adaptive trail
  const atrMomSMA50 = calcSMA(atrMom.map(v => isNaN(v) ? 0 : v), 50);

  let posType = 0, entryPrice = NaN, trailHigh = NaN, trailStop = NaN, barsHeld = 0;
  let hardSLLevel = NaN, equity = cfg.initialCapital, positionSize = 0;
  let highestCloseSinceEntry = NaN; // for chandelier
  let parabolicAF = 0, parabolicSAR = NaN, parabolicEP = NaN; // parabolic
  let rsiBelowCount = 0; // RSI cooldown counter

  const trades = [];
  let ct = null; // current trade

  for (let i = 1; i < n; i++) {
    const cl = closes[i], hi = highs[i], lo = lows[i];
    if (isNaN(rsiMom[i]) || isNaN(emaFast[i]) || isNaN(emaSlow[i]) || isNaN(erSmoothed[i])) continue;

    const isTrending = erSmoothed[i] >= cfg.erTrendThresh;
    const isChoppy = erSmoothed[i] < cfg.erTrendThresh;
    const uptrend = emaFast[i] > emaSlow[i];
    const bbLower = bbBasis[i] - bbStdev[i] * cfg.bbStd;
    const rsiMomCrossUp = rsiMom[i] >= cfg.rsiMomEntry && rsiMom[i - 1] < cfg.rsiMomEntry;
    const hasPos = posType !== 0;

    // === HARD SL / PROFIT LOCK-IN CHECK ===
    if (hasPos && !isNaN(hardSLLevel) && lo <= hardSLLevel) {
      const exitPrice = hardSLLevel;
      const pnlPct = (exitPrice / entryPrice - 1) * 100;
      const comm = positionSize * exitPrice * cfg.commissionPct / 100;
      equity += positionSize * (exitPrice - entryPrice) - comm;
      if (ct) {
        ct.exitBar = i; ct.exitPrice = exitPrice; ct.pnlPct = pnlPct;
        ct.exitReason = pnlPct >= 0 ? (posType === 1 ? "MOM_PROFIT_LOCK" : "MR_PROFIT_LOCK") : (posType === 1 ? "MOM_HARD_SL" : "MR_HARD_SL");
        ct.exitDate = new Date(ind.closes[i] ? candles_g[i].time : 0).toISOString().slice(0, 16);
        trades.push(ct); ct = null;
      }
      posType = 0; entryPrice = NaN; trailHigh = NaN; trailStop = NaN; barsHeld = 0; hardSLLevel = NaN; positionSize = 0;
      highestCloseSinceEntry = NaN; parabolicAF = 0; parabolicSAR = NaN; rsiBelowCount = 0;
      continue;
    }

    // === TRAIL UPDATE ===
    if (hasPos) {
      barsHeld++;
      const unrealizedPct = (cl / entryPrice - 1) * 100;
      const unrealizedHiPct = (hi / entryPrice - 1) * 100;

      // Track highest close for chandelier
      if (cl > highestCloseSinceEntry || isNaN(highestCloseSinceEntry)) highestCloseSinceEntry = cl;

      if (hi > trailHigh || isNaN(trailHigh)) trailHigh = hi;
      if (ct) {
        if (unrealizedHiPct > ct.maxUnrealizedPct) { ct.maxUnrealizedPct = unrealizedHiPct; ct.maxUnrealizedBar = i; }
      }

      if (posType === 1) {
        let mult = cfg.atrMomTrail;

        // Extended trail
        if (cfg.useExtendedTrail && unrealizedPct >= cfg.momExtTrailTrigger) mult = cfg.momExtTrailMult;

        // Time tightening
        if (cfg.useTimeTighten && barsHeld >= cfg.timeTightenBars) mult *= cfg.timeTightenFactor;

        // Volatility adaptive
        if (cfg.useVolAdaptiveTrail && !isNaN(atrMomSMA50[i]) && atrMomSMA50[i] > 0) {
          const ratio = atrMom[i] / atrMomSMA50[i];
          if (ratio > 1.2) mult *= cfg.volAdaptiveHighATRMult;
          else if (ratio < 0.8) mult *= cfg.volAdaptiveLowATRMult;
        }

        if (cfg.usePercentTrail) {
          trailStop = Math.max(trailStop || 0, (cfg.useTrailFromClose ? highestCloseSinceEntry : trailHigh) * (1 - cfg.momPercentTrail / 100));
        } else if (cfg.useTrailFromClose) {
          trailStop = highestCloseSinceEntry - atrMom[i] * mult;
        } else {
          trailStop = trailHigh - atrMom[i] * mult;
        }

        // Parabolic trail
        if (cfg.useParabolicTrail) {
          if (isNaN(parabolicSAR)) { parabolicSAR = entryPrice; parabolicEP = hi; parabolicAF = cfg.parabolicStart; }
          if (hi > parabolicEP) { parabolicEP = hi; parabolicAF = Math.min(parabolicAF + cfg.parabolicIncrement, cfg.parabolicMax); }
          parabolicSAR = parabolicSAR + parabolicAF * (parabolicEP - parabolicSAR);
          trailStop = Math.max(trailStop || 0, parabolicSAR);
        }

      } else if (posType === 2) {
        let mult = cfg.atrMrTrail;
        if (cfg.useExtendedTrail && unrealizedPct >= cfg.mrExtTrailTrigger) mult = cfg.mrExtTrailMult;
        if (cfg.useTimeTighten && barsHeld >= cfg.timeTightenBars) mult *= cfg.timeTightenFactor;

        if (cfg.usePercentTrail) {
          trailStop = Math.max(trailStop || 0, (cfg.useTrailFromClose ? highestCloseSinceEntry : trailHigh) * (1 - cfg.mrPercentTrail / 100));
        } else if (cfg.useTrailFromClose) {
          trailStop = highestCloseSinceEntry - atrMr[i] * mult;
        } else {
          trailStop = trailHigh - atrMr[i] * mult;
        }
      }

      // === PROFIT LOCK-IN: ratchet hardSLLevel upward ===
      if (cfg.useProfitLockIn && !isNaN(entryPrice)) {
        if (unrealizedPct >= cfg.lockT2Trigger) {
          const newSL = entryPrice * (1 + cfg.lockT2Level / 100);
          if (newSL > hardSLLevel) hardSLLevel = newSL;
        } else if (unrealizedPct >= cfg.lockT1Trigger) {
          const newSL = entryPrice * (1 + cfg.lockT1Level / 100);
          if (newSL > hardSLLevel) hardSLLevel = newSL;
        } else if (unrealizedPct >= cfg.lockBETrigger) {
          const newSL = entryPrice * (1 + cfg.lockBELevel / 100);
          if (newSL > hardSLLevel) hardSLLevel = newSL;
        }
      }

      // Breakeven-only
      if (cfg.useBreakevenOnly && !isNaN(entryPrice) && unrealizedPct >= cfg.breakevenTrigger) {
        const beSL = entryPrice * (1 + cfg.breakevenBuffer / 100);
        if (beSL > hardSLLevel) hardSLLevel = beSL;
      }
    }

    // === EXIT SIGNALS ===
    const unrealizedPct = hasPos && !isNaN(entryPrice) ? (cl / entryPrice - 1) * 100 : 0;

    // --- MOM RSI exit ---
    let momRsiThreshold = cfg.rsiMomExit;
    if (cfg.useDynamicMomRsi && unrealizedPct >= cfg.dynamicMomRsiProfitThresh) {
      momRsiThreshold = cfg.dynamicMomRsiNewExit;
    }
    let exitMomRsi = hasPos && posType === 1 && rsiMom[i] < momRsiThreshold;

    // RSI suppression
    if (cfg.useRsiSuppression && exitMomRsi && unrealizedPct >= cfg.momRsiSuppressAbovePnl) {
      exitMomRsi = false; // suppress RSI exit when in profit
    }

    // RSI cooldown
    if (cfg.useRsiCooldown && exitMomRsi) {
      rsiBelowCount++;
      if (rsiBelowCount < cfg.rsiCooldownBars) exitMomRsi = false;
    } else if (hasPos && posType === 1) {
      rsiBelowCount = 0;
    }

    // Min bars before RSI
    if (cfg.useMinBarsBeforeRsi && exitMomRsi && barsHeld < cfg.minBarsBeforeRsi) {
      exitMomRsi = false;
    }

    // EMA floor exit for MOM
    let exitEmaFloor = false;
    if (cfg.useEmaFloorExit && hasPos && posType === 1 && cl < emaFast[i] && barsHeld > 5) {
      exitEmaFloor = true;
    }

    // EMA crossover exit
    let exitEmaCross = false;
    if (cfg.useEmaCrossExit && hasPos && posType === 1 && emaFast[i] < emaSlow[i] && emaFast[i - 1] >= emaSlow[i - 1]) {
      exitEmaCross = true;
    }

    // HTF trend filter: suppress RSI exit if above ema100
    if (cfg.useHTFTrendFilter && exitMomRsi && posType === 1 && !isNaN(ema100[i]) && cl > ema100[i]) {
      exitMomRsi = false;
    }

    // MOM trail
    let exitMomTrail = hasPos && posType === 1 && !isNaN(trailStop) && cl < trailStop && !exitMomRsi;

    // Keltner exit for MOM
    let exitKeltner = false;
    if (cfg.useKeltnerExit && hasPos && posType === 1 && !isNaN(emaFast[i]) && !isNaN(atrMom[i])) {
      const keltnerUpper = emaFast[i] + atrMom[i] * cfg.keltnerMult;
      if (cl >= keltnerUpper) exitKeltner = true;
    }

    // Chandelier MOM exit
    let exitChandelierMom = false;
    if (cfg.useChandelierMom && hasPos && posType === 1 && !isNaN(atrMom[i]) && !isNaN(trailHigh)) {
      const chanStop = trailHigh - atrMom[i] * cfg.chandelierMomMult;
      if (cl < chanStop && barsHeld > 5) exitChandelierMom = true;
    }

    // MOM ATR profit target
    let exitMomATRPT = false;
    if (cfg.useMomATRProfitTarget && hasPos && posType === 1 && !isNaN(entryPrice) && !isNaN(atrMom[i])) {
      if (cl >= entryPrice + atrMom[i] * cfg.momATRPTMult) exitMomATRPT = true;
    }

    // MOM pct profit target
    let exitMomPctPT = false;
    if (cfg.useMomPctPT && hasPos && posType === 1 && unrealizedPct >= cfg.momPctPT) {
      exitMomPctPT = true;
    }

    // --- MR exits ---
    let mrPTActive = !cfg.removeMrPTCap;
    let exitMrProfit = mrPTActive && hasPos && posType === 2 && !isNaN(entryPrice) && cl >= entryPrice * (1 + cfg.mrProfitPct / 100);

    let mrSellThresh = cfg.rsiMrSell;
    if (cfg.useRsiSuppression && unrealizedPct >= cfg.mrRsiDynamicAbovePnl) {
      mrSellThresh = cfg.mrRsiDynamicThresh;
    }
    let exitMrRsi = hasPos && posType === 2 && rsiMr[i] > mrSellThresh && !exitMrProfit;
    let exitMrTrail = hasPos && posType === 2 && !isNaN(trailStop) && cl < trailStop && barsHeld > 3 && !exitMrProfit && !exitMrRsi;
    let exitMrTime = hasPos && posType === 2 && barsHeld >= cfg.mrMaxHold && !exitMrProfit && !exitMrRsi && !exitMrTrail;

    // Profit chandelier for MR
    let exitProfitChandelier = false;
    if (cfg.useProfitChandelier && hasPos && posType === 2 && unrealizedPct >= cfg.chandelierActivatePnl) {
      if (!isNaN(highestCloseSinceEntry) && !isNaN(atr14[i])) {
        const chanLevel = highestCloseSinceEntry - cfg.chandelierATRMult * atr14[i];
        if (cl < chanLevel) exitProfitChandelier = true;
      }
    }

    const anyExit = exitMomRsi || exitMomTrail || exitMrProfit || exitMrRsi || exitMrTrail || exitMrTime
                 || exitEmaCross || exitEmaFloor || exitKeltner || exitChandelierMom
                 || exitMomATRPT || exitMomPctPT || exitProfitChandelier;

    if (anyExit && hasPos) {
      const exitPrice = cl;
      const pnlPct = (exitPrice / entryPrice - 1) * 100;
      const comm = positionSize * exitPrice * cfg.commissionPct / 100;
      equity += positionSize * (exitPrice - entryPrice) - comm;
      let reason = exitMomRsi ? "MOM_RSI" : exitMomTrail ? "MOM_TRAIL" : exitEmaCross ? "MOM_EMA_X"
        : exitEmaFloor ? "MOM_EMA_FLOOR" : exitKeltner ? "MOM_KELTNER" : exitChandelierMom ? "MOM_CHANDELIER"
        : exitMomATRPT ? "MOM_ATR_PT" : exitMomPctPT ? "MOM_PCT_PT"
        : exitMrProfit ? "MR_PT" : exitMrRsi ? "MR_RSI" : exitMrTrail ? "MR_TRAIL"
        : exitProfitChandelier ? "MR_CHANDELIER" : "MR_TIMEOUT";
      if (ct) {
        ct.exitBar = i; ct.exitPrice = exitPrice; ct.pnlPct = pnlPct; ct.exitReason = reason;
        trades.push(ct); ct = null;
      }
      posType = 0; entryPrice = NaN; trailHigh = NaN; trailStop = NaN; barsHeld = 0;
      hardSLLevel = NaN; positionSize = 0; highestCloseSinceEntry = NaN;
      parabolicAF = 0; parabolicSAR = NaN; rsiBelowCount = 0;
    }

    // === ENTRY SIGNALS ===
    const isFlat = posType === 0;
    const entryMom = isFlat && rsiMomCrossUp && uptrend && isTrending && !anyExit;
    const entryMr = isFlat && cl <= bbLower && bbLower > 0 && rsiMr[i] < cfg.rsiMrBuy && isChoppy && !entryMom && !anyExit;

    if (entryMom) {
      entryPrice = cl;
      const comm = equity * cfg.commissionPct / 100;
      positionSize = (equity - comm) / cl;
      posType = 1; trailHigh = cl; trailStop = cl - atrMom[i] * cfg.atrMomTrail; barsHeld = 0;
      hardSLLevel = cl * (1 - cfg.momHardSLPct / 100);
      highestCloseSinceEntry = cl; parabolicAF = 0; parabolicSAR = NaN; rsiBelowCount = 0;
      ct = { type: "MOM", entryBar: i, entryPrice: cl, maxUnrealizedPct: 0, maxUnrealizedBar: i, equityAtEntry: equity };
    }
    if (entryMr) {
      entryPrice = cl;
      const comm = equity * cfg.commissionPct / 100;
      positionSize = (equity - comm) / cl;
      posType = 2; trailHigh = cl; trailStop = cl - atrMr[i] * cfg.atrMrTrail; barsHeld = 0;
      hardSLLevel = cl * (1 - cfg.mrHardSLPct / 100);
      highestCloseSinceEntry = cl; parabolicAF = 0; parabolicSAR = NaN; rsiBelowCount = 0;
      ct = { type: "MR", entryBar: i, entryPrice: cl, maxUnrealizedPct: 0, maxUnrealizedBar: i, equityAtEntry: equity };
    }
  }

  return { trades, finalEquity: equity };
}

// =============================================================================
// METRICS COMPUTATION
// =============================================================================
function metrics(trades, finalEquity, initialCapital) {
  if (trades.length === 0) return { trades: 0, winRate: 0, totalReturn: 0, avgPnl: 0, avgWin: 0, avgLoss: 0, maxDD: 0, sharpe: 0, avgGiveback: 0, profitFactor: 0, avgBars: 0 };
  const wins = trades.filter(t => t.pnlPct > 0);
  const losses = trades.filter(t => t.pnlPct <= 0);
  const avgWin = wins.length ? wins.reduce((s, t) => s + t.pnlPct, 0) / wins.length : 0;
  const avgLoss = losses.length ? losses.reduce((s, t) => s + t.pnlPct, 0) / losses.length : 0;
  const avgGiveback = trades.reduce((s, t) => s + (t.maxUnrealizedPct - t.pnlPct), 0) / trades.length;
  const totalReturn = (finalEquity / initialCapital - 1) * 100;

  // Profit factor
  const grossProfit = wins.reduce((s, t) => s + t.pnlPct, 0);
  const grossLoss = Math.abs(losses.reduce((s, t) => s + t.pnlPct, 0));
  const profitFactor = grossLoss > 0 ? grossProfit / grossLoss : grossProfit > 0 ? 999 : 0;

  // Max drawdown (on equity curve)
  let peak = initialCapital, maxDD = 0, eq = initialCapital;
  for (const t of trades) {
    eq = eq * (1 + t.pnlPct / 100);
    if (eq > peak) peak = eq;
    const dd = (peak - eq) / peak * 100;
    if (dd > maxDD) maxDD = dd;
  }

  // Avg bars held
  const avgBars = trades.reduce((s, t) => s + (t.exitBar - t.entryBar), 0) / trades.length;

  // Sharpe-like ratio (avg / stdev of trade PnL)
  const avgPnl = trades.reduce((s, t) => s + t.pnlPct, 0) / trades.length;
  const variance = trades.reduce((s, t) => s + (t.pnlPct - avgPnl) ** 2, 0) / trades.length;
  const sharpe = variance > 0 ? avgPnl / Math.sqrt(variance) : 0;

  return {
    trades: trades.length, winRate: wins.length / trades.length * 100,
    totalReturn, avgPnl, avgWin, avgLoss, maxDD, sharpe, avgGiveback, profitFactor, avgBars,
    momTrades: trades.filter(t => t.type === "MOM").length,
    mrTrades: trades.filter(t => t.type === "MR").length,
    momGiveback: (() => { const mt = trades.filter(t => t.type === "MOM"); return mt.length ? mt.reduce((s,t) => s + (t.maxUnrealizedPct - t.pnlPct), 0) / mt.length : 0; })(),
    mrGiveback: (() => { const mt = trades.filter(t => t.type === "MR"); return mt.length ? mt.reduce((s,t) => s + (t.maxUnrealizedPct - t.pnlPct), 0) / mt.length : 0; })(),
    worstGivebacks: trades.filter(t => t.maxUnrealizedPct >= 5 && t.pnlPct < 3).length,
    catastrophicReversals: trades.filter(t => t.maxUnrealizedPct >= 6 && t.pnlPct < 0).length,
  };
}

// =============================================================================
// DEFINE ALL VARIANTS TO TEST
// =============================================================================
function getVariants() {
  return [
    // BASELINE
    { name: "v3 BASELINE", changes: {} },

    // === GROUP 1: PROFIT LOCK-IN VARIANTS ===
    { name: "ProfitLock: BE@2/T1@4+2/T2@6+4", changes: { useProfitLockIn: true } },
    { name: "ProfitLock: BE@1.5/T1@3+1.5/T2@5+3", changes: { useProfitLockIn: true, lockBETrigger: 1.5, lockBELevel: 0.1, lockT1Trigger: 3.0, lockT1Level: 1.5, lockT2Trigger: 5.0, lockT2Level: 3.0 } },
    { name: "ProfitLock: BE@3/T1@5+3/T2@8+5", changes: { useProfitLockIn: true, lockBETrigger: 3.0, lockT1Trigger: 5.0, lockT1Level: 3.0, lockT2Trigger: 8.0, lockT2Level: 5.0 } },
    { name: "BreakevenOnly @2%", changes: { useBreakevenOnly: true, breakevenTrigger: 2.0 } },
    { name: "BreakevenOnly @3%", changes: { useBreakevenOnly: true, breakevenTrigger: 3.0 } },

    // === GROUP 2: RSI SUPPRESSION VARIANTS ===
    { name: "RSI Suppress MOM @3% PnL", changes: { useRsiSuppression: true, momRsiSuppressAbovePnl: 3.0 } },
    { name: "RSI Suppress MOM @2% PnL", changes: { useRsiSuppression: true, momRsiSuppressAbovePnl: 2.0 } },
    { name: "RSI Suppress MOM @5% PnL", changes: { useRsiSuppression: true, momRsiSuppressAbovePnl: 5.0 } },
    { name: "Dynamic MOM RSI -> 20 @3% PnL", changes: { useDynamicMomRsi: true, dynamicMomRsiProfitThresh: 3.0, dynamicMomRsiNewExit: 20 } },
    { name: "Dynamic MOM RSI -> 15 @3% PnL", changes: { useDynamicMomRsi: true, dynamicMomRsiProfitThresh: 3.0, dynamicMomRsiNewExit: 15 } },
    { name: "Dynamic MOM RSI -> 25 @2% PnL", changes: { useDynamicMomRsi: true, dynamicMomRsiProfitThresh: 2.0, dynamicMomRsiNewExit: 25 } },
    { name: "Min 10 bars before RSI exit", changes: { useMinBarsBeforeRsi: true, minBarsBeforeRsi: 10 } },
    { name: "Min 5 bars before RSI exit", changes: { useMinBarsBeforeRsi: true, minBarsBeforeRsi: 5 } },
    { name: "RSI cooldown 3 bars", changes: { useRsiCooldown: true, rsiCooldownBars: 3 } },
    { name: "RSI cooldown 5 bars", changes: { useRsiCooldown: true, rsiCooldownBars: 5 } },

    // === GROUP 3: TRAIL VARIANTS ===
    { name: "Extended trail MOM 8x@5%", changes: { useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0 } },
    { name: "Extended trail MOM 10x@5%", changes: { useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 10.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 7.0 } },
    { name: "Extended trail MOM 8x@3%", changes: { useExtendedTrail: true, momExtTrailTrigger: 3.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 2.0, mrExtTrailMult: 5.0 } },
    { name: "Percent trail MOM 3% / MR 2%", changes: { usePercentTrail: true, momPercentTrail: 3.0, mrPercentTrail: 2.0 } },
    { name: "Percent trail MOM 4% / MR 2.5%", changes: { usePercentTrail: true, momPercentTrail: 4.0, mrPercentTrail: 2.5 } },
    { name: "Time tighten 48bar 0.6x", changes: { useTimeTighten: true, timeTightenBars: 48, timeTightenFactor: 0.6 } },
    { name: "Time tighten 72bar 0.5x", changes: { useTimeTighten: true, timeTightenBars: 72, timeTightenFactor: 0.5 } },
    { name: "Parabolic trail 0.02/0.02/0.20", changes: { useParabolicTrail: true } },
    { name: "Parabolic trail 0.01/0.01/0.15", changes: { useParabolicTrail: true, parabolicStart: 0.01, parabolicIncrement: 0.01, parabolicMax: 0.15 } },
    { name: "Vol-adaptive trail 1.3x/0.7x", changes: { useVolAdaptiveTrail: true } },
    { name: "Trail from close (not high)", changes: { useTrailFromClose: true } },

    // === GROUP 4: ALTERNATIVE EXIT SIGNALS ===
    { name: "EMA crossover exit for MOM", changes: { useEmaCrossExit: true } },
    { name: "EMA floor exit (close < fast EMA)", changes: { useEmaFloorExit: true } },
    { name: "Keltner exit 2.5x ATR", changes: { useKeltnerExit: true, keltnerMult: 2.5 } },
    { name: "Keltner exit 3.0x ATR", changes: { useKeltnerExit: true, keltnerMult: 3.0 } },
    { name: "Chandelier MOM 3x ATR from high", changes: { useChandelierMom: true, chandelierMomMult: 3.0 } },
    { name: "Chandelier MOM 4x ATR from high", changes: { useChandelierMom: true, chandelierMomMult: 4.0 } },
    { name: "HTF trend filter (EMA100)", changes: { useHTFTrendFilter: true } },
    { name: "MOM pct PT 8%", changes: { useMomPctPT: true, momPctPT: 8.0 } },
    { name: "MOM pct PT 10%", changes: { useMomPctPT: true, momPctPT: 10.0 } },
    { name: "MOM ATR PT 4x", changes: { useMomATRProfitTarget: true, momATRPTMult: 4.0 } },
    { name: "Remove MR PT cap", changes: { removeMrPTCap: true } },

    // === GROUP 5: MR SPECIFIC ===
    { name: "MR Profit Chandelier 1.5x ATR @3%", changes: { useProfitChandelier: true, chandelierATRMult: 1.5, chandelierActivatePnl: 3.0 } },
    { name: "MR Profit Chandelier 2.0x ATR @2%", changes: { useProfitChandelier: true, chandelierATRMult: 2.0, chandelierActivatePnl: 2.0 } },
    { name: "MR RSI dynamic 75 @3% PnL", changes: { useRsiSuppression: true, momRsiSuppressAbovePnl: 99, mrRsiDynamicThresh: 75, mrRsiDynamicAbovePnl: 3.0 } },

    // === GROUP 6: COMBOS (user's proposed v4) ===
    { name: "USER v4 PROPOSAL (all changes)", changes: {
      useProfitLockIn: true,
      useRsiSuppression: true, momRsiSuppressAbovePnl: 3.0, mrRsiDynamicThresh: 75, mrRsiDynamicAbovePnl: 3.0,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0,
      removeMrPTCap: true,
      useProfitChandelier: true, chandelierATRMult: 1.5, chandelierActivatePnl: 3.0,
    }},

    // === GROUP 7: CUSTOM COMBOS I WANT TO TEST ===
    { name: "COMBO: ProfitLock + DynRSI20", changes: {
      useProfitLockIn: true,
      useDynamicMomRsi: true, dynamicMomRsiProfitThresh: 3.0, dynamicMomRsiNewExit: 20,
    }},
    { name: "COMBO: ProfitLock + RSI Suppress", changes: {
      useProfitLockIn: true,
      useRsiSuppression: true, momRsiSuppressAbovePnl: 3.0, mrRsiDynamicThresh: 75, mrRsiDynamicAbovePnl: 3.0,
    }},
    { name: "COMBO: ProfitLock + ExtTrail + DynRSI", changes: {
      useProfitLockIn: true,
      useDynamicMomRsi: true, dynamicMomRsiProfitThresh: 3.0, dynamicMomRsiNewExit: 20,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0,
    }},
    { name: "COMBO: ProfitLock + RSI Suppress + ExtTrail", changes: {
      useProfitLockIn: true,
      useRsiSuppression: true, momRsiSuppressAbovePnl: 3.0,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0,
    }},
    { name: "COMBO: BreakevenOnly + DynRSI + TimeTighten", changes: {
      useBreakevenOnly: true, breakevenTrigger: 2.0,
      useDynamicMomRsi: true, dynamicMomRsiProfitThresh: 3.0, dynamicMomRsiNewExit: 20,
      useTimeTighten: true, timeTightenBars: 48, timeTightenFactor: 0.6,
    }},
    { name: "COMBO: ProfitLock(tight) + RSI Suppress + ExtTrail + Chandelier", changes: {
      useProfitLockIn: true, lockBETrigger: 1.5, lockBELevel: 0.1, lockT1Trigger: 3.0, lockT1Level: 1.5, lockT2Trigger: 5.0, lockT2Level: 3.0,
      useRsiSuppression: true, momRsiSuppressAbovePnl: 3.0, mrRsiDynamicThresh: 75, mrRsiDynamicAbovePnl: 3.0,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0,
      useProfitChandelier: true, chandelierATRMult: 1.5, chandelierActivatePnl: 3.0,
    }},
    { name: "COMBO: ProfitLock + DynRSI15 + ExtTrail10x + Chandelier", changes: {
      useProfitLockIn: true,
      useDynamicMomRsi: true, dynamicMomRsiProfitThresh: 3.0, dynamicMomRsiNewExit: 15,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 10.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 7.0,
      removeMrPTCap: true,
      useProfitChandelier: true, chandelierATRMult: 1.5, chandelierActivatePnl: 3.0,
    }},
    { name: "COMBO: ProfitLock + Min10Bars + ExtTrail", changes: {
      useProfitLockIn: true,
      useMinBarsBeforeRsi: true, minBarsBeforeRsi: 10,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0,
    }},
    { name: "COMBO: ProfitLock + HTF Filter + ExtTrail", changes: {
      useProfitLockIn: true,
      useHTFTrendFilter: true,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0,
    }},
    { name: "KITCHEN SINK: Lock+Suppress+ExtTrail+NoPTCap+Chandelier+TimeTighten", changes: {
      useProfitLockIn: true,
      useRsiSuppression: true, momRsiSuppressAbovePnl: 3.0, mrRsiDynamicThresh: 75, mrRsiDynamicAbovePnl: 3.0,
      useExtendedTrail: true, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0, mrExtTrailTrigger: 3.0, mrExtTrailMult: 6.0,
      removeMrPTCap: true,
      useProfitChandelier: true, chandelierATRMult: 1.5, chandelierActivatePnl: 3.0,
      useTimeTighten: true, timeTightenBars: 72, timeTightenFactor: 0.6,
    }},
  ];
}

// =============================================================================
// SUB-PERIOD ANALYSIS
// =============================================================================
function periodMetrics(trades, finalEquity, initialCapital, startDate, endDate) {
  const filtered = trades.filter(t => {
    const entryTime = candles_g[t.entryBar].time;
    return entryTime >= startDate.getTime() && entryTime < endDate.getTime();
  });
  if (filtered.length === 0) return null;
  let eq = initialCapital;
  let peak = eq, maxDD = 0;
  for (const t of filtered) {
    eq *= (1 + t.pnlPct / 100);
    if (eq > peak) peak = eq;
    const dd = (peak - eq) / peak * 100;
    if (dd > maxDD) maxDD = dd;
  }
  return {
    trades: filtered.length,
    winRate: filtered.filter(t => t.pnlPct > 0).length / filtered.length * 100,
    totalReturn: (eq / initialCapital - 1) * 100,
    maxDD,
    avgGiveback: filtered.reduce((s,t) => s + (t.maxUnrealizedPct - t.pnlPct), 0) / filtered.length,
  };
}

// =============================================================================
// MAIN
// =============================================================================
let candles_g; // global for period analysis

async function main() {
  console.log("Fetching BTCUSDT 1H data from Binance...");
  const startTime = new Date("2023-01-01T00:00:00Z").getTime();
  const endTime = Date.now();
  candles_g = await fetchKlines("BTCUSDT", "1h", startTime, endTime);
  console.log(`Fetched ${candles_g.length} candles`);

  console.log("Pre-computing indicators...");
  const ind = precompute(candles_g);

  const variants = getVariants();
  console.log(`\nRunning ${variants.length} variants...\n`);

  const results = [];
  for (const v of variants) {
    const cfg = { ...CONFIG_BASE, ...v.changes };
    const { trades, finalEquity } = runBacktest(ind, cfg);
    const m = metrics(trades, finalEquity, cfg.initialCapital);

    // Sub-period: 2025-01-01 to now (bear market test)
    const bearPeriod = periodMetrics(trades, finalEquity, cfg.initialCapital,
      new Date("2025-01-01"), new Date("2026-12-31"));

    results.push({ name: v.name, m, bearPeriod, trades });
  }

  // Sort by total return
  const baseline = results[0];

  // =============================================================================
  // OUTPUT REPORT
  // =============================================================================
  const lines = [];
  const p = (v, d=2) => v.toFixed(d);

  lines.push("=".repeat(120));
  lines.push("  EXHAUSTIVE EXIT IMPROVEMENT RESEARCH — BTCUSDT 1H — 2023-01-01 to 2026-05-14");
  lines.push("  Each variant tested independently against " + candles_g.length + " candles");
  lines.push("=".repeat(120));

  // MAIN COMPARISON TABLE
  lines.push("\n" + "=".repeat(120));
  lines.push("  MAIN COMPARISON TABLE (sorted by total return)");
  lines.push("=".repeat(120));

  const sorted = [...results].sort((a, b) => b.m.totalReturn - a.m.totalReturn);
  const hdr = `${"#".padStart(3)} ${"Variant".padEnd(52)} ${"Return%".padStart(9)} ${"vs Base".padStart(8)} ${"WinRate".padStart(8)} ${"PF".padStart(6)} ${"MaxDD%".padStart(7)} ${"Sharpe".padStart(7)} ${"GiveB%".padStart(7)} ${"Worst5".padStart(7)} ${"Cat".padStart(4)} ${"Trades".padStart(7)}`;
  lines.push(hdr);
  lines.push("-".repeat(120));

  for (let i = 0; i < sorted.length; i++) {
    const r = sorted[i];
    const diff = r.m.totalReturn - baseline.m.totalReturn;
    const diffStr = (diff >= 0 ? "+" : "") + p(diff, 1);
    const isBase = r.name === "v3 BASELINE";
    const marker = isBase ? ">>>" : String(i + 1).padStart(3);
    lines.push(`${marker} ${r.name.padEnd(52)} ${p(r.m.totalReturn, 1).padStart(9)} ${diffStr.padStart(8)} ${p(r.m.winRate, 1).padStart(8)} ${p(r.m.profitFactor, 2).padStart(6)} ${p(r.m.maxDD, 1).padStart(7)} ${p(r.m.sharpe, 3).padStart(7)} ${p(r.m.avgGiveback, 2).padStart(7)} ${String(r.m.worstGivebacks).padStart(7)} ${String(r.m.catastrophicReversals).padStart(4)} ${String(r.m.trades).padStart(7)}`);
  }

  // BEAR MARKET SUB-PERIOD
  lines.push("\n" + "=".repeat(100));
  lines.push("  BEAR MARKET TEST (2025-01-01 to present) — sorted by return");
  lines.push("=".repeat(100));

  const bearSorted = [...results].filter(r => r.bearPeriod).sort((a, b) => b.bearPeriod.totalReturn - a.bearPeriod.totalReturn);
  lines.push(`${"#".padStart(3)} ${"Variant".padEnd(52)} ${"Return%".padStart(9)} ${"WinRate".padStart(8)} ${"MaxDD%".padStart(7)} ${"GiveB%".padStart(7)} ${"Trades".padStart(7)}`);
  lines.push("-".repeat(100));
  for (let i = 0; i < bearSorted.length; i++) {
    const r = bearSorted[i];
    const bp = r.bearPeriod;
    lines.push(`${String(i+1).padStart(3)} ${r.name.padEnd(52)} ${p(bp.totalReturn, 1).padStart(9)} ${p(bp.winRate, 1).padStart(8)} ${p(bp.maxDD, 1).padStart(7)} ${p(bp.avgGiveback, 2).padStart(7)} ${String(bp.trades).padStart(7)}`);
  }

  // DETAILED ANALYSIS OF TOP 10
  lines.push("\n" + "=".repeat(100));
  lines.push("  TOP 10 VARIANTS — DETAILED BREAKDOWN");
  lines.push("=".repeat(100));

  for (let i = 0; i < Math.min(10, sorted.length); i++) {
    const r = sorted[i];
    const m = r.m;
    lines.push(`\n--- #${i+1}: ${r.name} ---`);
    lines.push(`  Total Return: ${p(m.totalReturn, 1)}% | Trades: ${m.trades} (MOM: ${m.momTrades}, MR: ${m.mrTrades})`);
    lines.push(`  Win Rate: ${p(m.winRate, 1)}% | PF: ${p(m.profitFactor, 2)} | Sharpe: ${p(m.sharpe, 3)}`);
    lines.push(`  Avg Win: +${p(m.avgWin)}% | Avg Loss: ${p(m.avgLoss)}% | Max DD: ${p(m.maxDD, 1)}%`);
    lines.push(`  Avg Giveback: ${p(m.avgGiveback)}% (MOM: ${p(m.momGiveback)}%, MR: ${p(m.mrGiveback)}%)`);
    lines.push(`  Worst Givebacks (>=5% peak, <3% exit): ${m.worstGivebacks} | Catastrophic (>=6% peak, loss): ${m.catastrophicReversals}`);
    lines.push(`  Avg Hold: ${p(m.avgBars, 0)} bars`);
    if (r.bearPeriod) {
      lines.push(`  Bear Period (2025+): ${p(r.bearPeriod.totalReturn, 1)}% return, ${p(r.bearPeriod.winRate, 1)}% WR, ${p(r.bearPeriod.maxDD, 1)}% maxDD`);
    }

    // Exit reason breakdown
    const reasons = {};
    for (const t of r.trades) {
      if (!reasons[t.exitReason]) reasons[t.exitReason] = { count: 0, totalPnl: 0, avgMax: 0 };
      reasons[t.exitReason].count++;
      reasons[t.exitReason].totalPnl += t.pnlPct;
      reasons[t.exitReason].avgMax += t.maxUnrealizedPct;
    }
    lines.push(`  Exit Breakdown:`);
    for (const [reason, d] of Object.entries(reasons).sort((a,b) => b[1].count - a[1].count)) {
      const avgPnl = d.totalPnl / d.count;
      const avgMax = d.avgMax / d.count;
      lines.push(`    ${reason.padEnd(18)} ${String(d.count).padStart(4)}x  avg ${p(avgPnl).padStart(7)}%  peak ${p(avgMax).padStart(7)}%  giveback ${p(avgMax - avgPnl).padStart(7)}%`);
    }
  }

  // IMPROVEMENT RECOMMENDATIONS
  lines.push("\n" + "=".repeat(100));
  lines.push("  RESEARCH CONCLUSIONS & RECOMMENDATIONS");
  lines.push("=".repeat(100));

  // Find best in each category
  const bestReturn = sorted[0];
  const bestSharpe = [...results].sort((a,b) => b.m.sharpe - a.m.sharpe)[0];
  const bestGiveback = [...results].sort((a,b) => a.m.avgGiveback - b.m.avgGiveback)[0];
  const bestDD = [...results].sort((a,b) => a.m.maxDD - b.m.maxDD)[0];
  const bestPF = [...results].sort((a,b) => b.m.profitFactor - a.m.profitFactor)[0];
  const bestBear = bearSorted[0];

  lines.push(`\n  Best Total Return: ${bestReturn.name} (${p(bestReturn.m.totalReturn, 1)}%)`);
  lines.push(`  Best Sharpe:       ${bestSharpe.name} (${p(bestSharpe.m.sharpe, 3)})`);
  lines.push(`  Best Giveback:     ${bestGiveback.name} (${p(bestGiveback.m.avgGiveback, 2)}%)`);
  lines.push(`  Best Max DD:       ${bestDD.name} (${p(bestDD.m.maxDD, 1)}%)`);
  lines.push(`  Best Profit Factor:${bestPF.name} (${p(bestPF.m.profitFactor, 2)})`);
  if (bestBear) lines.push(`  Best Bear Period:  ${bestBear.name} (${p(bestBear.bearPeriod.totalReturn, 1)}%)`);

  // Compare user proposal vs best alternatives
  const userResult = results.find(r => r.name.includes("USER v4 PROPOSAL"));
  if (userResult) {
    lines.push(`\n  USER v4 PROPOSAL: ${p(userResult.m.totalReturn, 1)}% return, ${p(userResult.m.sharpe, 3)} sharpe, ${p(userResult.m.avgGiveback, 2)}% giveback`);
    lines.push(`  vs BASELINE:      ${p(baseline.m.totalReturn, 1)}% return, ${p(baseline.m.sharpe, 3)} sharpe, ${p(baseline.m.avgGiveback, 2)}% giveback`);
    lines.push(`  vs BEST:          ${p(bestReturn.m.totalReturn, 1)}% return (${bestReturn.name})`);
  }

  const report = lines.join("\n");
  const fs = await import('fs');
  fs.writeFileSync('audit_report.txt', report);
  console.log("Report written to audit_report.txt");
  console.log("\n" + report);
}

main().catch(e => { console.error(e); process.exit(1); });
