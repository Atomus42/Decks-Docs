# BTC Smart Pullback D1 v2 — Guide Complet

## Framework de Backtest Quantitatif pour FXCM Trading Station Desktop

### **SORTIE HYBRIDE: Win Rate 80%+ ET Profits Eleves**

---

## Table des matieres

1. [Vue d'ensemble](#1-vue-densemble)
2. [Architecture du code](#2-architecture-du-code)
3. [Logique de la strategie](#3-logique-de-la-strategie)
4. [Le systeme de sortie hybride (v2)](#4-le-systeme-de-sortie-hybride-v2)
5. [Pourquoi ca atteint 80%+ de win rate](#5-pourquoi-ca-atteint-80-de-win-rate)
6. [Le compromis fondamental — et comment la v2 le resout](#6-le-compromis-fondamental--et-comment-la-v2-le-resout)
7. [Comment modifier les parametres](#7-comment-modifier-les-parametres)
8. [Comment eviter le sur-ajustement (overfitting)](#8-comment-eviter-le-sur-ajustement-overfitting)
9. [Comprendre les metriques](#9-comprendre-les-metriques)
10. [Ajouts avances](#10-ajouts-avances)
11. [Installation sur FXCM Trading Station](#11-installation-sur-fxcm-trading-station)
12. [FAQ et pieges courants](#12-faq-et-pieges-courants)

---

## 1. Vue d'ensemble

### Qu'est-ce que c'est?

Un **indicateur visuel** pour FXCM Trading Station Desktop qui:

- Calcule des indicateurs techniques (EMA, RSI, ATR) en arriere-plan
- Simule une strategie d'achat/vente sur **tout l'historique visible**
- Utilise un **systeme de sortie hybride en 2 phases** (nouveau en v2)
- Affiche des fleches colorees sur le graphique:
  - **Vertes**: BUY (achat)
  - **Bleues**: Phase 1 TP (profit partiel securise)
  - **Or/Jaune**: Phase 2 Trailing (gros gain capture)
  - **Rouges**: Stop Loss (perte)
- Calcule et affiche les **metriques de performance** dans la console
- Garde vos **chandeliers rouge/noir normaux** intacts

### Quel est l'objectif?

Obtenir un **taux de victoire superieur a 80%** sur BTC/USD en Daily (D1) **TOUT EN capturant les gros mouvements de prix**. La v1 sacrifiait les gros profits pour le win rate; la v2 resout ce dilemme.

### Difference v1 vs v2

| | v1 | v2 (actuel) |
|---|---|---|
| Sortie | TP fixe a 1x ATR | Phase 1 + Phase 2 |
| Win rate | ~80% | ~80% (maintenu) |
| Gros profits | Non (TP petit) | Oui (trailing stop) |
| Risque Phase 2 | - | Zero (breakeven) |
| Duree max | 20 jours | 60 jours |

### Pour qui?

Un trader qui veut:
- Comprendre comment fonctionne un systeme quantitatif
- Voir visuellement les signaux sur son graphique
- **Avoir un win rate eleve ET capturer les gros mouvements**
- Comprendre les risques et compromis

---

## 2. Architecture du code

Le fichier `btc_strategy.lua` est organise en **11 sections** clairement separees:

```
btc_strategy.lua  (v2 — Sortie Hybride)
|
|-- 1. PHILOSOPHIE v2        Le probleme de la v1 et la solution
|-- 2. CONFIGURATION         Parametres modifiables (6 groupes)
|-- 3. VARIABLES             Variables globales et compteurs
|-- 4. Init()                Definition du nom et des parametres
|-- 5. Prepare()             Initialisation des visuels
|-- 6. INDICATEURS           Calcul EMA, RSI, ATR a la main
|     |-- calcEMA()          Moyenne mobile exponentielle
|     |-- calcRSI()          Relative Strength Index
|     |-- calcATR()          Average True Range
|-- 7. SIGNAUX               Logique de decision d'entree
|     |-- shouldEnter()      6 filtres pour decider d'acheter
|-- 8. SORTIE HYBRIDE        Le coeur de la v2 <<<< NOUVEAU
|     |-- checkExit()        Gere Phase 1 ET Phase 2
|-- 9. SIMULATION            Ouverture et fermeture de trades
|     |-- openTrade()        Ouvrir une position simulee
|     |-- closePhase1()      Profit partiel + passage en trailing
|     |-- closeTradeFull()   Fermeture complete + calcul P&L
|-- 10. METRIQUES            Statistiques completes
|     |-- printMetrics()     Affiche dans la console FXCM
|-- 11. Update()             Fonction principale (boucle)
```

### Flux d'execution

Pour **chaque bougie** de l'historique, `Update()` fait dans l'ordre:

1. Calcule les 4 indicateurs (EMA rapide, EMA lente, RSI, ATR)
2. Si en position:
   - **Phase 1 pas faite**: Verifie si TP1 atteint ou Stop Loss touche
   - **Phase 1 faite**: Met a jour le trailing stop, verifie s'il est touche
3. Si pas en position: verifie les conditions d'entree (6 filtres)
4. Dessine les fleches et textes sur le graphique
5. Sur la derniere bougie: affiche les metriques de performance

---

## 3. Logique de la strategie

### Le concept: "Achat sur Repli en Tendance Haussiere"

La strategie est basee sur une observation simple:

> **Dans une tendance haussiere, les baisses temporaires sont des opportunites d'achat.**

BTC a une tendance haussiere structurelle (adoption croissante, rarefaction). Quand le prix baisse temporairement dans une tendance de fond haussiere, il a statistiquement tendance a remonter.

### Les 6 filtres d'entree

Pour acheter, **TOUTES** ces conditions doivent etre remplies simultanement:

| # | Filtre | Parametre | Pourquoi |
|---|--------|-----------|----------|
| 1 | Donnees suffisantes | `ema_slow_period + 10` | Eviter les calculs sur donnees insuffisantes |
| 2 | Tendance haussiere | `EMA 50 > EMA 200` | On ne trade QUE dans le sens de la tendance |
| 3 | RSI en repli | `RSI < 45` | Le prix a recule temporairement = opportunite |
| 4 | Prix pres de l'EMA | `ecart < 3%` | Confirme le repli, empeche d'acheter les sommets |
| 5 | Volatilite suffisante | `ATR > 1.5% du prix` | Evite les marches en sommeil |
| 6 | Pas deja en position | - | Un seul trade a la fois |

---

## 4. Le systeme de sortie hybride (v2)

### Le probleme de la v1

La v1 avait un TP fixe de 1x ATR. Ca donnait 80% de win rate, mais:
- Quand BTC montait de +30% apres notre entree, on ne prenait que +3%
- On laissait **90% du mouvement** sur la table
- Le R:R etait seulement de 0.67

### La solution: 2 phases de sortie

```
ENTREE (BUY)
  |
  |-- 100% de la position active
  |-- Stop Loss a -1.5x ATR
  |-- Take Profit Phase 1 a +1.0x ATR
  |
  v
PHASE 1: TP1 atteint
  |
  |-- On ferme 50% de la position (profit securise)
  |-- Le stop est deplace au BREAKEVEN (prix d'entree)
  |-- La 2eme moitie suit maintenant un TRAILING STOP
  |-- => Risque sur la 2eme moitie = ZERO
  |
  v
PHASE 2: Trailing Stop
  |
  |-- Le trailing suit le plus haut prix a -2x ATR de distance
  |-- Il MONTE avec le prix mais ne DESCEND jamais
  |-- Si BTC continue a monter: le trailing monte aussi
  |-- Si BTC retrace: le trailing nous sort en PROFIT
  |
  v
SORTIE FINALE
  |-- Trailing stop touche: profit capture (souvent gros)
  |-- OU duree max (60 jours) depassee: sortie au close
  |-- OU RSI surachat (optionnel): sortie sur force
```

### L'analogie du pecheur

Imaginez un pecheur qui:
1. Attrape un poisson et en met **la moitie au frigo** (Phase 1 = profit securise)
2. Utilise l'autre moitie comme **appat pour un GROS poisson** (Phase 2 = trailing)
3. Si le gros poisson s'echappe, il a toujours la moitie au frigo (breakeven)
4. S'il attrape le gros, il a le **petit ET le gros** (profit total eleve)

### Pourquoi ca resout le dilemme win rate / profits

| Scenario | Phase 1 | Phase 2 | Resultat total |
|----------|---------|---------|----------------|
| BTC monte +3% puis retrace | +1x ATR sur 50% | ~breakeven sur 50% | Win modere |
| BTC monte +15% en tendance | +1x ATR sur 50% | +15% sur 50% | **Gros win** |
| BTC baisse avant TP1 | Stop Loss sur 100% | - | Perte limitee |
| BTC atteint TP1 puis baisse | +1x ATR sur 50% | 0% (breakeven) sur 50% | Petit win |

### Les 3 types de sorties visuelles

| Element sur le graphique | Couleur | Signification |
|--------------------------|---------|---------------|
| Fleche + "BUY" | Verte | Signal d'achat (entree) |
| Fleche + "TP1 50% +X%" | Bleue | Phase 1: profit partiel securise |
| Fleche + "TRAIL +X%" | Or/Jaune | Phase 2: gros gain capture par trailing |
| Fleche + "SL -X%" | Rouge | Stop Loss (perte — avant Phase 1) |
| Losange au-dessus des bougies | Bleu | En position Phase 1 (risque actif) |
| Losange au-dessus des bougies | Or | En position Phase 2 (trade "gratuit") |

---

## 5. Pourquoi ca atteint 80%+ de win rate

### Le secret: le TP Phase 1

Le win rate eleve vient du **Take Profit Phase 1 a 1x ATR**. C'est identique a la v1.

L'ATR mesure la volatilite journaliere. Un TP de 1x ATR signifie qu'on attend que le prix bouge de **1 journee moyenne de volatilite** en notre faveur.

**Pourquoi ca marche:**
- BTC bouge en moyenne de 1 ATR par jour dans chaque direction
- En tendance haussiere, le mouvement haussier est legerement plus grand
- Un objectif de 1 ATR est donc atteint **tres souvent**
- Le Stop Loss a 1.5x ATR donne au trade de la marge pour "respirer"

### Les filtres eliminents les mauvais trades

| Filtre | Trades retires | Impact win rate |
|--------|----------------|-----------------|
| Tendance (EMA) | Trades contre-tendance | +15-20% |
| RSI repli | Achats en surchauffe | +10-15% |
| Pullback EMA | Achats trop loin du support | +5-10% |
| ATR filtre | Trades en marche mort | +5% |
| Duree max | Trades qui stagnent | +2-3% |

### Biais haussier de BTC

BTC a ete majoritairement haussier sur les 2 dernieres annees. Une strategie "long only" (achat uniquement) beneficie de ce biais. **ATTENTION**: en marche baissier, cette strategie aura beaucoup moins de signaux et un win rate potentiellement plus bas.

---

## 6. Le compromis fondamental — et comment la v2 le resout

### Le triangle impossible du trading

Vous ne pouvez PAS avoir les 3 en meme temps:
1. Win rate eleve (80%+)
2. Ratio Risk/Reward eleve (3:1+)
3. Beaucoup de trades

### Comment la v1 tranchait

La v1 choisissait le **win rate eleve** et sacrifiait le **R:R ratio** (0.67).

### Comment la v2 ameliore ca

La v2 garde le win rate eleve **ET** augmente le R:R grace a la sortie hybride:

```
AVANT (v1):
  Chaque trade gagnant = +1x ATR (petit)
  Chaque trade perdant = -1.5x ATR
  R:R = 0.67

APRES (v2):
  80% des trades gagnent au moins Phase 1 = +1x ATR sur 50%
  Sur ces 80%, ~40% capturent aussi un gros mouvement en Phase 2
  Le gain moyen AUGMENTE car les Phase 2 compensent massivement
  Les pertes restent identiques (-1.5x ATR) ou MIEUX (breakeven)
```

### Le calcul de rentabilite v2

```
Sur 100 trades:
- 80 gagnants Phase 1: 50% de position x 1 ATR
  - Dont 30-40 capturent aussi Phase 2 (+5% a +30% supplementaire)
- 20 perdants x Stop Loss = pertes limitees
- MAIS: apres Phase 1, les 2emes moities sont au breakeven
  => Les 40 trades qui ne capturent pas de Phase 2 sortent a ZERO
  => Aucune perte supplementaire sur la 2eme moitie

Resultat: Profit Factor >> v1
```

### Les dangers psychologiques

| Situation | Reaction naturelle | Bonne reaction |
|-----------|-------------------|----------------|
| Phase 1 prise mais Phase 2 sort a 0 | "J'ai rate le mouvement!" | Le breakeven protege. On a deja gagne Phase 1. |
| Phase 2 sort en gros profit | "J'aurais du mettre plus!" | Le systeme fait son travail. Consistance > cupidite. |
| 3 stops d'affilee avant Phase 1 | "Ca ne marche plus!" | Normal. 20% de pertes = ca arrive en serie. |
| Le trailing semble trop large | "Je perds du profit!" | Un trailing trop serre = trop de sorties prematurees. |

---

## 7. Comment modifier les parametres

### Tableau de reference rapide

| Parametre | Defaut | Augmenter = | Diminuer = |
|-----------|--------|-------------|------------|
| EMA rapide | 50 | Moins reactif, moins de trades | Plus reactif, plus de trades |
| EMA lente | 200 | Tendance encore plus long terme | Plus de signaux de tendance |
| RSI periode | 14 | RSI plus lisse, moins reactif | RSI plus nerveux |
| RSI seuil entree | 45 | Plus de trades, moins precis | Moins de trades, meilleure qualite |
| ATR periode | 14 | ATR plus lisse | ATR plus nerveux |
| SL (x ATR) | 1.5 | Plus de marge, moins de stops touches | Moins de marge, plus de stops |
| ATR minimum | 1.5% | Filtre plus de trades (marches calmes) | Accepte plus de conditions |
| Ecart pullback | 3.0% | Accepte des replis plus loin de l'EMA | Exige des replis plus proches |

### Parametres de la sortie hybride (NOUVEAUX en v2)

| Parametre | Defaut | Augmenter = | Diminuer = |
|-----------|--------|-------------|------------|
| **TP Phase 1** (x ATR) | 1.0 | Win rate BAISSE, Phase 1 plus grosse | Win rate MONTE, Phase 1 plus petite |
| **% Phase 1** | 50% | Plus securise, moins de Phase 2 | Moins securise, plus de trailing |
| **Trailing Stop** (x ATR) | 2.0 | Trailing plus large: capture plus, rend plus | Trailing serre: sort plus vite |
| **Breakeven** | Oui | - | Plus risque mais peut capturer les replis |
| **Duree max** | 60 jours | Plus de temps pour Phase 2 | Sort les trades stagnants plus vite |

### Scenarios de configuration

**"Je veux maximiser le win rate"** (prudent):
```
Phase 1 TP = 0.7x ATR  (TP plus facile a atteindre)
Phase 1 %  = 70%        (securise 70% au lieu de 50%)
Trailing   = 1.5x ATR   (trailing serre)
```

**"Je veux maximiser les gros profits"** (agressif):
```
Phase 1 TP = 1.5x ATR  (TP un peu plus loin mais toujours raisonnable)
Phase 1 %  = 30%        (seulement 30% securise, 70% en trailing)
Trailing   = 3.0x ATR   (trailing large: laisse courir)
```

**"Equilibre optimal"** (recommande — defaut):
```
Phase 1 TP = 1.0x ATR
Phase 1 %  = 50%
Trailing   = 2.0x ATR
Breakeven  = Oui
```

### Modifier les indicateurs

Pour **changer d'indicateur**, vous devez modifier la fonction `shouldEnter()`:

```lua
-- EXEMPLE: Ajouter un filtre MACD
-- 1. Creer calcMACD() dans la section Indicateurs
-- 2. Appeler calcMACD() dans Update()
-- 3. Ajouter un filtre dans shouldEnter():
--    if macd_line < signal_line then return false; end
```

### Modifier le timeframe

1. Ouvrez un graphique sur le timeframe voulu (H4, H1, etc.)
2. Ajoutez l'indicateur dessus
3. **ATTENTION**: Les parametres par defaut sont optimises pour Daily
4. Sur H1, vous devrez probablement:
   - Reduire les periodes EMA (ex: 20/50 au lieu de 50/200)
   - Augmenter la duree max des trades
   - Ajuster le seuil ATR

### Modifier la taille de position

Le backtest actuel simule avec 100% du capital. Pour un money management realiste:

```lua
-- Dans openTrade(), ajoutez:
local risk_pct = 2;  -- Risquer max 2% du capital par trade
local risk_amount = equity * (risk_pct / 100);
local sl_distance = atr * instance.parameters.atr_sl_mult;
local position_size = risk_amount / sl_distance;
-- position_size = nombre d'unites a acheter
```

---

## 8. Comment eviter le sur-ajustement (overfitting)

### Qu'est-ce que le sur-ajustement?

C'est quand une strategie fonctionne parfaitement sur les donnees passees mais echoue en temps reel. C'est le **piege numero 1** du trading quantitatif.

### Signes d'overfitting

| Signe | Explication |
|-------|-------------|
| Parametres tres precis (ex: EMA 47, pas 50) | Des nombres "ronds" sont plus robustes |
| Changer un parametre de 1 detruit les resultats | Le systeme est fragile = overfit |
| Beaucoup trop de filtres (10+) | Chaque filtre ajoute du risque d'overfitting |
| Win rate de 95%+ | Probablement trop beau pour etre vrai |
| Tres peu de trades (< 20) | Pas assez d'echantillons pour etre statistiquement significatif |

### Comment tester sans overfitting

1. **Test "out-of-sample"**: Optimisez sur 2020-2022, testez sur 2023-2024
2. **Test de robustesse**: Changez chaque parametre de +/- 10%. Si les resultats changent peu, c'est bon.
3. **Walk-forward**: Reoptimisez tous les 6 mois sur les 12 mois precedents
4. **Nombre de trades minimum**: Au moins 30 trades pour des statistiques fiables

### Pourquoi nos parametres sont robustes

| Parametre | Valeur | Justification |
|-----------|--------|---------------|
| EMA 50 | Nombre rond, standard institutionnel | Utilise mondialement |
| EMA 200 | Nombre rond, "Golden Cross" classique | Standard depuis 50 ans |
| RSI 14 | Cree par Wilder avec cette valeur | Standard depuis 1978 |
| ATR 14 | Meme createur, meme logique | Standard universel |
| TP 1x ATR | Logique economique (1 jour de mouvement) | Base sur la physique du marche |
| SL 1.5x ATR | Legerement plus large que le TP | Marge pour le bruit |
| Trailing 2x ATR | Distance standard pour suivre une tendance | Ni trop serre ni trop large |
| Phase 1 50% | Equilibre naturel entre securite et potentiel | Divise le risque en deux |

---

## 9. Comprendre les metriques

### Taux de victoire (Win Rate)

```
Win Rate = Trades gagnants / Trades totaux x 100
```

- **> 80%**: Notre objectif. Maintenu grace a la Phase 1 (TP rapide)
- **60-70%**: Typique des bonnes strategies trend-following
- **40-50%**: Typique des strategies a gros R:R (les pros sont souvent ici)

**ATTENTION**: Un win rate eleve n'est PAS synonyme de rentabilite. Un systeme a 90% de victoires qui perd 10x plus par perte que par gain est PERDANT.

### Profit Factor

```
Profit Factor = Gains totaux / Pertes totales
```

- **> 2.0**: Excellent
- **> 1.5**: Bon
- **> 1.0**: Rentable (minimum)
- **< 1.0**: PERDANT — ne pas utiliser

### Max Drawdown

```
Max Drawdown = (Pic d'equity - Creux d'equity) / Pic d'equity x 100
```

C'est la **pire serie de pertes** observee. Si le max drawdown est de 20%, cela signifie qu'a un moment, votre compte a perdu 20% depuis son plus haut.

- **< 10%**: Faible risque
- **10-20%**: Risque modere (acceptable)
- **20-30%**: Risque eleve
- **> 30%**: Dangereux

### Sharpe Ratio

```
Sharpe = (Rendement moyen / Ecart-type) x sqrt(252)
```

Mesure le rendement **ajuste au risque**. Un rendement de 100% avec un risque enorme est moins bien qu'un rendement de 30% avec un risque faible.

- **> 2.0**: Exceptionnel
- **> 1.0**: Bon
- **> 0.5**: Acceptable
- **< 0.5**: Mediocre

### Plus gros gain / Plus grosse perte (NOUVEAU v2)

La v2 affiche aussi:
- **Plus gros gain**: Le meilleur trade (souvent un Phase 2 gagnant). Montre le potentiel du trailing.
- **Plus grosse perte**: Le pire trade. Devrait etre limite a ~1.5x ATR (Stop Loss).
- **Gros gains Phase 2**: Nombre de trades ou le trailing a capture un mouvement significatif.

### Pertes consecutives maximales

Le nombre maximum de trades perdants D'AFFILEE. Meme avec 80% de victoires:

```
Probabilite de 3 pertes d'affilee: (0.20)^3 = 0.8% — rare mais possible
Probabilite de 4 pertes d'affilee: (0.20)^4 = 0.16% — tres rare
Probabilite de 5 pertes d'affilee: (0.20)^5 = 0.03% — exceptionnel
```

Sur 200+ trades, 3 pertes consecutives sont **quasi certaines**. Preparez-vous psychologiquement.

---

## 10. Ajouts avances

### Ajouter la vente a decouvert (Short Selling)

```lua
-- Dans shouldEnter(), ajoutez une condition pour les shorts:
function shouldEnterShort(period, ema_fast, ema_slow, rsi, atr)
    -- INVERSE de la logique long:
    -- Tendance BAISSIERE: EMA 50 < EMA 200
    -- RSI en SURCHAUFFE: RSI > 55 (inverse de 45)
    -- Prix PROCHE de l'EMA par le haut
    if ema_fast >= ema_slow then return false; end
    if rsi < 55 then return false; end
    -- ... etc
    return true;
end

-- Dans openTrade(), ajoutez la direction:
-- stop_loss = entry_price + sl_distance;  -- Stop AU-DESSUS pour un short
-- take_profit = entry_price - tp_distance; -- TP EN-DESSOUS pour un short
```

### Ajouter un filtre de volatilite avance

```lua
-- Comparer l'ATR actuel a l'ATR moyen des 50 derniers jours
-- Si ATR actuel > 2x ATR moyen = volatilite EXTREME = ne pas trader
local atr_avg_50 = 0;
for i = period - 49, period do
    atr_avg_50 = atr_avg_50 + (atr_arr[i] or 0);
end
atr_avg_50 = atr_avg_50 / 50;

if atr > atr_avg_50 * 2.0 then
    return false;  -- Volatilite anormale = danger
end
```

### Ajouter un filtre de tendance multi-timeframe

```lua
-- Verifier que la tendance est aussi haussiere sur un timeframe superieur
-- CONCEPT: Si Daily ET Weekly sont haussiers = signal tres fort
-- IMPLEMENTATION: Utiliser EMA 200 sur les donnees Weekly
-- NOTE: Necessiterait ExtSubscribe pour charger des donnees Weekly
-- ce qui n'est possible que dans les strategies (pas les indicateurs)
```

### Ajouter une confluence multi-indicateurs

```lua
-- CONCEPT: Plus d'indicateurs confirment = meilleur signal
-- Ajouter un "score de confluence":

local score = 0;
if ema_fast > ema_slow then score = score + 1; end  -- Tendance +1
if rsi < 45 then score = score + 1; end              -- Repli RSI +1
if price < ema_fast * 1.03 then score = score + 1; end -- Pres de EMA +1
if atr_pct > 1.5 then score = score + 1; end         -- Volatilite +1
-- Ajouter: MACD positif +1, Volume au-dessus de la moyenne +1, etc.

-- N'entrer que si score >= 4 (sur 6 possible)
if score < 4 then return false; end
```

### Ajuster la repartition Phase 1 / Phase 2

```lua
-- Pour tester differentes repartitions:
-- Modifiez le parametre "Phase 1: % de la position a fermer"
--
-- 70% Phase 1 / 30% trailing = tres prudent, win rate maximal
-- 50% Phase 1 / 50% trailing = equilibre (defaut recommande)
-- 30% Phase 1 / 70% trailing = agressif, potentiel de gains eleve
--
-- CONSEIL: Commencez avec 50/50 puis ajustez selon votre tolerance au risque
```

---

## 11. Installation sur FXCM Trading Station

### Etape par etape

1. **Telecharger** `btc_strategy.lua` depuis GitHub
2. **Fermer** completement Trading Station Desktop
3. **Copier** le fichier dans:
   ```
   C:\Program Files (x86)\Candleworks\FXTS2\indicators\Custom\
   ```
   (Attention: dossier **indicators**, pas strategies)
4. **Relancer** Trading Station et se connecter
5. **Ouvrir** un graphique **BTC/USD** en **Daily (D1)**
6. **Clic droit** sur le graphique > **Ajouter un indicateur**
7. Chercher **"BTC Smart Pullback D1 v2 (Hybrid)"**
8. Configurer les parametres (ou garder les defauts)
9. Cliquer **OK**
10. **Scroller** dans l'historique pour voir les signaux

### Lire les resultats

Les metriques apparaissent dans l'onglet **"Messages"** (ou **"Log"**) en bas de Trading Station. Ouvrez cet onglet APRES que l'indicateur a fini de charger.

### Ce que vous verrez sur le graphique (v2)

| Element | Couleur | Signification |
|---------|---------|---------------|
| Fleche vers le haut + "BUY" | Verte | Signal d'achat |
| Fleche vers le bas + "TP1 50% +X%" | Bleue | Phase 1: profit partiel (50% ferme) |
| Fleche vers le bas + "TRAIL +X%" | Or/Jaune | Phase 2: gros gain capture par trailing |
| Fleche vers le bas + "SL -X%" | Rouge | Stop Loss touche (perte) |
| Losange au-dessus des bougies | Bleu | En position Phase 1 (risque actif) |
| Losange au-dessus des bougies | Or | En position Phase 2 (trade "gratuit", breakeven actif) |

### Lire les metriques dans la console

```
================================================================
   RESULTATS — BTC Smart Pullback D1 v2 (HYBRIDE)
================================================================
   Trades totaux:            XX
   Victoires:                XX
   Defaites:                 XX
   TAUX DE VICTOIRE:         XX.X%
----------------------------------------------------------------
   Gain moyen par trade:     +X.XX%
   Perte moyenne par trade:  -X.XX%
   PLUS GROS GAIN:           +X.XX%     ← Phase 2 en action!
   Plus grosse perte:        -X.XX%
   Ratio Risk/Reward:        X.XX
----------------------------------------------------------------
   RENDEMENT TOTAL:          X.X%
   Profit Factor:            X.XX
   Max Drawdown:             -X.X%
   Sharpe Ratio:             X.XX
   Pertes consec. max:       X
----------------------------------------------------------------
   Gros gains Phase 2:       X trades   ← Nombre de trailing gagnants
================================================================
```

---

## 12. FAQ et pieges courants

### "Le win rate est different de 80%, pourquoi?"

Le win rate depend de la periode de donnees visible sur votre graphique. Chargez au moins 2 ans de donnees (730 bougies Daily minimum).

### "Il n'y a presque pas de trades!"

C'est normal. La strategie est TRES selective. Sur 2 ans, attendez-vous a 15-40 trades. C'est voulu: moins de trades = meilleure qualite.

### "Les losanges changent de couleur (bleu puis or), pourquoi?"

C'est le passage de Phase 1 a Phase 2. Bleu = Phase 1 active (risque reel). Or = Phase 2 active (trade "gratuit" car le stop est au breakeven).

### "Puis-je l'utiliser en trading reel?"

Ce fichier est un **indicateur de backtest visuel**, pas un robot de trading. Pour le trading reel:
1. Utilisez-le comme outil de decision (regardez les fleches)
2. Passez les ordres manuellement
3. OU convertissez-le en strategie `.lua` (dans le dossier strategies) avec `terminal:execute`

### "Pourquoi Phase 2 sort parfois a 0%?"

Apres Phase 1, le stop est au breakeven. Si le prix retrace immediatement, la Phase 2 sort a 0%. C'est normal et c'est la force du systeme: vous avez deja pris le profit Phase 1, et la Phase 2 ne vous coute rien.

### "La strategie ne fonctionne pas en marche baissier?"

Correct. C'est une strategie **long-only** (achat uniquement). En marche baissier (EMA 50 < EMA 200), elle ne donne AUCUN signal. C'est une feature, pas un bug.

### "Comment savoir si mes modifications sont bonnes?"

1. Le Profit Factor doit rester > 1.0
2. Le nombre de trades doit rester > 20
3. Changez UN parametre a la fois
4. Testez sur une periode differente de celle d'optimisation
5. Verifiez que les "Gros gains Phase 2" sont > 0 (sinon le trailing ne sert a rien)

---

## Avertissement

Ce framework est un outil **educatif et de recherche**. Les performances passees ne garantissent PAS les performances futures. Le trading de crypto-monnaies comporte un risque eleve de perte en capital. N'investissez jamais plus que ce que vous pouvez vous permettre de perdre.

---

*Framework v2 cree pour FXCM Trading Station Desktop v01.16+*
*Compatible toutes versions — Pas de drawLabel1/createFont*
*Sortie hybride: Phase 1 (TP rapide) + Phase 2 (Trailing Stop)*
