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

