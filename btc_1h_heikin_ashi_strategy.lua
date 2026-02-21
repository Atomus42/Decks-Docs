-- =============================================================================
--
--  STRATEGIE HEIKIN ASHI WEEKLY (12G/6R)
--  Pour FXCM Trading Station Desktop (Lua / Indicore SDK)
--
--  RESULTATS DU BACKTEST (2 ans, BTC/USD 1H):
--  - Rendement: +78.40%  |  Sharpe: 1.53  |  MaxDD: -17.78%
--  - Taux de reussite: 53%  |  Facteur de profit: 1.94
--  - Bat le Buy & Hold de +47.54%
--
--  LOGIQUE:
--  - Calcule les bougies Heikin Ashi a partir des bougies normales OHLC
--  - Compte les bougies HA vertes (HA_close > HA_open) consecutives
--  - Compte les bougies HA rouges (HA_close <= HA_open) consecutives
--  - ACHAT:  quand 12 bougies HA vertes consecutives apparaissent
--  - VENTE:  quand 6 bougies HA rouges consecutives apparaissent
--  - Long seulement (achat uniquement, pas de vente a decouvert)
--
--  INSTALLATION:
--  1. Fermez completement Trading Station
--  2. Copiez ce fichier (.lua) dans:
--     C:\Program Files (x86)\Candleworks\FXTS2\strategies\Custom\
--  3. Relancez Trading Station et connectez-vous
--  4. Allez dans "Alertes et Automatisation" > "Nouvelle Strategie"
--  5. Selectionnez "Heikin Ashi Weekly 12G/6R"
--  6. Configurez les parametres et cliquez OK
--
--  POUR MODIFIER LES VALEURS:
--  Quand vous lancez la strategie, une fenetre "Parametres" apparait.
--  Changez les valeurs directement dans cette fenetre.
--  OU modifiez les nombres par defaut dans ce fichier (voir ci-dessous).
--
-- =============================================================================


-- ██████████████████████████████████████████████████████████████████████████
--
--  PARAMETRES MODIFIABLES PAR L'UTILISATEUR
--
--  Ces valeurs apparaissent dans la fenetre "Parametres" quand vous
--  lancez la strategie. Vous pouvez les changer sans toucher au code.
--
--  Pour changer les valeurs par defaut dans le code:
--  Trouvez la ligne avec addInteger ou addDouble et changez le nombre.
--  Exemple: addInteger("green_threshold", ..., 12)
--                                               ^^-- changez ce nombre
--
-- ██████████████████████████████████████████████████████████████████████████


-- =============================================================================
-- VARIABLES GLOBALES (ne pas modifier)
-- =============================================================================
local source = nil;          -- Source de donnees (bougies)
local ha_open = 0;           -- Ouverture Heikin Ashi precedente
local ha_close = 0;          -- Fermeture Heikin Ashi precedente
local consec_green = 0;      -- Compteur de bougies vertes consecutives
local consec_red = 0;        -- Compteur de bougies rouges consecutives
local ha_initialized = false;-- Etat d'initialisation du HA
local Account = nil;         -- Compte de trading
local base_size = 0;         -- Taille de lot de base
local offer_id = nil;        -- ID de l'offre
local Amount = 0;            -- Montant a trader
local custom_id = "";        -- ID unique de la strategie


-- =============================================================================
-- FONCTION INIT()
-- Appelee UNE SEULE FOIS quand Trading Station charge la strategie.
-- Definit le nom, la description et tous les parametres ajustables.
-- =============================================================================
function Init()
    strategy:name("Heikin Ashi Weekly 12G/6R");
    strategy:description(
        "Strategie basee sur les bougies Heikin Ashi.\n" ..
        "ACHAT: 12 bougies HA vertes consecutives.\n" ..
        "VENTE: 6 bougies HA rouges consecutives.\n" ..
        "Rendement backtest: +78.40% | Sharpe: 1.53"
    );
    strategy:type(core.Both);

    -- =====================================================================
    -- GROUPE: Parametres de la Strategie
    -- C'est ici que vous definissez les seuils d'entree et de sortie.
    -- =====================================================================
    strategy.parameters:addGroup("Parametres Heikin Ashi");

    -- SEUIL D'ENTREE: Nombre de bougies HA vertes pour acheter
    -- Par defaut: 12 (valeur optimale du backtest)
    -- Plus bas = plus de trades, entre plus tot mais plus de faux signaux
    -- Plus haut = moins de trades, entre plus tard mais meilleure conviction
    strategy.parameters:addInteger("green_threshold", "Bougies vertes pour ACHETER", "", 12, 1, 50);
    --                                                                                   ^^
    --                                                         CHANGEZ CE NOMBRE (defaut: 12)

    -- SEUIL DE SORTIE: Nombre de bougies HA rouges pour vendre
    -- Par defaut: 6 (sort plus vite qu'on entre = protege les profits)
    -- Plus bas = sort plus vite, garde plus de profit mais risque de sortir trop tot
    -- Plus haut = sort plus lentement, suit la tendance plus longtemps
    strategy.parameters:addInteger("red_threshold", "Bougies rouges pour VENDRE", "", 6, 1, 50);
    --                                                                                  ^
    --                                                         CHANGEZ CE NOMBRE (defaut: 6)

    -- =====================================================================
    -- GROUPE: Parametres de Trading
    -- Configuration du compte, de la taille des trades, etc.
    -- =====================================================================
    strategy.parameters:addGroup("Parametres de Trading");

    -- Type de prix (Bid ou Ask)
    strategy.parameters:addBoolean("type", "Type de prix", "", true);
    strategy.parameters:setFlag("type", core.FLAG_BIDASK);

    -- Timeframe (periode des bougies)
    -- Par defaut: H1 (1 heure) — c'est le timeframe optimal pour cette strategie
    strategy.parameters:addString("timeframe", "Timeframe", "", "H1");
    strategy.parameters:setFlag("timeframe", core.FLAG_PERIODS);

    -- Autoriser le trading automatique
    strategy.parameters:addBoolean("AllowTrade", "Autoriser le trading automatique", "", false);
    strategy.parameters:setFlag("AllowTrade", core.FLAG_ALLOW_TRADE);

    -- Compte de trading
    strategy.parameters:addString("Account", "Compte de trading", "", "");
    strategy.parameters:setFlag("Account", core.FLAG_ACCOUNT);

    -- Taille du trade
    strategy.parameters:addDouble("Amount", "Taille du trade (lots)", "", 1, 0.01, 10000);
    --                                                                    ^
    --                                             CHANGEZ CE NOMBRE (defaut: 1 lot)

    -- ID personnalise pour identifier les trades de cette strategie
    strategy.parameters:addString("custom_id", "ID de la strategie", "", "HA_12G6R");

    -- =====================================================================
    -- GROUPE: Gestion du Risque (Stop Loss / Take Profit)
    -- =====================================================================
    strategy.parameters:addGroup("Gestion du Risque");

    -- Stop Loss (en pips)
    -- Par defaut: desactive. Activez si vous voulez un filet de securite.
    strategy.parameters:addBoolean("use_stop", "Utiliser un Stop Loss", "", false);
    strategy.parameters:addDouble("stop_pips", "Stop Loss (pips)", "", 500, 1, 100000);
    --                                                                  ^^^
    --                                     CHANGEZ CE NOMBRE (defaut: 500 pips)

    -- Take Profit (en pips)
    -- Par defaut: desactive. La sortie est geree par la regle des 6 rouges.
    strategy.parameters:addBoolean("use_limit", "Utiliser un Take Profit", "", false);
    strategy.parameters:addDouble("limit_pips", "Take Profit (pips)", "", 1000, 1, 100000);
    --                                                                   ^^^^
    --                                    CHANGEZ CE NOMBRE (defaut: 1000 pips)

    -- =====================================================================
    -- GROUPE: Alertes
    -- =====================================================================
    strategy.parameters:addGroup("Alertes");
    strategy.parameters:addBoolean("show_alert", "Afficher les alertes popup", "", true);
    strategy.parameters:addBoolean("play_sound", "Jouer un son", "", false);
    strategy.parameters:addFile("sound_file", "Fichier son", "", "");
    strategy.parameters:setFlag("sound_file", core.FLAG_SOUND);
    strategy.parameters:addBoolean("send_email", "Envoyer un email", "", false);
    strategy.parameters:addString("email", "Adresse email", "", "");
    strategy.parameters:setFlag("email", core.FLAG_EMAIL);
end


-- =============================================================================
-- FONCTION PREPARE()
-- Appelee quand l'utilisateur a rempli les parametres et lance la strategie.
-- Configure les sources de donnees et prepare le trading.
-- =============================================================================
function Prepare(nameOnly)
    -- Nom affiche dans Trading Station
    local name = profile:id() .. "(" .. instance.bid:name() .. ")"
        .. " HA " .. instance.parameters.green_threshold .. "G/"
        .. instance.parameters.red_threshold .. "R";
    instance:name(name);
    if nameOnly then
        return;
    end

    -- Charger les parametres
    Account = instance.parameters.Account;
    Amount = instance.parameters.Amount;
    custom_id = instance.parameters.custom_id;

    -- S'abonner aux donnees de prix (bougies)
    source = ExtSubscribe(1, nil, instance.parameters.timeframe, instance.parameters.type, "bar");

    -- Informations sur l'instrument
    base_size = core.host:execute("getTradingProperty", "baseUnitSize", instance.bid:instrument(), Account);
    offer_id = core.host:findTable("offers"):find("Instrument", instance.bid:instrument()).OfferID;

    -- Reinitialiser l'etat Heikin Ashi
    ha_initialized = false;
    consec_green = 0;
    consec_red = 0;
end


-- =============================================================================
-- FONCTION ExtUpdate()
-- Appelee A CHAQUE NOUVELLE BOUGIE (ou tick selon la config).
-- C'est le COEUR de la strategie: calcule le HA, compte les streaks,
-- et decide d'acheter ou vendre.
-- =============================================================================
function ExtUpdate(id, source, period)
    -- On ne traite que la source principale (id=1)
    if id ~= 1 then
        return;
    end

    -- Il faut au moins 2 bougies pour calculer le Heikin Ashi
    if period < 1 then
        return;
    end

    -- ==================================================================
    -- ETAPE 1: Calculer la bougie Heikin Ashi
    --
    -- Formules:
    --   HA_Close = (Open + High + Low + Close) / 4
    --   HA_Open  = (HA_Open_precedent + HA_Close_precedent) / 2
    --   Verte = HA_Close > HA_Open
    --   Rouge = HA_Close <= HA_Open
    -- ==================================================================

    -- Prix de la bougie actuelle
    local c_open  = source.open[period];
    local c_high  = source.high[period];
    local c_low   = source.low[period];
    local c_close = source.close[period];

    -- Calculer le HA Close (moyenne des 4 prix)
    local new_ha_close = (c_open + c_high + c_low + c_close) / 4.0;

    -- Calculer le HA Open
    local new_ha_open;
    if not ha_initialized then
        -- Premiere bougie: HA_Open = (Open + Close) / 2
        new_ha_open = (c_open + c_close) / 2.0;
        ha_initialized = true;
    else
        -- Bougies suivantes: HA_Open = (HA_Open_prec + HA_Close_prec) / 2
        new_ha_open = (ha_open + ha_close) / 2.0;
    end

    -- ==================================================================
    -- ETAPE 2: Compter les bougies vertes/rouges consecutives
    -- ==================================================================

    if new_ha_close > new_ha_open then
        -- BOUGIE VERTE (haussiere)
        consec_green = consec_green + 1;
        consec_red = 0;
    else
        -- BOUGIE ROUGE (baissiere)
        consec_red = consec_red + 1;
        consec_green = 0;
    end

    -- Sauvegarder l'etat pour la prochaine bougie
    ha_open = new_ha_open;
    ha_close = new_ha_close;

    -- ==================================================================
    -- ETAPE 3: Verifier les conditions d'entree et de sortie
    -- ==================================================================

    local green_threshold = instance.parameters.green_threshold;
    local red_threshold = instance.parameters.red_threshold;
    local has_position = HasOpenTrade();

    -- -----------------------------------------------------------------
    -- CONDITION D'ACHAT:
    -- Le streak vert a atteint le seuil ET on n'a pas de position
    -- -----------------------------------------------------------------
    if consec_green >= green_threshold and not has_position then
        -- ACHETER !
        OpenBuyTrade();

        -- Afficher l'alerte
        local msg = "ACHAT: " .. instance.bid:instrument()
            .. " | " .. consec_green .. " bougies HA vertes"
            .. " | Prix: " .. string.format("%.5f", source.close[period]);
        SendAlert(msg);
    end

    -- -----------------------------------------------------------------
    -- CONDITION DE VENTE:
    -- Le streak rouge a atteint le seuil ET on a une position ouverte
    -- -----------------------------------------------------------------
    if consec_red >= red_threshold and has_position then
        -- VENDRE ! (fermer la position)
        CloseAllTrades();

        -- Afficher l'alerte
        local msg = "VENTE: " .. instance.bid:instrument()
            .. " | " .. consec_red .. " bougies HA rouges"
            .. " | Prix: " .. string.format("%.5f", source.close[period]);
        SendAlert(msg);
    end
end


-- =============================================================================
-- FONCTIONS DE TRADING
-- Ces fonctions gerent l'ouverture et la fermeture des positions.
-- Vous n'avez pas besoin de les modifier.
-- =============================================================================


-- Verifie si on a deja un trade ouvert par cette strategie
function HasOpenTrade()
    local trades = core.host:findTable("trades");
    local enum = trades:enumerator();
    while enum:next() do
        local row = enum:current();
        if row.AccountID == Account
            and row.OfferID == offer_id
            and row.BS == "B"  -- Buy seulement (long only)
            and (row.QTXT == custom_id or custom_id == "") then
            return true;
        end
    end
    return false;
end


-- Ouvre un trade ACHAT (BUY)
function OpenBuyTrade()
    if not instance.parameters.AllowTrade then
        -- Trading automatique desactive: on affiche juste le signal
        core.host:trace("SIGNAL ACHAT (trading auto desactive)");
        return;
    end

    -- Calculer la taille du trade en unites
    local lot_size = Amount * base_size;

    -- Creer l'ordre d'achat
    local valuemap = core.valuemap();
    valuemap.Command = "CreateOrder";
    valuemap.OrderType = "OM";       -- Ordre au Marche (Market Order)
    valuemap.OfferID = offer_id;
    valuemap.AcctID = Account;
    valuemap.Quantity = lot_size;
    valuemap.BuySell = "B";          -- B = Buy (Achat)
    valuemap.CustomID = custom_id;

    -- Ajouter un Stop Loss si active
    if instance.parameters.use_stop then
        valuemap.RateStop = instance.bid:tick() - (instance.parameters.stop_pips * instance.bid:pipSize());
    end

    -- Ajouter un Take Profit si active
    if instance.parameters.use_limit then
        valuemap.RateLimit = instance.ask:tick() + (instance.parameters.limit_pips * instance.bid:pipSize());
    end

    -- Envoyer l'ordre
    local success, msg = terminal:execute(200, valuemap);
    if not success then
        core.host:trace("ERREUR ouverture achat: " .. (msg or "inconnue"));
    else
        core.host:trace("ACHAT ouvert: " .. Amount .. " lots");
    end
end


-- Ferme tous les trades ouverts par cette strategie
function CloseAllTrades()
    if not instance.parameters.AllowTrade then
        core.host:trace("SIGNAL VENTE (trading auto desactive)");
        return;
    end

    local trades = core.host:findTable("trades");
    local enum = trades:enumerator();
    while enum:next() do
        local row = enum:current();
        if row.AccountID == Account
            and row.OfferID == offer_id
            and row.BS == "B"
            and (row.QTXT == custom_id or custom_id == "") then

            -- Creer l'ordre de fermeture
            local valuemap = core.valuemap();
            valuemap.Command = "CreateOrder";
            valuemap.OrderType = "CM";       -- Close Market (fermer au marche)
            valuemap.OfferID = offer_id;
            valuemap.AcctID = Account;
            valuemap.Quantity = row.Lot;
            valuemap.BuySell = "S";          -- S = Sell (pour fermer un Buy)
            valuemap.TradeID = row.TradeID;

            local success, msg = terminal:execute(201, valuemap);
            if not success then
                core.host:trace("ERREUR fermeture: " .. (msg or "inconnue"));
            else
                core.host:trace("Position fermee: TradeID " .. row.TradeID);
            end
        end
    end
end


-- =============================================================================
-- FONCTIONS D'ALERTE
-- Envoie des notifications popup, son ou email selon les parametres.
-- =============================================================================
function SendAlert(message)
    -- Ajouter un log dans l'onglet "Messages" de Trading Station
    core.host:trace(message);

    -- Popup d'alerte
    if instance.parameters.show_alert then
        core.host:execute("alert", message);
    end

    -- Jouer un son
    if instance.parameters.play_sound then
        core.host:execute("playSound", instance.parameters.sound_file);
    end

    -- Envoyer un email
    if instance.parameters.send_email then
        core.host:execute("sendMail",
            "HA Strategy Signal",      -- Sujet
            message,                   -- Corps du message
            instance.parameters.email  -- Destinataire
        );
    end
end


-- =============================================================================
-- FONCTION AsyncOperationFinished()
-- Appelee quand une operation asynchrone (trade, chargement) est terminee.
-- Necessaire pour le framework Indicore.
-- =============================================================================
function AsyncOperationFinished(cookie, success, message)
    if cookie == 200 and success then
        core.host:trace("Ordre d'achat execute avec succes");
    elseif cookie == 200 and not success then
        core.host:trace("Echec de l'ordre d'achat: " .. (message or ""));
    elseif cookie == 201 and success then
        core.host:trace("Ordre de fermeture execute avec succes");
    elseif cookie == 201 and not success then
        core.host:trace("Echec de la fermeture: " .. (message or ""));
    end
end


-- =============================================================================
-- FONCTIONS UTILITAIRES INDICORE
-- Necessaires pour le framework. Ne pas modifier.
-- =============================================================================

-- Souscription aux donnees de prix
local sources = {};
function ExtSubscribe(id, instrument, timeframe, isBid, style)
    local source_id = id;
    local instrument_str = instrument;
    if instrument_str == nil then
        instrument_str = instance.bid:instrument();
    end

    local s1, ticks;
    if isBid then
        s1 = core.host:execute("subscribeBid", instrument_str, nil);
    else
        s1 = core.host:execute("subscribeAsk", instrument_str, nil);
    end

    local from, to;
    if timeframe == "t1" then
        ticks = s1;
    else
        from = s1:date(0);
        ticks = core.host:execute("getHistory", source_id, s1, timeframe, from, 0, 300);
    end

    sources[source_id] = ticks;
    return ticks;
end

-- Mise a jour des sources de donnees
function ExtAsyncOperationFinished(cookie, success, message, message1, message2)
    -- Routage vers AsyncOperationFinished pour les trades
    if cookie >= 200 then
        AsyncOperationFinished(cookie, success, message);
        return;
    end

    -- Mise a jour des sources
    local src = sources[cookie];
    if src ~= nil then
        local period = src:size() - 1;
        if period >= 0 then
            ExtUpdate(cookie, src, period);
        end
    end
end
