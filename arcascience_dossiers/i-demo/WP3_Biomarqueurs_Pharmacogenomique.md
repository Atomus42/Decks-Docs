## WP3 -- Prédiction du rapport bénéfice-risque par biomarqueurs, cibles moléculaires et polymorphismes génétiques

**Responsable** : ArcaScience | **Partenaires** : Sanofi, Cedars Sinai, Mayo Clinic, Institut du Cerveau (ICM)
**Période** : Q2 2026 -- Q3 2027 | **Jalon principal** : EC2 (mi-2027)

---

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
