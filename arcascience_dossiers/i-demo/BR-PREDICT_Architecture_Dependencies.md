# BR-PREDICT -- Architecture, Dépendances & Gouvernance
## Diagramme de dépendances, Carte des artefacts (IO), Matrice RACI

**Programme** : BR-PREDICT -- Première plateforme d'évaluation prédictive du bénéfice-risque
**Porteur** : ArcaScience | **Pathologie d'ancrage** : Cancer du poumon

---

## 1. Diagramme de dépendances inter-WP

```
                ┌────────────────────────────────────────────────┐
                │   Evidence ingestion & contextualizing SLMs     │
                │ (high recall + high precision extraction stack) │
                └────────────────────────────────────────────────┘
                                   │
                                   ▼
        ┌─────────────────────────────────────────────────────────────┐
        │ WP5 — Semantic Layer + Ontology + Knowledge Graph (KG Spine) │
        │  - Unified schema + mappings + provenance + confidence       │
        │  - APIs for feature serving + audit trails                   │
        └─────────────────────────────────────────────────────────────┘
           │                │                   │                 │
           ▼                ▼                   ▼                 ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────────┐
│ WP1 Structure  │ │ WP2 Preclinical│ │ WP3 Targets/    │ │ WP4 Real-World      │
│ → priors + UQ  │ │ → tox modules  │ │ biomarkers/PGx  │ │ Evidence calibration│
│ (QSAR/GNN etc.)│ │ + reliability  │ │ personalization │ │ + drift monitoring  │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────────┘
           \___________   _____________   _____________   _____________/
                       \ /             \ /             \ /
                        ▼               ▼               ▼
           ┌───────────────────────────────────────────────────────────┐
           │ WP6 — WORLD MODEL (latent simulator for benefit–risk)      │
           │ - Multimodal fusion over KG evidence (not naive averaging) │
           │ - Temporal dynamics, uncertainty, counterfactuals          │
           │ - Explainability: "mental map" evidence → prediction       │
           └───────────────────────────────────────────────────────────┘
                                   │
                                   ▼
                ┌────────────────────────────────────────────────┐
                │     BR-PREDICT Decision APIs + Monitoring       │
                │  (deploy, validate, drift alerts, audit exports)│
                └────────────────────────────────────────────────┘
```

**Lecture du diagramme** :
- La couche d'ingestion (Contextualizing SLMs, 24 modèles) alimente l'ensemble du système en objets d'évidence structurés.
- **WP5** (KG Spine) est le pivot central : il unifie les terminologies et expose les données via API à tous les WPs.
- **WP1-4** sont les producteurs de prédictions par modalité, chacun consommant le KG et produisant des feature stores.
- **WP6** fusionne WP1-4 à travers WP5 pour produire le world model et les APIs de décision.

---

## 2. Carte des artefacts (Artifact IO Map)

Chaque WP est décrit comme une « boîte noire » : entrées consommées → artefacts produits.

### WP5 — Semantic Layer / KG Spine (alimente tous les WPs)

**Consomme :**
- Objets d'évidence bruts issus des Contextualizing SLMs (essais cliniques, publications, labels, rapports tox, RWE)
- Terminologies de référence (MedDRA, SNOMED CT, ChEBI, Gene Ontology, Disease Ontology, Reactome)
- Règles de schéma internes

**Produit (artefacts) :**

| Artefact | Description |
|----------|-------------|
| `KG_v1` | Schéma + nœuds/arêtes + provenance + scores de confiance |
| `MappingTables_v1` | Tables de correspondance inter-terminologies (crosswalks) |
| `EvidenceObjectSpec_v1` | Spécification des objets d'évidence canoniques |
| `FeatureServingAPI_v1` | API de service de features pour les modèles WP1-4 et WP6 |
| `AuditTrailAPI_v1` | API d'audit et de traçabilité |
| `CoherenceRules_v1` | Règles de gestion des contradictions, versionnage |

---

### WP1 — Structure → Priors & Uncertainty

**Consomme :**
- Entités moléculaires du `KG_v1` + endpoints labellisés (proxies efficacité/sécurité)
- Bibliothèques chimiques + jeux curés (molécules commercialisées/retirées, alertes tox)

**Produit (artefacts) :**

| Artefact | Description |
|----------|-------------|
| `StructureEncoder_v1` | Encodeur moléculaire (fingerprints/GNN) pré-entraîné |
| `QSAR_QSTR_Predictors_v1` | Têtes de prédiction par endpoint (efficacité + toxicité) |
| `ApplicabilityDomain_v1` | Module OOD + couverture du domaine d'applicabilité |
| `UQ_v1` | Incertitude calibrée ; hooks de politique d'abstention |
| `WP1_FeatureStore_v1` | Vecteurs de features + métadonnées pour WP6 |

---

### WP2 — Préclinique / In vivo / Tox → Modules translationnels

**Consomme :**
- Objets d'évidence préclinique du `KG_v1` (descripteurs d'études, endpoints)
- Métadonnées espèce/modèle et contexte pathologique

**Produit (artefacts) :**

| Artefact | Description |
|----------|-------------|
| `PreclinicalExtractorQA_v1` | Pipeline d'extraction NLP avec contrôle qualité |
| `TranslationalReliabilityScore_v1` | Score de fiabilité par modèle préclinique × pathologie |
| `ToxRiskModules_v1` | Prédicteurs toxicologiques ajustés pour les biais |
| `WP2_FeatureStore_v1` | Vecteurs de features + métadonnées pour WP6 |

---

### WP3 — Cibles / Biomarqueurs / Génétique → Couche de personnalisation

**Consomme :**
- Évidence cible-voie-biomarqueur du `KG_v1`
- Associations variants/phénotypes + endpoints biomarqueurs

**Produit (artefacts) :**

| Artefact | Description |
|----------|-------------|
| `MechanisticGraphFeatures_v1` | Features de graphe mécanistique (cibles → voies → outcomes) |
| `PatientContextEmbedding_v1` | Représentations patient prêtes pour la stratification |
| `GeneDrug_DrugTarget_Interactions_v1` | Modèle d'interactions gène-médicament et molécule-cible |
| `WP3_FeatureStore_v1` | Vecteurs de features + métadonnées pour WP6 |

---

### WP4 — RWE Calibration & Validité externe (FAERS / EDS / EHDS)

**Consomme :**
- Jeux RWE harmonisés et mappés sur le `KG_v1`
- Ensembles de facteurs confondants (comorbidités, co-médications, démographie)

**Produit (artefacts) :**

| Artefact | Description |
|----------|-------------|
| `RWE_CalibrationLayer_v1` | Courbes/paramètres de recalibration |
| `ConfoundingMitigationPipelines_v1` | Pipelines de mitigation des facteurs confondants |
| `SignalDetection_v1` | Module de détection de signaux de sécurité |
| `DriftMonitoring_v1` | Moniteur de dérive temporelle |
| `WP4_ValidationReports_v1` | Rapports de validation externe |

---

### WP6 — WORLD MODEL (Fusion + Simulation)

**Consomme :**
- `KG_v1` + `FeatureServingAPI_v1` (WP5)
- `WP1/2/3_FeatureStores_v1` + `WP4_CalibrationLayer_v1`

**Produit (artefacts) :**

| Artefact | Description |
|----------|-------------|
| `LatentStateModel_v1` | Représentation de l'état latent du world model |
| `FusionEngine_v1` | Attention sur l'évidence + gating par modalité |
| `CounterfactualEngine_v1` | Simulation d'interventions (dose, combo, population) |
| `UncertaintyEngine_v1` | Calibration bayésienne/ensemble de l'incertitude |
| `ExplainabilityMentalMap_v1` | Graphe d'évidence traçable → prédiction (carte mentale) |
| `BRPREDICT_API_v1` | API de décision grade-industriel |
| `DecisionGradeValidationReport_v1` | Rapport de validation rétrospective + prospective |

---

## 3. Matrice RACI (Who does what)

### Légende des rôles

| Abréviation | Rôle |
|-------------|------|
| **PM/Program** | Program manager / responsable livraison i-Demo |
| **PI/Chief Sci** | Directeur scientifique (BRA + IA) |
| **ML Lead** | Responsable architecture et entraînement des modèles |
| **Data Eng** | Responsable pipelines, stockage, performance |
| **Ontology Lead** | Responsable sémantique/KG + mappings terminologiques |
| **Pharmacoepi** | Responsable méthodes RWE, confounding/biais |
| **Clinical Safety** | Responsable endpoints, PV/BRA, validation domaine |
| **Reg/QA** | Responsable auditabilité, documentation, compliance-by-design |
| **Clinical Partner** | Centre clinique/hôpital (accès données + retour validation) |
| **Academic Partner** | Partenaire académique/méthodologique (benchmark indépendant) |

### Légende RACI

- **R** = Responsible (réalise le travail)
- **A** = Accountable (valide et signe)
- **C** = Consulted (consulté avant décision)
- **I** = Informed (informé après décision)

### Matrice

| Livrable / Cluster de tâches | PM | PI/Chief Sci | ML Lead | Data Eng | Ontology Lead | Pharmacoepi | Clinical Safety | Reg/QA | Clinical Partner | Academic Partner |
|-------|----|----|----|----|----|----|----|----|----|----|
| **WP5** EvidenceObjectSpec + schéma | C | A | C | R | R | C | C | C | I | C |
| **WP5** KG + mappings + règles de cohérence | I | A | C | R | R | C | C | C | I | C |
| **WP5** FeatureServingAPI + AuditTrailAPI | I | A | C | R | R | I | I | C | I | I |
| **WP1** Encodeurs structure + têtes QSAR/QSTR | I | A | R | C | C | I | C | I | I | C |
| **WP1** Domaine d'applicabilité + calibration incertitude | I | A | R | C | C | C | C | C | I | C |
| **WP2** Extraction préclinique QA + modules tox | I | A | R | R | C | C | C | I | C | C |
| **WP2** Score de fiabilité translationnelle | I | A | R | C | C | C | C | I | C | C |
| **WP3** Features graphe mécanistique + embeddings | I | A | R | C | R | I | C | I | I | C |
| **WP3** Modélisation interactions gène-drug / cible | I | A | R | C | R | C | C | I | I | C |
| **WP4** Harmonisation RWE vers KG | I | C | C | R | R | A | C | C | C | I |
| **WP4** Mitigation confounding + couche calibration | I | C | C | C | C | A/R | C | C | C | C |
| **WP4** Monitoring dérive + détection signaux | I | C | C | R | C | A/R | C | C | C | I |
| **WP6** Architecture world model + moteur fusion | I | A | R | C | C | C | C | C | I | C |
| **WP6** Moteur contrefactuel + incertitude | I | A | R | C | C | C | C | C | I | C |
| **WP6** Explicabilité « Mental Map » + exports audit | I | A | R | C | R | C | C | A/C | I | C |
| Validation end-to-end (rétrospective + pathologie ancrage) | C | A | R | C | C | R | R | C | C | C |
| Industrialisation : monitoring, docs, pack reproductibilité | A/R | C | C | R | C | C | C | A/R | I | I |

---

## 4. Flux de données synthétique

```
Sources brutes                    Extraction SLM              Unification WP5
─────────────                    ──────────────              ───────────────
Littérature ─────┐                                          ┌─→ KG (Neo4j+RDF)
Essais cliniques ─┤               24 Contextualizing        │   >100K entités
Labels/RCP ───────┼──→ Profiling ──→ SLMs (high recall ──→──┤   >1M relations
Rapports tox ─────┤    Base 100B     + high precision)      │   Provenance
FAERS/EDS/EHDS ───┘                                         └─→ APIs (REST/GraphQL)
                                                                    │
                            ┌───────────────────────────────────────┘
                            │
                            ▼
              ┌──────────────────────────────┐
              │   Feature Stores (WP1-4)      │
              │                              │
              │  WP1: z_mol (structure)      │
              │  WP2: z_preclin (in vivo)    │
              │  WP3: z_genomic (PGx)        │
              │  WP4: z_rwe (calibration)    │
              └──────────────────────────────┘
                            │
                            ▼
              ┌──────────────────────────────┐
              │   WP6 WORLD MODEL             │
              │                              │
              │  Fusion multimodale          │
              │  (cross-modal attention)     │
              │          │                   │
              │          ▼                   │
              │  SCM causal + contrefactuel  │
              │          │                   │
              │          ▼                   │
              │  Quantification incertitude  │
              │  (deep ensembles + bayésien) │
              │          │                   │
              │          ▼                   │
              │  Mental Map + BR-PREDICT API │
              └──────────────────────────────┘
                            │
                            ▼
              ┌──────────────────────────────┐
              │  Validation & Déploiement     │
              │                              │
              │  Rétrospective (200+ mol.)   │
              │  Prospective (partenaires)   │
              │  Monitoring + alertes dérive │
              │  Audit trail complet         │
              └──────────────────────────────┘
```

---

## 5. Correspondance artefacts → jalons i-Demo

| Jalon | Artefacts clés livrés | WPs contributeurs |
|-------|----------------------|-------------------|
| **M1 — Data & semantics readiness** (EC1, fin 2026) | `EvidenceObjectSpec_v1`, `KG_v1` (schéma), `MappingTables_v1`, pipelines extraction stables | WP5 (lead), WP1-4 (consommation) |
| **M2 — Modality predictors v1** (EC1-EC2) | `StructureEncoder_v1`, `QSAR_QSTR_Predictors_v1`, `TranslationalReliabilityScore_v1`, `MechanisticGraphFeatures_v1`, `RWE_CalibrationLayer_v1` | WP1, WP2, WP3, WP4 |
| **M3 — Integrated BR-PREDICT v1** (EC2, mi-2027) | `LatentStateModel_v1`, `FusionEngine_v1`, première évaluation end-to-end cancer du poumon | WP6 (lead), WP1-5 |
| **M4 — Decision-grade validation** (EC2-EC3) | `DecisionGradeValidationReport_v1`, stress-tests biais/confounding, généralisation N+ pathologies | WP4, WP5, WP6 |
| **M5 — Industrialisation** (EC3, fin 2028) | `BRPREDICT_API_v1`, `DriftMonitoring_v1`, documentation, pack reproductibilité, compliance | Tous WPs |
