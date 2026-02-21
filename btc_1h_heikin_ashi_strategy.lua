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
local Source = nil;              -- Source de donnees (bougies)
local ha_open = 0;               -- Ouverture Heikin Ashi precedente
local ha_close = 0;              -- Fermeture Heikin Ashi precedente
local consec_green = 0;          -- Compteur de bougies vertes consecutives
local consec_red = 0;            -- Compteur de bougies rouges consecutives
local ha_initialized = false;    -- Etat d'initialisation du HA
local Account = nil;             -- Compte de trading
local BaseSize = 0;              -- Taille de lot de base (unites minimum)
local Offer = nil;               -- ID de l'offre (instrument)
local Amount = 0;                -- Montant a trader (en lots)
local CanClose = false;          -- Si le compte supporte les ordres de fermeture
local SetLimit = false;          -- Si on utilise un take profit
local SetStop = false;           -- Si on utilise un stop loss
local Limit = 0;                 -- Take profit en pips
local Stop = 0;                  -- Stop loss en pips


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

    -- Compte de trading
    strategy.parameters:addString("Account", "Compte de trading", "", "");
    strategy.parameters:setFlag("Account", core.FLAG_ACCOUNT);

    -- Taille du trade
    strategy.parameters:addInteger("Amount", "Taille du trade (lots)", "", 1, 1, 1000);
    --                                                                      ^
    --                                             CHANGEZ CE NOMBRE (defaut: 1 lot)

    -- Autoriser le trading automatique
    strategy.parameters:addBoolean("AllowTrade", "Autoriser le trading automatique", "", false);
    strategy.parameters:setFlag("AllowTrade", core.FLAG_ALLOW_TRADE);

    -- =====================================================================
    -- GROUPE: Gestion du Risque (Stop Loss / Take Profit)
    -- =====================================================================
    strategy.parameters:addGroup("Gestion du Risque");

    -- Stop Loss (en pips)
    -- Par defaut: desactive. Activez si vous voulez un filet de securite.
    strategy.parameters:addBoolean("SetStop", "Utiliser un Stop Loss", "", false);
    strategy.parameters:addInteger("Stop", "Stop Loss (pips)", "", 500, 1, 100000);
    --                                                             ^^^
    --                                     CHANGEZ CE NOMBRE (defaut: 500 pips)

    -- Take Profit (en pips)
    -- Par defaut: desactive. La sortie est geree par la regle des 6 rouges.
    strategy.parameters:addBoolean("SetLimit", "Utiliser un Take Profit", "", false);
    strategy.parameters:addInteger("Limit", "Take Profit (pips)", "", 1000, 1, 100000);
    --                                                                ^^^^
    --                                    CHANGEZ CE NOMBRE (defaut: 1000 pips)

    -- =====================================================================
    -- GROUPE: Alertes
    -- =====================================================================
    strategy.parameters:addGroup("Alertes");
    strategy.parameters:addBoolean("ShowAlert", "Afficher les alertes popup", "", true);
    strategy.parameters:addBoolean("PlaySound", "Jouer un son", "", false);
    strategy.parameters:addFile("SoundFile", "Fichier son", "", "");
    strategy.parameters:setFlag("SoundFile", core.FLAG_SOUND);
    strategy.parameters:addBoolean("SendEmail", "Envoyer un email", "", false);
    strategy.parameters:addString("Email", "Adresse email", "", "");
    strategy.parameters:setFlag("Email", core.FLAG_EMAIL);
end


-- =============================================================================
-- FONCTION PREPARE()
-- Appelee quand l'utilisateur a rempli les parametres et lance la strategie.
-- Configure les sources de donnees et prepare le trading.
-- =============================================================================
function Prepare(nameOnly)
    -- Nom affiche dans Trading Station
    local name = profile:id() .. "(" .. instance.bid:name() .. ")";
    instance:name(name);
    if nameOnly then
        return;
    end

    -- Charger les parametres
    Account = instance.parameters.Account;
    Amount = instance.parameters.Amount;
    SetLimit = instance.parameters.SetLimit;
    SetStop = instance.parameters.SetStop;
    Limit = instance.parameters.Limit;
    Stop = instance.parameters.Stop;

    -- Informations sur l'instrument
    BaseSize = core.host:execute("getTradingProperty", "baseUnitSize", instance.bid:instrument(), Account);
    Offer = core.host:findTable("offers"):find("Instrument", instance.bid:instrument()).OfferID;
    CanClose = core.host:execute("getTradingProperty", "canCreateMarketClose", instance.bid:instrument(), Account);

    -- S'abonner aux donnees de prix (bougies)
    -- Le 2eme parametre nil = instrument courant, "H1" = timeframe 1 heure
    Source = ExtSubscribe(1, nil, "H1", instance.parameters.Account == "B", "bar");

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

    -- -----------------------------------------------------------------
    -- CONDITION D'ACHAT:
    -- Le streak vert a atteint le seuil ET on n'a pas de position
    -- -----------------------------------------------------------------
    if consec_green >= green_threshold and not haveTrades("B") then
        -- ACHETER !
        enter("B");

        -- Afficher l'alerte
        local msg = ">>> ACHAT: " .. instance.bid:instrument()
            .. " | " .. consec_green .. " bougies HA vertes"
            .. " | Prix: " .. string.format("%.5f", source.close[period]);
        Signal(msg);
    end

    -- -----------------------------------------------------------------
    -- CONDITION DE VENTE:
    -- Le streak rouge a atteint le seuil ET on a une position ouverte
    -- -----------------------------------------------------------------
    if consec_red >= red_threshold and haveTrades("B") then
        -- VENDRE ! (fermer la position)
        exit("B");

        -- Afficher l'alerte
        local msg = ">>> VENTE: " .. instance.bid:instrument()
            .. " | " .. consec_red .. " bougies HA rouges"
            .. " | Prix: " .. string.format("%.5f", source.close[period]);
        Signal(msg);
    end
end


-- =============================================================================
-- FONCTIONS DE TRADING
-- Ces fonctions gerent l'ouverture et la fermeture des positions.
-- Utilise le pattern standard FXCM avec terminal:execute.
-- =============================================================================

-- Verifie si on a deja un trade ouvert dans la direction donnee
-- BuySell = "B" pour Buy (achat) ou "S" pour Sell (vente)
function haveTrades(BuySell)
    local dominated = false;
    local trades = core.host:findTable("trades");
    local enum = trades:enumerator();
    while enum:next() do
        local row = enum:current();
        if row.AccountID == Account
            and row.OfferID == Offer
            and row.BS == BuySell then
            dominated = true;
        end
    end
    return dominated;
end


-- Ouvre un trade dans la direction donnee
-- BuySell = "B" pour acheter, "S" pour vendre
function enter(BuySell)
    if not instance.parameters.AllowTrade then
        -- Trading automatique desactive: on affiche juste le signal
        core.host:trace("SIGNAL ACHAT (trading auto desactive)");
        return;
    end

    -- Creer l'ordre d'achat au marche
    local valuemap = core.valuemap();
    valuemap.OrderType = "OM";           -- OM = Open Market (ordre au marche)
    valuemap.OfferID = Offer;
    valuemap.AcctID = Account;
    valuemap.Quantity = Amount * BaseSize;
    valuemap.BuySell = BuySell;

    -- Ajouter un Stop Loss si active (en pips, type pegged)
    if SetStop then
        valuemap.PegTypeStop = "O";      -- O = relatif au prix d'ouverture
        if BuySell == "B" then
            valuemap.PegPriceOffsetPipsStop = -Stop;   -- Stop sous le prix pour un achat
        else
            valuemap.PegPriceOffsetPipsStop = Stop;    -- Stop au-dessus pour une vente
        end
    end

    -- Ajouter un Take Profit si active (en pips, type pegged)
    if SetLimit then
        valuemap.PegTypeLimit = "O";     -- O = relatif au prix d'ouverture
        if BuySell == "B" then
            valuemap.PegPriceOffsetPipsLimit = Limit;  -- Limit au-dessus pour un achat
        else
            valuemap.PegPriceOffsetPipsLimit = -Limit; -- Limit sous le prix pour une vente
        end
    end

    -- Envoyer l'ordre via terminal:execute
    -- Le cookie 100 identifie cet ordre dans AsyncOperationFinished
    local success, msg = terminal:execute(100, valuemap);
    if not success then
        terminal:alertMessage(instance.bid:instrument(),
            instance.bid[NOW],
            "ERREUR ouverture: " .. (msg or "inconnue"),
            instance.bid:date(NOW));
    else
        core.host:trace("Ordre ACHAT envoye: " .. Amount .. " lot(s)");
    end
end


-- Ferme tous les trades ouverts dans la direction donnee
-- BuySell = "B" pour fermer les achats
function exit(BuySell)
    if not instance.parameters.AllowTrade then
        core.host:trace("SIGNAL VENTE (trading auto desactive)");
        return;
    end

    -- Determiner le cote oppose pour fermer
    local closeSide;
    if BuySell == "B" then
        closeSide = "S";    -- Pour fermer un Buy, on Sell
    else
        closeSide = "B";    -- Pour fermer un Sell, on Buy
    end

    if CanClose then
        -- Le compte supporte les ordres de fermeture directe (CM)
        -- On utilise NetQtyFlag pour fermer toutes les positions d'un coup
        local valuemap = core.valuemap();
        valuemap.OrderType = "CM";           -- CM = Close Market
        valuemap.OfferID = Offer;
        valuemap.AcctID = Account;
        valuemap.NetQtyFlag = "Y";           -- Fermer la position nette
        valuemap.BuySell = closeSide;

        local success, msg = terminal:execute(200, valuemap);
        if not success then
            terminal:alertMessage(instance.bid:instrument(),
                instance.bid[NOW],
                "ERREUR fermeture CM: " .. (msg or "inconnue"),
                instance.bid:date(NOW));
        else
            core.host:trace("Ordre de FERMETURE (CM) envoye");
        end
    else
        -- Compte FIFO ou pas de support CM: fermer avec un ordre oppose (OM)
        local trades = core.host:findTable("trades");
        local totalLots = 0;
        local enum = trades:enumerator();
        while enum:next() do
            local row = enum:current();
            if row.AccountID == Account
                and row.OfferID == Offer
                and row.BS == BuySell then
                totalLots = totalLots + row.Lot;
            end
        end

        if totalLots > 0 then
            local valuemap = core.valuemap();
            valuemap.OrderType = "OM";       -- Ordre au marche oppose
            valuemap.OfferID = Offer;
            valuemap.AcctID = Account;
            valuemap.Quantity = totalLots;
            valuemap.BuySell = closeSide;

            local success, msg = terminal:execute(200, valuemap);
            if not success then
                terminal:alertMessage(instance.bid:instrument(),
                    instance.bid[NOW],
                    "ERREUR fermeture OM: " .. (msg or "inconnue"),
                    instance.bid:date(NOW));
            else
                core.host:trace("Ordre de FERMETURE (OM oppose) envoye");
            end
        end
    end
end


-- =============================================================================
-- FONCTIONS D'ALERTE
-- Envoie des notifications popup, son ou email selon les parametres.
-- =============================================================================
function Signal(message)
    -- Ajouter un log dans l'onglet "Messages" de Trading Station
    core.host:trace(message);

    -- Popup d'alerte
    if instance.parameters.ShowAlert then
        terminal:alertMessage(instance.bid:instrument(),
            instance.bid[NOW],
            message,
            instance.bid:date(NOW));
    end

    -- Jouer un son
    if instance.parameters.PlaySound then
        terminal:alertSound(instance.parameters.SoundFile, false);
    end

    -- Envoyer un email
    if instance.parameters.SendEmail then
        terminal:alertEmail(instance.parameters.Email,
            "HA Strategy Signal",
            message);
    end
end


-- =============================================================================
-- FONCTION AsyncOperationFinished()
-- Appelee quand une operation asynchrone (trade) est terminee.
-- Cookie 100 = ouverture, Cookie 200 = fermeture.
-- =============================================================================
function AsyncOperationFinished(cookie, success, message)
    if cookie == 100 then
        if success then
            core.host:trace(">>> Ordre d'achat EXECUTE avec succes");
        else
            core.host:trace(">>> ECHEC de l'ordre d'achat: " .. (message or ""));
        end
    elseif cookie == 200 then
        if success then
            core.host:trace(">>> Ordre de fermeture EXECUTE avec succes");
        else
            core.host:trace(">>> ECHEC de la fermeture: " .. (message or ""));
        end
    end
end


-- =============================================================================
-- CHARGEMENT DE LA BIBLIOTHEQUE STANDARD (helper.lua)
--
-- IMPORTANT: Cette ligne charge les fonctions utilitaires fournies par
-- Trading Station (ExtSubscribe, ExtUpdate, ExtAsyncOperationFinished, etc.)
-- Elle DOIT etre a la fin du fichier.
--
-- Si Trading Station affiche une erreur "helper.lua not found", verifiez
-- que ce dossier existe:
-- C:\Program Files (x86)\Candleworks\FXTS2\strategies\standard\include\
-- =============================================================================
dofile(core.app_path() .. "\\strategies\\standard\\include\\helper.lua");
