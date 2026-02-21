-- =============================================================================
--
--  BTC TRADING TOOLKIT — ALL MAIN INDICATORS (FXCM Trading Station)
--
--  This is an INDICATOR for FXCM Trading Station (Indicore SDK / Lua).
--  It draws all the key technical indicators on your chart so you can
--  visually analyze the market yourself.
--
--  HOW TO INSTALL:
--  ---------------
--  1. Save this file as "btc_all_indicators_toolkit.lua"
--  2. Copy it to:
--     C:\Program Files (x86)\Candleworks\FXTS2\indicators\Custom\
--     (or wherever your Trading Station indicators folder is)
--  3. Restart Trading Station
--  4. Right-click chart → "Add Indicator" → find "BTC Trading Toolkit"
--  5. A settings dialog will appear with ALL the parameters you can change
--
--  HOW TO CUSTOMIZE:
--  -----------------
--  Option A — IN THE GUI:
--     When you add the indicator, a dialog box appears with all parameters.
--     Change any value there. Click OK. Done.
--
--  Option B — IN THIS CODE:
--     Find the line that starts with:  indicator:addParam("...")
--     The number after "setDefault" is the default value.
--     Change that number to whatever you want.
--     Look for the arrows: ◄◄◄ CHANGE THIS
--
--  Each section is clearly labeled with big comment headers.
--  Scroll to the indicator you want to modify.
--
-- =============================================================================


-- =============================================================================
-- INDICATOR PROFILE (name, description, type)
-- This is required by FXCM. You can change the name if you want.
-- =============================================================================

function Init()
    indicator:name("BTC Trading Toolkit — All Indicators")
    indicator:description("All-in-one toolkit: EMA, Bollinger, Donchian, Supertrend, RSI, MACD, Heikin Ashi, ATR, Ichimoku, Keltner, Volume, Pivots")
    indicator:requiredSource(core.Bar)  -- We need OHLCV data (candles, not just close)
    indicator:type(core.Indicator)      -- This is an indicator, not a strategy


    -- =========================================================================
    --
    --  SECTION 1: EMA (Exponential Moving Averages)
    --
    --  What it does: Smooths price to show the trend direction.
    --  - Price ABOVE the EMA = bullish trend
    --  - Price BELOW the EMA = bearish trend
    --  - Fast EMA crossing above Slow EMA = "Golden Cross" (buy signal)
    --  - Fast EMA crossing below Slow EMA = "Death Cross" (sell signal)
    --
    --  TO CHANGE: Modify the number after setDefault().
    --  Common values: 9, 21, 50, 100, 200, 300
    --  Shorter period = more responsive but more noise
    --  Longer period  = smoother but slower to react
    --
    -- =========================================================================

    -- Toggle: uncheck this in the GUI to hide all EMAs
    indicator:addParam("SHOW_EMA", "Show EMAs")
    indicator.parameters:addBoolean("SHOW_EMA", "Show EMAs on chart", "", true)

    -- EMA Fast Period
    indicator:addParam("EMA_FAST", "EMA Fast Period")
    indicator.parameters:addInteger("EMA_FAST", "EMA Fast Period (default: 21)", "", 21, 1, 500)
    --                                                                           ◄◄◄ CHANGE 21

    -- EMA Mid Period
    indicator:addParam("EMA_MID", "EMA Mid Period")
    indicator.parameters:addInteger("EMA_MID", "EMA Mid Period (default: 55)", "", 55, 1, 500)
    --                                                                          ◄◄◄ CHANGE 55

    -- EMA Slow Period
    indicator:addParam("EMA_SLOW", "EMA Slow Period")
    indicator.parameters:addInteger("EMA_SLOW", "EMA Slow Period (default: 200)", "", 200, 1, 500)
    --                                                                            ◄◄◄ CHANGE 200

    -- EMA Ultra-Slow Period (our best backtest used 100/300)
    indicator:addParam("EMA_ULTRA", "EMA Ultra-Slow Period")
    indicator.parameters:addInteger("EMA_ULTRA", "EMA Ultra-Slow Period (default: 300)", "", 300, 1, 1000)
    --                                                                                   ◄◄◄ CHANGE 300

    -- Show EMA cross signals (golden cross / death cross diamonds)
    indicator:addParam("SHOW_EMA_CROSS", "Show EMA Cross Signals")
    indicator.parameters:addBoolean("SHOW_EMA_CROSS", "Show Golden/Death Cross markers", "", true)


    -- =========================================================================
    --
    --  SECTION 2: BOLLINGER BANDS
    --
    --  What it does: Shows a "channel" around price based on volatility.
    --  - Upper band = price is expensive (overbought zone)
    --  - Lower band = price is cheap (oversold zone)
    --  - Middle band = the moving average (trend center)
    --  - Bands WIDEN  = high volatility (big moves happening)
    --  - Bands NARROW = low volatility (breakout coming soon)
    --
    --  TO CHANGE:
    --  - Period: how many bars for the average (default 200, our best backtest)
    --  - StdDev: how wide the bands are (default 1.5)
    --    Higher StdDev = wider bands = fewer signals
    --    Lower StdDev  = tighter bands = more signals
    --
    -- =========================================================================

    indicator:addParam("SHOW_BB", "Show Bollinger Bands")
    indicator.parameters:addBoolean("SHOW_BB", "Show Bollinger Bands on chart", "", true)

    indicator:addParam("BB_PERIOD", "BB Period")
    indicator.parameters:addInteger("BB_PERIOD", "Bollinger Bands period (default: 200)", "", 200, 1, 500)
    --                                                                                     ◄◄◄ CHANGE 200

    indicator:addParam("BB_STDDEV", "BB Standard Deviation")
    indicator.parameters:addDouble("BB_STDDEV", "Band width multiplier (default: 1.5)", "", 1.5, 0.1, 5.0)
    --                                                                                  ◄◄◄ CHANGE 1.5


    -- =========================================================================
    --
    --  SECTION 3: DONCHIAN CHANNEL (Breakout Channel)
    --
    --  What it does: Shows the highest high and lowest low over N bars.
    --  - Price breaking ABOVE the upper channel = breakout (buy signal)
    --  - Price breaking BELOW the lower channel = breakdown (sell signal)
    --  - Used by the famous "Turtle Traders" strategy
    --
    --  TO CHANGE:
    --  - Entry Period: lookback for the upper channel (default 168 = 7 days on 1H)
    --  - Exit Period:  lookback for the lower channel (default 72 = 3 days on 1H)
    --
    -- =========================================================================

    indicator:addParam("SHOW_DONCH", "Show Donchian Channel")
    indicator.parameters:addBoolean("SHOW_DONCH", "Show Donchian Channel on chart", "", false)

    indicator:addParam("DONCH_ENTRY", "Donchian Entry Period (upper)")
    indicator.parameters:addInteger("DONCH_ENTRY", "Upper channel lookback (default: 168)", "", 168, 1, 1000)
    --                                                                                      ◄◄◄ CHANGE 168

    indicator:addParam("DONCH_EXIT", "Donchian Exit Period (lower)")
    indicator.parameters:addInteger("DONCH_EXIT", "Lower channel lookback (default: 72)", "", 72, 1, 1000)
    --                                                                                    ◄◄◄ CHANGE 72


    -- =========================================================================
    --
    --  SECTION 4: SUPERTREND
    --
    --  What it does: A trend-following indicator that flips between
    --  bullish (green line below price) and bearish (red line above price).
    --  - Green = uptrend, stay long
    --  - Red   = downtrend, stay out
    --
    --  TO CHANGE:
    --  - ATR Period: how many bars for ATR calculation (default 50)
    --  - Multiplier: how far the band sits from price (default 3.0)
    --    Higher multiplier = fewer signals, wider stops
    --    Lower multiplier  = more signals, tighter stops
    --
    -- =========================================================================

    indicator:addParam("SHOW_ST", "Show Supertrend")
    indicator.parameters:addBoolean("SHOW_ST", "Show Supertrend on chart", "", true)

    indicator:addParam("ST_ATR", "Supertrend ATR Period")
    indicator.parameters:addInteger("ST_ATR", "ATR lookback period (default: 50)", "", 50, 1, 200)
    --                                                                              ◄◄◄ CHANGE 50

    indicator:addParam("ST_MULT", "Supertrend Multiplier")
    indicator.parameters:addDouble("ST_MULT", "Band distance multiplier (default: 3.0)", "", 3.0, 0.1, 10.0)
    --                                                                                   ◄◄◄ CHANGE 3.0


    -- =========================================================================
    --
    --  SECTION 5: RSI (Relative Strength Index)
    --
    --  What it does: Measures how overbought or oversold price is (0 to 100).
    --  - Above 70 = overbought (price may drop)
    --  - Below 30 = oversold (price may bounce)
    --  - Above 50 = bullish momentum
    --  - Below 50 = bearish momentum
    --
    --  TO CHANGE:
    --  - Period: how many bars (default 14, the standard)
    --    Shorter = more sensitive (try 7 or 9)
    --    Longer  = smoother (try 21 or 24)
    --
    -- =========================================================================

    indicator:addParam("SHOW_RSI", "Show RSI")
    indicator.parameters:addBoolean("SHOW_RSI", "Show RSI line", "", true)

    indicator:addParam("RSI_PERIOD", "RSI Period")
    indicator.parameters:addInteger("RSI_PERIOD", "RSI lookback (default: 14)", "", 14, 1, 100)
    --                                                                           ◄◄◄ CHANGE 14


    -- =========================================================================
    --
    --  SECTION 6: MACD (Moving Average Convergence Divergence)
    --
    --  What it does: Measures momentum by comparing two EMAs.
    --  - MACD line above Signal line = bullish momentum
    --  - MACD line below Signal line = bearish momentum
    --  - MACD line above zero = overall bullish
    --  - MACD line below zero = overall bearish
    --
    --  TO CHANGE:
    --  CLASSIC VALUES: 12, 26, 9 (default in most charting software)
    --  OUR OPTIMIZED:  48, 104, 36 (slower, fewer false signals on BTC 1H)
    --
    -- =========================================================================

    indicator:addParam("SHOW_MACD", "Show MACD")
    indicator.parameters:addBoolean("SHOW_MACD", "Show MACD lines", "", true)

    indicator:addParam("MACD_FAST", "MACD Fast EMA")
    indicator.parameters:addInteger("MACD_FAST", "Fast EMA period (default: 48, classic: 12)", "", 48, 1, 200)
    --                                                                                         ◄◄◄ CHANGE 48

    indicator:addParam("MACD_SLOW", "MACD Slow EMA")
    indicator.parameters:addInteger("MACD_SLOW", "Slow EMA period (default: 104, classic: 26)", "", 104, 1, 500)
    --                                                                                          ◄◄◄ CHANGE 104

    indicator:addParam("MACD_SIGNAL", "MACD Signal Line")
    indicator.parameters:addInteger("MACD_SIGNAL", "Signal smoothing (default: 36, classic: 9)", "", 36, 1, 100)
    --                                                                                           ◄◄◄ CHANGE 36


    -- =========================================================================
    --
    --  SECTION 7: HEIKIN ASHI CANDLE STREAK COUNTER
    --
    --  What it does: Counts consecutive green/red Heikin Ashi candles.
    --  This is the core of our winning strategy:
    --  - 12+ green HA candles in a row = strong bullish momentum (entry signal)
    --  -  6+ red HA candles in a row   = momentum reversal (exit signal)
    --
    --  TO CHANGE:
    --  - Green threshold: how many green bars to trigger entry (default 12)
    --  - Red threshold:   how many red bars to trigger exit (default 6)
    --
    -- =========================================================================

    indicator:addParam("SHOW_HA", "Show Heikin Ashi Signals")
    indicator.parameters:addBoolean("SHOW_HA", "Show HA streak signals on chart", "", true)

    indicator:addParam("HA_GREEN", "HA Green Bars for Entry")
    indicator.parameters:addInteger("HA_GREEN", "Consecutive green HA bars to enter (default: 12)", "", 12, 1, 50)
    --                                                                                               ◄◄◄ CHANGE 12

    indicator:addParam("HA_RED", "HA Red Bars for Exit")
    indicator.parameters:addInteger("HA_RED", "Consecutive red HA bars to exit (default: 6)", "", 6, 1, 50)
    --                                                                                        ◄◄◄ CHANGE 6


    -- =========================================================================
    --
    --  SECTION 8: ATR (Average True Range)
    --
    --  What it does: Measures volatility — how much price moves per bar.
    --  - High ATR = volatile, big candles, need wider stops
    --  - Low ATR  = quiet, small candles, tighter stops OK
    --  - NOT a direction indicator — just tells you HOW MUCH price moves
    --
    --  TO CHANGE:
    --  - Period: how many bars (default 14)
    --
    -- =========================================================================

    indicator:addParam("SHOW_ATR", "Show ATR")
    indicator.parameters:addBoolean("SHOW_ATR", "Show ATR line", "", true)

    indicator:addParam("ATR_PERIOD", "ATR Period")
    indicator.parameters:addInteger("ATR_PERIOD", "ATR lookback (default: 14)", "", 14, 1, 200)
    --                                                                           ◄◄◄ CHANGE 14


    -- =========================================================================
    --
    --  SECTION 9: ICHIMOKU CLOUD
    --
    --  What it does: A complete trend system from Japan.
    --  - Conversion line (Tenkan): short-term trend (like a fast MA)
    --  - Base line (Kijun):        medium-term trend (like a slow MA)
    --  - Cloud (Kumo):             support/resistance zone
    --    - Price ABOVE cloud = bullish
    --    - Price BELOW cloud = bearish
    --    - Price INSIDE cloud = no clear trend
    --
    --  TO CHANGE:
    --  - Tenkan period:  short-term lookback (default 9)
    --  - Kijun period:   medium-term lookback (default 26)
    --  - Senkou B period: long-term lookback (default 52)
    --
    -- =========================================================================

    indicator:addParam("SHOW_ICHI", "Show Ichimoku Cloud")
    indicator.parameters:addBoolean("SHOW_ICHI", "Show Ichimoku on chart", "", false)

    indicator:addParam("ICHI_TENKAN", "Tenkan (Conversion) Period")
    indicator.parameters:addInteger("ICHI_TENKAN", "Short-term lookback (default: 9)", "", 9, 1, 100)
    --                                                                                  ◄◄◄ CHANGE 9

    indicator:addParam("ICHI_KIJUN", "Kijun (Base) Period")
    indicator.parameters:addInteger("ICHI_KIJUN", "Medium-term lookback (default: 26)", "", 26, 1, 100)
    --                                                                                  ◄◄◄ CHANGE 26

    indicator:addParam("ICHI_SENKOU", "Senkou Span B Period")
    indicator.parameters:addInteger("ICHI_SENKOU", "Long-term lookback (default: 52)", "", 52, 1, 200)
    --                                                                                 ◄◄◄ CHANGE 52


    -- =========================================================================
    --
    --  SECTION 10: KELTNER CHANNEL
    --
    --  What it does: Similar to Bollinger Bands but uses ATR for width.
    --  - Upper = EMA + multiplier * ATR
    --  - Lower = EMA - multiplier * ATR
    --  - Price above upper = strong momentum breakout
    --  - More stable than Bollinger in trending markets
    --
    --  TO CHANGE:
    --  - EMA Period: center line period (default 200)
    --  - ATR Period: volatility period (default 168)
    --  - Multiplier: channel width (default 2.0)
    --
    -- =========================================================================

    indicator:addParam("SHOW_KELT", "Show Keltner Channel")
    indicator.parameters:addBoolean("SHOW_KELT", "Show Keltner Channel on chart", "", false)

    indicator:addParam("KELT_EMA", "Keltner EMA Period")
    indicator.parameters:addInteger("KELT_EMA", "Center EMA period (default: 200)", "", 200, 1, 500)
    --                                                                               ◄◄◄ CHANGE 200

    indicator:addParam("KELT_ATR", "Keltner ATR Period")
    indicator.parameters:addInteger("KELT_ATR", "Volatility period (default: 168)", "", 168, 1, 500)
    --                                                                               ◄◄◄ CHANGE 168

    indicator:addParam("KELT_MULT", "Keltner Multiplier")
    indicator.parameters:addDouble("KELT_MULT", "Channel width (default: 2.0)", "", 2.0, 0.1, 10.0)
    --                                                                           ◄◄◄ CHANGE 2.0

end


-- =============================================================================
-- GLOBAL VARIABLES
-- These store the output lines that get drawn on the chart.
-- You don't need to change anything here.
-- =============================================================================

-- Data source (the price candles)
local source
local first     -- index of the first bar we can compute from
local n         -- total number of bars

-- Output streams (the lines drawn on chart)
-- Each one is a separate line with its own color
local emaFastOut, emaMidOut, emaSlowOut, emaUltraOut
local bbUpperOut, bbMiddleOut, bbLowerOut
local donchUpperOut, donchMidOut, donchLowerOut
local supertrendOut
local rsiOut
local macdLineOut, macdSignalOut, macdHistOut
local haGreenStreakOut, haRedStreakOut
local atrOut
local ichiTenkanOut, ichiKijunOut, ichiSenkouAOut, ichiSenkouBOut
local keltUpperOut, keltMidOut, keltLowerOut

-- Parameters (loaded from the GUI settings)
local SHOW_EMA, EMA_FAST, EMA_MID, EMA_SLOW, EMA_ULTRA, SHOW_EMA_CROSS
local SHOW_BB, BB_PERIOD, BB_STDDEV
local SHOW_DONCH, DONCH_ENTRY, DONCH_EXIT
local SHOW_ST, ST_ATR, ST_MULT
local SHOW_RSI, RSI_PERIOD
local SHOW_MACD, MACD_FAST, MACD_SLOW, MACD_SIGNAL
local SHOW_HA, HA_GREEN, HA_RED
local SHOW_ATR, ATR_PERIOD
local SHOW_ICHI, ICHI_TENKAN, ICHI_KIJUN, ICHI_SENKOU
local SHOW_KELT, KELT_EMA, KELT_ATR, KELT_MULT


-- =============================================================================
-- PREPARE FUNCTION
-- Called once when the indicator is added to the chart.
-- Sets up all the output lines and loads your parameter values.
-- =============================================================================

function Prepare(onlyName)
    -- Load all parameter values from the settings dialog
    SHOW_EMA       = instance.parameters.SHOW_EMA
    EMA_FAST       = instance.parameters.EMA_FAST
    EMA_MID        = instance.parameters.EMA_MID
    EMA_SLOW       = instance.parameters.EMA_SLOW
    EMA_ULTRA      = instance.parameters.EMA_ULTRA
    SHOW_EMA_CROSS = instance.parameters.SHOW_EMA_CROSS

    SHOW_BB        = instance.parameters.SHOW_BB
    BB_PERIOD      = instance.parameters.BB_PERIOD
    BB_STDDEV      = instance.parameters.BB_STDDEV

    SHOW_DONCH     = instance.parameters.SHOW_DONCH
    DONCH_ENTRY    = instance.parameters.DONCH_ENTRY
    DONCH_EXIT     = instance.parameters.DONCH_EXIT

    SHOW_ST        = instance.parameters.SHOW_ST
    ST_ATR         = instance.parameters.ST_ATR
    ST_MULT        = instance.parameters.ST_MULT

    SHOW_RSI       = instance.parameters.SHOW_RSI
    RSI_PERIOD     = instance.parameters.RSI_PERIOD

    SHOW_MACD      = instance.parameters.SHOW_MACD
    MACD_FAST      = instance.parameters.MACD_FAST
    MACD_SLOW      = instance.parameters.MACD_SLOW
    MACD_SIGNAL    = instance.parameters.MACD_SIGNAL

    SHOW_HA        = instance.parameters.SHOW_HA
    HA_GREEN       = instance.parameters.HA_GREEN
    HA_RED         = instance.parameters.HA_RED

    SHOW_ATR       = instance.parameters.SHOW_ATR
    ATR_PERIOD     = instance.parameters.ATR_PERIOD

    SHOW_ICHI      = instance.parameters.SHOW_ICHI
    ICHI_TENKAN    = instance.parameters.ICHI_TENKAN
    ICHI_KIJUN     = instance.parameters.ICHI_KIJUN
    ICHI_SENKOU    = instance.parameters.ICHI_SENKOU

    SHOW_KELT      = instance.parameters.SHOW_KELT
    KELT_EMA       = instance.parameters.KELT_EMA
    KELT_ATR       = instance.parameters.KELT_ATR
    KELT_MULT      = instance.parameters.KELT_MULT

    -- Build the indicator name shown on chart
    local name = profile:id() .. "(" .. instance.bid:instrument() .. ")"
    instance:name(name)
    if onlyName then return end

    -- Get the data source
    source = instance.source
    first  = source:first()
    n      = source:size() - 1

    -- =====================================================================
    -- CREATE OUTPUT LINES
    -- Each addStream creates a line on the chart.
    -- The color is: core.rgb(Red, Green, Blue)  where each is 0-255.
    -- =====================================================================

    -- EMA lines
    emaFastOut  = instance:addStream("EMA_FAST",  core.Line, name .. ".EMA_FAST",  "EMA Fast",       core.rgb(0, 188, 212), first)   -- cyan
    emaMidOut   = instance:addStream("EMA_MID",   core.Line, name .. ".EMA_MID",   "EMA Mid",        core.rgb(255, 152, 0), first)   -- orange
    emaSlowOut  = instance:addStream("EMA_SLOW",  core.Line, name .. ".EMA_SLOW",  "EMA Slow",       core.rgb(233, 30, 99), first)   -- pink
    emaSlowOut:setWidth(2)
    emaUltraOut = instance:addStream("EMA_ULTRA", core.Line, name .. ".EMA_ULTRA", "EMA Ultra-Slow", core.rgb(156, 39, 176), first)  -- purple
    emaUltraOut:setWidth(2)

    -- Bollinger Bands
    bbUpperOut  = instance:addStream("BB_UPPER",  core.Line, name .. ".BB_UPPER",  "BB Upper",  core.rgb(33, 150, 243), first)  -- blue
    bbMiddleOut = instance:addStream("BB_MID",    core.Line, name .. ".BB_MID",    "BB Middle", core.rgb(33, 150, 243), first)
    bbLowerOut  = instance:addStream("BB_LOWER",  core.Line, name .. ".BB_LOWER",  "BB Lower",  core.rgb(33, 150, 243), first)

    -- Donchian Channel
    donchUpperOut = instance:addStream("DONCH_UP",  core.Line, name .. ".DONCH_UP",  "Donchian Upper", core.rgb(76, 175, 80), first)  -- green
    donchMidOut   = instance:addStream("DONCH_MID", core.Line, name .. ".DONCH_MID", "Donchian Mid",   core.rgb(76, 175, 80), first)
    donchLowerOut = instance:addStream("DONCH_LO",  core.Line, name .. ".DONCH_LO",  "Donchian Lower", core.rgb(76, 175, 80), first)

    -- Supertrend
    supertrendOut = instance:addStream("ST", core.Line, name .. ".ST", "Supertrend", core.rgb(38, 166, 154), first)  -- teal
    supertrendOut:setWidth(2)

    -- RSI (separate pane)
    rsiOut = instance:addStream("RSI", core.Line, name .. ".RSI", "RSI", core.rgb(255, 152, 0), first)  -- orange

    -- MACD (separate pane)
    macdLineOut   = instance:addStream("MACD",     core.Line, name .. ".MACD",     "MACD Line",   core.rgb(33, 150, 243), first)   -- blue
    macdSignalOut = instance:addStream("MACD_SIG", core.Line, name .. ".MACD_SIG", "MACD Signal", core.rgb(255, 152, 0), first)    -- orange
    macdHistOut   = instance:addStream("MACD_HST", core.Bar,  name .. ".MACD_HST", "MACD Hist",   core.rgb(156, 39, 176), first)   -- purple

    -- Heikin Ashi streaks (separate pane)
    haGreenStreakOut = instance:addStream("HA_GREEN", core.Line, name .. ".HA_GREEN", "HA Green Streak", core.rgb(38, 166, 154), first)
    haRedStreakOut   = instance:addStream("HA_RED",   core.Line, name .. ".HA_RED",   "HA Red Streak",   core.rgb(239, 83, 80), first)

    -- ATR (separate pane)
    atrOut = instance:addStream("ATR", core.Line, name .. ".ATR", "ATR", core.rgb(255, 87, 34), first)  -- deep orange

    -- Ichimoku
    ichiTenkanOut  = instance:addStream("ICHI_TEN", core.Line, name .. ".ICHI_TEN", "Tenkan",   core.rgb(0, 149, 255), first)   -- blue
    ichiKijunOut   = instance:addStream("ICHI_KIJ", core.Line, name .. ".ICHI_KIJ", "Kijun",    core.rgb(255, 109, 0), first)   -- orange
    ichiSenkouAOut = instance:addStream("ICHI_SA",  core.Line, name .. ".ICHI_SA",  "Senkou A", core.rgb(38, 166, 154), first)  -- teal
    ichiSenkouBOut = instance:addStream("ICHI_SB",  core.Line, name .. ".ICHI_SB",  "Senkou B", core.rgb(239, 83, 80), first)   -- red

    -- Keltner Channel
    keltUpperOut = instance:addStream("KELT_UP",  core.Line, name .. ".KELT_UP",  "Keltner Upper", core.rgb(255, 111, 0), first)  -- amber
    keltMidOut   = instance:addStream("KELT_MID", core.Line, name .. ".KELT_MID", "Keltner Mid",   core.rgb(255, 111, 0), first)
    keltLowerOut = instance:addStream("KELT_LO",  core.Line, name .. ".KELT_LO",  "Keltner Lower", core.rgb(255, 111, 0), first)
end


-- =============================================================================
-- HELPER FUNCTIONS
-- These do the math for each indicator.
-- You don't need to change these unless you want to modify the formulas.
-- =============================================================================


--- Calculate EMA (Exponential Moving Average)
-- @param src   data source (e.g. close prices)
-- @param period  number of bars
-- @param i     current bar index
-- @param prevEma  previous EMA value
-- @return new EMA value
function calcEMA(price, period, prevEma)
    local k = 2.0 / (period + 1.0)
    return price * k + prevEma * (1.0 - k)
end


--- Calculate SMA (Simple Moving Average) at bar i over N bars
function calcSMA(src, i, period)
    if i - first + 1 < period then return nil end
    local sum = 0
    for j = i - period + 1, i do
        sum = sum + src[j]
    end
    return sum / period
end


--- Calculate Standard Deviation at bar i over N bars
function calcStdDev(src, i, period, sma)
    if sma == nil then return nil end
    if i - first + 1 < period then return nil end
    local sumSq = 0
    for j = i - period + 1, i do
        local diff = src[j] - sma
        sumSq = sumSq + diff * diff
    end
    return math.sqrt(sumSq / period)
end


--- Find highest value in source over N bars ending at bar i
function calcHighest(src, i, period)
    if i - first + 1 < period then return nil end
    local maxVal = src[i]
    for j = i - period + 1, i do
        if src[j] > maxVal then maxVal = src[j] end
    end
    return maxVal
end


--- Find lowest value in source over N bars ending at bar i
function calcLowest(src, i, period)
    if i - first + 1 < period then return nil end
    local minVal = src[i]
    for j = i - period + 1, i do
        if src[j] < minVal then minVal = src[j] end
    end
    return minVal
end


--- Calculate True Range at bar i
function calcTR(i)
    if i <= first then return source.high[i] - source.low[i] end
    local hl  = source.high[i] - source.low[i]
    local hpc = math.abs(source.high[i] - source.close[i - 1])
    local lpc = math.abs(source.low[i] - source.close[i - 1])
    return math.max(hl, math.max(hpc, lpc))
end


-- =============================================================================
-- UPDATE FUNCTION
-- Called for each bar on the chart.
-- This is where all the indicators are calculated and drawn.
-- =============================================================================

-- Persistent state across bars (used by indicators that need memory)
local emaFastPrev, emaMidPrev, emaSlowPrev, emaUltraPrev
local rsiAvgGain, rsiAvgLoss
local macdEmaFastPrev, macdEmaSlowPrev, macdSignalPrev
local haOpenPrev
local haConsecGreen, haConsecRed
local stTrend, stFinalUpper, stFinalLower, stATRprev
local keltEmaPrev

-- Flag to know if this is the first Update call
local initialized = false

function Update(period, mode)
    -- "period" here is the bar index (confusing naming by FXCM, sorry)
    local i = period

    -- Skip bars where we don't have enough data
    if i < first then return end

    local closeVal = source.close[i]
    local highVal  = source.high[i]
    local lowVal   = source.low[i]
    local openVal  = source.open[i]


    -- =================================================================
    -- SECTION 1: EMA CALCULATION
    -- =================================================================
    if SHOW_EMA then
        if i == first then
            -- First bar: EMA starts at the close price
            emaFastPrev  = closeVal
            emaMidPrev   = closeVal
            emaSlowPrev  = closeVal
            emaUltraPrev = closeVal
        else
            emaFastPrev  = calcEMA(closeVal, EMA_FAST,  emaFastPrev)
            emaMidPrev   = calcEMA(closeVal, EMA_MID,   emaMidPrev)
            emaSlowPrev  = calcEMA(closeVal, EMA_SLOW,  emaSlowPrev)
            emaUltraPrev = calcEMA(closeVal, EMA_ULTRA, emaUltraPrev)
        end
        emaFastOut[i]  = emaFastPrev
        emaMidOut[i]   = emaMidPrev
        emaSlowOut[i]  = emaSlowPrev
        emaUltraOut[i] = emaUltraPrev
    end


    -- =================================================================
    -- SECTION 2: BOLLINGER BANDS CALCULATION
    -- =================================================================
    if SHOW_BB then
        local bbMid = calcSMA(source.close, i, BB_PERIOD)
        if bbMid ~= nil then
            local bbStd = calcStdDev(source.close, i, BB_PERIOD, bbMid)
            if bbStd ~= nil then
                bbUpperOut[i]  = bbMid + BB_STDDEV * bbStd
                bbMiddleOut[i] = bbMid
                bbLowerOut[i]  = bbMid - BB_STDDEV * bbStd
            end
        end
    end


    -- =================================================================
    -- SECTION 3: DONCHIAN CHANNEL CALCULATION
    -- =================================================================
    if SHOW_DONCH then
        local dUpper = calcHighest(source.high, i, DONCH_ENTRY)
        local dLower = calcLowest(source.low, i, DONCH_EXIT)
        if dUpper ~= nil and dLower ~= nil then
            donchUpperOut[i] = dUpper
            donchLowerOut[i] = dLower
            donchMidOut[i]   = (dUpper + dLower) / 2
        end
    end


    -- =================================================================
    -- SECTION 4: SUPERTREND CALCULATION
    -- =================================================================
    if SHOW_ST then
        -- ATR for Supertrend
        local tr = calcTR(i)
        if i == first then
            stATRprev    = tr
            stTrend      = 1   -- 1 = bullish, -1 = bearish
            stFinalUpper = (highVal + lowVal) / 2 + ST_MULT * tr
            stFinalLower = (highVal + lowVal) / 2 - ST_MULT * tr
        else
            -- Smoothed ATR (simple running average)
            stATRprev = (stATRprev * (ST_ATR - 1) + tr) / ST_ATR

            local hl2 = (highVal + lowVal) / 2
            local upperBand = hl2 + ST_MULT * stATRprev
            local lowerBand = hl2 - ST_MULT * stATRprev

            -- Tighten bands (standard Supertrend logic)
            if lowerBand > stFinalLower or source.close[i - 1] < stFinalLower then
                stFinalLower = lowerBand
            end
            if upperBand < stFinalUpper or source.close[i - 1] > stFinalUpper then
                stFinalUpper = upperBand
            end

            -- Determine trend direction
            if stTrend == 1 then
                if closeVal < stFinalLower then
                    stTrend = -1
                end
            else
                if closeVal > stFinalUpper then
                    stTrend = 1
                end
            end
        end

        -- Plot the appropriate band
        if stTrend == 1 then
            supertrendOut[i] = stFinalLower
            supertrendOut:setColor(i, core.rgb(38, 166, 154))   -- green = bullish
        else
            supertrendOut[i] = stFinalUpper
            supertrendOut:setColor(i, core.rgb(239, 83, 80))    -- red = bearish
        end
    end


    -- =================================================================
    -- SECTION 5: RSI CALCULATION
    -- =================================================================
    if SHOW_RSI then
        if i == first then
            rsiAvgGain = 0
            rsiAvgLoss = 0
        elseif i > first then
            local change = closeVal - source.close[i - 1]
            local gain = 0
            local loss = 0
            if change > 0 then gain = change end
            if change < 0 then loss = -change end

            if i - first <= RSI_PERIOD then
                -- Initial SMA phase
                rsiAvgGain = rsiAvgGain + gain / RSI_PERIOD
                rsiAvgLoss = rsiAvgLoss + loss / RSI_PERIOD
            else
                -- Smoothed (EMA-like) average
                rsiAvgGain = (rsiAvgGain * (RSI_PERIOD - 1) + gain) / RSI_PERIOD
                rsiAvgLoss = (rsiAvgLoss * (RSI_PERIOD - 1) + loss) / RSI_PERIOD
            end

            if i - first >= RSI_PERIOD then
                if rsiAvgLoss == 0 then
                    rsiOut[i] = 100
                else
                    local rs = rsiAvgGain / rsiAvgLoss
                    rsiOut[i] = 100 - 100 / (1 + rs)
                end
            end
        end
    end


    -- =================================================================
    -- SECTION 6: MACD CALCULATION
    -- =================================================================
    if SHOW_MACD then
        if i == first then
            macdEmaFastPrev = closeVal
            macdEmaSlowPrev = closeVal
            macdSignalPrev  = 0
        else
            macdEmaFastPrev = calcEMA(closeVal, MACD_FAST, macdEmaFastPrev)
            macdEmaSlowPrev = calcEMA(closeVal, MACD_SLOW, macdEmaSlowPrev)
            local macdVal   = macdEmaFastPrev - macdEmaSlowPrev
            macdSignalPrev  = calcEMA(macdVal, MACD_SIGNAL, macdSignalPrev)
            local histVal   = macdVal - macdSignalPrev

            macdLineOut[i]   = macdVal
            macdSignalOut[i] = macdSignalPrev
            macdHistOut[i]   = histVal
        end
    end


    -- =================================================================
    -- SECTION 7: HEIKIN ASHI STREAK CALCULATION
    -- =================================================================
    if SHOW_HA then
        -- Heikin Ashi candle calculation
        local haClose = (openVal + highVal + lowVal + closeVal) / 4.0
        local haOpen

        if i == first then
            haOpen = (openVal + closeVal) / 2.0
            haConsecGreen = 0
            haConsecRed   = 0
        else
            haOpen = (haOpenPrev + source._haClosePrev) / 2.0
        end

        -- Store for next bar
        haOpenPrev = haOpen
        -- We store haClose in a trick: attach it to the source table
        source._haClosePrev = haClose

        -- Is this HA candle green or red?
        local isGreen = haClose > haOpen

        -- Count consecutive streaks
        if isGreen then
            haConsecGreen = haConsecGreen + 1
            haConsecRed   = 0
        else
            haConsecRed   = haConsecRed + 1
            haConsecGreen = 0
        end

        haGreenStreakOut[i] = haConsecGreen
        haRedStreakOut[i]   = haConsecRed

        -- Mark entry/exit signals as spikes in the streak count
        -- (the visual signal: streak hits the threshold)
        -- You can watch for haConsecGreen >= HA_GREEN in the output
        -- and haConsecRed >= HA_RED as your entry/exit triggers
    end


    -- =================================================================
    -- SECTION 8: ATR CALCULATION
    -- =================================================================
    if SHOW_ATR then
        if i >= first + ATR_PERIOD then
            local atrSum = 0
            for j = i - ATR_PERIOD + 1, i do
                atrSum = atrSum + calcTR(j)
            end
            atrOut[i] = atrSum / ATR_PERIOD
        end
    end


    -- =================================================================
    -- SECTION 9: ICHIMOKU CLOUD CALCULATION
    -- =================================================================
    if SHOW_ICHI then
        local tenkan = nil
        local kijun  = nil

        local tHigh = calcHighest(source.high, i, ICHI_TENKAN)
        local tLow  = calcLowest(source.low, i, ICHI_TENKAN)
        if tHigh ~= nil and tLow ~= nil then
            tenkan = (tHigh + tLow) / 2
            ichiTenkanOut[i] = tenkan
        end

        local kHigh = calcHighest(source.high, i, ICHI_KIJUN)
        local kLow  = calcLowest(source.low, i, ICHI_KIJUN)
        if kHigh ~= nil and kLow ~= nil then
            kijun = (kHigh + kLow) / 2
            ichiKijunOut[i] = kijun
        end

        -- Senkou Span A = (tenkan + kijun) / 2
        -- Note: In FXCM, we can't easily shift forward. We plot at current bar.
        -- For proper cloud displacement, use FXCM's built-in Ichimoku indicator.
        if tenkan ~= nil and kijun ~= nil then
            ichiSenkouAOut[i] = (tenkan + kijun) / 2
        end

        -- Senkou Span B
        local sHigh = calcHighest(source.high, i, ICHI_SENKOU)
        local sLow  = calcLowest(source.low, i, ICHI_SENKOU)
        if sHigh ~= nil and sLow ~= nil then
            ichiSenkouBOut[i] = (sHigh + sLow) / 2
        end
    end


    -- =================================================================
    -- SECTION 10: KELTNER CHANNEL CALCULATION
    -- =================================================================
    if SHOW_KELT then
        if i == first then
            keltEmaPrev = closeVal
        else
            keltEmaPrev = calcEMA(closeVal, KELT_EMA, keltEmaPrev)
        end

        -- ATR for Keltner
        if i >= first + KELT_ATR then
            local katrSum = 0
            for j = i - KELT_ATR + 1, i do
                katrSum = katrSum + calcTR(j)
            end
            local katr = katrSum / KELT_ATR

            keltUpperOut[i] = keltEmaPrev + KELT_MULT * katr
            keltMidOut[i]   = keltEmaPrev
            keltLowerOut[i] = keltEmaPrev - KELT_MULT * katr
        end
    end

end
