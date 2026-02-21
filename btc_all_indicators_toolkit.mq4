//+------------------------------------------------------------------+
//|                        BTC Trading Toolkit — All Indicators       |
//|                        For FXCM MetaTrader 4                      |
//|                                                                    |
//|  HOW TO INSTALL:                                                   |
//|  1. Open MetaTrader 4                                              |
//|  2. Click File → Open Data Folder                                  |
//|  3. Go to MQL4 → Indicators                                       |
//|  4. Copy this file there                                           |
//|  5. In MT4: right-click Navigator → Refresh                       |
//|  6. Drag "btc_all_indicators_toolkit" onto your chart              |
//|                                                                    |
//|  HOW TO CHANGE VALUES:                                             |
//|  When you drag the indicator onto the chart, a popup appears.      |
//|  Click the "Inputs" tab — every value below is listed there.       |
//|  Change any number and click OK.                                   |
//|                                                                    |
//|  OR: Change the default values directly in this file.              |
//|  Look for lines like:                                              |
//|     input int EMA_Fast_Period = 21;                                |
//|  Change the number (21) to whatever you want.                      |
//|                                                                    |
//+------------------------------------------------------------------+

#property copyright "BTC Trading Toolkit"
#property link      ""
#property version   "1.00"
#property strict

// ==========================================================================
// This indicator draws ON TOP of price (overlay).
// RSI, MACD, ATR, HA streaks are shown in SEPARATE WINDOWS below the chart.
//
// We need separate_window for the oscillators.
// The main chart overlays (EMA, BB, etc.) are drawn using custom buffers.
//
// IMPORTANT: MT4 limits indicators to 8 buffers in one file.
// So this toolkit uses multiple chart objects and direct drawing.
// ==========================================================================

#property indicator_chart_window

// --------------------------------------------------------------------------
// We use 8 indicator buffers for the main chart overlay lines:
//   0 = EMA Fast
//   1 = EMA Mid
//   2 = EMA Slow
//   3 = EMA Ultra
//   4 = BB Upper
//   5 = BB Middle
//   6 = BB Lower
//   7 = Supertrend line
// --------------------------------------------------------------------------
#property indicator_buffers 8

#property indicator_color1 clrDodgerBlue      // EMA Fast
#property indicator_color2 clrOrange           // EMA Mid
#property indicator_color3 clrDeepPink         // EMA Slow
#property indicator_color4 clrMediumOrchid     // EMA Ultra
#property indicator_color5 clrCornflowerBlue   // BB Upper
#property indicator_color6 clrCornflowerBlue   // BB Middle
#property indicator_color7 clrCornflowerBlue   // BB Lower
#property indicator_color8 clrLime             // Supertrend

#property indicator_width1 1
#property indicator_width2 1
#property indicator_width3 2
#property indicator_width4 2
#property indicator_width5 1
#property indicator_width6 1
#property indicator_width7 1
#property indicator_width8 2

#property indicator_style6 STYLE_DOT          // BB Middle is dotted


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 1: EMA (Exponential Moving Averages)
//
//  What it does: Smooths price to show trend direction.
//  - Price ABOVE the EMA = bullish trend
//  - Price BELOW the EMA = bearish trend
//  - Fast EMA crossing above Slow EMA = "Golden Cross" (buy signal)
//  - Fast EMA crossing below Slow EMA = "Death Cross" (sell signal)
//
//  TO CHANGE: Modify the numbers after the "=" sign below.
//  Common values: 9, 21, 50, 100, 200, 300
//  Shorter period = more responsive but more noise
//  Longer period  = smoother but slower to react
//
// ██████████████████████████████████████████████████████████████████████████

// --- Set to true/false to show/hide EMAs ---
input bool   Show_EMAs        = true;      // Show EMAs on chart?

// --- CHANGE THESE NUMBERS to adjust EMA periods ---
input int    EMA_Fast_Period   = 21;       // EMA Fast Period (default: 21)
//                               ^^--- CHANGE THIS NUMBER

input int    EMA_Mid_Period    = 55;       // EMA Mid Period (default: 55)
//                               ^^--- CHANGE THIS NUMBER

input int    EMA_Slow_Period   = 200;      // EMA Slow Period (default: 200)
//                               ^^^--- CHANGE THIS NUMBER

input int    EMA_Ultra_Period  = 300;      // EMA Ultra-Slow Period (default: 300)
//                               ^^^--- CHANGE THIS NUMBER

input bool   Show_EMA_Cross    = true;     // Show Golden/Death Cross arrows?


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 2: BOLLINGER BANDS
//
//  What it does: Shows a "channel" around price based on volatility.
//  - Upper band = price is expensive (overbought zone)
//  - Lower band = price is cheap (oversold zone)
//  - Middle band = the moving average (trend center)
//  - Bands WIDEN  = high volatility (big moves happening)
//  - Bands NARROW = low volatility (breakout coming soon)
//
//  TO CHANGE:
//  - Period: how many bars for the average (default 200)
//  - StdDev: how wide the bands are (default 1.5)
//    Higher StdDev = wider bands = fewer signals
//    Lower StdDev  = tighter bands = more signals
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_BB           = true;     // Show Bollinger Bands?

input int    BB_Period          = 200;      // BB Period (default: 200)
//                                ^^^--- CHANGE THIS NUMBER

input double BB_StdDev          = 1.5;     // BB Standard Deviation (default: 1.5)
//                                ^^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 3: SUPERTREND
//
//  What it does: A trend line that flips between bullish and bearish.
//  - Green line below price = uptrend, stay long
//  - Red line above price   = downtrend, stay out
//
//  TO CHANGE:
//  - ATR Period: how many bars for volatility (default 50)
//  - Multiplier: how far the line is from price (default 3.0)
//    Higher multiplier = fewer signals, wider stops
//    Lower multiplier  = more signals, tighter stops
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_Supertrend    = true;    // Show Supertrend?

input int    ST_ATR_Period      = 50;      // Supertrend ATR Period (default: 50)
//                                ^^--- CHANGE THIS NUMBER

input double ST_Multiplier      = 3.0;    // Supertrend Multiplier (default: 3.0)
//                                ^^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 4: RSI (Relative Strength Index)
//
//  What it does: Measures overbought/oversold (0 to 100).
//  - Above 70 = overbought (price may drop)
//  - Below 30 = oversold (price may bounce)
//  - Above 50 = bullish momentum
//  - Below 50 = bearish momentum
//
//  NOTE: RSI is shown as a COMMENT on the chart (top-left text)
//  because MT4 overlay indicators can't draw sub-windows.
//  For a full RSI panel, add MT4's built-in RSI indicator separately.
//
//  TO CHANGE:
//  - Period: how many bars (default 14)
//    Shorter = more sensitive (try 7 or 9)
//    Longer  = smoother (try 21 or 24)
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_RSI           = true;    // Show RSI value?

input int    RSI_Period          = 14;     // RSI Period (default: 14)
//                                ^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 5: MACD (Moving Average Convergence Divergence)
//
//  What it does: Measures momentum by comparing two EMAs.
//  - MACD above Signal = bullish momentum
//  - MACD below Signal = bearish momentum
//  - MACD above zero   = overall bullish
//  - MACD below zero   = overall bearish
//
//  CLASSIC VALUES: 12, 26, 9
//  OUR OPTIMIZED:  48, 104, 36 (slower, fewer false signals)
//
//  TO CHANGE: Modify the numbers below.
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_MACD          = true;    // Show MACD values?

input int    MACD_Fast          = 48;      // MACD Fast EMA (default: 48, classic: 12)
//                                ^^--- CHANGE THIS NUMBER

input int    MACD_Slow          = 104;     // MACD Slow EMA (default: 104, classic: 26)
//                                ^^^--- CHANGE THIS NUMBER

input int    MACD_Signal        = 36;      // MACD Signal Line (default: 36, classic: 9)
//                                ^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 6: HEIKIN ASHI STREAK COUNTER
//
//  What it does: Counts consecutive green/red Heikin Ashi candles.
//  This is the core of our winning strategy:
//  - 12+ green HA candles = strong bullish momentum (buy signal)
//  -  6+ red HA candles   = momentum reversal (sell signal)
//
//  Shows arrows on chart when thresholds are hit.
//
//  TO CHANGE:
//  - Green threshold: how many green HA bars to trigger buy (default 12)
//  - Red threshold:   how many red HA bars to trigger sell (default 6)
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_HA            = true;    // Show Heikin Ashi signals?

input int    HA_Green_Threshold  = 12;     // HA consecutive green bars for BUY (default: 12)
//                                ^^--- CHANGE THIS NUMBER

input int    HA_Red_Threshold    = 6;      // HA consecutive red bars for SELL (default: 6)
//                                ^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 7: ATR (Average True Range)
//
//  What it does: Measures volatility (how much price moves per bar).
//  - High ATR = volatile, use wider stops
//  - Low ATR  = quiet, use tighter stops
//  - NOT a direction indicator, just measures movement size
//
//  TO CHANGE:
//  - Period: how many bars (default 14)
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_ATR           = true;    // Show ATR value?

input int    ATR_Period          = 14;     // ATR Period (default: 14)
//                                ^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 8: DONCHIAN CHANNEL
//
//  What it does: Shows the highest high / lowest low over N bars.
//  - Price above upper channel = breakout (buy signal)
//  - Price below lower channel = breakdown (sell signal)
//  - Used by the famous "Turtle Traders"
//
//  TO CHANGE:
//  - Entry Period: lookback for upper channel (default 168 = 7 days on 1H)
//  - Exit Period:  lookback for lower channel (default 72 = 3 days on 1H)
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_Donchian      = false;   // Show Donchian Channel?

input int    Donchian_Entry     = 168;     // Donchian upper channel period (default: 168)
//                                ^^^--- CHANGE THIS NUMBER

input int    Donchian_Exit      = 72;      // Donchian lower channel period (default: 72)
//                                ^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 9: ICHIMOKU CLOUD
//
//  What it does: Complete Japanese trend system.
//  - Price ABOVE cloud = bullish
//  - Price BELOW cloud = bearish
//  - Conversion above Base = short-term bullish
//
//  TO CHANGE:
//  - Tenkan: short-term (default 9)
//  - Kijun:  medium-term (default 26)
//  - Senkou B: long-term (default 52)
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_Ichimoku      = false;   // Show Ichimoku Cloud?

input int    Ichi_Tenkan        = 9;       // Tenkan (Conversion) Period (default: 9)
//                                ^--- CHANGE THIS NUMBER

input int    Ichi_Kijun         = 26;      // Kijun (Base) Period (default: 26)
//                                ^^--- CHANGE THIS NUMBER

input int    Ichi_SenkouB       = 52;      // Senkou Span B Period (default: 52)
//                                ^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 10: KELTNER CHANNEL
//
//  What it does: Like Bollinger Bands but uses ATR for width.
//  - More stable in trending markets than Bollinger
//  - Breakout above upper = strong momentum
//
//  TO CHANGE:
//  - EMA Period: center line (default 200)
//  - ATR Period: volatility (default 168)
//  - Multiplier: channel width (default 2.0)
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_Keltner       = false;   // Show Keltner Channel?

input int    Keltner_EMA_Period  = 200;    // Keltner EMA Period (default: 200)
//                                ^^^--- CHANGE THIS NUMBER

input int    Keltner_ATR_Period  = 168;    // Keltner ATR Period (default: 168)
//                                ^^^--- CHANGE THIS NUMBER

input double Keltner_Multiplier  = 2.0;   // Keltner Multiplier (default: 2.0)
//                                ^^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 11: PIVOT SUPPORT / RESISTANCE
//
//  What it does: Detects swing highs (resistance) and lows (support).
//
//  TO CHANGE:
//  - Lookback: bars left/right to confirm pivot (default 20)
//    Higher = fewer, more significant levels
//    Lower  = more levels
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_Pivots        = true;    // Show Support/Resistance?

input int    Pivot_Lookback      = 20;     // Pivot lookback bars each side (default: 20)
//                                ^^--- CHANGE THIS NUMBER


// ██████████████████████████████████████████████████████████████████████████
//
//  SECTION 12: DISPLAY OPTIONS
//
// ██████████████████████████████████████████████████████████████████████████

input bool   Show_Dashboard     = true;    // Show text dashboard on chart?
input int    Dashboard_Corner   = 0;       // Dashboard corner (0=top-left, 1=top-right, 2=bottom-left, 3=bottom-right)


// ==========================================================================
// INDICATOR BUFFERS (the lines drawn on chart)
// You should NOT need to change anything below here unless you are
// adding new indicators or modifying the drawing logic.
// ==========================================================================

double BufEmaFast[];
double BufEmaMid[];
double BufEmaSlow[];
double BufEmaUltra[];
double BufBBUpper[];
double BufBBMiddle[];
double BufBBLower[];
double BufSupertrend[];


//+------------------------------------------------------------------+
//| Custom indicator initialization function                          |
//| This runs ONCE when you add the indicator to the chart.           |
//+------------------------------------------------------------------+
int OnInit()
  {
   // --- Set up the 8 indicator buffers ---
   SetIndexBuffer(0, BufEmaFast);
   SetIndexBuffer(1, BufEmaMid);
   SetIndexBuffer(2, BufEmaSlow);
   SetIndexBuffer(3, BufEmaUltra);
   SetIndexBuffer(4, BufBBUpper);
   SetIndexBuffer(5, BufBBMiddle);
   SetIndexBuffer(6, BufBBLower);
   SetIndexBuffer(7, BufSupertrend);

   // --- Labels that appear in the Data Window ---
   SetIndexLabel(0, "EMA Fast ("  + IntegerToString(EMA_Fast_Period) + ")");
   SetIndexLabel(1, "EMA Mid ("   + IntegerToString(EMA_Mid_Period)  + ")");
   SetIndexLabel(2, "EMA Slow ("  + IntegerToString(EMA_Slow_Period) + ")");
   SetIndexLabel(3, "EMA Ultra (" + IntegerToString(EMA_Ultra_Period)+ ")");
   SetIndexLabel(4, "BB Upper");
   SetIndexLabel(5, "BB Middle");
   SetIndexLabel(6, "BB Lower");
   SetIndexLabel(7, "Supertrend");

   // --- Hide lines for disabled indicators ---
   if(!Show_EMAs)
     {
      SetIndexStyle(0, DRAW_NONE);
      SetIndexStyle(1, DRAW_NONE);
      SetIndexStyle(2, DRAW_NONE);
      SetIndexStyle(3, DRAW_NONE);
     }
   if(!Show_BB)
     {
      SetIndexStyle(4, DRAW_NONE);
      SetIndexStyle(5, DRAW_NONE);
      SetIndexStyle(6, DRAW_NONE);
     }
   if(!Show_Supertrend)
     {
      SetIndexStyle(7, DRAW_NONE);
     }

   return(INIT_SUCCEEDED);
  }


//+------------------------------------------------------------------+
//| Custom indicator deinitialization — cleanup when removed          |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   // Remove all objects this indicator created
   ObjectsDeleteAll(0, "TK_");
   Comment("");
  }


//+------------------------------------------------------------------+
//| Helper: Calculate EMA value at bar index                          |
//| (MT4 has iMA built-in, but this shows how it works)               |
//+------------------------------------------------------------------+
double GetEMA(int period, int shift)
  {
   return(iMA(NULL, 0, period, 0, MODE_EMA, PRICE_CLOSE, shift));
  }


//+------------------------------------------------------------------+
//| Helper: Calculate ATR at bar index                                |
//+------------------------------------------------------------------+
double GetATR(int period, int shift)
  {
   return(iATR(NULL, 0, period, shift));
  }


//+------------------------------------------------------------------+
//| Helper: Calculate RSI at bar index                                |
//+------------------------------------------------------------------+
double GetRSI(int period, int shift)
  {
   return(iRSI(NULL, 0, period, PRICE_CLOSE, shift));
  }


//+------------------------------------------------------------------+
//| Helper: Highest high over N bars starting from shift              |
//+------------------------------------------------------------------+
double HighestHigh(int period, int shift)
  {
   double hh = High[shift];
   for(int i = shift; i < shift + period && i < Bars; i++)
      if(High[i] > hh) hh = High[i];
   return(hh);
  }


//+------------------------------------------------------------------+
//| Helper: Lowest low over N bars starting from shift                |
//+------------------------------------------------------------------+
double LowestLow(int period, int shift)
  {
   double ll = Low[shift];
   for(int i = shift; i < shift + period && i < Bars; i++)
      if(Low[i] < ll) ll = Low[i];
   return(ll);
  }


//+------------------------------------------------------------------+
//| Helper: Draw an arrow object on the chart                         |
//+------------------------------------------------------------------+
void DrawArrow(string name, datetime time, double price, int code, color clr)
  {
   if(ObjectFind(name) >= 0) ObjectDelete(name);
   ObjectCreate(name, OBJ_ARROW, 0, time, price);
   ObjectSetInteger(0, name, OBJPROP_ARROWCODE, code);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, 2);
  }


//+------------------------------------------------------------------+
//| Helper: Draw a horizontal line for support/resistance             |
//+------------------------------------------------------------------+
void DrawHLine(string name, double price, color clr, int style)
  {
   if(ObjectFind(name) >= 0) ObjectDelete(name);
   ObjectCreate(name, OBJ_HLINE, 0, 0, price);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_STYLE, style);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, 1);
  }


//+------------------------------------------------------------------+
//| Helper: Draw a trend line for channels                            |
//+------------------------------------------------------------------+
void DrawTrendLine(string name, datetime t1, double p1, datetime t2, double p2, color clr, int width, int style)
  {
   if(ObjectFind(name) >= 0) ObjectDelete(name);
   ObjectCreate(name, OBJ_TREND, 0, t1, p1, t2, p2);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, width);
   ObjectSetInteger(0, name, OBJPROP_STYLE, style);
   ObjectSetInteger(0, name, OBJPROP_RAY, false);
  }


//+------------------------------------------------------------------+
//| Main calculation function — runs on every new bar/tick            |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
  {
   // How many bars to calculate (only new bars for speed)
   int limit = rates_total - prev_calculated;
   if(prev_calculated == 0) limit = rates_total - 1;
   if(limit < 0) limit = 0;

   // ==================================================================
   // CALCULATE INDICATOR BUFFERS FOR EACH BAR
   // ==================================================================

   for(int i = limit; i >= 0; i--)
     {
      // ---------------------------------------------------------------
      // SECTION 1: EMAs
      // ---------------------------------------------------------------
      if(Show_EMAs)
        {
         BufEmaFast[i]  = GetEMA(EMA_Fast_Period, i);
         BufEmaMid[i]   = GetEMA(EMA_Mid_Period, i);
         BufEmaSlow[i]  = GetEMA(EMA_Slow_Period, i);
         BufEmaUltra[i] = GetEMA(EMA_Ultra_Period, i);
        }
      else
        {
         BufEmaFast[i]  = EMPTY_VALUE;
         BufEmaMid[i]   = EMPTY_VALUE;
         BufEmaSlow[i]  = EMPTY_VALUE;
         BufEmaUltra[i] = EMPTY_VALUE;
        }

      // ---------------------------------------------------------------
      // SECTION 2: BOLLINGER BANDS
      // ---------------------------------------------------------------
      if(Show_BB)
        {
         // MT4 built-in Bollinger Bands
         BufBBUpper[i]  = iBands(NULL, 0, BB_Period, BB_StdDev, 0, PRICE_CLOSE, MODE_UPPER, i);
         BufBBMiddle[i] = iBands(NULL, 0, BB_Period, BB_StdDev, 0, PRICE_CLOSE, MODE_MAIN, i);
         BufBBLower[i]  = iBands(NULL, 0, BB_Period, BB_StdDev, 0, PRICE_CLOSE, MODE_LOWER, i);
        }
      else
        {
         BufBBUpper[i]  = EMPTY_VALUE;
         BufBBMiddle[i] = EMPTY_VALUE;
         BufBBLower[i]  = EMPTY_VALUE;
        }

      // ---------------------------------------------------------------
      // SECTION 3: SUPERTREND
      // Calculated manually: ATR-based bands that flip direction
      // ---------------------------------------------------------------
      if(Show_Supertrend)
        {
         BufSupertrend[i] = CalcSupertrend(i);
        }
      else
        {
         BufSupertrend[i] = EMPTY_VALUE;
        }
     }

   // ==================================================================
   // DRAW ADDITIONAL OBJECTS (arrows, channels, dashboard)
   // These only need to run on the latest bars, not the full history
   // ==================================================================

   // ---------------------------------------------------------------
   // EMA CROSS ARROWS
   // ---------------------------------------------------------------
   if(Show_EMAs && Show_EMA_Cross)
     {
      for(int i = MathMin(limit, 100); i >= 1; i--)
        {
         double fastNow  = BufEmaFast[i];
         double fastPrev = BufEmaFast[i+1];
         double slowNow  = BufEmaSlow[i];
         double slowPrev = BufEmaSlow[i+1];

         // Golden Cross: fast crosses above slow
         if(fastPrev <= slowPrev && fastNow > slowNow)
            DrawArrow("TK_GC_" + IntegerToString(i), Time[i], Low[i] - GetATR(14, i) * 0.5, 233, clrDodgerBlue);

         // Death Cross: fast crosses below slow
         if(fastPrev >= slowPrev && fastNow < slowNow)
            DrawArrow("TK_DC_" + IntegerToString(i), Time[i], High[i] + GetATR(14, i) * 0.5, 234, clrDeepPink);
        }
     }

   // ---------------------------------------------------------------
   // HEIKIN ASHI STREAK ARROWS
   // ---------------------------------------------------------------
   if(Show_HA)
     {
      for(int i = MathMin(limit, 200); i >= 1; i--)
        {
         int greenStreak = 0;
         int redStreak   = 0;
         CalcHAStreak(i, greenStreak, redStreak);

         int prevGreen = 0;
         int prevRed   = 0;
         CalcHAStreak(i+1, prevGreen, prevRed);

         // Entry arrow: first bar where green streak hits threshold
         if(greenStreak >= HA_Green_Threshold && prevGreen < HA_Green_Threshold)
            DrawArrow("TK_HA_BUY_" + IntegerToString(i), Time[i], Low[i] - GetATR(14, i) * 0.8, 241, clrLime);

         // Exit arrow: first bar where red streak hits threshold
         if(redStreak >= HA_Red_Threshold && prevRed < HA_Red_Threshold)
            DrawArrow("TK_HA_SELL_" + IntegerToString(i), Time[i], High[i] + GetATR(14, i) * 0.8, 242, clrRed);
        }
     }

   // ---------------------------------------------------------------
   // DONCHIAN CHANNEL (drawn as trend lines)
   // ---------------------------------------------------------------
   if(Show_Donchian && rates_total > Donchian_Entry + 1)
     {
      int barsToShow = MathMin(limit + 1, 300);
      for(int i = barsToShow; i >= 1; i--)
        {
         double dUpper = HighestHigh(Donchian_Entry, i);
         double dLower = LowestLow(Donchian_Exit, i);
         if(i < barsToShow)
           {
            double prevUpper = HighestHigh(Donchian_Entry, i+1);
            double prevLower = LowestLow(Donchian_Exit, i+1);
            DrawTrendLine("TK_DON_U_" + IntegerToString(i), Time[i+1], prevUpper, Time[i], dUpper, clrForestGreen, 1, STYLE_SOLID);
            DrawTrendLine("TK_DON_L_" + IntegerToString(i), Time[i+1], prevLower, Time[i], dLower, clrForestGreen, 1, STYLE_SOLID);
           }
        }
     }

   // ---------------------------------------------------------------
   // ICHIMOKU CLOUD (drawn as objects)
   // ---------------------------------------------------------------
   if(Show_Ichimoku)
     {
      int barsToShow = MathMin(limit + 1, 300);
      for(int i = barsToShow; i >= 1; i--)
        {
         double tenkanVal  = (HighestHigh(Ichi_Tenkan, i) + LowestLow(Ichi_Tenkan, i)) / 2.0;
         double kijunVal   = (HighestHigh(Ichi_Kijun, i) + LowestLow(Ichi_Kijun, i)) / 2.0;
         double senkouAVal = (tenkanVal + kijunVal) / 2.0;
         double senkouBVal = (HighestHigh(Ichi_SenkouB, i) + LowestLow(Ichi_SenkouB, i)) / 2.0;

         // Draw Tenkan and Kijun as trend segments
         if(i < barsToShow)
           {
            double prevTenkan = (HighestHigh(Ichi_Tenkan, i+1) + LowestLow(Ichi_Tenkan, i+1)) / 2.0;
            double prevKijun  = (HighestHigh(Ichi_Kijun, i+1) + LowestLow(Ichi_Kijun, i+1)) / 2.0;
            DrawTrendLine("TK_ICH_T_" + IntegerToString(i), Time[i+1], prevTenkan, Time[i], tenkanVal, clrDodgerBlue, 1, STYLE_SOLID);
            DrawTrendLine("TK_ICH_K_" + IntegerToString(i), Time[i+1], prevKijun, Time[i], kijunVal, clrOrangeRed, 1, STYLE_SOLID);
           }
        }
     }

   // ---------------------------------------------------------------
   // KELTNER CHANNEL (drawn as objects)
   // ---------------------------------------------------------------
   if(Show_Keltner)
     {
      int barsToShow = MathMin(limit + 1, 300);
      for(int i = barsToShow; i >= 1; i--)
        {
         double kMid   = GetEMA(Keltner_EMA_Period, i);
         double kAtr   = GetATR(Keltner_ATR_Period, i);
         double kUpper = kMid + Keltner_Multiplier * kAtr;
         double kLower = kMid - Keltner_Multiplier * kAtr;

         if(i < barsToShow)
           {
            double prevMid   = GetEMA(Keltner_EMA_Period, i+1);
            double prevAtr   = GetATR(Keltner_ATR_Period, i+1);
            double prevUpper = prevMid + Keltner_Multiplier * prevAtr;
            double prevLower = prevMid - Keltner_Multiplier * prevAtr;
            DrawTrendLine("TK_KLT_U_" + IntegerToString(i), Time[i+1], prevUpper, Time[i], kUpper, clrDarkOrange, 1, STYLE_SOLID);
            DrawTrendLine("TK_KLT_L_" + IntegerToString(i), Time[i+1], prevLower, Time[i], kLower, clrDarkOrange, 1, STYLE_SOLID);
           }
        }
     }

   // ---------------------------------------------------------------
   // PIVOT SUPPORT / RESISTANCE
   // ---------------------------------------------------------------
   if(Show_Pivots)
     {
      int lb = Pivot_Lookback;
      for(int i = lb + 1; i < MathMin(rates_total - lb, lb + 200); i++)
        {
         // Check if bar i is a swing high: highest of lb bars on each side
         bool isSwingHigh = true;
         bool isSwingLow  = true;
         for(int j = 1; j <= lb; j++)
           {
            if(High[i] <= High[i-j] || High[i] <= High[i+j]) isSwingHigh = false;
            if(Low[i]  >= Low[i-j]  || Low[i]  >= Low[i+j])  isSwingLow  = false;
           }
         if(isSwingHigh)
            DrawArrow("TK_PIV_H_" + IntegerToString(i), Time[i], High[i] + GetATR(14, i) * 0.3, 251, clrRed);
         if(isSwingLow)
            DrawArrow("TK_PIV_L_" + IntegerToString(i), Time[i], Low[i] - GetATR(14, i) * 0.3, 251, clrLime);
        }
     }

   // ---------------------------------------------------------------
   // DASHBOARD: Text display of all indicator values
   // ---------------------------------------------------------------
   if(Show_Dashboard)
     {
      string dash = "";
      dash += "═══ BTC TRADING TOOLKIT ═══\n";

      // RSI
      if(Show_RSI)
        {
         double rsi = GetRSI(RSI_Period, 0);
         string rsiStatus = "NEUTRAL";
         if(rsi > 70) rsiStatus = "OVERBOUGHT";
         if(rsi < 30) rsiStatus = "OVERSOLD";
         dash += "RSI(" + IntegerToString(RSI_Period) + "): " + DoubleToString(rsi, 1) + " [" + rsiStatus + "]\n";
        }

      // MACD
      if(Show_MACD)
        {
         double macdMain = iMACD(NULL, 0, MACD_Fast, MACD_Slow, MACD_Signal, PRICE_CLOSE, MODE_MAIN, 0);
         double macdSig  = iMACD(NULL, 0, MACD_Fast, MACD_Slow, MACD_Signal, PRICE_CLOSE, MODE_SIGNAL, 0);
         string macdStatus = macdMain > 0 ? "BULLISH" : "BEARISH";
         dash += "MACD: " + DoubleToString(macdMain, 1) + " Sig: " + DoubleToString(macdSig, 1) + " [" + macdStatus + "]\n";
        }

      // ATR
      if(Show_ATR)
        {
         double atr = GetATR(ATR_Period, 0);
         dash += "ATR(" + IntegerToString(ATR_Period) + "): " + DoubleToString(atr, (int)MarketInfo(Symbol(), MODE_DIGITS)) + "\n";
        }

      // Supertrend
      if(Show_Supertrend)
        {
         string stStatus = BufSupertrend[0] < Close[0] ? "BULLISH" : "BEARISH";
         dash += "Supertrend: " + DoubleToString(BufSupertrend[0], (int)MarketInfo(Symbol(), MODE_DIGITS)) + " [" + stStatus + "]\n";
        }

      // EMA Trend
      if(Show_EMAs)
        {
         string emaTrend = BufEmaFast[0] > BufEmaSlow[0] ? "BULLISH" : "BEARISH";
         dash += "EMA Trend: " + emaTrend + " (Fast " + IntegerToString(EMA_Fast_Period) + " vs Slow " + IntegerToString(EMA_Slow_Period) + ")\n";
        }

      // Heikin Ashi Streak
      if(Show_HA)
        {
         int gStreak = 0, rStreak = 0;
         CalcHAStreak(0, gStreak, rStreak);
         dash += "HA Green Streak: " + IntegerToString(gStreak) + " (entry at " + IntegerToString(HA_Green_Threshold) + ")\n";
         dash += "HA Red Streak: " + IntegerToString(rStreak) + " (exit at " + IntegerToString(HA_Red_Threshold) + ")\n";
        }

      // BB Position
      if(Show_BB)
        {
         string bbPos = "INSIDE BANDS";
         if(Close[0] > BufBBUpper[0]) bbPos = "ABOVE UPPER";
         if(Close[0] < BufBBLower[0]) bbPos = "BELOW LOWER";
         dash += "BB Position: " + bbPos + "\n";
        }

      Comment(dash);
     }

   return(rates_total);
  }


//+------------------------------------------------------------------+
//| Calculate Supertrend value for a given bar                        |
//|                                                                    |
//| Supertrend logic:                                                  |
//| - Compute upper/lower bands from ATR                               |
//| - Track direction: if price closes above upper band → bullish      |
//|                    if price closes below lower band → bearish      |
//| - In bullish mode, return the lower band (support line)            |
//| - In bearish mode, return the upper band (resistance line)         |
//+------------------------------------------------------------------+

// We need persistent state for Supertrend, so we use static arrays
double g_stUpper[];
double g_stLower[];
int    g_stDir[];
bool   g_stInitialized = false;

double CalcSupertrend(int shift)
  {
   // Initialize arrays on first call
   if(!g_stInitialized || ArraySize(g_stDir) != Bars)
     {
      ArrayResize(g_stUpper, Bars);
      ArrayResize(g_stLower, Bars);
      ArrayResize(g_stDir, Bars);
      ArrayInitialize(g_stUpper, 0);
      ArrayInitialize(g_stLower, 0);
      ArrayInitialize(g_stDir, 1);
      g_stInitialized = true;

      // Calculate from oldest to newest (Bars-1 down to 0)
      for(int i = Bars - 2; i >= 0; i--)
        {
         double atrVal = GetATR(ST_ATR_Period, i);
         double hl2    = (High[i] + Low[i]) / 2.0;
         double up     = hl2 + ST_Multiplier * atrVal;
         double dn     = hl2 - ST_Multiplier * atrVal;

         // Tighten bands
         if(dn > g_stLower[i+1] || Close[i+1] < g_stLower[i+1])
            g_stLower[i] = dn;
         else
            g_stLower[i] = g_stLower[i+1];

         if(up < g_stUpper[i+1] || Close[i+1] > g_stUpper[i+1])
            g_stUpper[i] = up;
         else
            g_stUpper[i] = g_stUpper[i+1];

         // Determine direction
         if(g_stDir[i+1] == 1) // was bullish
           {
            if(Close[i] < g_stLower[i])
               g_stDir[i] = -1;
            else
               g_stDir[i] = 1;
           }
         else // was bearish
           {
            if(Close[i] > g_stUpper[i])
               g_stDir[i] = 1;
            else
               g_stDir[i] = -1;
           }
        }
     }

   if(shift < 0 || shift >= Bars) return(EMPTY_VALUE);

   // Return the appropriate band based on direction
   // Bullish = show lower band (support), Bearish = show upper band (resistance)
   if(g_stDir[shift] == 1)
     {
      // Set color to green for bullish
      SetIndexStyle(7, DRAW_LINE, STYLE_SOLID, 2, clrLime);
      return(g_stLower[shift]);
     }
   else
     {
      // Set color to red for bearish
      SetIndexStyle(7, DRAW_LINE, STYLE_SOLID, 2, clrRed);
      return(g_stUpper[shift]);
     }
  }


//+------------------------------------------------------------------+
//| Calculate Heikin Ashi consecutive green/red streak at bar shift    |
//|                                                                    |
//| Heikin Ashi formulas:                                              |
//|   HA_Close = (Open + High + Low + Close) / 4                       |
//|   HA_Open  = (prev_HA_Open + prev_HA_Close) / 2                   |
//|   Green = HA_Close > HA_Open                                       |
//|   Red   = HA_Close <= HA_Open                                      |
//|                                                                    |
//| We count backwards from 'shift' until the color changes.           |
//+------------------------------------------------------------------+
void CalcHAStreak(int shift, int &greenStreak, int &redStreak)
  {
   greenStreak = 0;
   redStreak   = 0;

   // We need to compute HA from a far-enough starting point
   // Start from at least 500 bars back (or as far as we can)
   int startBar = MathMin(Bars - 2, shift + 500);

   double haOpen  = (Open[startBar] + Close[startBar]) / 2.0;
   double haClose = (Open[startBar] + High[startBar] + Low[startBar] + Close[startBar]) / 4.0;

   int consGreen = 0;
   int consRed   = 0;

   // Walk forward from startBar to shift
   for(int i = startBar - 1; i >= shift; i--)
     {
      haOpen  = (haOpen + haClose) / 2.0;
      haClose = (Open[i] + High[i] + Low[i] + Close[i]) / 4.0;

      if(haClose > haOpen)
        {
         consGreen++;
         consRed = 0;
        }
      else
        {
         consRed++;
         consGreen = 0;
        }
     }

   greenStreak = consGreen;
   redStreak   = consRed;
  }

//+------------------------------------------------------------------+
