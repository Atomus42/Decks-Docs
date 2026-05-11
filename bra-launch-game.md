# MISSION: CATALYSIS — Le Jeu de Lancement BRA Platform

> **Format:** Atelier gamifié de 3h (ou 2 x 1h30)
> **Joueurs:** Romain, Carlo, Erik, Vassili, Charbel, Jeff (+Tom en sponsor/jury)
> **Output réel:** Plan de lancement validé, engagements signés, risques assumés
> **Matériel:** 1 plateau imprimé (ce doc), cartes découpées, post-its, chrono, 1 dé à 6 faces

---

## CONCEPT

Le jeu simule les 7 semaines de lancement en 7 rounds accélérés. Chaque round = 1 semaine. L'équipe coopère pour atteindre **$500k ARR** avant la fin du Round 7. Si le score collectif atteint le seuil, **tout le monde gagne**. Sinon, le Chaos Board a gagné.

> C'est un jeu **coopératif** — pas de compétition entre joueurs.
> Mais chaque joueur a des **engagements personnels** qui alimentent le score collectif.

---

## PLATEAU DE JEU

```
 ┌──────────────────────────────────────────────────────────────┐
 │                    MISSION: CATALYSIS                        │
 │                                                              │
 │   SYNTHESIS          REACTION              CATALYSIS         │
 │   ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐   │
 │   │ S1  │→ │ S2  │→ │ R3  │→ │ R4  │→ │ C6  │→ │ C7  │   │
 │   │     │  │     │  │     │  │  R5  │  │     │  │     │   │
 │   └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘   │
 │                                                              │
 │   ┌──────────────────────────────────────────────────────┐   │
 │   │  SCORE COLLECTIF: _____ / $500k ARR                  │   │
 │   │  PIPELINE:        _____ / $1.2M                      │   │
 │   │  HEALTH:          _____ / 100 pts                    │   │
 │   └──────────────────────────────────────────────────────┘   │
 │                                                              │
 │   CHAOS BOARD: [  ] [  ] [  ] [  ] [  ] (5 slots max)       │
 └──────────────────────────────────────────────────────────────┘
```

---

## RÔLES & POUVOIRS SPÉCIAUX

Chaque joueur reçoit une **Carte Rôle** avec un pouvoir spécial utilisable 1x par partie.

### Carte Rôle: ROMAIN — Le Closer
- **Zone:** Revenue + Pipeline
- **Pouvoir spécial (1x):** *"Mode 100%"* — Annule 1 carte Chaos liée au pipeline. Déclare: "Je drop tout, je ne fais que du pipe pendant 1 semaine."
- **Scoring perso:** +10 pts par deal avancé d'un stage, +50 pts pour un close

### Carte Rôle: CARLO — Le Hunter
- **Zone:** Outbound + Discovery
- **Pouvoir spécial (1x):** *"Blitz Week"* — Double les points de meetings bookés ce round
- **Scoring perso:** +5 pts par meeting booké, +10 pts par warm intro convertie

### Carte Rôle: ERIK — Le Sniper
- **Zone:** Outbound + Demos
- **Pouvoir spécial (1x):** *"Perfect Pitch"* — Un deal avance de 2 stages au lieu d'1 ce round
- **Scoring perso:** +5 pts par meeting booké, +15 pts par demo délivrée

### Carte Rôle: VASSILI — Le Sage
- **Zone:** KOL + Validation + Thérapeutique
- **Pouvoir spécial (1x):** *"KOL Express"* — Valide immédiatement 1 axe thérapeutique (skip le délai de validation)
- **Scoring perso:** +15 pts par KOL validé, +20 pts par case study complète

### Carte Rôle: CHARBEL — L'Architecte
- **Zone:** Plateforme + Démo + UX
- **Pouvoir spécial (1x):** *"Ship It"* — Déploie 1 Epic immédiatement (skip le round de dev)
- **Scoring perso:** +15 pts par Epic déployé, +10 pts si démo live OK

### Carte Rôle: JEFF — Le Gardien
- **Zone:** Infra + Fiabilité + Observabilité
- **Pouvoir spécial (1x):** *"Bouclier Infra"* — Bloque 1 carte Chaos liée à la fiabilité/bugs
- **Scoring perso:** +10 pts par palier uptime atteint (97%, 99%), +10 pts pour 0 bugs critiques

---

## CARTES CHAOS (imprimer, mélanger, tirer 1 par round)

Le Chaos représente les aléas du réel. Au début de chaque round, un joueur tire 1 carte Chaos. L'équipe doit décider comment réagir — ou utiliser un pouvoir spécial pour l'annuler.

| # | Carte Chaos | Effet | Peut être bloquée par |
|---|---|---|---|
| C1 | **"Le KOL annule"** | Vassili perd 1 tour de validation. Retard KOL de 1 round. | Vassili (KOL Express) |
| C2 | **"Bug critique en Prod"** | -10 pts Health. Charbel + Jeff doivent dédier 50% du round au fix. | Jeff (Bouclier Infra) |
| C3 | **"Le champion change de poste"** | 1 deal actif recule de 1 stage. Romain choisit lequel. | Erik (Perfect Pitch) |
| C4 | **"Pipeline sèche"** | Aucun nouveau meeting ce round sauf si Carlo/Erik trouvent 1 solution créative en 2 min. | Carlo (Blitz Week) |
| C5 | **"Scope creep client"** | 1 deal demande du custom. -15 pts si accepté. L'équipe vote: refuser ou accepter. | Romain (Mode 100%) |
| C6 | **"Concurrent agressif"** | Veeva/IQVIA baisse ses prix. Chaque joueur doit donner 1 argument "Why we win" en 30s. | Aucun — tout le monde joue |
| C7 | **"Incident infra weekend"** | Uptime tombe à 95%. Jeff doit proposer un plan de fix en 1 min. -5 pts Health. | Jeff (Bouclier Infra) |
| C8 | **"Le prospect veut une démo demain"** | Charbel doit confirmer que la démo est prête. Si oui: +20 pts. Si non: -10 pts. | Charbel (Ship It) |
| C9 | **"F1 régresse après un merge"** | F1 score baisse de 10%. Data-Team + Vassili doivent proposer 1 action corrective. | Vassili (KOL Express) |
| C10 | **"BONNE NOUVELLE: Intro chaude d'un board member"** | +1 meeting gratuit avec un Top-10. +15 pts pipeline. Pas de blocage nécessaire. | — (carte positive!) |

---

## DÉROULEMENT DES ROUNDS

### Structure d'un Round (15-20 min)

```
 ┌─────────────────────────────────────────────────┐
 │  1. CHAOS (2 min)                               │
 │     Tirer 1 carte Chaos. Décider de la réponse. │
 │                                                  │
 │  2. ENGAGEMENTS (5 min)                          │
 │     Chaque joueur pose 1-3 post-its:             │
 │     "Cette semaine, je m'engage à _____"         │
 │     Format: [Action] → [Résultat mesurable]      │
 │                                                  │
 │  3. NÉGOCIATION (5 min)                          │
 │     Les joueurs peuvent demander de l'aide       │
 │     entre eux. "J'ai besoin que Vassili me       │
 │     donne 2 intros KOL pour mon deal Sanofi."    │
 │     Les deux joueurs doivent accepter.            │
 │                                                  │
 │  4. SCORING (3 min)                              │
 │     Calculer les points du round.                │
 │     Mettre à jour le Score Collectif.            │
 │     Si Health = 0: Game Over.                    │
 │                                                  │
 │  5. CHECKPOINT (2 min — Tom/sponsor)             │
 │     Tom valide ou challenge 1 engagement.        │
 │     "Est-ce que $500k pipeline en S3 est         │
 │     réaliste avec 3 meetings bookés?"            │
 └─────────────────────────────────────────────────┘
```

---

## LES 7 ROUNDS — OBJECTIFS MINIMUM

### Round 1-2: SYNTHESIS — Poser les fondations
**Seuil pour passer au Round 3:** ≥ 30 pts collectifs + Health ≥ 80

| Objectif Round | Points | Qui décide |
|---|---|---|
| OKRs signés par Tom | 10 pts | Romain pose le doc, Tom signe |
| Jira + pipeline configuré | 10 pts | Jeff confirme "c'est live" |
| 2 axes thérapeutiques sélectionnés | 10 pts | Vassili pitch 3 options, l'équipe vote |
| 50 comptes ciblés + recherchés | 10 pts | Carlo & Erik présentent la liste |
| 3 meetings bookés pour S3-S4 | 15 pts | Carlo/Erik/Romain montrent le calendrier |
| Pricing sheet finalisée | 10 pts | Romain + Tom valident |
| BRA V1 démo-able? (Y/N gate) | 10 pts si Y, 0 si N | Charbel fait une démo live de 2 min |
| Baseline infra documentée | 5 pts | Jeff montre les chiffres |

**Mini-jeu SYNTHESIS:** *"Elevator Pitch Battle"*
- Chaque joueur a 60 secondes pour pitcher BRA à un prospect fictif (Tom joue le prospect).
- Tom note de 1 à 5. Le meilleur pitch gagne +10 pts bonus pour l'équipe.
- But réel: aligner tout le monde sur le même message avant d'aller sur le terrain.

---

### Round 3-4: REACTION — Accélérer le pipeline
**Seuil pour passer au Round 5:** Score cumulé ≥ 100 pts + Pipeline ≥ $500k

| Objectif Round | Points | Qui décide |
|---|---|---|
| Epic 2 déployé en Prod | 15 pts | Charbel + Jeff confirment |
| Context Alt-T ≥ 50% | 10 pts | Data-Team + Vassili |
| 3-5 discovery calls réalisés | 15 pts | Romain/Carlo/Erik racontent |
| 2-3 démos live données | 20 pts | Romain + Charbel confirment |
| 1ère proposition pilote envoyée | 15 pts | Romain montre le mail |
| Gap analysis axes complète | 10 pts | Vassili présente en 2 min |
| Pipeline qualifié ≥ $500k | 15 pts | Romain montre le tracker |

**Mini-jeu REACTION:** *"Objection Ping-Pong"*
- Tom (ou un volontaire) joue un prospect sceptique et lance des objections.
- L'équipe répond en tag-team: chaque joueur a max 20 secondes pour répondre, puis passe à un coéquipier.
- Objections tirées des cartes: "On peut le construire en interne", "Veeva fait déjà ça", "L'IA c'est une boîte noire".
- Si l'équipe survit 3 rounds d'objections sans silence > 5s: +10 pts bonus.

---

### Round 5: REACTION — Peak Pipeline
**Seuil pour passer au Round 6:** Score cumulé ≥ 170 pts + Pipeline ≥ $1M

| Objectif Round | Points | Qui décide |
|---|---|---|
| Epic 3 déployé | 15 pts | Charbel + Jeff |
| Context ≥ 75% | 10 pts | Data-Team + Vassili |
| F1 ≥ 60% | 15 pts | Data-Team |
| Platform availability ≥ 97% | 10 pts | Jeff |
| 1 deal en S5 (négociation) | 25 pts | Romain montre le deal |
| Pipeline ≥ $1M | 15 pts | Romain |
| 2+ sessions KOL réalisées | 10 pts | Vassili |
| Sales deck v2 intégrant feedback | 5 pts | Romain |

**Mini-jeu PEAK:** *"Deal War Room"*
- Romain présente le deal le plus avancé (2 min). Toute l'équipe a 5 min pour identifier les risques et proposer des actions.
- Chaque action concrète proposée = +2 pts.
- But réel: préparer la vraie stratégie de close du premier deal.

---

### Round 6: CATALYSIS — Premier Logo
**Seuil pour passer au Round 7:** Score cumulé ≥ 280 pts + 1 deal fermé

| Objectif Round | Points | Qui décide |
|---|---|---|
| Epic 4 déployé | 15 pts | Charbel + Jeff |
| 0 bugs critiques en Prod | 15 pts | Jeff |
| **Premier logo fermé $100k-$175k** | **50 pts** | Romain montre le contrat |
| Validation externe: 2+ outputs | 15 pts | Vassili |
| GTM bundle axe 1 complet | 10 pts | Romain + Vassili |
| F1 ≥ 85% | 20 pts | Data-Team |
| Context ≥ 90% | 10 pts | Data-Team + Vassili |
| Pipeline maintenu ≥ $1.2M | 10 pts | Romain |
| 1ère expansion proposée | 10 pts | Romain/Carlo/Erik |

**Mini-jeu CATALYSIS:** *"Speed Closing"*
- Simulation: Tom joue un VP Medical Affairs qui a dit "oui en principe" mais hésite.
- Romain a 3 min pour closer. Les autres joueurs peuvent passer des "notes" (post-its) avec des arguments pendant la négo.
- Si Tom dit "deal": +20 pts bonus. Si "non": l'équipe discute ce qui a manqué (5 min).

---

### Round 7: CATALYSIS — Wrap & Win
**Seuil de victoire:** Score cumulé ≥ 400 pts + ARR ≥ $500k

| Objectif Round | Points | Qui décide |
|---|---|---|
| **5/5 Epics déployés (KR1.1a)** | 20 pts | Charbel + Jeff |
| **$500k ARR atteint** | **100 pts** | Romain + Tom valident |
| 2 démos fonctionnelles (KR2.3) | 15 pts | Data-Team + Vassili |
| Ship time ≤ 10 min (KR1.5d) | 10 pts | Jeff |
| APM 100% (KR1.5e) | 10 pts | Jeff |
| 10-50 users on platform | 15 pts | App-Team |
| Next-quarter pipeline ≥ $500k | 15 pts | Romain/Carlo/Erik |
| Board report prêt | 10 pts | Romain |
| Rétrospective complétée | 5 pts | Tous |

---

## SYSTÈME DE SCORING

### Score Collectif (ARR proxy)
Le score monte avec chaque milestone atteint. Le mapping:

| Score | ARR Proxy | Statut |
|---|---|---|
| 0-99 | $0-$100k | On construit les fondations |
| 100-199 | $100k-$250k | Pipeline chauffe |
| 200-299 | $250k-$400k | Deals en négociation |
| 300-399 | $400k-$499k | Presque... |
| **400+** | **$500k+** | **MISSION ACCOMPLIE** |

### Health (Platform + Team)
- Démarre à **100 pts**
- Les cartes Chaos enlèvent des points (-5 à -15)
- Les pouvoirs spéciaux et les actions correctives restaurent des points (+5 à +10)
- **Si Health tombe à 0: Game Over** — la plateforme est down, les démos annulées, les deals morts

### Points Bonus (individuel → collectif)
- **MVP du round:** Le joueur qui a le plus contribué gagne +5 pts pour l'équipe (voté à main levée)
- **Assist du round:** Un joueur qui a aidé un coéquipier de manière décisive: +5 pts (nominé par le bénéficiaire)

---

## CONDITIONS DE VICTOIRE

| Résultat | Condition | Célébration |
|---|---|---|
| **VICTOIRE TOTALE** | Score ≥ 400 + Health > 50 + Pipeline > $1.2M | L'équipe a prouvé qu'on peut closer $500k. Champagne. |
| **VICTOIRE** | Score ≥ 400 + Health > 0 | $500k atteint mais l'équipe est épuisée. Bon mais fragile. |
| **PRESQUE** | Score 300-399 | On y est presque. Discussion: qu'est-ce qui manque pour les derniers $100k? |
| **LE CHAOS GAGNE** | Score < 300 ou Health = 0 | Retour au tableau blanc. Qu'est-ce qu'on n'a pas vu venir? |

---

## APRÈS LE JEU: LE VRAI LIVRABLE (30 min)

Le jeu produit du **vrai travail**. À la fin des 7 rounds:

### 1. Mur d'Engagements
Tous les post-its d'engagements sont sur le mur, organisés par semaine. Chaque joueur:
- **Signe ses 3 engagements les plus importants** (photo + Slack)
- Format: "Moi [Nom], je m'engage à [action] d'ici [date]. Résultat mesurable: [KPI]."

### 2. Carte des Dépendances
Pendant la phase Négociation, les joueurs ont identifié qui a besoin de qui. Dessiner:
- Les flèches de dépendance entre joueurs
- Les bottlenecks identifiés
- Les "handoffs" critiques (ex: Vassili → Romain pour les intros KOL)

### 3. Plan Anti-Chaos
Les cartes Chaos tirées pendant le jeu révèlent les vrais risques. Pour chaque carte tirée:
- Est-ce qu'on a un plan B réel?
- Qui est le owner du plan B?
- À quel moment on déclenche le plan B?

### 4. Scoreboard Semaine 1
Remplir le vrai tableau B1 (Master OKR Scorecard) avec les baselines discutées pendant le jeu.

---

## MATÉRIEL À PRÉPARER

### À imprimer
- [ ] 6 Cartes Rôle (1 par joueur — découper la section "Rôles & Pouvoirs")
- [ ] 10 Cartes Chaos (découper le tableau, mettre face cachée)
- [ ] 1 Plateau de score (le schéma ASCII agrandi en A3)
- [ ] 7 feuilles "Round X" avec les objectifs pré-imprimés
- [ ] Post-its (3 couleurs: vert = engagement, jaune = besoin d'aide, rouge = risque)
- [ ] 1 chronomètre visible

### À préparer en amont
- [ ] Romain: liste des 50 comptes ciblés (draft)
- [ ] Charbel: statut réel de la démo BRA V1
- [ ] Jeff: baselines infra actuelles (uptime, ship time, APM)
- [ ] Vassili: 3 axes thérapeutiques candidats avec argumentaire
- [ ] Carlo & Erik: 10 premiers comptes recherchés

### Nice-to-have
- [ ] Musique de fond (soundtrack de heist movie)
- [ ] Timer visible sur grand écran
- [ ] Pizza pour la mi-temps (entre Round 4 et 5)
- [ ] Un petit trophée "Mission: Catalysis" pour l'équipe si victoire

---

## PLANNING SUGGÉRÉ

| Temps | Activité |
|---|---|
| 0:00 | Accueil + règles du jeu (10 min) |
| 0:10 | Distribution des Cartes Rôle |
| 0:15 | **Round 1-2: Synthesis** (20 min) + Mini-jeu Elevator Pitch (10 min) |
| 0:45 | **Round 3-4: Reaction** (20 min) + Mini-jeu Objection Ping-Pong (10 min) |
| 1:15 | **PAUSE** — Pizza + discussion libre (15 min) |
| 1:30 | **Round 5: Peak** (15 min) + Mini-jeu Deal War Room (10 min) |
| 1:55 | **Round 6: Catalysis** (15 min) + Mini-jeu Speed Closing (10 min) |
| 2:20 | **Round 7: Wrap** (15 min) |
| 2:35 | **Scoring final + Victoire ou pas** (5 min) |
| 2:40 | **Le Vrai Livrable:** Engagements + Dépendances + Anti-Chaos (20 min) |
| 3:00 | Fin |

---

*Mission: Catalysis — ArcaScience BRA Platform Launch Game — Q2 2026*
*"On ne planifie pas un lancement. On le joue."*
