-- =============================================================================
--
--  STRATEGIE VISUELLE HEIKIN ASHI WEEKLY (12G/6R) — TOUT-EN-UN
--  Pour FXCM Trading Station Desktop (Lua / Indicore SDK)
--  Compatible avec TOUTES les versions de Trading Station
--
--  CE FICHIER AFFICHE SUR LE GRAPHIQUE:
--  - Les bougies Heikin Ashi (vertes/rouges)
--  - Des fleches BUY (vertes, sous la bougie) aux signaux d'achat
--  - Des fleches SELL (rouges, au-dessus) aux signaux de vente
--  - Le texte "BUY" et "SELL +X%" a cote des fleches
--  - Le compteur de streak (1, 2, 3... 12) sous chaque bougie
--  - Des points bleus au-dessus des bougies quand "en position"
--
--  BACKTEST ORIGINAL (2 ans, BTC/USD 1H):
--  +78.40% | Sharpe 1.53 | MaxDD -17.78% | 53% win rate | PF 1.94
--
--  INSTALLATION:
--  1. Fermez completement Trading Station
--  2. Copiez ce fichier dans:
--     C:\Program Files (x86)\Candleworks\FXTS2\indicators\Custom\
--     *** ATTENTION: dossier "indicators", PAS "strategies" ***
--  3. Relancez Trading Station, ouvrez un graphique BTC/USD H1
--  4. Clic droit > Ajouter un indicateur > "HA 12G/6R Visual Strategy"
--  5. Vous verrez immediatement les bougies HA + fleches BUY/SELL
--     sur tout l'historique
--
-- =============================================================================


-- =============================================================================
-- VARIABLES GLOBALES
-- =============================================================================
local source = nil;

-- Sorties visuelles (bougies HA)
local ha_open_out = nil;
local ha_high_out = nil;
local ha_low_out = nil;
local ha_close_out = nil;

-- Fleches et textes (createTextOutput — compatible toutes versions)
local buy_arrow = nil;       -- Fleche BUY (Wingdings)
local buy_label = nil;       -- Texte "BUY" a cote de la fleche
local sell_arrow = nil;      -- Fleche SELL (Wingdings)
local sell_label = nil;      -- Texte "SELL +X%" a cote de la fleche
local streak_text = nil;     -- Compteur streak (1, 2, 3...)
local pos_marker = nil;      -- Point bleu quand en position

-- Suivi de position (simulation sur l'historique)
local in_position = false;
local entry_price = 0;


-- =============================================================================
-- FONCTION INIT()
-- =============================================================================
function Init()
    indicator:name("HA 12G/6R Visual Strategy");
    indicator:description(
        "Strategie visuelle Heikin Ashi 12G/6R.\n" ..
        "Affiche bougies HA, fleches BUY/SELL, compteur streak.\n" ..
        "Simule la strategie sur tout l'historique visible.\n" ..
        "Backtest: +78.40% | Sharpe 1.53 | PF 1.94"
    );
    indicator:requiredSource(core.Bar);
    indicator:type(core.Indicator);

    -- =====================================================================
    -- PARAMETRES: Seuils
    -- =====================================================================
    indicator.parameters:addGroup("Seuils de Signal");

    indicator.parameters:addInteger("green_threshold",
        "Bougies HA vertes pour BUY", "", 12, 1, 50);

    indicator.parameters:addInteger("red_threshold",
        "Bougies HA rouges pour SELL", "", 6, 1, 50);

    -- =====================================================================
    -- PARAMETRES: Visuel
    -- =====================================================================
    indicator.parameters:addGroup("Couleurs et Affichage");

    indicator.parameters:addColor("clrBullCandle",
        "Bougie HA haussiere (verte)", "", core.rgb(38, 166, 154));
    indicator.parameters:addColor("clrBearCandle",
        "Bougie HA baissiere (rouge)", "", core.rgb(239, 83, 80));
    indicator.parameters:addColor("clrBuy",
        "Fleche et texte BUY", "", core.rgb(0, 220, 100));
    indicator.parameters:addColor("clrSell",
        "Fleche et texte SELL", "", core.rgb(255, 60, 60));
    indicator.parameters:addColor("clrInPos",
        "Marqueur en position", "", core.rgb(100, 180, 255));

    indicator.parameters:addBoolean("showStreak",
        "Afficher compteur streak", "", true);
    indicator.parameters:addBoolean("showPositionDots",
        "Afficher points quand en position", "", true);
end


-- =============================================================================
-- FONCTION PREPARE()
-- =============================================================================
function Prepare(nameOnly)
    source = instance.source;
    local name = profile:id() .. "(" .. source:name() .. ", "
        .. instance.parameters.green_threshold .. "G/"
        .. instance.parameters.red_threshold .. "R)";
    instance:name(name);
    if nameOnly then
        return;
    end

    -- =====================================================================
    -- 4 streams pour dessiner les bougies Heikin Ashi
    -- =====================================================================
    ha_open_out = instance:addStream("HA_O", core.Line, name .. ".Open",
        "HA Open", instance.parameters.clrBullCandle, 0);
    ha_high_out = instance:addStream("HA_H", core.Line, name .. ".High",
        "HA High", instance.parameters.clrBullCandle, 0);
    ha_low_out = instance:addStream("HA_L", core.Line, name .. ".Low",
        "HA Low", instance.parameters.clrBullCandle, 0);
    ha_close_out = instance:addStream("HA_C", core.Line, name .. ".Close",
        "HA Close", instance.parameters.clrBullCandle, 0);

    -- Regrouper en bougies visuelles
    instance:createCandleGroup("HA", "Bougies Heikin Ashi",
        ha_open_out, ha_high_out, ha_low_out, ha_close_out);

    -- =====================================================================
    -- Fleche BUY: grosse fleche verte vers le haut, sous la bougie
    -- Wingdings char 233 = grosse fleche vers le haut
    -- =====================================================================
    buy_arrow = instance:createTextOutput("BuyArrow", "BUY Arrow",
        "Wingdings", 18,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);

    -- Texte "BUY" juste en dessous de la fleche
    buy_label = instance:createTextOutput("BuyText", "BUY Label",
        "Arial", 10,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, -15);

    -- =====================================================================
    -- Fleche SELL: grosse fleche rouge vers le bas, au-dessus de la bougie
    -- Wingdings char 234 = grosse fleche vers le bas
    -- =====================================================================
    sell_arrow = instance:createTextOutput("SellArrow", "SELL Arrow",
        "Wingdings", 18,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSell, 0);

    -- Texte "SELL +X%" juste au-dessus de la fleche
    sell_label = instance:createTextOutput("SellText", "SELL Label",
        "Arial", 10,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSell, -15);

    -- =====================================================================
    -- Compteur streak (petit texte sous les bougies)
    -- =====================================================================
    streak_text = instance:createTextOutput("Streak", "Streak Count",
        "Arial", 7,
        core.H_Center, core.V_Top,
        core.rgb(180, 180, 180), 0);

    -- =====================================================================
    -- Marqueur de position (petit cercle quand en position)
    -- Wingdings char 108 = losange plein (compatible toutes versions)
    -- =====================================================================
    pos_marker = instance:createTextOutput("InPos", "In Position",
        "Wingdings", 6,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrInPos, 0);

    -- Reinitialiser la simulation
    in_position = false;
    entry_price = 0;
end


-- =============================================================================
-- FONCTION Update()
-- Appelee pour CHAQUE bougie de l'historique.
-- =============================================================================
function Update(period, mode)
    if period < 1 then
        return;
    end

    -- ==================================================================
    -- 1. CALCULER LA BOUGIE HEIKIN ASHI
    -- ==================================================================
    local c_open  = source.open[period];
    local c_high  = source.high[period];
    local c_low   = source.low[period];
    local c_close = source.close[period];

    -- HA Close = moyenne des 4 prix
    local new_ha_close = (c_open + c_high + c_low + c_close) / 4.0;

    -- HA Open
    local new_ha_open;
    if period <= 1 then
        new_ha_open = (c_open + c_close) / 2.0;
    else
        new_ha_open = (ha_open_out[period - 1] + ha_close_out[period - 1]) / 2.0;
    end

    -- HA High / Low
    local new_ha_high = math.max(c_high, new_ha_open, new_ha_close);
    local new_ha_low  = math.min(c_low, new_ha_open, new_ha_close);

    -- Ecrire dans les streams (dessine les bougies HA)
    ha_open_out[period] = new_ha_open;
    ha_close_out[period] = new_ha_close;
    ha_high_out[period] = new_ha_high;
    ha_low_out[period] = new_ha_low;

    -- Colorer vert ou rouge
    local isGreen = (new_ha_close > new_ha_open);
    local candle_color;
    if isGreen then
        candle_color = instance.parameters.clrBullCandle;
    else
        candle_color = instance.parameters.clrBearCandle;
    end
    ha_open_out:setColor(period, candle_color);
    ha_close_out:setColor(period, candle_color);
    ha_high_out:setColor(period, candle_color);
    ha_low_out:setColor(period, candle_color);

    -- ==================================================================
    -- 2. COMPTER LES STREAKS
    -- ==================================================================
    local consec_green = 0;
    local consec_red = 0;

    local p = period;
    if isGreen then
        while p >= 1 and ha_close_out[p] > ha_open_out[p] do
            consec_green = consec_green + 1;
            p = p - 1;
        end
    else
        while p >= 1 and ha_close_out[p] <= ha_open_out[p] do
            consec_red = consec_red + 1;
            p = p - 1;
        end
    end

    -- ==================================================================
    -- 3. AFFICHER LE COMPTEUR STREAK
    -- ==================================================================
    if instance.parameters.showStreak then
        if consec_green > 0 then
            streak_text:set(period, source.low[period],
                tostring(consec_green),
                instance.parameters.clrBullCandle);
        elseif consec_red > 0 then
            streak_text:set(period, source.low[period],
                tostring(consec_red),
                instance.parameters.clrBearCandle);
        end
    end

    -- ==================================================================
    -- 4. SIMULER LA STRATEGIE
    -- ==================================================================
    local green_threshold = instance.parameters.green_threshold;
    local red_threshold = instance.parameters.red_threshold;

    -- ---- SIGNAL BUY ----
    if consec_green >= green_threshold and not in_position then
        in_position = true;
        entry_price = c_close;

        -- Fleche verte vers le haut sous la bougie
        buy_arrow:set(period, source.low[period], "\233");
        -- Texte "BUY" sous la fleche
        buy_label:set(period, source.low[period], "BUY");
    end

    -- ---- SIGNAL SELL ----
    if consec_red >= red_threshold and in_position then
        in_position = false;

        -- Calculer le P&L de ce trade
        local trade_pnl = 0;
        if entry_price > 0 then
            trade_pnl = ((c_close - entry_price) / entry_price) * 100;
        end

        -- Fleche rouge vers le bas au-dessus de la bougie
        sell_arrow:set(period, source.high[period], "\234");

        -- Texte "SELL +X%" au-dessus de la fleche
        local pnl_str;
        if trade_pnl >= 0 then
            pnl_str = "SELL +" .. string.format("%.1f", trade_pnl) .. "%";
        else
            pnl_str = "SELL " .. string.format("%.1f", trade_pnl) .. "%";
        end
        sell_label:set(period, source.high[period], pnl_str);

        entry_price = 0;
    end

    -- ==================================================================
    -- 5. MARQUEUR "EN POSITION" (point bleu)
    -- ==================================================================
    if instance.parameters.showPositionDots and in_position then
        -- Wingdings char 108 = losange plein
        pos_marker:set(period, source.high[period], "\108");
    end
end
