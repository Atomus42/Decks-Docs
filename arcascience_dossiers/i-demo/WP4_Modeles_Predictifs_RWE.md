## WP4 -- Modèles Prédictifs en Conditions Réelles (Real-World Evidence)

**Responsable** : ArcaScience | **Partenaires** : Cedars Sinai, Mayo Clinic, Institut du Cerveau (ICM), Gradient Health
**Période** : T0+6 (Q2 2026) -- T0+18 (Q4 2027) | **Jalon principal** : EC2 (mi-2027)

---

### Intitulé & Objectif

WP4 -- *Extraction, structuration et modélisation prédictive des données de vie réelle (RWE) pour la validation et le renforcement des relations structure-cible-bénéfice-risque.*

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
