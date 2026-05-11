# O2 — Launch i-Demo on Chemical Analysis

> *Public launch of the i-Demo product extended to chemical analysis (compound-level / ADMET / mechanism / bioactivity integration), with a live demo asset, official launch event/announcement, and the chemical-analysis module callable from the BRA platform.*

**Owners:** **Vassili** (Clinical/Chem Lead) | **Charbel** (Product Lead)

**Weekly Ritual:**
- **Every Wednesday — 30 min:** "Chemical Analysis Standup": module development progress, validation status, launch prep, blockers (Vassili + Charbel + Jeff + Data-Team)

---

## KR 2.1 — Chemical-Analysis Pipeline Deployed & Callable from BRA Platform

| Metric | Current | Target | Owner |
|---|---|---|---|
| Chemical-analysis module deployed in Prod | TBD — owner to fill Wk1 | Deployed & API-callable | Data-Team + App-Team |
| Module callable from BRA platform | TBD — owner to fill Wk1 | Yes — integrated in BRA workflow | Charbel + Jeff |
| Module scope coverage (5 sub-modules) | 0/5 | 5/5 | Data-Team |

### Chemical-Analysis Module — Scope & Sub-Modules

| Sub-Module | Description | Integration Point in BRA | Owner |
|---|---|---|---|
| **Compound Search** | Search by compound name, SMILES, InChI; return structure, properties, classification | Context step — enriches therapeutic options with compound data | Data-Team |
| **ADMET Prediction** | Absorption, Distribution, Metabolism, Excretion, Toxicity profiling | B&R Assessment — feeds safety/risk scoring | Data-Team |
| **Mechanism of Action** | Drug-target interaction, pathway mapping, pharmacodynamics | Context + B&R Assessment — explains therapeutic rationale | Data-Team |
| **Bioactivity Analysis** | IC50/EC50, dose-response, selectivity profiling | Data Analysis — quantitative evidence layer | Data-Team |
| **Drug-Target Binding** | Binding affinity, off-target predictions, structural docking | Decision-Support — risk/benefit trade-off inputs | Data-Team |

---

## KR 2.2 — ≥ 3 Validated Case Studies

| Metric | Current | Target | Owner |
|---|---|---|---|
| Case studies validated — external (KOL/client review) | 0 | ≥ 3 | Vassili |
| Case studies validated — internal (team review) | 0 | ≥ 3 | Data-Team |
| Case studies validated — LLM (automated validation) | 0 | ≥ 3 | Data-Team |

### Validation Approach (mirrors OKR1 KR 2.2 pattern)

**External Validation:**
- Identification and contact of 3–5 relevant KOLs / early-access clients
- Structured questionnaire per case study output
- Analysis of results as % data validated
- Integrate 100 % of feedback to improve outputs

**Internal Validation:**
- Generation of reference test datasets (known compounds)
- Creation of test requirements per sub-module
- Annotation of expected results
- Analysis of results as % data validated

**LLM Validation:**
- Creation and validation of test prompts
- Automated test execution across case studies
- Analysis of results as % data validated
- Comparison with internal + external results

### Case Study Tracker

| Case Study | Compound / Drug | Therapeutic Area | External Val. | Internal Val. | LLM Val. | Demo-Ready | Status |
|---|---|---|---|---|---|---|---|
| CS-1 — TBD | TBD — owner to fill Wk1 | TBD | [ ] | [ ] | [ ] | [ ] | __ % done |
| CS-2 — TBD | TBD — owner to fill Wk1 | TBD | [ ] | [ ] | [ ] | [ ] | __ % done |
| CS-3 — TBD | TBD — owner to fill Wk1 | TBD | [ ] | [ ] | [ ] | [ ] | __ % done |

---

## KR 2.3 — i-Demo Launch Event Executed

| Metric | Current | Target | Owner |
|---|---|---|---|
| Launch event executed | No | Yes — date set, executed | Vassili + CEO |
| Launch announcement published (LinkedIn, press, website) | No | Yes | CEO |
| Demo asset live and shareable | No | Yes — public URL | Charbel |
| Partner activations (co-announcements) | 0 | ≥ 1 | CEO |

---

## KR 2.4 — ≥ 50 Qualified Leads Captured

| Metric | Current | Target | Owner |
|---|---|---|---|
| Qualified leads captured (post-launch) | 0 | ≥ 50 | CEO |
| Demo requests received | 0 | ≥ 20 | CEO |
| Leads passed to pipeline (S0+) | 0 | ≥ 10 | CEO |

---

## Definition of Done (O2 — per Case Study)

A case study is **done** when all six criteria are satisfied:

| # | Criterion | KR |
|---|---|---|
| 1 | **Chemical-analysis pipeline runs end-to-end for this compound** | KR2.1 |
| 2 | **External Validation passed** | KR2.2 |
| 3 | **Internal Validation passed** | KR2.2 |
| 4 | **LLM Validation passed** | KR2.2 |
| 5 | **Integrated in BRA platform and callable** | KR2.1 |
| 6 | **Demo-ready: scripted walkthrough with compelling narrative** | KR2.3 |

---

## O2 — Weekly Scorecard (B1)

| KR | Metric | Owner | Weekly KPI | Wk1 | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| KR2.1a | Chem sub-modules deployed | Data-Team | Modules shipped (cumulative) | | | | | | | 5/5 |
| KR2.1b | Module callable from BRA | Charbel + Jeff | Integrated Y/N | | | | | | | Yes |
| KR2.2a | Case studies validated — external | Vassili | Validations completed | | | | | | | ≥ 3 |
| KR2.2b | Case studies validated — internal | Data-Team | Validations completed | | | | | | | ≥ 3 |
| KR2.2c | Case studies validated — LLM | Data-Team | Validations completed | | | | | | | ≥ 3 |
| KR2.3 | Launch event | Vassili + CEO | Executed Y/N | | | | | | | Yes |
| KR2.4 | Qualified leads captured | CEO | Count | | | | | | | ≥ 50 |

---

## O2 Red Flags — Check Weekly

- [ ] ≥ 2 sub-modules deployed by Wk2? (If not → scope cut to 3 core sub-modules)
- [ ] All 5 sub-modules deployed by Wk3? (If not → Jeff escalation)
- [ ] ≥ 1 case study fully validated by Wk4? (If not → Vassili sprint)
- [ ] Launch event date confirmed by Wk2? (If not → CEO to force-schedule)
- [ ] Demo asset functional by Wk3? (If not → Charbel war room)
- [ ] Lead capture mechanism live by Wk4? (If not → launch at risk)

---

## Cross-References

See also: [A2-Value-Chain](../Part-A-Present/A2-Value-Chain.md) | [B6-iDemo-Launch-Tracker](../Part-B-Track/B6-iDemo-Launch-Tracker.md) | [C4-Chemical-Analysis-Monetization-Playbook](../Part-C-Execute/C4-Chemical-Analysis-Monetization-Playbook.md) | [C9-iDemo-Launch-Runbook](../Part-C-Execute/C9-iDemo-Launch-Runbook.md) | [Appendix-D-iDemo-Chemical-Analysis-Spec](../Appendix/Appendix-D-iDemo-Chemical-Analysis-Spec.md)

---

*ArcaScience OKR2 Execution Blueprint — O2 Strategy*
