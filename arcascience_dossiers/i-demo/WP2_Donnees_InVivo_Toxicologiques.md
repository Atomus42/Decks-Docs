## WP2 -- Prédiction du rapport bénéfice-risque à partir des données in vivo et toxicologiques

**Responsable** : ArcaScience | **Partenaires** : Sanofi, Cedars Sinai, Mayo Clinic
**Période** : Q1 2026 -- Q3 2027 | **Jalon principal** : EC1 (fin 2026)

---

### Intitulé & Objectif

**WP2 : Modèles prédictifs de transposition préclinique-clinique pour l'estimation du rapport bénéfice-risque à partir des données in vivo.**

L'objectif de ce lot est de construire une couche prédictive qui exploite les données d'études précliniques -- efficacité pharmacologique in vivo, toxicologie réglementaire, pharmacocinétique animale -- pour prédire le profil B-R chez l'humain. Le WP2 introduit une innovation majeure : un **score de fiabilité par modèle préclinique et par pathologie**, quantifiant la transposabilité historique de chaque modèle animal vers l'issue clinique humaine. Ce lot se situe en aval du WP1 (structure chimique) et constitue le deuxième niveau de résolution prédictive de BR-PREDICT, mobilisable dès la fin des études précliniques réglementaires et pendant les phases I/II.

### Hypothèses scientifiques & périmètre

L'hypothèse centrale est que les données précliniques in vivo, bien que soumises à des biais de transposition inter-espèces bien documentés, contiennent un signal prédictif exploitable lorsqu'elles sont pondérées par la fiabilité historique du modèle animal utilisé. L'état de l'art confirme cette hypothèse : les approches hybrides ML + modélisation mécanistique PK ont atteint 64 % de précision pour la clairance et 62 % pour le volume de distribution, dans une marge d'erreur de facteur 2 (Lombardo et al.). Le périmètre couvre les petites molécules et les biologiques, ces derniers faisant l'objet d'un traitement spécifique compte tenu des limites connues de transposabilité (immunogénicité, modèles substitutifs). La pathologie d'ancrage reste l'oncologie pulmonaire.

### Méthodologie technique détaillée

**T2.1 -- Préparation de l'infrastructure (tâche mutualisée WP2/WP3/WP4).** Déployée en Q1 2026, cette tâche met en place l'infrastructure commune de stockage, d'indexation et de requêtage de la Profiling Base dédiée à BR-PREDICT. Elle comprend l'extension du graphe de connaissances existant (100 milliards de points de données/relations), le déploiement des pipelines ETL pour les nouvelles sources, et la configuration des environnements d'entraînement ML (GPU, versioning des modèles, traçabilité des expériences via MLflow).

**T2.2 -- Qualification des sources de données in vivo.** Trois catégories de sources sont qualifiées : (i) données d'efficacité préclinique (modèles xénogreffe, PDX, modèles transgéniques, données pharmacodynamiques), (ii) données toxicologiques réglementaires (études de dose-réponse, études de toxicité à doses répétées, études de génotoxicité, études de carcinogénicité), (iii) littérature générale rapportant des résultats in vivo avec issue clinique connue. Chaque source est évaluée selon sa couverture, sa standardisation, et ses biais potentiels (biais de publication, sous-déclaration des résultats négatifs).

**T2.3 -- Extraction NLP et structuration.** Les Contextualizing SLMs d'ArcaScience (24 modèles entraînés par des cliniciens) sont adaptés pour extraire, à partir de la littérature et des rapports d'études, les données structurées nécessaires : espèce, souche, modèle pathologique, doses, schéma posologique, endpoints d'efficacité (TGI, survie, réponse tumorale), endpoints de toxicité (NOAEL, LOAEL, organes cibles, sévérité), et paramètres PK (Cmax, AUC, t½, clairance). L'extraction est validée par confrontation avec des données manuellement annotées (précision objectif cible > 90 %).

**T2.4 -- Création de la base curée.** Les données extraites sont intégrées dans une base relationnelle liant chaque molécule à ses résultats précliniques (efficacité + toxicité), au modèle animal utilisé, et à l'issue clinique connue (pour les molécules commercialisées ou ayant échoué en développement clinique). Cette base constitue le corpus d'entraînement et de validation des modèles ML.

**T2.5 -- Modèle ML de prédiction d'efficacité avec score de fiabilité.** Un modèle ML est entraîné pour prédire l'efficacité clinique à partir des données précliniques. L'innovation clé réside dans l'intégration d'un **score de fiabilité par modèle préclinique et par pathologie**, calculé à partir de la concordance historique entre résultats précliniques et issues cliniques pour chaque combinaison {modèle animal x pathologie}. Ce score pondère la prédiction et permet de quantifier la confiance accordée à chaque donnée d'entrée. En oncologie pulmonaire, par exemple, les modèles PDX EGFR-mutés auront un score de fiabilité distinct de celui des xénogreffes sous-cutanées sur lignées cellulaires.

**T2.6 -- Modèle ML de prédiction de risque.** Un modèle parallèle est entraîné pour prédire les risques toxiques humains à partir des données animales. Les entrées incluent les NOAEL/LOAEL, les organes cibles identifiés en toxicologie, les marges de sécurité (HED/MRHD), et les signaux de toxicité fonctionnelle. Le modèle apprend les facteurs de transposition inter-espèces et les patterns de toxicité clinique historiquement non détectés en préclinique.

**T2.7 -- Validation et intégration.** Les modèles sont validés sur des molécules commercialisées en oncologie pulmonaire et sur des molécules ayant échoué en développement (attrition pour efficacité insuffisante ou toxicité inacceptable). La précision est comparée à celle du WP1 pour quantifier le gain incrémental apporté par les données in vivo.

### Tâches & articulation avec les autres WPs

Le WP2 s'appuie sur l'infrastructure commune déployée en T2.1 (partagée avec WP3 et WP4). Il reçoit les prédictions structurelles du WP1 comme baseline et transmet ses scores prédictifs au WP5 (intégration). Le WP2 alimente également le WP3 en fournissant les corrélations efficacité-biomarqueurs observées dans les études précliniques. Les partenaires Sanofi et Cedars-Sinai contribuent à la validation clinique ; Mayo Clinic fournit des données longitudinales pour l'évaluation rétrospective. Le calendrier s'étend de Q1 2026 à Q3 2027, avec une phase d'infrastructure commune en Q1 2026.

### Livrables & Jalons

- **L2.1** : Infrastructure commune opérationnelle (M3, partagée avec WP3/WP4).
- **L2.2** : Modèle NLP fonctionnel pour l'extraction de données in vivo (M9).
- **L2.3** : Score de fiabilité par modèle préclinique et par pathologie, calibré sur l'oncologie pulmonaire (M12).
- **L2.4** : Modèles ML prédictifs B-R basés sur les données in vivo, validés (M18).
- **Jalon EC1** (fin 2026) : objectifs de précision définis par périmètre (spécifique/non spécifique).

### KPI & protocole d'évaluation

L'objectif cible est une précision de prédiction sur les molécules commercialisées **supérieure à celle du WP1** (AUC > 0,65), démontrant la valeur incrémentale des données in vivo. Le protocole d'évaluation repose sur une validation rétrospective : les modèles sont entraînés sur des molécules dont le profil B-R clinique est connu, puis testés sur un jeu de validation externe. La précision du score de fiabilité est évaluée par la corrélation entre le score attribué et la concordance préclinique-clinique observée. Les résultats sont stratifiés par type de modèle animal et par sous-type de pathologie pulmonaire.

### Risques, verrous, et plans de mitigation

- **Données propriétaires derrière des paywalls** : une part significative des données précliniques est publiée dans des revues à accès restreint ou détenue en interne par les laboratoires. Mitigation : exploitation prioritaire des bases ouvertes (PubChem BioAssay, EPA ToxCast, littérature en accès libre), complétée par les données partenaires (Sanofi, Cedars-Sinai, Mayo Clinic) dans le cadre d'accords de partage.
- **Biais de publication et de rapportage** : les résultats négatifs en préclinique sont sous-publiés, ce qui biaise les modèles vers une surestimation de l'efficacité. Mitigation : pondération des sources par leur exhaustivité estimée, intégration de registres d'études négatives, et calibration du score de fiabilité sur des cohortes incluant explicitement les échecs.
- **Limites spécifiques aux biologiques** : immunogénicité spécifique à l'espèce, faible transposabilité des modèles substitutifs. Mitigation : traitement séparé des biologiques avec des modèles dédiés intégrant les facteurs de correction inter-espèces connus ; signalisation explicite de l'incertitude accrue pour cette classe thérapeutique.

### Contribution à la répétabilité multi-pathologies & à l'industrialisation

Le score de fiabilité par modèle préclinique et par pathologie est, par conception, extensible à d'autres aires thérapeutiques : il suffit de calculer la concordance historique {modèle animal x pathologie} sur les données disponibles pour chaque nouvelle indication. L'architecture NLP d'extraction est entraînée sur des structures textuelles génériques (protocoles d'études, résultats d'efficacité et de toxicité) et ne nécessite qu'une calibration terminologique mineure (~10 %) pour s'adapter à une nouvelle pathologie. Ce design assure la portabilité de la couche WP2 vers les futures extensions de BR-PREDICT au-delà de l'oncologie pulmonaire.
