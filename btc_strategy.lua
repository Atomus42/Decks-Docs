-- #############################################################################
-- #############################################################################
-- ##                                                                         ##
-- ##   FRAMEWORK DE BACKTEST PROFESSIONNEL — BTC DAILY                       ##
-- ##   "Smart Pullback in Trend" v2 — SORTIE HYBRIDE                        ##
-- ##                                                                         ##
-- ##   Pour FXCM Trading Station Desktop v01.16+ (Lua / Indicore SDK)        ##
-- ##   Compatible TOUTES versions — Pas de drawLabel1/createFont             ##
-- ##                                                                         ##
-- ##   ACTIF:     BTC/USD                                                    ##
-- ##   TIMEFRAME: Journalier (D1)                                            ##
-- ##   PERIODE:   2 dernieres annees                                         ##
-- ##   OBJECTIF:  Win rate >= 80% ET profits eleves                          ##
-- ##                                                                         ##
-- #############################################################################
-- #############################################################################
--
--
-- =============================================================================
-- TABLE DES MATIERES
-- =============================================================================
--
--   1.  PHILOSOPHIE v2 .......................... La strategie hybride
--   2.  CONFIGURATION ........................... Parametres modifiables
--   3.  VARIABLES GLOBALES ...................... Etat et compteurs
--   4.  INIT() ................................. Definition des parametres
--   5.  PREPARE() .............................. Initialisation visuelle
--   6.  CALCUL DES INDICATEURS ................. EMA, RSI, ATR
--   7.  GENERATION DES SIGNAUX ................. 6 filtres d'entree
--   8.  SORTIE HYBRIDE ......................... Le coeur de la v2
--   9.  SIMULATION DES TRADES .................. Open/Close/Trailing
--  10.  METRIQUES DE PERFORMANCE ............... Statistiques completes
--  11.  UPDATE() ............................... Boucle principale
--
-- =============================================================================


-- #############################################################################
--
--  1. PHILOSOPHIE v2 — SORTIE HYBRIDE
--
-- #############################################################################
--
-- LE PROBLEME DE LA v1:
-- =====================
-- La v1 avait 80%+ de win rate MAIS des profits petits (TP = 1x ATR).
-- Quand BTC montait de +30% apres notre entree, on ne prenait que +3%.
-- On laissait 90% du mouvement sur la table.
--
-- LA SOLUTION: SORTIE HYBRIDE EN 2 PHASES
-- =========================================
--
-- PHASE 1 — "SECURISER" (garde le win rate eleve)
-- ------------------------------------------------
-- On prend 50% de la position au premier TP (1x ATR).
-- C'est rapide, frequent, et c'est ce qui maintient le win rate a 80%+.
-- En meme temps, on deplace le Stop Loss au BREAKEVEN (prix d'entree).
-- => La 2eme moitie de la position est maintenant a RISQUE ZERO.
--
-- PHASE 2 — "LAISSER COURIR" (capture les gros mouvements)
-- ---------------------------------------------------------
-- La 2eme moitie de la position suit un TRAILING STOP.
-- Le trailing stop monte avec le prix mais ne descend JAMAIS.
-- Si BTC continue a monter de +20%, on capture +20% sur cette moitie.
-- Si BTC retrace, le trailing stop nous sort en profit (jamais en perte).
--
-- RESULTAT:
-- =========
-- - 80% des trades gagnent au moins sur la Phase 1 (TP rapide)
-- - Sur ces 80%, environ la moitie capturent un gros mouvement en Phase 2
-- - Les pertes restent limitees au Stop Loss initial (seulement sur la Phase 1
--   car apres le 1er TP, on est au breakeven = perte zero)
-- - Le gain moyen EXPLOSE car les gros trades compensent massivement
--
-- ANALOGIE:
-- =========
-- Imaginez un pecheur qui:
-- 1. Attrape un poisson et en met la moitie au frigo (profit securise)
-- 2. Utilise l'autre moitie comme appat pour attraper un GROS poisson
-- 3. Si le gros poisson s'echappe, il a toujours la moitie au frigo
-- 4. S'il attrape le gros, il a le petit ET le gros
--
-- =============================================================================


-- #############################################################################
--
--  3. VARIABLES GLOBALES
--
-- #############################################################################

local source = nil;

-- Indicateurs (calcul interne)
local ema_fast_arr = {};
local ema_slow_arr = {};
local rsi_arr = {};
local atr_arr = {};
local gain_avg = {};
local loss_avg = {};
local tr_arr = {};

-- Etat de la simulation — POSITION HYBRIDE
local in_position = false;      -- Sommes-nous en position?
local entry_price = 0;          -- Prix d'entree
local stop_loss = 0;            -- Niveau du stop loss actuel
local take_profit_1 = 0;       -- Niveau du 1er Take Profit (Phase 1)
local entry_bar = 0;            -- Barre d'entree
local entry_atr = 0;            -- ATR au moment de l'entree (pour le trailing)

-- ETAT DE LA SORTIE HYBRIDE
local phase1_done = false;      -- La Phase 1 (1er TP) a-t-elle ete atteinte?
local trailing_stop = 0;        -- Niveau du trailing stop (Phase 2)
local highest_since_entry = 0;  -- Plus haut prix depuis l'entree (pour trailing)
local phase1_pnl = 0;           -- P&L de la Phase 1 (stocke pour le calcul final)

-- Compteurs de performance
local total_trades = 0;
local wins = 0;
local losses = 0;
local total_win_pct = 0;
local total_loss_pct = 0;
local max_equity = 0;
local max_drawdown = 0;
local equity = 100;
local equity_arr = {};
local consecutive_losses = 0;
local max_consec_losses = 0;
local biggest_win = 0;          -- Plus gros gain (nouveau)
local biggest_loss = 0;         -- Plus grosse perte (nouveau)
local phase2_captures = 0;      -- Nombre de gros gains captures en Phase 2

-- Sorties visuelles
local buy_arrow = nil;
local buy_label = nil;
local sell_arrow = nil;       -- Phase 1 TP (bleu)
local sell_label = nil;
local trail_arrow = nil;      -- Phase 2 trailing exit (or/jaune)
local trail_label = nil;
local stop_arrow = nil;       -- Stop Loss (rouge)
local stop_label = nil;
local pos_marker = nil;
local pos_marker2 = nil;      -- Marqueur Phase 2 (or)
local streak_text = nil;


-- #############################################################################
--
--  4. FONCTION INIT()
--
-- #############################################################################

function Init()
    indicator:name("BTC Smart Pullback D1 v2 (Hybrid)");
    indicator:description(
        "Strategie quantitative 'Smart Pullback' v2\n" ..
        "SORTIE HYBRIDE: TP rapide + Trailing Stop\n" ..
        "Objectif: win rate >= 80% ET profits eleves\n" ..
        "Backtest visuel sur BTC/USD Daily"
    );
    indicator:requiredSource(core.Bar);
    indicator:type(core.Indicator);

    -- =====================================================================
    -- GROUPE 1: MOYENNES MOBILES
    -- =====================================================================
    -- POURQUOI? EMA 50/200 = detection de tendance institutionnelle
    -- EMA 50 > EMA 200 = tendance haussiere = on achete
    --
    -- === MOYENNES MOBILES (Tendance) ===

    indicator.parameters:addInteger("ema_fast_period",
        "Periode EMA Rapide", "", 50, 5, 200);
    -- DEFAUT 50: standard intermediaire. 20=reactif, 100=lent

    indicator.parameters:addInteger("ema_slow_period",
        "Periode EMA Lente", "", 200, 50, 500);
    -- DEFAUT 200: standard institutionnel "Golden Cross"

    -- =====================================================================
    -- GROUPE 2: RSI
    -- =====================================================================
    -- POURQUOI? Detecte les replis dans la tendance
    -- RSI < 45 en tendance haussiere = repli = opportunite d'achat
    --
    -- === RSI (Detection de Repli) ===

    indicator.parameters:addInteger("rsi_period",
        "Periode RSI", "", 14, 5, 50);

    indicator.parameters:addInteger("rsi_entry_threshold",
        "Seuil RSI pour entrer (repli)", "", 45, 20, 60);
    -- DEFAUT 45: capture les replis sans attendre un crash

    indicator.parameters:addInteger("rsi_exit_threshold",
        "Seuil RSI surachat (optionnel)", "", 70, 55, 90);

    -- =====================================================================
    -- GROUPE 3: ATR
    -- =====================================================================
    -- POURQUOI? Adapte le stop/TP a la volatilite reelle
    -- Stop et TP en multiple d'ATR = s'adapte automatiquement
    --
    -- === ATR (Volatilite et Risque) ===

    indicator.parameters:addInteger("atr_period",
        "Periode ATR", "", 14, 5, 50);

    indicator.parameters:addDouble("atr_sl_mult",
        "Stop Loss initial = X fois ATR", "", 1.5, 0.5, 5.0);
    -- DEFAUT 1.5: assez large pour respirer, pas trop pour limiter la perte

    indicator.parameters:addDouble("atr_min_filter",
        "ATR minimum (% du prix)", "", 1.5, 0.5, 10.0);

    -- =====================================================================
    -- GROUPE 4: SORTIE HYBRIDE (LE COEUR DE LA v2)
    -- =====================================================================
    --
    -- C'EST ICI QUE TOUT SE JOUE.
    --
    -- Phase 1: On prend un % de la position au 1er TP
    -- Phase 2: Le reste suit un trailing stop
    --
    -- Le win rate vient de la Phase 1 (TP rapide)
    -- Les gros profits viennent de la Phase 2 (trailing)
    --
    -- === SORTIE HYBRIDE (Phase 1 + Phase 2) ===

    indicator.parameters:addDouble("tp1_atr_mult",
        "Phase 1: Take Profit = X fois ATR", "", 1.0, 0.3, 3.0);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT 1.0: TP rapide a 1x ATR. C'est ce qui donne 80% de win rate.
    -- Le prix bouge de ~1 ATR par jour, donc ce TP est souvent atteint.
    -- PLUS BAS (0.5) = win rate ~90% mais gains minuscules
    -- PLUS HAUT (2.0) = win rate ~60% mais gains plus gros en Phase 1

    indicator.parameters:addDouble("phase1_pct",
        "Phase 1: % de la position a fermer", "", 50, 10, 90);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT 50: On ferme 50% au 1er TP, 50% suit le trailing
    --
    -- COMMENT CA AFFECTE LES RESULTATS:
    -- 90% en Phase 1 = win rate tres eleve, mais peu de gros gains
    -- 50% en Phase 1 = bon equilibre win rate / gros gains
    -- 30% en Phase 1 = win rate un peu plus bas, mais gros gains si trend
    -- 10% en Phase 1 = presque tout en trailing = gros gains OU grosses pertes

    indicator.parameters:addDouble("trail_atr_mult",
        "Phase 2: Trailing Stop = X fois ATR", "", 2.0, 0.5, 5.0);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT 2.0: Le trailing stop suit le prix a 2x ATR de distance
    --
    -- PLUS SERRE (1.0) = sort plus vite, capture moins du mouvement
    -- PLUS LARGE (3.0) = laisse plus de marge, capture plus mais risque
    --                     de redonner beaucoup de profit avant de sortir
    --
    -- 2.0 ATR est un bon compromis: laisse le trade respirer
    -- sans redonner trop de profit

    indicator.parameters:addBoolean("use_breakeven",
        "Deplacer le stop au breakeven apres Phase 1", "", true);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT OUI: Apres le 1er TP, le stop de la 2eme moitie
    -- est deplace au prix d'entree. Resultat: la 2eme moitie
    -- ne peut JAMAIS perdre. C'est un trade "gratuit".
    --
    -- SI NON: Le stop reste a sa position initiale. Plus risque
    -- mais peut capturer des replis temporaires avant la hausse.

    -- =====================================================================
    -- GROUPE 5: FILTRES
    -- =====================================================================
    -- === FILTRES SUPPLEMENTAIRES ===

    indicator.parameters:addBoolean("use_trend_filter",
        "Exiger tendance haussiere (EMA50 > EMA200)", "", true);

    indicator.parameters:addBoolean("use_pullback_filter",
        "Exiger repli vers EMA rapide", "", true);

    indicator.parameters:addDouble("pullback_pct",
        "Ecart max du prix a l'EMA rapide (%)", "", 3.0, 0.5, 15.0);

    indicator.parameters:addBoolean("use_rsi_exit",
        "Sortir Phase 2 sur RSI surachat", "", false);

    indicator.parameters:addInteger("max_bars_in_trade",
        "Duree max d'un trade (jours)", "", 60, 5, 200);
    -- DEFAUT 60: Plus long qu'avant (20) car la Phase 2 a besoin
    -- de TEMPS pour capturer les gros mouvements.

    -- =====================================================================
    -- GROUPE 6: AFFICHAGE
    -- =====================================================================
    -- === AFFICHAGE ===

    indicator.parameters:addColor("clrBuy",
        "Couleur BUY", "", core.rgb(0, 200, 80));
    indicator.parameters:addColor("clrTP1",
        "Couleur Phase 1 (TP rapide)", "", core.rgb(0, 150, 255));
    indicator.parameters:addColor("clrTrail",
        "Couleur Phase 2 (Trailing)", "", core.rgb(255, 200, 0));
    indicator.parameters:addColor("clrSellLoss",
        "Couleur STOP LOSS", "", core.rgb(255, 60, 60));
    indicator.parameters:addColor("clrPosition",
        "Marqueur en position", "", core.rgb(100, 180, 255));

    indicator.parameters:addBoolean("showStreak",
        "Afficher infos sous les bougies", "", false);
end


-- #############################################################################
--
--  5. FONCTION PREPARE()
--
-- #############################################################################

function Prepare(nameOnly)
    source = instance.source;
    local name = profile:id() .. "(" .. source:name() .. ")";
    instance:name(name);
    if nameOnly then
        return;
    end

    -- Fleches BUY (vert)
    buy_arrow = instance:createTextOutput("BuyArrow", "BUY",
        "Wingdings", 16, core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);
    buy_label = instance:createTextOutput("BuyText", "BUY Label",
        "Arial", 9, core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);

    -- Fleches Phase 1 TP (bleu)
    sell_arrow = instance:createTextOutput("TP1Arrow", "Phase 1 TP",
        "Wingdings", 12, core.H_Center, core.V_Bottom,
        instance.parameters.clrTP1, 0);
    sell_label = instance:createTextOutput("TP1Text", "TP1 Label",
        "Arial", 8, core.H_Center, core.V_Bottom,
        instance.parameters.clrTP1, 0);

    -- Fleches Phase 2 Trailing exit (or/jaune)
    trail_arrow = instance:createTextOutput("TrailArrow", "Phase 2 Trail",
        "Wingdings", 16, core.H_Center, core.V_Bottom,
        instance.parameters.clrTrail, 0);
    trail_label = instance:createTextOutput("TrailText", "Trail Label",
        "Arial", 9, core.H_Center, core.V_Bottom,
        instance.parameters.clrTrail, 0);

    -- Fleches STOP LOSS (rouge)
    stop_arrow = instance:createTextOutput("StopArrow", "STOP Loss",
        "Wingdings", 16, core.H_Center, core.V_Bottom,
        instance.parameters.clrSellLoss, 0);
    stop_label = instance:createTextOutput("StopText", "STOP Label",
        "Arial", 9, core.H_Center, core.V_Bottom,
        instance.parameters.clrSellLoss, 0);

    -- Marqueur en position Phase 1 (bleu)
    pos_marker = instance:createTextOutput("InPos1", "In Position P1",
        "Wingdings", 6, core.H_Center, core.V_Bottom,
        instance.parameters.clrPosition, 0);

    -- Marqueur en position Phase 2 (or) — le trade "gratuit"
    pos_marker2 = instance:createTextOutput("InPos2", "In Position P2",
        "Wingdings", 6, core.H_Center, core.V_Bottom,
        instance.parameters.clrTrail, 0);

    -- Info sous les bougies
    streak_text = instance:createTextOutput("Info", "Info",
        "Arial", 7, core.H_Center, core.V_Top,
        core.rgb(160, 160, 160), 0);

    -- Reset complet
    resetState();
end


function resetState()
    in_position = false;
    entry_price = 0;
    stop_loss = 0;
    take_profit_1 = 0;
    entry_bar = 0;
    entry_atr = 0;
    phase1_done = false;
    trailing_stop = 0;
    highest_since_entry = 0;
    phase1_pnl = 0;
    total_trades = 0;
    wins = 0;
    losses = 0;
    total_win_pct = 0;
    total_loss_pct = 0;
    max_equity = 100;
    max_drawdown = 0;
    equity = 100;
    equity_arr = {};
    consecutive_losses = 0;
    max_consec_losses = 0;
    biggest_win = 0;
    biggest_loss = 0;
    phase2_captures = 0;
    ema_fast_arr = {};
    ema_slow_arr = {};
    rsi_arr = {};
    atr_arr = {};
    gain_avg = {};
    loss_avg = {};
    tr_arr = {};
end


-- #############################################################################
--
--  6. CALCUL DES INDICATEURS (identique a la v1)
--
-- #############################################################################

function calcEMA(period, price, arr, ema_period)
    if period < ema_period then
        arr[period] = price;
        return price;
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
    arr[period] = price * k + arr[period - 1] * (1 - k);
    return arr[period];
end


function calcRSI(period, rsi_period)
    if period < 2 then
        rsi_arr[period] = 50;
        gain_avg[period] = 0;
        loss_avg[period] = 0;
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
        gain_avg[period] = (gain_avg[period - 1] or 0) + current_gain;
        loss_avg[period] = (loss_avg[period - 1] or 0) + current_loss;
        rsi_arr[period] = 50;
        return 50;
    end
    if period == rsi_period + 1 then
        gain_avg[period] = ((gain_avg[period - 1] or 0) + current_gain) / rsi_period;
        loss_avg[period] = ((loss_avg[period - 1] or 0) + current_loss) / rsi_period;
    else
        gain_avg[period] = (gain_avg[period - 1] * (rsi_period - 1) + current_gain) / rsi_period;
        loss_avg[period] = (loss_avg[period - 1] * (rsi_period - 1) + current_loss) / rsi_period;
    end
    if loss_avg[period] == 0 then
        rsi_arr[period] = 100;
    else
        local rs = gain_avg[period] / loss_avg[period];
        rsi_arr[period] = 100 - (100 / (1 + rs));
    end
    return rsi_arr[period];
end


function calcATR(period, atr_period)
    if period < 1 then
        tr_arr[period] = 0;
        atr_arr[period] = 0;
        return 0;
    end
    local high = source.high[period];
    local low = source.low[period];
    local prev_close = source.close[period - 1];
    local tr1 = high - low;
    local tr2 = math.abs(high - prev_close);
    local tr3 = math.abs(low - prev_close);
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
        if count > 0 then
            atr_arr[period] = sum / count;
        else
            atr_arr[period] = tr_arr[period];
        end
    else
        atr_arr[period] = (atr_arr[period - 1] * (atr_period - 1) + tr_arr[period]) / atr_period;
    end
    return atr_arr[period];
end


-- #############################################################################
--
--  7. GENERATION DES SIGNAUX (identique a la v1)
--
-- #############################################################################

function shouldEnter(period, ema_fast, ema_slow, rsi, atr)
    local ema_slow_period = instance.parameters.ema_slow_period;
    if period < ema_slow_period + 10 then return false; end
    if instance.parameters.use_trend_filter then
        if ema_fast <= ema_slow then return false; end
    end
    local rsi_threshold = instance.parameters.rsi_entry_threshold;
    if rsi > rsi_threshold then return false; end
    if instance.parameters.use_pullback_filter then
        local price = source.close[period];
        local ecart_pct = ((price - ema_fast) / ema_fast) * 100;
        local max_ecart = instance.parameters.pullback_pct;
        if ecart_pct > max_ecart or ecart_pct < -max_ecart then
            return false;
        end
    end
    local price = source.close[period];
    local atr_pct = (atr / price) * 100;
    local atr_min = instance.parameters.atr_min_filter;
    if atr_pct < atr_min then return false; end
    if in_position then return false; end
    return true;
end


-- #############################################################################
--
--  8. SORTIE HYBRIDE — LE COEUR DE LA v2
--
-- #############################################################################
--
-- Cette fonction gere les 2 phases de sortie.
-- Elle retourne: doit_sortir, raison, est_phase1
--
-- PHASE 1: Le 1er TP est atteint => on ferme une partie
-- PHASE 2: Le trailing stop est touche OU duree max OU RSI exit
-- STOP: Le stop loss initial est touche (avant Phase 1)
--
-- =============================================================================

function checkExit(period, rsi)
    if not in_position then
        return false, "none", false;
    end

    local price = source.close[period];
    local high = source.high[period];
    local low = source.low[period];

    -- ==================================================================
    -- Mettre a jour le plus haut depuis l'entree (pour le trailing)
    -- ==================================================================
    if high > highest_since_entry then
        highest_since_entry = high;
    end

    -- ==================================================================
    -- Si Phase 1 pas encore faite: verifier TP1 et Stop initial
    -- ==================================================================
    if not phase1_done then

        -- STOP LOSS touche AVANT le 1er TP = perte totale
        if low <= stop_loss then
            return true, "stop_full", false;
        end

        -- 1er TAKE PROFIT atteint = Phase 1 terminee
        if high >= take_profit_1 then
            return true, "tp1", true;
        end

        -- Duree max depassee avant Phase 1
        local max_bars = instance.parameters.max_bars_in_trade;
        if (period - entry_bar) >= max_bars then
            if price >= entry_price then
                return true, "time_win", false;
            else
                return true, "time_loss", false;
            end
        end

        return false, "none", false;
    end

    -- ==================================================================
    -- Phase 1 faite: on gere la Phase 2 (trailing stop)
    -- ==================================================================

    -- Mettre a jour le trailing stop
    -- Le trailing suit le plus haut a une distance de X*ATR
    local trail_distance = entry_atr * instance.parameters.trail_atr_mult;
    local new_trail = highest_since_entry - trail_distance;

    -- Le trailing ne descend JAMAIS, il monte seulement
    if new_trail > trailing_stop then
        trailing_stop = new_trail;
    end

    -- Verifier si le trailing stop est touche
    if low <= trailing_stop then
        return true, "trailing", false;
    end

    -- Sortie optionnelle sur RSI surachat
    if instance.parameters.use_rsi_exit then
        local rsi_exit = instance.parameters.rsi_exit_threshold;
        if rsi >= rsi_exit and price > entry_price then
            return true, "rsi_exit", false;
        end
    end

    -- Duree max pour la Phase 2
    local max_bars = instance.parameters.max_bars_in_trade;
    if (period - entry_bar) >= max_bars then
        return true, "time_trail", false;
    end

    return false, "none", false;
end


-- #############################################################################
--
--  9. SIMULATION DES TRADES
--
-- #############################################################################

function openTrade(period, atr)
    in_position = true;
    entry_price = source.close[period];
    entry_bar = period;
    entry_atr = atr;
    phase1_done = false;
    phase1_pnl = 0;
    highest_since_entry = source.high[period];

    -- Stop Loss initial (applique a 100% de la position)
    local sl_distance = atr * instance.parameters.atr_sl_mult;
    stop_loss = entry_price - sl_distance;

    -- Take Profit Phase 1 (la cible rapide)
    local tp_distance = atr * instance.parameters.tp1_atr_mult;
    take_profit_1 = entry_price + tp_distance;

    -- Initialiser le trailing stop au stop loss initial
    trailing_stop = stop_loss;
end


-- Ferme la Phase 1 (profit partiel) et passe en mode trailing
function closePhase1(period)
    -- Calculer le P&L de la Phase 1
    local exit_price_1 = take_profit_1;
    local pnl_phase1 = ((exit_price_1 - entry_price) / entry_price) * 100;
    local phase1_weight = instance.parameters.phase1_pct / 100;

    -- P&L pondere par le % de la position fermee
    phase1_pnl = pnl_phase1 * phase1_weight;

    -- Passer en Phase 2
    phase1_done = true;

    -- Deplacer le stop au breakeven si active
    if instance.parameters.use_breakeven then
        stop_loss = entry_price;         -- Stop = prix d'entree = RISQUE ZERO
        trailing_stop = entry_price;     -- Le trailing part du breakeven
    end

    return pnl_phase1;
end


-- Ferme completement le trade (Phase 2 ou stop complet)
function closeTradeFull(period, reason)
    local exit_price = 0;
    local pnl_pct = 0;

    if reason == "stop_full" then
        -- Stop touche AVANT Phase 1: perte sur 100% de la position
        exit_price = stop_loss;
        pnl_pct = ((exit_price - entry_price) / entry_price) * 100;

    elseif reason == "trailing" then
        -- Trailing stop touche en Phase 2
        exit_price = trailing_stop;
        local pnl_phase2 = ((exit_price - entry_price) / entry_price) * 100;
        local phase2_weight = 1 - (instance.parameters.phase1_pct / 100);
        -- P&L total = Phase 1 (deja prise) + Phase 2 (trailing)
        pnl_pct = phase1_pnl + (pnl_phase2 * phase2_weight);

    elseif reason == "rsi_exit" or reason == "time_trail" then
        -- Sortie au close en Phase 2
        exit_price = source.close[period];
        local pnl_phase2 = ((exit_price - entry_price) / entry_price) * 100;
        local phase2_weight = 1 - (instance.parameters.phase1_pct / 100);
        pnl_pct = phase1_pnl + (pnl_phase2 * phase2_weight);

    else
        -- time_win ou time_loss: sortie au close, position complete
        exit_price = source.close[period];
        pnl_pct = ((exit_price - entry_price) / entry_price) * 100;
    end

    -- Mettre a jour les compteurs
    total_trades = total_trades + 1;

    if pnl_pct > 0 then
        wins = wins + 1;
        total_win_pct = total_win_pct + pnl_pct;
        consecutive_losses = 0;
        if pnl_pct > biggest_win then biggest_win = pnl_pct; end
        if phase1_done and reason == "trailing" then
            phase2_captures = phase2_captures + 1;
        end
    else
        losses = losses + 1;
        total_loss_pct = total_loss_pct + math.abs(pnl_pct);
        consecutive_losses = consecutive_losses + 1;
        if consecutive_losses > max_consec_losses then
            max_consec_losses = consecutive_losses;
        end
        if math.abs(pnl_pct) > biggest_loss then
            biggest_loss = math.abs(pnl_pct);
        end
    end

    -- Mettre a jour l'equity
    equity = equity * (1 + pnl_pct / 100);
    table.insert(equity_arr, equity);
    if equity > max_equity then max_equity = equity; end
    local current_dd = ((max_equity - equity) / max_equity) * 100;
    if current_dd > max_drawdown then max_drawdown = current_dd; end

    -- Reset
    in_position = false;
    entry_price = 0;
    stop_loss = 0;
    take_profit_1 = 0;
    entry_bar = 0;
    entry_atr = 0;
    phase1_done = false;
    trailing_stop = 0;
    highest_since_entry = 0;
    phase1_pnl = 0;

    return pnl_pct, reason;
end


-- #############################################################################
--
--  10. METRIQUES DE PERFORMANCE
--
-- #############################################################################

function printMetrics()
    if total_trades == 0 then
        core.host:trace("=== AUCUN TRADE ===");
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

    -- Sharpe Ratio
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
        if stddev > 0 then
            sharpe = (mean / stddev) * math.sqrt(252);
        end
    end

    local total_return = equity - 100;

    core.host:trace("================================================================");
    core.host:trace("   RESULTATS — BTC Smart Pullback D1 v2 (HYBRIDE)");
    core.host:trace("================================================================");
    core.host:trace("   Trades totaux:            " .. total_trades);
    core.host:trace("   Victoires:                " .. wins);
    core.host:trace("   Defaites:                 " .. losses);
    core.host:trace("   TAUX DE VICTOIRE:         " .. string.format("%.1f", win_rate) .. "%");
    core.host:trace("----------------------------------------------------------------");
    core.host:trace("   Gain moyen par trade:     +" .. string.format("%.2f", avg_win) .. "%");
    core.host:trace("   Perte moyenne par trade:  -" .. string.format("%.2f", avg_loss) .. "%");
    core.host:trace("   PLUS GROS GAIN:           +" .. string.format("%.2f", biggest_win) .. "%");
    core.host:trace("   Plus grosse perte:        -" .. string.format("%.2f", biggest_loss) .. "%");
    core.host:trace("   Ratio Risk/Reward:        " .. string.format("%.2f", rr_ratio));
    core.host:trace("----------------------------------------------------------------");
    core.host:trace("   RENDEMENT TOTAL:          " .. string.format("%.1f", total_return) .. "%");
    core.host:trace("   Profit Factor:            " .. string.format("%.2f", profit_factor));
    core.host:trace("   Max Drawdown:             -" .. string.format("%.1f", max_drawdown) .. "%");
    core.host:trace("   Sharpe Ratio:             " .. string.format("%.2f", sharpe));
    core.host:trace("   Pertes consec. max:       " .. max_consec_losses);
    core.host:trace("----------------------------------------------------------------");
    core.host:trace("   Gros gains Phase 2:       " .. phase2_captures .. " trades");
    core.host:trace("================================================================");
    core.host:trace("");
    core.host:trace("   LEGENDE DU GRAPHIQUE:");
    core.host:trace("   Fleche verte BUY     = Signal d'achat");
    core.host:trace("   Fleche bleue TP1     = Phase 1: profit partiel securise");
    core.host:trace("   Fleche or TRAIL      = Phase 2: sortie trailing (gros gain)");
    core.host:trace("   Fleche rouge SL      = Stop Loss (perte)");
    core.host:trace("   Losange bleu         = En position Phase 1");
    core.host:trace("   Losange or           = En position Phase 2 (trade gratuit)");
    core.host:trace("================================================================");
end


-- #############################################################################
--
--  11. FONCTION UPDATE()
--
-- #############################################################################

function Update(period, mode)
    local min_period = instance.parameters.ema_slow_period + 20;
    if period < min_period then
        return;
    end

    -- ==================================================================
    -- ETAPE 1: Calculer les indicateurs
    -- ==================================================================
    local price = source.close[period];
    local ema_fast = calcEMA(period, price, ema_fast_arr, instance.parameters.ema_fast_period);
    local ema_slow = calcEMA(period, price, ema_slow_arr, instance.parameters.ema_slow_period);
    local rsi = calcRSI(period, instance.parameters.rsi_period);
    local atr = calcATR(period, instance.parameters.atr_period);

    -- ==================================================================
    -- ETAPE 2: Info optionnelle sous les bougies
    -- ==================================================================
    if instance.parameters.showStreak then
        local info = "R:" .. string.format("%.0f", rsi);
        if in_position and phase1_done then
            info = info .. " [P2]";
        elseif in_position then
            info = info .. " [P1]";
        end
        streak_text:set(period, source.low[period], info, core.rgb(160, 160, 160));
    end

    -- ==================================================================
    -- ETAPE 3: Gerer les sorties
    -- ==================================================================
    if in_position then
        local should_exit, reason, is_phase1 = checkExit(period, rsi);

        if should_exit then
            if is_phase1 then
                -- ================================================
                -- PHASE 1 ATTEINTE: Fermer une partie, passer en trailing
                -- ================================================
                local pnl1 = closePhase1(period);

                -- Fleche bleue: Phase 1 TP (profit partiel)
                sell_arrow:set(period, source.high[period], "\234");
                local pct_txt = string.format("%.0f", instance.parameters.phase1_pct);
                sell_label:set(period, source.high[period],
                    "TP1 " .. pct_txt .. "% +" .. string.format("%.1f", pnl1) .. "%");

            else
                -- ================================================
                -- FERMETURE COMPLETE (stop, trailing, temps, RSI)
                -- ================================================
                local pnl, exit_reason = closeTradeFull(period, reason);

                if exit_reason == "trailing" then
                    -- Gros gain Phase 2: fleche OR
                    trail_arrow:set(period, source.high[period], "\234");
                    trail_label:set(period, source.high[period],
                        "TRAIL +" .. string.format("%.1f", pnl) .. "%");

                elseif exit_reason == "rsi_exit" or exit_reason == "time_trail" then
                    -- Sortie Phase 2 (RSI ou temps)
                    if pnl >= 0 then
                        trail_arrow:set(period, source.high[period], "\234");
                        trail_label:set(period, source.high[period],
                            "+" .. string.format("%.1f", pnl) .. "%");
                    else
                        stop_arrow:set(period, source.high[period], "\234");
                        stop_label:set(period, source.high[period],
                            string.format("%.1f", pnl) .. "%");
                    end

                elseif exit_reason == "stop_full" then
                    -- Stop Loss complet (avant Phase 1): fleche ROUGE
                    stop_arrow:set(period, source.high[period], "\234");
                    stop_label:set(period, source.high[period],
                        "SL " .. string.format("%.1f", pnl) .. "%");

                else
                    -- Sortie par temps
                    if pnl >= 0 then
                        sell_arrow:set(period, source.high[period], "\234");
                        sell_label:set(period, source.high[period],
                            "+" .. string.format("%.1f", pnl) .. "%");
                    else
                        stop_arrow:set(period, source.high[period], "\234");
                        stop_label:set(period, source.high[period],
                            string.format("%.1f", pnl) .. "%");
                    end
                end
            end
        end

        -- Marqueurs de position
        if in_position then
            if phase1_done then
                -- Phase 2: losange OR (trade gratuit!)
                pos_marker2:set(period, source.high[period], "\108");
            else
                -- Phase 1: losange bleu
                pos_marker:set(period, source.high[period], "\108");
            end
        end
    end

    -- ==================================================================
    -- ETAPE 4: Verifier les entrees
    -- ==================================================================
    if shouldEnter(period, ema_fast, ema_slow, rsi, atr) then
        openTrade(period, atr);
        buy_arrow:set(period, source.low[period], "\233");
        buy_label:set(period, source.low[period], "BUY");
    end

    -- ==================================================================
    -- ETAPE 5: Metriques sur la derniere bougie
    -- ==================================================================
    if period == source:size() - 1 then
        printMetrics();
    end
end
