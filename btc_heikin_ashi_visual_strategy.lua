-- =============================================================================
--
--  STRATEGIE VISUELLE HEIKIN ASHI WEEKLY (12G/6R) — TOUT-EN-UN
--  Pour FXCM Trading Station Desktop (Lua / Indicore SDK)
--  Compatible avec TOUTES les versions de Trading Station
--
--  CE FICHIER AFFICHE SUR LE GRAPHIQUE (sans modifier les chandeliers):
--  - Des fleches BUY (vertes, sous la bougie) aux signaux d'achat
--  - Des fleches SELL (rouges, au-dessus) aux signaux de vente
--  - Le texte "BUY" et "SELL +X%" a cote des fleches
--  - Le compteur de streak (1, 2, 3... 12) sous chaque bougie
--  - Des points bleus au-dessus des bougies quand "en position"
--
--  VOS CHANDELIERS ROUGE/NOIR RESTENT TELS QUELS.
--  Le calcul Heikin Ashi se fait en arriere-plan (invisible).
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
--  5. Vous verrez les fleches BUY/SELL sur vos chandeliers normaux
--
-- =============================================================================


-- =============================================================================
-- VARIABLES GLOBALES
-- =============================================================================
local source = nil;

-- Calcul Heikin Ashi interne (pas affiche, juste pour les signaux)
local ha_open_arr = {};      -- Tableau des HA Open par periode
local ha_close_arr = {};     -- Tableau des HA Close par periode

-- Fleches et textes (createTextOutput — compatible toutes versions)
local buy_arrow = nil;       -- Fleche BUY (Wingdings)
local buy_label = nil;       -- Texte "BUY"
local sell_arrow = nil;      -- Fleche SELL (Wingdings)
local sell_label = nil;      -- Texte "SELL +X%"
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
        "Fleches BUY/SELL + compteur streak sur vos chandeliers normaux.\n" ..
        "Le calcul HA est invisible, seuls les signaux s'affichent.\n" ..
        "Backtest: +78.40% | Sharpe 1.53 | PF 1.94"
    );
    indicator:requiredSource(core.Bar);
    indicator:type(core.Indicator);

    -- =====================================================================
    -- PARAMETRES: Seuils
    -- =====================================================================
    -- === Seuils de Signal ===

    indicator.parameters:addInteger("green_threshold",
        "Bougies HA vertes pour BUY", "", 12, 1, 50);

    indicator.parameters:addInteger("red_threshold",
        "Bougies HA rouges pour SELL", "", 6, 1, 50);

    -- =====================================================================
    -- PARAMETRES: Visuel
    -- =====================================================================
    -- === Couleurs et Affichage ===

    indicator.parameters:addColor("clrBuy",
        "Fleche et texte BUY", "", core.rgb(0, 220, 100));
    indicator.parameters:addColor("clrSell",
        "Fleche et texte SELL", "", core.rgb(255, 60, 60));
    indicator.parameters:addColor("clrStreakGreen",
        "Compteur streak haussier", "", core.rgb(38, 166, 154));
    indicator.parameters:addColor("clrStreakRed",
        "Compteur streak baissier", "", core.rgb(239, 83, 80));
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

    -- PAS de bougies HA dessinees — on garde les chandeliers normaux

    -- =====================================================================
    -- Fleche BUY: grosse fleche verte vers le haut, sous la bougie
    -- =====================================================================
    buy_arrow = instance:createTextOutput("BuyArrow", "BUY Arrow",
        "Wingdings", 18,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);

    buy_label = instance:createTextOutput("BuyText", "BUY Label",
        "Arial", 10,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, -15);

    -- =====================================================================
    -- Fleche SELL: grosse fleche rouge vers le bas, au-dessus de la bougie
    -- =====================================================================
    sell_arrow = instance:createTextOutput("SellArrow", "SELL Arrow",
        "Wingdings", 18,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSell, 0);

    sell_label = instance:createTextOutput("SellText", "SELL Label",
        "Arial", 10,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSell, -15);

    -- =====================================================================
    -- Compteur streak
    -- =====================================================================
    streak_text = instance:createTextOutput("Streak", "Streak Count",
        "Arial", 7,
        core.H_Center, core.V_Top,
        core.rgb(180, 180, 180), 0);

    -- =====================================================================
    -- Marqueur de position (losange bleu)
    -- =====================================================================
    pos_marker = instance:createTextOutput("InPos", "In Position",
        "Wingdings", 6,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrInPos, 0);

    -- Reinitialiser
    in_position = false;
    entry_price = 0;
    ha_open_arr = {};
    ha_close_arr = {};
end


-- =============================================================================
-- FONCTION Update()
-- =============================================================================
function Update(period, mode)
    if period < 1 then
        return;
    end

    -- ==================================================================
    -- 1. CALCULER LA BOUGIE HEIKIN ASHI (en arriere-plan, invisible)
    -- ==================================================================
    local c_open  = source.open[period];
    local c_high  = source.high[period];
    local c_low   = source.low[period];
    local c_close = source.close[period];

    local new_ha_close = (c_open + c_high + c_low + c_close) / 4.0;

    local new_ha_open;
    if period <= 1 or ha_open_arr[period - 1] == nil then
        new_ha_open = (c_open + c_close) / 2.0;
    else
        new_ha_open = (ha_open_arr[period - 1] + ha_close_arr[period - 1]) / 2.0;
    end

    -- Stocker dans les tableaux internes (pas affiche)
    ha_open_arr[period] = new_ha_open;
    ha_close_arr[period] = new_ha_close;

    local isGreen = (new_ha_close > new_ha_open);

    -- ==================================================================
    -- 2. COMPTER LES STREAKS
    -- ==================================================================
    local consec_green = 0;
    local consec_red = 0;

    local p = period;
    if isGreen then
        while p >= 1 and ha_close_arr[p] ~= nil and ha_open_arr[p] ~= nil
              and ha_close_arr[p] > ha_open_arr[p] do
            consec_green = consec_green + 1;
            p = p - 1;
        end
    else
        while p >= 1 and ha_close_arr[p] ~= nil and ha_open_arr[p] ~= nil
              and ha_close_arr[p] <= ha_open_arr[p] do
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
                instance.parameters.clrStreakGreen);
        elseif consec_red > 0 then
            streak_text:set(period, source.low[period],
                tostring(consec_red),
                instance.parameters.clrStreakRed);
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

        buy_arrow:set(period, source.low[period], "\233");
        buy_label:set(period, source.low[period], "BUY");
    end

    -- ---- SIGNAL SELL ----
    if consec_red >= red_threshold and in_position then
        in_position = false;

        local trade_pnl = 0;
        if entry_price > 0 then
            trade_pnl = ((c_close - entry_price) / entry_price) * 100;
        end

        sell_arrow:set(period, source.high[period], "\234");

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
    -- 5. MARQUEUR "EN POSITION"
    -- ==================================================================
    if instance.parameters.showPositionDots and in_position then
        pos_marker:set(period, source.high[period], "\108");
    end
end
