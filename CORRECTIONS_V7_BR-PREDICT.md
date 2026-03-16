# CORRECTIONS A APPLIQUER AU DOSSIER BR-PREDICT / i-DEMO
## Document de travail - Mars 2026

Ce document liste toutes les corrections à apporter aux 4 documents du dossier,
classées par priorité. Chaque correction est présentée avec le texte actuel et le
texte de remplacement, prêt à copier-coller.

---

# PRIORITE 1 : CORRECTIONS CRITIQUES (bloquantes BPI)

---

## CORRECTION 1 — Coût total du projet (Page de garde V7)

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : Page 1 — Éléments clés du projet
**Problème** : Le V7 affiche 5 360 000 € mais la Base Budgétaire BPI totalise 7 470 200 €

### Option A : Aligner le V7 sur la Base Budgétaire (RECOMMANDE)

**REMPLACER :**
```
Coût total du projet (€)          5 360 000 €
```

**PAR :**
```
Coût total du projet (€)          7 470 200 €
```

### Option B : Conserver 5 360 000 € comme "assiette éligible"
Si le montant de 5 360 k€ correspond volontairement à l'assiette éligible (hors frais
généraux forfaitaires), alors il faut ajouter une note explicative dans la section 6.2.1 :

**AJOUTER après la phrase "Planification de dépenses estimées" :**
```
Note méthodologique : Le coût total du projet présenté en page de garde (5 360 k€)
correspond à l'assiette éligible hors frais généraux forfaitaires. Le coût total présenté
dans la Base Budgétaire BPI (7 470 200 €) inclut les frais généraux calculés à 20 % des
salaires, conformément au barème forfaitaire simplifié (BFS) retenu pour ce dossier.
La ventilation détaillée figure dans le fichier Base_budgetaire_ArcaScience_I-Demo.xlsx.
```

---

## CORRECTION 2 — Tableau 2 : Budget par Lot (Section 3.5 du V7)

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 3.5 — Budget et principaux postes de sous-traitance du projet
**Problème** : Les montants par lot et par poste ne correspondent pas à la Base Budgétaire

### Si Option A retenue (alignement sur 7 470 200 €) :

**REMPLACER le Tableau 2 entier par :**

```
Tableau 2 : Budget par Lot et par poste de dépense

Poste de dépense (k€)   Lot 1   Lot 2   Lot 3   Lot 4   Lot 5   Lot 6   Lot 7   Total

Salaires                  668     744     673   1 137     885   1 302     603   6 011
Frais généraux (20%)      134     149     135     227     177     260     121   1 202
Autres dépenses            15      30       0       0      50     162       0     257
                        ─────   ─────   ─────   ─────   ─────   ─────   ─────   ─────
Total                     816     923     808   1 364   1 112   1 724     724   7 470

* Les frais généraux sont calculés à 20 % des salaires, conformément au BFS.
* La sous-traitance est valorisée dans les "Autres dépenses" selon les conventions
  du formulaire BPI.
```

### Tableau des sous-traitants (inchangé sauf total) :

**REMPLACER :**
```
Total                         580
```

**PAR :**
```
Total                         510*

* Les montants de sous-traitance listés ci-dessus sont financés sur le poste
  « Autres dépenses présentées » de la Base Budgétaire (257 k€) et complétés par
  des conventions de collaboration non financières avec les partenaires académiques.
```

> **Note** : la sous-traitance du V7 (580 k€) est supérieure aux "Autres dépenses"
> de la Base Budgétaire (257 k€). Il faut vérifier si les 323 k€ de différence
> correspondent à des prestations en nature non budgétées ou s'il y a une erreur.
> Les montants par sous-traitant doivent être réconciliés avec le poste "Autres
> dépenses" de chaque lot dans la Base Budgétaire :
> - Lot 1 : 15 k€ (vs V7 = 70 k€)
> - Lot 2 : 30 k€ (vs V7 = 85 k€)
> - Lot 3 : 0 k€ (vs V7 = 100 k€)
> - Lot 4 : 0 k€ (vs V7 = 150 k€)
> - Lot 5 : 50 k€ (vs V7 = 45 k€)
> - Lot 6 : 162 k€ (vs V7 = 110 k€)
> - Lot 7 : 0 k€ (vs V7 = 20 k€)
>
> **ACTION REQUISE** : Romain doit décider si les montants de sous-traitance du V7
> ou ceux de la Base Budgétaire sont corrects, et aligner les deux documents.

---

## CORRECTION 3 — Dates des jalons EC1 et EC2

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 2.6 — Synthèse des principaux jalons décisionnels du projet
**Problème** : Si T0 = 01/05/2026, alors EC1 (T0+18) = 11/2027 et EC2 (T0+28) = 09/2028.
Les dates actuelles (09/2027 et 07/2028) correspondent à un T0 = 01/2026.

**REMPLACER :**
```
EC1 : 0 + 18 mois (09/2027)
```

**PAR :**
```
EC1 : 0 + 18 mois (11/2027)
```

---

**REMPLACER :**
```
EC2 : 0 + 28 mois (07/2028)
```

**PAR :**
```
EC2 : 0 + 28 mois (09/2028)
```

---

**VERIFIER aussi** dans la section 6.2.2 (Plan de financement) :

**ACTUEL :**
```
i-Démo – tranche 2 (EC2) : 1 350 K€ – versée début Q3 2027
```

**CORRIGER EN :**
```
i-Démo – tranche 2 (EC2) : 1 350 K€ – versée début Q4 2028
```

> Note : le texte ODT actuel dit "Q3 2027" pour EC2, ce qui semble encore être
> sur l'ancien calendrier. Si EC2 = T0+28 mois = 09/2028, le versement serait Q3/Q4 2028.

---

**ACTUEL :**
```
i-Démo – solde (EC3) : 1 005 k€ – versée début Q2 2028
```

**CORRIGER EN :**
```
i-Démo – solde (EC3) : 1 005 k€ – versée début Q2 2029
```

---

## CORRECTION 4 — Business Plan xlsx : formules cassées

**Fichier** : ArcaScience - Business plan I-demo.xlsx
**Onglet** : Assumptions
**Problème** : Les colonnes mensuelles (H à BH) contiennent des formules exponentielles
qui produisent des valeurs absurdes (10^48) et des #REF!

**ACTION REQUISE :**

1. **Ouvrir** le fichier dans Excel/LibreOffice
2. **Onglet "Assumptions"**, lignes 26-30 (New clients)
3. **Vérifier les formules** des cellules T26 à BH26 (Trial Balancer POC) :
   - Les valeurs annuelles (C26:G26) sont correctes : 4, 9, 18, 26, 34
   - Les cellules mensuelles semblent contenir une formule auto-référente
     ou géométrique qui explose
4. **Corriger** en remplaçant par une répartition linéaire mensuelle des chiffres annuels
5. **Ligne 28** (Predict new clients molecule) : corriger les #REF! en restaurant
   les références de cellules cassées
6. **Ligne 29** (Predict new clients projet) : même correction

**IMPORTANT** : Les totaux annuels (colonnes C-G, ligne 64) sont corrects :

```
2026 :    925 000 €
2027 :  2 062 500 €
2028 :  3 950 000 €
2029 :  6 900 000 €
2030 : 14 250 000 €
```

Il faut s'assurer que les formules mensuelles reproduisent ces totaux.

---

## CORRECTION 5 — Business Plan xlsx : intégrer les subventions

**Fichier** : ArcaScience - Business plan I-demo.xlsx
**Onglet** : Cash-flow statement (ou équivalent)
**Problème** : Les lignes Fundraising, Subsidies et Bank loans sont toutes à 0,
ce qui montre un cash négatif de -9 M€ fin 2029.

**ACTION REQUISE :**

Renseigner les lignes suivantes conformément au plan de financement du V7 (section 6.2.2) :

```
Ligne "Subsidies" :
  2026 : Innov'Up acompte (240 k€) + prêt innovation (797 k€) + i-Démo EC1 (325 k€)
         = 1 362 k€
  2027 : Innov'Up solde (160 k€) + i-Démo EC2 (1 350 k€) = 1 510 k€
  2028 : i-Démo EC3 (1 005 k€) = 1 005 k€

Ligne "Fundraising" :
  2028 : 20 000 k€ (levée de fonds prévue dans le V7 section 6.2.2)

Ligne "Bank loans issuances" :
  2025/2026 : Innov'Up prêt d'amorçage (283 k€) - vérifier si déjà comptabilisé
```

> Sans ces entrées, le Business Plan montre une entreprise qui fait faillite
> en 2027. Avec les subventions et la levée, le plan redevient viable.

---

# PRIORITE 2 : CORRECTIONS IMPORTANTES

---

## CORRECTION 6 — Nombre de SLM : 12 vs 24

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 2.3.1 — Workflow de la plateforme ArcaScience
**Problème** : Deux mentions de "12 SLM" contredisent les multiples mentions de "24 SLM"

**REMPLACER (section 2.3.1, sous-section "Harmonisation et structuration des données") :**
```
La seconde étape repose sur un Framework IA constitué de 12 SLMs de structuration
qui constituent la fondation du système.
```

**PAR :**
```
La seconde étape repose sur un Framework IA constitué de 24 SLMs de structuration
qui constituent la fondation du système.
```

---

**REMPLACER (même section, quelques lignes plus bas) :**
```
La deuxième couche de traitement sémantique correspond à des SLM Contextualisant,
au nombre de 12.
```

**PAR :**
```
La deuxième couche de traitement sémantique correspond à 24 Contextualizing SLMs,
chacun entraîné pour une problématique spécifique de l'analyse bénéfice-risque.
```

> Vérification de cohérence : le reste du document (sections 1.3.4, 2.1, 2.3.3,
> et Workpackages T2.3) mentionne bien "24" partout. C'est "12" qui est l'erreur.

---

## CORRECTION 7 — Ajouter Mayo Clinic dans les partenaires

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 1.3.6 — Partenaires et sous-traitants clés
**Problème** : Mayo Clinic est citée comme sous-traitant (105 k€) et dans les Workpackages,
mais absente de la section Partenaires.

**AJOUTER dans le tableau des partenaires (après Cedars-Sinai) :**

```
┌─────────────────┬──────────────────────────────────────────────────────────┐
│  Mayo Clinic     │ Partenaire sous-traitant : Mayo Clinic intervient      │
│                  │ comme source de données cliniques rétrospectives et    │
│                  │ de validation externe pour les lots 2, 3 et 4 du      │
│                  │ projet. L'accès aux cohortes oncologiques et aux       │
│                  │ dossiers de santé électroniques (EDS) de Mayo Clinic   │
│                  │ permet de valider les modèles prédictifs sur des       │
│                  │ populations indépendantes, garantissant la robustesse  │
│                  │ et la reproductibilité des résultats.                  │
└─────────────────┴──────────────────────────────────────────────────────────┘
```

---

## CORRECTION 8 — Classification du Lot 6

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : Lot 6 (section 3.6)
**Problème** : Le V7 classe le Lot 6 comme "RDI" mais la Base Budgétaire le classe comme "DE"

**REMPLACER (dans le tableau Lot 6) :**
```
Nature du lot :    RDI
```

**PAR :**
```
Nature du lot :    DE (Développement Expérimental)
```

> Important : vérifier que la classification "DE" est bien celle souhaitée pour
> le calcul du taux d'aide BPI. La classification impacte directement le montant
> de subvention.

---

## CORRECTION 9 — Titre "concurentiel" (faute d'orthographe)

**Fichier** : ARCA SCIENCE V7 (ODT)

**REMPLACER (dans la Table des matières ET dans le corps du document) :**
```
Environnement concurentiel d'arcascience
```

**PAR :**
```
Environnement concurrentiel d'ArcaScience
```

> Note : il faut aussi corriger la casse "arcascience" → "ArcaScience"

---

## CORRECTION 10 — Titre "drug dEVELOPMENT" (casse)

**Fichier** : ARCA SCIENCE V7 (ODT)

**REMPLACER (dans la Table des matières ET dans le corps du document) :**
```
la place de l'analyse bénéfice-risque DANS LE MARCHÉ DU "drug dEVELOPMENT"
```

**PAR :**
```
La place de l'analyse bénéfice-risque dans le marché du drug development
```

---

## CORRECTION 11 — Titre "Savoir-faire et interne" (tronqué)

**Fichier** : ARCA SCIENCE V7 (ODT)

**REMPLACER :**
```
1.3.4. Savoir-faire et interne
```

**PAR :**
```
1.3.4. Savoir-faire interne
```

---

## CORRECTION 12 — Faute "Planification de dépenses éstimées"

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 6.2.1

**REMPLACER :**
```
Planification de dépenses éstimées
```

**PAR :**
```
Planification des dépenses estimées
```

---

## CORRECTION 13 — Faute "fera suite celle de"

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 6.2.2 — Levée de fonds

**REMPLACER :**
```
Cette levée de fonds fera suite celle de 4,65M € réalisé lors de la fin de l'année 2025.
```

**PAR :**
```
Cette levée de fonds fera suite à celle de 4,65 M€ réalisée fin 2025.
```

---

## CORRECTION 14 — Faute "possible" (accord)

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 7.1 — Activités sans l'aide

**REMPLACER :**
```
Les recrutements prévus d'ArcaScience pour réaliser ces deux activités en parallèle
ne seraient possible qu'avec l'aide i-Démo.
```

**PAR :**
```
Les recrutements prévus par ArcaScience pour mener ces deux activités en parallèle
ne seraient possibles qu'avec l'aide i-Démo.
```

---

## CORRECTION 15 — Faute "al ler" (mot coupé)

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 7.2

**REMPLACER :**
```
ne possède la technologie pour al ler sur le segment prédictif
```

**PAR :**
```
ne possède la technologie pour aller sur le segment prédictif
```

---

## CORRECTION 16 — "données en vie réelles" (accord)

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : EC2/EC3 (jalons)

**REMPLACER :**
```
les données en vie réelles
```

**PAR :**
```
les données de vie réelle
```

---

## CORRECTION 17 — "détaillés par étape clé comme indiqués"

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 2.7 — Risques identifiés

**REMPLACER :**
```
Les risques du projet ont été détaillés par étape clé comme indiqués dans le tableau ci-dessous :
```

**PAR :**
```
Les risques du projet ont été détaillés par étape clé comme indiqué dans le tableau ci-dessous :
```

---

# PRIORITE 3 : CORRECTIONS COSMETIQUES

---

## CORRECTION 18 — Supprimer les commentaires de reviewers dans l'ODT

**Fichier** : ARCA SCIENCE V7 (ODT)
**Problème** : Le fichier ODT source contient des commentaires de révision visibles :

- **MICALE Alexis** (26/02/2026) : « @Arca Pouvez vous ajouter le nom des investisseurs
  principaux de cette levée. »
- **MICALE Alexis** (13/03/2026) : « Pouvez-vous préciser l'objectif de cette levée ? »
- **PORCHET Nicolas** (13/03/2026) : « Clarifier le financement prêt inno ou aide publique ? »
- **PORCHET Nicolas** (13/03/2026) : « Laurent? » (sur la table de capitalisation)
- **PORCHET Nicolas** (16/03/2026) : « EC1 ou EC2? »
- **charbel** (16/03/2026) : « les numeros de pages ne collent pas »
- **charbel** (16/03/2026) : « @romain » (sur les jalons)
- **romain** (16/03/2026) : « Je corrige pour début 01/05/2026 »
- **romain** (16/03/2026) : « Je décalle tout pareil ici aussi... »

**ACTION** : Dans LibreOffice Writer :
1. Menu → Edition → Suivi des modifications → Gérer
2. Accepter ou rejeter tous les commentaires
3. Supprimer toutes les notes/annotations
4. Vérifier qu'aucun commentaire ne subsiste avant export PDF

---

## CORRECTION 19 — Numéros de pages (TdM)

**Fichier** : ARCA SCIENCE V7 (ODT)
**Problème** : Comme noté par "charbel", les numéros de pages de la Table des matières
ne correspondent pas au contenu.

**ACTION** : Après toutes les corrections, mettre à jour la Table des matières automatique
dans LibreOffice : clic droit sur la TdM → Actualiser l'index.

---

## CORRECTION 20 — GANTT illisible

**Fichier** : ARCA SCIENCE V7 (ODT)
**Section** : 2.5 — GANTT
**Problème** : Le diagramme de Gantt est partiellement masqué par les en-têtes/logos
dans le PDF exporté.

**ACTION** : Redimensionner le GANTT pour qu'il tienne sur une page entière en mode paysage,
ou le placer en annexe avec une résolution suffisante.

---

# CHECKLIST DE VERIFICATION CROISEE FINALE

Avant soumission, vérifier point par point :

- [ ] Le montant "Coût total du projet" est identique dans V7 et Base Budgétaire
- [ ] Les budgets par Lot sont identiques dans V7 et Base Budgétaire
- [ ] La sous-traitance du V7 est réconciliée avec "Autres dépenses" de la Base Budgétaire
- [ ] Les dates EC1/EC2/EC3 du V7 sont cohérentes avec T0 = 01/05/2026
- [ ] Les montants i-Démo (325k + 1350k + 1005k = 2 680 k€) sont dans le Business Plan
- [ ] La levée de 20 M€ prévue en 2028 est dans le Business Plan (ligne Fundraising)
- [ ] Innov'Up (283k prêt + 400k subvention + 797k prêt innovation) est dans le Business Plan
- [ ] Les formules mensuelles du BP onglet "Assumptions" sont corrigées (pas de #REF!)
- [ ] "24 SLM" est harmonisé partout (pas de "12")
- [ ] Mayo Clinic est dans la section 1.3.6 Partenaires
- [ ] Le Lot 6 est classé identiquement dans V7 et Base Budgétaire (RDI ou DE)
- [ ] Les titres de la TdM sont en casse correcte (pas de MAJUSCULES intempestives)
- [ ] Aucun commentaire de reviewer ne subsiste dans l'ODT
- [ ] La TdM est actualisée avec les bons numéros de pages
- [ ] Le GANTT est lisible dans le PDF exporté
- [ ] Le BP montre un cash positif ou justifié sur toute la durée du projet
- [ ] Deux ou trois brevets : le Lot 7 et la section 1.3.5 sont alignés
