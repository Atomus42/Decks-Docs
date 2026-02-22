-- =============================================================================
--
--  INDICATEUR VISUEL HEIKIN ASHI WEEKLY (12G/6R)
--  Pour FXCM Trading Station Desktop (Lua / Indicore SDK)
--
--  CET INDICATEUR AFFICHE SUR LE GRAPHIQUE:
--  - Les bougies Heikin Ashi (vertes et rouges) en superposition
--  - Des FLECHES vers le haut quand le signal ACHAT se declenche (12 vertes)
--  - Des FLECHES vers le bas quand le signal VENTE se declenche (6 rouges)
--  - Le compteur de streak (nombre de bougies consecutives) en bas
--
--  ATTENTION: Ceci est un INDICATEUR, pas une strategie.
--  Il ne passe AUCUN ordre. Il montre visuellement les signaux.
--  Utilisez-le AVEC la strategie btc_1h_heikin_ashi_strategy.lua
--  ou seul pour du trading manuel.
--
--  INSTALLATION:
--  1. Fermez completement Trading Station
--  2. Copiez ce fichier (.lua) dans:
--     C:\Program Files (x86)\Candleworks\FXTS2\indicators\Custom\
--     ATTENTION: c'est le dossier "indicators", pas "strategies" !
--  3. Relancez Trading Station et connectez-vous
--  4. Ouvrez un graphique (ex: BTC/USD en H1)
--  5. Clic droit sur le graphique > "Ajouter un indicateur"
--  6. Cherchez "HA Weekly 12G/6R Visual" dans la liste
--  7. Cliquez OK
--
-- =============================================================================


-- =============================================================================
-- VARIABLES GLOBALES
-- =============================================================================
local first = nil;          -- Premiere periode valide
local source = nil;         -- Source de donnees (bougies)

-- Sorties visuelles (ce qui s'affiche sur le graphique)
local ha_open_out = nil;    -- Ligne HA Open (pour dessiner les bougies HA)
local ha_close_out = nil;   -- Ligne HA Close
local ha_high_out = nil;    -- Ligne HA High
local ha_low_out = nil;     -- Ligne HA Low
local up_arrow = nil;       -- Fleche ACHAT (vers le haut)
local down_arrow = nil;     -- Fleche VENTE (vers le bas)
local streak_out = nil;     -- Texte du compteur de streak

-- Etat interne du calcul
local prev_ha_open = 0;
local prev_ha_close = 0;


-- =============================================================================
-- FONCTION INIT()
-- =============================================================================
function Init()
    indicator:name("HA Weekly 12G/6R Visual");
    indicator:description(
        "Indicateur visuel Heikin Ashi avec signaux 12G/6R.\n" ..
        "Affiche bougies HA, fleches achat/vente, compteur streak."
    );
    indicator:requiredSource(core.Bar);    -- Necessite des bougies OHLC
    indicator:type(core.Indicator);        -- Type indicateur (sur le graphique principal)

    -- =====================================================================
    -- PARAMETRES MODIFIABLES
    -- =====================================================================
    -- === Seuils de Signal ===

    -- Nombre de bougies HA vertes pour signal ACHAT
    indicator.parameters:addInteger("green_threshold", "Bougies vertes pour signal ACHAT", "", 12, 1, 50);

    -- Nombre de bougies HA rouges pour signal VENTE
    indicator.parameters:addInteger("red_threshold", "Bougies rouges pour signal VENTE", "", 6, 1, 50);

    -- =====================================================================
    -- COULEURS DES BOUGIES HEIKIN ASHI
    -- =====================================================================
    -- === Couleurs ===

    indicator.parameters:addColor("clrGreen", "Couleur bougie HA verte (haussiere)", "", core.rgb(38, 166, 154));
    indicator.parameters:addColor("clrRed", "Couleur bougie HA rouge (baissiere)", "", core.rgb(239, 83, 80));
    indicator.parameters:addColor("clrBuy", "Couleur fleche ACHAT", "", core.rgb(0, 200, 0));
    indicator.parameters:addColor("clrSell", "Couleur fleche VENTE", "", core.rgb(255, 50, 50));
end


-- =============================================================================
-- FONCTION PREPARE()
-- Configure les sorties visuelles qui s'afficheront sur le graphique.
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
    -- Creer les 4 sorties pour dessiner les bougies Heikin Ashi
    -- On les regroupe en "candle group" pour que Trading Station
    -- les affiche comme de vraies bougies sur le graphique.
    -- =====================================================================
    ha_open_out = instance:addStream("HA_Open", core.Line, name .. ".HA_Open", "HA Open", instance.parameters.clrGreen, first);
    ha_high_out = instance:addStream("HA_High", core.Line, name .. ".HA_High", "HA High", instance.parameters.clrGreen, first);
    ha_low_out = instance:addStream("HA_Low", core.Line, name .. ".HA_Low", "HA Low", instance.parameters.clrGreen, first);
    ha_close_out = instance:addStream("HA_Close", core.Line, name .. ".HA_Close", "HA Close", instance.parameters.clrGreen, first);

    -- Regrouper les 4 lignes en une bougie visuelle
    instance:createCandleGroup("HA_Candles", "Bougies HA",
        ha_open_out, ha_high_out, ha_low_out, ha_close_out);

    -- =====================================================================
    -- Creer les fleches d'achat et de vente
    -- On utilise la police Wingdings:
    --   \225 = fleche vers le haut (achat)
    --   \226 = fleche vers le bas (vente)
    -- =====================================================================
    up_arrow = instance:createTextOutput("BuyArrow", "Signal ACHAT",
        "Wingdings", 14,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);

    down_arrow = instance:createTextOutput("SellArrow", "Signal VENTE",
        "Wingdings", 14,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSell, 0);

    -- =====================================================================
    -- Texte du compteur de streak (affiche le nombre sous chaque bougie)
    -- =====================================================================
    streak_out = instance:createTextOutput("Streak", "Compteur Streak",
        "Arial", 7,
        core.H_Center, core.V_Top,
        core.rgb(180, 180, 180), 0);

    first = 1;  -- On commence au calcul a partir de la 2eme bougie
end


-- =============================================================================
-- FONCTION UPDATE()
-- Appelee pour chaque bougie. Calcule le Heikin Ashi et affiche les signaux.
-- =============================================================================
function Update(period, mode)
    -- Il faut au moins 2 bougies
    if period < 1 then
        return;
    end

    -- ==================================================================
    -- ETAPE 1: Calculer la bougie Heikin Ashi
    -- ==================================================================
    local c_open  = source.open[period];
    local c_high  = source.high[period];
    local c_low   = source.low[period];
    local c_close = source.close[period];

    -- HA Close = moyenne des 4 prix
    local new_ha_close = (c_open + c_high + c_low + c_close) / 4.0;

    -- HA Open
    local new_ha_open;
    if period == 1 then
        -- Premiere bougie: HA_Open = (Open + Close) / 2
        new_ha_open = (c_open + c_close) / 2.0;
    else
        -- Bougies suivantes: utiliser les valeurs precedentes
        new_ha_open = (ha_open_out[period - 1] + ha_close_out[period - 1]) / 2.0;
    end

    -- HA High et HA Low
    local new_ha_high = math.max(c_high, new_ha_open, new_ha_close);
    local new_ha_low  = math.min(c_low, new_ha_open, new_ha_close);

    -- ==================================================================
    -- ETAPE 2: Ecrire les valeurs dans les sorties (dessine les bougies)
    -- ==================================================================
    ha_open_out[period] = new_ha_open;
    ha_close_out[period] = new_ha_close;
    ha_high_out[period] = new_ha_high;
    ha_low_out[period] = new_ha_low;

    -- Colorer la bougie: vert si haussiere, rouge si baissiere
    local isGreen = (new_ha_close > new_ha_open);
    if isGreen then
        ha_open_out:setColor(period, instance.parameters.clrGreen);
        ha_close_out:setColor(period, instance.parameters.clrGreen);
        ha_high_out:setColor(period, instance.parameters.clrGreen);
        ha_low_out:setColor(period, instance.parameters.clrGreen);
    else
        ha_open_out:setColor(period, instance.parameters.clrRed);
        ha_close_out:setColor(period, instance.parameters.clrRed);
        ha_high_out:setColor(period, instance.parameters.clrRed);
        ha_low_out:setColor(period, instance.parameters.clrRed);
    end

    -- ==================================================================
    -- ETAPE 3: Compter les streaks (bougies consecutives)
    -- On recalcule en arriere a partir de la bougie courante
    -- ==================================================================
    local consec_green = 0;
    local consec_red = 0;

    -- Compter les bougies vertes consecutives jusqu'a la courante
    local p = period;
    while p >= 1 do
        if ha_close_out[p] > ha_open_out[p] then
            consec_green = consec_green + 1;
            p = p - 1;
        else
            break;
        end
    end

    -- Si pas de streak vert, compter les rouges
    if consec_green == 0 then
        p = period;
        while p >= 1 do
            if ha_close_out[p] <= ha_open_out[p] then
                consec_red = consec_red + 1;
                p = p - 1;
            else
                break;
            end
        end
    end

    -- ==================================================================
    -- ETAPE 4: Afficher le compteur de streak sous la bougie
    -- ==================================================================
    if consec_green > 0 then
        streak_out:set(period, source.low[period], tostring(consec_green), core.rgb(38, 166, 154));
    elseif consec_red > 0 then
        streak_out:set(period, source.low[period], tostring(consec_red), core.rgb(239, 83, 80));
    end

    -- ==================================================================
    -- ETAPE 5: Afficher les fleches de signal
    -- ==================================================================
    local green_threshold = instance.parameters.green_threshold;
    local red_threshold = instance.parameters.red_threshold;

    -- Fleche ACHAT: exactement au moment ou le seuil est atteint
    if consec_green == green_threshold then
        -- \225 = fleche vers le haut dans Wingdings
        up_arrow:set(period, source.low[period], "\225");
    end

    -- Fleche VENTE: exactement au moment ou le seuil est atteint
    if consec_red == red_threshold then
        -- \226 = fleche vers le bas dans Wingdings
        down_arrow:set(period, source.high[period], "\226");
    end
end
