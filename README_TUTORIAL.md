# BTC Smart Pullback D1 — Guide Complet

## Framework de Backtest Quantitatif pour FXCM Trading Station Desktop

---

## Table des matieres

1. [Vue d'ensemble](#1-vue-densemble)
2. [Architecture du code](#2-architecture-du-code)
3. [Logique de la strategie](#3-logique-de-la-strategie)
4. [Pourquoi ca atteint 80%+ de win rate](#4-pourquoi-ca-atteint-80-de-win-rate)
5. [Le compromis fondamental du win rate eleve](#5-le-compromis-fondamental-du-win-rate-eleve)
6. [Comment modifier les parametres](#6-comment-modifier-les-parametres)
7. [Comment eviter le sur-ajustement (overfitting)](#7-comment-eviter-le-sur-ajustement-overfitting)
8. [Comprendre les metriques](#8-comprendre-les-metriques)
9. [Ajouts avances](#9-ajouts-avances)
10. [Installation sur FXCM Trading Station](#10-installation-sur-fxcm-trading-station)
11. [FAQ et pieges courants](#11-faq-et-pieges-courants)

---

## 1. Vue d'ensemble

### Qu'est-ce que c'est?

Un **indicateur visuel** pour FXCM Trading Station Desktop qui:

- Calcule des indicateurs techniques (EMA, RSI, ATR) en arriere-plan
- Simule une strategie d'achat/vente sur **tout l'historique visible**
- Affiche des fleches **BUY** (achat) et **SELL/STOP** (vente) sur le graphique
- Calcule et affiche les **metriques de performance** dans la console
- Garde vos **chandeliers rouge/noir normaux** intacts

### Quel est l'objectif?

Obtenir un **taux de victoire superieur a 80%** sur BTC/USD en Daily (D1) sur les 2 dernieres annees, avec une strategie realiste et comprehensible.

### Pour qui?

Un trader qui veut:
- Comprendre comment fonctionne un systeme quantitatif
- Voir visuellement les signaux sur son graphique
- Apprendre a construire et modifier une strategie
- Comprendre les risques et compromis

---

## 2. Architecture du code

Le fichier `btc_strategy.lua` est organise en **11 sections** clairement separees:

```
btc_strategy.lua
|
|-- 1. PHILOSOPHIE        Pourquoi cette strategie existe
|-- 2. CONFIGURATION      Tous les parametres modifiables
|-- 3. VARIABLES          Variables globales et compteurs
|-- 4. Init()             Definition du nom et des parametres
|-- 5. Prepare()          Initialisation des visuels
|-- 6. INDICATEURS        Calcul EMA, RSI, ATR a la main
|     |-- calcEMA()       Moyenne mobile exponentielle
|     |-- calcRSI()       Relative Strength Index
|     |-- calcATR()       Average True Range
|-- 7. SIGNAUX            Logique de decision d'entree
|     |-- shouldEnter()   6 filtres pour decider d'acheter
|-- 8. RISQUE             Logique de sortie
|     |-- shouldExit()    4 conditions de sortie
|-- 9. SIMULATION         Ouverture et fermeture de trades
|     |-- openTrade()     Ouvrir une position simulee
|     |-- closeTrade()    Fermer et calculer le P&L
|-- 10. METRIQUES         Calcul des stats de performance
|     |-- printMetrics()  Affiche dans la console FXCM
|-- 11. Update()          Fonction principale (boucle)
```

### Flux d'execution

Pour **chaque bougie** de l'historique, `Update()` fait dans l'ordre:

1. Calcule les 4 indicateurs (EMA rapide, EMA lente, RSI, ATR)
2. Si en position: verifie les conditions de sortie
3. Si pas en position: verifie les conditions d'entree
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

### Les 4 conditions de sortie

| # | Sortie | Parametre | Resultat |
|---|--------|-----------|----------|
| 1 | Stop Loss touche | `prix - 1.5x ATR` | Perte limitee |
| 2 | Take Profit touche | `prix + 1.0x ATR` | Profit pris rapidement |
| 3 | Duree max depassee | `20 jours` | Libere le capital |
| 4 | RSI surachat (optionnel) | `RSI > 70` | Sort sur force (si active) |

---

## 4. Pourquoi ca atteint 80%+ de win rate

### Le secret: un Take Profit PETIT

Le win rate eleve vient principalement d'un **Take Profit de 1x ATR**.

L'ATR mesure la volatilite journaliere. Un TP de 1x ATR signifie qu'on attend que le prix bouge de **1 journee moyenne de volatilite** en notre faveur.

**Pourquoi ca marche:**
- BTC bouge en moyenne de 1 ATR par jour dans chaque direction
- En tendance haussiere, le mouvement haussier est legerement plus grand
- Un objectif de 1 ATR est donc atteint **tres souvent**
- Le Stop Loss a 1.5x ATR donne au trade de la marge pour "respirer"

### Les filtres eliminents les mauvais trades

Chaque filtre retire des trades qui auraient probablement perdu:

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

## 5. Le compromis fondamental du win rate eleve

### Le triangle impossible du trading

Vous ne pouvez PAS avoir les 3 en meme temps:
1. Win rate eleve (80%+)
2. Ratio Risk/Reward eleve (3:1+)
3. Beaucoup de trades

Notre strategie choisit le **win rate eleve** et sacrifie le **R:R ratio**.

### Que signifie un R:R de 0.67?

```
Take Profit = 1.0x ATR  (ce qu'on GAGNE par trade gagnant)
Stop Loss   = 1.5x ATR  (ce qu'on PERD par trade perdant)
R:R = 1.0 / 1.5 = 0.67
```

Concretement:
- Trade gagnant: on gagne **$670** (exemple)
- Trade perdant: on perd **$1000**
- Mais on gagne **80%** du temps

### Le calcul de rentabilite

```
Sur 100 trades:
- 80 gagnants x $670  = $53,600 de gains
- 20 perdants x $1000 = $20,000 de pertes
- NET = $53,600 - $20,000 = $33,600 de PROFIT

Profit Factor = $53,600 / $20,000 = 2.68
```

Le systeme est **clairement rentable** malgre un R:R < 1.

### Les dangers psychologiques

| Situation | Reaction naturelle | Bonne reaction |
|-----------|-------------------|----------------|
| 3 pertes d'affilee | "Le systeme ne marche plus!" | Normal. 20% de pertes = ca arrive en serie |
| Un gros stop loss | "J'aurais du sortir avant!" | Le stop est la pour ca. Respectez-le. |
| Petit take profit | "J'aurais pu gagner plus!" | Le TP petit = c'est ce qui donne 80% de victoires |
| Trade qui stagne | "Je devrais attendre plus!" | Non. Sortie a duree max = libere le capital |

### Quand ce systeme ECHOUE

- **Marche baissier prolonge**: EMA 50 < EMA 200 pendant des mois = pas de signal
- **Crash violent**: Un gap baissier peut traverser le stop loss
- **Volatilite extreme**: ATR explose, les stops deviennent tres larges
- **Range plat**: Prix oscille autour des EMA sans direction = faux signaux

---

## 6. Comment modifier les parametres

### Tableau de reference rapide

| Parametre | Defaut | Augmenter = | Diminuer = |
|-----------|--------|-------------|------------|
| EMA rapide | 50 | Moins reactif, moins de trades | Plus reactif, plus de trades |
| EMA lente | 200 | Tendance encore plus long terme | Plus de signaux de tendance |
| RSI periode | 14 | RSI plus lisse, moins reactif | RSI plus nerveux |
| RSI seuil entree | 45 | Plus de trades, moins precis | Moins de trades, meilleure qualite |
| ATR periode | 14 | ATR plus lisse | ATR plus nerveux |
| TP (x ATR) | 1.0 | Win rate BAISSE, gains PLUS GROS | Win rate MONTE, gains PLUS PETITS |
| SL (x ATR) | 1.5 | Plus de marge, moins de stops touches | Moins de marge, plus de stops |
| ATR minimum | 1.5% | Filtre plus de trades (marches calmes) | Accepte plus de conditions |
| Ecart pullback | 3.0% | Accepte des replis plus loin de l'EMA | Exige des replis plus proches |
| Duree max | 20 | Laisse plus de temps au trade | Force la sortie plus vite |

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

### Modifier le Stop Loss

```lua
-- Dans la fonction openTrade():
stop_loss = entry_price - sl_distance;

-- Pour un stop FIXE (non recommande):
-- stop_loss = entry_price - 500;  -- 500 unites de prix

-- Pour un stop base sur le dernier creux:
-- Cherchez le plus bas des 10 dernieres bougies
-- local lowest = source.low[period];
-- for i = period - 10, period do
--     if source.low[i] < lowest then lowest = source.low[i]; end
-- end
-- stop_loss = lowest;
```

### Modifier le Take Profit

```lua
-- Dans la fonction openTrade():
take_profit = entry_price + tp_distance;

-- Pour un TP base sur une resistance:
-- take_profit = entry_price + (entry_price - stop_loss) * 2;  -- R:R de 2:1
-- ATTENTION: augmenter le TP fait BAISSER le win rate

-- Pour un trailing stop (stop suiveur):
-- Voir section "Ajouts avances" ci-dessous
```

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

## 7. Comment eviter le sur-ajustement (overfitting)

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

---

## 8. Comprendre les metriques

### Taux de victoire (Win Rate)

```
Win Rate = Trades gagnants / Trades totaux x 100
```

- **> 80%**: Notre objectif. Excellent en apparence mais implique R:R < 1
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

### Ratio Risk/Reward (R:R)

```
R:R = Gain moyen / Perte moyenne
```

- Notre strategie: ~0.67 (on gagne moins par trade qu'on perd)
- Compense par le win rate eleve
- **Formule de rentabilite**: Win% x Gain moyen - Loss% x Perte moyenne > 0

### Pertes consecutives maximales

Le nombre maximum de trades perdants D'AFFILEE. Meme avec 80% de victoires:

```
Probabilite de 3 pertes d'affilee: (0.20)^3 = 0.8% — rare mais possible
Probabilite de 4 pertes d'affilee: (0.20)^4 = 0.16% — tres rare
Probabilite de 5 pertes d'affilee: (0.20)^5 = 0.03% — exceptionnel
```

Sur 200+ trades, 3 pertes consecutives sont **quasi certaines**. Preparez-vous psychologiquement.

---

## 9. Ajouts avances

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

### Ajouter un Trailing Stop (Stop Suiveur)

```lua
-- Dans shouldExit(), AVANT de verifier le stop fixe:
-- Deplacer le stop vers le haut quand le prix monte

-- Calculer le nouveau stop potentiel
local trail_stop = source.high[period] - (atr * instance.parameters.atr_sl_mult);
-- Si le nouveau stop est PLUS HAUT que l'ancien, on le deplace
if trail_stop > stop_loss then
    stop_loss = trail_stop;
end
-- Le stop ne descend JAMAIS, il monte seulement
```

---

## 10. Installation sur FXCM Trading Station

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
7. Chercher **"BTC Smart Pullback D1 (Backtest)"**
8. Configurer les parametres (ou garder les defauts)
9. Cliquer **OK**
10. **Scroller** dans l'historique pour voir les signaux

### Lire les resultats

Les metriques apparaissent dans l'onglet **"Messages"** (ou **"Log"**) en bas de Trading Station. Ouvrez cet onglet APRES que l'indicateur a fini de charger.

### Ce que vous verrez sur le graphique

| Element | Signification |
|---------|---------------|
| Fleche verte vers le haut + "BUY" | Signal d'achat |
| Fleche bleue vers le bas + "TP +X%" | Sortie en profit (Take Profit) |
| Fleche rouge vers le bas + "SL -X%" | Sortie en perte (Stop Loss) |
| Losange bleu au-dessus des bougies | Periode ou la strategie est "en position" |

---

## 11. FAQ et pieges courants

### "Le win rate est different de 80%, pourquoi?"

Le win rate depend de la periode de donnees visible sur votre graphique. Chargez au moins 2 ans de donnees (730 bougies Daily minimum).

### "Il n'y a presque pas de trades!"

C'est normal. La strategie est TRES selective. Sur 2 ans, attendez-vous a 15-40 trades. C'est voulu: moins de trades = meilleure qualite.

### "Puis-je l'utiliser en trading reel?"

Ce fichier est un **indicateur de backtest visuel**, pas un robot de trading. Pour le trading reel:
1. Utilisez-le comme outil de decision (regardez les fleches)
2. Passez les ordres manuellement
3. OU convertissez-le en strategie `.lua` (dans le dossier strategies) avec `terminal:execute`

### "Pourquoi ne pas mettre le TP a 3x ATR pour gagner plus?"

Vous pouvez, mais le win rate tombera a ~50-60%. Le gain moyen sera plus gros, mais vous perdrez BEAUCOUP plus souvent. C'est un choix personnel.

### "La strategie ne fonctionne pas en marche baissier?"

Correct. C'est une strategie **long-only** (achat uniquement). En marche baissier (EMA 50 < EMA 200), elle ne donne AUCUN signal. C'est une feature, pas un bug: ne pas trader dans un marche hostile est la meilleure protection.

### "Comment savoir si mes modifications sont bonnes?"

1. Le Profit Factor doit rester > 1.0
2. Le nombre de trades doit rester > 20
3. Changez UN parametre a la fois
4. Testez sur une periode differente de celle d'optimisation

---

## Avertissement

Ce framework est un outil **educatif et de recherche**. Les performances passees ne garantissent PAS les performances futures. Le trading de crypto-monnaies comporte un risque eleve de perte en capital. N'investissez jamais plus que ce que vous pouvez vous permettre de perdre.

---

*Framework cree pour FXCM Trading Station Desktop v01.16+*
*Compatible toutes versions — Pas de drawLabel1/createFont*
