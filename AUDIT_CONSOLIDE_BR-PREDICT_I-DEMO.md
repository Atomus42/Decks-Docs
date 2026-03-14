# RAPPORT D'AUDIT CONSOLIDÉ — DOSSIER I-DÉMO BR-PREDICT (ARCASCIENCE)

**Date :** 14 mars 2026
**Objet :** Audit multi-axes du dossier de candidature au programme i-Démo (BPI France / France 2030)
**Projet :** BR-Predict — Première plateforme prédictive d'évaluation bénéfice-risque médicamenteux
**Porteur :** ArcaScience SAS, Paris 13e
**Budget :** 5 360 000 € sur 36 mois (01/2026 – 12/2028)

---

## TABLE DES MATIÈRES

1. [Synthèse exécutive et verdict global](#1-synthèse-exécutive)
2. [Matrice de scoring consolidée](#2-matrice-de-scoring)
3. [Axe 1 — Solidité financière](#3-axe-1--solidité-financière)
4. [Axe 2 — Solidité technique et répétabilité](#4-axe-2--solidité-technique)
5. [Axe 3 — Compétences et partenariats](#5-axe-3--compétences-et-partenariats)
6. [Axe 4 — Intérêt stratégique pour l'État français](#6-axe-4--intérêt-stratégique)
7. [Axe 5 — Cohérence documentaire (V7 vs Workpackages)](#7-axe-5--cohérence-documentaire)
8. [Synthèse des anomalies critiques bloquantes](#8-anomalies-critiques-bloquantes)
9. [Plan d'action prioritaire consolidé](#9-plan-daction-prioritaire)
10. [Conclusion](#10-conclusion)

---

## 1. SYNTHÈSE EXÉCUTIVE

Le dossier BR-Predict repose sur des **fondamentaux solides** : une technologie validée par des clients tier-1 (Sanofi, ICON, AstraZeneca), une levée série A structurante (4,65 M€), un positionnement monopolistique européen sur un segment stratégique, et un partenariat organique avec INRIA.

**Cependant, en l'état actuel, le dossier n'est pas soumissible à BPI France.**

Les raisons sont principalement rédactionnelles et structurelles, pas technologiques :

- **8 anomalies critiques bloquantes** identifiées (placeholders XXX/xx dans tous les lots, sections 6 et 7 absentes du V7, GANTT absent, incohérences de seuils AUC)
- **Le document V7 (Présentation détaillée) est manifestement un brouillon** dans sa section 4 (lots détaillés) alors que le dossier Workpackages est très mature
- **L'argumentaire "intérêt d'État"** — le facteur le plus souvent décisif en comité — est sous-exploité (note estimée 12/20)
- **Les projections financières 2030-2032** (TCAC de 84%) ne sont pas crédibles

**La bonne nouvelle :** toutes ces faiblesses sont remédiables. Le projet a les atouts pour obtenir le financement si les corrections sont appliquées.

### Verdict par axe

| Axe | Score actuel | Score cible | Risque sans correction |
|-----|-------------|-------------|----------------------|
| Solidité financière | **20/35** (57%) | 30/35 (86%) | Rejet en pré-instruction |
| Solidité technique | **3,1/5** (62%) | 4,2/5 (84%) | Questions éliminatoires des experts ML |
| Compétences & partenariats | **6,5/10** (65%) | 8/10 (80%) | Doutes sur la capacité d'exécution |
| Intérêt stratégique État | **12/20** (60%) | 17/20 (85%) | Score technique insuffisant pour compenser |
| Cohérence documentaire | **Non soumissible** | Soumissible | Irrecevabilité administrative |

---

## 2. MATRICE DE SCORING CONSOLIDÉE

### Les 15 faiblesses les plus critiques (classées par impact sur l'évaluation BPI)

| # | Faiblesse | Axe | Gravité | Impact BPI |
|---|-----------|-----|---------|-----------|
| 1 | Tous les postes budgétaires des 7 lots sont des templates vides (XXX/xx) | Financier + Cohérence | BLOQUANT | Irrecevabilité |
| 2 | Sections 6 (Éléments financiers) et 7 (Justification de l'aide) absentes du V7 | Financier | BLOQUANT | Irrecevabilité |
| 3 | Diagramme de GANTT absent ("Cf excel") | Cohérence | BLOQUANT | Irrecevabilité |
| 4 | Toutes les dates de tâches et livrables en "T0+XX mois" non renseignées | Cohérence | BLOQUANT | Irrecevabilité |
| 5 | Triple incohérence seuil AUC jalon EC1 (0,6 vs 0,65 vs 0,75) | Technique + Cohérence | CRITIQUE | Doute sur la rigueur |
| 6 | Incohérence calendaire Lot 4/WP4 (décalage > 1 an) | Cohérence | CRITIQUE | Doute sur le planning |
| 7 | Aucune mention de France 2030 dans un dossier i-Démo | Stratégique | CRITIQUE | Signal de non-appropriation |
| 8 | Le ratio 90/10 est une assertion non démontrée empiriquement | Technique | CRITIQUE | Question éliminatoire des experts |
| 9 | Projections CA 2030-2032 non crédibles (TCAC 84%) | Financier | ÉLEVÉ | Perte de crédibilité globale |
| 10 | Validation sur molécules commercialisées/retirées = biais de survie | Technique | ÉLEVÉ | Question des experts scientifiques |
| 11 | Absence de biostatisticien senior dans un projet "benefit-risk" | Compétences | ÉLEVÉ | Lacune thématique flagrante |
| 12 | Pas de protocole anti-data leakage entre WPs | Technique | ÉLEVÉ | Question des experts ML |
| 13 | Pas de scénario contrefactuel ("et si on ne finance pas ?") | Stratégique | ÉLEVÉ | Argumentaire incomplet |
| 14 | Le mot "souveraineté" n'apparaît qu'une seule fois | Stratégique | ÉLEVÉ | Sous-exploitation de l'atout principal |
| 15 | Concentration client excessive (Sanofi + ICON = ~70% CA) | Financier | ÉLEVÉ | Risque de dépendance |

### Les 10 forces les plus différenciantes

| # | Force | Axe | Impact BPI |
|---|-------|-----|-----------|
| 1 | Seul acteur européen sur le segment (11 concurrents tous US/UK) | Stratégique | Décisif en comité |
| 2 | 24 SLMs propriétaires — aucune dépendance aux LLMs américains | Technique + Stratégique | Architecture souveraine |
| 3 | Contrat ICON chiffré à 600 k€ + Sanofi multi-niveaux | Financier + Compétences | Validation marché |
| 4 | Levée série A structurée (4,65 M€, Pleiade Venture lead) | Financier | Solidité capitalistique |
| 5 | Taux de conversion POC → licence = 100% (2/2) | Financier | Argument sous-exploité |
| 6 | Partenariat organique INRIA (co-fondateur = DR INRIA) | Compétences | Crédibilité scientifique |
| 7 | Comité scientifique de 14 membres (Sanofi SVP, VP IBM, ICM) | Compétences | Caution institutionnelle |
| 8 | Actif technologique pré-existant (Trial Balancer, F1 88-92%) | Technique | Réduit le risque projet |
| 9 | Progressivité calibrée des KPI (EC1→EC2→EC3) | Technique | Méthodologie crédible |
| 10 | Cas d'usage Sanofi validé (18 mois → 2 mois) | Technique + Commercial | Preuve industrielle |

---

## 3. AXE 1 — SOLIDITÉ FINANCIÈRE

**Score : 20/35 (57%) → Cible : 30/35 (86%)**

### Forces

- **CA 2025 quasi-sécurisé** : 925 k€ adossé à 9 contrats signés avec 7 clients
- **Levée série A structurante** : 4,65 M€ avec Pleiade Venture (lead spécialisé santé) + Kima Ventures, Plug & Play
- **Diversité du pool investisseurs** : 7+ investisseurs au capital = validation croisée
- **Modèle économique clair** : SaaS on-premise, 125 k€/licence/an (Trial Balancer) + 125 k€ (BR-Predict)
- **Taux de conversion POC 100%** : Biocodex (20 k€ → 126 k€), Dilon (20 k€ → 42 k€)
- **Aide publique obtenue** : 1,8 M€ Innov'Up IDF = capacité démontrée à passer des comités

### Faiblesses critiques

1. **Champs XXX/xx non renseignés** — Éliminatoire en l'état. Templates vides pour la sous-traitance, achats et amortissements sur les 7 lots.
2. **Lot 7 management non budgété** : les lots 1-6 totalisent 5 200 k€, laissant 160 k€ pour le Lot 7 (4 400 €/mois pour 36 mois de gestion — extrêmement faible)
3. **Projections 2030-2032 non crédibles** : 8,3 M€ → 51,5 M€ en 3 ans (facteur 6,2x). Back-calculation : 51,5 M€ à 250 k€/molécule/an = 206 molécules simultanées pour ~55 personnes.
4. **Concentration client** : Sanofi (~46% CA) + ICON (~65% sur la période) = risque de dépendance
5. **Pas de scénario pessimiste** : BPI attend systématiquement un scénario bas/médian/haut
6. **Coûts GPU/compute non détaillés** pour le Lot 6 (World Model) — risque de dépassement

### Recommandations financières (11)

| # | Action | Priorité | Délai |
|---|--------|----------|-------|
| R-F1 | Compléter TOUS les champs XXX/xx (sous-traitance, achats, amortissements par lot) | BLOQUANT | Avant dépôt |
| R-F2 | Chiffrer le Lot 7 et vérifier somme = 5 360 k€ | BLOQUANT | Avant dépôt |
| R-F3 | Ajouter 3 scénarios financiers (bas/médian/haut) pour CA 2025-2028 | CRITIQUE | Avant dépôt |
| R-F4 | Retravailler les projections post-2028 (plafond réaliste ~15-20 M€ en 2032) | CRITIQUE | Avant dépôt |
| R-F5 | Détailler le plan de recrutement par profil, lot et trimestre | ÉLEVÉ | Avant dépôt |
| R-F6 | Détailler le budget compute Lot 6 (type GPU, heures, fournisseur) | ÉLEVÉ | Avant dépôt |
| R-F7 | Produire analyse de concentration client + plan de diversification | ÉLEVÉ | Avant dépôt |
| R-F8 | Clarifier articulation Innov'Up / i-Démo (non-chevauchement) | ÉLEVÉ | Avant dépôt |
| R-F9 | Ajouter chapitre gestion des risques formalisé | ÉLEVÉ | Avant dépôt |
| R-F10 | Fournir métriques SaaS (CAC, LTV, LTV/CAC, churn, NRR) | MODÉRÉ | Avant dépôt |
| R-F11 | Mettre en avant le taux de conversion POC 100% de manière visible | MODÉRÉ | Avant dépôt |

---

## 4. AXE 2 — SOLIDITÉ TECHNIQUE

**Score : 3,1/5 (62%) → Cible : 4,2/5 (84%)**

### Forces

- **Actif technologique pré-existant** : 24 SLMs, Profiling Base 100 Mds points, F1 scores 88-92%
- **Cas d'usage Sanofi validé** : 18 mois comprimés en 2 mois — preuve industrielle
- **Architecture modulaire 90/10** bien structurée WP par WP
- **Choix judicieux du NSCLC** comme pathologie d'ancrage (densité de données maximale)
- **KPI progressifs calibrés** : EC1 (AUC>0,6) → EC2 (AUC>0,75) → EC3 (AUC>0,8/0,9)
- **Sources de données de référence** correctement identifiées (ChEMBL, PharmGKB, FAERS, etc.)
- **Identification lucide du WP4 comme le plus risqué**

### Faiblesses critiques

1. **Le ratio 90/10 n'est pas démontré empiriquement** — C'est une assertion marketing, pas un résultat. Aucune courbe de transfert, aucune expérience d'ablation, aucune métrique de transférabilité.
2. **Validation sur molécules commercialisées/retirées = biais de survie majeur** — Prédire ex post est bien plus facile que prédire prospectivement. N=200 avec ~10% d'échecs = ~20 vrais positifs, intervalles de confiance très larges.
3. **Aucun protocole anti-data leakage** — Pas de split temporel, pas d'isolation des données entre WPs, pas de nested cross-validation.
4. **Saut oncologie → immunologie sous-argumenté** — Concordance PDX 87% en oncologie vs 40-50% en inflammation. Le "10% de calibration" est probablement plus proche de 30-40% inter-aires thérapeutiques.
5. **Exclusion des biothérapies non traitée** — WP1 limité aux petites molécules, alors que les anti-PD-1/PD-L1 dominent le NSCLC en première ligne.
6. **Pas de modèle d'additivité des WPs** — Comment les AUC individuelles se composent pour donner l'AUC finale ?
7. **Ambiguïté périmètre "prédiction B/R"** — Oscillation entre prédiction de propriétés moléculaires (QSAR) et prédiction du rapport bénéfice-risque clinique.

### Recommandations techniques (8)

| # | Action | Priorité | Délai |
|---|--------|----------|-------|
| R-T1 | Réaliser une expérience de transfert empirique sur Trial Balancer (courbe performance = f(% calibration)) | CRITIQUE | Avant dépôt |
| R-T2 | Spécifier un protocole de validation anti-leakage (split temporel strict, nested CV, power analysis) | CRITIQUE | Avant dépôt |
| R-T3 | Modéliser l'additivité des WPs (tableau AUC cumulatif WP1 → WP1+2 → ... → WP6) | ÉLEVÉ | Avant dépôt |
| R-T4 | Traiter explicitement le cas des biothérapies (limitation actuelle + feuille de route) | ÉLEVÉ | Avant dépôt |
| R-T5 | Renforcer le plan de mitigation WP4 (3 niveaux : FAERS seul → EDS → données fédérées) | ÉLEVÉ | Avant dépôt |
| R-T6 | Préciser le saut oncologie → immunologie (cartographie transférabilité, KPI spécifiques) | MODÉRÉ | Avant dépôt |
| R-T7 | Objectiver la validation experte (protocole standardisé, kappa inter-évaluateurs) | MODÉRÉ | Avant dépôt |
| R-T8 | Ajouter section positionnement réglementaire (SaMD, MDR, Drug Development Tool Qualification) | MODÉRÉ | Avant dépôt |

---

## 5. AXE 3 — COMPÉTENCES ET PARTENARIATS

**Score : 6,5/10 (65%) → Cible : 8/10 (80%)**

### Forces

- **Complémentarité remarquable** de l'équipe fondatrice (GSK + CentraleSupélec + INRIA DR + ex-Owkin CMO)
- **CTO + co-fondateur technique** = double couverture rare pour une startup de 8 ETP
- **Vassili Soumelis (ex-Owkin) comme CMO** = signal de recrutement de haut calibre
- **Partenariat INRIA organique** (Romary co-fondateur ET DR INRIA = lien structurel)
- **Contrat ICON/MAPI chiffré** (600 k€) = validation commerciale objective
- **Triple ancrage Sanofi** (Future4Care + Philippe Peyre au comité + projet IHI)
- **Comité scientifique de 14 membres** couvrant 4 pôles (scientifique, industriel, data/IA, marché)
- **Plan de recrutement en courbe S** (10/5/20/12) — temporalité réaliste
- **Dimension internationale** (Cedars-Sinai, projets IHI européens)

### Faiblesses

1. **Effectif sous-dimensionné** : 8 ETP pour 5,36 M€ sur 6 WPs = 1,3 ETP/WP
2. **Absence de biostatisticien senior** — lacune la plus critique dans un projet "benefit-risk"
3. **Absence d'expert réglementaire dédié** (SaMD/MDR/FDA)
4. **Formalisation incertaine des partenariats** — Cedars-Sinai et AstraZeneca semblent informels
5. **Pic 2028 (20 recrues)** = triplement de l'effectif en 12 mois — défi organisationnel
6. **Ratio stagiaires/ETP élevé** (37,5%) — signal de dépendance à main-d'œuvre non pérenne
7. **Force commerciale insuffisante** en phase initiale (1 ETP)
8. **Pas de partenariat CHU "de terrain"** au-delà de l'ICM

### Recommandations compétences & partenariats (10)

| # | Action | Priorité | Délai |
|---|--------|----------|-------|
| R-C1 | Recruter un biostatisticien senior (ou l'ajouter au comité scientifique) | CRITIQUE | Avant dépôt |
| R-C2 | Obtenir des lettres de soutien signées de Sanofi, INRIA, ICM, ICON | CRITIQUE | Avant dépôt |
| R-C3 | Recruter un chef de projet R&D i-Démo dédié | ÉLEVÉ | Avant démarrage |
| R-C4 | Clarifier le statut de chaque partenariat (signé/LOI/informel) | ÉLEVÉ | Avant dépôt |
| R-C5 | Présenter un tableau "ETP mobilisables au T0" incluant partenaires (>12-14 ETP-eq) | ÉLEVÉ | Avant dépôt |
| R-C6 | Détailler le plan de recrutement 2028 par trimestre (vagues de 4-6 max) | MODÉRÉ | Avant dépôt |
| R-C7 | Nouer un partenariat CHU complémentaire (AP-HP, Gustave Roussy) | MODÉRÉ | T1 2026 |
| R-C8 | Initier contact EMA Regulatory Sandbox ou ANSM guichet innovation | MODÉRÉ | T1-T2 2026 |
| R-C9 | Identifier consultant réglementaire SaMD/MDR et l'inclure au dossier | ÉLEVÉ | Avant dépôt |
| R-C10 | Souscrire assurance homme-clé et le mentionner | MODÉRÉ | Avant dépôt |

---

## 6. AXE 4 — INTÉRÊT STRATÉGIQUE POUR L'ÉTAT FRANÇAIS

**Score : 12/20 (60%) → Cible : 17/20 (85%)**

### Forces existantes (sous-exploitées)

- **Positionnement monopolistique européen** — 11 concurrents tous US/UK. ArcaScience est le seul acteur indépendant français sur ce segment.
- **Architecture souveraine par conception** — 24 SLMs propriétaires, déploiement on-premise, aucune dépendance OpenAI/Anthropic/Google
- **Ancrage institutionnel français** — INRIA, ICM, Future4Care, Innov'Up
- **Clients big pharma signés** — revenus d'exportation de services à haute VA
- **Impact sociétal chiffrable** — 10-300 patients épargnés par essai évité, réduction CO2

### Lacunes critiques

1. **Aucune mention de France 2030** dans un dossier i-Démo — lacune la plus grave
2. **"Souveraineté" n'apparaît qu'une seule fois** (p.47, contexte données)
3. **Pas de scénario contrefactuel** ("que se passe-t-il si on ne finance pas ?")
4. **Pas de mention du Plan Innovation Santé 2030**
5. **Pas de mention de la Stratégie Nationale IA**
6. **Pas de mention de l'EHDS** (European Health Data Space)
7. **Pas de chiffrage balance commerciale** des services technologiques en santé
8. **Section 5.3.1 "Retombées sociales" trop courte et générique**
9. **Pas de comparaison des investissements internationaux** (US, UK, Chine)

### Recommandations stratégiques (10) — avec textes proposés

| # | Action | Priorité |
|---|--------|----------|
| R-S1 | Ajouter encadré "Alignement France 2030" (Objectifs 3 et 4 + levier souveraineté) | ABSOLUE |
| R-S2 | Ajouter paragraphe "Souveraineté technologique" en 3 dimensions (données, décisionnelle, industrielle) | ABSOLUE |
| R-S3 | Ajouter phrase d'ancrage "intérêt national" dans le résumé exécutif | ABSOLUE |
| R-S4 | Réécrire et étoffer section 5.3.1 "Retombées sociales" (accès patients, inégalités, sécurité, emplois) | HAUTE |
| R-S5 | Ajouter scénario contrefactuel (3 scénarios : captation US, délocalisation, fragmentation) | HAUTE |
| R-S6 | Intégrer data points de contexte international (investissements US 3,6 Mds$, UK 1,2 Md£, asymétrie startups) | HAUTE |
| R-S7 | Mentionner l'EHDS comme opportunité stratégique (conformité by design) | IMPORTANTE |
| R-S8 | Mentionner le Plan Innovation Santé 2030 (mesures 1, 7, 10) | IMPORTANTE |
| R-S9 | Renforcer dimension formation (4 CIFRE, 8 stagiaires/an, filière IA/réglementation inexistante en France) | IMPORTANTE |
| R-S10 | Quantifier impact balance commerciale (200-400 M€/an d'externalisation captée par US) | IMPORTANTE |

**Phrase d'ancrage proposée pour le résumé exécutif :**
> *"BR-Predict est le seul projet français — et à notre connaissance européen — visant à créer une plateforme souveraine d'intelligence artificielle pour l'évaluation bénéfice-risque des médicaments, un segment stratégique aujourd'hui intégralement dominé par des acteurs américains et britanniques. Son financement dans le cadre de France 2030 permettrait à la France de combler une lacune critique de souveraineté sanitaire et de positionner un champion national sur un marché mondial de 13,2 milliards de dollars."*

---

## 7. AXE 5 — COHÉRENCE DOCUMENTAIRE (V7 vs WORKPACKAGES)

**Verdict : Document V7 non soumissible en l'état**

### Anomalies bloquantes (CRITIQUE)

| # | Anomalie | Localisation | Impact |
|---|----------|-------------|--------|
| 1 | Templates budgétaires vides (XXX/xx) dans les 7 lots | V7 p.38-46 | Irrecevabilité |
| 2 | Coût Lot 7 = "XX EUR" (écart de 160 k€) | V7 p.44-45 | Incohérence arithmétique |
| 3 | Sections 6 et 7 absentes du PDF | V7 p.51-53 (TdM) | Dossier incomplet |
| 4 | GANTT = "Cf excel" | V7 p.36 | Aucune visibilité planning |
| 5 | Triple incohérence seuil AUC EC1 : 0,6 (description) vs 0,65 (indicateurs) vs 0,75 (WP) | V7 p.36 + WP1 | Doute sur la rigueur |
| 6 | Incohérence calendaire majeure Lot 4/WP4 (V7 : 06/2026, WP : Q3 2027) | V7 p.42 + WP4 | Décalage > 1 an |
| 7 | Toutes les dates de tâches = "Mx - My" non renseignées | V7 p.38-45 | Planning absent |
| 8 | Tous les mois de livraison = "T0+XX mois" | V7 p.38-45 | Livrables non datés |

### Anomalies importantes

| # | Anomalie | Localisation |
|---|----------|-------------|
| 9 | Incohérence 2 vs 3 brevets (section 5.1.3 vs Lot 7 T7.4) | V7 p.45 vs p.48 |
| 10 | Placeholder "[À compléter par références sectorielles récentes]" | V7 p.30 |
| 11 | Erreur calcul Lot 5 : "T0+12 mois (Juin 2028)" — mathématiquement faux | V7 p.35 |
| 12 | Incohérence calendaire Lot 3/WP3 : fin 12/2027 vs fin Q3 2027 | V7 p.41 + WP3 |
| 13 | Incohérence calendaire Lot 5/WP5 : 12 mois vs 24 mois | V7 p.42 + WP5 |
| 14 | Numérotation erronée livrables Lot 7 : "L6.1, L6.2, L6.4" au lieu de "L7.x" | V7 p.45 |
| 15 | Colonne "Description des travaux" vide dans tableau clients | V7 p.14 |
| 16 | Financeur levée 2020 = "financée par XXX" | V7 p.4 |

### Anomalies mineures

| # | Anomalie |
|---|----------|
| 17 | "Plus de 20 SLMs" vs "24 SLMs" — harmoniser |
| 18 | Nature du Lot 7 non renseignée |
| 19 | Divergence numérotation livrables L2.x (WP a un livrable infrastructure supplémentaire) |
| 20 | Divergence découpe livrables L6.x (6 dans V7 vs 4 dans WP) |

### Constat structurel

Le V7 et le dossier Workpackages présentent un **niveau de maturité radicalement différent** :

| Dimension | V7 (Lots détaillés) | Dossier Workpackages |
|-----------|--------------------|--------------------|
| Description des tâches | 2-3 lignes, très synthétique | 1-3 pages avec méthodologie détaillée |
| KPI / protocole d'évaluation | Absents | Présents par WP avec métriques précises |
| Risques et mitigation | 1 tableau générique (8 risques) | Tableau détaillé par WP |
| Livrables | Dates "T0+XX" (non renseignées) | Mois précis (M6, M9, M12, M18) |
| Références bibliographiques | Absentes | Présentes (Olson, Gao, Park, etc.) |
| Cadre scientifique | Non formalisé | Hypothèses H1/H2/H3 par WP |

**Le dossier WP est la source de vérité technique. Le V7 doit être aligné sur le WP, pas l'inverse.**

---

## 8. ANOMALIES CRITIQUES BLOQUANTES — RÉCAPITULATIF

Ces éléments doivent être corrigés **avant toute soumission** sous peine d'irrecevabilité ou de rejet immédiat :

### Catégorie A — Irrecevabilité administrative
1. Renseigner tous les postes budgétaires (sous-traitance, achats, amortissements) pour les 7 lots
2. Rédiger et intégrer les sections 6 et 7 du V7 (éléments financiers + justification de l'aide)
3. Intégrer le diagramme de GANTT dans le PDF
4. Renseigner toutes les dates de tâches et mois de livraison

### Catégorie B — Rejet en évaluation
5. Harmoniser le seuil AUC du jalon EC1 : choisir une valeur unique (recommandation : 0,75)
6. Résoudre l'incohérence calendaire Lot 4/WP4
7. Ajouter l'alignement France 2030
8. Démontrer empiriquement le ratio 90/10 (ou le reformuler en termes vérifiables)

---

## 9. PLAN D'ACTION PRIORITAIRE CONSOLIDÉ

### Phase 1 — BLOQUANTS (J-30 à J-15 avant dépôt)

| # | Action | Responsable suggéré | Effort estimé |
|---|--------|-------------------|---------------|
| 1 | Compléter tous les XXX/xx budgétaires des 7 lots | CFO / CEO | 2-3 jours |
| 2 | Rédiger sections 6 et 7 du V7 | CFO | 3-5 jours |
| 3 | Intégrer le GANTT dans le PDF | Chef de projet | 1 jour |
| 4 | Renseigner toutes les dates de tâches et livrables | Chef de projet | 1-2 jours |
| 5 | Harmoniser seuil AUC EC1 partout (valeur unique) | CTO / CMO | 0,5 jour |
| 6 | Résoudre incohérences calendaires (Lot 4, 3, 5) | Chef de projet | 1 jour |
| 7 | Ajouter encadré France 2030 + phrase d'ancrage résumé exécutif | CEO | 1 jour |
| 8 | Corriger numérotation livrables Lot 7, brevets (2 vs 3), calcul Lot 5 | Rédacteur | 0,5 jour |

### Phase 2 — CRITIQUES (J-15 à J-7 avant dépôt)

| # | Action | Effort estimé |
|---|--------|---------------|
| 9 | Réaliser expérience de transfert empirique pour le 90/10 | 5-7 jours (R&D) |
| 10 | Spécifier protocole de validation anti-leakage | 2-3 jours |
| 11 | Recruter/identifier biostatisticien senior (ou ajout comité scientifique) | 1-2 semaines |
| 12 | Obtenir lettres de soutien (Sanofi, INRIA, ICM, ICON) | 2-3 semaines |
| 13 | Ajouter 3 scénarios financiers (bas/médian/haut) | 2 jours |
| 14 | Retravailler projections post-2028 | 1 jour |
| 15 | Ajouter paragraphe souveraineté tripartite | 1 jour |
| 16 | Réécrire section 5.3.1 "Retombées sociales" | 1-2 jours |
| 17 | Ajouter scénario contrefactuel | 1 jour |

### Phase 3 — RENFORCEMENTS (J-7 à J-0)

| # | Action | Effort estimé |
|---|--------|---------------|
| 18 | Modéliser additivité des WPs (tableau AUC cumulatif) | 1 jour |
| 19 | Traiter cas des biothérapies (limitation + feuille de route) | 1 jour |
| 20 | Mentionner EHDS, Plan Innovation Santé 2030, Stratégie Nationale IA | 0,5 jour |
| 21 | Ajouter data points internationaux (investissements US/UK/CN) | 0,5 jour |
| 22 | Clarifier articulation Innov'Up / i-Démo | 0,5 jour |
| 23 | Fournir métriques SaaS (CAC, LTV, NRR) | 1 jour |
| 24 | Mettre en avant taux de conversion POC 100% | 0,5 jour |
| 25 | Tableau ETP mobilisables au T0 (incluant partenaires) | 0,5 jour |
| 26 | Assurance homme-clé | 1 semaine (process) |

---

## 10. CONCLUSION

### Le diagnostic

Le dossier BR-Predict est paradoxal : il porte un projet **objectivement exceptionnel** (position monopolistique européenne, actif techno validé, clients tier-1, architecture souveraine) mais le présente dans un **document manifestement inachevé** (templates vides, sections absentes, incohérences multiples entre V7 et WP).

Le dossier Workpackages est techniquement mature et scientifiquement solide. Le document V7 de présentation détaillée, en revanche, est un brouillon dans sa section 4 (lots détaillés) et dans ses sections 6-7 (absentes).

### Le pronostic

**Avec les corrections de Phase 1 (bloquants) :** le dossier devient recevable.
**Avec les corrections de Phases 1+2 (bloquants + critiques) :** le dossier devient compétitif.
**Avec les corrections de Phases 1+2+3 :** le dossier devient excellent et difficile à refuser.

### Le message central

L'effort requis est principalement rédactionnel (environ 15-20 jours-homme au total), pas technique ou scientifique. Les fondamentaux du projet sont là. Ce qui manque, c'est la finition du dossier et la théâtralisation de l'intérêt d'État.

Le point le plus sous-exploité du dossier reste le **positionnement souveraineté** : ArcaScience est le seul acteur européen sur un segment de 13,2 milliards de dollars dominé à 100% par des entreprises américaines et britanniques. C'est un argument décisif en comité i-Démo / France 2030, et il doit devenir le fil rouge du dossier, pas un détail technique.

---

*Rapport généré le 14 mars 2026. 5 audits parallèles consolidés (financier, technique, compétences/partenariats, stratégie d'État, cohérence documentaire). Chaque axe détaillé est disponible sur demande.*
