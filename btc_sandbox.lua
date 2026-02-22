-- #############################################################################
-- #############################################################################
-- ##                                                                         ##
-- ##   SANDBOX DE TRADING — VOTRE LABORATOIRE PERSONNEL                     ##
-- ##                                                                         ##
-- ##   Pour FXCM Trading Station Desktop v01.16+ (Lua / Indicore SDK)        ##
-- ##   Compatible TOUTES versions — Pas de drawLabel1/createFont/addGroup    ##
-- ##                                                                         ##
-- ##   CE FICHIER EST VOTRE TERRAIN DE JEU.                                  ##
-- ##   Tous les indicateurs sont pre-calcules et prets a l'emploi.           ##
-- ##   Votre seul travail: ecrire VOS regles dans maStrategie().             ##
-- ##                                                                         ##
-- #############################################################################
-- #############################################################################
--
--
-- =============================================================================
-- COMMENT UTILISER CE FICHIER
-- =============================================================================
--
-- 1. INSTALLATION:
--    Copier dans: C:\Program Files (x86)\Candleworks\FXTS2\indicators\Custom\
--    Ouvrir un graphique BTC/USD (ou autre), clic droit > Ajouter indicateur
--    Chercher "Sandbox Trading"
--
-- 2. OU ECRIRE VOTRE STRATEGIE:
--    Allez directement a la section "VOTRE STRATEGIE ICI" (cherchez "maStrategie")
--    C'est la SEULE fonction que vous devez modifier.
--    Tout le reste (indicateurs, visuels, metriques) est deja fait.
--
-- 3. INDICATEURS DISPONIBLES:
--    Tous ces indicateurs sont DEJA calcules pour chaque bougie.
--    Vous n'avez qu'a les utiliser dans maStrategie().
--
--    | Variable          | Description                        | Exemple d'utilisation           |
--    |-------------------|------------------------------------|---------------------------------|
--    | ema_20            | EMA 20 periodes (rapide)           | if price > ema_20 then          |
--    | ema_50            | EMA 50 periodes (moyen)            | if ema_50 > ema_200 then        |
--    | ema_200           | EMA 200 periodes (lent)            | if price < ema_200 then         |
--    | rsi               | RSI 14 periodes (0-100)            | if rsi < 30 then -- survendu    |
--    | atr               | ATR 14 periodes (volatilite)       | stop = price - 1.5 * atr        |
--    | ha_open           | Heikin Ashi Open                   | if ha_close > ha_open then      |
--    | ha_close          | Heikin Ashi Close                  | bougie_verte = ha_close > ha_open|
--    | ha_high           | Heikin Ashi High                   | ha_range = ha_high - ha_low     |
--    | ha_low            | Heikin Ashi Low                    | (range HA)                      |
--    | macd_line         | MACD (EMA12 - EMA26)               | if macd_line > signal then      |
--    | macd_signal       | Signal MACD (EMA9 du MACD)         | croisement = macd > signal      |
--    | macd_hist         | Histogramme MACD                   | if macd_hist > 0 then           |
--    | bb_upper          | Bande de Bollinger haute           | if price > bb_upper then        |
--    | bb_middle         | Bande de Bollinger milieu (SMA20)  | tendance = price > bb_middle    |
--    | bb_lower          | Bande de Bollinger basse           | if price < bb_lower then        |
--    | stoch_k           | Stochastique %K (0-100)            | if stoch_k < 20 then           |
--    | stoch_d           | Stochastique %D (SMA de %K)        | croisement = stoch_k > stoch_d  |
--    | adx               | ADX (force de tendance, 0-100)     | if adx > 25 then -- tendance    |
--    | plus_di           | +DI (pression acheteuse)           | if plus_di > minus_di then      |
--    | minus_di          | -DI (pression vendeuse)            | (tendance haussiere)            |
--    | cci               | CCI 20 periodes                    | if cci < -100 then -- survendu  |
--    | williams_r        | Williams %R (0 a -100)             | if williams_r < -80 then        |
--    | momentum          | Momentum 10 periodes               | if momentum > 0 then            |
--    | roc               | Rate of Change (%)                 | if roc > 2 then -- +2%          |
--    | price             | Prix de cloture actuel             | (le prix)                       |
--    | high              | Plus haut de la bougie             | (le high)                       |
--    | low               | Plus bas de la bougie              | (le low)                        |
--    | open              | Ouverture de la bougie             | (l'open)                        |
--
-- 4. VISUELS DISPONIBLES:
--    Les fleches BUY/SELL et marqueurs sont automatiques.
--    Quand maStrategie() retourne "buy", une fleche verte apparait.
--    Quand maStrategie() retourne "sell", une fleche rouge apparait.
--    Un losange bleu apparait quand vous etes en position.
--
-- 5. METRIQUES:
--    A la fin du graphique, les resultats s'affichent dans l'onglet Messages:
--    Win Rate, Profit Factor, Max Drawdown, Sharpe Ratio, etc.
--
-- =============================================================================


-- #############################################################################
--  VARIABLES GLOBALES (ne pas toucher)
-- #############################################################################

local source = nil;

-- Tableaux internes pour le calcul des indicateurs
local ema_20_arr = {};
local ema_50_arr = {};
local ema_200_arr = {};
local ema_12_arr = {};
local ema_26_arr = {};
local ema_macd_signal_arr = {};
local rsi_arr = {};
local rsi_gain_avg = {};
local rsi_loss_avg = {};
local atr_arr = {};
local tr_arr = {};
local ha_open_arr = {};
local ha_close_arr = {};
local ha_high_arr = {};
local ha_low_arr = {};
local sma_20_arr = {};
local bb_stddev_arr = {};
local stoch_k_arr = {};
local stoch_d_buf = {};
local adx_arr = {};
local plus_di_arr = {};
local minus_di_arr = {};
local tr_adx_arr = {};
local plus_dm_arr = {};
local minus_dm_arr = {};
local smooth_tr_arr = {};
local smooth_plus_dm_arr = {};
local smooth_minus_dm_arr = {};
local dx_arr = {};
local cci_arr = {};
local momentum_arr = {};
local roc_arr = {};
local williams_r_arr = {};
local macd_line_arr = {};
local macd_signal_arr = {};
local macd_hist_arr = {};

-- Etat de la simulation
local in_position = false;
local entry_price = 0;
local entry_bar = 0;
local custom_stop = 0;
local custom_tp = 0;

-- Compteurs
local total_trades = 0;
local wins = 0;
local losses = 0;
local total_win_pct = 0;
local total_loss_pct = 0;
local equity = 100;
local equity_arr = {};
local max_equity = 100;
local max_drawdown = 0;
local consecutive_losses = 0;
local max_consec_losses = 0;
local biggest_win = 0;
local biggest_loss = 0;

-- Visuels
local buy_arrow = nil;
local buy_label = nil;
local sell_arrow = nil;
local sell_label = nil;
local stop_arrow = nil;
local stop_label = nil;
local pos_marker = nil;
local info_text = nil;


-- #############################################################################
--  INIT() — Parametres de l'indicateur
-- #############################################################################

function Init()
    indicator:name("Sandbox Trading — Votre Laboratoire");
    indicator:description(
        "Framework sandbox avec TOUS les indicateurs pre-calcules.\n" ..
        "Modifiez la fonction maStrategie() pour tester vos idees.\n" ..
        "Compatible FXCM Trading Station v01.16+"
    );
    indicator:requiredSource(core.Bar);
    indicator:type(core.Indicator);

    -- === Parametres generaux ===
    indicator.parameters:addInteger("max_bars_in_trade",
        "Duree max d'un trade (bougies)", "", 30, 1, 500);

    indicator.parameters:addBoolean("show_info",
        "Afficher infos sous les bougies", "", false);

    -- === Couleurs ===
    indicator.parameters:addColor("clrBuy",
        "Couleur BUY", "", core.rgb(0, 200, 80));
    indicator.parameters:addColor("clrSellWin",
        "Couleur SELL (profit)", "", core.rgb(0, 150, 255));
    indicator.parameters:addColor("clrSellLoss",
        "Couleur SELL (perte)", "", core.rgb(255, 60, 60));
    indicator.parameters:addColor("clrPosition",
        "Marqueur en position", "", core.rgb(100, 180, 255));
end


-- #############################################################################
--  PREPARE() — Initialisation des visuels
-- #############################################################################

function Prepare(nameOnly)
    source = instance.source;
    local name = profile:id() .. "(" .. source:name() .. ")";
    instance:name(name);
    if nameOnly then return; end

    buy_arrow = instance:createTextOutput("BuyArrow", "BUY",
        "Wingdings", 16, core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);
    buy_label = instance:createTextOutput("BuyText", "BUY Label",
        "Arial", 9, core.H_Center, core.V_Top,
        instance.parameters.clrBuy, -15);

    sell_arrow = instance:createTextOutput("SellArrow", "SELL Win",
        "Wingdings", 16, core.H_Center, core.V_Bottom,
        instance.parameters.clrSellWin, 0);
    sell_label = instance:createTextOutput("SellText", "SELL Label",
        "Arial", 9, core.H_Center, core.V_Bottom,
        instance.parameters.clrSellWin, -15);

    stop_arrow = instance:createTextOutput("StopArrow", "STOP",
        "Wingdings", 16, core.H_Center, core.V_Bottom,
        instance.parameters.clrSellLoss, 0);
    stop_label = instance:createTextOutput("StopText", "STOP Label",
        "Arial", 9, core.H_Center, core.V_Bottom,
        instance.parameters.clrSellLoss, -15);

    pos_marker = instance:createTextOutput("InPos", "In Position",
        "Wingdings", 6, core.H_Center, core.V_Bottom,
        instance.parameters.clrPosition, 0);

    info_text = instance:createTextOutput("Info", "Info",
        "Arial", 7, core.H_Center, core.V_Top,
        core.rgb(160, 160, 160), 0);

    resetState();
end


function resetState()
    in_position = false;
    entry_price = 0;
    entry_bar = 0;
    custom_stop = 0;
    custom_tp = 0;
    total_trades = 0;
    wins = 0;
    losses = 0;
    total_win_pct = 0;
    total_loss_pct = 0;
    equity = 100;
    equity_arr = {};
    max_equity = 100;
    max_drawdown = 0;
    consecutive_losses = 0;
    max_consec_losses = 0;
    biggest_win = 0;
    biggest_loss = 0;
end


-- #############################################################################
-- #############################################################################
-- ##                                                                         ##
-- ##                    CALCUL DE TOUS LES INDICATEURS                       ##
-- ##                                                                         ##
-- ##   Ces fonctions sont appelees automatiquement.                          ##
-- ##   Vous n'avez PAS besoin de les modifier.                               ##
-- ##   Lisez les commentaires pour comprendre chaque indicateur.             ##
-- ##                                                                         ##
-- #############################################################################
-- #############################################################################


-- =============================================================================
-- EMA — Moyenne Mobile Exponentielle
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Une moyenne qui donne plus de poids aux prix recents.
-- Plus reactive qu'une SMA (Simple Moving Average).
--
-- COMMENT L'UTILISER:
-- - Prix > EMA = tendance haussiere
-- - Prix < EMA = tendance baissiere
-- - EMA rapide > EMA lente = "Golden Cross" = signal haussier
-- - EMA rapide < EMA lente = "Death Cross" = signal baissier
--
-- PERIODES CLASSIQUES:
-- - EMA 20: tres court terme (scalping, day trading)
-- - EMA 50: moyen terme (swing trading)
-- - EMA 200: long terme (investissement, tendance de fond)
--
-- FORMULE: EMA = Prix * k + EMA_precedent * (1 - k), ou k = 2 / (periode + 1)
--
function calcEMA(period, price_val, arr, ema_period)
    if period < ema_period then
        arr[period] = price_val;
        return price_val;
    end
    if arr[period - 1] == nil then
        local sum = 0;
        for i = period - ema_period + 1, period do
            sum = sum + source.close[i];
        end
        arr[period] = sum / ema_period;
        return arr[period];
    end
    local k = 2.0 / (ema_period + 1);
    arr[period] = price_val * k + arr[period - 1] * (1 - k);
    return arr[period];
end


-- =============================================================================
-- SMA — Moyenne Mobile Simple
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- La moyenne arithmetique des N derniers prix de cloture.
-- Chaque prix a le meme poids.
--
-- COMMENT L'UTILISER:
-- - Comme support/resistance dynamique
-- - Pour les Bandes de Bollinger (SMA 20 = bande du milieu)
-- - Pour comparer avec l'EMA (SMA plus lisse, EMA plus reactive)
--
-- FORMULE: SMA = (prix_1 + prix_2 + ... + prix_N) / N
--
function calcSMA(period, sma_period)
    if period < sma_period - 1 then
        sma_20_arr[period] = source.close[period];
        return source.close[period];
    end
    local sum = 0;
    for i = period - sma_period + 1, period do
        sum = sum + source.close[i];
    end
    sma_20_arr[period] = sum / sma_period;
    return sma_20_arr[period];
end


-- =============================================================================
-- RSI — Relative Strength Index
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Oscillateur entre 0 et 100 qui mesure la force du mouvement.
-- Cree par J. Welles Wilder en 1978.
--
-- COMMENT L'UTILISER:
-- - RSI < 30 = SURVENDU = le prix a trop baisse = potentiel de rebond
-- - RSI > 70 = SURACHAT = le prix a trop monte = potentiel de correction
-- - RSI < 45 en tendance haussiere = bon point d'entree (repli)
-- - RSI > 55 en tendance baissiere = bon point pour shorter
--
-- DIVERGENCE:
-- - Prix fait un nouveau haut MAIS RSI fait un haut plus bas = FAIBLESSE
-- - Prix fait un nouveau bas MAIS RSI fait un bas plus haut = FORCE
--
-- FORMULE: RSI = 100 - (100 / (1 + RS)), RS = Gains moyens / Pertes moyennes
--
function calcRSI(period, rsi_period)
    if period < 2 then
        rsi_arr[period] = 50;
        rsi_gain_avg[period] = 0;
        rsi_loss_avg[period] = 0;
        return 50;
    end
    local change = source.close[period] - source.close[period - 1];
    local current_gain = 0;
    local current_loss = 0;
    if change > 0 then
        current_gain = change;
    else
        current_loss = math.abs(change);
    end
    if period < rsi_period + 1 then
        rsi_gain_avg[period] = (rsi_gain_avg[period - 1] or 0) + current_gain;
        rsi_loss_avg[period] = (rsi_loss_avg[period - 1] or 0) + current_loss;
        rsi_arr[period] = 50;
        return 50;
    end
    if period == rsi_period + 1 then
        rsi_gain_avg[period] = ((rsi_gain_avg[period - 1] or 0) + current_gain) / rsi_period;
        rsi_loss_avg[period] = ((rsi_loss_avg[period - 1] or 0) + current_loss) / rsi_period;
    else
        rsi_gain_avg[period] = (rsi_gain_avg[period - 1] * (rsi_period - 1) + current_gain) / rsi_period;
        rsi_loss_avg[period] = (rsi_loss_avg[period - 1] * (rsi_period - 1) + current_loss) / rsi_period;
    end
    if rsi_loss_avg[period] == 0 then
        rsi_arr[period] = 100;
    else
        local rs = rsi_gain_avg[period] / rsi_loss_avg[period];
        rsi_arr[period] = 100 - (100 / (1 + rs));
    end
    return rsi_arr[period];
end


-- =============================================================================
-- ATR — Average True Range
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Mesure la volatilite moyenne sur N periodes.
-- Le "True Range" prend en compte les gaps (ecarts d'ouverture).
--
-- COMMENT L'UTILISER:
-- - Pour definir les Stop Loss: SL = prix - 1.5 * ATR
-- - Pour definir les Take Profit: TP = prix + 1.0 * ATR
-- - Pour filtrer les marches calmes: si ATR < 1% du prix = pas de trade
-- - Pour adapter la taille de position: plus ATR est grand, plus petit le trade
--
-- VALEURS TYPIQUES (BTC/USD Daily):
-- - ATR ~2000-3000$ = volatilite normale
-- - ATR > 5000$ = volatilite elevee
-- - ATR < 1000$ = marche calme
--
-- FORMULE: TR = max(High-Low, |High-Close_prev|, |Low-Close_prev|)
--          ATR = Moyenne lissee de TR sur N periodes
--
function calcATR(period, atr_period)
    if period < 1 then
        tr_arr[period] = 0;
        atr_arr[period] = 0;
        return 0;
    end
    local h = source.high[period];
    local l = source.low[period];
    local pc = source.close[period - 1];
    local tr1 = h - l;
    local tr2 = math.abs(h - pc);
    local tr3 = math.abs(l - pc);
    tr_arr[period] = math.max(tr1, tr2, tr3);
    if period < atr_period + 1 then
        local sum = 0;
        local count = 0;
        for i = 1, period do
            if tr_arr[i] ~= nil then
                sum = sum + tr_arr[i];
                count = count + 1;
            end
        end
        atr_arr[period] = (count > 0) and (sum / count) or tr_arr[period];
    else
        atr_arr[period] = (atr_arr[period - 1] * (atr_period - 1) + tr_arr[period]) / atr_period;
    end
    return atr_arr[period];
end


-- =============================================================================
-- HEIKIN ASHI — Bougies lissees
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Des bougies modifiees qui lissent le bruit du marche.
-- Plus facile de voir la tendance qu'avec les bougies normales.
--
-- COMMENT L'UTILISER:
-- - ha_close > ha_open = bougie HA verte = tendance haussiere
-- - ha_close < ha_open = bougie HA rouge = tendance baissiere
-- - Compter les bougies vertes/rouges consecutives = force de la tendance
-- - Bougie sans meche basse (ha_low == ha_open) = forte tendance haussiere
-- - Bougie sans meche haute (ha_high == ha_open) = forte tendance baissiere
--
-- FORMULE:
-- HA_Close = (O + H + L + C) / 4
-- HA_Open  = (HA_Open_prev + HA_Close_prev) / 2
-- HA_High  = max(H, HA_Open, HA_Close)
-- HA_Low   = min(L, HA_Open, HA_Close)
--
function calcHeikinAshi(period)
    local o = source.open[period];
    local h = source.high[period];
    local l = source.low[period];
    local c = source.close[period];

    local ha_c = (o + h + l + c) / 4;
    local ha_o;
    if period < 1 or ha_open_arr[period - 1] == nil then
        ha_o = (o + c) / 2;
    else
        ha_o = (ha_open_arr[period - 1] + ha_close_arr[period - 1]) / 2;
    end
    local ha_h = math.max(h, ha_o, ha_c);
    local ha_l = math.min(l, ha_o, ha_c);

    ha_open_arr[period] = ha_o;
    ha_close_arr[period] = ha_c;
    ha_high_arr[period] = ha_h;
    ha_low_arr[period] = ha_l;

    return ha_o, ha_c, ha_h, ha_l;
end


-- =============================================================================
-- MACD — Moving Average Convergence Divergence
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Indicateur de tendance et de momentum.
-- Mesure la convergence/divergence entre 2 EMAs.
--
-- COMMENT L'UTILISER:
-- - MACD Line > Signal Line = HAUSSIER (croisement haussier)
-- - MACD Line < Signal Line = BAISSIER (croisement baissier)
-- - Histogramme > 0 = momentum haussier
-- - Histogramme < 0 = momentum baissier
-- - Histogramme qui grossit = momentum qui accelere
-- - Histogramme qui retrecit = momentum qui faiblit
--
-- PARAMETRES CLASSIQUES: EMA 12, EMA 26, Signal EMA 9
--
-- FORMULE:
-- MACD Line = EMA(12) - EMA(26)
-- Signal Line = EMA(9) de la MACD Line
-- Histogramme = MACD Line - Signal Line
--
function calcMACD(period)
    local ema12 = calcEMA(period, source.close[period], ema_12_arr, 12);
    local ema26 = calcEMA(period, source.close[period], ema_26_arr, 26);
    local macd_l = ema12 - ema26;
    macd_line_arr[period] = macd_l;

    -- Signal line = EMA 9 du MACD
    if period < 34 then
        macd_signal_arr[period] = macd_l;
        ema_macd_signal_arr[period] = macd_l;
    else
        if ema_macd_signal_arr[period - 1] == nil then
            ema_macd_signal_arr[period] = macd_l;
        else
            local k = 2.0 / (9 + 1);
            ema_macd_signal_arr[period] = macd_l * k + ema_macd_signal_arr[period - 1] * (1 - k);
        end
        macd_signal_arr[period] = ema_macd_signal_arr[period];
    end

    macd_hist_arr[period] = macd_l - (macd_signal_arr[period] or 0);

    return macd_l, macd_signal_arr[period] or 0, macd_hist_arr[period] or 0;
end


-- =============================================================================
-- BANDES DE BOLLINGER
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- 3 bandes autour du prix basees sur la volatilite (ecart-type).
-- Se contractent quand le marche est calme, s'ecartent quand il bouge.
--
-- COMMENT L'UTILISER:
-- - Prix touche/depasse la bande HAUTE = potentiel de retournement baissier
-- - Prix touche/depasse la bande BASSE = potentiel de retournement haussier
-- - "Bollinger Squeeze" (bandes tres proches) = gros mouvement a venir
-- - Prix au-dessus de la bande du milieu = tendance haussiere
-- - Prix en-dessous de la bande du milieu = tendance baissiere
--
-- PARAMETRES CLASSIQUES: SMA 20, ecart-type x2
--
-- FORMULE:
-- Bande milieu = SMA(20)
-- Bande haute  = SMA(20) + 2 * StdDev(20)
-- Bande basse  = SMA(20) - 2 * StdDev(20)
--
function calcBollinger(period, bb_period, bb_mult)
    local sma = calcSMA(period, bb_period);
    if period < bb_period - 1 then
        return sma, sma, sma;
    end
    local sum_sq = 0;
    for i = period - bb_period + 1, period do
        local diff = source.close[i] - sma;
        sum_sq = sum_sq + diff * diff;
    end
    local stddev = math.sqrt(sum_sq / bb_period);
    local upper = sma + bb_mult * stddev;
    local lower = sma - bb_mult * stddev;
    return upper, sma, lower;
end


-- =============================================================================
-- STOCHASTIQUE
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Oscillateur entre 0 et 100 qui compare le prix actuel au range recent.
-- Mesure ou se situe le prix par rapport a ses extremes.
--
-- COMMENT L'UTILISER:
-- - %K < 20 = SURVENDU = potentiel de rebond
-- - %K > 80 = SURACHAT = potentiel de correction
-- - %K croise %D vers le haut EN zone survendu = signal ACHAT
-- - %K croise %D vers le bas EN zone surachat = signal VENTE
-- - En tendance forte, le stochastique peut rester en zone extreme longtemps
--
-- PARAMETRES CLASSIQUES: %K = 14, %D = 3 (SMA de %K)
--
-- FORMULE:
-- %K = (Close - LowestLow(14)) / (HighestHigh(14) - LowestLow(14)) * 100
-- %D = SMA(3) de %K
--
function calcStochastic(period, stoch_period, smooth_period)
    if period < stoch_period then
        stoch_k_arr[period] = 50;
        stoch_d_buf[period] = 50;
        return 50, 50;
    end
    local highest = source.high[period];
    local lowest = source.low[period];
    for i = period - stoch_period + 1, period do
        if source.high[i] > highest then highest = source.high[i]; end
        if source.low[i] < lowest then lowest = source.low[i]; end
    end
    local range = highest - lowest;
    local k;
    if range == 0 then
        k = 50;
    else
        k = ((source.close[period] - lowest) / range) * 100;
    end
    stoch_k_arr[period] = k;

    -- %D = SMA de %K
    if period < stoch_period + smooth_period - 1 then
        stoch_d_buf[period] = k;
        return k, k;
    end
    local sum = 0;
    for i = period - smooth_period + 1, period do
        sum = sum + (stoch_k_arr[i] or 50);
    end
    local d = sum / smooth_period;
    stoch_d_buf[period] = d;
    return k, d;
end


-- =============================================================================
-- ADX — Average Directional Index
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Mesure la FORCE de la tendance (pas sa direction).
-- +DI et -DI mesurent la direction.
--
-- COMMENT L'UTILISER:
-- - ADX > 25 = tendance FORTE (utilisez des strategies de tendance)
-- - ADX < 20 = PAS de tendance (utilisez des strategies de range)
-- - ADX > 40 = tendance TRES forte
-- - +DI > -DI = tendance HAUSSIERE
-- - -DI > +DI = tendance BAISSIERE
-- - ADX monte = tendance qui se renforce
-- - ADX descend = tendance qui faiblit
--
-- PARAMETRES CLASSIQUES: 14 periodes
--
function calcADX(period, adx_period)
    if period < 2 then
        adx_arr[period] = 0;
        plus_di_arr[period] = 0;
        minus_di_arr[period] = 0;
        return 0, 0, 0;
    end

    -- Calculer +DM et -DM
    local up_move = source.high[period] - source.high[period - 1];
    local down_move = source.low[period - 1] - source.low[period];
    local plus_dm = 0;
    local minus_dm = 0;
    if up_move > down_move and up_move > 0 then plus_dm = up_move; end
    if down_move > up_move and down_move > 0 then minus_dm = down_move; end
    plus_dm_arr[period] = plus_dm;
    minus_dm_arr[period] = minus_dm;

    -- True Range pour ADX
    local h = source.high[period];
    local l = source.low[period];
    local pc = source.close[period - 1];
    tr_adx_arr[period] = math.max(h - l, math.abs(h - pc), math.abs(l - pc));

    if period < adx_period + 1 then
        adx_arr[period] = 0;
        plus_di_arr[period] = 0;
        minus_di_arr[period] = 0;
        return 0, 0, 0;
    end

    -- Lissage de Wilder
    if period == adx_period + 1 then
        local s_tr = 0; local s_plus = 0; local s_minus = 0;
        for i = period - adx_period + 1, period do
            s_tr = s_tr + (tr_adx_arr[i] or 0);
            s_plus = s_plus + (plus_dm_arr[i] or 0);
            s_minus = s_minus + (minus_dm_arr[i] or 0);
        end
        smooth_tr_arr[period] = s_tr;
        smooth_plus_dm_arr[period] = s_plus;
        smooth_minus_dm_arr[period] = s_minus;
    else
        smooth_tr_arr[period] = (smooth_tr_arr[period - 1] or 0) - ((smooth_tr_arr[period - 1] or 0) / adx_period) + (tr_adx_arr[period] or 0);
        smooth_plus_dm_arr[period] = (smooth_plus_dm_arr[period - 1] or 0) - ((smooth_plus_dm_arr[period - 1] or 0) / adx_period) + plus_dm;
        smooth_minus_dm_arr[period] = (smooth_minus_dm_arr[period - 1] or 0) - ((smooth_minus_dm_arr[period - 1] or 0) / adx_period) + minus_dm;
    end

    local s_tr = smooth_tr_arr[period] or 1;
    if s_tr == 0 then s_tr = 1; end
    local pdi = (smooth_plus_dm_arr[period] / s_tr) * 100;
    local mdi = (smooth_minus_dm_arr[period] / s_tr) * 100;
    plus_di_arr[period] = pdi;
    minus_di_arr[period] = mdi;

    local di_sum = pdi + mdi;
    local dx = 0;
    if di_sum > 0 then dx = (math.abs(pdi - mdi) / di_sum) * 100; end
    dx_arr[period] = dx;

    -- ADX = EMA/SMA lissee du DX
    if period < adx_period * 2 + 1 then
        adx_arr[period] = dx;
        return dx, pdi, mdi;
    end
    adx_arr[period] = ((adx_arr[period - 1] or 0) * (adx_period - 1) + dx) / adx_period;
    return adx_arr[period], pdi, mdi;
end


-- =============================================================================
-- CCI — Commodity Channel Index
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Oscillateur qui mesure l'ecart du prix par rapport a sa moyenne.
-- Peut aller bien au-dela de +/-100.
--
-- COMMENT L'UTILISER:
-- - CCI > +100 = surachat / tendance forte haussiere
-- - CCI < -100 = survendu / tendance forte baissiere
-- - CCI croise +100 vers le haut = debut de tendance haussiere
-- - CCI croise -100 vers le bas = debut de tendance baissiere
-- - CCI entre -100 et +100 = marche sans direction
--
-- FORMULE:
-- Typical Price = (H + L + C) / 3
-- CCI = (TP - SMA(TP, 20)) / (0.015 * Mean Deviation)
--
function calcCCI(period, cci_period)
    if period < cci_period then
        cci_arr[period] = 0;
        return 0;
    end
    local tp = (source.high[period] + source.low[period] + source.close[period]) / 3;
    local tp_sum = 0;
    for i = period - cci_period + 1, period do
        tp_sum = tp_sum + (source.high[i] + source.low[i] + source.close[i]) / 3;
    end
    local tp_avg = tp_sum / cci_period;
    local md_sum = 0;
    for i = period - cci_period + 1, period do
        local t = (source.high[i] + source.low[i] + source.close[i]) / 3;
        md_sum = md_sum + math.abs(t - tp_avg);
    end
    local mean_dev = md_sum / cci_period;
    if mean_dev == 0 then
        cci_arr[period] = 0;
        return 0;
    end
    cci_arr[period] = (tp - tp_avg) / (0.015 * mean_dev);
    return cci_arr[period];
end


-- =============================================================================
-- WILLIAMS %R
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Oscillateur entre 0 et -100 (attention, echelle inversee).
-- Similaire au Stochastique mais inverse.
--
-- COMMENT L'UTILISER:
-- - %R > -20 = SURACHAT = potentiel de correction
-- - %R < -80 = SURVENDU = potentiel de rebond
-- - Utiliser en combinaison avec d'autres indicateurs
--
-- FORMULE: %R = (HighestHigh - Close) / (HighestHigh - LowestLow) * -100
--
function calcWilliamsR(period, wr_period)
    if period < wr_period then
        williams_r_arr[period] = -50;
        return -50;
    end
    local highest = source.high[period];
    local lowest = source.low[period];
    for i = period - wr_period + 1, period do
        if source.high[i] > highest then highest = source.high[i]; end
        if source.low[i] < lowest then lowest = source.low[i]; end
    end
    local range = highest - lowest;
    if range == 0 then
        williams_r_arr[period] = -50;
        return -50;
    end
    williams_r_arr[period] = ((highest - source.close[period]) / range) * -100;
    return williams_r_arr[period];
end


-- =============================================================================
-- MOMENTUM & RATE OF CHANGE (ROC)
-- =============================================================================
--
-- QU'EST-CE QUE C'EST?
-- Mesure la vitesse du changement de prix.
-- Momentum = difference de prix. ROC = difference en pourcentage.
--
-- COMMENT L'UTILISER:
-- - Momentum > 0 = prix en hausse par rapport a N periodes
-- - Momentum < 0 = prix en baisse par rapport a N periodes
-- - ROC > 0 = hausse en % par rapport a N periodes
-- - ROC > 5% = forte hausse recente
-- - ROC < -5% = forte baisse recente
-- - Croisement de zero = changement de direction
--
-- FORMULE:
-- Momentum = Close - Close[N periodes avant]
-- ROC = ((Close - Close[N]) / Close[N]) * 100
--
function calcMomentumROC(period, mom_period)
    if period < mom_period then
        momentum_arr[period] = 0;
        roc_arr[period] = 0;
        return 0, 0;
    end
    local prev_close = source.close[period - mom_period];
    momentum_arr[period] = source.close[period] - prev_close;
    if prev_close ~= 0 then
        roc_arr[period] = ((source.close[period] - prev_close) / prev_close) * 100;
    else
        roc_arr[period] = 0;
    end
    return momentum_arr[period], roc_arr[period];
end


-- #############################################################################
-- #############################################################################
-- ##                                                                         ##
-- ##   >>> VOTRE STRATEGIE ICI <<<                                           ##
-- ##                                                                         ##
-- ##   C'est la SEULE fonction que vous devez modifier.                       ##
-- ##   Tous les indicateurs sont deja calcules et disponibles.               ##
-- ##                                                                         ##
-- ##   RETOURNEZ:                                                            ##
-- ##     "buy"  = ouvrir une position                                        ##
-- ##     "sell" = fermer la position                                         ##
-- ##     "none" = ne rien faire                                              ##
-- ##                                                                         ##
-- ##   Vous pouvez aussi definir custom_stop et custom_tp                    ##
-- ##   pour votre propre Stop Loss et Take Profit.                           ##
-- ##                                                                         ##
-- #############################################################################
-- #############################################################################

function maStrategie(period, price, open, high, low,
                     ema_20, ema_50, ema_200,
                     rsi,
                     atr,
                     ha_open, ha_close, ha_high, ha_low,
                     macd_line, macd_signal, macd_hist,
                     bb_upper, bb_middle, bb_lower,
                     stoch_k, stoch_d,
                     adx, plus_di, minus_di,
                     cci,
                     williams_r,
                     momentum, roc)

    -- =================================================================
    -- EXEMPLE 1: Strategie simple EMA + RSI (ACTIVE par defaut)
    -- Decommentez/commentez les exemples pour tester
    -- =================================================================

    -- CONDITION D'ACHAT:
    -- - Tendance haussiere (EMA 50 > EMA 200)
    -- - RSI en repli (< 45)
    -- - Prix pres de l'EMA 50
    if not in_position then
        if ema_50 > ema_200
           and rsi < 45
           and math.abs((price - ema_50) / ema_50) < 0.03
           and atr > 0 and (atr / price) * 100 > 1.5
        then
            -- Definir votre Stop Loss et Take Profit
            custom_stop = price - 1.5 * atr;  -- SL = 1.5x ATR en dessous
            custom_tp   = price + 2.0 * atr;  -- TP = 2.0x ATR au dessus
            return "buy";
        end
    end

    -- CONDITION DE VENTE:
    if in_position then
        -- Stop Loss touche
        if low <= custom_stop then
            return "sell";
        end
        -- Take Profit touche
        if high >= custom_tp then
            return "sell";
        end
        -- Duree max depassee
        if (period - entry_bar) >= instance.parameters.max_bars_in_trade then
            return "sell";
        end
    end

    return "none";


    -- =================================================================
    -- EXEMPLE 2: Strategie MACD croisement (INACTIF — decommentez)
    -- =================================================================
    --[[
    if not in_position then
        -- Acheter quand MACD croise au-dessus du signal
        if macd_line > macd_signal
           and macd_hist > 0
           and ema_50 > ema_200
        then
            custom_stop = price - 2.0 * atr;
            custom_tp   = price + 3.0 * atr;
            return "buy";
        end
    end

    if in_position then
        if low <= custom_stop then return "sell"; end
        if high >= custom_tp then return "sell"; end
        -- Sortie sur croisement MACD baissier
        if macd_line < macd_signal and macd_hist < 0 then
            return "sell";
        end
    end

    return "none";
    --]]


    -- =================================================================
    -- EXEMPLE 3: Strategie Bollinger Bounce (INACTIF — decommentez)
    -- =================================================================
    --[[
    if not in_position then
        -- Acheter quand le prix touche la bande basse
        if price <= bb_lower
           and rsi < 35
        then
            custom_stop = bb_lower - 1.0 * atr;
            custom_tp   = bb_middle;  -- TP = retour au milieu
            return "buy";
        end
    end

    if in_position then
        if low <= custom_stop then return "sell"; end
        if high >= custom_tp then return "sell"; end
        if price >= bb_upper then return "sell"; end  -- Sortie sur bande haute
    end

    return "none";
    --]]


    -- =================================================================
    -- EXEMPLE 4: Strategie Heikin Ashi Streak (INACTIF — decommentez)
    -- =================================================================
    --[[
    -- Compter les bougies HA vertes consecutives
    local green_count = 0;
    local p = period;
    while p >= 1 and (ha_close_arr[p] or 0) > (ha_open_arr[p] or 0) do
        green_count = green_count + 1;
        p = p - 1;
    end

    if not in_position then
        -- Acheter apres 5 bougies HA vertes
        if green_count >= 5 and ema_50 > ema_200 then
            custom_stop = price - 1.5 * atr;
            custom_tp   = price + 2.0 * atr;
            return "buy";
        end
    end

    if in_position then
        if low <= custom_stop then return "sell"; end
        if high >= custom_tp then return "sell"; end
        -- Compter les rouges
        local red_count = 0;
        local r = period;
        while r >= 1 and (ha_close_arr[r] or 0) < (ha_open_arr[r] or 0) do
            red_count = red_count + 1;
            r = r - 1;
        end
        if red_count >= 3 then return "sell"; end
    end

    return "none";
    --]]


    -- =================================================================
    -- EXEMPLE 5: Strategie ADX + Stochastique (INACTIF — decommentez)
    -- =================================================================
    --[[
    if not in_position then
        -- Acheter en tendance forte + stochastique survendu
        if adx > 25
           and plus_di > minus_di
           and stoch_k < 25
           and stoch_k > stoch_d
        then
            custom_stop = price - 2.0 * atr;
            custom_tp   = price + 3.0 * atr;
            return "buy";
        end
    end

    if in_position then
        if low <= custom_stop then return "sell"; end
        if high >= custom_tp then return "sell"; end
        -- Sortir quand le stochastique est surachat
        if stoch_k > 80 and stoch_k < stoch_d then
            return "sell";
        end
    end

    return "none";
    --]]


    -- =================================================================
    -- VOTRE STRATEGIE PERSONNALISEE (INACTIF — decommentez et codez!)
    -- =================================================================
    --[[

    -- ENTREE:
    if not in_position then
        -- Ecrivez vos conditions d'achat ici
        -- Utilisez n'importe quelle combinaison des indicateurs:
        --   ema_20, ema_50, ema_200
        --   rsi
        --   atr
        --   ha_open, ha_close, ha_high, ha_low
        --   macd_line, macd_signal, macd_hist
        --   bb_upper, bb_middle, bb_lower
        --   stoch_k, stoch_d
        --   adx, plus_di, minus_di
        --   cci
        --   williams_r
        --   momentum, roc
        --   price, open, high, low

        if true then  -- <== REMPLACEZ "true" PAR VOS CONDITIONS
            custom_stop = price - 1.5 * atr;
            custom_tp   = price + 2.0 * atr;
            return "buy";
        end
    end

    -- SORTIE:
    if in_position then
        if low <= custom_stop then return "sell"; end
        if high >= custom_tp then return "sell"; end

        -- Ajoutez des conditions de sortie supplementaires ici
        -- Exemple: sortie sur RSI surachat
        -- if rsi > 75 then return "sell"; end
    end

    return "none";
    --]]
end


-- #############################################################################
--  SIMULATION DES TRADES (ne pas toucher)
-- #############################################################################

function closeTrade(period)
    local exit_price = source.close[period];
    -- Verifier si c'est le stop ou le TP qui a ete touche
    if source.low[period] <= custom_stop then
        exit_price = custom_stop;
    elseif source.high[period] >= custom_tp then
        exit_price = custom_tp;
    end

    local pnl = ((exit_price - entry_price) / entry_price) * 100;

    total_trades = total_trades + 1;
    if pnl > 0 then
        wins = wins + 1;
        total_win_pct = total_win_pct + pnl;
        consecutive_losses = 0;
        if pnl > biggest_win then biggest_win = pnl; end
    else
        losses = losses + 1;
        total_loss_pct = total_loss_pct + math.abs(pnl);
        consecutive_losses = consecutive_losses + 1;
        if consecutive_losses > max_consec_losses then
            max_consec_losses = consecutive_losses;
        end
        if math.abs(pnl) > biggest_loss then biggest_loss = math.abs(pnl); end
    end

    equity = equity * (1 + pnl / 100);
    table.insert(equity_arr, equity);
    if equity > max_equity then max_equity = equity; end
    local current_dd = ((max_equity - equity) / max_equity) * 100;
    if current_dd > max_drawdown then max_drawdown = current_dd; end

    in_position = false;
    entry_price = 0;
    entry_bar = 0;

    return pnl;
end


-- #############################################################################
--  METRIQUES DE PERFORMANCE (ne pas toucher)
-- #############################################################################

function printMetrics()
    if total_trades == 0 then
        core.host:trace("=== SANDBOX: AUCUN TRADE ===");
        core.host:trace("Modifiez la fonction maStrategie() pour generer des signaux.");
        return;
    end

    local win_rate = (wins / total_trades) * 100;
    local avg_win = 0;
    local avg_loss = 0;
    if wins > 0 then avg_win = total_win_pct / wins; end
    if losses > 0 then avg_loss = total_loss_pct / losses; end
    local rr_ratio = 0;
    if avg_loss > 0 then rr_ratio = avg_win / avg_loss; end
    local profit_factor = 0;
    if total_loss_pct > 0 then
        profit_factor = total_win_pct / total_loss_pct;
    else
        profit_factor = 999;
    end

    local sharpe = 0;
    if #equity_arr >= 2 then
        local returns = {};
        for i = 2, #equity_arr do
            table.insert(returns, (equity_arr[i] - equity_arr[i-1]) / equity_arr[i-1]);
        end
        local mean = 0;
        for _, r in ipairs(returns) do mean = mean + r; end
        mean = mean / #returns;
        local var = 0;
        for _, r in ipairs(returns) do var = var + (r - mean)^2; end
        var = var / #returns;
        local stddev = math.sqrt(var);
        if stddev > 0 then sharpe = (mean / stddev) * math.sqrt(252); end
    end

    local total_return = equity - 100;

    core.host:trace("================================================================");
    core.host:trace("   RESULTATS SANDBOX — Votre Strategie");
    core.host:trace("================================================================");
    core.host:trace("   Trades totaux:            " .. total_trades);
    core.host:trace("   Victoires:                " .. wins);
    core.host:trace("   Defaites:                 " .. losses);
    core.host:trace("   TAUX DE VICTOIRE:         " .. string.format("%.1f", win_rate) .. "%");
    core.host:trace("----------------------------------------------------------------");
    core.host:trace("   Gain moyen:               +" .. string.format("%.2f", avg_win) .. "%");
    core.host:trace("   Perte moyenne:            -" .. string.format("%.2f", avg_loss) .. "%");
    core.host:trace("   PLUS GROS GAIN:           +" .. string.format("%.2f", biggest_win) .. "%");
    core.host:trace("   Plus grosse perte:        -" .. string.format("%.2f", biggest_loss) .. "%");
    core.host:trace("   Ratio Risk/Reward:        " .. string.format("%.2f", rr_ratio));
    core.host:trace("----------------------------------------------------------------");
    core.host:trace("   RENDEMENT TOTAL:          " .. string.format("%.1f", total_return) .. "%");
    core.host:trace("   Profit Factor:            " .. string.format("%.2f", profit_factor));
    core.host:trace("   Max Drawdown:             -" .. string.format("%.1f", max_drawdown) .. "%");
    core.host:trace("   Sharpe Ratio:             " .. string.format("%.2f", sharpe));
    core.host:trace("   Pertes consec. max:       " .. max_consec_losses);
    core.host:trace("================================================================");
end


-- #############################################################################
--  UPDATE() — Boucle principale (ne pas toucher)
-- #############################################################################

function Update(period, mode)
    if period < 201 then return; end

    -- ==================================================================
    -- ETAPE 1: Calculer TOUS les indicateurs
    -- ==================================================================
    local price = source.close[period];
    local open_p = source.open[period];
    local high_p = source.high[period];
    local low_p = source.low[period];

    -- EMAs
    local ema_20 = calcEMA(period, price, ema_20_arr, 20);
    local ema_50 = calcEMA(period, price, ema_50_arr, 50);
    local ema_200 = calcEMA(period, price, ema_200_arr, 200);

    -- RSI
    local rsi = calcRSI(period, 14);

    -- ATR
    local atr = calcATR(period, 14);

    -- Heikin Ashi
    local ha_open, ha_close, ha_high, ha_low = calcHeikinAshi(period);

    -- MACD
    local macd_line, macd_signal, macd_hist = calcMACD(period);

    -- Bollinger
    local bb_upper, bb_middle, bb_lower = calcBollinger(period, 20, 2.0);

    -- Stochastique
    local stoch_k, stoch_d = calcStochastic(period, 14, 3);

    -- ADX
    local adx, plus_di, minus_di = calcADX(period, 14);

    -- CCI
    local cci = calcCCI(period, 20);

    -- Williams %R
    local williams_r = calcWilliamsR(period, 14);

    -- Momentum & ROC
    local momentum, roc = calcMomentumROC(period, 10);


    -- ==================================================================
    -- ETAPE 2: Info sous les bougies (optionnel)
    -- ==================================================================
    if instance.parameters.show_info then
        local txt = "R:" .. string.format("%.0f", rsi)
            .. " M:" .. string.format("%.0f", macd_hist);
        if in_position then txt = txt .. " [IN]"; end
        info_text:set(period, low_p, txt, core.rgb(160, 160, 160));
    end


    -- ==================================================================
    -- ETAPE 3: Appeler VOTRE strategie
    -- ==================================================================
    local signal = maStrategie(
        period, price, open_p, high_p, low_p,
        ema_20, ema_50, ema_200,
        rsi,
        atr,
        ha_open, ha_close, ha_high, ha_low,
        macd_line, macd_signal, macd_hist,
        bb_upper, bb_middle, bb_lower,
        stoch_k, stoch_d,
        adx, plus_di, minus_di,
        cci,
        williams_r,
        momentum, roc
    );


    -- ==================================================================
    -- ETAPE 4: Gerer les sorties
    -- ==================================================================
    if in_position and signal == "sell" then
        local pnl = closeTrade(period);
        if pnl >= 0 then
            sell_arrow:set(period, high_p, "\234");
            sell_label:set(period, high_p,
                "+" .. string.format("%.1f", pnl) .. "%");
        else
            stop_arrow:set(period, high_p, "\234");
            stop_label:set(period, high_p,
                string.format("%.1f", pnl) .. "%");
        end
    end

    -- ==================================================================
    -- ETAPE 5: Gerer les entrees
    -- ==================================================================
    if not in_position and signal == "buy" then
        in_position = true;
        entry_price = price;
        entry_bar = period;
        buy_arrow:set(period, low_p, "\233");
        buy_label:set(period, low_p, "BUY");
    end

    -- ==================================================================
    -- ETAPE 6: Marqueur de position
    -- ==================================================================
    if in_position then
        pos_marker:set(period, high_p, "\108");
    end

    -- ==================================================================
    -- ETAPE 7: Metriques sur la derniere bougie
    -- ==================================================================
    if period == source:size() - 1 then
        printMetrics();
    end
end
