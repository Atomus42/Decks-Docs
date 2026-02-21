//+------------------------------------------------------------------+
//|        BTC 1H Heikin Ashi Weekly Strategy (12G/6R)                |
//|        Expert Advisor for FXCM MetaTrader 4                       |
//|                                                                    |
//|  WHAT THIS DOES:                                                   |
//|  This is an AUTO-TRADING Expert Advisor (EA). It will open and     |
//|  close trades automatically based on Heikin Ashi candle streaks.   |
//|                                                                    |
//|  STRATEGY:                                                         |
//|  - BUY when 12 consecutive green Heikin Ashi candles appear        |
//|  - SELL when 6 consecutive red Heikin Ashi candles appear          |
//|  - Long only, no short selling                                     |
//|  - One trade at a time (no pyramiding)                             |
//|                                                                    |
//|  BACKTEST RESULTS (2 years, 1H BTC/USD):                           |
//|  - Return: +78.40%  |  Sharpe: 1.53  |  MaxDD: -17.78%            |
//|  - Win Rate: 53%    |  Profit Factor: 1.94                         |
//|  - Beat Buy & Hold by +47.54%                                      |
//|                                                                    |
//|  HOW TO INSTALL:                                                   |
//|  1. Open MetaTrader 4                                              |
//|  2. File -> Open Data Folder -> MQL4 -> Experts                    |
//|  3. Copy this file there                                           |
//|  4. Restart MT4 or right-click Navigator -> Refresh                |
//|  5. Drag "btc_1h_heikin_ashi_strategy" onto a BTC/USD 1H chart     |
//|  6. Make sure "AutoTrading" button is ON (green) in the toolbar    |
//|  7. In the EA popup, check "Allow live trading"                    |
//|                                                                    |
//|  HOW TO CHANGE VALUES:                                             |
//|  When you drag the EA onto the chart, click the "Inputs" tab.      |
//|  Every value below is listed there. Change any number and hit OK.  |
//|                                                                    |
//|  WARNING: This EA will place REAL trades if AutoTrading is ON.     |
//|  Test on a DEMO account first!                                     |
//|                                                                    |
//+------------------------------------------------------------------+

#property copyright "Heikin Ashi Weekly Strategy"
#property link      ""
#property version   "1.00"
#property strict


// ██████████████████████████████████████████████████████████████████████████
//
//  STRATEGY PARAMETERS — CHANGE THESE TO CUSTOMIZE
//
//  These appear in the "Inputs" tab when you attach the EA to a chart.
//  You can change them without editing the code.
//
// ██████████████████████████████████████████████████████████████████████████

// --- ENTRY RULE ---
// How many consecutive GREEN Heikin Ashi candles before we BUY.
// Default: 12 (our backtested optimal value)
// Lower = more trades, enters earlier but more false signals
// Higher = fewer trades, enters later but higher conviction
input int    Green_Entry_Threshold = 12;    // Consecutive green HA bars to BUY
//                                   ^^--- CHANGE THIS NUMBER

// --- EXIT RULE ---
// How many consecutive RED Heikin Ashi candles before we SELL.
// Default: 6 (exits faster than we enter — protects profits)
// Lower = exits faster, keeps more profit but may exit too early
// Higher = exits slower, rides trends longer but risks giving back profit
input int    Red_Exit_Threshold    = 6;     // Consecutive red HA bars to SELL
//                                   ^--- CHANGE THIS NUMBER

// --- POSITION SIZING ---
// What percentage of your account balance to risk per trade.
// Default: 99% (aggressive — matches our backtest)
// For real trading, consider 10-50% to limit risk
input double Lot_Percent           = 99.0;  // Percent of balance to use (default: 99%)
//                                   ^^^^--- CHANGE THIS NUMBER

// --- FIXED LOT SIZE ---
// If you prefer a fixed lot size instead of percentage, set this > 0
// and it will override the percentage above.
// Default: 0.0 (disabled — uses percentage instead)
// Example: set to 0.1 for 0.1 lots per trade
input double Fixed_Lots            = 0.0;   // Fixed lot size (0 = use percentage)
//                                   ^^^--- CHANGE THIS NUMBER (0 = disabled)

// --- MAGIC NUMBER ---
// A unique ID so this EA only manages its own trades.
// Change this if you run multiple EAs on the same account.
input int    Magic_Number          = 12060;  // Unique EA identifier
//                                   ^^^^^--- CHANGE if running multiple EAs

// --- SLIPPAGE ---
// Maximum allowed slippage in points when opening/closing orders.
input int    Max_Slippage          = 30;     // Max slippage in points
//                                   ^^--- CHANGE THIS NUMBER

// --- ALERTS ---
// Set to true to get popup/sound alerts on entry and exit signals.
input bool   Enable_Alerts         = true;   // Show alert popups?
input bool   Enable_Push           = false;  // Send push notifications to phone?


// ██████████████████████████████████████████████████████████████████████████
//
//  VISUAL OPTIONS — Controls what you see on the chart
//
// ██████████████████████████████████████████████████████████████████████████

// Show buy/sell arrows on the chart
input bool   Show_Arrows           = true;   // Show entry/exit arrows on chart?

// Show the on-chart dashboard with current status
input bool   Show_Dashboard        = true;   // Show info dashboard on chart?

// Dashboard corner: 0=top-left, 1=top-right, 2=bottom-left, 3=bottom-right
input int    Dashboard_Corner      = 1;      // Dashboard position (0-3)


// ██████████████████████████████████████████████████████████████████████████
//
//  INTERNAL VARIABLES — No need to change these
//
// ██████████████████████████████████████████████████████████████████████████

// Persistent Heikin Ashi state
double g_haOpen;          // Previous HA open value
double g_haClose;         // Previous HA close value
bool   g_haInitialized;   // Whether HA state has been initialized
int    g_consecGreen;     // Current consecutive green HA bar count
int    g_consecRed;       // Current consecutive red HA bar count
datetime g_lastBarTime;   // Time of last processed bar (prevents double-processing)


//+------------------------------------------------------------------+
//| Expert initialization — runs ONCE when EA is attached to chart    |
//+------------------------------------------------------------------+
int OnInit()
  {
   g_haInitialized = false;
   g_consecGreen   = 0;
   g_consecRed     = 0;
   g_lastBarTime   = 0;

   // Validate inputs
   if(Green_Entry_Threshold < 1)
     {
      Alert("Green_Entry_Threshold must be >= 1");
      return(INIT_PARAMETERS_INCORRECT);
     }
   if(Red_Exit_Threshold < 1)
     {
      Alert("Red_Exit_Threshold must be >= 1");
      return(INIT_PARAMETERS_INCORRECT);
     }

   Print("=== Heikin Ashi Weekly Strategy (12G/6R) initialized ===");
   Print("Entry: ", Green_Entry_Threshold, " green HA bars");
   Print("Exit:  ", Red_Exit_Threshold, " red HA bars");

   return(INIT_SUCCEEDED);
  }


//+------------------------------------------------------------------+
//| Expert deinitialization — cleanup when EA is removed              |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   // Remove all chart objects created by this EA
   ObjectsDeleteAll(0, "HA_");
   Comment("");
  }


//+------------------------------------------------------------------+
//| Calculate lot size based on account balance and settings          |
//|                                                                    |
//| If Fixed_Lots > 0, use that exact lot size.                        |
//| Otherwise, calculate lots as a percentage of account balance.      |
//+------------------------------------------------------------------+
double CalcLotSize()
  {
   // --- If user set a fixed lot size, use it ---
   if(Fixed_Lots > 0)
      return(NormalizeDouble(Fixed_Lots, 2));

   // --- Otherwise, calculate from percentage of balance ---
   double balance    = AccountBalance();
   double riskAmount = balance * (Lot_Percent / 100.0);

   // Get the value of 1 lot in account currency
   double tickValue = MarketInfo(Symbol(), MODE_TICKVALUE);
   double tickSize  = MarketInfo(Symbol(), MODE_TICKSIZE);
   double lotStep   = MarketInfo(Symbol(), MODE_LOTSTEP);
   double minLot    = MarketInfo(Symbol(), MODE_MINLOT);
   double maxLot    = MarketInfo(Symbol(), MODE_MAXLOT);

   // Calculate lot size
   double lots = 0;
   if(tickValue > 0 && Ask > 0)
     {
      // For crypto/forex: lots = risk / (price * contract_size) approximately
      double contractSize = MarketInfo(Symbol(), MODE_LOTSIZE);
      if(contractSize > 0)
         lots = riskAmount / (Ask * contractSize / AccountLeverage());
      else
         lots = riskAmount / Ask;
     }

   // Round to lot step
   if(lotStep > 0)
      lots = MathFloor(lots / lotStep) * lotStep;

   // Clamp to min/max
   if(lots < minLot) lots = minLot;
   if(lots > maxLot) lots = maxLot;

   return(NormalizeDouble(lots, 2));
  }


//+------------------------------------------------------------------+
//| Check if we currently have an open position from this EA          |
//+------------------------------------------------------------------+
bool HasOpenPosition()
  {
   for(int i = OrdersTotal() - 1; i >= 0; i--)
     {
      if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
        {
         // Only count orders from THIS EA on THIS symbol
         if(OrderSymbol() == Symbol() && OrderMagicNumber() == Magic_Number)
           {
            if(OrderType() == OP_BUY)
               return(true);
           }
        }
     }
   return(false);
  }


//+------------------------------------------------------------------+
//| Close all open BUY positions from this EA                         |
//+------------------------------------------------------------------+
bool CloseAllPositions()
  {
   bool allClosed = true;

   for(int i = OrdersTotal() - 1; i >= 0; i--)
     {
      if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
        {
         if(OrderSymbol() == Symbol() && OrderMagicNumber() == Magic_Number)
           {
            if(OrderType() == OP_BUY)
              {
               // Close at current Bid price
               bool closed = OrderClose(OrderTicket(), OrderLots(), Bid, Max_Slippage, clrRed);
               if(!closed)
                 {
                  Print("ERROR closing order #", OrderTicket(), ": ", GetLastError());
                  allClosed = false;
                 }
               else
                 {
                  Print("Closed BUY order #", OrderTicket(),
                        " | Profit: ", DoubleToString(OrderProfit(), 2));
                 }
              }
           }
        }
     }
   return(allClosed);
  }


//+------------------------------------------------------------------+
//| Calculate Heikin Ashi values and streak for ALL historical bars   |
//| This ensures the streak count is accurate from the start.         |
//+------------------------------------------------------------------+
void InitializeHA()
  {
   if(g_haInitialized) return;
   if(Bars < 2) return;

   // Start from the oldest bar
   int startBar = Bars - 1;

   // First HA candle
   g_haOpen  = (Open[startBar] + Close[startBar]) / 2.0;
   g_haClose = (Open[startBar] + High[startBar] + Low[startBar] + Close[startBar]) / 4.0;
   g_consecGreen = 0;
   g_consecRed   = 0;

   if(g_haClose > g_haOpen)
     { g_consecGreen = 1; g_consecRed = 0; }
   else
     { g_consecRed = 1; g_consecGreen = 0; }

   // Walk forward through all bars to build accurate streak
   for(int i = startBar - 1; i >= 1; i--)
     {
      double newHaOpen  = (g_haOpen + g_haClose) / 2.0;
      double newHaClose = (Open[i] + High[i] + Low[i] + Close[i]) / 4.0;

      if(newHaClose > newHaOpen)
        {
         g_consecGreen++;
         g_consecRed = 0;
        }
      else
        {
         g_consecRed++;
         g_consecGreen = 0;
        }

      g_haOpen  = newHaOpen;
      g_haClose = newHaClose;
     }

   g_lastBarTime   = Time[1];
   g_haInitialized = true;

   Print("HA initialized | Green streak: ", g_consecGreen,
         " | Red streak: ", g_consecRed);
  }


//+------------------------------------------------------------------+
//| Process current bar's Heikin Ashi candle                           |
//| Returns: 1 = green candle, -1 = red candle                        |
//+------------------------------------------------------------------+
int ProcessCurrentBar()
  {
   // Only process when a NEW bar has formed (bar [1] is the last closed bar)
   if(Time[1] == g_lastBarTime) return(0);
   g_lastBarTime = Time[1];

   // Calculate HA values for the just-closed bar (bar [1])
   double newHaOpen  = (g_haOpen + g_haClose) / 2.0;
   double newHaClose = (Open[1] + High[1] + Low[1] + Close[1]) / 4.0;

   int result = 0;

   if(newHaClose > newHaOpen)
     {
      // GREEN candle
      g_consecGreen++;
      g_consecRed = 0;
      result = 1;
     }
   else
     {
      // RED candle
      g_consecRed++;
      g_consecGreen = 0;
      result = -1;
     }

   // Update state for next bar
   g_haOpen  = newHaOpen;
   g_haClose = newHaClose;

   return(result);
  }


//+------------------------------------------------------------------+
//| Draw an arrow on the chart                                         |
//+------------------------------------------------------------------+
void DrawSignalArrow(string name, datetime time, double price, int code, color clr)
  {
   if(!Show_Arrows) return;
   if(ObjectFind(name) >= 0) ObjectDelete(name);
   ObjectCreate(name, OBJ_ARROW, 0, time, price);
   ObjectSetInteger(0, name, OBJPROP_ARROWCODE, code);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, 2);
  }


//+------------------------------------------------------------------+
//| Update the on-chart dashboard                                      |
//+------------------------------------------------------------------+
void UpdateDashboard()
  {
   if(!Show_Dashboard) return;

   string sep = "-----------------------------\n";
   string txt = "";

   txt += "=== HEIKIN ASHI WEEKLY (12G/6R) ===\n";
   txt += sep;

   // Current streak
   txt += "Green Streak: " + IntegerToString(g_consecGreen);
   if(g_consecGreen >= Green_Entry_Threshold)
      txt += " >>> ENTRY SIGNAL <<<";
   txt += "\n";

   txt += "Red Streak:   " + IntegerToString(g_consecRed);
   if(g_consecRed >= Red_Exit_Threshold)
      txt += " >>> EXIT SIGNAL <<<";
   txt += "\n";

   txt += sep;

   // Thresholds
   txt += "Entry at: " + IntegerToString(Green_Entry_Threshold) + " green bars\n";
   txt += "Exit at:  " + IntegerToString(Red_Exit_Threshold) + " red bars\n";
   txt += sep;

   // Position status
   if(HasOpenPosition())
     {
      txt += "Position: LONG\n";

      // Find the open order and show P&L
      for(int i = OrdersTotal() - 1; i >= 0; i--)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(OrderSymbol() == Symbol() && OrderMagicNumber() == Magic_Number && OrderType() == OP_BUY)
              {
               double pnl     = OrderProfit() + OrderSwap() + OrderCommission();
               double pnlPct  = (Bid - OrderOpenPrice()) / OrderOpenPrice() * 100.0;
               txt += "Entry Price: " + DoubleToString(OrderOpenPrice(), (int)MarketInfo(Symbol(), MODE_DIGITS)) + "\n";
               txt += "Current P&L: " + DoubleToString(pnl, 2) + " (" + DoubleToString(pnlPct, 2) + "%)\n";
               txt += "Lots: " + DoubleToString(OrderLots(), 2) + "\n";
               break;
              }
           }
        }
     }
   else
     {
      txt += "Position: FLAT (no trade open)\n";
     }

   txt += sep;
   txt += "Timeframe: " + PeriodToStr() + "\n";
   txt += "Last bar: " + TimeToString(Time[1], TIME_DATE|TIME_MINUTES) + "\n";

   Comment(txt);
  }


//+------------------------------------------------------------------+
//| Convert period to readable string                                  |
//+------------------------------------------------------------------+
string PeriodToStr()
  {
   switch(Period())
     {
      case PERIOD_M1:  return("M1");
      case PERIOD_M5:  return("M5");
      case PERIOD_M15: return("M15");
      case PERIOD_M30: return("M30");
      case PERIOD_H1:  return("H1");
      case PERIOD_H4:  return("H4");
      case PERIOD_D1:  return("D1");
      case PERIOD_W1:  return("W1");
      case PERIOD_MN1: return("MN1");
      default:         return("Period " + IntegerToString(Period()));
     }
  }


//+------------------------------------------------------------------+
//| Main tick function — runs on EVERY price tick                      |
//|                                                                    |
//| This is the heart of the EA. On every tick:                        |
//| 1. Initialize HA state if needed                                   |
//| 2. Check if a new bar has formed                                   |
//| 3. Update the HA streak counter                                    |
//| 4. Check entry/exit conditions                                     |
//| 5. Open or close trades                                            |
//| 6. Update the dashboard                                            |
//+------------------------------------------------------------------+
void OnTick()
  {
   // ------------------------------------------------------------------
   // STEP 1: Initialize Heikin Ashi state on first run
   // This walks through all historical bars to build an accurate
   // streak count from the start.
   // ------------------------------------------------------------------
   InitializeHA();

   // ------------------------------------------------------------------
   // STEP 2: Process the latest closed bar
   // We only trade on NEW bars (not every tick) to avoid noise.
   // Returns: 1 = new green bar, -1 = new red bar, 0 = same bar
   // ------------------------------------------------------------------
   int barResult = ProcessCurrentBar();

   // ------------------------------------------------------------------
   // STEP 3: If a new bar formed, check for trade signals
   // ------------------------------------------------------------------
   if(barResult != 0)
     {
      bool isInPosition = HasOpenPosition();

      // ---------------------------------------------------------------
      // ENTRY CONDITION:
      // Green streak has reached the threshold AND we're not in a trade
      // ---------------------------------------------------------------
      if(g_consecGreen >= Green_Entry_Threshold && !isInPosition)
        {
         double lots = CalcLotSize();

         // Open a BUY order
         int ticket = OrderSend(
            Symbol(),           // Current chart symbol
            OP_BUY,             // Buy order
            lots,               // Lot size
            Ask,                // Entry at Ask price
            Max_Slippage,       // Maximum slippage
            0,                  // No stop loss (managed by exit rule)
            0,                  // No take profit (managed by exit rule)
            "HA Entry " + IntegerToString(g_consecGreen) + "G",  // Comment
            Magic_Number,       // Our unique EA ID
            0,                  // No expiration
            clrLime             // Arrow color on chart
         );

         if(ticket > 0)
           {
            Print(">>> ENTRY: BUY ", DoubleToString(lots, 2), " lots at ",
                  DoubleToString(Ask, (int)MarketInfo(Symbol(), MODE_DIGITS)),
                  " | Green streak: ", g_consecGreen);

            // Draw arrow on chart
            DrawSignalArrow("HA_BUY_" + IntegerToString(Time[1]),
                           Time[1], Low[1] - iATR(NULL, 0, 14, 1) * 0.5,
                           241, clrLime);

            // Alerts
            if(Enable_Alerts)
               Alert("HA Strategy: BUY signal at ", DoubleToString(Ask, (int)MarketInfo(Symbol(), MODE_DIGITS)),
                     " | Green streak: ", g_consecGreen);
            if(Enable_Push)
               SendNotification("HA Strategy: BUY at " + DoubleToString(Ask, (int)MarketInfo(Symbol(), MODE_DIGITS)));
           }
         else
           {
            Print("ERROR opening BUY order: ", GetLastError());
           }
        }

      // ---------------------------------------------------------------
      // EXIT CONDITION:
      // Red streak has reached the threshold AND we're in a trade
      // ---------------------------------------------------------------
      if(g_consecRed >= Red_Exit_Threshold && isInPosition)
        {
         Print(">>> EXIT: Red streak ", g_consecRed, " >= ", Red_Exit_Threshold);

         // Draw arrow on chart
         DrawSignalArrow("HA_SELL_" + IntegerToString(Time[1]),
                        Time[1], High[1] + iATR(NULL, 0, 14, 1) * 0.5,
                        242, clrRed);

         // Close all our open positions
         bool closed = CloseAllPositions();

         if(closed)
           {
            if(Enable_Alerts)
               Alert("HA Strategy: EXIT signal | Red streak: ", g_consecRed);
            if(Enable_Push)
               SendNotification("HA Strategy: EXIT | Red streak: " + IntegerToString(g_consecRed));
           }
        }
     }

   // ------------------------------------------------------------------
   // STEP 4: Update the dashboard on every tick
   // ------------------------------------------------------------------
   UpdateDashboard();
  }

//+------------------------------------------------------------------+
