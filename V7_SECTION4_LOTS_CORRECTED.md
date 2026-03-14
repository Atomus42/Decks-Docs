# 4. LOTS DÉTAILLÉS — VERSION CORRIGÉE

> **Note :** Cette section remplace intégralement la section 4 du V7 (pages 36-46). Toutes les dates, budgets et livrables ont été harmonisés avec le dossier Workpackages.

---

## 4.1. LOT 1

| | |
|---|---|
| **Lot n°** | 1 |
| **Intitulé du lot** | Modèles prédictifs QSAR/QSTR pour l'estimation du rapport bénéfice-risque à partir de la structure moléculaire seule |
| **Nature du lot** | DE (Développement Expérimental) |
| **Durée** | 15 mois (01/2026 – 03/2027) |
| **Coût total du lot** | 650 k€ |

### Objectifs

L'objectif de ce lot est de démontrer qu'il est possible, dès la phase de criblage chimique, de produire une estimation quantitative du profil bénéfice-risque (B-R) d'un candidat-médicament à partir de sa seule représentation structurale. Ce lot constitue la couche prédictive la plus précoce de BR-PREDICT. La pathologie d'ancrage est le cancer du poumon non à petites cellules (NSCLC). L'objectif cible est une AUC > 0,75 sur le jeu de validation externe, seuil cohérent avec l'état de l'art QSAR sur des espaces chimiques diversifiés.

### Travaux réalisés

| Tâche | Période | Description |
|-------|---------|-------------|
| **T1.1** | M1 – M6 (01/2026 – 06/2026) | **Qualification des sources de données.** Exploitation de trois corpus de référence : ChEMBL 34 (~2,4M composés), ToxCast (~10K composés, ~600 endpoints) et NCGC qHTS (~300K composés). Audit de couverture, cohérence et biais de publication. |
| **T1.2** | M1 – M9 (01/2026 – 09/2026) | **Construction et curation de la base de données.** Constitution d'une base dédiée de ~4 500 molécules commercialisées avec profil B-R documenté. Normalisation des identifiants chimiques (InChI, SMILES), déduplication, annotation croisée avec la Profiling Base d'ArcaScience. |
| **T1.3** | M1 – M6 (01/2026 – 06/2026) | **Représentation moléculaire et calcul de descripteurs.** Conversion en vecteurs de features : fingerprints moléculaires (Morgan/ECFP, MACCS), descripteurs physicochimiques (RDKit), et représentations par graphes moléculaires pour les architectures GNN. |
| **T1.4** | M3 – M12 (03/2026 – 12/2026) | **Développement des modèles QSAR (bénéfice).** Entraînement et comparaison de plusieurs approches ML : Random Forest, Gradient Boosting et réseaux de neurones sur graphes (GNN). Définition du domaine d'applicabilité par modèle. Panel de cibles oncologie pulmonaire (EGFR, ALK, KRAS, PD-L1). |
| **T1.5** | M3 – M12 (03/2026 – 12/2026) | **Développement des modèles QSTR (risque).** Architecture parallèle entraînée sur données de toxicité ToxCast et NCGC. Couverture : cytotoxicité (~10 000 composés), cardiotoxicité hERG (~10-15 000), génotoxicité (~5-8 000), hépatotoxicité (~3-5 000). |
| **T1.6** | M9 – M15 (09/2026 – 03/2027) | **Intégration et validation.** Intégration des scores QSAR et QSTR en un score B-R composite via méta-modèle calibré. Validation sur trois piliers : cross-validation stratifiée 5-fold, test externe sur molécules à B-R connu, validation sur base WITHDRAWN (retraits pour motifs de sécurité). |

### Livrables

| Livrable | Échéance | Description |
|----------|----------|-------------|
| **L1.1** | T0 + 6 mois (06/2026) | Base de données traitée structure-activité-toxicité |
| **L1.2** | T0 + 9 mois (09/2026) | Modèles QSAR validés sur les cibles d'intérêt en oncologie pulmonaire |
| **L1.3** | T0 + 9 mois (09/2026) | Modèles QSTR validés sur les endpoints toxicologiques prioritaires |
| **L1.4** | T0 + 12 mois (12/2026) | Score B-R composite intégré et rapport de validation |

### Description des dépenses

| Poste | Détail |
|-------|--------|
| **Dépenses de sous-traitance** | Gradient Health : 40 k€ pour fourniture de jeux de données annotés et structurés. INRIA : 30 k€ pour support méthodologique sur l'ingénierie des modèles et la traçabilité des pipelines. **Total : 70 k€** |
| **Dépenses des achats** | Licences logicielles (RDKit Pro, bases de données ChEMBL/ToxCast), accès aux données réglementaires (labels FDA, rapports EMA). **Total : 25 k€** |
| **Contribution aux amortissements** | Serveurs GPU dédiés à l'entraînement des modèles QSAR/QSTR. **Total : 15 k€** |

---

## 4.2. LOT 2

| | |
|---|---|
| **Lot n°** | 2 |
| **Intitulé du lot** | Modèles prédictifs de transposition préclinique-clinique pour l'estimation du rapport bénéfice-risque à partir des données *in vivo* |
| **Nature du lot** | DE (Développement Expérimental) |
| **Durée** | 18 mois (06/2026 – 12/2027) |
| **Coût total du lot** | 750 k€ |

### Objectifs

L'objectif de ce lot est de construire une couche prédictive exploitant les données d'études précliniques *in vivo* (efficacité pharmacologique, toxicologie réglementaire, pharmacocinétique animale) pour prédire le profil B-R chez l'humain. Innovation majeure : un score de fiabilité par modèle préclinique et par pathologie. Ce lot constitue le deuxième niveau de résolution prédictive de BR-PREDICT.

### Travaux réalisés

| Tâche | Période | Description |
|-------|---------|-------------|
| **T2.1** | M6 – M9 (06/2026 – 09/2026) | **Préparation de l'infrastructure (mutualisée WP2/WP3/WP4).** Mise en place de l'infrastructure commune de stockage, d'indexation et de requêtage de la Profiling Base dédiée à BR-PREDICT. Extension du graphe de connaissances existant (100 milliards de points de données/relations). Configuration des environnements d'entraînement ML (GPU, MLflow). |
| **T2.2** | M6 – M12 (06/2026 – 12/2026) | **Qualification des sources de données *in vivo*.** Qualification de trois catégories : données d'efficacité préclinique (PDX, modèles transgéniques), données toxicologiques réglementaires (toxicité à doses répétées, génotoxicité, carcinogénicité), littérature avec issue clinique connue. |
| **T2.3** | M6 – M15 (06/2026 – 09/2027) | **Extraction NLP et structuration.** Adaptation des 24 Contextualizing SLMs d'ArcaScience pour extraire les données structurées nécessaires : modèle pathologique, doses, schéma posologique, endpoints d'efficacité (TGI, survie, réponse tumorale), indicateurs de toxicité (NOAEL, LOAEL, organes cibles). |
| **T2.4** | M9 – M18 (09/2026 – 06/2027) | **Création de la base traitée et structurée.** Base relationnelle liant chaque molécule à ses résultats précliniques, au modèle animal utilisé et à l'issue clinique connue. Estimation : 5 000 à 8 000 composés exploitables. |
| **T2.5** | M12 – M21 (12/2026 – 09/2027) | **Modèle ML de prédiction d'efficacité avec score de fiabilité.** Intégration d'un score de fiabilité par modèle préclinique et par pathologie, calculé à partir de la concordance historique. Concordance globale : ~57 % (modèles murins standard) à ~67 % (PDX). |
| **T2.6** | M12 – M21 (12/2026 – 09/2027) | **Modèle ML de prédiction de risque.** Architecture XGBoost adaptée, exploitant les descripteurs tabulaires. Entrées : paramètres dose-réponse (NOAEL/LOAEL, marges de sécurité), données toxicologiques qualitatives, variables de contexte. |
| **T2.7** | M18 – M24 (06/2027 – 12/2027) | **Validation et intégration.** Validation croisée, dataset indépendant (30 %), validation sur molécules commercialisées et ayant échoué en développement. Test de DeLong comparant WP1+WP2 vs WP1 seul. |

### Livrables

| Livrable | Échéance | Description |
|----------|----------|-------------|
| **L2.1** | T0 + 6 mois (06/2026) | Infrastructure commune opérationnelle (partagée avec WP3/WP4) |
| **L2.2** | T0 + 9 mois (09/2026) | Modèle NLP fonctionnel pour l'extraction de données *in vivo* |
| **L2.3** | T0 + 12 mois (12/2026) | Score de fiabilité par modèle préclinique et par pathologie, calibré sur l'oncologie pulmonaire |
| **L2.4** | T0 + 18 mois (06/2027) | Modèles ML prédictifs Bénéfices et Risques, basés sur les données *in vivo*, validés |

### Description des dépenses

| Poste | Détail |
|-------|--------|
| **Dépenses de sous-traitance** | Gradient Health : 50 k€ pour données RWE annotées et structurées. Cedars-Sinai : 35 k€ pour validation clinique sur cohortes rétrospectives. **Total : 85 k€** |
| **Dépenses des achats** | Bases de données précliniques (PubChem BioAssay, EPA ToxCast), licences logicielles. **Total : 30 k€** |
| **Contribution aux amortissements** | Infrastructure GPU/cloud pour entraînement des modèles. **Total : 20 k€** |

---

## 4.3. LOT 3

| | |
|---|---|
| **Lot n°** | 3 |
| **Intitulé du lot** | Modèles prédictifs pharmaco-génomiques pour l'estimation du rapport bénéfice-risque par intégration des biomarqueurs, cibles thérapeutiques et variants génétiques |
| **Nature du lot** | DE (Développement Expérimental) |
| **Durée** | 18 mois (06/2026 – 12/2027) |
| **Coût total du lot** | 850 k€ |

### Objectifs

L'objectif de ce lot est de construire la couche prédictive la plus granulaire de BR-PREDICT, exploitant les relations entre une drogue, ses cibles moléculaires, les biomarqueurs génomiques associés à une pathologie, et les polymorphismes génétiques influençant la réponse thérapeutique et la survenue d'effets indésirables. Ce lot couvre toutes les classes thérapeutiques et toutes les pathologies, avec une validation prioritaire en oncologie pulmonaire.

### Travaux réalisés

| Tâche | Période | Description |
|-------|---------|-------------|
| **T3.1** | M6 – M12 (06/2026 – 12/2026) | **Qualification des sources.** Deux axes : (i) bases de données biomarqueurs génomiques–pathologie (PharmGKB, ClinVar, COSMIC, OncoKB, cBioPortal), (ii) bases de variants génétiques des enzymes de métabolisation et des cibles thérapeutiques (UniProt, gnomAD, dbSNP, ClinGen, CPIC). |
| **T3.2** | M6 – M15 (06/2026 – 09/2027) | **Extraction NLP des polymorphismes génétiques et structuration fonctionnelle.** Adaptation des Contextualizing SLMs pour extraire les variants en trois catégories : polymorphismes constitutionnels (germinaux), variants somatiques tumoraux (mutations driver), et variants des cibles thérapeutiques. |
| **T3.3** | M9 – M18 (09/2026 – 06/2027) | **Base de données intégrée multi-dimensionnelle.** Structure de deux graphes relationnels complémentaires : Drogue ⇒ Biomarqueurs génomiques ⇒ Pathologie et Drogue ⇒ Cible ⇒ Variants ⇒ Impacts fonctionnels. |
| **T3.4** | M12 – M21 (12/2026 – 09/2027) | **Modèle ML de prédiction de bénéfice.** Architecture sur graphe (GAT ou Relational Graph Transformer) opérant sur le sous-graphe {molécule-cibles-biomarqueurs-pathologie}. Panel de ~100 associations de niveau de preuve 1 (PharmGKB 1A/1B). |
| **T3.5** | M12 – M21 (12/2026 – 09/2027) | **Modèle ML de prédiction du risque.** Exploitation des polymorphismes pharmacogénomiques constitutionnels (CYP2D6, DPYD, UGT1A1, etc.) et du mécanisme d'action de la molécule. Objectif : généraliser les relations {cible × molécule} par apprentissage. |
| **T3.6** | M18 – M24 (06/2027 – 12/2027) | **Validation et intégration.** Validation rétrospective sur cohortes de patients avec profil génomique et issue clinique connus (Cedars-Sinai, Mayo Clinic, ICM). Confrontation croisée WP1+WP3 pour évaluer le gain incrémental. |

### Livrables

| Livrable | Échéance | Description |
|----------|----------|-------------|
| **L3.1** | T0 + 9 mois (09/2026) | Pipeline opérationnel NLP pour extraction et structuration d'informations génétiques et pharmacogénomiques |
| **L3.2** | T0 + 12 mois (12/2026) | Base de données intégrée cibles ↔ biomarqueurs ↔ pathologie ↔ variants génétiques |
| **L3.3** | T0 + 18 mois (06/2027) | Modèles ML prédictifs de bénéfices et risques basés sur la génétique, validés |
| **L3.4** | T0 + 18 mois (06/2027) | Démonstration quantifiée de la capacité de prédiction B-R via génomique + cible. AUC > 0,80 (associations niveau 1A/1B), AUC > 0,75 (associations émergentes niveau 2) |

### Description des dépenses

| Poste | Détail |
|-------|--------|
| **Dépenses de sous-traitance** | ICM : 60 k€ pour accès aux cohortes génomiques et validation clinique. Mayo Clinic : 40 k€ pour données de cohortes et validation externe. **Total : 100 k€** |
| **Dépenses des achats** | Licences PharmGKB, ClinVar, accès bases COSMIC/OncoKB. **Total : 35 k€** |
| **Contribution aux amortissements** | Infrastructure GPU pour entraînement des modèles sur graphes. **Total : 20 k€** |

---

## 4.4. LOT 4

| | |
|---|---|
| **Lot n°** | 4 |
| **Intitulé du lot** | Extraction, structuration et modélisation prédictive des données de vie réelle (RWE) pour la validation et le renforcement des relations structure-cible-bénéfice-risque |
| **Nature du lot** | DE (Développement Expérimental) |
| **Durée** | 24 mois (07/2026 – 06/2028) |
| **Coût total du lot** | 1 100 k€ |

### Objectifs

L'objectif est double. Premièrement, construire un pipeline reproductible d'extraction et de normalisation des données de pharmacovigilance et des données de réponse thérapeutique en conditions réelles (FAERS, EDS hospitaliers). Deuxièmement, développer des modèles prédictifs exploitant ces données pour valider, compléter et corriger les profils B-R générés par les WP1-3. Ce lot est identifié comme le plus risqué du projet.

### Travaux réalisés

| Tâche | Période | Description |
|-------|---------|-------------|
| **T4.1** | M7 – M15 (07/2026 – 03/2027) | **Qualification des sources RWE.** Évaluation multicritère de chaque source (couverture, granularité, complétude MedDRA/CIM-10/ATC, biais). Protocole d'harmonisation rigoureux. Score de qualité composite ; seules les sources dépassant le seuil alimentent les modèles. |
| **T4.2** | M9 – M18 (09/2026 – 06/2027) | **Extraction et structuration.** Les Contextualizing SLMs extraient les entités des narratifs FAERS et des comptes rendus d'hospitalisation (EDS partenaires). Normalisation vers MedDRA 27.x, Ontologie ArcaScience, ChEBI. Module de dédoublonnage probabiliste et de pseudonymisation RGPD/HIPAA. |
| **T4.3** | M15 – M27 (03/2027 – 03/2028) | **Modèles prédictifs RWE – Bénéfices.** Fusion des variables RWE avec descripteurs moléculaires et précliniques. Architecture gradient-boosted (XGBoost/LightGBM) + attention temporelle (Temporal Fusion Transformer). Prédiction de la réponse thérapeutique (survie, réponse RECIST). |
| **T4.4** | M15 – M27 (03/2027 – 03/2028) | **Modèles prédictifs RWE – Risques.** Prédiction de la survenue d'EIG codés MedDRA PT dans les 6/12/24 mois. Validation croisée stratifiée par source. |
| **T4.5** | M24 – M30 (12/2027 – 06/2028) | **Validation et calibration.** Validation spécifique cancer du poumon sur cohortes rétrospectives indépendantes (Mayo Clinic, ICM). Calibration externe multi-sources. Analyse de sous-groupes (âge, comorbidités, ethnie). |

### Livrables

| Livrable | Échéance | Description |
|----------|----------|-------------|
| **L4.1** | EC1, fin 2026 (12/2026) | Pipeline d'extraction/structuration opérationnel ; grille de qualification appliquée à FAERS et à 2 EDS partenaires |
| **L4.2** | EC2, mi-2027 (06/2027) | Modèles prédictifs RWE B-R pour le cancer du poumon, rapport de calibration externe |
| **L4.3** | EC2 + 3 mois (09/2027) | Modèle généralisable intégrant données RWE + moléculaires + précliniques (WP1-3 + WP4), applicable à 2+ pathologies |
| **L4.4** | EC3, fin 2028 (12/2028) | Documentation complète du pipeline, code reproductible, rapport de validation multi-pathologies |

### Description des dépenses

| Poste | Détail |
|-------|--------|
| **Dépenses de sous-traitance** | Gradient Health : 80 k€ pour données RWE structurées et annotées. Cedars-Sinai / Mayo Clinic : 70 k€ pour accès EDS et validation externe. **Total : 150 k€** |
| **Dépenses des achats** | Accès bases FAERS, licences MedDRA 27.x, outils de normalisation terminologique. **Total : 40 k€** |
| **Contribution aux amortissements** | Infrastructure cloud/GPU pour traitement des volumes de données RWE. **Total : 30 k€** |

---

## 4.5. LOT 5

| | |
|---|---|
| **Lot n°** | 5 |
| **Intitulé du lot** | Conception et déploiement d'un graphe de connaissances interopérable intégrant les données moléculaires, précliniques, génomiques et de vie réelle dans une couche sémantique unifiée |
| **Nature du lot** | DE (Développement Expérimental) |
| **Durée** | 24 mois (01/2027 – 12/2028) |
| **Coût total du lot** | 550 k€ |

### Objectifs

L'objectif de ce lot est de créer un cadre de connaissances structuré et interopérable qui intègre de multiples sources de données hétérogènes (structures moléculaires, résultats précliniques, données génomiques, données de vie réelle) dans une couche sémantique unifiée. Ce Knowledge Graph (KG) sert d'ontologie fondamentale et d'architecture de données permettant de contextualiser, comparer et combiner les prédictions des L1-4.

### Travaux réalisés

| Tâche | Période | Description |
|-------|---------|-------------|
| **T5.1** | M13 – M18 (01/2027 – 06/2027) | **Conception ontologique.** Schéma modulaire : noyau partagé (*Molecule, Target, Pathway, Phenotype, AdverseEvent, Patient, ClinicalOutcome*). Alignement sur MedDRA, ChEBI, Gene Ontology, Disease Ontology, Reactome. Sous-ontologies pathologie-spécifiques (staging TNM, mutations driver). |
| **T5.2** | M15 – M24 (03/2027 – 12/2027) | **Harmonisation et mapping d'entités.** Pipeline de résolution d'entités (*entity linking*) combinant correspondance exacte (CAS, DrugBank ID, UniProt ID) et correspondance approximative (ANN + cross-encoder). |
| **T5.3** | M18 – M30 (06/2027 – 06/2028) | **Construction du KG.** Implémentation sur base graphe (Neo4j) + stockage RDF parallèle (SPARQL). Objectif : >100 000 entités et >1 million de relations au stade EC3, dont >95 % des arêtes avec score de confiance et provenance traçable. |
| **T5.4** | M18 – M33 (06/2027 – 09/2028) | **Extraction NLP et validation des relations.** Les 24 Contextualizing SLMs extraient en continu des relations à partir de la littérature et des données brutes. Processus de validation croisée : concordance entre SLMs, cohérence avec le KG, validation par échantillonnage expert. |
| **T5.5** | M24 – M36 (12/2027 – 12/2028) | **Interface de requête et API.** API RESTful et GraphQL exposant le KG. Requêtes multi-niveaux : simples, chemins causaux, profils B-R agrégés. Cache hiérarchique pour respect du KPI de latence < 2 secondes. |

### Livrables

| Livrable | Échéance | Description |
|----------|----------|-------------|
| **L5.1** | EC2, mi-2027 (06/2027) | Schéma ontologique finalisé, validé par le comité scientifique ; tables de correspondance WP1-3 livrées ; couverture ≥ 80 % des entités WP1-3 |
| **L5.2** | EC2 + 6 mois (12/2027) | KG peuplé avec intégration complète des données RWE (WP4) ; > 100 000 entités, > 1 million de relations |
| **L5.3** | EC3, fin 2028 (12/2028) | API opérationnelle testée selon les exigences WP6, documentation technique et guide d'utilisation, rapport qualité données (couverture, scores de confiance, taux de contradictions résolues) |
| **L5.4** | T0 + 30 mois (06/2028) | Rapport de qualité des données montrant la couverture et les scores de confiance |

### Description des dépenses

| Poste | Détail |
|-------|--------|
| **Dépenses de sous-traitance** | INRIA : 45 k€ pour support ontologique, méthodologique et alignement sur les standards internationaux. **Total : 45 k€** |
| **Dépenses des achats** | Licences Neo4j Enterprise, infrastructure de stockage, outils de visualisation de graphes. **Total : 20 k€** |
| **Contribution aux amortissements** | Serveurs dédiés au KG et à l'indexation. **Total : 15 k€** |

---

## 4.6. LOT 6

| | |
|---|---|
| **Lot n°** | 6 |
| **Intitulé du lot** | Conception, intégration et validation d'un *world model* capable de simuler des profils bénéfice-risque complets pour toute molécule en développement, par fusion multimodale des modèles prédictifs WP1-4 et du graphe de connaissances WP5 |
| **Nature du lot** | DE (Développement Expérimental) |
| **Durée** | 24 mois (01/2027 – 12/2028) |
| **Coût total du lot** | 1 300 k€ |

### Objectifs

L'objectif de ce lot est d'intégrer tous les modèles prédictifs (L1-4) avec le paysage de connaissances (L5) pour créer un « modèle du monde » capable de simuler des profils bénéfice-risque pour n'importe quelle molécule. Ce modèle prédit les résultats au niveau individuel, les interactions médicamenteuses et les risques spécifiques au contexte en apprenant les relations causales entre les propriétés moléculaires, les mécanismes biologiques et les caractéristiques des patients.

### Travaux réalisés

| Tâche | Période | Description |
|-------|---------|-------------|
| **T6.1** | M13 – M24 (01/2027 – 12/2027) | **Architecture du World Model.** Représentation en espace latent multimodal. Chaque drogue encodée comme vecteur latent z_drug issu d'un encodeur pré-entraîné sur la Profiling Base. Architecture conçue pour traiter l'absence de modalités comme cas par défaut. Module d'attention multimodale (cross-modal attention). |
| **T6.2** | M18 – M30 (06/2027 – 06/2028) | **Intégration d'ensemble WP1-4.** Méta-apprenante (stacking) combinant les prédictions individuelles et leurs intervalles de confiance. Module de résolution de conflits interrogeant le KG (WP5) pour identifier les variables confondantes. |
| **T6.3** | M21 – M33 (09/2027 – 09/2028) | **Modélisation causale et prédiction des interactions.** Graphe causal structurel (SCM) initialisé à partir du KG (WP5). Simulation de DDI, d'interactions gène-médicament, et de scénarios contrefactuels (ex. profil de sécurité pour métaboliseur lent CYP2D6). |
| **T6.4** | M24 – M33 (12/2027 – 09/2028) | **Quantification de l'incertitude.** Deep ensembles (10 répliques) + approximation variationnelle bayésienne. Décomposition des sources d'incertitude : épistémique vs aléatoire. Surcoût computationnel < 30 %. |
| **T6.5** | M27 – M36 (03/2028 – 12/2028) | **Interface de visualisation — Mental Map.** Frontend interactif projetant le profil B-R sous forme de réseau navigable. Molécule au centre, connectée à ses cibles, voies métaboliques, résultats cliniques. Filtrage par type de données, seuil de confiance, sous-population. |
| **T6.6** | M30 – M36 (06/2028 – 12/2028) | **Validation et calibration.** Phase rétrospective : ≥ 200 molécules commercialisées ou retirées. Phase prospective : monitoring chez les partenaires (Sanofi, Cedars-Sinai, ICM). Métriques : AUC-ROC > 0,8, taux de faux négatifs < 10 % (DDI), évaluation qualitative par panel d'experts (> 70 % « cliniquement plausible »). |

### Livrables

| Livrable | Échéance | Description |
|----------|----------|-------------|
| **L6.1** | EC2, mi-2027 (06/2027) | Architecture du world model validée, encodeurs pré-entraînés opérationnels, prototype d'intégration d'ensemble sur cancer du poumon |
| **L6.2** | EC3 – 6 mois (06/2028) | Module d'interactions (DDI, gène-drug), module d'incertitude fonctionnel, prototype Mental Map interactif |
| **L6.3** | EC3, fin 2028 (12/2028) | World model opérationnel intégrant WP1-5, rapport de validation rétrospective (≥ 200 molécules), rapport de validation prospective (monitoring partenaires), tests d'acceptation utilisateur avec ≥ 5 partenaires pharmaceutiques |
| **L6.4** | EC3, fin 2028 (12/2028) | Documentation utilisateur, matériaux de formation, système prêt au déploiement avec quantification de l'incertitude |

### Description des dépenses

| Poste | Détail |
|-------|--------|
| **Dépenses de sous-traitance** | AMI Labs : 60 k€ pour validation méthodologique et évaluation indépendante. Sanofi : 50 k€ pour validation clinique prospective sur cas d'usage réels. **Total : 110 k€** |
| **Dépenses des achats** | Infrastructure GPU haute performance (A100/H100), licences logicielles de visualisation, outils de monitoring ML. **Total : 50 k€** |
| **Contribution aux amortissements** | Serveurs GPU dédiés à l'entraînement du world model et aux deep ensembles. **Total : 40 k€** |

---

## 4.7. LOT 7

| | |
|---|---|
| **Lot n°** | 7 |
| **Intitulé du lot** | Management du projet |
| **Nature du lot** | Gestion |
| **Durée** | 36 mois (01/2026 – 12/2028) |
| **Coût total du lot** | 160 k€ |

### Objectifs

Ce work package vise à assurer la coordination globale du projet, le suivi administratif et scientifique, la diffusion des résultats, le développement des partenariats industriels nécessaires aux phases de test, ainsi que la gestion de la propriété intellectuelle issue des travaux de R&D.

### Travaux réalisés

| Tâche | Période | Description |
|-------|---------|-------------|
| **T7.1** | M1 – M36 (01/2026 – 12/2028) | **Reporting et suivi du projet.** Coordination globale, préparation des rapports périodiques à BPI France, suivi des jalons et livrables, réunions de pilotage régulières. |
| **T7.2** | M1 – M36 (01/2026 – 12/2028) | **Dissémination et valorisation scientifique.** Participation à des congrès internationaux (IA, recherche biomédicale), publications scientifiques, renforcement de la visibilité académique et industrielle. |
| **T7.3** | M1 – M24 (01/2026 – 12/2027) | **Discussions partenariales avec l'industrie pharmaceutique.** Identification de partenaires industriels pour les phases de test du WP6, définition des modalités de collaboration et d'accès aux données. |
| **T7.4** | M1 – M36 (01/2026 – 12/2028) | **Gestion de la propriété intellectuelle.** Veille permanente, préparation des éléments techniques et scientifiques, rédaction des dossiers de dépôt. Objectif : deux brevets correspondant aux principales innovations développées dans le cadre du projet. |

### Livrables

| Livrable | Échéance | Description |
|----------|----------|-------------|
| **L7.1** | T0 + 6 mois (06/2026), puis semestriel | Rapports de suivi du projet |
| **L7.2** | T0 + 12 mois (12/2026), puis annuel | Synthèse des actions de diffusion et de valorisation |
| **L7.3** | T0 + 36 mois (12/2028) | Deux brevets déposés correspondant aux principales innovations du projet |

### Description des dépenses

| Poste | Détail |
|-------|--------|
| **Dépenses de sous-traitance** | Cabinets de propriété intellectuelle et conseil réglementaire pour la préparation et le dépôt des brevets. **Total : 20 k€** |
| **Dépenses des achats** | Inscriptions congrès, frais de publication, outils de veille PI. **Total : 5 k€** |
| **Contribution aux amortissements** | Outils de gestion de projet et de reporting. **Total : 5 k€** |

---

### Récapitulatif budgétaire par lot

| Poste de dépense (k€) | Lot 1 | Lot 2 | Lot 3 | Lot 4 | Lot 5 | Lot 6 | Lot 7 | **Total** |
|----------------------|-------|-------|-------|-------|-------|-------|-------|---------|
| Personnel | 540 | 615 | 695 | 880 | 470 | 1 100 | 130 | **4 430** |
| Sous-traitance | 70 | 85 | 100 | 150 | 45 | 110 | 20 | **580** |
| Achats | 25 | 30 | 35 | 40 | 20 | 50 | 5 | **205** |
| Amortissements | 15 | 20 | 20 | 30 | 15 | 40 | 5 | **145** |
| **Total** | **650** | **750** | **850** | **1 100** | **550** | **1 300** | **160** | **5 360** |
