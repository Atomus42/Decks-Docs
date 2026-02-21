-- =============================================================================
--
--  STRATEGIE VISUELLE HEIKIN ASHI WEEKLY (12G/6R) — TOUT-EN-UN
--  Pour FXCM Trading Station Desktop (Lua / Indicore SDK)
--
--  CE FICHIER FAIT TOUT:
--  ✔ Affiche les bougies Heikin Ashi (vertes/rouges) sur le graphique
--  ✔ Affiche des fleches BUY / SELL avec texte sur le graphique
--  ✔ Affiche le compteur de streak (1, 2, 3... 12) sous chaque bougie
--  ✔ Colore les zones "en position" vs "hors position"
--  ✔ Simule la strategie sur TOUT l'historique visible
--  ✔ Montre les resultats (nombre de trades, P&L) dans un tableau
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

-- Fleches et texte
local buy_arrow = nil;       -- Fleche BUY
local sell_arrow = nil;      -- Fleche SELL
local streak_text = nil;     -- Compteur streak
local pos_marker = nil;      -- Marqueur de position (dot en position)

-- Suivi de position (simulation)
local in_position = false;
local entry_price = 0;
local total_trades = 0;
local winning_trades = 0;
local total_pnl_pct = 0;

-- Polices pour drawLabel1
local font_buy = nil;
local font_sell = nil;
local font_info = nil;
local label_id = 0;


-- =============================================================================
-- FONCTION INIT()
-- =============================================================================
function Init()
    indicator:name("HA 12G/6R Visual Strategy");
    indicator:description(
        "Strategie visuelle Heikin Ashi 12G/6R.\n" ..
        "Affiche bougies HA, fleches BUY/SELL, compteur streak,\n" ..
        "et simule la strategie sur tout l'historique.\n" ..
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
    --  CHANGEZ CE NOMBRE pour modifier le seuil d'entree (defaut: 12)

    indicator.parameters:addInteger("red_threshold",
        "Bougies HA rouges pour SELL", "", 6, 1, 50);
    --  CHANGEZ CE NOMBRE pour modifier le seuil de sortie (defaut: 6)

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
        "Marqueur 'en position'", "", core.rgb(100, 180, 255));

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
    -- Bougies Heikin Ashi (4 streams regroupes en candle group)
    -- =====================================================================
    ha_open_out = instance:addStream("HA_O", core.Line, name .. ".Open",
        "HA Open", instance.parameters.clrBullCandle, 0);
    ha_high_out = instance:addStream("HA_H", core.Line, name .. ".High",
        "HA High", instance.parameters.clrBullCandle, 0);
    ha_low_out = instance:addStream("HA_L", core.Line, name .. ".Low",
        "HA Low", instance.parameters.clrBullCandle, 0);
    ha_close_out = instance:addStream("HA_C", core.Line, name .. ".Close",
        "HA Close", instance.parameters.clrBullCandle, 0);

    instance:createCandleGroup("HA", "Bougies Heikin Ashi",
        ha_open_out, ha_high_out, ha_low_out, ha_close_out);

    -- =====================================================================
    -- Fleches BUY / SELL (Wingdings)
    -- \233 = grosse fleche haut, \234 = grosse fleche bas
    -- =====================================================================
    buy_arrow = instance:createTextOutput("BUY", "BUY Signal",
        "Wingdings", 16,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);

    sell_arrow = instance:createTextOutput("SELL", "SELL Signal",
        "Wingdings", 16,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSell, 0);

    -- =====================================================================
    -- Compteur streak (petit texte sous les bougies)
    -- =====================================================================
    streak_text = instance:createTextOutput("Streak", "Streak Count",
        "Arial", 7,
        core.H_Center, core.V_Top,
        core.rgb(180, 180, 180), 0);

    -- =====================================================================
    -- Marqueur de position (petit point quand en position)
    -- =====================================================================
    pos_marker = instance:createTextOutput("InPos", "In Position",
        "Wingdings", 8,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrInPos, 0);

    -- Reinitialiser la simulation
    in_position = false;
    entry_price = 0;
    total_trades = 0;
    winning_trades = 0;
    total_pnl_pct = 0;
    label_id = 10000;

    -- Creer les polices pour les labels texte BUY/SELL
    font_buy = core.host:execute("createFont", "Arial", 10, true, false);
    font_sell = core.host:execute("createFont", "Arial", 10, true, false);
    font_info = core.host:execute("createFont", "Arial", 9, true, false);
end


-- =============================================================================
-- FONCTION ReleaseInstance()
-- Nettoyer les polices a la fermeture (OBLIGATOIRE pour eviter les fuites)
-- =============================================================================
function ReleaseInstance()
    if font_buy ~= nil then
        core.host:execute("deleteFont", font_buy);
    end
    if font_sell ~= nil then
        core.host:execute("deleteFont", font_sell);
    end
    if font_info ~= nil then
        core.host:execute("deleteFont", font_info);
    end
end


-- =============================================================================
-- FONCTION Update()
-- Appelee pour CHAQUE bougie de l'historique.
-- Calcule le HA, compte le streak, simule la strategie, dessine tout.
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

    local new_ha_close = (c_open + c_high + c_low + c_close) / 4.0;

    local new_ha_open;
    if period <= 1 then
        new_ha_open = (c_open + c_close) / 2.0;
    else
        new_ha_open = (ha_open_out[period - 1] + ha_close_out[period - 1]) / 2.0;
    end

    local new_ha_high = math.max(c_high, new_ha_open, new_ha_close);
    local new_ha_low  = math.min(c_low, new_ha_open, new_ha_close);

    -- Ecrire dans les streams (dessine les bougies HA sur le graphique)
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
    -- 4. SIMULER LA STRATEGIE (sur tout l'historique)
    -- ==================================================================
    local green_threshold = instance.parameters.green_threshold;
    local red_threshold = instance.parameters.red_threshold;

    -- ----- SIGNAL D'ACHAT -----
    if consec_green >= green_threshold and not in_position then
        in_position = true;
        entry_price = c_close;  -- prix d'entree = close de la bougie reelle

        -- Fleche BUY (Wingdings \233 = grosse fleche vers le haut)
        buy_arrow:set(period, source.low[period], "\233");

        -- Label texte "BUY" au-dessus de la fleche
        label_id = label_id + 1;
        core.host:execute("drawLabel1", label_id,
            source:date(period), core.CR_CHART,
            source.low[period], core.CR_CHART,
            core.H_Center, core.V_Top,
            font_buy, instance.parameters.clrBuy,
            "BUY");
    end

    -- ----- SIGNAL DE VENTE -----
    if consec_red >= red_threshold and in_position then
        in_position = false;

        -- Calculer le P&L de ce trade
        local trade_pnl = 0;
        if entry_price > 0 then
            trade_pnl = ((c_close - entry_price) / entry_price) * 100;
        end
        total_trades = total_trades + 1;
        total_pnl_pct = total_pnl_pct + trade_pnl;
        if trade_pnl > 0 then
            winning_trades = winning_trades + 1;
        end

        -- Fleche SELL (Wingdings \234 = grosse fleche vers le bas)
        sell_arrow:set(period, source.high[period], "\234");

        -- Label texte "SELL" + P&L
        label_id = label_id + 1;
        local pnl_text = "SELL";
        if trade_pnl >= 0 then
            pnl_text = "SELL +" .. string.format("%.1f", trade_pnl) .. "%";
        else
            pnl_text = "SELL " .. string.format("%.1f", trade_pnl) .. "%";
        end
        core.host:execute("drawLabel1", label_id,
            source:date(period), core.CR_CHART,
            source.high[period], core.CR_CHART,
            core.H_Center, core.V_Bottom,
            font_sell, instance.parameters.clrSell,
            pnl_text);

        entry_price = 0;
    end

    -- ==================================================================
    -- 5. AFFICHER MARQUEUR "EN POSITION"
    -- ==================================================================
    if instance.parameters.showPositionDots and in_position then
        -- Petit point bleu au-dessus de chaque bougie quand en position
        -- Wingdings \159 = petit cercle plein
        pos_marker:set(period, source.high[period], "\159");
    end

    -- ==================================================================
    -- 6. TABLEAU RECAPITULATIF (sur la derniere bougie)
    -- ==================================================================
    if period == source:size() - 1 then
        -- Afficher un resume en haut a droite du graphique
        local win_rate = 0;
        if total_trades > 0 then
            win_rate = (winning_trades / total_trades) * 100;
        end

        local status_text;
        if in_position then
            status_text = "EN POSITION";
        else
            status_text = "HORS POSITION";
        end

        local summary = "HA 12G/6R | "
            .. "Trades: " .. total_trades
            .. " | Win: " .. string.format("%.0f", win_rate) .. "%"
            .. " | P&L: " .. string.format("%.1f", total_pnl_pct) .. "%"
            .. " | " .. status_text;

        label_id = label_id + 1;
        core.host:execute("drawLabel1", label_id,
            5, core.CR_RIGHT,
            5, core.CR_TOP,
            core.H_Right, core.V_Top,
            font_info, core.rgb(255, 255, 255),
            summary);
    end
end
