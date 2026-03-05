## WP5 -- Graphe de Connaissances & Couche Ontologique Unifiée

**Responsable** : ArcaScience | **Partenaires** : -- (WP interne, consommant les sorties WP1-4, alimentant WP6)
**Période** : T0+12 (Q3 2027) -- T0+24 (Q2 2028) | **Jalons** : EC2 (mi-2027, schéma ontologique), EC3 (fin 2028, KG complet + API)

---

### Intitulé & Objectif

WP5 -- *Conception et déploiement d'un graphe de connaissances interopérable intégrant les données moléculaires, précliniques, génomiques et de vie réelle dans une couche sémantique unifiée au service du world model BR-PREDICT.*

Les WP1 à WP4 produisent des prédictions à partir de types de données hétérogènes (structures moléculaires, profils précliniques, variants génomiques, signaux RWE) encodés dans des terminologies et des espaces de représentation distincts. Sans unification sémantique, ces prédictions ne peuvent être ni comparées, ni combinées, ni auditées de façon cohérente. WP5 résout ce verrou en construisant un Knowledge Graph (KG) dont les noeuds représentent les entités biologiques, chimiques, cliniques et les arêtes les relations quantifiées et sourcées entre elles. Ce KG sert de couche d'interopérabilité fondatrice pour le world model de WP6 et constitue la base de l'explicabilité de la plateforme BR-PREDICT.

### Hypothèses scientifiques & périmètre

H1 : Un schéma ontologique s'appuyant sur les standards internationaux (MedDRA, SNOMED CT, ChEBI, Disease Ontology, Gene Ontology) peut couvrir >= 90 % des entités générées par WP1-4 sans extension ad hoc majeure. H2 : Les relations extraites par les Contextualizing SLMs à partir de la Profiling Base (100 milliards de points de données/relations) peuvent être projetées dans ce schéma avec un score de confiance traçable. H3 : Un KG peuplé et indexé permet des requêtes multi-sources complexes avec un temps de réponse < 2 secondes, compatible avec l'usage interactif en WP6.

Le périmètre couvre l'ensemble des entités et relations pertinentes pour le cancer du poumon (pathologie d'ancrage), extensible à d'autres aires thérapeutiques par ajout de sous-graphes calibrés.

### Méthodologie technique détaillée

**Conception ontologique (T5.1).** Le schéma est construit par composition modulaire : un noyau partagé (upper ontology) définit les classes de premier niveau (Molecule, Target, Pathway, Phenotype, AdverseEvent, Patient, ClinicalOutcome) et les types de relations (binds_to, inhibits, causes, associated_with, treats, metabolized_by). Ce noyau est aligné sur les ontologies de référence : MedDRA 27.x pour les événements indésirables, SNOMED CT pour les concepts cliniques, ChEBI pour les entités chimiques, Gene Ontology et Reactome pour les voies biologiques, Disease Ontology pour les pathologies. Les extensions pathologie-spécifiques (ex. staging TNM, mutations driver EGFR/ALK/ROS1 pour le cancer du poumon) sont modélisées en sous-ontologies enfichables, validées par les experts du comité scientifique (Pr. Alexis Brice, Dr. Philippe Peyre).

**Harmonisation et mapping d'entités (T5.2).** Chaque sortie de WP1-4 est projetée sur le schéma ontologique via un pipeline de résolution d'entités (entity linking) combinant : (i) correspondance exacte sur identifiants normalisés (CAS, DrugBank ID, UniProt ID, MedDRA PT code) ; (ii) correspondance approximative par similarité sémantique (embeddings des Contextualizing SLMs, cosine similarity > 0,92) ; (iii) arbitrage humain pour les entités ambiguës (< 5 % attendu). Les tables de correspondance sont versionnées et auditables.

**Construction du KG (T5.3).** Le graphe est implémenté sur une base de données graphe (Neo4j ou équivalent) avec un stockage RDF parallèle pour l'interopérabilité SPARQL. Les noeuds portent des attributs typés (identifiants, scores de confiance, provenance WP, timestamps). Les arêtes sont pondérées par un score de confiance composite intégrant : la fréquence d'observation dans la Profiling Base, le niveau de preuve (essai clinique > cohorte RWE > cas rapporté > prédiction in silico), et la concordance inter-WP. L'objectif cible est un KG de > 100 000 entités et > 1 million de relations au stade EC3.

**Extraction NLP et validation des relations (T5.4).** Les 24 Contextualizing SLMs d'ArcaScience extraient en continu des relations à partir de la littérature, des rapports réglementaires et des données brutes alimentant la Profiling Base. Chaque relation extraite est scorée (précision estimée, rappel par échantillonnage) et soumise à un processus de validation croisée : concordance entre SLMs indépendants, cohérence avec les relations existantes du KG (détection de contradictions), validation par échantillonnage expert (gold standard sur 5 % des nouvelles relations par trimestre).

**Interface de requête et API (T5.5).** Une API RESTful et GraphQL expose le KG avec un langage de requête multi-niveaux : requêtes simples (entité -> voisins directs), requêtes de chemin (plus court chemin entre deux entités, chemins causaux), requêtes agrégées (profil B-R complet d'une molécule = sous-graphe de toutes les relations bénéfice et risque avec scores). Un système de cache hiérarchique (in-memory pour les requêtes fréquentes, disque pour les requêtes complexes) garantit le respect du KPI de latence < 2 s. L'API est conçue pour être consommée par le world model de WP6 et par l'interface de visualisation (Mental Map, T6.5).

### Tâches & articulation avec les autres WPs

| Tâche | Entrée principale | Sortie | Lien WP |
|-------|-------------------|--------|---------|
| T5.1 Ontology design | Standards (MedDRA, SNOMED CT, ChEBI, GO, DO) | Schéma ontologique validé | WP1-4 (couverture des entités) |
| T5.2 Harmonisation & mapping | Sorties WP1-4, Profiling Base | Tables de correspondance versionnées | WP1, WP2, WP3, WP4 |
| T5.3 Construction KG | Entités mappées, relations scorées | KG peuplé (Neo4j + RDF) | WP1-4 (données), WP6 (consommation) |
| T5.4 Extraction NLP & validation | Profiling Base, littérature, rapports | Relations validées avec scores de confiance | Contextualizing SLMs (transversal) |
| T5.5 API & interface de requête | KG peuplé | API RESTful/GraphQL, documentation | WP6 (intégration), T6.5 (Mental Map) |

WP5 est structurellement le pivot entre les WP de production de connaissances (WP1-4) et le WP d'intégration/simulation (WP6). Toute relation alimentant le world model de WP6 transite par le KG et porte une provenance traçable.

### Livrables & Jalons

- **L5.1** (EC2, mi-2027) : Schéma ontologique finalisé, validé par le comité scientifique ; tables de correspondance WP1-3 livrées ; couverture >= 80 % des entités WP1-3.
- **L5.2** (EC2+6 mois) : KG peuplé avec intégration complète des données RWE (WP4) ; > 100 000 entités, > 1 million de relations.
- **L5.3** (EC3, fin 2028) : API opérationnelle testée selon les exigences WP6, documentation technique et guide d'utilisation, rapport qualité données (couverture, scores de confiance, taux de contradictions résolues).

### KPI & protocole d'évaluation

- **KPI-1** : >= 90 % des entités produites par WP1-4 intégrées dans le KG avec relations sémantiques validées.
- **KPI-2** : Temps de réponse < 2 secondes pour les requêtes multi-sources complexes (95e percentile mesuré sur un benchmark de 500 requêtes types définies avec les partenaires WP6).
- **KPI-3** : Taux de contradictions non résolues < 5 % des relations du KG.
- Protocole : audit trimestriel par échantillonnage (200 relations tirées aléatoirement, vérification manuelle par expert domaine, calcul de précision/rappel).

### Risques, verrous, et plans de mitigation

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Couverture ontologique insuffisante pour cibles émergentes ou maladies rares | Moyen | Moyenne | Architecture modulaire (sous-ontologies enfichables) ; processus d'extension trimestriel piloté par les lacunes identifiées en WP6 |
| Exhaustivité du KG dépendante de la qualité des données WP1-4 | Élevé | Moyenne | Scores de confiance par relation ; propagation explicite de l'incertitude vers WP6 ; seuils de qualité minimaux pour l'intégration |
| Maintien de la cohérence lors de l'ajout continu de nouvelles données | Moyen | Élevée | Pipeline de détection de contradictions (T5.4) ; versionnage du KG avec snapshots immuables par jalon ; processus de curation continue (1 ETP dédié) |
| Performance de requête dégradée avec la croissance du KG | Faible | Moyenne | Indexation incrémentale, partitionnement par domaine thérapeutique, cache hiérarchique ; tests de charge trimestriels |

### Contribution à la répétabilité multi-pathologies & à l'industrialisation

Le KG est structurellement conçu pour la généralisation. Le noyau ontologique est pathologie-agnostique : les classes Molecule, Target, Pathway, AdverseEvent ne sont pas spécifiques au cancer du poumon. L'ajout d'une nouvelle pathologie se traduit par l'instanciation de sous-ontologies spécifiques (staging, biomarqueurs, endpoints) et le peuplement du sous-graphe correspondant à partir des données WP1-4 calibrées. L'API unifiée permet à WP6 d'interroger le KG de manière identique quelle que soit la pathologie, garantissant que le world model consomme une couche d'abstraction stable. Enfin, le caractère traçable de chaque relation (provenance, score de confiance, niveau de preuve) répond aux exigences d'auditabilité réglementaire (ICH E2C(R2), CIOMS XII) et prépare la plateforme à un usage en contexte de soumission réglementaire.
