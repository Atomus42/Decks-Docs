# CORRECTIONS DIVERSES DU V7

> **Note :** Ce document contient les corrections de la section 3 (GANTT, jalons, budget, risques) et les corrections ponctuelles à appliquer dans les sections 1 et 5.

---

## 1. DIAGRAMME DE GANTT (remplace « Cf excel » en section 3.2)

### 3.2. GANTT

Le diagramme ci-dessous présente le planning de réalisation des 7 lots du projet BR-Predict sur la période 01/2026 – 12/2028 (36 mois).

```
                    2026                              2027                              2028
            Q1      Q2      Q3      Q4      Q1      Q2      Q3      Q4      Q1      Q2      Q3      Q4
           Jan-Mar Avr-Jun Jul-Sep Oct-Déc Jan-Mar Avr-Jun Jul-Sep Oct-Déc Jan-Mar Avr-Jun Jul-Sep Oct-Déc

 Lot 1     ████████████████████████████████████████████████████████
 QSAR/     M1━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━M15
 QSTR      650 k€ │ 15 mois

 Lot 2                     ██████████████████████████████████████████████████████████████████
 Préclin.                  M6━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━M24
                           750 k€ │ 18 mois

 Lot 3                     ██████████████████████████████████████████████████████████████████
 Génomiq.                  M6━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━M24
                           850 k€ │ 18 mois

 Lot 4                             █████████████████████████████████████████████████████████████████████████████
 RWE                               M7━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━M30
                                   1 100 k€ │ 24 mois

 Lot 5                                                     █████████████████████████████████████████████████████████████████████████████
 KG                                                        M13━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━M36
                                                           550 k€ │ 24 mois

 Lot 6                                                     █████████████████████████████████████████████████████████████████████████████
 World                                                     M13━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━M36
 Model                                                     1 300 k€ │ 24 mois

 Lot 7     ████████████████████████████████████████████████████████████████████████████████████████████████████
 Mgmt      M1━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━M36
           160 k€ │ 36 mois

           ▲                                       ▲                                       ▲
           T0                                   EC1 (M15)                               EC2 (M24)
           01/2026                              03/2027                                 12/2027

                                                                                                       ▲
                                                                                                    EC3 (M36)
                                                                                                    12/2028
```

### Jalons décisionnels

| Jalon | Date | Lots concernés | Description |
|-------|------|---------------|-------------|
| **EC1** | M15 – 03/2027 | L1, L2, L4 | Démonstration capacité de prédiction B-R depuis la structure chimique seule (L1) et les données précliniques (L2). Pipeline RWE opérationnel (L4). |
| **EC2** | M24 – 12/2027 | L1-L5 | Intégration préclinique + génomique + RWE. Schéma ontologique validé. Architecture World Model validée. |
| **EC3** | M36 – 12/2028 | L1-L7 | World model opérationnel. Démonstrateur interactif (Mental Map). Validation sur 2+ aires thérapeutiques. |

---

## 2. SYNTHÈSE DES JALONS DÉCISIONNELS HARMONISÉS (remplace section 3.3)

### 3.3. Synthèse des principaux jalons décisionnels du projet et de leurs indicateurs de succès associés

| Jalon | Échéance | Description détaillée | Indicateurs de succès quantifiés |
|-------|----------|----------------------|--------------------------------|
| **EC1** | T0 + 15 mois (03/2027) | Démonstration de la capacité à prédire le profil bénéfice-risque d'un candidat médicament à partir de la structure chimique seule (WP1), avec intégration des premières données précliniques *in vivo* (WP2) et mise en service du pipeline d'extraction des données de vie réelle (WP4). Ce jalon valide la faisabilité scientifique du concept BR-Predict sur la pathologie d'ancrage (NSCLC). | **AUC > 0,75** sur jeu de validation externe pour les modèles QSAR/QSTR (WP1). **AUC > 0,70** sur le score de fiabilité préclinique (WP2). Pipeline d'extraction FAERS + 2 EDS partenaires opérationnel avec taux de couverture > 80 % des EIG connus (WP4). Incertitude quantifiée pour chaque prédiction. |
| **EC2** | T0 + 24 mois (12/2027) | Intégration des couches génomique (WP3) et données de vie réelle (WP4) aux modèles WP1-2. Validation du schéma ontologique et peuplement initial du Knowledge Graph (WP5). Architecture du World Model validée avec prototype d'intégration d'ensemble (WP6). Ce jalon démontre la valeur ajoutée de l'approche multi-sources. | **AUC > 0,75** en validation multi-sources (WP1+WP2+WP3). Gain incrémental statistiquement significatif (test de DeLong, p < 0,05) de WP1+WP2+WP3 vs WP1 seul. KG peuplé > 100 000 entités, > 1 million de relations. AUC > 0,80 sur les associations pharmacogénomiques de niveau 1A/1B (WP3). |
| **EC3** | T0 + 36 mois (12/2028) | World model opérationnel intégrant les 5 couches prédictives (WP1-4) via le Knowledge Graph (WP5). Démonstrateur interactif Mental Map fonctionnel. Validation rétrospective sur ≥ 200 molécules et validation prospective chez les partenaires. Extension à 2+ aires thérapeutiques au-delà de l'oncologie pulmonaire. | **AUC > 0,8** en validation externe multi-pathologies (générique). **AUC > 0,9** spécifique cancer du poumon. Taux de faux négatifs < 10 % pour les DDI connues. > 70 % des prédictions jugées « cliniquement plausibles » par le panel d'experts (≥ 10 évaluateurs, ≥ 3 institutions). Tests d'acceptation utilisateur réussis avec ≥ 5 partenaires pharmaceutiques. |

---

## 3. RISQUES IDENTIFIÉS ET PLAN DE SUIVI (section 3.4 enrichie)

### 3.4. Risques identifiés et plan de suivi

| # | Risque | Impact | Probabilité | Plan de mitigation |
|---|--------|--------|------------|-------------------|
| R1 | **Qualité/complétude variable des données RWE** (sous-reporting FAERS, données manquantes EDS) | Élevé | Élevée | Grille de qualification stricte (T4.1) ; imputation multiple avec analyse de sensibilité ; pondération inverse de la probabilité de notification |
| R2 | **Domaine d'applicabilité limité des modèles QSAR** (scaffolds moléculaires nouveaux) | Élevé | Moyenne | Définition explicite du domaine d'applicabilité par modèle ; combinaison de modèles spécialisés ; score de confiance associé à chaque prédiction ; enrichissement itératif du jeu d'entraînement |
| R3 | **Transposition inter-espèces imprécise** (concordance préclinique-clinique variable) | Élevé | Moyenne | Score de fiabilité par modèle animal × pathologie (WP2) ; pondération des prédictions par la concordance historique ; signalisation explicite de l'incertitude accrue |
| R4 | **Hétérogénéité et incomplétude des données génomiques** (biais ethniques, couverture variable) | Moyen | Moyenne | Stratification des modèles par population ; enrichissement via cohortes partenaires internationales (Cedars-Sinai, Mayo Clinic) ; signalisation des sous-groupes insuffisamment représentés |
| R5 | **Fuite de données entre WPs (data leakage)** | Élevé | Faible | **Protocole anti-leakage strict** : split temporel (hold-out 2022-2025), validation croisée par exclusion de molécules (leave-drug-out), nested cross-validation pour l'optimisation d'hyperparamètres, isolation complète des jeux d'entraînement/validation entre WPs |
| R6 | **Accès aux données EHDS non finalisé dans le calendrier** | Moyen | Moyenne | Sources FAERS + EDS partenaires suffisantes pour la validation cancer du poumon ; EHDS traité comme source complémentaire, non bloquante |
| R7 | **Complexité d'intégration multi-WP** (dépendances calendaires, formats) | Moyen | Élevée | Spécification précoce des interfaces (formats de sortie WP1-4, API WP5) dès EC1 ; intégration incrémentale (WP1-3 d'abord, WP4 ensuite, WP5 en parallèle) ; sprints d'intégration trimestriels |
| R8 | **Acceptation utilisateur insuffisante** (interface complexe, confiance limitée) | Moyen | Moyenne | Co-conception de la Mental Map avec les partenaires cliniques dès T6.5 ; tests utilisateurs itératifs (3 cycles) ; scoring d'incertitude comme levier de confiance ; formation dédiée |
| R9 | **Risque réglementaire** (qualification SaMD/MDR) | Moyen | Faible | Positionnement initial comme outil de recherche et d'aide à la décision (non-diagnostic) ; veille réglementaire continue ; architecture compatible avec les futures exigences de traçabilité/reproductibilité |
| R10 | **Pic de recrutement 2028** (20 embauches en 12 mois) | Moyen | Moyenne | Recrutement par vagues de 4-6 maximum ; pipeline de candidats alimenté par le réseau INRIA/ICM/Future4Care ; programme d'accueil et d'intégration structuré |

---

## 4. BUDGET ET PRINCIPAUX POSTES DE SOUS-TRAITANCE (section 3.5)

### 3.5. Budget et principaux postes de sous-traitance du projet

#### Budget par lot et par catégorie de dépense (k€)

| Poste de dépense | Lot 1 | Lot 2 | Lot 3 | Lot 4 | Lot 5 | Lot 6 | Lot 7 | **Total** |
|-----------------|-------|-------|-------|-------|-------|-------|-------|---------|
| Personnel (salaires + charges) | 540 | 615 | 695 | 880 | 470 | 1 100 | 130 | **4 430** |
| Sous-traitance | 70 | 85 | 100 | 150 | 45 | 110 | 20 | **580** |
| Achats (licences, données) | 25 | 30 | 35 | 40 | 20 | 50 | 5 | **205** |
| Amortissements | 15 | 20 | 20 | 30 | 15 | 40 | 5 | **145** |
| **Total** | **650** | **750** | **850** | **1 100** | **550** | **1 300** | **160** | **5 360** |

#### Principaux postes de sous-traitance

| Partenaire | Lots | Montant (k€) | Nature de la prestation |
|------------|------|-------------|----------------------|
| Gradient Health | L1, L2, L4 | 170 | Fourniture de jeux de données RWE annotés et structurés (imagerie clinique corrélée, données hospitalières) |
| Cedars-Sinai / Mayo Clinic | L2, L4 | 105 | Accès aux entrepôts de données de santé (EDS), cohortes rétrospectives pour validation externe, données longitudinales |
| INRIA | L1, L5 | 75 | Support méthodologique sur l'ingénierie des modèles, la traçabilité des pipelines, le support ontologique et l'alignement standards |
| ICM (Institut du Cerveau) | L3 | 60 | Accès aux cohortes génomiques avec profils cliniques, validation clinique, expertise neurologie pour extensions futures |
| AMI Labs | L6 | 60 | Validation méthodologique indépendante du world model, évaluation des architectures d'intégration |
| Sanofi | L6 | 50 | Validation clinique prospective sur cas d'usage réels en développement, accès à des données de pipeline interne |
| Cabinets PI / réglementaire | L7 | 20 | Préparation et dépôt de deux brevets, veille PI, conseil stratégique en propriété intellectuelle |
| **Total** | | **580** | |

---

## 5. CORRECTIONS PONCTUELLES À APPLIQUER DANS LE V7

### 5.1. Section 1.1 — Levée d'amorçage 2020

**Texte actuel :** « Une première levée d'amorçage a été réalisée en 2020 pour un montant de 550 k€, financée par XXX. »

**Texte corrigé :** « Une première levée d'amorçage a été réalisée en 2020 pour un montant de **550 k€**, financée par les fondateurs et premiers soutiens de la société. »

---

### 5.2. Section 1.4.3 — Tableau clients (colonne « Description des travaux »)

Le tableau actuel a la colonne « Description des travaux » vide pour tous les clients. Voici les descriptions à intégrer :

| Client | Montant | Description des travaux |
|--------|---------|------------------------|
| **ICON** | Juillet 2025 : 600 k€ | Structuration de données cliniques CRO à grande échelle, industrialisation des workflows d'analyse bénéfice-risque, intégration des standards B/R dans les processus décisionnels ICON/MAPI |
| **Sanofi** | Août 2025 : 235 k€ | Validation des modèles IA sur cas d'usage oncologie avancée, co-développement de modules d'analyse prédictive pour le pipeline interne |
| **Sanofi** | Juin 2025 : 100 k€ | Analyse comparative bénéfice-risque en dermatologie, calibration des modèles sur données internes Sanofi |
| **Sanofi** | Sept. 2024 : 90 k€ | POC initial, structuration de la base de données et profiling moléculaire sur molécules du portefeuille |
| **Vidal** | Sept. 2025 : 250 k€ | Intégration des données de référence médicamenteuses Vidal dans la Profiling Base, enrichissement du corpus réglementaire |
| **Mapi Research Trust** | Déc. 2024 : 156 k€ | Structuration des PRO (Patient-Reported Outcomes) et mesures de résultats patients, consolidation des profils B/R avec données patient |
| **Biocodex** | POC mars 2025 : 20 k€ ; Juin 2025 : 126 k€ | POC en gastro-entérologie (maladie de Crohn, rectocolite hémorragique), puis déploiement de la licence Trial Balancer en mode SaaS on-premise |
| **Dilon** | POC fév. 2025 : 20 k€ ; Mai 2025 : 42 k€ | POC en développement préclinique sur molécules candidates, puis licence plateforme Trial Balancer |
| **AstraZeneca** | Sept. 2025 : 60 k€ | Participation au projet IHI pédiatrique, structuration de projets collaboratifs R&D et alignement des données industrielles avec les standards ArcaScience |

---

### 5.3. Section 5.1.3 — Brevets (harmonisation)

**Conserver** le texte de la section 5.1.3 qui mentionne « **deux dépôts de brevets** ».

**Corriger** la section 4.7 (Lot 7), tâche T7.4, où il est écrit « le dépôt des **trois** brevets » → remplacer par « le dépôt des **deux** brevets ».

**Corriger** le livrable L7.3 : « Brevet » → « Deux brevets déposés correspondant aux principales innovations du projet ».

---

### 5.4. Harmonisation « SLMs » dans tout le document

**Remplacer partout** les occurrences de « plus de 20 SLMs » ou « plus de vingt modèles » par « **24 SLMs propriétaires** » ou « **24 Contextualizing SLMs** ».

Occurrences identifiées :
- Section 1.3.4 (Savoir-faire interne) : « vingt-quatre modèles propriétaires » ✓ (déjà correct)
- Section 2.3.2 (Données antérieures) : vérifier la formulation
- Section 1.5.1 (Ambition) : « 90 % de l'architecture repose sur des modèles non spécifiques » → vérifier la cohérence

---

### 5.5. Section 3.4 — Ajout du risque data leakage

Ajouter au tableau des risques existant (section 3.4) le risque suivant :

| Risque | Impact | Probabilité | Plan de mitigation |
|--------|--------|------------|-------------------|
| **Fuite de données entre jeux d'entraînement et de validation (data leakage)** | Élevé — invalidation des résultats de performance | Faible si protocole respecté | Protocole anti-leakage strict : split temporel (hold-out 2022-2025), validation croisée par exclusion de molécules (leave-drug-out), nested cross-validation pour l'optimisation d'hyperparamètres, isolation complète des jeux entre WPs. Audit de conformité à chaque jalon. |

---

### 5.6. Référence sectorielle manquante (p.30 du V7)

**Texte actuel :** « [À compléter par références sectorielles récentes] »

**Texte de remplacement :**
« Les principaux acteurs positionnés sur le segment de l'IA appliquée aux phases précoces du développement pharmaceutique incluent nference (analyse de données hospitalières structurées et non structurées, levée de 300 M$), Tempus (études translationnelles et analyses clinico-génomiques, levée de 1,1 Md$), Owkin (apprentissage fédéré et biomarqueurs en oncologie, 300 M$ levés), BenevolentAI (priorisation de candidats médicaments, cotée au LSE) et Recursion (criblage phénotypique par IA, 1,5 Md$ levé). Ces acteurs, tous américains ou britanniques, confirment la dynamique d'investissement massive dans ce segment et l'absence d'acteur européen continental, renforçant la pertinence stratégique du positionnement d'ArcaScience. »
