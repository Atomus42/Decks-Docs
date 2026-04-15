# I-demo -- Réponses aux questions du comité d'évaluation

**BR-PREDICT / ArcaScience**

Avril 2026 -- Confidentiel

---

# Agenda

| # | Thématique | Questions |
|---|------------|-----------|
| 1 | Infrastructure & Ressources | Q1 |
| 2 | RH & Dissémination scientifique | Q2--Q3 |
| 3 | LLM & Explicabilité | Q4--Q5 |
| 4 | Trustworthy AI & Biais | Q6--Q7 |
| 5 | Validation & Golden Standard | Q8--Q10 |
| 6 | Monitoring & Déploiement on-premise | Q11--Q12 |
| 7 | Sous-traitance, PI & Qualité | Q13--Q16 |
| 8 | Structure capitalistique & Financement | Q17--Q23 |
| 9 | Modèle économique & Positionnement | Q24--Q30 |

30 questions -- 1 slide par question -- réponses structurées et sourcées depuis le dossier V7 et les Work Packages

---

# Q1 -- Capacités de stockage et calcul

> *De quelles capacités de stockage et de calcul dispose actuellement ArcaScience ? Quels sont les sous-traitants ? Des dépenses de cette nature sont précisées dans les WP5 (infra Neo4j cloud) et WP6 (cloud GPU haute performance), quelles ressources sont allouées aux WP1-4 ?*
>
> What storage and computing capabilities does ArcaScience currently have? Who are the subcontractors? What resources are allocated to WP1-4?

## Plateforme actuelle

- DataFactory BRA indexe **>40 millions d'entrées textuelles** (PubMed, MEDLINE, registres d'essais cliniques)
- Feuille de route technique définie sous la tâche **T2.1**, planifiée pour Q2--Q3 2026

## Calcul

- **WP1 et WP2** fonctionnent sur **clusters CPU standards** -- pas de GPU nécessaire
- **WP3, WP4 et WP6** requièrent des **environnements GPU supplémentaires** -- spécifications dimensionnées après expériences de validation focalisées
- **MLflow** pour l'automatisation des tâches ML, tracking des expériences, versioning des modèles et stockage des artefacts

## Stockage

- Extension de l'infrastructure existante pour les datasets WP-spécifiques (Fichiers plats sur **Buckets S3**, **ElasticSearch**, **Qdrant**)
- KG WP5 évalué sur **Neo4j** et des backends analytiques alternatifs optimisés pour les charges de requêtes, avec **benchmarks cold/cached comme KPIs WP5**

## Sous-traitants

- **Infrastructure :** Cloud agnostique, multi-cloud **Scaleway + AWS** (~200K EUR/an total)
- **Partenaires identifiés :** INRIA (support méthodologique), Gradient Health (données RWE structurées), AMI Labs (évaluation méthodologique indépendante)

**Clarification importante :** La mention de « 100 milliards de relations » dans WP6 correspond au recours à des **encodeurs pré-entraînés externes** (ChemBERTa, PubMedBERT, ESM-2), et non un entraînement from scratch

**WP : Cross-WP / Infrastructure**

---

# Q2 -- ETP prévus par WP et profils

> *Quels sont les ETP prévus par WP et pour quels types de profils ?*
>
> What are the planned FTEs per WP and for what types of profiles?

## À compléter -- RH / Direction

| WP | IT (ETP) | R&D (ETP) | Médical (ETP) |
|----|----------|-----------|---------------|
| WP1 | — | — | — |
| WP2 | — | — | — |
| WP3 | — | — | — |
| WP4 | — | — | — |
| WP5 | — | — | — |
| WP6 | — | — | — |
| WP7 | — | — | — |

## Proposition de réponse (DRAFT -- à valider par RH / Direction)

Estimation basée sur les périmètres WP et le plan de recrutement 2026 :

| WP | IT (ETP) | R&D (ETP) | Médical (ETP) |
|----|----------|-----------|---------------|
| WP1 | 1.5 | 2.0 | 0.5 |
| WP2 | 1.5 | 2.0 | 1.0 |
| WP3 | 1.0 | 2.0 | 1.0 |
| WP4 | 1.5 | 1.5 | 1.0 |
| WP5 | 2.0 | 1.5 | 0.5 |
| WP6 | 2.0 | 3.0 | 1.0 |
| WP7 | 0.5 | 0.5 | 0.5 |
| **Total** | **10.0** | **12.5** | **5.5** |

Total ~28 ETP -- aligné avec le plan de 47 postes dont 27 R&D

**WP : Cross-WP / RH**

---

# Q3 -- Dissémination scientifique & CIFRE

> *Dissémination scientifique : 4 doctorants CIFRE sont prévus (IA, pharmacologie et réglementaire). Pourront-ils publier ? Quelle articulation avec la stratégie PI (brevets et secret) ?*
>
> Will the 4 CIFRE doctoral students be able to publish? How does this align with the IP strategy (patents and trade secrets)?

## Expérience académique

- L'équipe dirigeante maîtrise les pré-requis CIFRE : VS a dirigé **19 thèses** dont **2 CIFRE** (Sanofi et Servier)
- Équilibre entre découvertes scientifiques originales et applications industrielles intégré dès la définition du sujet

## Stratégie de publication

- **Les doctorants pourront publier** -- essentiel pour la validation de leur thèse
- Objectif : **5 publications annuelles** pour établir ArcaScience comme acteur de référence international sur la prédiction du bénéfice-risque

## Protection IP

- **Brevets** sur pipeline de gestion/indexation de données d'entraînement
- **Secret industriel** sur les architectures propriétaires et la Profiling Base
- Stratégie définie dès le sujet de thèse, réévaluée régulièrement
- Si obstacle à la publication anticipé (situation très peu probable car tout sera cadré à l'avance) → stratégie modifiée

**WP : Gouvernance / IP**

---

# Q4 -- LLM pour résumés et rapports

> *Il est fait mention de LLM pour générer les résumés et rapports. S'agit-il d'un modèle propriétaire ? Quelle est la solution utilisée ?*
>
> LLMs are mentioned for generating summaries and reports. Is it a proprietary model? What solution is used?

## Solution actuelle

- Utilisation de **Mistral**, déployé sur nos propres serveurs GPU hébergés chez **Scaleway**

## Trois impératifs

- **Souveraineté des données :** aucune donnée ne transite par des APIs tierces
- **Souveraineté technologique :** modèle open-source, pas de dépendance contractuelle
- **Flexibilité :** évaluation continue des nouveaux modèles (Llama, Gemma, Qwen)

## Architecture

- Déploiement on-premise sur infrastructure Scaleway
- Capacité d'intégrer rapidement les modèles les plus performants sans contrainte contractuelle
- Suivi actif de l'évolution très rapide des LLMs open-source et souverains

**WP : Cross-WP / Infrastructure**

> **Note présentateur (ne pas afficher) :** Contrairement au dossier, nous utilisons actuellement des modèles OpenAI pour la summarization et les rapports. Ce point doit être clarifié avant la présentation.

---

# Q5 -- Transparence des BDD et explicabilité

> *Quelle transparence des BDD (publiques et privées) utilisées par la plateforme auprès des clients/utilisateurs finaux ? La traçabilité des analyses et des prédictions est un argument mis en avant, comment l'explicabilité se traduit-elle pour l'utilisateur ?*
>
> What transparency is provided regarding the databases used? How does explainability translate for the user?

## Explicabilité des modèles

- **Essentielle dans la construction** : vérification de cohérence, validation des relations entre mécanismes et outputs (efficacité ou toxicité)
- Un modèle **explicable et validé** sera plus robuste qu'un modèle « black-box »
- Côté client/utilisateur final : éléments mécanistiques explicables consultables, mais l'essentiel reste la **performance prédictive** (VPP et VPN)

## Bases de données utilisées (DRAFT -- à valider par VS / Théo)

**Publiques :**
- ChEMBL, PubMed, MEDLINE, ClinicalTrials.gov, FAERS, DisGeNET, PharmGKB, ClinVar, ToxCast, WITHDRAWN

**Privées / partenaires :**
- Sanofi (données internes), Cedars-Sinai (EDS), Mayo Clinic (EDS), ICM (cohortes)

## Explicabilité par couche (DRAFT -- à valider par VS / Théo)

- **SLM :** provenance documentaire de chaque extraction
- **KG (WP5) :** provenance au niveau de chaque arête, score de confiance, niveau de preuve
- **WP6 :** SHAP values, attention weights, explications en langage naturel

**WP : Cross-WP**

---

# Q6 -- Problématiques de Trustworthy AI

> *Comment sont adressées les problématiques de trustworthy AI ?*
>
> How are trustworthy AI issues addressed?

## Briques en place

| Pilier | Implémentation |
|--------|---------------|
| **Explicabilité** | SHAP, attention weights, explications en langage naturel (WP6) |
| **Traçabilité** | MLflow pour le versioning ; provenance au niveau des arêtes dans le KG ; audit trail via API sécurisée |
| **Quantification de l'incertitude** | Variance inter-modèles (ensemble), OOD detection, intervalles de confiance explicites, décomposition incertitude (T6.4) |
| **Conformité réglementaire** | Architecture compatible ICH E2C(R2) et CIOMS XII ; alignement FDA, EMA et PMDA |
| **Positionnement éthique** | Outil d'aide à la décision (usage pharma R&D), non dispositif médical (MDR/IVDR non applicable) ; veille continue |
| **Gouvernance des données** | Accords institutionnels, dé-identification des données patient, approbations comités d'éthique (WP4) |

## Framework RAISE (DRAFT -- à valider par VS / Théo)

- **Accountable :** MLflow audit trail, provenance KG, comité scientifique
- **Fair & Ethical :** dé-identification, détection biais ethniques (WP3), biais de publication (WP2)
- **Robust & Safe :** ensemble models, OOD detection, validation multi-niveaux, plan de mitigation par WP
- **Transparent & Explainable :** SHAP, Mental Map (T6.5), explications en langage naturel
- **Eco-Responsible :** optimisation architectures attention-free (T6.1), overhead <30%

**WP : WP6 / Cross-WP**

---

# Q7 -- Détection et correction des biais

> *Quelle est la stratégie pour détecter et corriger les biais dans le World Model ? Comment est-ce qu'elle s'intègre dans le planning du projet ?*
>
> What is the strategy for detecting and correcting biases in the World Model? How does it fit into the project timeline?

## Biais identifiés dans le projet

- **Biais de publication** (WP2) -- sous-représentation des résultats négatifs
- **Biais de sélection d'efficacité** (WP2)
- **Biais de représentation ethnique** dans les cohortes génomiques (WP3)
- **Sous-déclaration** dans les données RWE / FAERS (WP4)
- **Biais des études publiées** affectant la qualité des modèles (cross-WP)

## Stratégie de correction

- **Audit Knowledge Graph** (WP5) : détection de contradictions entre relations
- **Détection hors-distribution** (OOD) : avertissements explicites lorsque le modèle extrapole au-delà de sa zone de confiance
- **Monitoring prospectif continu** avec les partenaires (T6.6)

## Intégration dans le planning

- WP2 (Q1--Q3 2026) : pondération des sources par exhaustivité, registres d'études négatives
- WP3 (Q2 2026--Q3 2027) : stratification par population, signalisation des sous-groupes sous-représentés
- WP5 (Q3 2027--Q2 2028) : pipeline de détection de contradictions opérationnel
- WP6 (Q1 2027--Q4 2028) : décomposition des sources d'incertitude intégrée

**WP : WP6**

> **Note présentateur (ne pas afficher) :** Gap documenté -- une stratégie formalisée et unifiée de correction des biais pour le World Model (WP6) n'est pas encore spécifiée dans le dossier. C'est un point ouvert identifié.

---

# Q8 -- Validation Golden Standard

> *Concernant la validation des modèles avec un golden standard, de quel dataset s'agit-il ? (ex. p32)*
>
> Regarding model validation with a golden standard, which dataset is this?

## Qualités médicales Gold Standard

- Données cliniques vérifiées par des ARC qualifiés, critères diagnostiques selon les **référentiels les plus récents**
- Données manquantes **<10%** avec stratégie claire de gestion et d'imputation
- Contrôles qualité rigoureux sur toutes les données biologiques/imagerie -- jeux de qualité insuffisante exclus

## NLP extraction (WP2, WP3, WP4)

- Datasets **annotés manuellement** avec cliniciens, guidelines co-développées avec experts domaine
- F1 per-field cible **>0.85**, complétude record-level cible **>0.70**
- Validation externe : Sanofi (**96% couverture risque, 97% bénéfice**), DisGeNET (**92% top 30 biomarqueurs**)

## Modèles prédictifs (WP1--WP4, WP6)

- Panel de référence oncologie pulmonaire : **succès** (osimertinib, alectinib, lorlatinib) et **échecs** (buparlisib, idelalisib, selumetinib, vandetanib)
- Base **WITHDRAWN** : 578 médicaments retirés + molécules FDA boxed warning
- **~4 500 molécules commercialisées** avec profils B-R documentés (ChEMBL v35)

## World Model (WP6)

- Validation rétrospective : **≥200 molécules** dont les profils B-R réels sont connus
- Validation prospective : monitoring chez partenaires (Sanofi, Cedars-Sinai, Mayo Clinic, ICM)
- Panel d'experts : **≥5 partenaires pharmaceutiques**, cible **≥70% « cliniquement plausible »**

Le golden standard n'est **pas un dataset unique** mais un **cadre de validation stratifié** conçu pour tester différents aspects du système à chaque niveau de prédiction

**WP : Cross-WP**

---

# Q9 -- Absence de biais -- études rétrospectives

> *Sur les études rétrospectives prévues, comment pensez-vous garantir l'absence de biais (ex. données relatives à la molécule commercialisée dans le(s) modèle(s) utilisé(s)) ?*
>
> For the planned retrospective studies, how do you intend to ensure the absence of bias?

## Prévention fuite de données (data leakage)

- **Temporal split** : hold-out period 2022--2025 pour données post-cutoff
- **Leave-drug-out cross-validation** : la molécule évaluée est entièrement exclue de l'entraînement (composés, analogues, données cliniques)
- **Nested cross-validation** pour optimisation des hyperparamètres
- WP1 : **leave-one-scaffold-out** pour généralisation à de nouvelles structures chimiques
- Conformité auditée à chaque jalon (EC1, EC2, EC3)

## Biais de survie (survivorship bias)

- Validation **non limitée aux médicaments approuvés** : inclut la base WITHDRAWN (578 retraits) + FDA boxed warnings
- WP2 : inclut molécules ayant échoué en développement clinique (efficacité insuffisante ou toxicité inacceptable)

## Contrôle des facteurs confondants (WP4 RWE)

- **Analyse de sous-groupes** : âge, comorbidités, ethnie déclarée
- **Cross-validation stratifiée par source** pour éviter la dominance d'une base
- Ajustements statistiques pour biais de sélection identifiés dans chaque source RWE

## Barrière informationnelle

- Panel de référence défini **prospectivement**, verrouillé avant développement WP1
- Jeu de validation WP6 (≥200 molécules) défini indépendamment
- **Évaluation en aveugle** pendant la phase de prédiction

**WP : Cross-WP**

---

# Q10 -- Méthodologie validation par experts

> *Il est fait mention de la validation utilisateurs par des experts évaluateurs (de partenaires externes) jugeant les prédictions comme « cliniquement plausibles ». Pouvez-vous expliciter la méthodologie envisagée pour cette évaluation ?*
>
> Can you elaborate on the methodology for expert evaluator validation of predictions as "clinically plausible"?

## Approche knowledge-driven

- Experts sélectionnés sur la base d'un profil **physician-scientist**, avec expertise à l'interface entre physiopathologie, mécanismes et soins cliniques
- Chaque prédiction = **un outcome** (bénéfice ou risque) + **un mécanisme sous-jacent** (structure moléculaire, expression génique) ou combinaison de mécanismes

## Trois catégories de validation

| Catégorie | Signification | Impact |
|-----------|--------------|--------|
| **1) Connexion déjà décrite** | Mécanisme documenté dans la littérature | Validation littérature |
| **2) Connexion compatible** | Non décrite mais cohérente avec les connaissances existantes | Nouveau mécanisme potentiel identifié par le modèle |
| **3) Connexion incompatible** | Non décrite et incompatible avec les connaissances | Prédiction non validée |

## Passage à l'échelle

- Possibilité de compléter le travail expert par des **LLMs** pour valider un grand nombre d'hypothèses
- Objectif : mesures **statistiquement significatives** de la puissance prédictive, sensibilité et spécificité

**WP : WP6**

---

# Q11 -- Stratégie de monitoring

> *Monitoring : quelle est la stratégie envisagée pour le World Model ? Qu'est-ce qui est mis en place actuellement sur la plateforme Trial Balancer ?*
>
> Monitoring: what is the strategy for the World Model? What is currently in place on Trial Balancer?

## Trial Balancer -- actuellement en place

- Réévaluation des modèles **tous les 3--6 mois** selon criticité
- Mise à jour continue : détection automatique de nouvelles publications, analyse et intégration
- SLM : **F1 entre 80% et 95%** selon le modèle ; modèle appraisal : **précision 80--95%**
- Monitoring infrastructure via **Prometheus et Grafana**

## World Model (BR-PREDICT) -- stratégie planifiée

- **Monitoring performance modèle :** évaluation continue, retraining basé sur triggers (pas calendaire)
- **Détection de drift :** vérification automatique de la distribution des features vs. hypothèses d'entraînement
- **Maintenance KG (WP5) :** mises à jour continues (nouveaux médicaments approuvés, nouvelles cibles, nouveaux EI, mises à jour ontologiques)
- **Monitoring incertitude (T6.4) :** augmentation de la proportion de prédictions à haute incertitude = signal de dégradation
- **MLflow :** versionnage complet, rollback si une mise à jour dégrade les performances
- **Post-déploiement on-premise :** chaque résultat traçable, monitoring sous règles compliance client

**WP : WP6**

> **Note présentateur (ne pas afficher) :** Certaines affirmations ne reflètent pas la réalité actuelle, notamment l'existence des modèles WP6, les performances modèles décrites, et le monitoring infrastructure. Ces éléments sont des objectifs, pas l'état actuel. Formuler au futur.

---

# Q12 -- Infrastructure déploiement on-premise

> *Quelles sont les caractéristiques (stockage, ressources de calcul) des infrastructures nécessaires à un client pour le déploiement de la plateforme on-premise ?*
>
> What infrastructure characteristics (storage, computing) are required by a client for on-premise deployment?

## Architecture de déploiement

- **Docker** (isolation) + **Kubernetes** (orchestration microservices) + **Ansible/Terraform** (automatisation installation)
- Outils DevOps open-source standards, compatibles avec l'IT pharma existant
- Solution **autonome post-installation** ; accès ArcaScience compatible avec les règles compliance client

## Calcul -- inférence uniquement

- Tout l'entraînement est réalisé **chez ArcaScience** avant déploiement → besoins calcul client drastiquement réduits
- **CPU :** WP1 et WP2 sur serveurs enterprise standards
- **GPU :** composants DL (WP3 Graph Attention Network, WP4 Temporal Fusion Transformer, WP6 ensemble) → **un GPU enterprise** (NVIDIA T4 ou A10)
- Optimisation active : architectures attention-free évaluées (T6.1), overhead **<30%** vs. passe standard

## Stockage

- Base structurée : capacités enterprise standards (dépend du périmètre projet)
- Stockage documentaire : **Elasticsearch + vector embeddings** pour recherche sémantique

## Sécurité & conformité

- Chiffrement **AES 256-bit**, protocoles **HIPAA-compatibles**
- Données client indexées **sur le serveur du client uniquement**
- **Aucune donnée client** ne transite par des APIs externes ou services cloud

**WP : Cross-WP / Déploiement**

> **Note présentateur (ne pas afficher) :** Aucun de ces éléments ne reflète la réalité actuelle. Ce sont des capacités planifiées et des objectifs d'architecture. Formuler ces points comme la cible de déploiement, pas comme l'état existant.

---

# Q13 -- Stratégie RH -- profils rares

> *Le projet présente une stratégie de croissance RH ambitieuse. Quelle est la stratégie pour s'assurer de trouver les profils adéquats, potentiellement rares sur le marché ?*
>
> What is the strategy for ensuring that adequate profiles, potentially rare on the market, can be found?

## À compléter -- RH / Direction

## Proposition de réponse (DRAFT -- à valider par RH / Direction)

- **Pipeline CIFRE :** 4 doctorants en IA, pharmacologie et réglementaire -- vivier académique directement intégré au projet
- **Co-supervision INRIA :** accès au réseau de chercheurs seniors en ML/IA pour les profils R&D les plus pointus
- **Sourcing international :** partenariats Sanofi, Cedars-Sinai, Mayo Clinic comme canaux de recrutement (physician-scientists, data scientists cliniques)
- **Plan de recrutement 2026 :** 47 postes dont 27 R&D -- recrutement échelonné aligné sur les jalons WP
- **Packages compétitifs :** equity + participation au projet I-demo comme levier d'attractivité
- **Équipe fondatrice expérimentée :** VS (19 thèses dirigées), expertise en encadrement scientifique

**WP : Gouvernance / RH**

---

# Q14 -- Scénarios alternatifs -- défaillance WP

> *Y a-t-il des scénarios alternatifs prévus en cas de défaillance d'un WP (difficulté d'accès à une BDD, absence de validation d'un modèle…) ?*
>
> Are there alternative scenarios in case of WP failure (database access issues, model validation failure)?

## Accès aux données

- Anticipation : jusqu'à **50% des BDD** peuvent ne pas être exploitables (qualité, contrats, délais)
- Stratégie : **multiplication des sources et partenaires** -- aucun n'est indispensable
- **WP4 (RWE) :** risque plus élevé mais non bloquant : « WP dont la faisabilité ne compromet pas le projet global, aucune dépendance stricte ; WP1-3 et WP5 suffisent pour un modèle original et ambitieux »
- **WP1--3 :** sources principalement publiques (ChEMBL, ToxCast, PharmGKB, ClinVar…) -- risque d'accès faible

## Absence de validation d'un modèle

- Validation = **notion multi-niveaux** : 1) in silico, 2) basée sur les connaissances, 3) expérimentale
- Validation **quantitative et par tâche** -- un modèle peut être validé partiellement
- Si validation insuffisante → **analyse des causes** → 1) boucle rétroactive pour améliorer la structure, 2) ajout de données ciblées

## Architecture résiliente

- **WP1--4 indépendants :** chacun délivre une valeur standalone
- WP6 World Model : gère les modalités manquantes via **learned mask tokens** (mode dégradé mais robuste)
- WP6 = **axe exploratoire** (recherche de frontière, pas ingénierie appliquée) -- validé par expériences focalisées avant engagement complet

## Validation médicale -- passage en production

Valider un modèle implique plusieurs étapes avant production :
- **Standards multi-points** qualitatifs et quantitatifs appliqués systématiquement
- Pas de mise en production tant que les seuils de performance (AUC, F1, calibration) ne sont pas atteints
- Outil d'**aide à la décision** (non dispositif médical) -- pas de risque direct pour les patients

**WP : Cross-WP**

---

# Q15 -- Sous-traitance INRIA et PI

> *Quelle est la nature de la sous-traitance de l'INRIA et quels sont les profils impliqués du côté de ce prestataire ? Y a-t-il un partage de la PI ?*
>
> What is the nature of INRIA's subcontracting? What profiles are involved? Is there IP sharing?

## À compléter -- Direction / Cabinet Carrel

## Proposition de réponse (DRAFT -- à valider par Direction / Cabinet Carrel)

### Nature de la sous-traitance

- **Support méthodologique** sur WP5 (Knowledge Graph) et WP6 (World Model)
- Expertise en graphes de connaissances, raisonnement causal, modélisation ML

### Profils INRIA

- Chercheurs seniors en ML/IA, spécialistes graphes et ontologies
- Co-supervision des thèses CIFRE liées aux axes WP5/WP6

### Partage de la PI

- **Background IP :** retenue par chaque partie
- **Foreground IP :** co-propriété avec droits d'exploitation exclusifs pour ArcaScience dans le domaine pharma B-R
- **Publications :** soumises à un délai de confidentialité (typiquement 6 mois) pour permettre le dépôt de brevets le cas échéant

**WP : WP5 / WP6**

---

# Q16 -- Management traçabilité et qualité

> *Quelle est la stratégie de management de la traçabilité et de la qualité des développements prévus dans les WP ? Quelles méthodes et outils seront mis en place ?*
>
> What is the management strategy for traceability and quality of the developments planned in the WPs?

## Cadre de contrôle qualité

- Contrôle qualité **à toutes les étapes** : cohortes patients, données, traitement, intégration dans le modèle, structure du modèle, performances
- **SOPs préparées à l'avance** et suivies de façon rigoureuse
- SOPs **transmises à tous les partenaires** pour garantir la qualité et l'homogénéité des procédures

## Outils

| Outil | Fonction |
|-------|----------|
| **MLflow** | Versioning modèles, tracking expériences, stockage artefacts |
| **SonarQube** | Quality gate sur chaque mise en production |
| **Prometheus / Grafana** | Monitoring infrastructure et disponibilité |
| **API sécurisée** | Audit trail complet |

## Attention particulière aux biais

- Détection et mitigation **systématiques** à chaque étape
- Objectif : modèle basé sur des **éléments cliniques et biologiques robustes** en diminuant les biais et le bruit inhérents à toute donnée biomédicale

**WP : Cross-WP / Qualité**

---

# Q17 -- Discussions partenariales pharma (T7.3)

> *Pourquoi les discussions partenariales avec l'industrie pharmaceutique (T7.3) s'arrêtent à M24 sur le diagramme de Gantt ? Quelle est la portée de ces discussions ? (accès aux BDD privées, accès datasets de validation… ?)*
>
> Why do partnership discussions with pharma (T7.3) stop at M24? What is their scope?

## À compléter -- Direction / Stratégie commerciale

## Proposition de réponse (DRAFT -- à valider par Direction / Stratégie commerciale)

### Portée des discussions T7.3

- Accès aux **BDD privées** (EDS Cedars-Sinai, Mayo Clinic, données internes Sanofi)
- Accès aux **datasets de validation** pour calibration des modèles
- Accords de **co-développement** sur des indications spécifiques
- Contrats **early adopter** avec conditions préférentielles

### Pourquoi M24 sur le Gantt

- Le Gantt ne montre que la tâche formelle **« négociation partenariale »**
- Les discussions **continuent au-delà de M24** sous le volet commercial de WP7
- Après M24, les partenariats signés **entrent en phase d'exécution** (accès données, validation, co-développement)

### Pipeline commercial

- 5-7 nouveaux logos ciblés par trimestre
- Expansion des comptes existants
- Motion **disease-specific-first** : les versions thérapeutiques compressent les cycles de vente de 40-60%

**WP : WP7**

---

# Q18 -- KG publics et interopérabilité

> *WP5 : les graphes publics de référence sont-ils utilisés par des concurrents ? Pourquoi une interopérabilité avec ces KG n'est-elle pas envisagée ?*
>
> Are the public reference graphs used by competitors? Why is interoperability with these KGs not considered?

## Positionnement vs KG publics

- **DRKG** (5.9M arêtes non pondérées) et **PrimeKG** (4M relations sans statut causal) cités comme baseline de comparaison
- **BR-PREDICT KG** : **>95% des arêtes** annotées avec scores de confiance, provenance traçable (source WP, origine données) et niveau de preuve (RCT > cohorte > cas rapporté > in silico)
- Chaque arête typée : **causal-validé**, **directionnel-inféré**, ou **associatif** -- seuls les deux premiers alimentent le SCM (WP6)

## Pourquoi pas d'import depuis les KG publics

- KG publics **sans statut causal, sans scores de confiance, ni provenance** → incompatibilité qualité fondamentale
- Import contaminerait le KG avec des relations non qualifiées → **dégradation de l'auditabilité réglementaire**
- Exigences **ICH E2C(R2) et CIOMS XII** imposent une traçabilité complète

## Interopérabilité effective

- **Stockage RDF parallèle** pour interopérabilité SPARQL
- Alignement sur **ontologies standards** : MedDRA, ChEBI, Gene Ontology, Reactome, Disease Ontology
- Architecture **interopérable au niveau ontologique** -- ne consomme pas les KG publics comme input

La non-interopérabilité est un **choix délibéré de qualité**, pas un oubli

**WP : WP5**

---

# Q19 -- AMI Labs -- évaluation précoce

> *AMI Labs intervient en tant que prestataire en fin de projet pour définir la méthodologie d'évaluation. Quelles sont les motivations de ne pas intégrer l'évaluation dès les premières phases de développement de la solution ?*
>
> Why is AMI Labs' evaluation methodology not integrated from the earliest development phases?

## Raison pragmatique

- Le World Model **n'existe pas avant M18--M30** → rien à évaluer de façon intégrée avant cette date
- AMI Labs intervient quand le système est suffisamment mature pour une **évaluation méthodologique indépendante**

## Évaluation per-WP existante dès le début

- Chaque WP (1--4) dispose de **son propre protocole de validation** avec KPIs définis
- Validation continue tout au long du développement : F1, AUC, calibration, etc.
- La validation n'attend pas AMI Labs -- elle est intégrée dans chaque WP

## Amélioration identifiée

- Une **consultation méthodologique précoce** avec AMI Labs sur les protocoles per-WP aurait été justifiable
- Ce point sera **intégré plus tôt dans la réalisation du projet**

**WP : WP6**

---

# Q20 -- Structure capitalistique et juridique

> *Une opération affectant la structure juridique et/ou capitalistique de votre structure est-elle envisagée dans les deux ans à venir ?*
>
> Is any operation affecting the legal and/or capital structure planned within the next two years?

## À compléter -- Direction / Cabinet Carrel

## Proposition de réponse (DRAFT -- à valider par Direction / CEO)

- **Levée de fonds** prévue dans les 12--18 prochains mois pour soutenir l'exécution du plan I-demo
- **Structure juridique stable** -- SAS de droit français
- Pas de fusion, scission ou changement de forme juridique envisagé
- Accompagnement juridique : **Cabinet Carrel** (fondé par l'ex-directrice d'Inserm Transfert)

**WP : Gouvernance**

---

# Q21 -- Levée de fonds

> *Votre structure envisage-t-elle une levée de fonds dans les deux ans à venir ? Si oui, pouvez-vous nous indiquer l'identité des investisseurs/fonds d'investissement, les montants envisagés et le calendrier ?*
>
> Is a fundraising round planned? If so, investor identity, amounts, and timeline?

## À compléter -- CEO

## Proposition de réponse (DRAFT -- à valider par CEO)

- Levée de fonds **en cours de structuration** pour H2 2026 -- H1 2027
- Montant, identité des investisseurs et calendrier : **à compléter par la direction**
- Objectif : financer l'accélération commerciale et l'exécution des WP6--7

**WP : Gouvernance / Financement**

---

# Q22 -- Sources publiques de financement

> *Êtes-vous déjà bénéficiaire, ou en cours de demande, directement ou indirectement au titre de ce projet (de façon consolidée au niveau de l'ensemble des sociétés du groupe) d'autres financements (financements nationaux, régionaux, aides européennes, etc.) ?*
>
> Are you already receiving or applying for other public funding for this project?

## À compléter -- Direction / DAF

## Proposition de réponse (DRAFT -- à valider par Direction / DAF)

- Détailler les financements existants (CIR, JEI, subventions régionales, etc.)
- Lister les demandes en cours
- Confirmer la conformité avec les règles de cumul d'aides Bpifrance

**WP : Gouvernance / Financement**

---

# Q23 -- Accords de sous-traitance

> *Des sous-traitances dans le cadre du projet sont envisagées, pouvez-vous nous fournir les accords/modèles d'accord encadrant ces relations de sous-traitance ? Si un sous-traitant est défaillant, avez-vous identifié des alternatives ?*
>
> Can you provide subcontracting agreements? Have you identified alternatives if a subcontractor fails?

## Stratégie de mitigation

- **Gradient Health :** écosystème large de partenaires données -- multiplication des sources pour compenser les défections
- **Cedars-Sinai / Mayo Clinic :** fournisseurs de données et sites de validation
- **ICM :** cohortes génomiques et cliniques
- **Aucun partenaire unique n'est indispensable** -- couverture redondante par design

## Accords contractuels

- Modèles d'accord à fournir au comité (SOPs et templates contractuels existants)
- Accompagnement juridique : **Cabinet Carrel** (fondé par l'ex-directrice d'Inserm Transfert)

**WP : Gouvernance**

---

# Q24 -- Veille réglementaire

> *Comment est faite la veille réglementaire au sein de votre structure ?*
>
> How is regulatory monitoring conducted within your organization?

## Organisation interne

- **1 Q&A GxP** (Charbel / Clarisse) -- conformité pharmaceutique et réglementaire
- **1 Q&A IT** (Théo) -- conformité technique et cybersécurité
- **1 Comité scientifique** -- veille scientifique et méthodologique

## Périmètre de veille

- **Réglementation pharmaceutique :** ICH, EMA, FDA, PMDA
- **Réglementation IA :** EU AI Act, guidelines nationales
- **Protection des données :** RGPD, HIPAA
- **Dispositifs médicaux :** MDR/IVDR (veille -- non applicable dans le périmètre actuel)

**WP : Gouvernance / Réglementaire**

---

# Q25 -- Verrous juridiques

> *Comment et par qui êtes-vous accompagnés sur le plan juridique et réglementaire (équipe interne, cabinet de conseil, cabinet d'avocats) ? Est-ce que vous avez relevé des verrous juridiques pour mener à bien ce projet ? Si oui, lesquels sont-ils et quelle est la stratégie pour le(s) lever ?*
>
> Who provides legal and regulatory support? Have you identified any legal barriers?

## Accompagnement juridique

- **Cabinet Carrel** -- fondé par l'ex-directrice d'Inserm Transfert
- Expertise en propriété intellectuelle, contrats de recherche collaborative, droit de la santé

## Verrous juridiques

- **Aucun verrou juridique identifié à ce stade**
- Les verrous ont été **levés et intégrés au développement** d'ArcaScience au fil des années
- **Veille continue** pour anticiper les évolutions réglementaires (EU AI Act, EHDS, etc.)

**WP : Gouvernance / Juridique**

---

# Q26 -- Retour clients mode SaaS

> *Pourriez-vous nous donner le retour de vos premiers clients sur le mode SaaS ?*
>
> Could you give us feedback from your first SaaS clients?

## À compléter -- CEO / Direction commerciale

## Proposition de réponse (DRAFT -- à valider par CEO / Direction commerciale)

- Plateforme BRA en phase de déploiement auprès des premiers utilisateurs
- Objectif Q en cours : **10--50 utilisateurs** de **1--5 entreprises** (KR 1.1)
- Pricing SaaS structuré :
  - **BRA Essentials** : 75--100K EUR/an (mid-market biotech)
  - **BRA Professional** : 125--175K EUR/an (mid-to-large pharma)
  - **BRA Enterprise** : 200--300K EUR/an (Top-20 pharma)
- Retours qualitatifs à collecter et présenter (feedback pipeline, NPS, cas d'usage validés)

**WP : WP7 / Commercial**

---

# Q27 -- Contrat ICON

> *Où en est le contrat avec ICON ?*
>
> What is the status of the contract with ICON?

## À compléter -- CEO

## Proposition de réponse (DRAFT -- à valider par CEO)

- Statut actuel du contrat ICON : **à détailler**
- Périmètre de la collaboration, montant, jalons
- Lien avec la stratégie go-to-market et le pipeline commercial

**WP : WP7 / Commercial**

---

# Q28 -- Contrat Vidal et module Synapse

> *Pourriez-vous donner plus d'informations sur votre contrat avec Vidal et comment ce nouveau module peut ou pourrait s'articuler avec les modules d'analyse de risques d'interactions médicamenteuses comme celui de Synapse ?*
>
> More details on the Vidal contract and how this module articulates with drug interaction risk modules like Synapse?

## Positionnement différenciant

- **Technologie Synapse/Vidal :** compréhension des leaflets et du travail du G-TIAM
- **ArcaScience :** en **amont** -- identification des cas d'interactions médicamenteuses issus de la vie réelle et de la littérature
- **Complémentarité :** ArcaScience enrichit les signaux en amont, Vidal les diffuse en aval

## À compléter -- CEO / Direction commerciale

## Proposition de réponse (DRAFT -- à valider par CEO / Direction commerciale)

- Détailler le périmètre du contrat Vidal (nature, montant, durée)
- Expliquer le module spécifique développé ou en cours de développement
- Articuler avec la stratégie d'interactions médicamenteuses de BR-PREDICT (T6.3 -- modélisation causale et prédiction d'interactions DDI)

**WP : WP7 / Commercial**

---

# Q29 -- Identification et contact clients

> *Comment êtes-vous structurés pour l'identification et la prise de contact auprès des clients potentiels ?*
>
> How are you structured for identifying and contacting potential clients?

## À compléter -- CEO / Direction commerciale

## Proposition de réponse (DRAFT -- à valider par CEO)

- **Organisation sales structurée** avec pipeline discipliné
- Target : **10 outbounds + 5 warm intros** par quinzaine
- Pipeline coverage target : **3x du target revenue** ($1.5M)
- Motion **disease-specific-first** : les versions thérapeutiques compressent les cycles de vente de **40--60%**
- Win rate cible : **25--35%** sur opportunités qualifiées
- Cycle de vente moyen : **<60 jours**
- Profils cibles : Top-20 pharma, mid-market biotech, CROs

**WP : WP7 / Commercial**

---

# Q30 -- Choix du NSCLC et indications futures

> *Pourquoi avoir choisi le NSCLC comme première indication ? Quelles seraient les indications suivantes et quel sera le rationnel pour les choisir ? Comment allez-vous sourcer les données pour répondre au 10% de spécifique par indication ?*
>
> Why NSCLC first? What are the next indications? How will you source the 10% indication-specific data?

## Choix du NSCLC

- Stratégie orientée **cancer** : NSCLC comme socle initial
- **Pertinence scientifique et richesse de données maximales** dans cette indication
- Création d'une base de données critique qui augmente la pertinence scientifique transversale

## Indications suivantes

- Extension vers l'**immuno-inflammation** en fonction de la disponibilité des données
- **Transfer learning entre aires thérapeutiques** : la similarité des pathologies facilite le transfert de modèles
- Architecture **90/10** : ~10% de calibration spécifique par nouvelle indication (choix des cibles, seuils de pertinence clinique, jeu de validation)

## Sourcing des 10% spécifiques par indication

| Source | Exemples |
|--------|----------|
| **1) Moissonnage** | Données open structurées (ChEMBL, ClinicalTrials.gov, FAERS) et non-structurées (PubMed, MEDLINE) |
| **2) Partenariats privés** | Gradient Health, Cedars-Sinai, Mayo Clinic |
| **3) Partenariats publics** | ICM, Institut Bergonié |

**WP : Stratégie / Cross-WP**

---

# Prochaines étapes

1. **Finaliser les réponses DRAFT flaguées** -- chaque owner valide son périmètre
2. **Valider les aspects juridiques et PI** avec Cabinet Carrel + revue RH
3. **Renvoyer la version consolidée** au comité d'évaluation Bpifrance

---

# Annexe -- Items DRAFT & À compléter

| Question | Item | Owner |
|----------|------|-------|
| Q2 | ETP par WP -- table à compléter | RH / Direction |
| Q5 | Liste BDD publiques/privées + explicabilité par couche | VS / Théo |
| Q6 | Framework RAISE Trustworthy AI | VS / Théo |
| Q13 | Stratégie RH profils rares | RH / Direction |
| Q15 | Sous-traitance INRIA -- nature, profils, PI | Direction / Cabinet Carrel |
| Q17 | T7.3 discussions pharma après M24 | Direction / Stratégie |
| Q20 | Structure capitalistique | Direction / CEO |
| Q21 | Levée de fonds -- montant, investisseurs, calendrier | CEO |
| Q22 | Sources publiques de financement | Direction / DAF |
| Q26 | Retour clients SaaS | CEO / Direction commerciale |
| Q27 | Contrat ICON | CEO |
| Q28 | Contrat Vidal / Synapse | CEO / Direction commerciale |
| Q29 | Organisation sales | CEO |
