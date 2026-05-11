# O1 — Finalize the BRA Platform End-to-End

> *All BRA pipeline steps (Context, Benefit & Risk Assessment, Data Analysis, Reporting, Decision-Support) fully developed, productionized, and observable — from prototype to production-grade in 6 weeks.*

**Owners:** **Charbel** (Product Lead — Workflow & UX) | **Jeff** (CTO/Eng Lead — Reliability & Infra) | **Vassili** (Clinical/Medical Lead — Benefit-Risk & Validation)

**Weekly Ritual:**
- **Every day — 30 min:** "BRA OKR Scoreboard" review: time-to-output, insights, acceptance, bugs, uptime
- **Every Thursday — 60 min:** "Fixing" session: credibility, noise, calibration — maintains quality while moving fast

---

## KR 1.1 — 100 % of Platform Steps Live in Production

| Metric | Current | Target | Owner |
|---|---|---|---|
| BRA pipeline steps fully deployed in Prod | TBD — owner to fill Wk1 | 5/5 (Context, B&R Assessment, Data Analysis, Reporting, Decision-Support) | App-Team + Data-Team |
| End-to-end BRA run completable without manual hand-off | TBD — owner to fill Wk1 | Yes — fully automated pipeline | Charbel + Jeff |

### Pipeline Steps — Status Tracker

| Step | Status (Wk1) | Target (Wk2) | Owner |
|---|---|---|---|
| 1 — Context | TBD — owner to fill Wk1 | Production-ready | Data-Team |
| 2 — Benefit & Risk Assessment | TBD — owner to fill Wk1 | Production-ready | Data-Team |
| 3 — Data Analysis | TBD — owner to fill Wk1 | Production-ready | Data-Team |
| 4 — Reporting | TBD — owner to fill Wk1 | Production-ready | Data-Team + App-Team |
| 5 — Decision-Support | TBD — owner to fill Wk1 | Production-ready | Data-Team + App-Team |

---

## KR 1.2 — F1 ≥ 90 % on Safety & Efficacy Extraction

| Metric | Current | Target | Owner |
|---|---|---|---|
| F1 on Risk/Safety endpoints (ref dataset) | TBD — owner to fill Wk1 | ≥ 90 % | Data-Team |
| F1 on Efficacy endpoints (ref dataset) | TBD — owner to fill Wk1 | ≥ 90 % | Data-Team |
| Validation dataset size | TBD — owner to fill Wk1 | ≥ 20 studies | Vassili |

---

## KR 1.3 — < 1 h Human Work per Full BRA

| Metric | Current | Target | Owner |
|---|---|---|---|
| Human work for full BRA (Context → Decision-Support) | TBD — owner to fill Wk1 | < 1 h | Data-Team + App-Team |
| Human work — Context step | TBD — owner to fill Wk1 | < 15 min | Data-Team |
| Human work — B&R Assessment step | TBD — owner to fill Wk1 | < 15 min | Data-Team |
| Human work — Data Analysis step | TBD — owner to fill Wk1 | < 15 min | Data-Team |
| Human work — Reporting step | TBD — owner to fill Wk1 | < 10 min | App-Team |
| Human work — Decision-Support step | TBD — owner to fill Wk1 | < 5 min | App-Team |

---

## KR 1.4 — 99.5 % Platform Availability

| Metric | Current | Target | Owner |
|---|---|---|---|
| Platform availability (trailing 7d) | TBD — owner to fill Wk1 | 99.5 % | Devops-Team |
| Code tested (Webapp + API) | TBD — owner to fill Wk1 | ≥ 85 % | App-Team + Data-Team |
| Critical / Major bugs in Prod | TBD — owner to fill Wk1 | 0 | App-Team + Data-Team |
| Ship time to Prod | TBD — owner to fill Wk1 | < 10 min | Devops-Team |
| APM data coverage | TBD — owner to fill Wk1 | 100 % | Devops-Team |

---

## Definition of Done (O1)

All O1 deliverables must satisfy these seven criteria:

| # | Criterion | Description |
|---|---|---|
| 1 | **Data Quality Validation** | Each data output validated by medical team with representative panel of tests |
| 2 | **Data Traceability** | Each intermediate stage generates fully auditable output |
| 3 | **Platform Usage Analysis** | App instrumented for usage analysis |
| 4 | **Platform Perf Monitoring** | APM active on every pipeline step |
| 5 | **Code Quality Gate** | Passes SonarQube Quality Gate |
| 6 | **85 % Code Tested** | 85 % code coverage minimum + UI test cases |
| 7 | **End-to-End Smoke Test** | Full BRA pipeline runs unattended on 3 reference drugs without error |

---

## O1 — Weekly Scorecard (B1)

| KR | Metric | Owner | Weekly KPI | Wk1 | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| KR1.1 | Pipeline steps in Prod | App/Data-Team | Steps shipped (cumulative) | | | | | | | 5/5 |
| KR1.2a | F1 Risk/Safety | Data-Team | F1 score | | | | | | | ≥ 90 % |
| KR1.2b | F1 Efficacy | Data-Team | F1 score | | | | | | | ≥ 90 % |
| KR1.3 | Human work per full BRA | Data/App-Team | Hours | | | | | | | < 1 h |
| KR1.4a | Platform availability | Devops-Team | Trailing 7d uptime % | | | | | | | 99.5 % |
| KR1.4b | Code tested | App/Data-Team | Coverage % | | | | | | | ≥ 85 % |
| KR1.4c | Critical/Major bugs | App/Data-Team | Count | | | | | | | 0 |
| KR1.4d | Ship time to Prod | Devops-Team | Minutes | | | | | | | < 10 min |
| KR1.4e | APM data coverage | Devops-Team | % available | | | | | | | 100 % |

---

## O1 Red Flags — Check Weekly

- [ ] All 5 pipeline steps at least in staging by Wk2? (If not → scope review with Charbel + Jeff)
- [ ] F1 ≥ 80 % by Wk3? (If not → calibration sprint)
- [ ] Human work per BRA < 2 h by Wk3? (If not → automation sprint)
- [ ] Uptime > 98 % in any rolling week? (If not → war room)
- [ ] End-to-end smoke test passing by Wk4? (If not → Charbel + Jeff escalation)
- [ ] Reporting + Decision-Support steps in Prod by Wk4? (If not → scope cut)

---

## Cross-References

See also: [A2-Value-Chain](../Part-A-Present/A2-Value-Chain.md) | [B1-Master-OKR-Scorecard](../Part-B-Track/B1-Master-OKR-Scorecard.md) | [C2-Owner-Checklists](../Part-C-Execute/C2-Owner-Checklists.md) | [C8-6-Week-Execution-Timeline](../Part-C-Execute/C8-6-Week-Execution-Timeline.md)

---

*ArcaScience OKR2 Execution Blueprint — O1 Strategy*
