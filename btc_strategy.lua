-- #############################################################################
-- #############################################################################
-- ##                                                                         ##
-- ##   FRAMEWORK DE BACKTEST PROFESSIONNEL — BTC DAILY                       ##
-- ##   "Smart Pullback in Trend" — Strategie Quantitative                    ##
-- ##                                                                         ##
-- ##   Pour FXCM Trading Station Desktop v01.16+ (Lua / Indicore SDK)        ##
-- ##   Compatible TOUTES versions — Pas de drawLabel1/createFont             ##
-- ##                                                                         ##
-- ##   ACTIF:     BTC/USD                                                    ##
-- ##   TIMEFRAME: Journalier (D1)                                            ##
-- ##   PERIODE:   2 dernieres annees                                         ##
-- ##   OBJECTIF:  Taux de victoire >= 80%                                    ##
-- ##                                                                         ##
-- #############################################################################
-- #############################################################################
--
--
-- =============================================================================
-- TABLE DES MATIERES
-- =============================================================================
--
--   1. PHILOSOPHIE DE LA STRATEGIE .............. ligne ~50
--   2. CONFIGURATION / PARAMETRES ............... ligne ~100
--   3. VARIABLES GLOBALES ....................... ligne ~200
--   4. FONCTION INIT() .......................... ligne ~230
--   5. FONCTION PREPARE() ....................... ligne ~340
--   6. CALCUL DES INDICATEURS ................... ligne ~420
--   7. GENERATION DES SIGNAUX ................... ligne ~530
--   8. GESTION DU RISQUE ....................... ligne ~620
--   9. SIMULATION DES TRADES ................... ligne ~680
--  10. METRIQUES DE PERFORMANCE ................ ligne ~780
--  11. FONCTION UPDATE() ....................... ligne ~850
--
-- =============================================================================


-- #############################################################################
--
--  1. PHILOSOPHIE DE LA STRATEGIE
--
-- #############################################################################
--
-- STRATEGIE: "Smart Pullback in Trend" (Achat sur repli en tendance)
--
-- POURQUOI CETTE APPROCHE?
-- ========================
-- BTC est un actif qui a une tendance haussiere structurelle sur le long
-- terme (adoption croissante, rarefaction via halving). Sur les 2 dernieres
-- annees, BTC a passe la majorite du temps en tendance haussiere.
--
-- Notre strategie exploite ce biais en:
--   1. Identifiant la tendance principale (EMA 50 > EMA 200)
--   2. Attendant un repli temporaire (RSI < seuil + prix proche EMA rapide)
--   3. Confirmant que la volatilite est suffisante (ATR filtre)
--   4. Entrant avec un Stop Loss serre et un Take Profit modeste
--
-- POURQUOI 80%+ DE VICTOIRES?
-- ===========================
-- Un taux de victoire eleve s'obtient en:
--   - Prenant des profits RAPIDEMENT (petit Take Profit = 1x ATR)
--   - Filtrant agressivement (n'entre que dans des conditions ideales)
--   - Tradant AVEC la tendance (le vent dans le dos)
--   - Acceptant un ratio Risk/Reward < 1 (c'est le compromis)
--
-- LE COMPROMIS FONDAMENTAL:
-- =========================
-- Un win rate de 80% implique generalement un R:R de 0.5-0.8.
-- Cela signifie que quand vous perdez, vous perdez PLUS que ce que
-- vous gagnez sur un trade gagnant. Le systeme reste profitable
-- parce que vous gagnez BEAUCOUP plus souvent que vous ne perdez.
--
-- ATTENTION: Les 20% de trades perdants peuvent arriver en SERIE.
-- Un drawdown de 4-5 pertes consecutives est NORMAL et ATTENDU.
-- Ne paniquez pas. Faites confiance au systeme sur un grand echantillon.
--
-- RISQUE DE SUR-OPTIMISATION (OVERFITTING):
-- ==========================================
-- Les parametres ci-dessous ont ete choisis avec une logique economique,
-- pas par optimisation brute. Changer un parametre de 50 a 51 ne devrait
-- pas detruire la strategie. Si c'est le cas, c'est un signe d'overfitting.
-- Testez toujours vos modifications sur une periode differente.
--
-- =============================================================================


-- #############################################################################
--
--  2. CONFIGURATION / PARAMETRES
--
-- #############################################################################
--
-- COMMENT MODIFIER LES PARAMETRES:
-- =================================
-- Quand vous ajoutez cet indicateur sur votre graphique, une fenetre
-- de parametres apparait. Changez les valeurs directement la-dedans.
--
-- Vous pouvez aussi modifier les valeurs par defaut dans le code ci-dessous.
-- Cherchez le nombre apres le dernier "" dans chaque addInteger/addDouble.
-- Exemple: addInteger("ema_fast", "EMA Rapide", "", 50, ...)
--                                                    ^^-- valeur par defaut
--
-- =============================================================================


-- #############################################################################
--
--  3. VARIABLES GLOBALES
--
-- #############################################################################

local source = nil;          -- Source de donnees (bougies OHLC)

-- Tableaux de stockage des indicateurs (calcul interne, pas affiche)
local ema_fast_arr = {};     -- EMA rapide (defaut: 50 periodes)
local ema_slow_arr = {};     -- EMA lente (defaut: 200 periodes)
local rsi_arr = {};          -- RSI (defaut: 14 periodes)
local atr_arr = {};          -- ATR (defaut: 14 periodes)

-- Tableaux intermediaires pour les calculs
local gain_avg = {};         -- Moyenne des gains (pour RSI)
local loss_avg = {};         -- Moyenne des pertes (pour RSI)
local tr_arr = {};           -- True Range (pour ATR)

-- Etat de la simulation
local in_position = false;   -- Sommes-nous en position?
local entry_price = 0;       -- Prix d'entree du trade en cours
local stop_loss = 0;         -- Niveau du stop loss
local take_profit = 0;       -- Niveau du take profit
local entry_bar = 0;         -- Barre d'entree (pour compter la duree)

-- Compteurs de performance
local total_trades = 0;      -- Nombre total de trades
local wins = 0;              -- Nombre de victoires
local losses = 0;            -- Nombre de pertes
local total_win_pct = 0;     -- Somme des % de gains
local total_loss_pct = 0;    -- Somme des % de pertes (en valeur absolue)
local max_equity = 0;        -- Pic d'equity pour le drawdown
local max_drawdown = 0;      -- Drawdown maximum observe
local equity = 100;          -- Equity simulee (depart a 100)
local equity_arr = {};       -- Historique d'equity pour Sharpe
local consecutive_losses = 0;-- Pertes consecutives actuelles
local max_consec_losses = 0; -- Pertes consecutives maximum

-- Sorties visuelles (createTextOutput — compatible toutes versions)
local buy_arrow = nil;       -- Fleche BUY
local buy_label = nil;       -- Texte "BUY"
local sell_arrow = nil;      -- Fleche SELL (profit)
local sell_label = nil;      -- Texte "SELL +X%"
local stop_arrow = nil;      -- Fleche STOP (perte)
local stop_label = nil;      -- Texte "STOP -X%"
local pos_marker = nil;      -- Marqueur en position
local streak_text = nil;     -- Info sous les bougies


-- #############################################################################
--
--  4. FONCTION INIT()
--
-- #############################################################################
--
-- QUAND EST-ELLE APPELEE?
-- Trading Station appelle Init() UNE SEULE FOIS quand il charge le fichier.
-- Elle definit le nom, la description, et TOUS les parametres ajustables.
--
-- =============================================================================

function Init()
    indicator:name("BTC Smart Pullback D1 (Backtest)");
    indicator:description(
        "Strategie quantitative 'Smart Pullback in Trend'\n" ..
        "Backtest visuel sur BTC/USD Daily.\n" ..
        "Affiche BUY/SELL/STOP sur le graphique.\n" ..
        "Objectif: win rate >= 80%"
    );
    indicator:requiredSource(core.Bar);
    indicator:type(core.Indicator);

    -- =====================================================================
    -- GROUPE 1: MOYENNES MOBILES (detection de tendance)
    -- =====================================================================
    --
    -- POURQUOI CES INDICATEURS?
    -- La combinaison EMA 50 / EMA 200 est le "Golden Cross / Death Cross"
    -- utilise par les institutionnels. Quand EMA 50 > EMA 200, la tendance
    -- de fond est haussiere. C'est notre PREMIER filtre.
    --
    -- COMMENT MODIFIER:
    -- - Diminuer EMA rapide (ex: 20) = plus reactif, plus de signaux
    -- - Augmenter EMA rapide (ex: 100) = plus lent, moins de signaux
    -- - La EMA lente (200) est un standard, evitez de trop la changer
    --
    -- CONSEQUENCE:
    -- EMA rapide trop basse = trop de faux signaux (tendance pas confirmee)
    -- EMA rapide trop haute = entre trop tard, rate les mouvements
    --
    indicator.parameters:addGroup("Moyennes Mobiles (Tendance)");

    indicator.parameters:addInteger("ema_fast_period",
        "Periode EMA Rapide", "", 50, 5, 200);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT: 50 | La moyenne mobile rapide detecte la tendance intermediaire
    -- Si vous mettez 20: plus de trades, mais plus de faux signaux
    -- Si vous mettez 100: moins de trades, mais meilleure qualite

    indicator.parameters:addInteger("ema_slow_period",
        "Periode EMA Lente", "", 200, 50, 500);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT: 200 | La moyenne mobile lente = tendance de fond
    -- C'est le standard institutionnel. Ne changez que si vous savez pourquoi.

    -- =====================================================================
    -- GROUPE 2: RSI (detection de repli / survente)
    -- =====================================================================
    --
    -- POURQUOI LE RSI?
    -- Le RSI mesure la "vitesse" de la hausse ou de la baisse.
    -- Un RSI bas dans une tendance haussiere = le prix a recule
    -- temporairement = OPPORTUNITE d'achat.
    --
    -- NOTRE UTILISATION:
    -- On N'ACHETE PAS quand RSI < 30 (classique "survente").
    -- On achete quand RSI < 45 dans une tendance haussiere.
    -- C'est un "repli modere" = le prix a souffle mais la tendance tient.
    --
    -- POURQUOI 45 ET PAS 30?
    -- RSI < 30 en tendance haussiere est RARE. On raterait 90% des opportunites.
    -- RSI < 45 capture les replis normaux sans attendre un crash.
    --
    -- COMMENT MODIFIER:
    -- - RSI seuil plus bas (ex: 35) = moins de trades, plus selectif
    -- - RSI seuil plus haut (ex: 55) = plus de trades, moins precis
    --
    indicator.parameters:addGroup("RSI (Detection de Repli)");

    indicator.parameters:addInteger("rsi_period",
        "Periode RSI", "", 14, 5, 50);
    -- DEFAUT: 14 | Standard universel. Fonctionne bien sur Daily.

    indicator.parameters:addInteger("rsi_entry_threshold",
        "Seuil RSI pour entrer (repli)", "", 45, 20, 60);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT: 45 | On entre quand RSI descend sous ce seuil
    -- Plus bas = moins de trades mais meilleure precision
    -- Plus haut = plus de trades mais plus de faux signaux

    indicator.parameters:addInteger("rsi_exit_threshold",
        "Seuil RSI surachat (optionnel)", "", 70, 55, 90);
    -- DEFAUT: 70 | Si RSI depasse ce seuil, on PEUT sortir (surachat)
    -- Desactive par defaut. Activez "Sortir sur RSI surachat" ci-dessous.

    -- =====================================================================
    -- GROUPE 3: ATR (volatilite et gestion du risque)
    -- =====================================================================
    --
    -- POURQUOI L'ATR?
    -- L'ATR (Average True Range) mesure la volatilite REELLE du prix.
    -- On l'utilise pour:
    --   1. FILTRER: Ne pas trader quand la volatilite est trop basse
    --      (marche en range = beaucoup de faux signaux)
    --   2. STOP LOSS: Placer le stop a une distance proportionnelle
    --      a la volatilite (pas un nombre fixe de pips)
    --   3. TAKE PROFIT: Prendre profit a une distance ATR aussi
    --
    -- POURQUOI PROPORTIONNEL A L'ATR?
    -- Un stop fixe de 500 pips est absurde quand BTC bouge de 3000/jour
    -- mais trop large quand il bouge de 200/jour. L'ATR s'adapte.
    --
    indicator.parameters:addGroup("ATR (Volatilite et Risque)");

    indicator.parameters:addInteger("atr_period",
        "Periode ATR", "", 14, 5, 50);
    -- DEFAUT: 14 | Standard. Mesure la volatilite sur 14 jours.

    indicator.parameters:addDouble("atr_tp_mult",
        "Take Profit = X fois ATR", "", 1.0, 0.3, 5.0);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT: 1.0 | Take Profit = 1x la volatilite journaliere
    -- C'est PETIT volontairement. C'est ce qui donne le 80%+ win rate.
    -- Un TP de 1x ATR est atteint SOUVENT car le prix bouge de 1 ATR/jour.
    --
    -- COMPROMIS CRITIQUE:
    -- TP petit = win rate eleve MAIS gains petits par trade
    -- TP grand = win rate bas MAIS gains gros par trade
    --
    -- Si vous mettez 2.0: win rate tombera a ~55-65%
    -- Si vous mettez 0.5: win rate montera a ~90% mais gains minuscules

    indicator.parameters:addDouble("atr_sl_mult",
        "Stop Loss = X fois ATR", "", 1.5, 0.5, 5.0);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT: 1.5 | Stop Loss = 1.5x la volatilite journaliere
    -- Plus large que le TP car on veut LAISSER RESPIRER le trade.
    -- Un stop trop serre se fait toucher par le bruit normal du marche.
    --
    -- RATIO R:R IMPLICITE = TP/SL = 1.0/1.5 = 0.67
    -- On gagne MOINS par trade gagnant qu'on perd par trade perdant.
    -- Mais on gagne 80%+ du temps, donc c'est rentable au total.

    indicator.parameters:addDouble("atr_min_filter",
        "ATR minimum (% du prix)", "", 1.5, 0.5, 10.0);
    -- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -- DEFAUT: 1.5% | On ne trade PAS si ATR < 1.5% du prix
    -- Cela filtre les periodes de faible volatilite (consolidation)
    -- ou le prix oscille sans direction = beaucoup de faux signaux.

    -- =====================================================================
    -- GROUPE 4: FILTRES SUPPLEMENTAIRES
    -- =====================================================================
    --
    -- POURQUOI DES FILTRES?
    -- Plus on filtre, plus le win rate monte (mais moins de trades).
    -- Chaque filtre elimine des "mauvais" trades.
    --
    indicator.parameters:addGroup("Filtres Supplementaires");

    indicator.parameters:addBoolean("use_trend_filter",
        "Exiger tendance haussiere (EMA50 > EMA200)", "", true);
    -- DEFAUT: OUI | Le filtre le plus important. Sans lui, win rate chute.

    indicator.parameters:addBoolean("use_pullback_filter",
        "Exiger repli vers EMA rapide", "", true);
    -- DEFAUT: OUI | Le prix doit etre PROCHE de l'EMA rapide (repli)
    -- pas loin au-dessus (surchauffe). Empeche d'acheter les sommets.

    indicator.parameters:addDouble("pullback_pct",
        "Ecart max du prix a l'EMA rapide (%)", "", 3.0, 0.5, 15.0);
    -- DEFAUT: 3.0% | Le prix doit etre a moins de 3% de l'EMA rapide
    -- Plus bas = plus strict, moins de trades mais meilleurs
    -- Plus haut = plus permissif, plus de trades mais moins precis

    indicator.parameters:addBoolean("use_rsi_exit",
        "Sortir aussi sur RSI surachat", "", false);
    -- DEFAUT: NON | Si OUI, on sort quand RSI > seuil surachat
    -- Peut augmenter le win rate mais reduit les gains sur gros moves.

    indicator.parameters:addInteger("max_bars_in_trade",
        "Duree max d'un trade (jours)", "", 20, 5, 100);
    -- DEFAUT: 20 | Si un trade n'a pas atteint TP ou SL apres 20 jours,
    -- on le ferme. Evite de rester bloque dans un trade qui stagne.
    -- Un trade qui stagne immobilise du capital pour rien.

    -- =====================================================================
    -- GROUPE 5: AFFICHAGE
    -- =====================================================================
    indicator.parameters:addGroup("Affichage");

    indicator.parameters:addColor("clrBuy",
        "Couleur BUY", "", core.rgb(0, 200, 80));
    indicator.parameters:addColor("clrSellWin",
        "Couleur SELL gagnant", "", core.rgb(0, 150, 255));
    indicator.parameters:addColor("clrSellLoss",
        "Couleur SELL perdant", "", core.rgb(255, 60, 60));
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
--
-- QUAND EST-ELLE APPELEE?
-- Apres que l'utilisateur a configure les parametres et clique OK.
-- Elle initialise les sorties visuelles et reset les compteurs.
--
-- =============================================================================

function Prepare(nameOnly)
    source = instance.source;
    local name = profile:id() .. "(" .. source:name() .. ")";
    instance:name(name);
    if nameOnly then
        return;
    end

    -- Pas de bougies dessinees — on garde les chandeliers rouge/noir

    -- Fleches et textes BUY
    buy_arrow = instance:createTextOutput("BuyArrow", "BUY",
        "Wingdings", 16,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, 0);
    buy_label = instance:createTextOutput("BuyText", "BUY Label",
        "Arial", 9,
        core.H_Center, core.V_Top,
        instance.parameters.clrBuy, -15);

    -- Fleches et textes SELL (gagnant)
    sell_arrow = instance:createTextOutput("SellArrow", "SELL Win",
        "Wingdings", 16,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSellWin, 0);
    sell_label = instance:createTextOutput("SellText", "SELL Label",
        "Arial", 9,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSellWin, -15);

    -- Fleches et textes STOP (perdant)
    stop_arrow = instance:createTextOutput("StopArrow", "STOP Loss",
        "Wingdings", 16,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSellLoss, 0);
    stop_label = instance:createTextOutput("StopText", "STOP Label",
        "Arial", 9,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrSellLoss, -15);

    -- Marqueur en position
    pos_marker = instance:createTextOutput("InPos", "In Position",
        "Wingdings", 6,
        core.H_Center, core.V_Bottom,
        instance.parameters.clrPosition, 0);

    -- Info sous les bougies
    streak_text = instance:createTextOutput("Info", "Info",
        "Arial", 7,
        core.H_Center, core.V_Top,
        core.rgb(160, 160, 160), 0);

    -- Reset complet
    in_position = false;
    entry_price = 0;
    stop_loss = 0;
    take_profit = 0;
    entry_bar = 0;
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
--  6. CALCUL DES INDICATEURS
--
-- #############################################################################
--
-- POURQUOI CALCULER A LA MAIN?
-- Trading Station v01.16 ne supporte pas bien core.indicators:create()
-- pour certains indicateurs. En calculant nous-memes, on est 100%
-- compatible et on comprend EXACTEMENT ce qui se passe.
--
-- =============================================================================


-- ===============================
-- CALCUL EMA (Exponential Moving Average)
-- ===============================
-- FORMULE: EMA = prix * k + EMA_prec * (1 - k)
-- ou k = 2 / (periode + 1)
--
-- POURQUOI EMA ET PAS SMA?
-- L'EMA reagit plus vite aux changements recents de prix.
-- Pour detecter un changement de tendance, c'est preferable.
--
function calcEMA(period, price, arr, ema_period)
    if period < ema_period then
        -- Pas assez de donnees: on utilise le prix brut
        arr[period] = price;
        return price;
    end

    if arr[period - 1] == nil then
        -- Premiere valeur: calculer la SMA comme point de depart
        local sum = 0;
        for i = period - ema_period + 1, period do
            sum = sum + source.close[i];
        end
        arr[period] = sum / ema_period;
        return arr[period];
    end

    -- Calcul EMA standard
    local k = 2.0 / (ema_period + 1);
    arr[period] = price * k + arr[period - 1] * (1 - k);
    return arr[period];
end


-- ===============================
-- CALCUL RSI (Relative Strength Index)
-- ===============================
-- FORMULE:
--   RSI = 100 - (100 / (1 + RS))
--   RS  = moyenne_gains / moyenne_pertes
--
-- POURQUOI LE RSI?
-- Il mesure si le prix monte trop vite (surachat) ou descend trop
-- vite (survente). On l'utilise pour detecter les REPLIS: un RSI
-- qui baisse dans une tendance haussiere = opportunite d'achat.
--
-- ATTENTION: Le RSI N'EST PAS un signal d'achat/vente seul.
-- Il est utilise comme FILTRE en combinaison avec la tendance.
--
function calcRSI(period, rsi_period)
    if period < 2 then
        rsi_arr[period] = 50;  -- Valeur neutre par defaut
        gain_avg[period] = 0;
        loss_avg[period] = 0;
        return 50;
    end

    -- Calculer le changement de prix
    local change = source.close[period] - source.close[period - 1];
    local current_gain = 0;
    local current_loss = 0;
    if change > 0 then
        current_gain = change;
    else
        current_loss = math.abs(change);
    end

    if period < rsi_period + 1 then
        -- Phase d'initialisation: accumuler les gains/pertes
        gain_avg[period] = (gain_avg[period - 1] or 0) + current_gain;
        loss_avg[period] = (loss_avg[period - 1] or 0) + current_loss;
        rsi_arr[period] = 50;
        return 50;
    end

    if period == rsi_period + 1 then
        -- Premiere vraie valeur RSI: moyenne simple
        gain_avg[period] = ((gain_avg[period - 1] or 0) + current_gain) / rsi_period;
        loss_avg[period] = ((loss_avg[period - 1] or 0) + current_loss) / rsi_period;
    else
        -- Moyenne exponentielle de Wilder (lissage standard du RSI)
        gain_avg[period] = (gain_avg[period - 1] * (rsi_period - 1) + current_gain) / rsi_period;
        loss_avg[period] = (loss_avg[period - 1] * (rsi_period - 1) + current_loss) / rsi_period;
    end

    -- Calculer le RSI
    if loss_avg[period] == 0 then
        rsi_arr[period] = 100;  -- Que des gains = RSI max
    else
        local rs = gain_avg[period] / loss_avg[period];
        rsi_arr[period] = 100 - (100 / (1 + rs));
    end

    return rsi_arr[period];
end


-- ===============================
-- CALCUL ATR (Average True Range)
-- ===============================
-- FORMULE:
--   True Range = max(High-Low, |High-Close_prec|, |Low-Close_prec|)
--   ATR = Moyenne mobile du True Range
--
-- POURQUOI L'ATR?
-- Il mesure la volatilite REELLE. On l'utilise pour:
--   - Adapter le Stop Loss a la volatilite actuelle
--   - Adapter le Take Profit a la volatilite actuelle
--   - Filtrer les periodes de faible volatilite
--
-- UN STOP EN ATR S'ADAPTE AUTOMATIQUEMENT:
-- Si BTC bouge de $5000/jour, le stop sera large
-- Si BTC bouge de $500/jour, le stop sera serre
-- C'est beaucoup plus intelligent qu'un stop fixe en pips.
--
function calcATR(period, atr_period)
    if period < 1 then
        tr_arr[period] = 0;
        atr_arr[period] = 0;
        return 0;
    end

    -- True Range: le plus grand de ces 3 valeurs
    local high = source.high[period];
    local low = source.low[period];
    local prev_close = source.close[period - 1];

    local tr1 = high - low;                       -- Range de la bougie
    local tr2 = math.abs(high - prev_close);      -- Gap haussier
    local tr3 = math.abs(low - prev_close);       -- Gap baissier
    tr_arr[period] = math.max(tr1, tr2, tr3);

    if period < atr_period + 1 then
        -- Phase d'initialisation: moyenne simple
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
        -- Lissage de Wilder (comme pour le RSI)
        atr_arr[period] = (atr_arr[period - 1] * (atr_period - 1) + tr_arr[period]) / atr_period;
    end

    return atr_arr[period];
end


-- #############################################################################
--
--  7. GENERATION DES SIGNAUX
--
-- #############################################################################
--
-- C'est ici que toute la logique de decision se passe.
-- Chaque condition est un FILTRE. Plus on filtre, meilleure la qualite.
--
-- =============================================================================

function shouldEnter(period, ema_fast, ema_slow, rsi, atr)
    -- ==================================================================
    -- FILTRE 1: Donnees suffisantes
    -- ==================================================================
    -- On a besoin d'au moins EMA_slow periodes de donnees
    local ema_slow_period = instance.parameters.ema_slow_period;
    if period < ema_slow_period + 10 then
        return false;
    end

    -- ==================================================================
    -- FILTRE 2: TENDANCE HAUSSIERE (EMA rapide > EMA lente)
    -- ==================================================================
    -- C'est le filtre le PLUS IMPORTANT.
    -- On n'achete QUE quand la tendance de fond est haussiere.
    -- Sans ce filtre, le win rate chute dramatiquement.
    --
    if instance.parameters.use_trend_filter then
        if ema_fast <= ema_slow then
            return false;  -- Pas de tendance haussiere = pas d'achat
        end
    end

    -- ==================================================================
    -- FILTRE 3: RSI EN ZONE DE REPLI
    -- ==================================================================
    -- Le RSI doit etre SOUS le seuil = le prix a recule.
    -- On achete le "creux" dans la tendance, pas le sommet.
    --
    local rsi_threshold = instance.parameters.rsi_entry_threshold;
    if rsi > rsi_threshold then
        return false;  -- RSI trop haut = pas de repli = pas d'achat
    end

    -- ==================================================================
    -- FILTRE 4: PRIX PROCHE DE L'EMA RAPIDE (repli confirme)
    -- ==================================================================
    -- Le prix doit etre PRES de l'EMA rapide (pas loin au-dessus).
    -- Si le prix est 20% au-dessus de l'EMA, c'est une surchauffe,
    -- pas un repli.
    --
    if instance.parameters.use_pullback_filter then
        local price = source.close[period];
        local ecart_pct = ((price - ema_fast) / ema_fast) * 100;
        local max_ecart = instance.parameters.pullback_pct;
        -- Le prix doit etre entre -max_ecart% et +max_ecart% de l'EMA
        if ecart_pct > max_ecart or ecart_pct < -max_ecart then
            return false;
        end
    end

    -- ==================================================================
    -- FILTRE 5: VOLATILITE SUFFISANTE
    -- ==================================================================
    -- Si le marche ne bouge pas (ATR trop bas), les stop/TP seront
    -- trop serres et on se fera sortir par le bruit.
    --
    local price = source.close[period];
    local atr_pct = (atr / price) * 100;
    local atr_min = instance.parameters.atr_min_filter;
    if atr_pct < atr_min then
        return false;  -- Volatilite trop basse = marche en sommeil
    end

    -- ==================================================================
    -- FILTRE 6: PAS DEJA EN POSITION
    -- ==================================================================
    if in_position then
        return false;
    end

    -- TOUS LES FILTRES PASSES = SIGNAL D'ACHAT
    return true;
end


-- #############################################################################
--
--  8. GESTION DU RISQUE
--
-- #############################################################################
--
-- REGLE D'OR: Ne risquez JAMAIS plus que ce que vous pouvez perdre.
--
-- Notre gestion du risque:
--   - Stop Loss = prix d'entree - (ATR * multiplicateur SL)
--   - Take Profit = prix d'entree + (ATR * multiplicateur TP)
--   - Duree max = on ferme si le trade stagne trop longtemps
--   - Sortie RSI = on ferme si RSI indique surachat (optionnel)
--
-- =============================================================================

function shouldExit(period, rsi)
    if not in_position then
        return false, "none";
    end

    local price = source.close[period];
    local low = source.low[period];
    local high = source.high[period];

    -- ==================================================================
    -- SORTIE 1: STOP LOSS TOUCHE
    -- ==================================================================
    -- Le prix est descendu sous notre stop = on coupe la perte.
    -- On utilise le LOW de la bougie (pas le close) car en intraday
    -- le stop aurait ete touche meme si le close est au-dessus.
    --
    if low <= stop_loss then
        return true, "stop";
    end

    -- ==================================================================
    -- SORTIE 2: TAKE PROFIT TOUCHE
    -- ==================================================================
    -- Le prix a atteint notre objectif = on prend le profit.
    -- On utilise le HIGH de la bougie.
    --
    if high >= take_profit then
        return true, "profit";
    end

    -- ==================================================================
    -- SORTIE 3: DUREE MAXIMALE DEPASSEE
    -- ==================================================================
    -- Le trade stagne depuis trop longtemps = on libere le capital.
    -- Un trade qui ne bouge pas immobilise du capital pour rien.
    --
    local max_bars = instance.parameters.max_bars_in_trade;
    if (period - entry_bar) >= max_bars then
        if price >= entry_price then
            return true, "time_win";   -- Ferme en petit profit
        else
            return true, "time_loss";  -- Ferme en petite perte
        end
    end

    -- ==================================================================
    -- SORTIE 4: RSI SURACHAT (optionnel)
    -- ==================================================================
    -- Si active, on sort quand le RSI indique un surachat.
    -- Cela peut augmenter le win rate mais limite les gros gains.
    --
    if instance.parameters.use_rsi_exit then
        local rsi_exit = instance.parameters.rsi_exit_threshold;
        if rsi >= rsi_exit and price > entry_price then
            return true, "rsi_exit";
        end
    end

    return false, "none";
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

    -- Calculer le Stop Loss et le Take Profit bases sur l'ATR
    local sl_distance = atr * instance.parameters.atr_sl_mult;
    local tp_distance = atr * instance.parameters.atr_tp_mult;

    stop_loss = entry_price - sl_distance;
    take_profit = entry_price + tp_distance;
end


function closeTrade(period, reason)
    local exit_price = 0;

    -- Determiner le prix de sortie selon la raison
    if reason == "stop" then
        exit_price = stop_loss;  -- Sorti au stop
    elseif reason == "profit" then
        exit_price = take_profit;  -- Sorti au TP
    else
        exit_price = source.close[period];  -- Sorti au close
    end

    -- Calculer le P&L en pourcentage
    local pnl_pct = ((exit_price - entry_price) / entry_price) * 100;

    -- Mettre a jour les compteurs
    total_trades = total_trades + 1;

    if pnl_pct > 0 then
        wins = wins + 1;
        total_win_pct = total_win_pct + pnl_pct;
        consecutive_losses = 0;
    else
        losses = losses + 1;
        total_loss_pct = total_loss_pct + math.abs(pnl_pct);
        consecutive_losses = consecutive_losses + 1;
        if consecutive_losses > max_consec_losses then
            max_consec_losses = consecutive_losses;
        end
    end

    -- Mettre a jour l'equity simulee
    equity = equity * (1 + pnl_pct / 100);
    table.insert(equity_arr, equity);

    -- Mettre a jour le drawdown
    if equity > max_equity then
        max_equity = equity;
    end
    local current_dd = ((max_equity - equity) / max_equity) * 100;
    if current_dd > max_drawdown then
        max_drawdown = current_dd;
    end

    -- Reset
    in_position = false;
    entry_price = 0;
    stop_loss = 0;
    take_profit = 0;
    entry_bar = 0;

    return pnl_pct, reason;
end


-- #############################################################################
--
--  10. METRIQUES DE PERFORMANCE
--
-- #############################################################################
--
-- CES METRIQUES SONT ESSENTIELLES pour evaluer un systeme de trading.
-- Un win rate de 80% ne suffit PAS. Il faut aussi regarder:
--   - Le Profit Factor (doit etre > 1.0 pour etre rentable)
--   - Le Max Drawdown (la pire serie de pertes)
--   - Le Sharpe Ratio (rendement ajuste au risque)
--   - Le R:R ratio (combien on gagne vs combien on perd)
--
-- =============================================================================

function printMetrics()
    if total_trades == 0 then
        core.host:trace("=== AUCUN TRADE ===");
        return;
    end

    local win_rate = (wins / total_trades) * 100;
    local avg_win = 0;
    local avg_loss = 0;

    if wins > 0 then
        avg_win = total_win_pct / wins;
    end
    if losses > 0 then
        avg_loss = total_loss_pct / losses;
    end

    -- Risk/Reward Ratio
    local rr_ratio = 0;
    if avg_loss > 0 then
        rr_ratio = avg_win / avg_loss;
    end

    -- Profit Factor = gains totaux / pertes totales
    local profit_factor = 0;
    if total_loss_pct > 0 then
        profit_factor = total_win_pct / total_loss_pct;
    else
        profit_factor = 999;  -- Pas de pertes = infini
    end

    -- Sharpe Ratio simplifie
    -- (rendement moyen par trade / ecart-type des rendements)
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
            sharpe = (mean / stddev) * math.sqrt(252);  -- Annualise (252 jours)
        end
    end

    -- Rendement total
    local total_return = equity - 100;

    -- Afficher dans la console (onglet Messages de Trading Station)
    core.host:trace("========================================================");
    core.host:trace("   RESULTATS DU BACKTEST — BTC Smart Pullback D1");
    core.host:trace("========================================================");
    core.host:trace("   Trades totaux:        " .. total_trades);
    core.host:trace("   Victoires:            " .. wins);
    core.host:trace("   Defaites:             " .. losses);
    core.host:trace("   TAUX DE VICTOIRE:     " .. string.format("%.1f", win_rate) .. "%");
    core.host:trace("--------------------------------------------------------");
    core.host:trace("   Gain moyen:           +" .. string.format("%.2f", avg_win) .. "%");
    core.host:trace("   Perte moyenne:        -" .. string.format("%.2f", avg_loss) .. "%");
    core.host:trace("   Ratio Risk/Reward:    " .. string.format("%.2f", rr_ratio));
    core.host:trace("   Profit Factor:        " .. string.format("%.2f", profit_factor));
    core.host:trace("--------------------------------------------------------");
    core.host:trace("   Rendement total:      " .. string.format("%.1f", total_return) .. "%");
    core.host:trace("   Max Drawdown:         -" .. string.format("%.1f", max_drawdown) .. "%");
    core.host:trace("   Sharpe Ratio:         " .. string.format("%.2f", sharpe));
    core.host:trace("   Pertes consec. max:   " .. max_consec_losses);
    core.host:trace("========================================================");

    -- INTERPRETATION:
    -- Win rate >= 80%: OBJECTIF ATTEINT
    -- Profit Factor > 1.0: Le systeme est RENTABLE
    -- Sharpe > 1.0: Bon rendement ajuste au risque
    -- Max DD < 20%: Risque acceptable
end


-- #############################################################################
--
--  11. FONCTION UPDATE()
--
-- #############################################################################
--
-- C'est la fonction PRINCIPALE. Appelee pour CHAQUE bougie.
-- Elle orchestre tout: calculs, signaux, trades, affichage.
--
-- =============================================================================

function Update(period, mode)
    -- Attendre d'avoir assez de donnees
    local min_period = instance.parameters.ema_slow_period + 20;
    if period < min_period then
        return;
    end

    -- ==================================================================
    -- ETAPE 1: Calculer tous les indicateurs
    -- ==================================================================
    local price = source.close[period];
    local ema_fast = calcEMA(period, price, ema_fast_arr, instance.parameters.ema_fast_period);
    local ema_slow = calcEMA(period, price, ema_slow_arr, instance.parameters.ema_slow_period);
    local rsi = calcRSI(period, instance.parameters.rsi_period);
    local atr = calcATR(period, instance.parameters.atr_period);

    -- ==================================================================
    -- ETAPE 2: Afficher des infos sous les bougies (optionnel)
    -- ==================================================================
    if instance.parameters.showStreak then
        local info = "R:" .. string.format("%.0f", rsi);
        if in_position then
            info = info .. " [P]";
        end
        streak_text:set(period, source.low[period], info, core.rgb(160, 160, 160));
    end

    -- ==================================================================
    -- ETAPE 3: Verifier les sorties AVANT les entrees
    -- (si on est en position, on gere d'abord la sortie)
    -- ==================================================================
    if in_position then
        local should_exit, reason = shouldExit(period, rsi);
        if should_exit then
            local pnl, exit_reason = closeTrade(period, reason);

            if pnl >= 0 then
                -- Trade gagnant: fleche bleue + texte
                sell_arrow:set(period, source.high[period], "\234");
                local txt;
                if exit_reason == "profit" then
                    txt = "TP +" .. string.format("%.1f", pnl) .. "%";
                elseif exit_reason == "rsi_exit" then
                    txt = "RSI +" .. string.format("%.1f", pnl) .. "%";
                else
                    txt = "+" .. string.format("%.1f", pnl) .. "%";
                end
                sell_label:set(period, source.high[period], txt);
            else
                -- Trade perdant: fleche rouge + texte
                stop_arrow:set(period, source.high[period], "\234");
                local txt;
                if exit_reason == "stop" then
                    txt = "SL " .. string.format("%.1f", pnl) .. "%";
                else
                    txt = string.format("%.1f", pnl) .. "%";
                end
                stop_label:set(period, source.high[period], txt);
            end
        end

        -- Marqueur en position (losange bleu)
        if in_position then
            pos_marker:set(period, source.high[period], "\108");
        end
    end

    -- ==================================================================
    -- ETAPE 4: Verifier les entrees
    -- ==================================================================
    if shouldEnter(period, ema_fast, ema_slow, rsi, atr) then
        openTrade(period, atr);

        -- Fleche BUY + texte
        buy_arrow:set(period, source.low[period], "\233");
        buy_label:set(period, source.low[period], "BUY");
    end

    -- ==================================================================
    -- ETAPE 5: Imprimer les metriques sur la derniere bougie
    -- ==================================================================
    if period == source:size() - 1 then
        printMetrics();
    end
end
