# BR-PREDICT -- Dossier i-Demo Bpifrance
## Description des Work Packages (WP1 -- WP6)

**Programme** : BR-PREDICT -- Première plateforme d'évaluation prédictive du bénéfice-risque
**Porteur** : ArcaScience | **Pathologie d'ancrage** : Cancer du poumon
**Architecture** : 90 % générique (schéma, extraction, calibration, fusion) / ~10 % calibration pathologie-spécifique

---

## WP1 -- Prédiction du rapport bénéfice-risque à partir de la structure chimique

### Intitulé & Objectif

**WP1 : Modèles prédictifs QSAR/QSTR pour l'estimation du rapport bénéfice-risque à partir de la structure moléculaire seule.**

L'objectif de ce lot est de démontrer qu'il est possible, dès la phase de criblage chimique, de produire une estimation quantitative du profil bénéfice-risque (B-R) d'un candidat-médicament à partir de sa seule représentation structurale. Ce lot constitue la couche prédictive la plus précoce de BR-PREDICT : il intervient en amont de toute donnée biologique ou clinique et vise à réduire le taux d'attrition -- aujourd'hui de 92 % entre la phase préclinique et la mise sur le marché -- en identifiant, dès la conception moléculaire, les signaux d'efficacité potentielle et les alertes de toxicité structurelle.

### Hypothèses scientifiques & périmètre

L'hypothèse fondatrice est que la structure chimique d'une molécule encode une information suffisante pour prédire, avec une incertitude contrôlée, à la fois son activité biologique sur des cibles d'intérêt (volet bénéfice) et sa propension à induire des effets toxiques (volet risque). Cette hypothèse repose sur les principes fondamentaux de la relation structure-activité quantitative (QSAR) et de la relation structure-toxicité quantitative (QSTR), validés dans la littérature sur des périmètres restreints (par exemple, QSAR FGFR-1 : R² = 0,7809 en entraînement, 0,7413 en test). Le périmètre couvre les petites molécules organiques ; les biologiques (anticorps, protéines recombinantes) sont explicitement hors champ pour ce lot, leur profil B-R relevant davantage des WP2 et WP3. La pathologie d'ancrage pour la validation est le cancer du poumon, conformément à la stratégie projet.

### Méthodologie technique détaillée

**T1.1 -- Qualification des sources.** Trois corpus de référence sont exploités : les données de cytotoxicité qHTS du NCGC (National Chemical Genomics Center), la base ChEMBL (données d'activité biologique structurées, > 2,4 millions de composés) et ToxCast (données toxicologiques haute débitance de l'EPA). Chaque source fait l'objet d'un audit de couverture, de cohérence et de biais de publication avant intégration dans la Profiling Base.

**T1.2 -- Construction et curation de la base de données.** Une base dédiée est constituée, regroupant les molécules commercialisées, les adjuvants et les protéines disposant d'un profil B-R documenté. La curation inclut la normalisation des identifiants chimiques (InChI, SMILES canoniques), la déduplication, et l'annotation croisée avec les données réglementaires (RCP, rapports PSUR) disponibles dans la Profiling Base 100B d'ArcaScience.

**T1.3 -- Représentation moléculaire et calcul de descripteurs.** Chaque molécule est convertie en vecteurs de descripteurs exploitables par les modèles ML : fingerprints moléculaires (Morgan/ECFP, MACCS), descripteurs physicochimiques (RDKit), et représentations par graphes moléculaires pour les architectures GNN. L'objectif est de disposer de représentations complémentaires permettant d'alimenter plusieurs familles d'algorithmes.

**T1.4 -- Développement des modèles QSAR (bénéfice).** Plusieurs approches ML sont entraînées et comparées : Random Forest, Gradient Boosting, et réseaux de neurones sur graphes (GNN). Les modèles sont entraînés sur les données d'activité (IC50, EC50, Ki) pour les cibles pertinentes en oncologie pulmonaire (EGFR, ALK, KRAS, PD-L1, etc.). Un domaine d'applicabilité est défini pour chaque modèle afin de quantifier la confiance de la prédiction en fonction de la distance au jeu d'entraînement.

**T1.5 -- Développement des modèles QSTR (risque).** Selon une architecture parallèle, des modèles ML sont entraînés sur les données de toxicité (cytotoxicité, génotoxicité, hépatotoxicité, cardiotoxicité hERG) pour produire un score de risque structurel. Les données ToxCast et NCGC alimentent ces modèles. Une attention particulière est portée au déséquilibre de classes, traité par suréchantillonnage (SMOTE) et pondération des pertes.

**T1.6 -- Intégration et validation.** Les scores QSAR (bénéfice) et QSTR (risque) sont intégrés dans un score B-R composite, calibré sur des molécules commercialisées dont le profil B-R est connu. La validation est réalisée par cross-validation stratifiée et sur un jeu de test externe constitué de molécules retirées du marché (volet risque) et de molécules approuvées en oncologie pulmonaire (volet bénéfice).

### Tâches & articulation avec les autres WPs

Le WP1 fournit la couche prédictive structurelle qui constitue le premier niveau d'entrée du moteur BR-PREDICT. Ses scores alimentent directement le WP5 (intégration multi-échelle) et servent de baseline pour mesurer le gain incrémental apporté par les données in vivo (WP2) et génomiques (WP3). Les partenaires Sanofi, Cedars-Sinai et Mayo Clinic contribuent à la validation en confrontant les prédictions WP1 à des cas réels de leur pipeline. Le calendrier s'étend de Q1 2026 à Q1 2027.

### Livrables & Jalons

- **L1.1** : Base de données curée structure-activité-toxicité (M6).
- **L1.2** : Modèles QSAR validés sur les cibles d'intérêt en oncologie pulmonaire (M9).
- **L1.3** : Modèles QSTR validés sur les endpoints toxicologiques prioritaires (M9).
- **L1.4** : Score B-R composite intégré et rapport de validation (M12).
- **Jalon EC1** (fin 2026) : démonstration de la capacité à prédire le profil B-R à partir de la structure chimique seule, avec incertitude quantifiée.

### KPI & protocole d'évaluation

L'objectif cible est une AUC > 0,65 sur le jeu de validation externe, seuil cohérent avec l'état de l'art QSAR sur des espaces chimiques diversifiés. La précision est mesurée par AUC-ROC pour les modèles de classification et par R²/RMSE pour les modèles de régression. Le protocole inclut une validation croisée 5-fold sur le jeu d'entraînement et une évaluation finale sur un jeu de test externe strictement disjoint. Les résultats sont stratifiés par famille chimique pour identifier les zones de confiance et les zones de faiblesse du domaine d'applicabilité.

### Risques, verrous, et plans de mitigation

- **Domaine d'applicabilité limité** : aucun modèle QSAR unique ne couvre l'intégralité de l'espace chimique. Mitigation : définition explicite du domaine d'applicabilité par modèle, combinaison de modèles spécialisés, et score de confiance associé à chaque prédiction.
- **Dégradation de précision sur scaffolds dissimilaires** : les performances des GNN et Random Forest chutent significativement sur les structures éloignées du jeu d'entraînement. Mitigation : enrichissement itératif de la base d'entraînement, apprentissage par transfert, et signalisation explicite des prédictions hors domaine.
- **Exclusion des biologiques** : le WP1 ne couvre pas les anticorps et protéines thérapeutiques. Mitigation : cette limitation est compensée par les WP2 et WP3 qui traitent ces modalités via des données biologiques et génomiques.

### Contribution à la répétabilité multi-pathologies & à l'industrialisation

Les modèles QSAR/QSTR développés dans le WP1 sont, par construction, indépendants de la pathologie : ils s'appuient sur la structure chimique et des endpoints biologiques/toxicologiques génériques. La calibration sur l'oncologie pulmonaire porte uniquement sur le choix des cibles d'intérêt et des seuils de pertinence clinique, soit environ 10 % de la configuration. Le passage à une autre pathologie (neurologie, immunologie, cardiologie) nécessite uniquement la redéfinition du panel de cibles et du jeu de validation, sans réentraînement de l'architecture. Ce design modulaire contribue directement à l'objectif d'industrialisation de BR-PREDICT comme plateforme générique de prédiction B-R.

---

## WP2 -- Prédiction du rapport bénéfice-risque à partir des données in vivo et toxicologiques

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

---

## WP3 -- Prédiction du rapport bénéfice-risque par biomarqueurs, cibles moléculaires et polymorphismes génétiques

### Intitulé & Objectif

**WP3 : Modèles prédictifs pharmaco-génomiques pour l'estimation du rapport bénéfice-risque par intégration des biomarqueurs, cibles thérapeutiques et variants génétiques.**

L'objectif de ce lot est de construire la couche prédictive la plus granulaire de BR-PREDICT, exploitant les relations entre une molécule, ses cibles moléculaires, les biomarqueurs associés à une pathologie, et les polymorphismes génétiques influençant la réponse thérapeutique et la survenue d'effets indésirables. Le WP3 constitue l'axe d'innovation le plus avancé du projet : si les approches de pharmacogénomique ont démontré des précisions élevées sur des périmètres restreints (UGenome, 2025 : jusqu'à 99 % de précision sur certains panels), elles n'ont jamais été déployées à l'échelle d'une plateforme systématique de prédiction B-R intégrant simultanément structure moléculaire, profil génomique et contexte pathologique. Ce lot s'applique à toutes les modalités thérapeutiques (petites molécules, biologiques, thérapies ciblées) et pose les fondations de la médecine personnalisée prédictive dans BR-PREDICT.

### Hypothèses scientifiques & périmètre

Trois hypothèses guident ce lot. Premièrement, le profil génomique du patient (polymorphismes des gènes codant pour les cibles thérapeutiques, les enzymes métaboliques, et les transporteurs) module significativement le rapport B-R individuel d'un traitement donné. Deuxièmement, les relations entre biomarqueurs et issues cliniques, aujourd'hui dispersées dans la littérature et les bases de données spécialisées, peuvent être extraites, structurées et modélisées par apprentissage automatique pour produire des prédictions exploitables. Troisièmement, l'intégration du mécanisme d'action (MoA) de la molécule avec le génotype de la cible permet de prédire non seulement l'efficacité mais aussi le profil de risque spécifique au patient. L'état de l'art soutient ces hypothèses : Park et al. (2023) ont démontré la capacité de modèles ML/DL à prédire l'IC50 à partir de profils moléculaires ; Miranda et al. (2021) ont montré que l'intégration de polymorphismes et de variables cliniques améliore la prédiction de la réponse thérapeutique et des effets indésirables. Le périmètre du WP3 est volontairement transversal : il couvre toutes les classes thérapeutiques et toutes les pathologies, avec une validation prioritaire en oncologie pulmonaire.

### Méthodologie technique détaillée

**T3.1 -- Qualification des sources.** Deux axes de sources sont qualifiés : (i) les bases de données biomarqueurs-pathologie (PharmGKB, ClinVar, COSMIC, OncoKB, cBioPortal) et (ii) les bases de données de variants génétiques des cibles thérapeutiques (UniProt variants, gnomAD, dbSNP, ClinGen). Chaque source est évaluée sur sa couverture en oncologie pulmonaire, sa qualité d'annotation fonctionnelle (variant bénin / pathogène / de signification incertaine), et sa compatibilité avec les ontologies utilisées dans la Profiling Base.

**T3.2 -- Extraction NLP des polymorphismes génétiques et structuration fonctionnelle.** Les Contextualizing SLMs sont entraînés pour extraire de la littérature biomédicale les informations suivantes : variants génétiques mentionnés (notation HGVS), effet fonctionnel rapporté (perte/gain de fonction, modification d'affinité, altération métabolique), association à une réponse thérapeutique ou à un effet indésirable, et niveau de preuve (étude de cas, cohorte, essai contrôlé). L'extraction produit des triplets structurés {variant -- effet fonctionnel -- issue clinique} qui alimentent la base de données intégrée.

**T3.3 -- Base de données intégrée multi-dimensionnelle.** La base de données du WP3 structure deux graphes relationnels complémentaires : (i) Molécule -> Biomarqueurs/Génomique -> Pathologie, reliant chaque molécule à ses biomarqueurs de réponse et aux pathologies concernées ; (ii) Molécule -> Cible -> Variants -> Impacts fonctionnels, reliant chaque molécule à ses cibles thérapeutiques, aux variants connus de ces cibles, et aux conséquences fonctionnelles documentées. Ces deux graphes sont intégrés dans la Profiling Base existante et indexés pour le requêtage par les modèles ML.

**T3.4 -- Modèle ML de prédiction du bénéfice.** Le modèle de bénéfice prend en entrée le profil biomarqueurs/génomique du patient et les caractéristiques de la cible thérapeutique, et produit en sortie une prédiction de bénéfice (probabilité de réponse, durée de réponse estimée). L'architecture combine des embeddings de graphes de connaissances (pour capturer les relations complexes biomarqueurs-cibles-pathologie) et des couches d'attention pour pondérer la contribution de chaque biomarqueur. En oncologie pulmonaire, le modèle est entraîné sur les associations connues : mutations EGFR et réponse aux TKI, réarrangements ALK/ROS1 et réponse au crizotinib/lorlatinib, expression PD-L1 et réponse aux anti-PD-1/PD-L1, charge mutationnelle tumorale et réponse à l'immunothérapie.

**T3.5 -- Modèle ML de prédiction du risque.** Le modèle de risque prend en entrée le génotype de la cible thérapeutique et le mécanisme d'action de la molécule, et produit en sortie une prédiction de risque (probabilité et sévérité des effets indésirables). Ce modèle exploite les relations connues entre polymorphismes pharmacogénomiques et toxicité : variants CYP2D6 et toxicité des métaboliseurs lents, variants DPYD et toxicité au 5-fluorouracile, variants UGT1A1 et toxicité à l'irinotécan. L'objectif est de généraliser ces relations à l'ensemble des couples {cible x molécule} par apprentissage sur les données historiques.

**T3.6 -- Validation et intégration.** La validation suit un protocole en deux temps : (i) validation rétrospective sur des cohortes de patients avec profil génomique et issue clinique connus (données Cedars-Sinai, Mayo Clinic, ICM) ; (ii) confrontation croisée avec les prédictions WP1 et WP2 pour évaluer la complémentarité et le gain incrémental de la couche génomique. Les résultats sont intégrés dans le moteur BR-PREDICT via le WP5.

### Tâches & articulation avec les autres WPs

Le WP3 partage l'infrastructure commune déployée en T2.1 (WP2). Il reçoit du WP2 les corrélations efficacité-biomarqueurs observées in vivo et fournit au WP5 les scores prédictifs génomiques pour l'intégration multi-échelle. Le WP3 entretient un lien étroit avec le WP4 (données cliniques) qui fournit les cohortes de validation avec profils génomiques annotés. Les partenaires Institut du Cerveau (ICM), Cedars-Sinai et Mayo Clinic contribuent les données de cohortes génomiques ; Sanofi valide les prédictions sur des candidats en développement. Le calendrier s'étend de Q2 2026 à Q3 2027.

### Livrables & Jalons

- **L3.1** : Modèle NLP pour l'extraction d'informations génétiques et pharmacogénomiques (M9).
- **L3.2** : Base de données intégrée cibles <-> biomarqueurs <-> pathologie <-> variants génétiques (M12).
- **L3.3** : Modèles ML prédictifs B-R basés sur les données génomiques et les cibles, validés (M18).
- **L3.4** : Capacité démontrée de prédiction B-R pour une structure donnée via le profil génomique et les caractéristiques de la cible (M18).
- **Jalon EC2** (mi-2027) : objectifs de précision atteints pour un modèle généralisable par cible et par pathologie.

### KPI & protocole d'évaluation

La précision de prédiction est mesurée sur les molécules commercialisées disposant de données pharmacogénomiques validées. Les objectifs cibles de précision sont définis par périmètre : pour les associations pharmacogénomiques bien établies (niveau de preuve 1A/1B PharmGKB), l'objectif cible est une AUC > 0,80 ; pour les associations émergentes, l'objectif cible est une AUC > 0,65. Le protocole inclut une validation croisée sur les données d'entraînement et une évaluation externe sur les cohortes partenaires. La valeur ajoutée du WP3 est mesurée par le gain de précision par rapport aux prédictions combinées WP1+WP2 seules.

### Risques, verrous, et plans de mitigation

- **Hétérogénéité et incomplétude des données génomiques** : les cohortes disponibles présentent des biais de représentation ethnique et des taux de couverture variables selon les gènes. Mitigation : stratification des modèles par population, signalisation explicite des sous-groupes insuffisamment représentés, enrichissement progressif via les cohortes partenaires internationales (Cedars-Sinai, Mayo Clinic).
- **Variants de signification incertaine (VUS)** : une fraction significative des variants identifiés n'a pas d'annotation fonctionnelle validée. Mitigation : les VUS sont traités comme des features à incertitude élevée dans les modèles, avec un score de confiance réduit ; les modèles sont conçus pour fonctionner de manière dégradée en l'absence de cette information.
- **Passage à l'échelle non testé** : la pharmacogénomique prédictive n'a jamais été déployée à l'échelle systématique d'une plateforme B-R couvrant simultanément toutes les cibles et toutes les pathologies. Mitigation : approche incrémentale, validation d'abord sur les associations bien établies, puis extension progressive du périmètre avec des critères de qualité explicites à chaque palier.

### Contribution à la répétabilité multi-pathologies & à l'industrialisation

Le WP3 est, parmi les lots de données, celui dont la portabilité multi-pathologies est la plus intrinsèque : les relations entre polymorphismes génétiques et réponse thérapeutique sont, par nature, indépendantes de la pathologie d'ancrage. Les architectures de graphes relationnels {Molécule -> Cible -> Variants -> Impacts} sont identiques quelle que soit l'aire thérapeutique. La calibration pathologie-spécifique porte uniquement sur la sélection des biomarqueurs pertinents et des cohortes de validation, soit un effort estimé à moins de 10 % du travail total de déploiement. Ce lot constitue ainsi le socle de la stratégie de médecine personnalisée prédictive de BR-PREDICT, directement extensible à la neurologie (via l'ICM), à la cardiologie, et à l'immunologie dans les phases ultérieures de commercialisation.

---

## WP4 -- Modèles Prédictifs en Conditions Réelles (Real-World Evidence)

**Partenaires** : Cedars Sinai, Mayo Clinic, Institut du Cerveau (ICM), Gradient Health
**Période** : Q2 2026 -- Q4 2027 | **Jalon principal** : EC2 (mi-2027)

### Intitulé & Objectif

**WP4 : Extraction, structuration et modélisation prédictive des données de vie réelle (RWE) pour la validation et le renforcement des relations structure-cible-bénéfice-risque.**

L'objectif est double. Premièrement, construire un pipeline reproductible d'extraction et de normalisation des données de pharmacovigilance et de données cliniques réelles issues de FAERS (FDA Adverse Event Reporting System), d'entrepôts de données de santé hospitaliers (EDS) et de sources prototypiques de l'European Health Data Space (EHDS). Deuxièmement, développer des modèles prédictifs qui exploitent ces données pour valider, compléter et, le cas échéant, corriger les profils bénéfice-risque (B-R) générés par les WP1-3 à partir de données moléculaires, précliniques et génomiques. La valeur ajoutée de WP4 réside dans l'intégration de facteurs absents des essais cliniques contrôlés : comorbidités, polymédication, variabilité socio-démographique et conditions d'utilisation en pratique.

### Hypothèses scientifiques & périmètre

H1 : Les signaux de sécurité et d'efficacité détectables dans les bases RWE permettent de discriminer, avec une précision supérieure aux modèles WP1-3 seuls, le profil B-R d'une molécule en conditions réelles. H2 : L'hétérogénéité des populations non sélectionnées (comorbidités, âge, polymédication) constitue une source d'information exploitable -- et non uniquement un bruit -- lorsqu'elle est correctement modélisée. H3 : Un modèle généraliste intégrant données RWE et données moléculaires/précliniques (WP1-3) est transférable entre pathologies moyennant une calibration limitée (~10 % des paramètres).

Le périmètre initial cible la pathologie d'ancrage (cancer du poumon) puis sera étendu à au moins deux aires thérapeutiques supplémentaires avant EC3.

### Méthodologie technique détaillée

**Qualification des sources (T4.1).** Chaque source RWE est évaluée selon une grille multicritère : couverture temporelle, granularité (patient-level vs. agrégé), complétude des variables clés (indication, posologie, durée d'exposition, événements indésirables codés MedDRA PT/SOC, comorbidités CIM-10, co-prescriptions ATC), biais de notification (sous-reporting FAERS, biais de sélection EDS). Un score de qualité composite est attribué ; seules les sources dépassant le seuil prédéfini alimentent les modèles.

**Extraction et structuration (T4.2).** Les Contextualizing SLMs d'ArcaScience -- modèles de langage de petite taille entraînés par des cliniciens -- extraient les entités pertinentes des narratifs FAERS (champs libre-texte du formulaire MedWatch) et des comptes rendus d'hospitalisation des EDS partenaires (Cedars Sinai, Mayo Clinic, ICM). L'extraction est suivie d'une normalisation terminologique vers MedDRA 27.x, SNOMED CT et ChEBI, puis d'un alignement temporel (date index = date de première prescription). Le pipeline intègre un module de dédoublonnage probabiliste (record linkage) pour les cas FAERS multiples et un module de pseudonymisation conforme RGPD/HIPAA.

**Modèles prédictifs -- Bénéfices (T4.3) et Risques (T4.4).** Pour chaque molécule, les variables RWE structurées sont fusionnées avec les descripteurs moléculaires et précliniques issus de WP1-3. L'architecture retenue est un modèle gradient-boosted (XGBoost/LightGBM) pour la prédiction tabulaire, complété par un réseau à attention temporelle (Temporal Fusion Transformer) pour les trajectoires patient longitudinales. Les cibles prédictives sont : (i) survenue d'EIG codés MedDRA PT dans les 6/12/24 mois ; (ii) réponse thérapeutique (survie sans progression, réponse RECIST pour l'oncologie). Les modèles sont entraînés avec validation croisée stratifiée par source pour garantir la robustesse inter-bases.

**Validation et calibration (T4.5).** Calibration externe sur cohortes rétrospectives indépendantes (Mayo Clinic, ICM). Métriques : AUC-ROC, AUC-PR, calibration slope et intercept (calibration plots), Net Reclassification Improvement par rapport aux prédictions WP1-3 seules. Analyse de sous-groupes (âge, comorbidités, ethnie déclarée) pour identifier les populations où le gain RWE est maximal.

### Tâches & articulation avec les autres WPs

| Tâche | Entrée | Sortie | Lien WP |
|-------|--------|--------|---------|
| T4.1 Qualification sources | Catalogues FAERS, EDS, EHDS | Grille qualité, sources qualifiées | -- |
| T4.2 Extraction & structuration | Données brutes sources qualifiées | Tables normalisées patient-level | WP5 (terminologies) |
| T4.3 Modèles prédictifs Bénéfices | Tables T4.2 + descripteurs WP1-3 | Scores prédictifs efficacité | WP1, WP2, WP3 |
| T4.4 Modèles prédictifs Risques | Tables T4.2 + descripteurs WP1-3 | Scores prédictifs EIG/ADR | WP1, WP2, WP3 |
| T4.5 Validation & calibration | Prédictions T4.3/T4.4, cohortes externes | Rapport de performance, calibration | WP6 (intégration) |

Gradient Health fournit un accès structuré à des jeux de données d'imagerie annotés corrélés aux données cliniques, utilisés comme variables complémentaires dans T4.3/T4.4. Cedars Sinai et Mayo Clinic sont à la fois fournisseurs de données (EDS) et sites de validation externe (T4.5).

### Livrables & Jalons

- **L4.1** (EC1, fin 2026) : Pipeline d'extraction/structuration opérationnel, grille de qualification appliquée à FAERS + 2 EDS.
- **L4.2** (EC2, mi-2027) : Modèles prédictifs RWE B-R pour le cancer du poumon, rapport de calibration externe.
- **L4.3** (EC2+3 mois) : Modèle généralisable intégrant données RWE + moléculaires + précliniques (WP1-3 + WP4), applicable à 2+ pathologies.
- **L4.4** (EC3, fin 2028) : Documentation complète du pipeline, code reproductible, rapport de validation multi-pathologies.

### KPI & protocole d'évaluation

- **KPI-1** : AUC-ROC du modèle WP4 (RWE intégré) strictement supérieure à celle des modèles WP1-3 seuls sur la cohorte de test cancer du poumon (objectif cible : delta AUC >= 0,05).
- **KPI-2** : Calibration slope entre 0,8 et 1,2 sur cohorte externe.
- **KPI-3** : Couverture >= 80 % des EIG connus (MedDRA PT) pour les molécules du jeu de validation.
- Protocole : validation croisée 5-fold stratifiée par source, puis validation externe sur cohorte temporellement disjointe (hold-out temporel 2022-2025).

### Risques, verrous, et plans de mitigation

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Qualité/complétude variable des données RWD (sous-reporting FAERS, données manquantes EDS) | Élevé | Élevée | Grille de qualification stricte (T4.1) ; imputation multiple avec analyse de sensibilité ; pondération inverse de la probabilité de notification |
| Hétérogénéité entre sources RWD (codages, granularité, populations) | Moyen | Élevée | Normalisation terminologique centralisée (T4.2 + WP5) ; modèles avec variable indicatrice de source ; méta-analyse à effets aléatoires |
| Variabilité inter-pathologies difficile à modéliser | Élevé | Moyenne | Architecture modulaire : couche partagée (90 %) + couche spécifique calibrée par pathologie (~10 %) ; validation incrémentale pathologie par pathologie |
| Accès aux données EHDS non finalisé dans le calendrier | Moyen | Moyenne | Sources FAERS + EDS partenaires suffisantes pour la validation cancer du poumon ; EHDS traité comme source complémentaire, non bloquante |

### Contribution à la répétabilité multi-pathologies & à l'industrialisation

L'architecture de WP4 est conçue pour être 90 % générique. Le pipeline d'extraction (T4.2) repose sur les Contextualizing SLMs d'ArcaScience dont les capacités NER/RE sont indépendantes de la pathologie, et sur des terminologies standardisées (MedDRA, SNOMED CT). Les modèles prédictifs (T4.3/T4.4) séparent une couche de représentation partagée -- descripteurs moléculaires, profil patient, signaux RWE -- d'une couche de calibration pathologie-spécifique paramétrable en fine-tuning sur un volume limité de données annotées. Ce découplage permet un déploiement incrémental vers de nouvelles aires thérapeutiques sans reconstruction complète. Le modèle généralisable livré en L4.3 constitue le socle de l'intégration WP6 et alimente directement le Knowledge Graph de WP5 en relations validées par les données de vie réelle.

---

## WP5 -- Graphe de Connaissances & Couche Ontologique Unifiée

**Période** : Q3 2027 -- Q2 2028 | **Jalons** : EC2 (mi-2027, schéma ontologique), EC3 (fin 2028, KG complet + API)

### Intitulé & Objectif

**WP5 : Conception et déploiement d'un graphe de connaissances interopérable intégrant les données moléculaires, précliniques, génomiques et de vie réelle dans une couche sémantique unifiée au service du world model BR-PREDICT.**

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

---

## WP6 -- World Model : Intégration Prédictive, Raisonnement Causal et Simulation Bénéfice-Risque

**Partenaires validation** : Sanofi, Cedars Sinai, Mayo Clinic, Institut du Cerveau (ICM), AMI Labs (en cours de cadrage) | **Partenaire données** : Gradient Health
**Période** : Q1 2027 -- Q4 2028 | **Jalons** : EC2 (mi-2027, architecture intégrée), EC3 (fin 2028, world model opérationnel validé)

### Intitulé & Objectif

**WP6 : Conception, intégration et validation d'un world model capable de simuler des profils bénéfice-risque complets pour toute molécule en développement, de la phase préclinique à la phase II, par fusion multimodale des modèles prédictifs WP1-4 et du graphe de connaissances WP5.**

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
