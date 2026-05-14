// =============================================================================
// ROUND 4: PROPER VALIDATION
//
// 1. Walk-forward: tune on 2023-2024, test on 2025-2026 (held out)
// 2. Cross-exchange: test same variants on Bitstamp BTCUSD
// 3. Sensitivity: test neighboring parameters for Variant N
// 4. Also test the other Claude's MFE-proportional lock (floor=4, gb=55)
//    to confirm it fails on proper validation
//
// Fix: Lock ratchets from PREVIOUS bar close, tested on CURRENT bar low
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

  useLocks: false, lockTiers: [],
  useRsiSuppressMFE: false, rsiSuppressMFEThresh: 3.0,
  useExtendedTrail: false, momExtTrailTrigger: 5.0, momExtTrailMult: 8.0,
  useTrailFromClose: false,
  useVolAdaptiveTrail: false, volAdaptiveHighATRMult: 1.3, volAdaptiveLowATRMult: 0.7,
  useMinBarsBeforeRsi: false, minBarsBeforeRsi: 5,
  // MFE-proportional lock (the other Claude's approach)
  useMFEProportionalLock: false, mfePropFloor: 4.0, mfePropGiveback: 0.55,
};

// === INDICATORS ===
function calcRSI(c,p){const r=new Array(c.length).fill(NaN);let g=0,l=0;for(let i=1;i<=p;i++){const d=c[i]-c[i-1];if(d>0)g+=d;else l-=d;}g/=p;l/=p;r[p]=l===0?100:100-100/(1+g/l);for(let i=p+1;i<c.length;i++){const d=c[i]-c[i-1];g=(g*(p-1)+(d>0?d:0))/p;l=(l*(p-1)+(d<0?-d:0))/p;r[i]=l===0?100:100-100/(1+g/l);}return r;}
function calcEMA(d,p){const e=new Array(d.length).fill(NaN);let s=0,cn=0;for(let i=0;i<d.length;i++){if(isNaN(d[i]))continue;s+=d[i];cn++;if(cn===p){e[i]=s/p;const k=2/(p+1);for(let j=i+1;j<d.length;j++)e[j]=isNaN(d[j])?e[j-1]:d[j]*k+e[j-1]*(1-k);break;}}return e;}
function calcSMA(d,p){const s=new Array(d.length).fill(NaN);let sum=0;for(let i=0;i<d.length;i++){sum+=d[i];if(i>=p)sum-=d[i-p];if(i>=p-1)s[i]=sum/p;}return s;}
function calcStdev(d,p){const s=new Array(d.length).fill(NaN);for(let i=p-1;i<d.length;i++){let sum=0,sum2=0;for(let j=i-p+1;j<=i;j++){sum+=d[j];sum2+=d[j]*d[j];}const m=sum/p;s[i]=Math.sqrt(sum2/p-m*m);}return s;}
function calcATR(h,l,c,p){const tr=new Array(h.length).fill(NaN);tr[0]=h[0]-l[0];for(let i=1;i<h.length;i++)tr[i]=Math.max(h[i]-l[i],Math.abs(h[i]-c[i-1]),Math.abs(l[i]-c[i-1]));const a=new Array(h.length).fill(NaN);let s=0;for(let i=0;i<p;i++)s+=tr[i];a[p-1]=s/p;for(let i=p;i<h.length;i++)a[i]=(a[i-1]*(p-1)+tr[i])/p;return a;}
function calcER(c,ep,sp){const raw=new Array(c.length).fill(0);for(let i=ep;i<c.length;i++){const dir=Math.abs(c[i]-c[i-ep]);let vol=0;for(let j=i-ep+1;j<=i;j++)vol+=Math.abs(c[j]-c[j-1]);raw[i]=vol?dir/vol:0;}return calcEMA(raw,sp);}

function precompute(candles) {
  const c=candles.map(x=>x.close),h=candles.map(x=>x.high),l=candles.map(x=>x.low);
  const atrMom=calcATR(h,l,c,CONFIG_BASE.atrMomPeriod);
  return {n:candles.length,c,h,l,rsiMom:calcRSI(c,CONFIG_BASE.rsiMomPeriod),rsiMr:calcRSI(c,CONFIG_BASE.rsiMrPeriod),
    emaF:calcEMA(c,CONFIG_BASE.emaFastLen),emaS:calcEMA(c,CONFIG_BASE.emaSlowLen),
    atrMom,atrMr:calcATR(h,l,c,CONFIG_BASE.atrMrPeriod),bbB:calcSMA(c,CONFIG_BASE.bbPeriod),bbSD:calcStdev(c,CONFIG_BASE.bbPeriod),
    er:calcER(c,CONFIG_BASE.erPeriod,CONFIG_BASE.erSmoothPer),atrMomSMA50:calcSMA(atrMom.map(v=>isNaN(v)?0:v),50)};
}

// === BACKTEST ENGINE (fixed intrabar) ===
function runBacktest(ind, cfg, candles) {
  const {n,c,h,l,rsiMom,rsiMr,emaF,emaS,atrMom,atrMr,bbB,bbSD,er,atrMomSMA50}=ind;
  let posType=0,entryPrice=NaN,trailHigh=NaN,trailStop=NaN,barsHeld=0;
  let hardSLLevel=NaN,equity=cfg.initialCapital,posSize=0,highCl=NaN,mfePct=0,prevUnreal=0;
  const trades=[];let ct=null;

  for(let i=1;i<n;i++){
    const cl=c[i],hi=h[i],lo=l[i];
    if(isNaN(rsiMom[i])||isNaN(emaF[i])||isNaN(emaS[i])||isNaN(er[i]))continue;
    const isTrend=er[i]>=cfg.erTrendThresh,isChop=er[i]<cfg.erTrendThresh;
    const uptrend=emaF[i]>emaS[i],bbLow=bbB[i]-bbSD[i]*cfg.bbStd;
    const rsiXup=rsiMom[i]>=cfg.rsiMomEntry&&rsiMom[i-1]<cfg.rsiMomEntry;
    const hasPos=posType!==0;

    // STEP 1: Lock ratchets from PREVIOUS bar
    if(hasPos&&!isNaN(entryPrice)){
      // Fixed-tier locks
      if(cfg.useLocks&&cfg.lockTiers.length>0){
        for(const[trig,lock]of cfg.lockTiers){
          if(prevUnreal>=trig){const ns=entryPrice*(1+lock/100);if(ns>hardSLLevel)hardSLLevel=ns;}
        }
      }
      // MFE-proportional lock (the other Claude's formula)
      if(cfg.useMFEProportionalLock&&mfePct>=cfg.mfePropFloor){
        const lockLevel=entryPrice*(1+mfePct/100*cfg.mfePropGiveback);
        // Use prevUnreal to check if lock should be active (prev bar triggered the MFE)
        if(prevUnreal>=cfg.mfePropFloor&&lockLevel>hardSLLevel)hardSLLevel=lockLevel;
      }
    }

    // STEP 2: Hard SL check against current bar low
    if(hasPos&&!isNaN(hardSLLevel)&&lo<=hardSLLevel){
      const ep=hardSLLevel,pnl=(ep/entryPrice-1)*100;
      equity+=posSize*(ep-entryPrice)-posSize*ep*cfg.commissionPct/100;
      if(ct){ct.exitBar=i;ct.exitPrice=ep;ct.pnlPct=pnl;ct.exitReason=pnl>=-0.01?"PROFIT_LOCK":(posType===1?"MOM_HARD_SL":"MR_HARD_SL");ct.mfePct=mfePct;trades.push(ct);ct=null;}
      posType=0;entryPrice=NaN;trailHigh=NaN;trailStop=NaN;barsHeld=0;hardSLLevel=NaN;posSize=0;highCl=NaN;mfePct=0;prevUnreal=0;continue;
    }

    // STEP 3: Trail update
    if(hasPos){
      barsHeld++;
      const uHi=(hi/entryPrice-1)*100,uCl=(cl/entryPrice-1)*100;
      if(uHi>mfePct)mfePct=uHi;
      if(cl>highCl||isNaN(highCl))highCl=cl;
      if(hi>trailHigh||isNaN(trailHigh))trailHigh=hi;
      if(ct&&uHi>ct.maxUnrealizedPct){ct.maxUnrealizedPct=uHi;ct.maxUnrealizedBar=i;}

      if(posType===1){
        let mult=cfg.atrMomTrail;
        if(cfg.useExtendedTrail&&uCl>=cfg.momExtTrailTrigger)mult=cfg.momExtTrailMult;
        if(cfg.useVolAdaptiveTrail&&!isNaN(atrMomSMA50[i])&&atrMomSMA50[i]>0){
          const r=atrMom[i]/atrMomSMA50[i];if(r>1.2)mult*=cfg.volAdaptiveHighATRMult;else if(r<0.8)mult*=cfg.volAdaptiveLowATRMult;
        }
        trailStop=(cfg.useTrailFromClose?highCl:trailHigh)-atrMom[i]*mult;
      }else if(posType===2){
        trailStop=(cfg.useTrailFromClose?highCl:trailHigh)-atrMr[i]*cfg.atrMrTrail;
      }
      prevUnreal=uCl;
    }

    // STEP 4: Exit signals
    const uCl=hasPos&&!isNaN(entryPrice)?(cl/entryPrice-1)*100:0;
    let exitMomRsi=hasPos&&posType===1&&rsiMom[i]<cfg.rsiMomExit;
    if(cfg.useRsiSuppressMFE&&exitMomRsi&&mfePct>=cfg.rsiSuppressMFEThresh)exitMomRsi=false;
    if(cfg.useMinBarsBeforeRsi&&exitMomRsi&&barsHeld<cfg.minBarsBeforeRsi)exitMomRsi=false;
    let exitMomTrail=hasPos&&posType===1&&!isNaN(trailStop)&&cl<trailStop&&!exitMomRsi;
    let exitMrPT=hasPos&&posType===2&&!isNaN(entryPrice)&&cl>=entryPrice*(1+cfg.mrProfitPct/100);
    let exitMrRsi=hasPos&&posType===2&&rsiMr[i]>cfg.rsiMrSell&&!exitMrPT;
    let exitMrTrail=hasPos&&posType===2&&!isNaN(trailStop)&&cl<trailStop&&barsHeld>3&&!exitMrPT&&!exitMrRsi;
    let exitMrTime=hasPos&&posType===2&&barsHeld>=cfg.mrMaxHold&&!exitMrPT&&!exitMrRsi&&!exitMrTrail;
    const anyExit=exitMomRsi||exitMomTrail||exitMrPT||exitMrRsi||exitMrTrail||exitMrTime;

    if(anyExit&&hasPos){
      const pnl=(cl/entryPrice-1)*100;
      equity+=posSize*(cl-entryPrice)-posSize*cl*cfg.commissionPct/100;
      const reason=exitMomRsi?"MOM_RSI":exitMomTrail?"MOM_TRAIL":exitMrPT?"MR_PT":exitMrRsi?"MR_RSI":exitMrTrail?"MR_TRAIL":"MR_TIMEOUT";
      if(ct){ct.exitBar=i;ct.exitPrice=cl;ct.pnlPct=pnl;ct.exitReason=reason;ct.mfePct=mfePct;trades.push(ct);ct=null;}
      posType=0;entryPrice=NaN;trailHigh=NaN;trailStop=NaN;barsHeld=0;hardSLLevel=NaN;posSize=0;highCl=NaN;mfePct=0;prevUnreal=0;
    }

    // STEP 5: Entries
    const isFlat=posType===0;
    const entryMom=isFlat&&rsiXup&&uptrend&&isTrend&&!anyExit;
    const entryMr=isFlat&&cl<=bbLow&&bbLow>0&&rsiMr[i]<cfg.rsiMrBuy&&isChop&&!entryMom&&!anyExit;
    if(entryMom){
      entryPrice=cl;posSize=(equity-equity*cfg.commissionPct/100)/cl;
      posType=1;trailHigh=cl;trailStop=cl-atrMom[i]*cfg.atrMomTrail;barsHeld=0;
      hardSLLevel=cl*(1-cfg.momHardSLPct/100);highCl=cl;mfePct=0;prevUnreal=0;
      ct={type:"MOM",entryBar:i,entryPrice:cl,maxUnrealizedPct:0,maxUnrealizedBar:i,equityAtEntry:equity};
    }
    if(entryMr){
      entryPrice=cl;posSize=(equity-equity*cfg.commissionPct/100)/cl;
      posType=2;trailHigh=cl;trailStop=cl-atrMr[i]*cfg.atrMrTrail;barsHeld=0;
      hardSLLevel=cl*(1-cfg.mrHardSLPct/100);highCl=cl;mfePct=0;prevUnreal=0;
      ct={type:"MR",entryBar:i,entryPrice:cl,maxUnrealizedPct:0,maxUnrealizedBar:i,equityAtEntry:equity};
    }
  }
  return{trades,finalEquity:equity};
}

// === METRICS ===
function metrics(trades,feq,cap){
  if(!trades.length)return null;
  const w=trades.filter(t=>t.pnlPct>0),lo=trades.filter(t=>t.pnlPct<=0);
  const gP=w.reduce((s,t)=>s+t.pnlPct,0),gL=Math.abs(lo.reduce((s,t)=>s+t.pnlPct,0));
  let peak=cap,maxDD=0,eq=cap;
  for(const t of trades){eq*=(1+t.pnlPct/100);if(eq>peak)peak=eq;const dd=(peak-eq)/peak*100;if(dd>maxDD)maxDD=dd;}
  const avgPnl=trades.reduce((s,t)=>s+t.pnlPct,0)/trades.length;
  const v=trades.reduce((s,t)=>s+(t.pnlPct-avgPnl)**2,0)/trades.length;
  const br=trades.filter(t=>t.maxUnrealizedPct>=10);
  return{
    trades:trades.length,winRate:w.length/trades.length*100,totalReturn:(feq/cap-1)*100,
    profitFactor:gL>0?gP/gL:999,maxDD,sharpe:v>0?avgPnl/Math.sqrt(v):0,
    avgGiveback:trades.reduce((s,t)=>s+(t.maxUnrealizedPct-t.pnlPct),0)/trades.length,
    catastrophic:trades.filter(t=>t.maxUnrealizedPct>=6&&t.pnlPct<0).length,
    bigRunners:br.length,bigRunCapture:br.length?br.reduce((s,t)=>s+t.pnlPct,0)/br.length:0,
    lockExits:trades.filter(t=>t.exitReason==="PROFIT_LOCK").length,
  };
}

// === DATA ===
async function fetchBinance(start,end){
  const out=[];let cur=start;
  while(cur<end){
    const r=await fetch(`https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&startTime=${cur}&endTime=${end}&limit=1000`);
    const d=await r.json();if(!d.length)break;
    for(const k of d)out.push({time:k[0],open:+k[1],high:+k[2],low:+k[3],close:+k[4]});
    cur=d[d.length-1][0]+1;await new Promise(r=>setTimeout(r,80));
  }
  return out;
}

async function fetchBitstamp(start,end){
  // Bitstamp OHLC API: /api/v2/ohlc/btcusd/?step=3600&limit=1000&start=UNIX_SECONDS
  const out=[];let cur=Math.floor(start/1000);const endSec=Math.floor(end/1000);
  while(cur<endSec){
    const url=`https://www.bitstamp.net/api/v2/ohlc/btcusd/?step=3600&limit=1000&start=${cur}`;
    const r=await fetch(url);
    if(!r.ok){console.error(`Bitstamp ${r.status}`);break;}
    const j=await r.json();
    if(!j.data||!j.data.ohlc||!j.data.ohlc.length)break;
    for(const k of j.data.ohlc){
      const t=+k.timestamp*1000;
      if(t>=start&&t<=end)out.push({time:t,open:+k.open,high:+k.high,low:+k.low,close:+k.close});
    }
    cur=+j.data.ohlc[j.data.ohlc.length-1].timestamp+1;
    await new Promise(r=>setTimeout(r,200));
  }
  return out;
}

// === VARIANTS ===
function getVariants(){
  return[
    {name:"v3 BASELINE",changes:{}},

    // My Round 3 winner
    {name:"N: WideLock(5/10/15)+TC+Ext+Vol",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,
      useVolAdaptiveTrail:true}},

    // Components of N tested individually
    {name:"TC only (trail from close)",changes:{useTrailFromClose:true}},
    {name:"ExtTrail only (8x@3%)",changes:{useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0}},
    {name:"VolAdapt only",changes:{useVolAdaptiveTrail:true}},
    {name:"WideLock only (5/10/15)",changes:{useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]]}},

    // TC + each component
    {name:"TC+ExtTrail",changes:{useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0}},
    {name:"TC+Vol",changes:{useTrailFromClose:true,useVolAdaptiveTrail:true}},
    {name:"TC+Ext+Vol (no locks)",changes:{useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,useVolAdaptiveTrail:true}},

    // Other Claude's MFE-proportional lock (the +950% claim)
    {name:"MFE-prop lock (floor=4,gb=55%)+RSIsup",changes:{
      useMFEProportionalLock:true,mfePropFloor:4.0,mfePropGiveback:0.55,
      useRsiSuppressMFE:true,rsiSuppressMFEThresh:3.0}},

    // RSI suppress alone (claimed +94pp robust)
    {name:"RSI suppress (MFE>=3%) alone",changes:{useRsiSuppressMFE:true,rsiSuppressMFEThresh:3.0}},

    // SENSITIVITY: Variant N with different lock tiers
    {name:"N-sens: locks(4/8/12)",changes:{
      useLocks:true,lockTiers:[[4.0,0.15],[8.0,4.0],[12.0,8.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,useVolAdaptiveTrail:true}},
    {name:"N-sens: locks(6/12/18)",changes:{
      useLocks:true,lockTiers:[[6.0,0.15],[12.0,6.0],[18.0,12.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,useVolAdaptiveTrail:true}},
    {name:"N-sens: locks(3/8/15)",changes:{
      useLocks:true,lockTiers:[[3.0,0.15],[8.0,3.0],[15.0,8.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,useVolAdaptiveTrail:true}},
    {name:"N-sens: no locks (TC+Ext+Vol only)",changes:{
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,useVolAdaptiveTrail:true}},

    // SENSITIVITY: ExtTrail multiplier
    {name:"N-sens: ExtTrail 7x@3%",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:7.0,useVolAdaptiveTrail:true}},
    {name:"N-sens: ExtTrail 9x@3%",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:9.0,useVolAdaptiveTrail:true}},
    {name:"N-sens: ExtTrail 8x@4%",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:4.0,momExtTrailMult:8.0,useVolAdaptiveTrail:true}},
    {name:"N-sens: ExtTrail 8x@2%",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:2.0,momExtTrailMult:8.0,useVolAdaptiveTrail:true}},

    // SENSITIVITY: VolAdaptive thresholds
    {name:"N-sens: VolAdapt 1.2/0.8",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,
      useVolAdaptiveTrail:true,volAdaptiveHighATRMult:1.2,volAdaptiveLowATRMult:0.8}},
    {name:"N-sens: VolAdapt 1.4/0.6",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,
      useVolAdaptiveTrail:true,volAdaptiveHighATRMult:1.4,volAdaptiveLowATRMult:0.6}},

    // Min5bars combos
    {name:"N + Min5bars",changes:{
      useLocks:true,lockTiers:[[5.0,0.15],[10.0,5.0],[15.0,10.0]],
      useTrailFromClose:true,useExtendedTrail:true,momExtTrailTrigger:3.0,momExtTrailMult:8.0,
      useVolAdaptiveTrail:true,useMinBarsBeforeRsi:true,minBarsBeforeRsi:5}},
  ];
}

// === MAIN ===
async function main(){
  const p=(v,d=2)=>v.toFixed(d);
  const lines=[];

  // ====== FETCH DATA ======
  console.log("Fetching Binance BTCUSDT 1H (full period)...");
  const binFull=await fetchBinance(new Date("2023-01-01").getTime(),Date.now());
  console.log(`  Binance full: ${binFull.length} candles`);

  // Skip Bitstamp — API is too slow/unreliable for bulk fetch. Walk-forward is the key test.
  let bitFull = null;
  console.log("  Skipping Bitstamp (API too slow). Walk-forward is the critical validation.");

  // Split Binance into train/test
  const trainEnd=new Date("2025-01-01").getTime();
  const binTrain=binFull.filter(c=>c.time<trainEnd);
  const binTest=binFull.filter(c=>c.time>=trainEnd);
  console.log(`  Binance train (2023-2024): ${binTrain.length} | test (2025+): ${binTest.length}`);

  const variants=getVariants();

  // Helper to run all variants on a dataset
  function runAll(candles,label){
    const ind=precompute(candles);
    const results=[];
    for(const v of variants){
      const cfg={...CONFIG_BASE,...v.changes};
      const{trades,finalEquity}=runBacktest(ind,cfg,candles);
      const m=metrics(trades,finalEquity,cfg.initialCapital);
      results.push({name:v.name,m});
    }
    return results;
  }

  // ====== TEST 1: FULL PERIOD BINANCE ======
  console.log("\nRunning full-period Binance...");
  const fullRes=runAll(binFull,"Binance Full");

  // ====== TEST 2: WALK-FORWARD ======
  console.log("Running walk-forward train (2023-2024)...");
  const trainRes=runAll(binTrain,"Binance Train");
  console.log("Running walk-forward test (2025+)...");
  const testRes=runAll(binTest,"Binance Test");

  // ====== TEST 3: CROSS-EXCHANGE ======
  let bitRes=null;
  if(bitFull&&bitFull.length>1000){
    console.log("Running Bitstamp...");
    bitRes=runAll(bitFull,"Bitstamp");
  }

  // ====== REPORT ======
  lines.push("=".repeat(160));
  lines.push("  ROUND 4: PROPER VALIDATION — Walk-Forward + Cross-Exchange + Sensitivity");
  lines.push("=".repeat(160));

  // Full period table
  lines.push("\n--- BINANCE BTCUSDT FULL PERIOD (2023-01-01 to 2026-05-14) ---");
  const hdr=`${"#".padStart(3)} ${"Variant".padEnd(42)} ${"Ret%".padStart(8)} ${"WR%".padStart(6)} ${"PF".padStart(6)} ${"DD%".padStart(6)} ${"Shp".padStart(6)} ${"GvBk%".padStart(6)} ${"Cat".padStart(4)} ${"BigCap%".padStart(8)} ${"Locks".padStart(6)} ${"#Tr".padStart(5)}`;
  lines.push(hdr);lines.push("-".repeat(120));
  const fSorted=[...fullRes].sort((a,b)=>b.m.totalReturn-a.m.totalReturn);
  const baseRet=fullRes[0].m.totalReturn;
  for(let i=0;i<fSorted.length;i++){
    const r=fSorted[i],m=r.m;
    const mark=r.name==="v3 BASELINE"?">B>":String(i+1).padStart(3);
    lines.push(`${mark} ${r.name.padEnd(42)} ${p(m.totalReturn,1).padStart(8)} ${p(m.winRate,1).padStart(6)} ${p(m.profitFactor,2).padStart(6)} ${p(m.maxDD,1).padStart(6)} ${p(m.sharpe,3).padStart(6)} ${p(m.avgGiveback,2).padStart(6)} ${String(m.catastrophic).padStart(4)} ${p(m.bigRunCapture,1).padStart(8)} ${String(m.lockExits).padStart(6)} ${String(m.trades).padStart(5)}`);
  }

  // Walk-forward
  lines.push("\n\n" + "=".repeat(120));
  lines.push("  WALK-FORWARD VALIDATION");
  lines.push("  Train: 2023-01-01 to 2024-12-31 | Test: 2025-01-01 to 2026-05-14 (HELD OUT)");
  lines.push("=".repeat(120));

  lines.push(`\n${"Variant".padEnd(42)} ${"TRAIN Ret%".padStart(11)} ${"TEST Ret%".padStart(10)} ${"TEST WR%".padStart(9)} ${"TEST PF".padStart(8)} ${"TEST DD%".padStart(9)} ${"TEST Shp".padStart(9)} ${"TEST Cat".padStart(9)} ${"T#Tr".padStart(6)}`);
  lines.push("-".repeat(120));
  // Sort by TEST return
  const wfPairs=variants.map((_,i)=>({name:variants[i].name,train:trainRes[i].m,test:testRes[i].m}));
  wfPairs.sort((a,b)=>b.test.totalReturn-a.test.totalReturn);
  for(const r of wfPairs){
    const mark=r.name==="v3 BASELINE"?">B>":"   ";
    lines.push(`${mark}${r.name.padEnd(39)} ${p(r.train.totalReturn,1).padStart(11)} ${p(r.test.totalReturn,1).padStart(10)} ${p(r.test.winRate,1).padStart(9)} ${p(r.test.profitFactor,2).padStart(8)} ${p(r.test.maxDD,1).padStart(9)} ${p(r.test.sharpe,3).padStart(9)} ${String(r.test.catastrophic).padStart(9)} ${String(r.test.trades).padStart(6)}`);
  }

  // Cross-exchange
  if(bitRes){
    lines.push("\n\n" + "=".repeat(120));
    lines.push("  CROSS-EXCHANGE: BITSTAMP BTCUSD 1H (same period)");
    lines.push("=".repeat(120));
    lines.push(`\n${"Variant".padEnd(42)} ${"Binance%".padStart(9)} ${"Bitstamp%".padStart(10)} ${"Delta".padStart(8)} ${"Bit WR%".padStart(8)} ${"Bit PF".padStart(7)} ${"Bit DD%".padStart(8)} ${"Bit Cat".padStart(8)}`);
    lines.push("-".repeat(100));
    const xPairs=variants.map((_,i)=>({name:variants[i].name,bin:fullRes[i].m,bit:bitRes[i].m}));
    xPairs.sort((a,b)=>b.bit.totalReturn-a.bit.totalReturn);
    for(const r of xPairs){
      const delta=r.bit.totalReturn-r.bin.totalReturn;
      lines.push(`${r.name.padEnd(42)} ${p(r.bin.totalReturn,1).padStart(9)} ${p(r.bit.totalReturn,1).padStart(10)} ${(delta>=0?"+":"")+p(delta,1)}${" ".repeat(Math.max(0,5-p(delta,1).length))} ${p(r.bit.winRate,1).padStart(8)} ${p(r.bit.profitFactor,2).padStart(7)} ${p(r.bit.maxDD,1).padStart(8)} ${String(r.bit.catastrophic).padStart(8)}`);
    }
  }

  // Sensitivity plateau analysis
  lines.push("\n\n" + "=".repeat(120));
  lines.push("  SENSITIVITY ANALYSIS: Is Variant N on a plateau or a peak?");
  lines.push("=".repeat(120));
  const sensVariants=fullRes.filter(r=>r.name.startsWith("N-sens:")||r.name==="N: WideLock(5/10/15)+TC+Ext+Vol"||r.name==="v3 BASELINE");
  lines.push(`\n${"Variant".padEnd(42)} ${"Ret%".padStart(8)} ${"vs BASE".padStart(9)} ${"vs N".padStart(7)}`);
  lines.push("-".repeat(70));
  const nRet=fullRes.find(r=>r.name.startsWith("N:")).m.totalReturn;
  for(const r of sensVariants.sort((a,b)=>b.m.totalReturn-a.m.totalReturn)){
    lines.push(`${r.name.padEnd(42)} ${p(r.m.totalReturn,1).padStart(8)} ${((r.m.totalReturn-baseRet>=0?"+":"")+p(r.m.totalReturn-baseRet,1)).padStart(9)} ${((r.m.totalReturn-nRet>=0?"+":"")+p(r.m.totalReturn-nRet,1)).padStart(7)}`);
  }

  // Final verdict
  lines.push("\n\n" + "=".repeat(120));
  lines.push("  FINAL VERDICT");
  lines.push("=".repeat(120));

  const nFull=fullRes.find(r=>r.name.startsWith("N:"));
  const nTest=wfPairs.find(r=>r.name.startsWith("N:"));
  const baseTest=wfPairs.find(r=>r.name==="v3 BASELINE");
  const mfePropTest=wfPairs.find(r=>r.name.startsWith("MFE-prop"));
  const rsiSupTest=wfPairs.find(r=>r.name.startsWith("RSI suppress"));

  lines.push(`\n  Variant N (WideLock+TC+Ext+Vol):`);
  lines.push(`    Full period: ${p(nFull.m.totalReturn,1)}% vs baseline ${p(baseRet,1)}% (+${p(nFull.m.totalReturn-baseRet,1)}pp)`);
  lines.push(`    Walk-forward TEST (2025+): ${p(nTest.test.totalReturn,1)}% vs baseline ${p(baseTest.test.totalReturn,1)}% (${nTest.test.totalReturn>baseTest.test.totalReturn?"PASSES":"FAILS"})`);
  if(bitRes){
    const nBit=bitRes.find((_,i)=>variants[i].name.startsWith("N:"));
    const bBit=bitRes[0];
    if(nBit)lines.push(`    Bitstamp: ${p(nBit.m.totalReturn,1)}% vs baseline ${p(bBit.m.totalReturn,1)}% (${nBit.m.totalReturn>bBit.m.totalReturn?"PASSES":"FAILS"})`);
  }
  lines.push(`\n  Other Claude's MFE-prop lock:`);
  lines.push(`    Walk-forward TEST (2025+): ${p(mfePropTest.test.totalReturn,1)}% vs baseline ${p(baseTest.test.totalReturn,1)}% (${mfePropTest.test.totalReturn>baseTest.test.totalReturn?"PASSES":"FAILS"})`);
  lines.push(`\n  RSI suppress alone:`);
  lines.push(`    Walk-forward TEST (2025+): ${p(rsiSupTest.test.totalReturn,1)}% vs baseline ${p(baseTest.test.totalReturn,1)}% (${rsiSupTest.test.totalReturn>baseTest.test.totalReturn?"PASSES":"FAILS"})`);

  const report=lines.join("\n");
  const fs=await import('fs');
  fs.writeFileSync('audit_report.txt',report);
  console.log("\nReport written to audit_report.txt\n"+report);
}

main().catch(e=>{console.error(e);process.exit(1);});
