# AUDIT FINANCIER COMPLET — DOSSIER BR-PREDICT i-DEMO
## Cross-référencement V7 / Business Plan / Base Budgétaire / Workpackages
### Mars 2026

---

# TABLE DES MATIERES

1. [Synthèse exécutive](#1-synthèse-exécutive)
2. [Matrice de cross-référencement des totaux](#2-matrice-de-cross-référencement)
3. [Ecarts critiques](#3-écarts-critiques)
4. [Ecarts importants](#4-écarts-importants)
5. [Vérification logique du Business Plan](#5-vérification-logique-bp)
6. [Vérification logique de la Base Budgétaire](#6-vérification-logique-bb)
7. [Cohérence revenus / effectifs / dépenses](#7-cohérence-revenus-effectifs)
8. [Plan de financement : V7 vs BP](#8-plan-financement)
9. [Résumé des actions requises](#9-actions-requises)

---

# 1. SYNTHESE EXECUTIVE

L'audit croisé des 4 documents du dossier BR-PREDICT i-Démo révèle **2 incohérences majeures**, **6 écarts importants** et **plusieurs points de vigilance logique** dans le Business Plan.

**Verdict global** : Les documents ne sont PAS alignés en l'état. Le dossier présente un risque élevé de rejet BPI si les écarts financiers ne sont pas corrigés.

### Documents audités :
| Document | Désignation | Total projet |
|---|---|---|
| V7 PDF | ARCA_SCIENCE_V7_github.pdf (76 pages) | **5 360 000 €** |
| Business Plan | ArcaScience_Business_plan_I-demo.xlsx (24 onglets) | N/A (P&L global) |
| Base Budgétaire | Base_budgetaire_ArcaScience_full.xlsx (15 onglets) | **7 470 200 €** |
| Workpackages | I-demo_Workpackages_dossier.docx | Qualitatif |

---

# 2. MATRICE DE CROSS-REFERENCEMENT DES TOTAUX

## 2.1 Budget total du projet

| Source | Montant | Ecart vs BB |
|---|---|---|
| **Base Budgétaire (BB)** | **7 470 200 €** | Référence |
| **V7 (page 1 + Tableau 2)** | **5 360 000 €** | **-2 110 200 € (-28,2%)** |

**Explication probable** : Le V7 présente un budget en 4 postes (Personnel / Sous-traitance / Achats / Amortissements) qui ne suit PAS la structure BPI. La BB utilise la structure BPI officielle (Salaires / FG 20% / Autres dépenses). La différence de 2,11 M€ correspond approximativement aux frais généraux forfaitaires (1 202 200 €) + autres écarts.

## 2.2 Budget par lot

| Lot | V7 (Tableau 2) | Base Budgétaire | Ecart | Ecart % |
|---|---|---|---|---|
| Lot 1 (QSAR/QSTR) | 650 000 | 816 000 | +166 000 | +25,5% |
| Lot 2 (In vivo) | 750 000 | 922 800 | +172 800 | +23,0% |
| Lot 3 (Pharmaco-géno) | 850 000 | 807 600 | -42 400 | -5,0% |
| Lot 4 (RWE) | 1 100 000 | 1 363 800 | +263 800 | +24,0% |
| Lot 5 (KG) | 550 000 | 1 112 000 | +562 000 | +102,2% |
| Lot 6 (World Model) | 1 300 000 | 1 724 400 | +424 400 | +32,6% |
| Lot 7 (Management) | 160 000 | 723 600 | +563 600 | +352,3% |
| **TOTAL** | **5 360 000** | **7 470 200** | **+2 110 200** | **+39,4%** |

**ALERTE** : Le Lot 7 (Management) passe de 160 k€ dans le V7 à 723,6 k€ dans la BB (+352%). Le Lot 5 double (+102%). Cela suggère que le V7 sous-estime systématiquement les coûts de personnel affectés à ces lots.

## 2.3 Budget par nature de dépense

| Nature | V7 (Tableau 2) | Base Budgétaire | Ecart |
|---|---|---|---|
| Personnel/Salaires | 4 430 000 | 6 011 000 | **+1 581 000** |
| Sous-traitance | 580 000 | 0 | **-580 000** |
| Achats/Autres dép. | 205 000 | 257 000 | +52 000 |
| Amortissements | 145 000 | 0 | **-145 000** |
| Frais généraux (20%) | N/A | 1 202 200 | +1 202 200 |
| **TOTAL** | **5 360 000** | **7 470 200** | **+2 110 200** |

### Analyse de la réconciliation :
- **Salaires** : V7 = 4 430k vs BB = 6 011k. Ecart de +1 581k. La BB calcule les salaires sur la base de 582 personnes.mois (266 cat1 x 12 500€ + 316 cat2 x 8 500€ = 6 011 000€). Le V7 semble utiliser un périmètre restreint.
- **Sous-traitance** : V7 = 580k (détaillée : Gradient Health 170k, Cedars-Sinai/Mayo 105k, INRIA 75k, ICM 60k, L6 60k, brevets 20k, surplus 90k). BB = 0€. **Contradiction totale.**
- **Frais généraux** : Absents du V7, présents dans BB à 20% des salaires (1 202 200€). C'est le BFS (Barème Forfaitaire Simplifié).
- **Amortissements** : V7 = 145k, BB = 0€. Les amortissements du V7 pourraient être reclassés en "Autres dépenses" dans la BB.

---

# 3. ECARTS CRITIQUES

## ECART C1 — Sous-traitance : 580 000 € dans le V7, 0 € dans la Base Budgétaire

**Gravité : BLOQUANT BPI**

Le V7 détaille 580 k€ de sous-traitance répartis entre 6 prestataires :

| Prestataire | Lots | Montant V7 |
|---|---|---|
| Gradient Health | L1, L2, L4 | 170 000 € |
| Cedars-Sinai / Mayo Clinic | L2, L4 | 105 000 € |
| INRIA | L1, L5 | 75 000 € |
| ICM | L3 | 60 000 € |
| AMI Labs / Sanofi (L6) | L6 | 110 000 € |
| Brevets (L7) | L7 | 20 000 € |
| Non-attribué | -- | 40 000 € |
| **TOTAL** | | **580 000 €** |

Or, dans la Base Budgétaire (feuille Part. Nature, sheet9), la ligne "Sous-traitance présentée" est à **0 €** pour tous les lots.

**Impact** : BPI va comparer le texte narratif du V7 qui détaille la sous-traitance avec la BB qui montre 0€. Ce sera immédiatement relevé comme incohérence majeure.

**Action requise** :
- Option A : Intégrer les 580 k€ de sous-traitance dans la BB (nécessite de redistribuer les coûts)
- Option B : Retirer toute mention de sous-traitance du V7 et reclasser en coûts internes (déconseillé car les prestataires sont réels)

## ECART C2 — Budget total : 5 360 000 € dans le V7, 7 470 200 € dans la Base Budgétaire

**Gravité : BLOQUANT BPI**

Le V7 page 1 indique "Coût total du projet (€) : 5 360 000 €". La Base Budgétaire totalise 7 470 200 €.

**Action requise** : Choisir un montant unique et aligner tous les documents. Voir CORRECTIONS_V7_BR-PREDICT.md pour les options détaillées.

---

# 4. ECARTS IMPORTANTS

## ECART I1 — Revenus V7 vs Business Plan

| Année | V7 (page 67) | BP (P&L) | Ecart |
|---|---|---|---|
| 2026 | 925 k€ | 925 000 | **OK** |
| 2027 | 2 062 k€ / "1 987 k€" | 2 062 500 | **~OK** (le V7 donne 2 valeurs) |
| 2028 | 3 950 k€ / "3 600 k€" | 3 950 000 | **ECART V7 interne** |
| 2029 | 6 900 k€ / "5 325 k€" | 6 900 000 | **ECART V7 interne** |
| 2030 | 14 250 k€ / "8 425 k€" | 14 250 000 | **ECART V7 interne** |

**Diagnostic** : Le V7 présente DEUX tableaux de revenus distincts (page 66-67) :
1. Un tableau "CA Total" Trial Balancer only : 925k / 1 987k / 3 600k / 5 325k / 8 425k
2. Un tableau "CA Total" TB + BR-Predict : 925k / 2 062k / 3 950k / 6 900k / 14 250k

Le BP utilise les chiffres du tableau 2 (avec BR-Predict). **Les deux tableaux doivent être clairement distingués dans le V7** pour éviter toute confusion du rapporteur.

## ECART I2 — Effectifs : V7 vs Business Plan

| Source | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| V7 (p.7) "27 recrutements" | 14,5 ETP + 6 = ~20 | +4 = ~24 | +13 = ~37 | +4 = ~41 | -- |
| V7 (p.7) "47 personnes sur la durée" | ~20 | ~24 | ~44 (pic 2028) | -- | -- |
| BP (T1 Effectifs) | **23** | **35** | **53** | **65** | **72** |

**Diagnostic** : Le V7 annonce "27 recrutements planifiés" et "47 personnes sur la durée du projet", mais le BP montre un effectif croissant de 23 à 72 personnes, soit 49 recrutements nets (72 - 23 = 49 nouveaux postes entre 2026 et 2030). Le chiffre "47" du V7 ne correspond pas à la trajectoire du BP.

## ECART I3 — Dépenses opérationnelles : V7 vs Business Plan

Le V7 (page 71) mentionne des "Dépenses opérationnelles totales de 16 042 k€" sur la durée du projet, décomposées en :
- RH : 13 218 k€ (83%)
- Marketing : 761 k€ (4%)
- Autres : 2 063 k€ (13%)

Le BP donne :

| Poste | BP Cumul 2026-2030 | V7 (p.71) | Ecart |
|---|---|---|---|
| Total HR | 29 079 k€ | 13 218 k€ | **+15 861 k€** |
| Total OPEX | 6 199 k€ | 2 063 k€ | **+4 136 k€** |
| Marketing (dans OPEX) | 1 726 k€ | 761 k€ | **+965 k€** |

**Diagnostic** : Le V7 section 6.2.2 présente des charges opérationnelles nettement inférieures au BP. Le V7 couvre probablement uniquement la période projet (36 mois = 2026-2029, soit 3 ans) tandis que le BP va jusqu'à 2030 (5 ans). Mais même sur 2026-2029, le BP donne :
- HR 2026-2029 : 20 762 k€ vs V7 13 218 k€ (écart de 7 544 k€)

**Le V7 et le BP ne sont PAS sur le même périmètre RH.** Le V7 semble ne compter que le personnel "projet" (R&D), tandis que le BP compte tout le personnel (G&A + IT + Sales + Marketing).

## ECART I4 — Classification Lot 6 : V7 vs Base Budgétaire

Le V7 Tableau 2 ne précise pas la classification des lots. Mais dans la BB :
- **Lot 6 (World Model) est classé DE (Développement Expérimental)** : 1 724 400 €

Le V7 décrit le Lot 6 comme un travail de R&D fondamentale (architecture world model, JEPA, modélisation causale). Une classification en "RI" (Recherche Industrielle) serait plus cohérente avec la description narrative et donnerait un meilleur taux d'aide BPI.

**Action recommandée** : Vérifier si DE est intentionnel. Si le travail du Lot 6 peut être qualifié de RI, le taux d'aide serait plus favorable (jusqu'à 45% pour RI vs 25% pour DE pour une PE).

## ECART I5 — Personnes.mois : V7 vs Base Budgétaire

La BB donne 582 personnes.mois totales (266 cat1 + 316 cat2). Le V7 ne fournit PAS de tableau récapitulatif des personnes.mois — les descriptions de lots donnent uniquement des montants en euros par tâche.

**Vérification croisée BB :**
- 266 PM cat1 × 12 500 €/PM = 3 325 000 €
- 316 PM cat2 × 8 500 €/PM = 2 686 000 €
- Total salaires = 6 011 000 € ✅ (cohérent avec Part. Nature)
- FG = 6 011 000 × 20% = 1 202 200 € ✅
- Total = 6 011 000 + 1 202 200 + 257 000 = 7 470 200 € ✅

La BB est internement cohérente.

## ECART I6 — Innov'Up : V7 vs Business Plan

| Composante | V7 (section 6.2.2) | BP (Financements) |
|---|---|---|
| Prêt d'amorçage | 283 000 € | -- |
| Acompte | 240 000 € | -- |
| Prêt innovation | "797 k€" (implicite) | -- |
| Solde | 160 000 € | -- |
| **Total Innov'Up** | **~1 480 000 €** | **1 500 000 €** (dont 400k subvention) |

Le BP montre un Innov'Up de 1 500 000 € (dont 400 000 € de subvention, le reste en prêt à 4,01% sur 60 mois avec 24 mois de différé). Le V7 donne des détails différents mais cohérents en ordre de grandeur (~1,48M vs 1,5M).

**Cash-in Innov'Up dans le BP** : 900 000 € reçus en 2026, 0 ensuite (le capital restant dû montre 630 000 € fin 2026 puis 1 100 000 € fin 2027, ce qui implique un décaissement progressif).

---

# 5. VERIFICATION LOGIQUE DU BUSINESS PLAN

## 5.1 Cohérence interne P&L

| Test | Résultat |
|---|---|
| Revenue = TB POC + TB licence + Predict mol. + Predict projet | ✅ OK |
| Gross Margin = Revenue - COGS | ✅ OK (90% à partir de 2027) |
| EBITDA Cash = Gross Margin - Total HR - Total OPEX | ✅ OK |
| EBITDA post prod immo = EBITDA Cash + Capitalised Production | ✅ OK |
| EBIT = EBITDA post prod immo - D&A | ✅ OK |
| Net Income = EBT - Tax | ✅ OK |

## 5.2 Cohérence T1 BPI

| Test | Résultat |
|---|---|
| CA dans T1 = Revenue dans P&L | ✅ OK (925k / 2 062k / 3 950k / 6 900k / 14 250k) |
| Production immobilisée = Capitalised Production | ✅ OK |
| Charges personnel T1 (2 717k) vs HR P&L (2 752k) | ⚠️ Ecart de 35k (= Impôts et taxes non inclus dans T1 R29) |
| Résultat T1 = Net Income + CIR | ✅ OK (-1 232k vs -1 571k + 340k CIR = -1 231k) |
| CAF = Résultat + Amortissements | ✅ OK |

## 5.3 Cohérence T2 BPI (Plan de financement)

| Test | Résultat |
|---|---|
| CAF dans T2 = CAF dans T1 | ✅ OK (-1 071k / -651k / +506k / +2 942k / +9 364k) |
| Augmentation de capital 2027 = 20 000 k€ | ✅ Présent (= levée Series B de 20 M€) |
| Autres aides publiques = 240k (2026) + 160k (2027) | ✅ = Innov'Up subvention (400k total) |
| Emprunts négociés = 1 037k (2026) | ✅ = Innov'Up prêt portion |
| Cumul trésorerie > 0 toutes les années | ✅ OK (3 683k, 23 192k, 23 546k, 26 279k, 35 426k) |

**ATTENTION** : Le T2 montre une trésorerie TRES positive grâce à la levée de 20M€ en 2027. Sans cette levée, la trésorerie serait négative dès 2027 (-2 228k dans le cash-flow sheet9). **La levée de 20 M€ est absolument critique.**

## 5.4 Cohérence Cash-flow vs T2

Le cash-flow (sheet9) ne montre **PAS** la levée de 20 M€ ni l'Innov'Up ni l'i-Démo. Il ne montre qu'un flux opérationnel + remboursement de dette. C'est un **cash-flow opérationnel** uniquement.

| Année | Cash-flow opérationnel (sheet9) | T2 avec financements | Ecart |
|---|---|---|---|
| 2026 | Cash end = 1 107k | Cumul = 3 683k | Delta de 2 576k |
| 2027 | Cash end = -2 228k | Cumul = 23 192k | Delta de 25 420k |

Le T2 est la vue correcte pour BPI (avec financements). Le cash-flow sheet9 est une vue partielle.

## 5.5 i-Démo manquant dans le BP

**PROBLEME MAJEUR** : Le V7 section 6.2.2 détaille l'aide i-Démo demandée :
- EC1 (acompte) : 325 000 €
- EC2 (tranche 2) : 1 350 000 €
- EC3 (solde) : 1 005 000 €
- **Total i-Démo : 2 680 000 €**

Or, dans le BP :
- T2 ligne "Aide envisagée" (row 25) : **VIDE** (pas de montant)
- Financements sheet24 : **Aucune ligne i-Démo**
- Cash-flow sheet9 : **Aucun versement i-Démo**

**L'aide i-Démo de 2 680 k€ n'est pas intégrée dans le Business Plan.** C'est une omission grave car :
1. BPI s'attend à voir l'aide dans le plan de financement
2. Sans cette aide, le cash position est 2,68 M€ plus bas que prévu
3. Cela fausse le calcul de solvabilité

**Action requise** : Ajouter dans le BP :
- T2 ligne "Aide envisagée" : 325k (2026), 1 350k (2027), 1 005k (2028)
- Financements sheet24 : Nouvelle ligne "i-Démo BPI France" avec les 3 versements

---

# 6. VERIFICATION LOGIQUE DE LA BASE BUDGETAIRE

## 6.1 Cohérence interne

| Test | Résultat |
|---|---|
| Somme lots = Total | ✅ 816k + 922,8k + 807,6k + 1 363,8k + 1 112k + 1 724,4k + 723,6k = 7 470,2k |
| Somme EC = Total | ✅ 3 560,4k + 2 314,1k + 1 595,7k = 7 470,2k |
| Somme natures = Total | ✅ 6 011k + 1 202,2k + 257k = 7 470,2k |
| FG = 20% × Salaires | ✅ 1 202 200 = 20% × 6 011 000 |
| Salaires = Cat1_PM × Sal1 + Cat2_PM × Sal2 | ✅ 266 × 12 500 + 316 × 8 500 = 3 325 000 + 2 686 000 = 6 011 000 |
| ADM + RI + DE = Total | ✅ 723,6k + 5 022,2k + 1 724,4k = 7 470,2k |

**La Base Budgétaire est parfaitement cohérente internement.**

## 6.2 Calendrier EC

| EC | Mois fin | Date (approx.) |
|---|---|---|
| T0 | - | ~Avril/Mai 2026 |
| EC1 | Mois 14 | ~Juin 2027 |
| EC2 | Mois 23 | ~Mars 2028 |
| EC3 | Mois 35 | ~Mars 2029 |

**Durée totale** : 35 mois (pas 36 comme indiqué dans le V7 page 1 qui dit "36 mois").
Le V7 dit "36 mois" avec dates 01/05/2026 - 30/04/2029. La BB calcule 35 mois (fin EC3 = mois 35). Ecart mineur mais à vérifier.

## 6.3 Taux de salaire moyens

- Cat 1 : 12 500 €/PM (ingénieur senior, PhD, team lead)
- Cat 2 : 8 500 €/PM (ingénieur junior, data scientist)
- Moyenne pondérée : 10 328 €/PM

Ces taux sont cohérents avec le marché Paris deeptech 2026 et les standards BPI.

---

# 7. COHERENCE REVENUS / EFFECTIFS / DEPENSES

## 7.1 Revenu par employé

| Année | Revenue | Effectifs | Rev/ETP |
|---|---|---|---|
| 2026 | 925 k€ | 23 | 40 k€/ETP |
| 2027 | 2 063 k€ | 35 | 59 k€/ETP |
| 2028 | 3 950 k€ | 53 | 75 k€/ETP |
| 2029 | 6 900 k€ | 65 | 106 k€/ETP |
| 2030 | 14 250 k€ | 72 | 198 k€/ETP |

La productivité par ETP triple entre 2028 et 2030 (75k→198k). C'est plausible pour un modèle SaaS à forte scalabilité, mais agressif. BPI pourrait questionner le doublement du CA entre 2029 et 2030 (+106%) avec seulement 7 recrutements supplémentaires.

## 7.2 Coût moyen par employé (BP)

| Année | Total HR | Effectifs | Coût/ETP |
|---|---|---|---|
| 2026 | 2 752 k€ | 23 | 120 k€/ETP |
| 2027 | 4 246 k€ | 35 | 121 k€/ETP |
| 2028 | 6 219 k€ | 53 | 117 k€/ETP |
| 2029 | 7 544 k€ | 65 | 116 k€/ETP |
| 2030 | 8 318 k€ | 72 | 116 k€/ETP |

Le coût moyen par ETP (120k€ charges comprises, soit ~83k€ brut annuel / ~6,9k€ brut mensuel) est cohérent avec le marché tech Paris pour un mix juniors/seniors.

## 7.3 Burn Rate et Runway

| Année | EBITDA Cash | Cash début | Runway (mois) |
|---|---|---|---|
| 2026 | -2 549 k€ | 3 683 k€ | ~17 mois |
| 2027 | -3 308 k€ | ~1 107 k€ | ~4 mois ⚠️ |
| 2028 | -3 873 k€ | -- | NEGATIF sans levée |

**Sans la levée de 20 M€ en 2027, l'entreprise est en cessation de paiement mi-2027.**
Avec la levée : runway confortable (20M + 1,1M = ~21M de trésorerie, soit >6 ans de burn).

---

# 8. PLAN DE FINANCEMENT : V7 vs BP

## 8.1 Sources de financement déclarées

| Source | V7 (section 6.2.2) | BP (T2 + Financements) | Statut |
|---|---|---|---|
| Série A (2025) | 4 650 k€ | 4 350 k€ | ⚠️ Ecart de 300k€ |
| Innov'Up total | ~1 480 k€ | 1 500 k€ (dont 400k sub) | ~OK |
| i-Démo | 2 680 k€ | **NON INTEGRE** | **MANQUANT** |
| Levée Series B (2028) | 20 000 k€ | 20 000 k€ (en 2027 dans T2) | ⚠️ Date différente |
| CIR | Non mentionné | 340k→1 551k (2026-2030) | Présent BP only |

### Détail des écarts :

**Série A** : V7 dit "4,65 M€" (p.5), BP montre 4 350 000 € (sheet24 row 12). Ecart de 300 k€ à clarifier.

**Levée Series B** : V7 dit "20 M€ prévue pour 2028" (p.72), le T2 du BP la place en **2027** (colonne F = 2027, row 20). Ecart d'un an — à aligner.

**i-Démo 2 680 k€** : Absent du BP. A intégrer d'urgence.

## 8.2 CIR (Crédit Impôt Recherche)

Le BP intègre un CIR significatif :

| Année | CIR | % des charges R&D |
|---|---|---|
| 2026 | 340 k€ | 31% |
| 2027 | 569 k€ | 31% |
| 2028 | 919 k€ | 30% |
| 2029 | 1 173 k€ | 30% |
| 2030 | 1 551 k€ | 30% |

Le CIR est calculé à ~30% des dépenses R&D éligibles (personnel R&D + amortissements). C'est cohérent avec le taux JEI/PME.

**ATTENTION** : Le CIR est intégré dans le Résultat de l'exercice (T1 row 41) mais PAS dans le cash-flow opérationnel (sheet9). Il apparaît dans le T3 startup (6-month cash) comme "CIR/CII/TVA" encaissé avec un décalage de ~12 mois. C'est logiquement correct (le CIR est remboursé l'année suivante pour les PME).

## 8.3 Production immobilisée (Prod. Immo.)

Le BP capitalise une partie significative des coûts R&D :

| Année | Prod. Immo | % du total HR+OPEX |
|---|---|---|
| 2026 | 1 172 k€ | 34% |
| 2027 | 2 131 k€ | 41% |
| 2028 | 3 501 k€ | 47% |
| 2029 | 4 652 k€ | 51% |
| 2030 | 6 653 k€ | 65% |

La part croissante de production immobilisée (de 34% à 65%) réduit artificiellement les charges dans le P&L (EBE) mais ne change pas le cash réel. C'est une pratique courante pour les startups deeptech avec des investissements R&D lourds. Cependant, BPI pourrait questionner un taux de capitalisation supérieur à 50%.

---

# 9. RESUME DES ACTIONS REQUISES

## Actions BLOQUANTES (à corriger avant soumission)

| # | Action | Documents concernés | Impact |
|---|---|---|---|
| **A1** | Aligner le budget total V7 avec la BB (5 360k → 7 470k ou ajout note BFS) | V7 | Rejet si non corrigé |
| **A2** | Résoudre la contradiction sous-traitance (580k V7 vs 0 BB) | V7 + BB | Rejet si non corrigé |
| **A3** | Intégrer l'aide i-Démo (2 680k) dans le BP | BP (T2 + Financements) | Incohérence flagrante |
| **A4** | Réécrire le Tableau 2 du V7 avec la structure BPI correcte | V7 | Rejet si non corrigé |

## Actions IMPORTANTES (fortement recommandées)

| # | Action | Documents concernés |
|---|---|---|
| **B1** | Corriger la Série A : 4 650k (V7) vs 4 350k (BP) | V7 ou BP |
| **B2** | Aligner la date de la levée Series B : 2028 (V7) vs 2027 (BP) | V7 ou BP |
| **B3** | Clarifier les deux tableaux de CA dans le V7 (TB seul vs TB+Predict) | V7 |
| **B4** | Vérifier la classification DE du Lot 6 (possibilité de RI ?) | BB |
| **B5** | Aligner les effectifs V7 ("47 personnes") avec le BP (23→72 ETP) | V7 |
| **B6** | Ajouter un tableau de personnes.mois dans le V7 | V7 |

## Points de vigilance (questions probables du rapporteur BPI)

| # | Question anticipée | Réponse à préparer |
|---|---|---|
| **V1** | "Comment financez-vous les 3,3 M€ de burn annuel en 2027 avec 1,1 M€ de cash ?" | La levée de 20 M€ est prévue S1 2027 + les aides BPI |
| **V2** | "Le CA double en 2030 avec 7 recrues seulement, comment ?" | Scalabilité SaaS : le module BR-Predict démarre en 2029, les licences récurrentes s'accumulent |
| **V3** | "65% de prod. immo en 2030, n'est-ce pas excessif ?" | L'entreprise reste en phase de R&D intensive, toute la R&D est capitalisée selon les normes IFRS |
| **V4** | "Pourquoi la sous-traitance n'apparaît-elle pas dans la BB ?" | [A CORRIGER AVANT] |

---

---

# ANNEXE A — CROISEMENT DETAILLE LOT PAR LOT : V7 vs BASE BUDGETAIRE

## A.1 Personnel / Salaires par Lot

| Lot | V7 "Personnel" | BB "Salaires" | BB "Salaires + FG 20%" | Ecart V7 vs BB (Sal+FG) |
|---|---|---|---|---|
| Lot 1 | 540 000 | 667 500 | 801 000 | -261 000 |
| Lot 2 | 615 000 | 744 000 | 892 800 | -277 800 |
| Lot 3 | 695 000 | 673 000 | 807 600 | -112 600 |
| Lot 4 | 880 000 | 1 136 500 | 1 363 800 | -483 800 |
| Lot 5 | 470 000 | 885 000 | 1 062 000 | -592 000 |
| Lot 6 | 1 100 000 | 1 302 000 | 1 562 400 | -462 400 |
| Lot 7 | 130 000 | 603 000 | 723 600 | -593 600 |
| **TOTAL** | **4 430 000** | **6 011 000** | **7 213 200** | **-2 783 200** |

**Analyse** : Le V7 "Personnel" est systématiquement inférieur à BB "Salaires + FG" pour chaque lot. L'écart total de -2,78 M€ se décompose en :
- Frais généraux 20% absents du V7 : 1 202 200 €
- Ecart pur sur les salaires : 1 581 000 € (V7 sous-estime les salaires)

## A.2 Achats (V7) vs Autres dépenses (BB) — par Lot

| Lot | V7 "Achats" | V7 "Amort." | V7 Total (Achats+Amort.) | BB "Autres dépenses" | Ecart |
|---|---|---|---|---|---|
| Lot 1 | 25 000 | 15 000 | 40 000 | 15 000 | **+25 000** |
| Lot 2 | 30 000 | 20 000 | 50 000 | 30 000 | **+20 000** |
| Lot 3 | 35 000 | 20 000 | 55 000 | 0 | **+55 000** |
| Lot 4 | 40 000 | 30 000 | 70 000 | 0 | **+70 000** |
| Lot 5 | 20 000 | 15 000 | 35 000 | 50 000 | **-15 000** |
| Lot 6 | 50 000 | 40 000 | 90 000 | 162 000 | **-72 000** |
| Lot 7 | 5 000 | 5 000 | 10 000 | 0 | **+10 000** |
| **TOTAL** | **205 000** | **145 000** | **350 000** | **257 000** | **+93 000** |

**Analyse** : Le V7 sépare les dépenses non-RH en "Achats" et "Amortissements" (total 350 k€), tandis que la BB ne les met qu'en "Autres dépenses" (257 k€). La structure est différente et les montants ne correspondent pas. Notamment :
- Lots 5 et 6 : la BB a des "Autres dépenses" bien plus élevées que le V7 (infra Neo4j Cloud 50k, Cloud GPU 162k), mais le V7 a des montants plus faibles dans ses catégories
- Lots 3 et 4 : le V7 annonce des dépenses, la BB montre 0 €

**Conclusion** : Les dépenses non-RH sont réparties différemment entre V7 et BB. La BB semble regrouper les GPU/Cloud en "Autres dépenses" alors que le V7 les classe en "Amortissements". Il faut harmoniser.

## A.3 Personnes.mois par Lot (Base Budgétaire uniquement)

| Lot | Cat 1 (12 500€/PM) | Cat 2 (8 500€/PM) | Total PM | Salaires calculés |
|---|---|---|---|---|
| Lot 1 | 33 | 30 | 63 | 667 500 ✅ |
| Lot 2 | 33 | 39 | 72 | 744 000 ✅ |
| Lot 3 | 28 | 38 | 66 | 673 000 ✅ |
| Lot 4 | 44 | 69 | 113 | 1 136 500 ✅ |
| Lot 5 | 30 | 60 | 90 | 885 000 ✅ |
| Lot 6 | 62 | 62 | 124 | 1 302 000 ✅ |
| Lot 7 | 36 | 18 | 54 | 603 000 ✅ |
| **TOTAL** | **266** | **316** | **582** | **6 011 000** ✅ |

Tous les calculs de salaires sont vérifiés : Cat1 × 12 500 + Cat2 × 8 500 = Salaires pour chaque lot.

## A.4 Sous-traitance détaillée : V7 vs BB

### V7 — Sous-traitance par prestataire et par lot

| Prestataire | L1 | L2 | L3 | L4 | L5 | L6 | L7 | Total |
|---|---|---|---|---|---|---|---|---|
| Gradient Health | 40k | 50k | 80k | - | - | - | - | 170k |
| Cedars-Sinai/Mayo | - | 35k | 70k | - | - | - | - | 105k |
| INRIA | 30k | - | - | 45k | - | - | - | 75k |
| ICM | - | - | - | - | - | - | - | 60k (L3) |
| AMI Labs | - | - | - | - | - | 60k | - | 60k |
| Sanofi (validation) | - | - | - | - | - | 50k | - | 50k |
| INRIA (L5) | - | - | - | - | 37,5k | - | - | 37,5k |
| Brevets | - | - | - | - | - | - | 20k | 20k |
| **Total par lot** | **70k** | **85k** | **150k** | **45k** | **37,5k** | **110k** | **20k** | **~580k** |

Note : Le total des sous-traitances dans le descriptif des lots du V7 donne environ 577,5 k€, arrondi à 580 k€ dans le Tableau 2.

### BB — Sous-traitance

**ZERO pour tous les lots et toutes les tâches.**

### Ecart

| Lot | V7 Sous-traitance | BB Sous-traitance | Ecart |
|---|---|---|---|
| Lot 1 | 70 000 | 0 | **70 000** |
| Lot 2 | 85 000 | 0 | **85 000** |
| Lot 3 | 150 000 | 0 | **150 000** |
| Lot 4 | 45 000 | 0 | **45 000** |
| Lot 5 | 37 500 | 0 | **37 500** |
| Lot 6 | 110 000 | 0 | **110 000** |
| Lot 7 | 20 000 | 0 | **20 000** |
| **TOTAL** | **~580 000** | **0** | **~580 000** |

**C'est l'incohérence la plus flagrante du dossier.** BPI vérifie systématiquement la concordance entre le texte narratif (V7) et le tableur budgétaire (BB). 580 k€ de sous-traitance dans le V7 et 0 € dans la BB sera immédiatement identifié.

---

# ANNEXE B — DISTRIBUTION EC : V7 vs BASE BUDGETAIRE

## B.1 Répartition des coûts par Etape Clé (BB)

| Lot | EC1 (M0-M14) | EC2 (M14-M23) | EC3 (M23-M35) | Total |
|---|---|---|---|---|
| Lot 1 | 816 000 (100%) | 0 | 0 | 816 000 |
| Lot 2 | 595 200 (65%) | 327 600 (35%) | 0 | 922 800 |
| Lot 3 | 480 000 (59%) | 327 600 (41%) | 0 | 807 600 |
| Lot 4 | 742 200 (54%) | 444 600 (33%) | 177 000 (13%) | 1 363 800 |
| Lot 5 | 73 578 (7%) | 520 600 (47%) | 517 822 (46%) | 1 112 000 |
| Lot 6 | 564 000 (33%) | 507 600 (29%) | 652 800 (38%) | 1 724 400 |
| Lot 7 | 289 440 (40%) | 186 069 (26%) | 248 091 (34%) | 723 600 |
| **TOTAL** | **3 560 418 (48%)** | **2 314 069 (31%)** | **1 595 713 (21%)** | **7 470 200** |

## B.2 Comparaison avec les versements i-Démo (V7)

| EC | Coûts BB | i-Démo (V7) | Taux couverture |
|---|---|---|---|
| EC1 | 3 560 418 | 325 000 | 9,1% |
| EC2 | 2 314 069 | 1 350 000 | 58,3% |
| EC3 | 1 595 713 | 1 005 000 | 63,0% |
| **TOTAL** | **7 470 200** | **2 680 000** | **35,9%** |

Le taux d'aide moyen de 35,9% est cohérent avec les taux BPI i-Démo pour une PE en RI/DE (typiquement 25-45%). Cependant, le taux EC1 (9,1%) semble anormalement bas pour un acompte — BPI verse habituellement ~40% de l'aide totale en acompte. Il faudrait vérifier que 325 k€ est bien le bon montant d'acompte.

---

# ANNEXE C — COMPARAISON DEPENSES OPERATIONNELLES V7 vs BP (5 ans)

## C.1 Total des dépenses par année (Business Plan)

| Poste | 2026 | 2027 | 2028 | 2029 | 2030 | Cumul |
|---|---|---|---|---|---|---|
| HR Total | 2 752k | 4 246k | 6 219k | 7 544k | 8 318k | **29 079k** |
| dont HR R&D | 1 081k | 1 845k | 3 012k | 3 858k | 4 386k | **14 182k** |
| COGS | 24k | 206k | 395k | 690k | 1 425k | **2 740k** |
| OPEX | 698k | 917k | 1 209k | 1 516k | 1 860k | **6 200k** |
| D&A | 161k | 551k | 1 262k | 2 268k | 3 428k | **7 670k** |
| Prod. Immo | 1 172k | 2 131k | 3 501k | 4 652k | 6 653k | **18 109k** |
| CIR | 340k | 569k | 919k | 1 173k | 1 551k | **4 552k** |

## C.2 Croisement avec le V7 (page 71 — 16 042 k€ total)

Le V7 annonce 16 042 k€ de dépenses opérationnelles totales. Si l'on prend le BP sur la période projet (2026-2029, 4 ans) :

| Poste BP | 2026-2029 | V7 (p.71) |
|---|---|---|
| HR R&D | 9 796k | ~13 218k (RH) |
| HR Total (avec Sales/G&A) | 20 761k | |
| OPEX + COGS | 5 064k | ~2 063k (Autres) |
| Marketing (dans OPEX) | 1 181k | ~761k |
| **Total** | ~25 825k | **16 042k** |

**Le V7 annonce 16 042 k€ sur 36 mois là où le BP donne 25 825 k€ sur 48 mois (2026-2029).** Même réduit à 36 mois, le BP donne environ 19 000 k€ de dépenses. Le V7 semble présenter uniquement les coûts directs du projet (pas tout le P&L de l'entreprise).

---

*Rapport généré le 16 mars 2026 par audit automatisé Claude.*
*Sources : V7 PDF (76 pages), Business Plan xlsx (24 onglets), Base Budgétaire xlsx (15 onglets), Workpackages docx.*
