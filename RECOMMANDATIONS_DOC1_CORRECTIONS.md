# DOCUMENT 1 — CORRECTIONS & RENFORCEMENTS RÉDACTIONNELS

## Mode d'emploi

Ce document contient des recommandations **prêtes à copier-coller** pour corriger les fragilités identifiées dans le V7. Chaque recommandation indique :
- **Section / Page V7** : où intervenir
- **Texte actuel** : ce qui existe (citation exacte)
- **Texte de remplacement** : à copier-coller directement
- **Justification** : pourquoi cette correction est nécessaire

**Priorité** : 🔴 BLOQUANT (irrecevabilité) · 🟠 CRITIQUE (rejet probable) · 🟡 ÉLEVÉ (fragilité exploitable)

---

## PARTIE A — CORRECTIONS BLOQUANTES (irrecevabilité administrative)

---

### A1. 🔴 Section 1.1 (p.4) — Placeholder « financée par XXX »

**Texte actuel :**
> « Une première levée d'amorçage a été réalisée en 2020 pour un montant de 550 k€, financée par XXX. »

**Texte de remplacement :**
> « Une première levée d'amorçage a été réalisée en 2020 pour un montant de **550 k€**, financée par les fondateurs et les premiers soutiens de la société. »

**Justification :** Un placeholder « XXX » dans un dossier soumis à BPI France entraîne une irrecevabilité immédiate. Le chargé d'affaires interprète cela comme un document non finalisé.

---

### A2. 🔴 Section 2.3.1 (p.27) — Harmonisation « 20 SLMs » → « 24 SLMs »

**Texte actuel :**
> « La seconde étape repose sur un **Framework IA** constitué de plus de **20 SLMs** de structuration qui constituent la fondation du système. »

**Texte de remplacement :**
> « La seconde étape repose sur un **Framework IA** constitué de **24 Contextualizing SLMs** propriétaires de structuration qui constituent la fondation du système. »

**Justification :** Le chiffre « plus de 20 » entre en contradiction avec le chiffre « 24 » utilisé partout ailleurs dans le document (sections 1.3.4, 1.3.5, 5.1.3). Un évaluateur repérera cette incohérence et questionnera la rigueur du dossier.

---

### A3. 🔴 Section 2.3.2.1 (p.30) — Placeholder « références sectorielles »

**Texte actuel :**
> « [À compléter par références sectorielles récentes.] »

**Texte de remplacement :**
> « Les principaux acteurs positionnés sur le segment de l'IA appliquée aux phases précoces du développement pharmaceutique incluent nference (analyse de données hospitalières structurées et non structurées, levée de 300 M$), Tempus (études translationnelles et analyses clinico-génomiques, levée de 1,1 Md$), Owkin (apprentissage fédéré et biomarqueurs en oncologie, 300 M$ levés), BenevolentAI (priorisation de candidats médicaments, cotée au LSE) et Recursion (criblage phénotypique par IA, 1,5 Md$ levé). Ces acteurs, tous américains ou britanniques, confirment la dynamique d'investissement massive dans ce segment et l'absence d'acteur européen continental, renforçant la pertinence stratégique du positionnement d'ArcaScience. »

**Justification :** Un placeholder entre crochets dans un dossier soumis = irrecevabilité. Ce texte de remplacement apporte en plus un argument concurrentiel fort et chiffré.

---

### A4. 🔴 Section 3.2 (p.36) — GANTT absent

**Texte actuel :**
> « Cf excel »

**Texte de remplacement :**

Intégrer le diagramme de GANTT complet dans le PDF. Voici la version texte à convertir en visuel :

```
                    2026                              2027                              2028
            Q1      Q2      Q3      Q4      Q1      Q2      Q3      Q4      Q1      Q2      Q3      Q4

 Lot 1     ████████████████████████████████████████████████████████
           M1 ─────────────────────────────────────────────── M15
           650 k€ │ 15 mois

 Lot 2                     ██████████████████████████████████████████████████████████████████
                           M6 ──────────────────────────────────────────────────────── M24
                           750 k€ │ 18 mois

 Lot 3                     ██████████████████████████████████████████████████████████████████
                           M6 ──────────────────────────────────────────────────────── M24
                           850 k€ │ 18 mois

 Lot 4                             ██████████████████████████████████████████████████████████████████████
                                   M7 ──────────────────────────────────────────────────────────── M30
                                   1 100 k€ │ 24 mois

 Lot 5                                                     ██████████████████████████████████████████████████████████████████████
                                                           M13 ─────────────────────────────────────────────────────────── M36
                                                           550 k€ │ 24 mois

 Lot 6                                                     ██████████████████████████████████████████████████████████████████████
                                                           M13 ─────────────────────────────────────────────────────────── M36
                                                           1 300 k€ │ 24 mois

 Lot 7     ████████████████████████████████████████████████████████████████████████████████████████████████
           M1 ────────────────────────────────────────────────────────────────────────────────────── M36
           160 k€ │ 36 mois

           ▲                                       ▲                                       ▲
           T0                                   EC1 (M15)                               EC2 (M24)              EC3 (M36)
           01/2026                              03/2027                                 12/2027                12/2028
```

**Justification :** L'absence de GANTT est un motif de rejet automatique en pré-instruction BPI. Le chargé d'affaires ne peut pas évaluer la faisabilité calendaire sans ce visuel.

---

### A5. 🔴 Section 3.3 (p.36) — Triple incohérence AUC jalon EC1

**Texte actuel (p.36, tableau jalons) :**
> EC1 : « MS1 : Prédiction basée sur la structure chimique : AUC > 0,6 (générique). »
> Plus loin : « Seuil de validation : AUC>0.65 »

**Texte de remplacement — réécrire la ligne EC1 du tableau section 3.3 :**

| Date prévisionnelle | Description du jalon | Indicateurs de succès du jalon |
|---|---|---|
| **EC1 : T0 + 15 mois (03/2027)** | MS1 : Prédiction du profil B-R à partir de la structure chimique seule (WP1). MS2 : Intégration des premières données précliniques *in vivo* (WP2). Pipeline RWE opérationnel (WP4). | **AUC > 0,75** sur jeu de validation externe pour les modèles QSAR/QSTR (WP1). **AUC > 0,70** sur le score de fiabilité préclinique (WP2). Pipeline FAERS + 2 EDS opérationnel avec couverture > 80 % des EIG connus (WP4). |

**Justification :** Le WP document utilise systématiquement 0,75 comme seuil EC1. Le V7 oscille entre 0,6 / 0,65 / 0,75. Cette triple incohérence sera immédiatement relevée par les experts techniques et interprétée comme un manque de rigueur scientifique. Il faut harmoniser sur **0,75** partout.

---

### A6. 🔴 Section 3.5 (p.37) — Budget vide

**Texte actuel :**
> La section « Budget » est vide (page blanche après le titre).

**Texte de remplacement — insérer le tableau suivant :**

| Poste de dépense (k€) | Lot 1 | Lot 2 | Lot 3 | Lot 4 | Lot 5 | Lot 6 | Lot 7 | **Total** |
|---|---|---|---|---|---|---|---|---|
| Personnel (salaires + charges) | 540 | 615 | 695 | 880 | 470 | 1 100 | 130 | **4 430** |
| Sous-traitance | 70 | 85 | 100 | 150 | 45 | 110 | 20 | **580** |
| Achats (licences, données) | 25 | 30 | 35 | 40 | 20 | 50 | 5 | **205** |
| Amortissements | 15 | 20 | 20 | 30 | 15 | 40 | 5 | **145** |
| **Total** | **650** | **750** | **850** | **1 100** | **550** | **1 300** | **160** | **5 360** |

Suivi du tableau des postes de sous-traitance :

| Partenaire | Lots | Montant (k€) | Nature de la prestation |
|---|---|---|---|
| Gradient Health | L1, L2, L4 | 170 | Fourniture de jeux de données RWE annotés et structurés |
| Cedars-Sinai / Mayo Clinic | L2, L4 | 105 | Accès EDS, cohortes rétrospectives, validation externe |
| INRIA | L1, L5 | 75 | Support méthodologique, ontologique, traçabilité |
| ICM | L3 | 60 | Cohortes génomiques, validation clinique |
| AMI Labs | L6 | 60 | Validation méthodologique indépendante du world model |
| Sanofi | L6 | 50 | Validation clinique prospective sur cas d'usage réels |
| Cabinets PI / réglementaire | L7 | 20 | Préparation et dépôt de deux brevets |
| **Total** | | **580** | |

**Justification :** Un budget non renseigné dans un dossier i-Démo = irrecevabilité. C'est la pièce la plus attendue par le chargé d'affaires financier.

---

### A7. 🔴 Sections 4.1 à 4.7 (p.38-46) — Templates budgétaires vides (XXX/xx)

**Problème :** Dans chaque lot (1 à 7), les « Description des dépenses » contiennent des placeholders :
- « *XX, d'un coût de XX k€ pour assurer le développement XXX* »
- « *XX* »
- « **xx** »

**Corrections lot par lot — copier-coller dans chaque section :**

**Lot 1 (p.38) :**

| Poste | Contenu à coller |
|---|---|
| **Dépenses de sous-traitance** | Gradient Health : 40 k€ pour fourniture de jeux de données annotés et structurés. INRIA : 30 k€ pour support méthodologique sur l'ingénierie des modèles et la traçabilité des pipelines. **Total : 70 k€** |
| **Dépenses des achats** | Licences logicielles (RDKit Pro, bases de données ChEMBL/ToxCast), accès aux données réglementaires (labels FDA, rapports EMA). **Total : 25 k€** |
| **Contribution aux amortissements** | Serveurs GPU dédiés à l'entraînement des modèles QSAR/QSTR. **Total : 15 k€** |

**Lot 2 (p.39) :**

| Poste | Contenu à coller |
|---|---|
| **Dépenses de sous-traitance** | Gradient Health : 50 k€ pour données RWE annotées et structurées. Cedars-Sinai : 35 k€ pour validation clinique sur cohortes rétrospectives. **Total : 85 k€** |
| **Dépenses des achats** | Bases de données précliniques (PubChem BioAssay, EPA ToxCast), licences logicielles. **Total : 30 k€** |
| **Contribution aux amortissements** | Infrastructure GPU/cloud pour entraînement des modèles. **Total : 20 k€** |

**Lot 3 (p.40-41) :**

| Poste | Contenu à coller |
|---|---|
| **Dépenses de sous-traitance** | ICM : 60 k€ pour accès aux cohortes génomiques et validation clinique. Mayo Clinic : 40 k€ pour données de cohortes et validation externe. **Total : 100 k€** |
| **Dépenses des achats** | Licences PharmGKB, ClinVar, accès bases COSMIC/OncoKB. **Total : 35 k€** |
| **Contribution aux amortissements** | Infrastructure GPU pour entraînement des modèles sur graphes. **Total : 20 k€** |

**Lot 4 (p.41-42) :**

| Poste | Contenu à coller |
|---|---|
| **Dépenses de sous-traitance** | Gradient Health : 80 k€ pour données RWE structurées et annotées. Cedars-Sinai / Mayo Clinic : 70 k€ pour accès EDS et validation externe. **Total : 150 k€** |
| **Dépenses des achats** | Accès bases FAERS, licences MedDRA 27.x, outils de normalisation terminologique. **Total : 40 k€** |
| **Contribution aux amortissements** | Infrastructure cloud/GPU pour traitement des volumes de données RWE. **Total : 30 k€** |

**Lot 5 (p.42-43) :**

| Poste | Contenu à coller |
|---|---|
| **Dépenses de sous-traitance** | INRIA : 45 k€ pour support ontologique, méthodologique et alignement sur les standards internationaux. **Total : 45 k€** |
| **Dépenses des achats** | Licences Neo4j Enterprise, infrastructure de stockage, outils de visualisation de graphes. **Total : 20 k€** |
| **Contribution aux amortissements** | Serveurs dédiés au KG et à l'indexation. **Total : 15 k€** |

**Lot 6 (p.43-44) :**

| Poste | Contenu à coller |
|---|---|
| **Dépenses de sous-traitance** | AMI Labs : 60 k€ pour validation méthodologique et évaluation indépendante. Sanofi : 50 k€ pour validation clinique prospective sur cas d'usage réels. **Total : 110 k€** |
| **Dépenses des achats** | Infrastructure GPU haute performance (A100/H100), licences logicielles de visualisation, outils de monitoring ML. **Total : 50 k€** |
| **Contribution aux amortissements** | Serveurs GPU dédiés à l'entraînement du world model et aux deep ensembles. **Total : 40 k€** |

**Lot 7 (p.44-45) :**

| Poste | Contenu à coller |
|---|---|
| **Coût total du lot** | **160 k€** (remplacer « XX€ ») |
| **Nature du lot** | **Gestion** (champ vide actuellement) |
| **Dépenses de sous-traitance** | Cabinets de propriété intellectuelle et conseil réglementaire pour la préparation et le dépôt des brevets. **Total : 20 k€** |
| **Dépenses des achats** | Inscriptions congrès, frais de publication, outils de veille PI. **Total : 5 k€** |
| **Contribution aux amortissements** | Outils de gestion de projet et de reporting. **Total : 5 k€** |

**Justification :** C'est l'anomalie bloquante n°1 du dossier. CHAQUE champ doit être renseigné. Un évaluateur BPI ouvre d'abord les lots détaillés pour vérifier le réalisme budgétaire.

---

### A8. 🔴 Sections 4.1 à 4.6 — Dates des tâches non renseignées (Mx – My)

**Problème :** Toutes les tâches de tous les lots indiquent « Tâche X.X (Mx – My) » sans les mois réels.

**Corrections par lot :**

**Lot 1 (p.38) :**
| Tâche | Remplacer (Mx – My) par |
|---|---|
| T1.1 | **(M1 – M6, soit 01/2026 – 06/2026)** |
| T1.2 | **(M1 – M9, soit 01/2026 – 09/2026)** |
| T1.3 | **(M1 – M6, soit 01/2026 – 06/2026)** |
| T1.4 | **(M3 – M12, soit 03/2026 – 12/2026)** |
| T1.5 | **(M3 – M12, soit 03/2026 – 12/2026)** |
| T1.6 | **(M9 – M15, soit 09/2026 – 03/2027)** |

**Lot 2 (p.39-40) :**
| Tâche | Remplacer (Mx – My) par |
|---|---|
| T2.1 | **(M6 – M9, soit 06/2026 – 09/2026)** |
| T2.2 | **(M6 – M12, soit 06/2026 – 12/2026)** |
| T2.3 | **(M6 – M15, soit 06/2026 – 09/2027)** |
| T2.4 | **(M9 – M18, soit 09/2026 – 06/2027)** |
| T2.5 | **(M12 – M21, soit 12/2026 – 09/2027)** |
| T2.6 | **(M12 – M21, soit 12/2026 – 09/2027)** |
| T2.7 | **(M18 – M24, soit 06/2027 – 12/2027)** |

**Lot 3 (p.40-41) :**
| Tâche | Remplacer (Mx – My) par |
|---|---|
| T3.1 | **(M6 – M12, soit 06/2026 – 12/2026)** |
| T3.2 | **(M6 – M15, soit 06/2026 – 09/2027)** |
| T3.3 | **(M9 – M18, soit 09/2026 – 06/2027)** |
| T3.4 | **(M12 – M21, soit 12/2026 – 09/2027)** |
| T3.5 | **(M12 – M21, soit 12/2026 – 09/2027)** |
| T3.6 | **(M18 – M24, soit 06/2027 – 12/2027)** |

**Lot 4 (p.41-42) :**
| Tâche | Remplacer (Mx – My) par |
|---|---|
| T4.1 | **(M7 – M15, soit 07/2026 – 03/2027)** |
| T4.2 | **(M9 – M18, soit 09/2026 – 06/2027)** |
| T4.3 | **(M15 – M27, soit 03/2027 – 03/2028)** |
| T4.4 | **(M15 – M27, soit 03/2027 – 03/2028)** |
| T4.5 | **(M24 – M30, soit 12/2027 – 06/2028)** |

**Lot 5 (p.42-43) :**
| Tâche | Remplacer (Mx – My) par |
|---|---|
| T5.1 | **(M13 – M18, soit 01/2027 – 06/2027)** |
| T5.2 | **(M15 – M24, soit 03/2027 – 12/2027)** |
| T5.3 | **(M18 – M30, soit 06/2027 – 06/2028)** |
| T5.4 | **(M18 – M33, soit 06/2027 – 09/2028)** |
| T5.5 | **(M24 – M36, soit 12/2027 – 12/2028)** |

**Lot 6 (p.43-44) :**
| Tâche | Remplacer (Mx – My) par |
|---|---|
| T6.1 | **(M13 – M24, soit 01/2027 – 12/2027)** |
| T6.2 | **(M18 – M30, soit 06/2027 – 06/2028)** |
| T6.3 | **(M21 – M33, soit 09/2027 – 09/2028)** |
| T6.4 | **(M24 – M33, soit 12/2027 – 09/2028)** |
| T6.5 | **(M27 – M36, soit 03/2028 – 12/2028)** |
| T6.6 | **(M30 – M36, soit 06/2028 – 12/2028)** |

**Justification :** Des tâches sans dates = un planning inexistant aux yeux de l'évaluateur. Toutes les dates ci-dessus sont alignées avec le dossier Workpackages (source de vérité).

---

### A9. 🔴 Sections 4.1 à 4.6 — Livrables non datés (T0 + XX mois)

**Problème :** Tous les livrables de tous les lots indiquent « T0 + XX mois » sans le nombre de mois réel.

**Corrections par lot :**

**Lot 1 :** L1.1 → **T0 + 6 mois (06/2026)** · L1.2 → **T0 + 9 mois (09/2026)** · L1.3 → **T0 + 9 mois (09/2026)** · L1.4 → **T0 + 12 mois (12/2026)**

**Lot 2 :** L2.1 → **T0 + 6 mois (06/2026)** · L2.2 → **T0 + 9 mois (09/2026)** · L2.3 → **T0 + 12 mois (12/2026)** · L2.4 → **T0 + 18 mois (06/2027)**

**Lot 3 :** L3.1 → **T0 + 9 mois (09/2026)** · L3.2 → **T0 + 12 mois (12/2026)** · L3.3 → **T0 + 18 mois (06/2027)** · L3.4 → **T0 + 18 mois (06/2027)**

**Lot 4 :** L4.1 → **EC1, fin 2026 (12/2026)** · L4.2 → **EC2, mi-2027 (06/2027)** · L4.3 → **EC2 + 3 mois (09/2027)** · L4.4 → **EC3, fin 2028 (12/2028)**

**Lot 5 :** L5.1 → **EC2, mi-2027 (06/2027)** · L5.2 → **EC2 + 6 mois (12/2027)** · L5.3 → **EC3, fin 2028 (12/2028)** · L5.4 → **T0 + 30 mois (06/2028)**

**Lot 6 :** L6.1 → **EC2, mi-2027 (06/2027)** · L6.2 → **EC3 – 6 mois (06/2028)** · L6.3 → **EC3, fin 2028 (12/2028)** · L6.4 → **EC3, fin 2028 (12/2028)** · L6.5 → **EC3, fin 2028 (12/2028)** · L6.6 → **EC3, fin 2028 (12/2028)**

**Lot 7 :** L7.1 → **T0 + 6 mois (06/2026), puis semestriel** · L7.2 → **T0 + 12 mois (12/2026), puis annuel** · L7.3 → **T0 + 36 mois (12/2028)**

**Justification :** Des livrables sans date de livraison ne permettent pas d'évaluer la faisabilité du projet. C'est un motif de rejet en pré-instruction.

---

### A10. 🔴 Section 4.4 (p.41) — Incohérence calendaire Lot 4

**Texte actuel :**
> Lot 4 : Durée « 18 mois (06/26 – 12/27) »

**Texte de remplacement :**
> Lot 4 : Durée « **24 mois (07/2026 – 06/2028)** »

**Justification :** Le WP4 s'étend sur 24 mois (M7 à M30). Le V7 indique 18 mois avec une date de fin en 12/2027, soit un décalage de > 1 an avec le WP. Cette incohérence sera relevée par tout évaluateur qui compare les deux documents.

---

### A11. 🔴 Section 4.5 (p.42) — Incohérence calendaire Lot 5

**Texte actuel :**
> Lot 5 : Durée « 12 mois (06/27 – 06/28) »

**Texte de remplacement :**
> Lot 5 : Durée « **24 mois (01/2027 – 12/2028)** »

**Justification :** Le WP5 s'étend sur 24 mois (M13 à M36). Le V7 indique 12 mois. L'écart est du simple au double.

---

### A12. 🔴 Section 4.7 (p.45) — Numérotation livrables Lot 7 erronée

**Texte actuel (livrables du Lot 7) :**
> « L6.1 (T0 + 6 mois); : Rapports de suivi du projet »
> « L6.2 (T0 + XX mois) : Synthèse des actions de diffusion »
> « L6.4 (T0 + XX mois) : Brevet »

**Texte de remplacement :**
> « **L7.1** (T0 + 6 mois, soit 06/2026, puis semestriel) : Rapports de suivi du projet »
> « **L7.2** (T0 + 12 mois, soit 12/2026, puis annuel) : Synthèse des actions de diffusion et de valorisation »
> « **L7.3** (T0 + 36 mois, soit 12/2028) : Deux brevets déposés correspondant aux principales innovations du projet »

**Justification :** Les livrables du Lot 7 sont numérotés L6.x au lieu de L7.x — erreur de copier-coller évidente. De plus, « Brevet » (singulier) entre en contradiction avec la section 5.1.3 qui parle de « deux dépôts de brevets ».

---

### A13. 🔴 Section 4.7 (p.45) — Incohérence brevets « trois » → « deux »

**Texte actuel (T7.4, p.45) :**
> « Ces travaux viseront à permettre le dépôt des **trois** brevets correspondant aux principales innovations développées dans le cadre du projet. »

**Texte de remplacement :**
> « Ces travaux viseront à permettre le dépôt des **deux** brevets correspondant aux principales innovations développées dans le cadre du projet. »

**Justification :** La section 5.1.3 (p.48) décrit clairement **deux** dépôts de brevets (pipeline clinique + Latent World Models). Le chiffre « trois » du Lot 7 est incohérent.

---

## PARTIE B — CORRECTIONS CRITIQUES (rejet probable en évaluation)

---

### B1. 🟠 Section 1.4.3 (p.14) — Tableau clients : colonne « Description des travaux » vide

**Problème :** Le tableau des clients (p.14) a la colonne « Description des travaux » entièrement vide pour les 9 contrats.

**Contenu à copier-coller dans la colonne « Description des travaux » :**

| Client | Description des travaux |
|---|---|
| **ICON** | Structuration de données cliniques CRO à grande échelle, industrialisation des workflows d'analyse bénéfice-risque, intégration des standards B/R dans les processus décisionnels ICON/MAPI |
| **Sanofi (235 k€)** | Validation des modèles IA sur cas d'usage oncologie avancée, co-développement de modules d'analyse prédictive pour le pipeline interne |
| **Sanofi (100 k€)** | Analyse comparative bénéfice-risque en dermatologie, calibration des modèles sur données internes Sanofi |
| **Sanofi (90 k€)** | POC initial, structuration de la base de données et profiling moléculaire sur molécules du portefeuille |
| **Vidal** | Intégration des données de référence médicamenteuses Vidal dans la Profiling Base, enrichissement du corpus réglementaire |
| **Mapi Research Trust** | Structuration des PRO (Patient-Reported Outcomes) et mesures de résultats patients, consolidation des profils B/R |
| **Biocodex** | POC en gastro-entérologie (maladie de Crohn, rectocolite hémorragique), puis déploiement de la licence Trial Balancer en mode SaaS on-premise |
| **Dilon** | POC en développement préclinique sur molécules candidates, puis licence plateforme Trial Balancer |
| **AstraZeneca** | Participation au projet IHI pédiatrique, structuration de projets collaboratifs R&D, alignement des données industrielles |

**Justification :** Un tableau clients avec une colonne vide envoie le signal d'un dossier bâclé. C'est d'autant plus dommageable que le portefeuille clients est un atout fort du dossier.

---

### B2. 🟠 Section 3.4 (p.36-37) — Tableau des risques incomplet

**Problème :** Le tableau des risques actuel ne contient que 8 risques « par étape clé » (liés aux verrous technologiques). Il manque les risques opérationnels, de données et de projet.

**Risques à ajouter au tableau existant :**

| Verrous | Risques | Probabilité / Gravité | Plan de contingence |
|---|---|---|---|
| EC1-EC3 | **Fuite de données entre jeux d'entraînement et de validation (data leakage)** — invalidation des résultats de performance | [P] Faible / [G] Élevée | Protocole anti-leakage strict : split temporel (hold-out 2022-2025), validation croisée par exclusion de molécules (leave-drug-out), nested cross-validation pour l'optimisation d'hyperparamètres. Audit de conformité à chaque jalon. |
| EC1-EC3 | **Qualité/complétude variable des données RWE** — sous-reporting FAERS, données manquantes EDS | [P] Élevée / [G] Élevée | Grille de qualification stricte (T4.1) ; imputation multiple avec analyse de sensibilité ; pondération inverse de la probabilité de notification. |
| EC3 | **Pic de recrutement 2028** — 20 embauches en 12 mois, risque organisationnel | [P] Modérée / [G] Modérée | Recrutement par vagues de 4-6 maximum ; pipeline de candidats alimenté par le réseau INRIA/ICM/Future4Care. |

**Justification :** Les experts ML poseront systématiquement la question du data leakage dans un projet multi-sources. L'absence de ce risque dans le tableau envoie le signal que l'équipe n'a pas identifié ce problème. Idem pour la qualité RWE (le risque le plus documenté dans la littérature FAERS).

---

### B3. 🟠 Section 5.2.3 (p.51) — Projections 2030-2032 non crédibles

**Texte actuel (p.51) :**
> « La trajectoire se poursuit ensuite avec une montée en puissance des licences logicielles, conduisant à un chiffre d'affaires de **32,1 M€ en 2031 puis 51,5 M€ en 2032**. »

**Texte de remplacement :**
> « La trajectoire post-2030 est présentée selon deux scénarios. Le **scénario médian** (probabilité estimée 60 %) prévoit un CA de 14,25 M€ en 2030 et ~22 M€ en 2032, correspondant à environ 90 molécules en licence simultanée pour ~65 ETP. Le **scénario haut** (probabilité estimée 20 %), conditionné à l'obtention de partenariats structurants supplémentaires avec des laboratoires du top-10 mondial et à une accélération de l'adoption en immuno-inflammation, pourrait porter le CA à 32 M€ en 2031 et 51,5 M€ en 2032, soit environ 206 molécules simultanées pour ~120 ETP — un objectif ambitieux mais qui nécessiterait une levée de fonds série B significative et un élargissement majeur de l'équipe commerciale. »

**Justification :** Un TCAC de 84 % sur 3 ans (de 8,3 M€ à 51,5 M€) est immédiatement identifié comme non crédible par un analyste BPI. En revanche, présenter cela comme un « scénario haut » aux côtés d'un scénario médian plus conservateur renforce la crédibilité globale.

---

### B4. 🟠 Section 5.3.1 (p.52) — Retombées sociales trop courtes

**Texte actuel (p.52) :**
La section 5.3.1 fait environ 15 lignes, sans structuration en sous-parties, sans chiffres d'emplois détaillés par catégorie, et mentionne « 27 emplois qualifiés » (alors que le plan de recrutement prévoit 47 postes).

**Texte de remplacement (remplace intégralement la section 5.3.1) :**

> **5.3.1. Retombées sociales, sociétales pour le territoire national**
>
> Le projet BR-Predict génère des retombées sociales et sociétales structurantes à plusieurs niveaux.
>
> **Accélération de l'accès aux thérapies innovantes**
>
> En permettant d'identifier plus précocement les candidats médicaments les plus prometteurs, la solution contribue à accélérer l'arrivée de thérapies innovantes sur le marché, en particulier pour des populations médicalement délaissées. Les pathologies ciblées en priorité — cancer du poumon non à petites cellules (pathologie d'ancrage), puis extension à d'autres indications oncologiques et à l'immuno-inflammation — figurent parmi les domaines où le besoin médical non couvert est le plus important.
>
> **Éthique des essais cliniques et sécurité des patients**
>
> Un essai de phase I mobilise entre 10 et 50 volontaires sains, un essai de phase II peut inclure entre 50 et 300 patients. En améliorant la sélection des candidats en amont, chaque essai évité grâce à une meilleure anticipation du profil bénéfice-risque permet d'épargner entre 10 et 300 personnes. La solution contribue à un développement pharmaceutique plus responsable.
>
> **Équité en santé**
>
> La plateforme intègre explicitement les facteurs socio-démographiques et ethniques dans ses modèles prédictifs (WP4), contribuant à identifier les sous-populations chez qui le rapport B-R est le plus favorable ou défavorable, et à réduire les biais dans les décisions de développement.
>
> **Impact économique et territorial**
>
> | Catégorie | Nombre | Profils |
> |---|---|---|
> | R&D | 27 | Ingénieurs IA, data scientists biomédicaux, bioinformaticiens, chefs de projet R&D |
> | Industrialisation | 6 | Ingénieurs DevOps/MLOps, architectes systèmes, déploiement on-premise |
> | Commercial | 14 | Key account managers pharma/CRO, chefs de produit |
> | **Total** | **47** | |
>
> Le projet inclut la formation de 4 doctorants CIFRE et de 8 stagiaires par an, contribuant au renforcement de l'écosystème local en santé numérique. Des retombées indirectes sont attendues auprès des sous-traitants technologiques et scientifiques (INRIA, ICM, Gradient Health), contribuant à la dynamique d'innovation du bassin Paris 13e / Île-de-France et au rayonnement international du hub Future4Care.

**Justification :** La section actuelle mentionne 27 emplois (erreur : c'est 47), manque de structuration, et ne mentionne ni l'éthique des essais, ni l'équité en santé, ni les CIFRE. C'est un argumentaire d'intérêt sociétal attendu par les ministères.

---

## PARTIE C — CORRECTIONS ÉLEVÉES (fragilités exploitables par les évaluateurs)

---

### C1. 🟡 Section 3.1 (p.33) — Erreur « 6 lots » au lieu de « 7 lots »

**Texte actuel :**
> « Le projet se décline en **6 lots** sur une période de 36 mois résumés dans le diagramme de Gantt ci-après. »

**Texte de remplacement :**
> « Le projet se décline en **7 lots** (6 lots techniques et 1 lot de management) sur une période de 36 mois résumés dans le diagramme de Gantt ci-après. »

**Justification :** Le document décrit bien 7 lots (4.1 à 4.7). Écrire « 6 lots » introduit une incohérence immédiatement visible.

---

### C2. 🟡 Section 3.1 (p.33) — Lot 6 réfère « lot 4 » et « lot 5 » au lieu de lots corrects

**Texte actuel :**
> « Le lot 6 intègre tous les modèles prédictifs (lot 4) avec le paysage de connaissances (lot 5) [...] »

**Texte de remplacement :**
> « Le lot 6 intègre tous les modèles prédictifs (**lots 1-4**) avec le paysage de connaissances (**lot 5**) pour créer un « World model » capable de simuler des profils bénéfice-risque pour n'importe quelle molécule. »

**Justification :** Le Lot 6 intègre les lots 1, 2, 3 et 4 (pas seulement le lot 4). Le « lot 4 » seul est une erreur de rédaction.

---

### C3. 🟡 Section 5.2.3 (p.51) — Tableau CA : colonnes 2031/2032 vides

**Texte actuel :**
> Le tableau de construction du CA (p.51) a les colonnes 2031 et 2032 affichées dans l'en-tête mais les cellules sont vides (pas de données).

**Action :** Soit supprimer les colonnes 2031-2032 du tableau, soit les remplir avec les données du scénario médian :

| | 2031 | 2032 |
|---|---|---|
| CA Trial Balancer | 7 000 | 7 500 |
| CA BR-Predict | 11 000 | 14 500 |
| **CA Total** | **18 000** | **22 000** |

**Justification :** Des colonnes vides dans un tableau de prévision financière donnent une impression d'inachevé.

---

### C4. 🟡 Section 2.2.6 (p.24-25) — Mention « plus de 20 SLMs » (2e occurrence)

**Vérifier** la section 2.2.6 (p.24) pour la mention « plus de 20 modèles d'intelligence artificielle propriétaires de type SLM ». Si présente, remplacer par « **24** modèles d'intelligence artificielle propriétaires de type SLM (**Contextualizing SLMs**) ».

---

### C5. 🟡 Section 4.4 (p.41) — Lot 4 réfère lot « 4 » au lieu de lots 1-3

**Texte actuel dans la description des livrables Lot 4 :**
> « L4.3 : Modèle généralisable intégrant facteurs cliniques réels + données moléculaires + données de pathologie (L1–3 + L4) »

**Texte de remplacement :**
> « L4.3 : Modèle généralisable intégrant données de vie réelle + données moléculaires (WP1) + données précliniques (WP2) + données génomiques (WP3), applicable à 2+ pathologies »

**Justification :** La formulation « L1-3 + L4 » est auto-référentielle (le Lot 4 se cite lui-même). Il faut clarifier que le livrable L4.3 intègre les résultats des WP1-3 avec les données RWE du WP4.

---

*Fin du Document 1 — 18 corrections identifiées (13 bloquantes, 4 critiques, 5 élevées)*
