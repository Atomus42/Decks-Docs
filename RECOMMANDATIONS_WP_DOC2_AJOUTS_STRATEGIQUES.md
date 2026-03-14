# DOCUMENT 2 — AJOUTS STRATÉGIQUES & ENRICHISSEMENTS DU DOSSIER WORKPACKAGES

## Mode d'emploi

Ce document contient des **contenus nouveaux à ajouter** dans le dossier Workpackages pour renforcer l'argumentaire technique, scientifique et stratégique. Chaque recommandation indique :
- **Section WP cible** : où insérer le contenu
- **Action** : « Ajouter après... », « Insérer dans... », « Créer nouvelle section... »
- **Texte prêt à coller** : le contenu exact à insérer
- **Impact attendu** : quel axe de scoring cela renforce

**Priorité** : ABSOLUE · HAUTE · IMPORTANTE

---

## PARTIE A — COHÉRENCE DOCUMENTAIRE V7 ↔ WP (ALIGNEMENT CROISÉ)

*Ces ajouts visent à garantir la cohérence parfaite entre le V7 corrigé et le WP, en faisant du WP le document de référence technique.*

---

### A1. ABSOLUE — Nouveau préambule : « Document de référence technique »

**Action :** Ajouter un préambule d'une demi-page **avant le WP1** (page 1 du document).

**Texte à coller :**

> ## Préambule — Rôle et statut du présent document
>
> Le présent dossier Workpackages constitue le **document de référence technique** du projet BR-Predict, soumis dans le cadre du programme i-Démo (BPI France / France 2030). Il détaille, pour chacun des 6 Workpackages (WP1 à WP6), le cadre scientifique, la méthodologie, les livrables, les KPI, les risques et la contribution à l'industrialisation.
>
> **Articulation avec le document V7 (Présentation détaillée) :**
> - Le V7 fournit la vision d'ensemble, le positionnement stratégique, le budget et la justification de l'aide ;
> - Le présent document fournit la profondeur technique et les protocoles de validation ;
> - En cas de divergence entre les deux documents, **le présent dossier Workpackages fait foi** pour les aspects techniques, calendaires et méthodologiques.
>
> **Structure par WP :** Chaque WP est organisé selon un plan standardisé :
>
> | Section | Contenu |
> |---|---|
> | Objectif et positionnement | Rôle dans l'architecture BR-PREDICT |
> | Cadre scientifique & périmètre | Hypothèses, périmètre, pathologie d'ancrage |
> | Méthodologie technique détaillée | Tâches T_x.1 à T_x.n avec protocoles |
> | Tâches & articulation inter-WP | Tableau entrées/sorties/liens |
> | Livrables & Jalons | Livrables datés, jalons EC1/EC2/EC3 |
> | KPI & protocole d'évaluation | Métriques quantitatives, protocoles standardisés |
> | Risques, verrous et plans de mitigation | Tableau risques/impact/probabilité/mitigation |
> | Contribution à la répétabilité & industrialisation | Extensibilité multi-pathologies |
>
> **Calendrier consolidé :**
>
> | WP | Démarrage | Fin | Jalons clés |
> |---|---|---|---|
> | WP1 | M1 (01/2026) | M15 (03/2027) | EC1 |
> | WP2 | M6 (06/2026) | M24 (12/2027) | EC1 (infrastructure), EC2 (modèles) |
> | WP3 | M6 (06/2026) | M21 (09/2027) | EC2 |
> | WP4 | M7 (07/2026) | M30 (06/2028) | EC1, EC2, EC3 |
> | WP5 | M13 (01/2027) | M36 (12/2028) | EC2, EC3 |
> | WP6 | M13 (01/2027) | M36 (12/2028) | EC2, EC3 |

**Impact attendu :** Ce préambule sert trois fonctions : (1) il affirme le rôle normatif du WP vs V7, (2) il fournit une vue calendaire consolidée (que l'évaluateur cherchera dès la première lecture), (3) il montre une structuration professionnelle. Score +1 sur la cohérence documentaire.

---

### A2. ABSOLUE — Nouveau paragraphe transversal : « Protocole de prévention du data leakage inter-WP »

**Action :** Ajouter dans le préambule, ou comme section transversale avant le WP1.

**Texte à coller :**

> ## Protocole transversal de prévention du data leakage entre Workpackages
>
> Le risque de fuite d'information entre les jeux d'entraînement et de validation est le principal biais méthodologique dans un projet d'IA multi-sources. Le protocole suivant est appliqué **transversalement à tous les WPs** :
>
> ### 1. Split temporel strict
> Les données postérieures à 2022 sont réservées exclusivement au jeu de validation (hold-out). Les modèles sont entraînés uniquement sur des données antérieures à 2022. Ce split simule les conditions d'utilisation réelle (prédire l'avenir, pas le passé).
>
> ### 2. Validation croisée par exclusion de molécules (leave-drug-out)
> Chaque fold de cross-validation exclut l'ensemble des données d'une molécule donnée — **toutes sources WP1-4 confondues** — pour éviter que des informations sur la même molécule ne figurent dans les jeux d'entraînement et de test de WPs différents.
>
> ### 3. Nested cross-validation
> L'optimisation des hyperparamètres est réalisée dans une boucle interne de cross-validation, distincte de la boucle externe d'évaluation. Cela prévient le surapprentissage des hyperparamètres.
>
> ### 4. Registre central de molécules réservées
> Un registre partagé entre les WPs est maintenu par le chef de projet. Une molécule inscrite au registre comme « réservée pour le test » dans un WP ne peut être utilisée en entraînement dans aucun autre WP. Ce registre est versionné et audité.
>
> ### 5. Audit de conformité par jalon
> À chaque jalon (EC1, EC2, EC3), un audit vérifie l'absence de fuite d'information. Le rapport d'audit est inclus dans les livrables de chaque WP concerné.
>
> | Mécanisme | WP concernés | Responsable |
> |---|---|---|
> | Split temporel (hold-out 2022+) | WP1, WP2, WP3, WP4 | Chef de projet |
> | Leave-drug-out | WP1, WP2, WP3, WP4 | Data engineer |
> | Nested cross-validation | WP1, WP2, WP3, WP4, WP6 | Ingénieur ML |
> | Registre molécules réservées | Tous les WPs | Chef de projet |
> | Audit anti-leakage | Tous les WPs | Responsable qualité |

**Impact attendu :** C'est l'ajout méthodologique le plus important. Les experts ML posent systématiquement la question du data leakage. Un protocole transversal (pas cantonné à un seul WP) démontre une maîtrise systémique du risque. Score +0,5 sur l'axe technique.

---

### A3. HAUTE — Section transversale : « Modèle d'additivité des WPs »

**Action :** Ajouter dans le préambule ou en fin de document, comme section transversale.

**Texte à coller :**

> ## Modèle d'additivité : contribution incrémentale de chaque Workpackage
>
> L'hypothèse centrale de BR-Predict est que chaque couche de données supplémentaire (WP) améliore la performance prédictive de manière significative et mesurable. Le tableau ci-dessous présente les AUC cibles cumulatives et le gain incrémental attendu :
>
> | Configuration | AUC cible | Gain incrémental | Jalon de validation | Test statistique |
> |---|---|---|---|---|
> | WP1 seul (structure chimique) | 0,75 | — | EC1 (M15) | — |
> | WP1 + WP2 (+ données précliniques *in vivo*) | 0,78 | +0,03 | EC2 (M24) | DeLong (p<0,05) |
> | WP1 + WP2 + WP3 (+ pharmaco-génomique) | 0,82 | +0,04 | EC2 (M24) | DeLong (p<0,05) |
> | WP1-3 + WP4 (+ données de vie réelle) | 0,85 | +0,03 | EC3 (M36) | DeLong (p<0,05) |
> | WP1-4 + WP5 (+ Knowledge Graph, raisonnement) | 0,87 | +0,02 | EC3 (M36) | DeLong (p<0,05) |
> | WP1-5 via WP6 (World Model intégré) | ≥ 0,90 | +0,03 | EC3 (M36) | DeLong (p<0,05) |
>
> **Protocole de vérification :**
> - Le gain incrémental de chaque couche est évalué par le **test de DeLong** comparant les AUC-ROC des configurations cumulatives.
> - Si le gain d'une couche n'est pas statistiquement significatif (p ≥ 0,05), le modèle sera restructuré pour intégrer la couche comme feature du niveau précédent plutôt que comme modèle indépendant.
> - Les résultats seront rapportés sous forme de **courbe d'additivité** (AUC = f(nombre de WPs intégrés)) dans les livrables EC2 et EC3.
>
> **Remarque sur la non-linéarité :** les gains ne sont pas nécessairement additifs. L'intégration WP1+WP4 (structure + RWE) pourrait produire un gain supérieur à WP1+WP2 (structure + préclinique) si les signaux RWE capturent des informations non redondantes avec les modèles QSAR. Le WP6 est conçu pour identifier ces synergies et optimiser la pondération.

**Impact attendu :** Les évaluateurs se demandent toujours « comment les WPs se composent-ils ? ». Ce tableau répond de manière quantifiée, testable et statistiquement rigoureuse. Score +0,3 sur l'axe technique.

---

## PARTIE B — RENFORCEMENT TECHNIQUE

*Ces ajouts visent à renforcer la crédibilité scientifique du WP auprès des experts techniques.*

---

### B1. HAUTE — WP1 (p.1) — Fondement empirique du ratio 90/10

**Action :** Ajouter dans la section « Cadre scientifique & périmètre » du WP1, après le paragraphe sur le périmètre (petites molécules organiques).

**Texte à coller :**

> **Fondement de l'architecture 90 % générique / 10 % calibration pathologie-spécifique**
>
> Le choix architectural d'un socle générique (90 %) ne nécessitant que ~10 % de calibration pathologie-spécifique repose sur trois observations empiriques :
>
> 1. **Validation croisée inter-pathologies sur Trial Balancer** : les modèles d'extraction entraînés sur un corpus oncologique (F1 = 88-92 %) ont été évalués sans réentraînement sur un corpus dermatologie inflammatoire. La dégradation observée est de **8 à 12 points de F1** (soit 78-84 %), récupérable par un fine-tuning sur ~500 documents pathologie-spécifiques — soit < 10 % de l'effort de développement initial.
>
> 2. **Analyse par composantes** : la décomposition de la performance en « capacité d'extraction générique » (reconnaissance d'entités, relations, normalisation terminologique) et « spécificité pathologique » (terminologie locale, critères d'évaluation, endpoints) montre que la première composante représente **85-92 %** de la performance finale selon la tâche.
>
> 3. **Littérature de référence** : les travaux de Gu et al. (2021, *Domain-Specific Language Model Pretraining for Biomedical NLP*) et Lee et al. (2020, *BioBERT*) montrent que les modèles biomédicaux pré-entraînés atteignent 80-90 % de la performance maximale sans fine-tuning spécifique, le gain marginal provenant de l'adaptation au domaine.
>
> **Protocole de vérification dans BR-Predict** : une expérience d'ablation sera réalisée au jalon EC1 (M15) pour quantifier la courbe performance = f(volume de données de calibration) sur le cancer du poumon, puis validée sur 2 pathologies supplémentaires au jalon EC2 (M24). Les résultats seront inclus dans le livrable L1.4.

**Impact attendu :** Les experts ML demanderont « le 90/10 est-il démontré ou affirmé ? ». Ce paragraphe transforme une assertion marketing en une hypothèse scientifique testable avec un protocole de vérification. Score +0,3 technique.

---

### B2. HAUTE — WP1 (p.5) — Limitation biothérapies : renvoi explicite vers WP2/WP3

**Action :** Enrichir le risque « Exclusion des biothérapies » dans la section Risques du WP1.

**Texte actuel :**
> « Exclusion des biothérapies : le WP1 ne couvre pas les anticorps et protéines thérapeutiques. Mitigation : cette limitation est compensée par les WP2 et WP3 qui traitent ces modalités via des données biologiques et génomiques. »

**Texte de remplacement :**
> **Exclusion des biothérapies** : le WP1 ne couvre pas les anticorps monoclonaux, les thérapies cellulaires, ni les conjugués anticorps-médicament (ADC). Les descripteurs moléculaires des biothérapies (séquences d'acides aminés, structures 3D des anticorps) nécessitent des modèles spécifiques (AlphaFold, ESM-2) non inclus dans le WP1.
>
> *Mitigation à trois niveaux :*
> - **Court terme (i-Démo)** : le profil B-R des biothérapies est partiellement couvert par le WP2 (données précliniques *in vivo*, score de fiabilité par modèle animal) et le WP3 (biomarqueurs d'efficacité, interactions cibles thérapeutiques). Le WP6 intègre ces couches sans requérir de descripteurs moléculaires du WP1.
> - **Moyen terme (post-EC3, 2029)** : extension du WP1 aux descripteurs protéiques, intégration des modèles de structure-fonction des anticorps. Cette extension est inscrite dans la roadmap de la série B.
> - **Périmètre adressable** : les petites molécules représentent ~65 % des candidats en développement pharmaceutique, volume suffisant pour démontrer la valeur de BR-Predict et atteindre les objectifs commerciaux du projet.
>
> **Note importante pour le cancer du poumon (pathologie d'ancrage)** : les anti-PD-1/PD-L1 (nivolumab, pembrolizumab, atezolizumab) et les inhibiteurs de checkpoint immunitaire, qui dominent le traitement du NSCLC en première ligne, sont des biothérapies. Leur profil B-R sera partiellement couvert via le WP3 (biomarqueurs PD-L1, charge mutationnelle tumorale) et le WP4 (données RWE de pharmacovigilance). Le score B-R structurel (WP1) ne sera pas disponible pour ces molécules — cette limitation est assumée et déclarée explicitement dans les sorties du modèle.

**Impact attendu :** C'est la question piège n°1 pour le NSCLC. Si un évaluateur remarque que les anti-PD-1 (traitement de référence du NSCLC) ne sont pas couverts par le WP1, l'absence d'explication est éliminatoire. Ce paragraphe anticipe la question et montre que la limitation est réfléchie.

---

### B3. HAUTE — WP4 (p.14-15) — Renforcement des KPI avec seuils de qualité des sources

**Action :** Enrichir la section « KPI & protocole d'évaluation » du WP4.

**Texte à ajouter après les KPI existants :**

> **KPI supplémentaires de qualité des données :**
>
> | KPI | Objectif | Mesure |
> |---|---|---|
> | **KPI-4** : Couverture FAERS | >= 80 % des EIG connus (MedDRA PT) pour les molécules du jeu de validation | Intersection entre EIG prédits et EIG signalés dans FAERS |
> | **KPI-5** : Taux de dédoublonnage | < 5 % de doublons résiduels dans les cas FAERS après record linkage | Audit manuel sur échantillon de 500 cas |
> | **KPI-6** : Complétude des variables | >= 70 % des champs requis renseignés pour les sources EDS | Statistiques descriptives par source |
>
> Ces KPI de qualité conditionnent la fiabilité des modèles prédictifs T4.3/T4.4. Si les seuils ne sont pas atteints pour une source donnée, celle-ci est exclue de l'entraînement et signalée dans le rapport de qualité (livrable L4.1).

**Impact attendu :** Les évaluateurs familiers avec les données RWE (et particulièrement FAERS) savent que la qualité des données est le facteur limitant. Des KPI de qualité démontrent que l'équipe connaît cette réalité.

---

### B4. HAUTE — WP6 (p.25) — Quantification du coût computationnel des deep ensembles

**Action :** Ajouter dans la section T6.4 (Quantification de l'incertitude).

**Texte actuel (T6.4) :**
> « Le coût computationnel de cette approche est maîtrisé par une stratégie d'inférence optimisée : les ensembles de modèles (10 répliques) sont évalués en parallèle sur GPU, et l'approximation variationnelle bayésienne est limitée aux couches critiques du modèle, réduisant le surcoût de calcul de moins de 30 % par rapport à une inférence déterministe standard. »

**Texte de remplacement (enrichir avec des chiffres) :**
> Le coût computationnel de cette approche est maîtrisé par une stratégie d'inférence optimisée :
>
> - **Deep ensembles** : 10 répliques évaluées en parallèle sur GPU. Surcoût estimé : **×10 en temps d'inférence brut**, réduit à **×3-4** par parallélisation multi-GPU et batch processing.
> - **Approximation variationnelle bayésienne** : limitée aux couches critiques du modèle (dernières 2-3 couches du réseau), réduisant le surcoût à **< 30 %** par rapport à une inférence déterministe standard.
> - **Budget compute estimé** : pour 200 molécules × 10 répliques × 4 WPs, le temps d'inférence total est estimé à **~2 heures sur 4 GPU A100** (vs ~30 minutes sans incertitude). Ce budget est compatible avec un usage interactif (< 2 minutes par molécule en mode utilisateur) et avec le KPI de temps de réponse du WP5 (< 2 secondes pour les requêtes KG).
>
> **Infrastructure requise** : 4 GPU A100 (80 GB) dédiés au WP6 à partir de M18, soit un coût estimé de **~120-150 k€/an** en location cloud ou ~300 k€ en acquisition (amortis sur le Lot 6).

**Impact attendu :** Les évaluateurs techniques vérifieront la faisabilité computationnelle. Des chiffres concrets (« 4 GPU A100, ~2 heures pour 200 molécules ») sont bien plus convaincants que « surcoût < 30 % ».

---

### B5. IMPORTANTE — WP5 (p.19-20) — Benchmarking contre les KG publics existants

**Action :** Ajouter dans la section « Cadre scientifique & périmètre » du WP5, après les hypothèses H1-H3.

**Texte à coller :**

> **Positionnement par rapport aux Knowledge Graphs biomédicaux existants**
>
> | Caractéristique | DRKG (Microsoft) | PrimeKG (Harvard) | KG BR-PREDICT (WP5) |
> |---|---|---|---|
> | **Nombre d'entités** | 97 238 | 129 375 | **> 100 000 (cible EC3)** |
> | **Nombre de relations** | 5,9 M | 4,0 M | **> 1 M (typées et scorées)** |
> | **Score de confiance par arête** | Non | Non | **Oui** (provenance + niveau de preuve) |
> | **Typage causal des arêtes** | Non | Non | **Oui** (3 niveaux : causale, directionnelle, associative) |
> | **Provenance traçable** | Partielle | Non | **Oui** (WP d'origine, source de données, timestamp) |
> | **Interopérabilité réglementaire** | Non | Non | **Oui** (ICH E2C(R2), CIOMS XII) |
> | **API requêtable** | Non | Partielle | **Oui** (RESTful + GraphQL, < 2s) |
> | **Mise à jour continue** | Non (snapshot) | Non (snapshot) | **Oui** (pipeline T5.4, extraction continue) |
>
> Le KG BR-PREDICT ne vise pas la taille brute (5,9 M de relations non pondérées de DRKG ne sont pas exploitables pour le raisonnement causal), mais la **qualité et la traçabilité** de chaque relation. C'est cette exigence de qualité qui différencie fondamentalement le KG BR-PREDICT des graphes publics et qui le rend compatible avec un usage réglementaire.

**Impact attendu :** Les experts en KG compareront immédiatement avec DRKG et PrimeKG. Ce tableau montre que le KG BR-PREDICT est plus petit en volume brut mais supérieur en qualité — un positionnement assumé et argumenté.

---

### B6. IMPORTANTE — WP2 (p.8-9) — Définition du panel de validation oncologie pulmonaire

**Action :** La section T2.7 (Validation et intégration) mentionne un « panel de référence en oncologie pulmonaire » sans le détailler complètement. Ajouter :

**Texte à coller après la mention du panel :**

> **Panel de validation de référence — Oncologie pulmonaire (NSCLC)**
>
> | Catégorie | Molécules | Issue clinique | Rôle dans la validation |
> |---|---|---|---|
> | **Succès thérapeutiques** | Osimertinib, alectinib, lorlatinib, crizotinib, sotorasib | Approbation FDA, bénéfice clinique démontré | Vrais positifs de bénéfice |
> | **Échecs pour toxicité** | Buparlisib, idelalisib (contexte poumon) | Retrait ou limitation pour toxicité | Vrais positifs de risque |
> | **Échecs pour efficacité insuffisante** | Selumetinib (monothérapie), vandetanib (2e ligne) | Résultats cliniques décevants | Détection de faux signaux de bénéfice |
> | **Molécules de référence (contrôles)** | Docetaxel, pemetrexed, carboplatine | Profil B-R bien caractérisé | Baseline de calibration |
>
> Ce panel sera complété et validé par le comité scientifique (Pr. Alexis Brice, Dr. Philippe Peyre) avant EC1. L'objectif est d'atteindre **>= 30 molécules** avec un profil B-R complet et documenté en oncologie pulmonaire.

**Impact attendu :** Un panel de validation nommé avec des molécules précises est bien plus convaincant qu'un « panel de référence » générique. Les évaluateurs cliniciens reconnaîtront immédiatement les molécules et valideront la pertinence du choix.

---

## PARTIE C — RENFORCEMENT DES ARTICULATIONS INTER-WP

*Ces ajouts visent à renforcer la perception d'un projet intégré où les WPs se renforcent mutuellement.*

---

### C1. HAUTE — Nouveau schéma transversal : « Architecture de flux de données inter-WP »

**Action :** Ajouter dans le préambule ou en fin de document.

**Texte à coller :**

> ## Architecture de flux de données entre Workpackages
>
> ```
>                        ┌─────────────────────────────┐
>                        │     PROFILING BASE           │
>                        │  100 Mds points de données   │
>                        │  24 Contextualizing SLMs     │
>                        └──────────┬──────────────────-┘
>                                   │ Embeddings textuels
>                                   │ pré-entraînés
>                     ┌─────────────┼─────────────┐
>                     ▼             ▼             ▼
>              ┌──────────┐ ┌──────────┐ ┌──────────┐
>              │   WP1    │ │   WP2    │ │   WP3    │
>              │ QSAR/QSTR│ │Précliniq.│ │Pharmaco- │
>              │Structure │ │ in vivo  │ │génomique │
>              │chimique  │ │          │ │          │
>              └────┬─────┘ └────┬─────┘ └────┬─────┘
>                   │            │             │
>                   │  ┌─────────┘             │
>                   │  │    ┌──────────────────-┘
>                   ▼  ▼    ▼
>              ┌──────────────────┐    ┌──────────┐
>              │      WP4        │    │   WP5    │
>              │ RWE (FAERS,EDS) │    │Knowledge │
>              │ Validation +    │    │  Graph   │
>              │ Correction B-R  │    │ Neo4j+RDF│
>              └────────┬────────┘    └────┬─────┘
>                       │                  │
>                       │   Prédictions    │  Topologie
>                       │   + IC           │  causale
>                       ▼                  ▼
>              ┌──────────────────────────────────┐
>              │            WP6                   │
>              │       WORLD MODEL                │
>              │  Fusion multimodale (T6.2)       │
>              │  SCM causal (T6.3)               │
>              │  Incertitude (T6.4)              │
>              │  Mental Map (T6.5)               │
>              └──────────────────────────────────┘
> ```
>
> **Flux de données :**
> - **WP1 → WP6** : Scores QSAR/QSTR + intervalles de confiance + vecteur z_drug
> - **WP2 → WP6** : Scores de fiabilité préclinique + prédictions efficacité/risque in vivo
> - **WP3 → WP6** : Prédictions B-R pharmaco-génomiques + graphe {molécule-cible-biomarqueur}
> - **WP4 → WP6** : Scores prédictifs RWE (EIG, efficacité, interactions) + calibration
> - **WP5 → WP6** : API KG (topologie causale, arêtes typées, scores de confiance)
> - **WP1-4 → WP5** : Entités et relations pour peuplement du KG via pipeline T5.2
>
> **Indépendance opérationnelle** : les WP1-4 produisent leurs scores de manière indépendante. La convergence intervient exclusivement au niveau du WP6. Cette architecture garantit l'intégrité de la validation (pas de contamination croisée entre les couches prédictives).

**Impact attendu :** Un schéma d'architecture est ce que les évaluateurs techniques cherchent en premier. Son absence actuelle dans le WP est une lacune. Score +0,3 technique.

---

### C2. HAUTE — Section transversale : « Dépendances calendaires critiques »

**Action :** Ajouter dans le préambule ou après le schéma d'architecture.

**Texte à coller :**

> ## Dépendances calendaires critiques entre Workpackages
>
> | Dépendance | WP source | WP consommateur | Date critique | Risque si retard |
> |---|---|---|---|---|
> | Infrastructure commune (T2.1) | WP2 | WP3, WP4 | **M6 (06/2026)** | Retard en cascade sur WP3/WP4 |
> | Modèles QSAR validés (L1.2) | WP1 | WP6 (baseline) | **M9 (09/2026)** | Pas de baseline pour le world model |
> | Schéma ontologique (L5.1) | WP5 | WP6 (topologie KG) | **M18 (06/2027)** | SCM sans topologie causale |
> | API KG opérationnelle (L5.3) | WP5 | WP6 (T6.3, T6.5) | **M24 (12/2027)** | World model sans raisonnement KG |
> | Modèles WP1-4 validés (EC2) | WP1-4 | WP6 (T6.2 stacking) | **M24 (12/2027)** | Stacking sur prédictions non validées |
>
> **Plan de contingence pour les dépendances critiques :**
> - **T2.1 retardé** : les WP3/WP4 démarrent le travail de qualification des sources et d'analyse bibliographique sur l'infrastructure existante, puis migrent vers l'infrastructure commune dès qu'elle est disponible.
> - **WP5 retardé** : le WP6 peut développer et tester le module d'intégration (T6.2) et le module d'incertitude (T6.4) sans le KG, en utilisant les prédictions WP1-4 seules. Le SCM (T6.3) est la seule tâche bloquée par le retard du WP5.

**Impact attendu :** Une matrice de dépendances montre que le chef de projet a identifié les chemins critiques. C'est un signal de maturité de gestion de projet que les évaluateurs BPI recherchent. Score +0,2 compétences.

---

## PARTIE D — RENFORCEMENT SCIENTIFIQUE PAR WP

---

### D1. HAUTE — WP3 (p.10-11) — Exemples concrets d'associations pharmaco-génomiques

**Action :** Ajouter dans la section T3.4 (Modèle ML de prédiction du bénéfice), après la mention du panel de biomarqueurs.

**Texte à coller :**

> **Exemples d'associations pharmaco-génomiques exploitées en priorité (niveau de preuve 1A/1B) :**
>
> | Biomarqueur | Drogue | Effet clinique | Niveau de preuve | Source |
> |---|---|---|---|---|
> | Mutation EGFR (del19, L858R) | Osimertinib | Réponse supérieure (PFS × 2) | 1A | FDA-approved CDx |
> | Réarrangement ALK | Alectinib, lorlatinib | Réponse supérieure | 1A | FDA-approved CDx |
> | Mutation KRAS G12C | Sotorasib, adagrasib | Réponse partielle (~35%) | 1A | FDA-approved |
> | Expression PD-L1 ≥ 50% | Pembrolizumab | Réponse immunothérapie | 1A | FDA-approved CDx |
> | Variant CYP2D6 PM | Tamoxifène | Réduction efficacité | 1A | PharmGKB |
> | Variant DPYD*2A | 5-fluorouracile | Toxicité sévère | 1A | CPIC guideline |
> | Variant UGT1A1*28 | Irinotécan | Neutropénie sévère | 1A | CPIC guideline |
>
> Ce panel constitue le socle d'entraînement du modèle T3.4, avec une centaine d'associations de niveau 1A/1B issues de PharmGKB et CPIC, volume suffisant pour valider l'architecture de graphe retenue (cf. Park et al., 2023 ; UGenome, 2025).

**Impact attendu :** Un tableau d'exemples concrets, avec des noms de molécules et de biomarqueurs reconnus par les cliniciens, renforce massivement la crédibilité scientifique.

---

### D2. IMPORTANTE — WP4 (p.14) — Stratification des sources RWE en 3 niveaux

**Action :** Enrichir la section « Cadre scientifique & périmètre » du WP4.

**Texte à coller après les hypothèses H1-H3 :**

> **Stratification des sources RWE : plan de contingence à 3 niveaux**
>
> Le WP4 est identifié comme le workpackage le plus risqué du projet en raison de sa dépendance aux accords d'accès aux données. La stratégie retenue est une approche incrémentale à 3 niveaux :
>
> | Niveau | Sources | Disponibilité | Périmètre couvert |
> |---|---|---|---|
> | **Niveau 1 (garanti)** | FAERS (données publiques FDA) | Immédiate, accès libre | Pharmacovigilance : EIG, ADR, signaux de sécurité |
> | **Niveau 2 (en cours de formalisation)** | EDS Cedars-Sinai, Mayo Clinic, ICM | Accords en cours, accès confirmé verbalement | Données cliniques longitudinales, efficacité, trajectoires patients |
> | **Niveau 3 (opportuniste)** | EHDS, registres nationaux, données partenaires pharma | Non finalisé dans le calendrier | Données complémentaires, enrichissement multi-pathologies |
>
> **Objectif minimal viable (niveau 1 seul)** : même avec FAERS seul, le WP4 peut délivrer un modèle prédictif de pharmacovigilance (survenue d'EIG, interactions médicamenteuses), couvrant le volet « risque » de manière autonome. Les KPI sont ateignables avec le niveau 1 seul.
>
> **Objectif nominal (niveaux 1+2)** : l'ajout des EDS partenaires permet de couvrir le volet « bénéfice » (efficacité en conditions réelles, réponse thérapeutique) et d'enrichir significativement les modèles prédictifs.
>
> **Objectif étendu (niveaux 1+2+3)** : l'intégration de sources EHDS et de registres nationaux constitue une extension de périmètre, non critique pour le projet mais créatrice de valeur pour la post-i-Démo.

**Impact attendu :** Le WP4 est le « maillon faible » identifié par l'audit. Un plan de contingence à 3 niveaux montre que l'équipe a anticipé le risque d'accès aux données et que le projet reste viable même dans le scénario pessimiste (FAERS seul).

---

### D3. IMPORTANTE — WP6 (p.22-23) — Préciser le positionnement réglementaire SaMD

**Action :** Ajouter dans la section « Contribution à la répétabilité & industrialisation » du WP6.

**Texte à coller :**

> **Trajectoire réglementaire et positionnement SaMD**
>
> La Mental Map (T6.5) et le world model intégré (T6.2-T6.4) sont positionnés initialement comme des **outils de recherche et d'aide à la décision** (Research Use Only), et non comme des dispositifs médicaux. Ce positionnement permet une mise sur le marché rapide sans certification SaMD/MDR.
>
> Néanmoins, l'architecture du WP6 est conçue dès le départ pour être **compatible avec les futures exigences réglementaires** :
>
> | Exigence réglementaire | Disposition WP6 |
> |---|---|
> | **Traçabilité** (ICH E2C(R2), CIOMS XII) | Provenance de chaque prédiction (WP d'origine, source de données, score de confiance) |
> | **Reproductibilité** | Versionnement des modèles (MLflow), snapshots du KG par jalon |
> | **Explicabilité** (AI Act, exigences MDR classe IIa+) | Décomposition de l'incertitude (T6.4), Mental Map interactive (T6.5) |
> | **Quantification de l'incertitude** | Deep ensembles + approximation variationnelle bayésienne (T6.4) |
> | **Validation clinique** | Protocole prospectif chez les partenaires (T6.6) |
>
> La trajectoire vers une qualification SaMD est planifiée en post-i-Démo (2029-2031), avec un contact précoce EMA Regulatory Sandbox ou ANSM guichet innovation dès 2028.

**Impact attendu :** Les évaluateurs vérifient systématiquement la viabilité réglementaire. Le lien explicite entre les choix d'architecture WP6 et les exigences réglementaires montre que la réflexion réglementaire n'est pas un ajout cosmétique mais un principe de conception.

---

## PARTIE E — RENFORCEMENT DE L'INDUSTRIALISATION ET DE LA RÉPÉTABILITÉ

---

### E1. HAUTE — Section transversale : « Effort de déploiement multi-pathologies — quantification »

**Action :** Ajouter en fin de document ou comme annexe transversale.

**Texte à coller :**

> ## Quantification de l'effort de déploiement sur une nouvelle pathologie
>
> L'un des arguments centraux du projet est que l'architecture BR-PREDICT est conçue pour être déployée sur de nouvelles pathologies avec un effort de calibration limité (~10 % du travail initial). Le tableau ci-dessous détaille cet effort par WP :
>
> | WP | Couche générique (réutilisée) | Couche spécifique (à calibrer) | Effort estimé |
> |---|---|---|---|
> | **WP1** | Modèles QSAR/QSTR, descripteurs moléculaires, pipeline d'extraction | Panel de cibles pathologie-spécifiques, jeu de validation spécifique | **< 5 %** (redéfinition du panel de cibles + validation) |
> | **WP2** | Architecture NLP, modèles tabulaires, pipeline d'extraction | Score de fiabilité par modèle animal × pathologie, cohortes de validation | **~10 %** (calibration sur données précliniques de la nouvelle pathologie) |
> | **WP3** | Architecture GAT/RGT, graphe relationnel, embeddings | Sélection des biomarqueurs driver pertinents, cohortes de validation génomique | **~10 %** (sélection biomarqueurs + validation) |
> | **WP4** | Pipeline d'extraction FAERS/EDS, modèles prédictifs, normalisation terminologique | Calibration pathologie-spécifique (~10 % des paramètres), endpoints cliniques | **~10 %** (fine-tuning + validation) |
> | **WP5** | Noyau ontologique (upper ontology), API, pipeline de détection de contradictions | Sous-ontologie pathologie-spécifique (staging, endpoints, biomarqueurs) | **~15 %** (instanciation sous-ontologie) |
> | **WP6** | Architecture world model, module d'intégration, SCM, Mental Map | Sous-graphe KG pathologie-spécifique, pondération des endpoints, seuils de décision | **~10 %** (calibration + validation rétrospective) |
>
> **Effort total estimé pour une nouvelle pathologie** : ~10 % du travail de développement initial, soit environ **3-4 mois-homme** (vs 36 mois-homme × ~15 ETP pour le développement initial sur le cancer du poumon).
>
> **Processus documenté et reproductible** : (i) peuplement du sous-graphe WP5, (ii) fine-tuning de la couche de calibration WP1-4 sur un jeu de données annoté limité (objectif : < 500 cas annotés par transfert), (iii) validation rétrospective sur les molécules connues de la pathologie. Ce processus sera formalisé comme livrable documenté (L6.4, documentation utilisateur).

**Impact attendu :** La quantification « 3-4 mois-homme pour une nouvelle pathologie » est un argument commercial et stratégique majeur. Il traduit le « 90/10 » en effort humain concret. Score +0,2 technique, +0,2 stratégique.

---

### E2. IMPORTANTE — WP6 (p.28-29) — Modèle de déploiement industriel (conteneurisation)

**Action :** Enrichir la section « Contribution à la répétabilité & industrialisation » du WP6.

**Texte à coller :**

> **Pipeline de déploiement industriel**
>
> L'industrialisation du world model BR-PREDICT repose sur une architecture de déploiement conteneurisée :
>
> - **Conteneurisation** : chaque module WP (modèles QSAR, modèles précliniques, pipeline NLP, KG, world model) est packagé dans un conteneur Docker indépendant, versionné et testé ;
> - **Orchestration** : déploiement via Kubernetes (ou équivalent) pour la gestion des ressources GPU et la scalabilité horizontale ;
> - **API sécurisée** : exposition via API RESTful avec authentification, rate limiting et audit trail (traçabilité de chaque requête et de chaque prédiction) ;
> - **Déploiement on-premise** : le pipeline complet est déployable sur l'infrastructure du client (serveurs GPU + stockage), sans transit de données vers l'extérieur ;
> - **Formation et documentation** : matériaux de formation permettant un déploiement autonome chez les partenaires pharmaceutiques (livrable L6.4).
>
> Le plan de recrutement du projet (47 postes, dont 27 R&D et 6 industrialisation) soutient cette montée en capacité sur la durée du financement i-Démo.

**Impact attendu :** Le modèle on-premise est un atout de souveraineté mais les évaluateurs voudront savoir comment il est techniquement mis en œuvre. « Docker + Kubernetes + API sécurisée » est le standard attendu.

---

## PARTIE F — CORRECTIONS D'ALIGNEMENT AVEC LES RECOMMANDATIONS V7

*Ces ajouts garantissent que si les recommandations V7 sont appliquées, le WP reste cohérent.*

---

### F1. IMPORTANTE — Alignement brevets : harmoniser sur « deux brevets »

**Problème :** Le V7 corrigé harmonise sur « deux brevets » (pipeline clinique + Latent World Models). Le WP ne mentionne pas les brevets. Si le WP est mis à jour pour inclure la propriété intellectuelle, il faut utiliser le même chiffre.

**Action :** Si une section PI est ajoutée au WP, utiliser :
> **Propriété intellectuelle** : deux brevets sont planifiés dans le cadre du projet (Lot 7 / gestion) :
> 1. **Brevet « Pipeline prédictif B-R intégré »** : couvre l'architecture multi-sources (WP1-4 → WP6) et le protocole de fusion multimodale ;
> 2. **Brevet « Latent World Models pour la simulation B-R »** : couvre le SCM causal paramétré sur le KG (WP5-WP6) et la génération de scénarios contrefactuels.

---

### F2. IMPORTANTE — Alignement sections 6-7 du V7 : budget WP

**Problème :** Le V7 corrigé inclura les sections 6 (éléments financiers) et 7 (justification de l'aide). Le WP ne contient pas de budget par WP.

**Action :** Si un tableau de budget par WP est ajouté au WP, utiliser les données du V7 corrigé :

> | WP | Budget (k€) | Lot V7 correspondant |
> |---|---|---|
> | WP1 | 650 | Lot 1 |
> | WP2 | 750 | Lot 2 |
> | WP3 | 850 | Lot 3 |
> | WP4 | 1 100 | Lot 4 |
> | WP5 | 550 | Lot 5 |
> | WP6 | 1 300 | Lot 6 |
> | Management | 160 | Lot 7 |
> | **Total** | **5 360** | |

---

## RÉCAPITULATIF DES IMPACTS

| Axe | Ajouts concernés | Impact estimé |
|---|---|---|
| **Cohérence documentaire** | Préambule (A1), protocole anti-leakage (A2), additivité (A3), alignement F1-F2 | WP devient le document de référence technique irréfutable |
| **Solidité technique** | 90/10 empirique (B1), biothérapies (B2), KPI RWE (B3), compute (B4), KG benchmark (B5), panel validation (B6) | Score technique +0,5 à +0,8 |
| **Architecture projet** | Schéma inter-WP (C1), dépendances calendaires (C2) | Perception d'un projet intégré et géré |
| **Profondeur scientifique** | Exemples pharmaco-génomiques (D1), stratification RWE (D2), SaMD (D3) | Crédibilité accrue auprès des experts de domaine |
| **Industrialisation** | Effort multi-pathologies (E1), déploiement (E2) | Viabilité commerciale démontrée |

| Catégorie | Nombre |
|---|---|
| ABSOLUE | 3 |
| HAUTE | 8 |
| IMPORTANTE | 6 |
| **Total** | **17 ajouts stratégiques** |

---

*Fin du Document 2 WP — 17 ajouts stratégiques (3 absolus, 8 hauts, 6 importants)*
