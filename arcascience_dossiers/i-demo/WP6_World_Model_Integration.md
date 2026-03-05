## WP6 -- World Model : Intégration Prédictive, Raisonnement Causal et Simulation Bénéfice-Risque

**Responsable** : ArcaScience | **Partenaires validation** : Sanofi, Cedars Sinai, Mayo Clinic, Institut du Cerveau (ICM), AMI Labs (en cours de cadrage) | **Partenaire données** : Gradient Health
**Période** : T0+9 (Q1 2027) -- T0+30 (Q4 2028) | **Jalons** : EC2 (mi-2027, architecture intégrée), EC3 (fin 2028, world model opérationnel validé)

---

### Intitulé & Objectif

WP6 -- *Conception, intégration et validation d'un world model capable de simuler des profils bénéfice-risque complets pour toute molécule en développement, de la phase préclinique à la phase II, par fusion multimodale des modèles prédictifs WP1-4 et du graphe de connaissances WP5.*

Le world model BR-PREDICT constitue la finalité scientifique et industrielle du projet. Il ne s'agit pas d'une agrégation naïve de prédictions, mais d'un système intégré qui apprend à pondérer, réconcilier et enrichir les prédictions issues de sources de données hétérogènes (structure moléculaire, profils précliniques, variants génomiques, données de vie réelle) en exploitant les relations causales encodées dans le Knowledge Graph (WP5). L'objectif est de fournir, pour une molécule entrant en phase I ou II, un profil B-R simulé comprenant : prédiction d'efficacité, profil de sécurité avec hiérarchisation des risques, comparaison aux thérapies existantes, estimation de l'incertitude, et visualisation interactive sous forme de Mental Map.

### Hypothèses scientifiques & périmètre

H1 : L'intégration pondérée de modèles prédictifs entraînés sur des données de nature différente (WP1-4) produit des estimations B-R plus robustes que tout modèle individuel, à condition de modéliser explicitement les contradictions inter-sources et de propager l'incertitude. H2 : Les relations causales entre propriétés moléculaires, mécanismes biologiques et caractéristiques patient, lorsqu'elles sont structurées dans un graphe (WP5) et exploitées par un module de raisonnement causal, permettent de simuler des scénarios contrefactuels (ex. "quel serait le profil de sécurité de cette molécule chez un patient porteur d'un variant CYP2D6 poor metabolizer ?"). H3 : La Profiling Base existante (100 milliards de points de données/relations) et la pile d'extraction des 24 Contextualizing SLMs constituent un actif suffisant pour pré-entraîner les représentations latentes du world model et réduire significativement le besoin de données annotées spécifiques au projet.

Périmètre : cancer du poumon (validation spécifique complète), puis extension à 2+ aires thérapeutiques pour la validation générique.

### Méthodologie technique détaillée

**Architecture du world model (T6.1).** Le world model repose sur une représentation en espace latent multimodal. Chaque molécule est encodée comme un vecteur latent z_mol issu d'un encodeur pré-entraîné sur la Profiling Base (fingerprints moléculaires, descripteurs ADMET, profils d'activité cible). Chaque patient est représenté par un vecteur z_pat intégrant données démographiques, comorbidités, co-médications et variants pharmacogénomiques. Le contexte pathologique est encodé via un vecteur z_path extrait du sous-graphe WP5 correspondant (topologie locale du KG autour de la pathologie d'intérêt).

La fusion de ces représentations s'opère par un module d'attention multimodale (cross-modal attention) : chaque source de prédiction (WP1-4) est traitée comme un token d'évidence portant un embedding, un score de confiance et une provenance. Le mécanisme d'attention apprend à pondérer ces tokens en fonction du contexte (pathologie, type de molécule, données disponibles). Un module de dynamique temporelle (architecture récurrente ou Transformer causal) modélise l'évolution du profil B-R dans le temps (exposition cumulée, émergence progressive d'effets indésirables, tachyphylaxie).

Le pré-entraînement des encodeurs moléculaires et des modules d'attention exploite directement les 100 milliards de relations de la Profiling Base. Les Contextualizing SLMs, entraînés par des cliniciens sur des corpus réglementaires et de pharmacovigilance, fournissent les embeddings textuels des événements indésirables, des mécanismes d'action et des endpoints cliniques, garantissant que l'espace latent du world model est ancré dans un vocabulaire clinique validé. Cette fondation en données propriétaires massives est ce qui rend crédible un world model opérationnel dans le calendrier du projet : le pré-entraînement est largement réalisé, le projet i-Demo finance la couche d'intégration et de raisonnement causal.

**Intégration d'ensemble WP1-4 (T6.2).** Les prédictions de WP1 (structure-activité), WP2 (préclinique), WP3 (génomique) et WP4 (RWE) ne sont pas moyennées. Le module d'intégration implémente une méta-apprenante (stacking) où les prédictions individuelles et leurs intervalles de confiance sont les features d'un modèle de second niveau. Ce modèle apprend les patterns de concordance et de contradiction entre WPs. Lorsque deux WPs divergent significativement (ex. WP1 prédit faible risque hépatotoxique, WP4 détecte un signal FAERS), un module de résolution de conflit est activé : il interroge le KG (WP5) pour identifier si une variable confondante (ex. co-médication hépatotoxique fréquente en RWE) explique la divergence, et propage l'incertitude résiduelle vers la sortie finale. Cette approche est fondamentalement supérieure à un vote majoritaire ou à une moyenne pondérée fixe.

**Modélisation causale et prédiction d'interactions (T6.3).** Le world model intègre un graphe causal structurel (Structural Causal Model, SCM) dont la topologie est initialisée à partir du KG (WP5) et dont les paramètres sont estimés par les données WP1-4. Ce SCM permet : (i) la simulation d'interactions médicamenteuses (drug-drug interactions, DDI) en combinant données moléculaires (inhibition enzymatique CYP, compétition au site de liaison) et signaux RWE (co-prescription observée + événements associés) ; (ii) la prédiction d'interactions gène-médicament (pharmacogénomique) en intégrant les variants identifiés en WP3 avec les voies métaboliques du KG ; (iii) la simulation dose-réponse et temps-vers-événement (time-to-event) via des modèles de survie paramétriques conditionnés par les variables latentes du world model. Le raisonnement contrefactuel est opéré par intervention sur les noeuds du SCM (ex. do(CYP2D6 = poor metabolizer)) et propagation des effets dans le graphe, permettant de répondre à des questions du type "quel profil de sécurité pour cette molécule si le patient était un métaboliseur lent ?".

**Quantification de l'incertitude (T6.4).** L'incertitude est modélisée à deux niveaux. Au niveau épistémique (incertitude liée aux données insuffisantes) : ensembles de modèles (deep ensembles, 10 répliques avec initialisation différente) et approximation variationnelle bayésienne sur les couches critiques. Au niveau aléatoire (variabilité intrinsèque) : modélisation hétéroscédastique des résidus. La sortie du world model est donc un profil B-R probabiliste : pour chaque événement prédit, un intervalle de confiance et une décomposition des sources d'incertitude (données moléculaires limitées vs. signal RWE contradictoire vs. faible couverture KG). Cette décomposition est essentielle pour l'interprétabilité et pour guider le pharmacien/clinicien vers les zones nécessitant une investigation complémentaire.

**Interface de visualisation -- Mental Map (T6.5).** La Mental Map est une interface interactive qui projette le profil B-R d'une molécule sous forme de réseau navigable : la molécule au centre, connectée à ses cibles thérapeutiques, elles-mêmes liées aux voies métaboliques perturbées, débouchant sur les résultats cliniques (efficacité et effets indésirables). Chaque noeud et chaque arête portent leur score de confiance, leur provenance (WP d'origine, source de données), et leur niveau de preuve. L'utilisateur peut filtrer par type de données, par seuil de confiance, par sous-population patient, ou simuler un scénario contrefactuel (ajout d'une co-médication, changement de variant génomique). La Mental Map est conçue pour être utilisable par un évaluateur réglementaire, un pharmacovigilant ou un clinicien investigateur sans formation spécifique en data science.

**Validation et calibration (T6.6).** La validation est conduite en deux phases. Phase rétrospective : le world model est évalué sur un jeu de >= 200 molécules commercialisées ou retirées du marché, dont les profils B-R réels sont connus. Les métriques sont : AUC-ROC pour la prédiction d'EIG sévères (objectif cible > 0,8 en validation externe), taux de faux négatifs < 10 % pour les DDI connues, et évaluation qualitative par un panel d'experts (objectif cible : > 70 % des prédictions jugées "cliniquement plausibles"). Phase prospective : monitoring en conditions réelles sur des molécules en développement chez les partenaires (Sanofi, institutions partenaires), avec comparaison longitudinale entre prédictions et observations de pharmacovigilance. AMI Labs (cadrage en cours) interviendra sur la validation des méthodologies d'évaluation.

### Tâches & articulation avec les autres WPs

| Tâche | Entrée | Sortie | Lien WP |
|-------|--------|--------|---------|
| T6.1 Architecture world model | Profiling Base, embeddings SLM | Encodeurs pré-entraînés, architecture fusion | Transversal (SLMs, Profiling Base) |
| T6.2 Intégration d'ensemble WP1-4 | Prédictions + IC WP1-4 | Prédictions intégrées, carte de concordance | WP1, WP2, WP3, WP4 |
| T6.3 Modélisation causale & interactions | KG (WP5), données WP1-4 | SCM paramétré, prédictions DDI/gène-drug | WP5 (topologie causale) |
| T6.4 Quantification incertitude | Ensemble de modèles T6.1-6.3 | Profils B-R probabilistes, décomposition incertitude | -- |
| T6.5 Mental Map | Profils B-R (T6.2-6.4), KG (WP5) | Interface interactive, visualisation réseau | WP5 (API) |
| T6.6 Validation & calibration | Jeu rétrospectif + prospectif | Rapport de validation, métriques | Sanofi, Cedars Sinai, Mayo, ICM, AMI Labs |

### Livrables & Jalons

- **L6.1** (EC2, mi-2027) : Architecture du world model validée, encodeurs pré-entraînés opérationnels, prototype d'intégration d'ensemble sur cancer du poumon.
- **L6.2** (EC3-6 mois) : Module d'interactions (DDI, gène-drug), module d'incertitude, prototype Mental Map fonctionnel.
- **L6.3** (EC3, fin 2028) : World model opérationnel intégrant WP1-5, rapport de validation rétrospective (>= 200 molécules), rapport de validation prospective (monitoring partenaires), tests d'acceptation utilisateur avec >= 5 partenaires pharmaceutiques.
- **L6.4** (EC3) : Documentation utilisateur, matériaux de formation, système déployable avec quantification d'incertitude.

**Jalon pathologie spécifique (cancer du poumon)** : démonstration du workflow complet -- entrée : molécule en Phase I/II ; sortie : profil B-R complet incluant efficacité prédite (ensemble WP1-4), profil de sécurité hiérarchisé, comparaison aux thérapies existantes (immunothérapies, TKI), estimation d'incertitude, visualisation Mental Map. Validation par panel d'experts cliniques.

**Jalon générique** : world model opérationnel sur 2+ domaines thérapeutiques ; AUC > 0,8 pour la prédiction d'EIG sévères en validation externe ; taux de faux négatifs < 10 % pour les DDI connues ; tests d'acceptation avec >= 5 partenaires industriels.

### KPI & protocole d'évaluation

- **KPI-1** : Sensibilité/spécificité élevées pour la prédiction d'EIG sévères sur molécules de test (objectif cible : AUC > 0,8 en validation externe d'ensemble).
- **KPI-2** : Capacité à générer des profils B-R cohérents intégrant >= 3 sources de données indépendantes (moléculaire, préclinique/génomique, RWE).
- **KPI-3** : > 70 % des évaluateurs experts jugent les prédictions "cliniquement plausibles" (évaluation en aveugle, grille standardisée).
- **KPI-4** : Taux de faux négatifs < 10 % pour les DDI connues (base de référence : DrugBank + FAERS validated signals).
- Protocole : validation rétrospective sur cohorte hold-out temporellement disjointe ; validation prospective par monitoring continu chez les partenaires ; évaluation qualitative par panel d'experts indépendants (>= 10 évaluateurs, >= 3 institutions).

### Risques, verrous, et plans de mitigation

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Données insuffisantes pour les scaffolds moléculaires nouveaux ou les maladies rares (zone d'extrapolation) | Élevé | Moyenne | Détection automatique des zones hors-distribution (OOD detection) avec avertissement explicite dans le profil B-R ; limitation volontaire de la prédiction au périmètre de confiance ; enrichissement continu de la Profiling Base |
| Interactions émergentes absentes des données d'entraînement | Élevé | Faible-Moyenne | Le SCM causal permet une forme de généralisation par composition (combinaison de mécanismes connus), mais les interactions véritablement inédites restent une limitation déclarée ; monitoring prospectif (T6.6) comme filet de sécurité |
| Complexité d'intégration multi-WP (dépendances calendaires, formats) | Moyen | Élevée | Spécification précoce des interfaces (formats de sortie WP1-4, API WP5) dès EC1 ; intégration incrémentale (WP1-3 d'abord, WP4 ensuite, WP5 en parallèle) ; sprints d'intégration trimestriels |
| Acceptation utilisateur insuffisante (interface trop complexe, confiance limitée) | Moyen | Moyenne | Co-conception de la Mental Map avec les partenaires cliniques dès T6.5 ; tests utilisateurs itératifs (3 cycles) ; formation dédiée ; scoring d'incertitude comme levier de confiance (l'utilisateur voit où le modèle doute) |
| Risque réglementaire : qualification du world model comme dispositif médical ou outil d'aide à la décision soumis à MDR/IVDR | Moyen | Faible | Positionnement initial comme outil de recherche et d'aide à la décision non-clinique (usage pharma R&D, non diagnostic) ; veille réglementaire continue ; architecture compatible avec les exigences futures de traçabilité/reproductibilité |

### Contribution à la répétabilité multi-pathologies & à l'industrialisation

Le world model est conçu selon le principe 90/10 : 90 % de l'architecture est pathologie-agnostique (encodeurs moléculaires, module d'attention multimodale, SCM, module d'incertitude, Mental Map, pipeline de validation), et ~10 % nécessitent une calibration spécifique (sous-graphe KG pathologie, pondération des endpoints cliniques, seuils de décision). L'ajout d'une nouvelle pathologie se traduit par : (i) peuplement du sous-graphe WP5 correspondant ; (ii) fine-tuning de la couche de calibration sur un jeu de données annoté limité (objectif : < 500 cas annotés suffisants grâce au transfert) ; (iii) validation rétrospective sur les molécules connues de cette pathologie. Ce processus est documenté et reproductible. La Profiling Base (100 milliards de relations) et les 24 Contextualizing SLMs fournissent la couche de pré-entraînement qui rend ce transfert réaliste : les représentations moléculaires et cliniques apprises sont fondamentalement transversales. L'industrialisation passe par la conteneurisation du pipeline complet, l'exposition via API sécurisée (authentification, rate limiting, audit trail), et la production de matériaux de formation permettant un déploiement autonome chez les partenaires pharmaceutiques. Le plan de recrutement du projet (47 postes, dont 27 R&D) soutient cette montée en capacité sur la durée du financement i-Demo.
