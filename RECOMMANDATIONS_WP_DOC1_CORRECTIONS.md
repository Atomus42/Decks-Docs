# DOCUMENT 1 — CORRECTIONS & RENFORCEMENTS RÉDACTIONNELS DU DOSSIER WORKPACKAGES

## Mode d'emploi

Ce document contient des recommandations **prêtes à copier-coller** pour corriger les fragilités identifiées dans le dossier Workpackages (I-demo_Workpackages_dossier.pdf, 29 pages). Chaque recommandation indique :
- **Section / WP** : où intervenir
- **Texte actuel** : ce qui existe (citation exacte ou description)
- **Texte de remplacement** : à copier-coller directement
- **Justification** : pourquoi cette correction est nécessaire

**Priorité** : BLOQUANT (irrecevabilité ou incohérence avec le V7) · CRITIQUE (rejet probable en évaluation) · ÉLEVÉ (fragilité exploitable par les évaluateurs)

---

## PARTIE A — CORRECTIONS BLOQUANTES (incohérences V7 ↔ WP et erreurs structurelles)

---

### A1. BLOQUANT — WP1 (p.4) — Seuil AUC EC1 : harmoniser avec le V7

**Texte actuel (WP1, KPI & protocole d'évaluation) :**
> « L'objectif cible est une AUC > 0,75 sur le jeu de validation externe »

**Problème :** Ce seuil est correct et c'est la valeur de référence vers laquelle le V7 doit converger. Cependant, le V7 oscille entre 0,6 / 0,65 / 0,75 pour EC1. Le WP doit explicitement mentionner qu'il s'agit du seuil harmonisé pour EC1 afin de servir de point d'ancrage indiscutable.

**Texte de remplacement :**
> « L'objectif cible est une **AUC > 0,75** sur le jeu de validation externe, seuil cohérent avec l'état de l'art QSAR sur des espaces chimiques diversifiés. **Ce seuil constitue le critère de succès harmonisé pour l'ensemble du jalon EC1** (T0 + 15 mois), applicable à tous les modèles QSAR du WP1. La précision est mesurée par AUC-ROC pour les modèles de classification et par R²/RMSE pour les modèles de régression. »

**Justification :** Les évaluateurs compareront les seuils entre V7 et WP. Rendre le WP explicitement normatif (« seuil harmonisé pour l'ensemble du jalon EC1 ») renforce la cohérence documentaire et ancre la valeur 0,75.

---

### A2. BLOQUANT — WP2 (p.8) — Incohérence calendaire avec le V7

**Texte actuel (WP2, Tâches & articulation) :**
> « Le calendrier s'étend de Q2 2026 à Q4 2027, avec une phase d'infrastructure commune en 21 2026. »

**Problèmes :**
1. « 21 2026 » est une coquille — probablement « S1 2026 » ou « H1 2026 »
2. Le V7 Lot 2 indique une fin en 12/2027, ce qui est cohérent avec Q4 2027
3. Mais le V7 indique un démarrage en 06/2026 (M6), tandis que le WP dit Q2 2026 (avril) — décalage de 2 mois

**Texte de remplacement :**
> « Le calendrier s'étend de **M6 (juin 2026) à M24 (décembre 2027)**, soit 18 mois, avec une phase d'infrastructure commune (T2.1) déployée dès **Q2 2026 (M4-M6)** en amont du démarrage opérationnel du WP2. »

**Justification :** La coquille « 21 2026 » est une erreur de frappe qui nuit à la crédibilité. Le recalage calendaire M6-M24 aligne le WP avec le V7 corrigé.

---

### A3. BLOQUANT — WP4 (p.16) — Incohérence calendaire majeure avec le V7

**Texte actuel (WP4, en-tête implicite) :**
Le WP4 ne mentionne pas explicitement sa période dans l'en-tête, mais les tâches et livrables indiquent un démarrage EC1 (fin 2026) et une fin EC3 (fin 2028).

**Problème :** Le V7 Lot 4 indique « Durée 18 mois (06/26 – 12/27) » — en totale contradiction avec le WP4 qui s'étend sur ~24 mois (M7 à M30). Le Doc 1 V7 corrige cette durée à « 24 mois (07/2026 – 06/2028) ». Le WP doit être explicite sur cette période.

**Action :** Ajouter en en-tête du WP4 (comme pour WP3 qui a « Période : Q2 2026 - Q4 2027 ») :

**Texte à ajouter :**
> **Partenaires** : Cedars-Sinai, Mayo Clinic, Institut du Cerveau (ICM), Gradient Health
> **Période** : Q3 2026 – Q2 2028 (M7 – M30) | **Jalons** : EC1 (fin 2026, pipeline opérationnel), EC2 (mi-2027, modèles RWE validés), EC3 (fin 2028, documentation complète)

**Justification :** L'absence d'en-tête calendaire explicite pour le WP4 est une omission structurelle qui rend la comparaison avec le V7 impossible. Le WP4 est identifié comme « le plus risqué » dans l'audit — il faut que son cadrage temporel soit irréprochable.

---

### A4. BLOQUANT — WP4 (p.15-16) — Livrables L4.1 à L4.4 : dates incohérentes avec V7

**Texte actuel (WP4, Livrables & Jalons) :**
> - L4.1 (EC1, fin 2026)
> - L4.2 (EC2, mi-2027)
> - L4.3 (EC2+3 mois)
> - L4.4 (EC3, fin 2028)

**Problème :** Le V7 corrigé indique les dates suivantes pour le Lot 4 : L4.1 → EC1 fin 2026, L4.2 → EC2 mi-2027, L4.3 → EC2+3 mois (09/2027), L4.4 → EC3 fin 2028. Ces dates sont cohérentes, mais le V7 non corrigé indiquait « T0+XX mois ». Pour garantir l'alignement, le WP doit utiliser les mêmes mois absolus.

**Texte de remplacement :**
> - **L4.1** (EC1, **M12 = décembre 2026**) : Pipeline d'extraction/structuration opérationnel ; grille de qualification appliquée à FAERS et à 2 EDS partenaires, avec résultats documentés sur la couverture, la complétude et les biais de chaque source.
> - **L4.2** (EC2, **M18 = juin 2027**) : Modèles prédictifs RWE B-R pour le cancer du poumon, rapport de calibration externe.
> - **L4.3** (EC2+3 mois, **M21 = septembre 2027**) : Modèle généralisable intégrant données RWE + données moléculaires (WP1) + données précliniques (WP2) + données génomiques (WP3), applicable à 2+ pathologies.
> - **L4.4** (EC3, **M36 = décembre 2028**) : Documentation complète du pipeline, code reproductible, rapport de validation multi-pathologies.

**Justification :** Les mois absolus (M12, M18, M21, M36) permettent aux évaluateurs de vérifier instantanément l'alignement V7 ↔ WP sans calcul mental. L'ajout de descriptions enrichies pour chaque livrable renforce la traçabilité.

---

### A5. BLOQUANT — WP6 (p.23) — Incohérence « 100 milliards » vs « 100 milliards de relations »

**Texte actuel (WP6, Méthodologie technique, T6.1) :**
> « Le WP6 revendique un pré-entraînement sur 100 milliards de relations. Le WP5 cible ~1 million de relations en fin de projet. Ces chiffres sont incohérents d'un facteur ~100 000. »

**Le document le dit lui-même :**
> « Ces chiffres sont incohérents d'un facteur ~100 000. Le document doit clarifier ce qui est réellement utilisé pour le pré-entraînement. »

**Problème :** Le WP6 reconnaît explicitement cette incohérence mais ne la résout pas. Les « 100 milliards » font référence aux points de données de la Profiling Base (traitée par les 24 SLMs), et non aux relations du KG WP5. Le WP doit clarifier cette distinction.

**Texte de remplacement (remplacer le passage ambigu dans T6.1) :**
> Le WP6 s'appuie sur deux couches de données distinctes :
>
> 1. **Couche de pré-entraînement (Profiling Base)** : les 24 Contextualizing SLMs sont pré-entraînés sur la Profiling Base d'ArcaScience, qui contient **100 milliards de points de données/relations** issus de corpus réglementaires, de la littérature biomédicale et de bases de données spécialisées. Cette couche fournit les embeddings textuels (z_drug, z_pat) qui alimentent l'espace latent du world model. **Ce pré-entraînement est un actif existant**, largement réalisé avant le démarrage du projet i-Démo.
>
> 2. **Couche de raisonnement structuré (KG WP5)** : le Knowledge Graph construit dans le cadre du WP5 cible **> 100 000 entités et > 1 million de relations** au stade EC3. C'est sur cette couche que le SCM (Structural Causal Model) du WP6 opère pour le raisonnement causal et contrefactuel. Le projet i-Démo finance la construction de cette couche et la couche d'intégration WP6, pas le pré-entraînement des SLMs.
>
> **L'articulation est donc la suivante** : les SLMs (pré-entraînés sur 100 Mds de points) fournissent les représentations latentes ; le KG (1 M de relations) fournit la topologie causale ; le world model WP6 fusionne ces deux sources dans un espace latent multimodal.

**Justification :** L'incohérence d'un facteur 100 000 est actuellement auto-identifiée dans le WP mais non résolue. Un évaluateur qui lit « 100 milliards » puis « 1 million » dans le même document conclura soit à une erreur, soit à une exagération. Cette clarification est indispensable.

---

### A6. BLOQUANT — WP6 (p.23-24) — Nombre de molécules pour le deep ensemble (200-800)

**Texte actuel (WP6, T6.1) :**
> « Le nombre de molécules disposant simultanément de données dans les quatre WPs est estimé à 200-800 (molécules approuvées avec données structurales, précliniques, pharmacogénomiques et post-AMM documentées), volume suffisant pour calibrer le module d'intégration de second niveau, mais insuffisant pour entraîner un espace latent partagé profond. »

**Problème :** Le chiffre 200-800 est honnête mais dangereux sans contextualisation. Les évaluateurs calculeront : 200 molécules × 4 WPs = 200 vecteurs d'entraînement pour un modèle multimodal. C'est très faible pour un deep ensemble. Le WP doit expliquer pourquoi c'est suffisant.

**Texte de remplacement (enrichir le passage) :**
> Le nombre de molécules disposant simultanément de données dans les quatre WPs est estimé à **200-800** (molécules approuvées avec données structurales, précliniques, pharmacogénomiques et post-AMM documentées). Ce volume est **suffisant pour calibrer le module d'intégration de second niveau** (stacking), car :
>
> - Le stacking opère sur les **prédictions** (scores + intervalles de confiance) des WP1-4 comme features, soit un espace de dimension réduite (~20-40 features par molécule), pour lequel 200-800 exemples suffisent amplement (règle empirique : ≥ 10 exemples par feature) ;
> - L'architecture est conçue pour traiter l'absence de modalités comme le cas par défaut : chaque module WP fonctionne de façon dégradée mais robuste en l'absence de données d'un WP donné ;
> - Les **200 molécules constituent le socle minimal** (molécules avec données complètes dans les 4 WPs), tandis que les modèles individuels de chaque WP sont entraînés sur des volumes bien supérieurs (WP1 : ~4 500 molécules, WP2 : 5 000-8 000, WP3 : 150-300 associations, WP4 : cohortes FAERS).
>
> En revanche, ce volume est **insuffisant pour entraîner un espace latent partagé profond** de type auto-encodeur multimodal. L'architecture retenue traite donc explicitement les modalités manquantes via des embeddings de remplacement et des masques d'attention, garantissant des prédictions robustes y compris pour les molécules en développement précoce ne disposant que de données structurales.

**Justification :** Le chiffre 200-800 sera le premier chiffre attaqué par les experts ML. L'explication « le stacking opère sur ~20-40 features → 200 exemples suffisent » est un argument technique solide qui anticipe l'objection.

---

### A7. BLOQUANT — WP1 (p.5) — Coquille typographique dans T1.4

**Texte actuel (WP1, T1.4) :**
> « Les modèles sont entraînés sur l'ensemble deses données d'activité sur l'ensemble des cibles pertinentes en oncologie pulmonaire (EGFR, ALK, KRAS, PD-L1, etc.). »

**Texte de remplacement :**
> « Les modèles sont entraînés sur l'ensemble **des** données d'activité sur les cibles pertinentes en oncologie pulmonaire (EGFR, ALK, KRAS, PD-L1, etc.). »

**Justification :** Coquille de fusion « deses données [...] sur l'ensemble des ». Petite erreur mais visible pour un relecteur attentif.

---

### A8. BLOQUANT — WP1 (p.5) — Phrase tronquée T1.4

**Texte actuel (WP1, T1.4) :**
> « Ces 8 à 10 prédictions sont ensuite agrégées en un score de bénéfice composite.Les modèles sont entraînés sur l'ensemble deses données d'activité [...] »

**Texte de remplacement :**
> « Ces 8 à 10 prédictions sont ensuite agrégées en un score de bénéfice composite. Les modèles sont entraînés sur l'ensemble des données d'activité [...] »

**Justification :** Deux phrases fusionnées sans espace (« composite.Les »). Corrobore l'impression d'un document n'ayant pas fait l'objet d'une relecture finale.

---

## PARTIE B — CORRECTIONS CRITIQUES (rejet probable en évaluation)

---

### B1. CRITIQUE — WP4 (p.14-15) — Absence de protocole anti-data leakage explicite

**Texte actuel (WP4, KPI & protocole d'évaluation) :**
> « Protocole : validation croisée par exclusion de molécules (leave-drug-out) pour prévenir les fuites de données entre sources, complétée par une validation externe sur une cohorte temporellement disjointe (hold-out 2022-2025). »

**Problème :** Le WP4 mentionne le leave-drug-out et le hold-out temporel — c'est un bon début — mais le protocole est insuffisamment formalisé. Il manque :
1. L'isolation explicite des données entre WPs (une même molécule dans le jeu de test WP1 ne doit pas être dans le jeu d'entraînement WP4)
2. La nested cross-validation pour l'optimisation d'hyperparamètres
3. Le registre central de molécules réservées

**Texte de remplacement (remplacer le point « Protocole ») :**
> **Protocole de validation anti-leakage :**
>
> 1. **Split temporel strict** : les données postérieures à 2022 sont réservées exclusivement au jeu de validation (hold-out 2022-2025). Les modèles sont entraînés uniquement sur des données antérieures à 2022.
> 2. **Leave-drug-out** : chaque fold de validation croisée exclut l'ensemble des données d'une molécule donnée (toutes sources WP1-4 confondues) pour éviter que des informations sur la même molécule ne figurent dans l'entraînement et le test.
> 3. **Nested cross-validation** : l'optimisation des hyperparamètres est réalisée dans une boucle interne distincte de la boucle externe d'évaluation, prévenant le surapprentissage des hyperparamètres.
> 4. **Registre central de molécules réservées** : un registre partagé entre les WPs garantit qu'une molécule réservée pour le test dans un WP n'est pas utilisée en entraînement dans un autre WP. Ce registre est maintenu par le chef de projet et audité à chaque jalon.
> 5. **Audit de conformité** : à chaque jalon (EC1, EC2, EC3), un audit vérifie l'absence de fuite d'information. Le rapport d'audit est inclus dans les livrables.

**Justification :** Le data leakage inter-WPs est le risque méthodologique n°1 d'un projet multi-sources. Les experts ML poseront cette question systématiquement. Le WP4 a une ébauche de réponse — il faut la compléter pour être irréprochable.

---

### B2. CRITIQUE — WP2 (p.6) — Couverture biothérapies incohérente avec WP1

**Texte actuel (WP2, Cadre scientifique & périmètre) :**
> « Le périmètre couvre les petites molécules et les biothérapies, ces derniers faisant l'objet d'un traitement spécifique compte tenu des limites connues de transposabilité (immunogénicité, modèles substitutifs). »

**Problème :** Le WP1 exclut explicitement les biothérapies (« Les biothérapies ou "biologics" [...] sont explicitement hors champ pour ce lot »). Le WP2 dit les couvrir. Il faut clarifier le périmètre exact.

**Texte de remplacement :**
> « Le périmètre principal couvre les **petites molécules**, en cohérence avec le WP1. Les **biothérapies** (anticorps monoclonaux, thérapies ciblées) font l'objet d'un traitement **séparé et explicitement qualifié comme exploratoire** dans le cadre de ce lot, compte tenu des limites connues de transposabilité préclinique-clinique (immunogénicité spécifique à l'espèce, faible transposabilité des modèles substitutifs). Les résultats sur les biothérapies seront rapportés séparément avec une signalisation explicite de l'incertitude accrue. Le profil B-R complet des biothérapies relève davantage du WP3 (données génomiques, cibles thérapeutiques) et constitue une extension post-i-Démo. »

**Justification :** L'incohérence WP1 (« hors champ ») vs WP2 (« couvert ») sera immédiatement relevée. La clarification « exploratoire / rapporté séparément » est la formulation la plus honnête.

---

### B3. CRITIQUE — WP3 (p.13) — Seuil AUC « niveau de preuve 2 » trop bas (0,65)

**Texte actuel (WP3, KPI & protocole d'évaluation) :**
> « pour les associations émergentes (niveau de preuve 2), l'objectif cible est une AUC > 0,65, reflétant l'incertitude inhérente à ces associations tout en démontrant leur exploitabilité prédictive. »

**Problème :** Un seuil AUC de 0,65 est très faible — à peine mieux qu'un modèle aléatoire amélioré. Les évaluateurs techniques pourraient considérer ce seuil comme insuffisant pour justifier l'intégration dans le world model WP6.

**Texte de remplacement :**
> « pour les associations émergentes (niveau de preuve 2), l'objectif cible est une AUC > **0,70**, reflétant l'incertitude inhérente à ces associations tout en démontrant leur exploitabilité prédictive. Ce seuil est volontairement inférieur au seuil de 0,80 des associations établies, car les variants de niveau 2 présentent une taille de cohorte réduite et une hétérogénéité phénotypique plus élevée. **Un seuil de 0,65 sera néanmoins considéré comme un résultat exploratoire acceptable** si le gain incrémental par rapport aux prédictions WP1+WP2 seules est statistiquement significatif (test de DeLong, p < 0,05). »

**Justification :** Rehausser le seuil cible de 0,65 à 0,70 tout en conservant 0,65 comme seuil exploratoire montre de l'ambition technique tout en restant réaliste. Cela neutralise l'objection « votre seuil est trop bas ».

---

### B4. CRITIQUE — WP5 (p.20) — Seuil KPI-3 « contradictions non résolues < 5% » non opérationnalisé

**Texte actuel (WP5, KPI) :**
> « KPI-3 : Taux de contradictions non résolues < 5 % des relations du KG. »

**Problème :** Comment mesure-t-on une « contradiction » dans un KG ? Le KPI est énoncé mais le protocole de mesure est absent.

**Texte de remplacement :**
> **KPI-3** : Taux de contradictions non résolues < 5 % des relations du KG.
>
> *Protocole de mesure* : une contradiction est définie comme deux arêtes portant sur la même paire d'entités avec des assertions incompatibles (ex. : « molécule X inhibe cible Y » vs « molécule X n'a pas d'effet sur cible Y »). La détection est automatisée via le pipeline T5.4 (détection de contradictions), et les contradictions identifiées sont soumises à un workflow de résolution : (i) vérification de la provenance et du niveau de preuve de chaque arête, (ii) résolution par priorisation du niveau de preuve le plus élevé, (iii) annotation explicite des contradictions non résolues avec les deux versions conservées et un flag « contradiction ouverte ». L'audit trimestriel (200 relations aléatoires) vérifie que le taux de contradictions non résolues reste < 5 %.

**Justification :** Un KPI sans protocole de mesure opérationnel n'est pas évaluable. Les experts en KG demanderont « comment savez-vous qu'il y a une contradiction ? ».

---

### B5. CRITIQUE — WP6 (p.27) — Jalon EC1 pour WP6 absent

**Problème :** Le WP6 liste des livrables et des jalons (L6.1 à L6.4, jalon pathologie spécifique et jalon générique) mais ne mentionne **aucune contribution au jalon EC1** (T0+15 mois). Or les WP1-4 ont tous des livrables EC1. Le WP6 démarre au M13 — son premier livrable est L6.1 (EC2, mi-2027).

**Action :** Ajouter une clarification après la liste des livrables WP6.

**Texte à ajouter :**
> **Note sur le jalon EC1** : le WP6 ne contribue pas directement au jalon EC1 (T0+15 mois), car son démarrage opérationnel est fixé à M13 (janvier 2027). Au jalon EC1, les contributions du WP6 se limitent à : (i) la spécification de l'architecture du world model (document de conception, T6.1), (ii) les spécifications d'interface avec les WP1-4 (formats de sortie, protocoles d'échange), et (iii) le démarrage du pré-entraînement des encodeurs moléculaires sur la Profiling Base. Le premier livrable opérationnel du WP6 est L6.1 (EC2, mi-2027).

**Justification :** Un évaluateur qui cherche « que livre le WP6 à EC1 ? » ne trouvera rien. L'absence de réponse sera interprétée comme un manque de planification. Une mention explicite « pas de contribution directe + 3 activités préparatoires » neutralise l'objection.

---

### B6. CRITIQUE — WP5 (p.19) — Période manquante dans l'en-tête

**Texte actuel (WP5, en-tête, informations générales) :**
Le WP5 mentionne dans le corps du texte « Q1 2027 - Q4 2028 » et dans les jalons « EC2 (mi-2027), EC3 (fin 2028) ».

**Problème :** Le WP5 n'a pas d'en-tête structuré « Partenaires / Période / Jalons » comme le WP3. Les informations de cadrage sont dispersées.

**Texte à ajouter en en-tête du WP5 :**
> **Partenaires validation** : Sanofi, Cedars Sinai, Mayo Clinic, Institut du Cerveau (ICM), AMI Labs (en cours de cadrage) | **Partenaire données** : Gradient Health
> **Période** : Q1 2027 – Q4 2028 (M13 – M36) | **Jalons** : EC2 (mi-2027, schéma ontologique validé), EC3 (fin 2028, KG complet + API opérationnelle)

**Justification :** L'en-tête structuré avec Partenaires / Période / Jalons figure dans le WP3 mais pas dans les WP4 et WP5. Cette inconsistance de format nuit à la lisibilité. Harmoniser le format sur tous les WPs.

---

## PARTIE C — CORRECTIONS ÉLEVÉES (fragilités exploitables)

---

### C1. ÉLEVÉ — WP2 (p.7) — Coquille « T2.3 - Extraction NLP et structuration » : 24 SLMs à mentionner explicitement comme « Contextualizing SLMs »

**Texte actuel :**
> « Les Contextualizing SLMs d'ArcaScience (24 modèles spécialisés -classifieurs de phrases, modèles NER, modèles d'embedding, modules hybrides règles+modèles) [...] »

**Action :** Vérifier que toutes les mentions de « 24 SLMs » ou « 24 modèles » dans le WP sont harmonisées en « **24 Contextualizing SLMs** ». Occurrences à vérifier :
- WP2 T2.3 (p.7) : OK ✓
- WP4 T4.2 (p.16) : mentionne « Contextualizing SLMs » mais ne précise pas « 24 » → ajouter « Les **24** Contextualizing SLMs d'ArcaScience »
- WP5 T5.4 (p.20) : mentionne « Les 24 Contextualizing SLMs » → OK ✓
- WP6 T6.1 (p.23) : mentionne « 24 Contextualizing SLMs » → OK ✓

**Justification :** Le V7 oscille entre « plus de 20 SLMs » et « 24 SLMs ». Le WP doit systématiquement utiliser « 24 Contextualizing SLMs » pour servir de référence harmonisée.

---

### C2. ÉLEVÉ — WP1 (p.4-5) — Nombre de livrables WP1 : divergence avec le V7

**Texte actuel (WP1, Livrables & Jalons) :**
> - L1.1 : Base de données traitée structure-activité-toxicité (M6)
> - L1.2 : Modèles QSAR validés (M9)
> - L1.3 : Modèles QSTR validés (M9)
> - L1.4 : Score B-R composite intégré et rapport de validation (M12)
> - Jalon EC1 (fin 2026)

**Problème :** Le WP1 a 4 livrables (L1.1-L1.4). Le V7 Lot 1 a aussi 4 livrables mais les descriptions diffèrent légèrement. Plus important : le V7 corrigé ajoute un livrable L1.5 (rapport de validation anti-leakage). Si ce livrable est ajouté au V7, il faut l'ajouter aussi au WP.

**Texte à ajouter (si le livrable anti-leakage est ajouté au V7) :**
> - **L1.5** : Rapport d'audit anti-data leakage — vérification de l'absence de fuite d'information entre les jeux d'entraînement et de validation, incluant le registre des molécules réservées et les résultats de la nested cross-validation (M15, livré avec le jalon EC1).

**Justification :** Alignement préventif V7 ↔ WP. Si le V7 corrigé ajoute un livrable anti-leakage (recommandation B2 du Doc 2 V7), le WP doit le refléter.

---

### C3. ÉLEVÉ — WP2 (p.9) — Nombre de livrables WP2 : divergence avec V7

**Texte actuel (WP2, Livrables & Jalons) :**
> - L2.1 : Infrastructure commune opérationnelle (M3, partagée WP3/WP4)
> - L2.2 : Modèle NLP fonctionnel pour l'extraction de données in vivo (M9)
> - L2.3 : Score de fiabilité par modèle préclinique et par pathologie, calibré sur l'oncologie pulmonaire (M12)
> - L2.4 : Modèles ML prédictifs Bénéfits et Risks basés sur les données in vivo, validés (M18)

**Problème :** Le WP a 4 livrables (L2.1-L2.4) dont L2.1 est un livrable d'infrastructure. Le V7 Lot 2 corrigé aura également 4 livrables mais la numérotation V7 n'inclut pas l'infrastructure dans L2.1. Cette divergence de découpe peut créer de la confusion.

**Recommandation :** Ajouter une note clarificatrice :
> *Note : Le livrable L2.1 (Infrastructure commune) est une tâche mutualisée avec les WP3 et WP4. Il est comptabilisé dans le WP2 en tant que porteur de la tâche T2.1, mais son coût est réparti entre les 3 lots concernés.*

**Justification :** Un évaluateur qui compte les livrables V7 vs WP trouvera des divergences dans la numérotation. La note clarifie.

---

### C4. ÉLEVÉ — WP3 (p.12) — T3.4 : Modèle Graph Transformer — justification de l'architecture manquante

**Texte actuel (WP3, T3.4) :**
> « L'architecture repose sur un réseau à attention sur graphe (GAT ou Relational Graph Transformer) opérant directement sur le sous-graphe {molécule-cibles-biomarqueurs-pathologie}. »

**Problème :** L'hésitation « GAT ou Relational Graph Transformer » montre que le choix architectural n'est pas tranché. C'est acceptable pour un projet de recherche, mais il faut l'assumer explicitement.

**Texte de remplacement :**
> « L'architecture repose sur un réseau à attention sur graphe. Le choix entre **GAT** (Graph Attention Network, Veličković et al., 2018) et **Relational Graph Transformer** (RGT) sera arbitré lors de la phase T3.1-T3.3 en fonction de : (i) la taille effective du sous-graphe {molécule-cibles-biomarqueurs-pathologie} (GAT favorisé si < 10 000 nœuds, RGT si > 10 000), (ii) la diversité des types de relations (RGT favorisé si > 5 types distincts), et (iii) les performances comparatives sur le panel de validation WP1 EC1. Le choix sera documenté et justifié dans le livrable L3.3a (M18). »

**Justification :** Transformer l'hésitation en critère de décision documenté montre la maturité méthodologique. Un évaluateur ML préfère lire « nous choisirons en fonction de X et Y » que « nous ferons l'un ou l'autre ».

---

### C5. ÉLEVÉ — WP6 (p.25-26) — Validation sur 200 molécules : biais de survie non traité

**Texte actuel (WP6, T6.6 Validation et calibration) :**
> « Phase rétrospective : le world model est évalué sur un jeu de >= 200 molécules commercialisées ou retirées du marché, dont les profils B-R réels sont connus. Ce seuil de 200 molécules est cohérent avec les standards de validation des plateformes de prédiction B-R publiées dans la littérature. »

**Problème :** Valider sur des molécules dont on connaît l'issue = biais de survie/hindsight. C'est le standard de l'industrie, mais il faut le reconnaître et le mitiger.

**Texte de remplacement :**
> Phase rétrospective : le world model est évalué sur un jeu de >= 200 molécules commercialisées ou retirées du marché, dont les profils B-R réels sont connus. Ce seuil de 200 molécules est cohérent avec les standards de validation des plateformes de prédiction B-R publiées dans la littérature, et sera appliqué de façon homogène à chaque WP pour permettre une comparaison directe des performances entre niveaux de résolution prédictive.
>
> **Limitation connue — biais rétrospectif :** la validation sur des molécules à issue connue introduit un biais de survie (hindsight bias). Pour le mitiger : (i) le split temporel strict (données post-2022 en hold-out) simule une prédiction prospective ; (ii) les molécules retirées du marché sont surreprésentées dans le jeu de test (~40 % vs ~10 % en population réelle) pour augmenter la puissance statistique sur les vrais positifs de risque ; (iii) la **phase prospective** (monitoring chez les partenaires Sanofi, Cedars-Sinai) constituera la validation ultime en conditions réelles.

**Justification :** Le biais de survie est identifié dans l'audit comme le problème n°10. Le WP le mentionne implicitement (200 molécules commercialisées/retirées) mais ne le traite pas. Les experts scientifiques poseront cette question.

---

### C6. ÉLEVÉ — WP6 (p.27) — KPI-3 « > 70% cliniquement plausible » : protocole d'évaluation qualitative insuffisant

**Texte actuel (WP6, KPI) :**
> « KPI-3 : > 70 % des évaluateurs experts jugent le KPI « cliniquement plausible » nécessite un protocole d'évaluation : nombre d'évaluateurs, grille de notation standardisée, mesure de l'accord inter-évaluateurs (kappa de Fleiss), et évaluation en aveugle »

**Problème :** Le WP reconnaît explicitement que ce KPI nécessite un protocole mais ne le fournit pas. C'est une auto-critique non résolue.

**Texte de remplacement :**
> **KPI-3** : > 70 % des évaluateurs experts jugent les prédictions « cliniquement plausibles ».
>
> *Protocole d'évaluation qualitative :*
> - **Panel** : >= 10 évaluateurs indépendants issus de >= 3 institutions (Sanofi, Cedars-Sinai, Mayo Clinic, ICM)
> - **Grille de notation** : échelle de Likert à 5 niveaux (1 = cliniquement implausible, 5 = cliniquement très plausible), appliquée à chaque composante du profil B-R (efficacité, sécurité, interactions, incertitude)
> - **Évaluation en aveugle** : les évaluateurs ne connaissent pas la molécule évaluée ni la source des prédictions (modèle vs profil B-R réel shufflé comme contrôle)
> - **Accord inter-évaluateurs** : mesuré par kappa de Fleiss (seuil minimal : κ > 0,40 = accord modéré)
> - **Seuil de succès** : >= 70 % des évaluations ≥ 3/5 (« plausible » ou « très plausible »)

**Justification :** Un KPI qualitatif sans protocole standardisé est un chèque en blanc. Le protocole ci-dessus est le standard méthodologique pour les évaluations d'experts en IA médicale.

---

### C7. ÉLEVÉ — WP4 (p.16) — Tableau Tâches & articulation : absence de lien avec le WP6

**Texte actuel (WP4, Tâches & articulation) :**
Le tableau liste T4.1 à T4.5 avec leurs entrées, sorties et liens WP. La tâche T4.5 (Validation et calibration) indique « Lien WP : WP6 (intégration) ».

**Problème :** Le lien T4.5 → WP6 est correct mais trop vague. Les tâches T4.3 et T4.4 (modèles prédictifs) ont aussi un lien vers le WP6 (elles alimentent le stacking WP6 T6.2) qui n'est pas mentionné.

**Texte de remplacement pour les liens WP dans le tableau :**

| Tâche | Lien WP actuel | Lien WP corrigé |
|---|---|---|
| T4.3 Modèles prédictifs Bénéfices | WP1, WP2, WP3 | WP1, WP2, WP3, **WP6 (T6.2 stacking)** |
| T4.4 Modèles prédictifs Risques | WP1, WP2, WP3 | WP1, WP2, WP3, **WP6 (T6.2 stacking)** |
| T4.5 Validation & calibration | WP6 (intégration) | **WP6 (T6.2 intégration, T6.6 validation)** |

**Justification :** Rendre les liens inter-WP plus précis (avec numéro de tâche) renforce la perception de cohérence architecturale.

---

### C8. ÉLEVÉ — WP5 (p.20-21) — Typage des arêtes : terminologie « causale / directionnelle / associative » non définie dans le corps du WP5

**Texte actuel (WP5, après le tableau des tâches, p.21) :**
> « Chaque arête est annotée selon trois catégories explicites : (i) causale validée (issue d'études interventionnelles), (ii) directionnelle inférée (soutenue par un mécanisme biologique connu), (iii) associative (co-occurrence, sans direction causale établie). Le SCM du WP6 n'opère que sur les arêtes de types (i) et (ii). »

**Problème :** Ce passage apparaît dans la section « WP5 est structurellement le pivot entre les WP de production de connaissances et le WP d'intégration/simulation », mais la définition des trois types n'est pas reprise dans la section T5.3 (Construction du KG) ni dans la section T5.4 (Extraction NLP). C'est une information cruciale qui devrait figurer dans la méthodologie technique.

**Action :** Ajouter dans la section T5.3 (Construction du KG, p.20) le passage suivant :

**Texte à insérer dans T5.3 :**
> Chaque arête du KG est annotée selon **trois niveaux de causalité** :
> - **(i) Causale validée** : relation issue d'une étude interventionnelle (essai clinique randomisé, étude in vitro mécanistique). Score de confiance maximal.
> - **(ii) Directionnelle inférée** : relation soutenue par un mécanisme biologique documenté (voie de signalisation, métabolisme enzymatique) mais non démontrée par intervention directe. Score de confiance intermédiaire.
> - **(iii) Associative** : co-occurrence statistique sans direction causale établie (ex. : corrélation observée dans les données RWE). Score de confiance minimal.
>
> Cette distinction est fondamentale pour le WP6 : le SCM (Structural Causal Model) n'opère que sur les arêtes de types (i) et (ii), garantissant que le raisonnement causal du world model repose exclusivement sur des relations à évidence mécanistique ou interventionnelle.

**Justification :** Le typage causal des arêtes est l'innovation structurelle majeure du KG par rapport aux KG publics existants (DRKG, PrimeKG). Ce passage doit figurer dans la méthodologie, pas seulement dans un paragraphe de contexte.

---

### C9. ÉLEVÉ — WP6 (p.28) — Tableau Tâches & articulation : « Lien WP » de T6.1 trop vague

**Texte actuel (WP6, Tableau Tâches & articulation, p.28) :**

| Tâche | Lien WP |
|---|---|
| T6.1 Architecture world model | Transversal (SLMs, Profiling Base) |

**Problème :** « Transversal (SLMs, Profiling Base) » est vague. T6.1 consomme les embeddings SLM (actif pré-existant) et la Profiling Base (actif pré-existant). Il faudrait expliciter que ce ne sont pas des WPs du projet mais des actifs d'entrée.

**Texte de remplacement :**

| Tâche | Lien WP |
|---|---|
| T6.1 Architecture world model | **Actifs pré-existants** (24 Contextualizing SLMs, Profiling Base 100 Mds points). Spécifications d'interface avec WP1-4 (formats de sortie) et WP5 (API KG, T5.5) |

**Justification :** Clarifier que T6.1 s'appuie sur des actifs pré-existants (et non sur des livrables des WPs du projet) renforce l'argumentaire « le pré-entraînement est largement réalisé, le projet finance l'intégration ».

---

## PARTIE D — CORRECTIONS DE FORME ET D'HARMONISATION

---

### D1. FORME — Tous les WPs — Harmonisation des en-têtes

**Problème :** La structure des en-têtes varie d'un WP à l'autre :
- WP1 : pas d'en-tête structuré (Partenaires / Période / Jalons)
- WP2 : pas d'en-tête structuré
- WP3 : en-tête structuré ✓ (Partenaires / Période / Jalon principal)
- WP4 : pas d'en-tête structuré
- WP5 : en-tête structuré ✓ (Partenaires validation / Partenaire données / Période / Jalons)
- WP6 : pas d'en-tête structuré

**Action :** Ajouter un en-tête structuré pour chaque WP manquant :

**WP1 :**
> **Partenaires** : Sanofi, Cedars-Sinai, Mayo Clinic (validation)
> **Période** : Q1 2026 – Q1 2027 (M1 – M15) | **Jalon principal** : EC1 (fin 2026)

**WP2 :**
> **Partenaires** : Sanofi, Cedars-Sinai, Mayo Clinic (validation clinique), Gradient Health (données)
> **Période** : Q2 2026 – Q4 2027 (M6 – M24) | **Jalon principal** : EC1 (fin 2026, infrastructure + modèles NLP)

**WP4 :**
> **Partenaires** : Cedars-Sinai, Mayo Clinic, Institut du Cerveau (ICM), Gradient Health
> **Période** : Q3 2026 – Q2 2028 (M7 – M30) | **Jalon principal** : EC2 (mi-2027, modèles RWE validés)

**WP6 :**
> **Partenaires validation** : Sanofi, Cedars-Sinai, Mayo Clinic, ICM, AMI Labs (cadrage en cours)
> **Période** : Q1 2027 – Q4 2028 (M13 – M36) | **Jalons** : EC2 (mi-2027, architecture validée), EC3 (fin 2028, world model opérationnel)

**Justification :** L'uniformité de présentation est un signal de rigueur. Un évaluateur qui feuillette le WP s'attend à trouver les mêmes informations au même endroit dans chaque WP.

---

### D2. FORME — WP3 (p.14) — Faute « pharmacogénomiqe »

**Texte actuel (WP3, Contribution à la répétabilité) :**
> « pharmacogénomiqe »

**Texte de remplacement :**
> « pharmacogénomique »

**Justification :** Coquille simple.

---

### D3. FORME — WP2 (p.8) — Phrase coupée dans Tâches & articulation

**Texte actuel :**
> « Le calendrier s'étend de Q2 2026 à Q4 2027, avec une phase d'infrastructure commune en 21 2026. »

**Voir correction A2** — « 21 2026 » est une coquille.

---

## RÉCAPITULATIF

| Catégorie | Nombre | Impact |
|---|---|---|
| **BLOQUANT** | 8 corrections (A1-A8) | Incohérences V7↔WP, erreurs factuelles, coquilles structurelles |
| **CRITIQUE** | 6 corrections (B1-B6) | Lacunes méthodologiques exploitables par les évaluateurs |
| **ÉLEVÉ** | 9 corrections (C1-C9) | Fragilités de forme, précisions manquantes, liens inter-WP |
| **FORME** | 3 corrections (D1-D3) | Harmonisation, coquilles typographiques |
| **Total** | **26 corrections** | |

---

*Fin du Document 1 WP — 26 corrections identifiées (8 bloquantes, 6 critiques, 9 élevées, 3 de forme)*
