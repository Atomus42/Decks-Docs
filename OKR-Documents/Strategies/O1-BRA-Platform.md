# O1 — Make the BRA Platform the Reference Way to Do Benefit-Risk

> *Deliver the V1 of the BRA-Platform validated by real client usage, with a fully operational BRA pipeline (Context, Benefit & Risk Assessment, Data Analysis), production-grade reliability, and complete observability.*

**Owners:** Charbel (Product Lead — Workflow & UX) | Jeff (CTO/Eng Lead — Reliability & Infra) | Vassili (Clinical Lead — Benefit-Risk & Validation)

**Weekly Ritual:**
- **Every day — 30 min:** "BRA OKR Scoreboard" review: time-to-output, insights, acceptance, bugs, uptime
- **Every Thursday — 60 min:** "Fixing" session: credibility, noise, calibration — maintains quality while moving fast

---

## KR 1.1 — Deliver the V1 of the BRA-Platform validated by real client usage

| Metric | Current | Target | Owner |
|---|---|---|---|
| Main epics deployed and usable in Production | 1 | 5 | App-Team |
| Users from companies using the platform | 0 users from 0 companies | 10-50 users from 1-5 companies | App-Team, Sales-Team |

---

## KR 1.2 — BRA Step 1: "Context" up and running

| Metric | Current | Target | Owner |
|---|---|---|---|
| Completeness of "alternative T. options" validated on a set of 10 known studies | 0 | >= 90% | Data-Team |
| Human work for Therapeutic option | 0 | < 4h | Data-Team |
| Study details V1 | 0 | Delivered | Data-Team |

---

## KR 1.3 — BRA Step 2: "Benefit & Risk Assessment" up and running

| Metric | Current | Target | Owner |
|---|---|---|---|
| F1 on Risk/Safety endpoints pipeline for drug and comparator on a ref dataset | 0% | >= 85% | Data-Team |
| F1 on Efficacy endpoints data extraction | 0% | >= 85% | Data-Team |
| Human work for this step | 0 | < 4h | Data-Team |

---

## KR 1.4 — BRA Step 3: "Data Analysis" up and running

| Metric | Current | Target | Owner |
|---|---|---|---|
| V0 implemented | 0 | Delivered | Data-Team |
| Human work for this step | 0 | < 48h | Data-Team |

---

## KR 1.5 — Reliability

| Metric | Current | Target | Owner |
|---|---|---|---|
| Code tested (Webapp + API) | 80% | 80% | App-Team, Data-Team |
| Critical / Major bugs in Prod | 0 | 0 | App-Team, Data-Team |
| Availability of Platform and Services | 95% | 99% | Devops-Team |
| Time to ship any modification in Prod | 30 min | 10 min | Devops-Team |
| APM data available (User actions, Errors, Treatment time, Cost) | 0% | 100% | Devops-Team |

---

## Definition of Done

All O1 deliverables must satisfy these six criteria:

| Criterion | Description |
|---|---|
| **Data Quality Validation** | Each data output is validated by the medical team with a representative panel of tests |
| **Data Traceability** | Each intermediate stage of the BRA pipeline generates fully auditable output |
| **Platform Usage Analysis** | The App is instrumented in order to be able to analyse platform usage |
| **Platform Perf Monitoring** | Each intermediate stage of the BRA pipeline generates fully auditable output |
| **Code Quality Gate** | Each new version of code delivered in Prod has to pass the SonarQube Quality Gate |
| **80% Code Tested** | 80% code coverage minimum mandatory and test cases for UI validation |

---

## O1 — Weekly Scorecard (B1)

| KR | Metric | Owner | Weekly KPI | Wk1 | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Wk7 | Wk8 | Wk9 | Wk10 | Wk11 | Wk12 | Target |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KR1.1a | Main epics deployed in Prod | App-Team | Epics shipped (cumulative) | | | | | | | | | | | | | 5 |
| KR1.1b | Users on platform | App-Team, Sales | Active users / companies | | | | | | | | | | | | | 10-50 users / 1-5 co. |
| KR1.2a | "Context" — Alt. T. options completeness | Data-Team | % validated on 10 studies | | | | | | | | | | | | | >= 90% |
| KR1.2b | "Context" — Human work | Data-Team | Hours per therapeutic option | | | | | | | | | | | | | < 4h |
| KR1.3a | "B&R Assessment" — F1 Risk/Safety | Data-Team | F1 score | | | | | | | | | | | | | >= 85% |
| KR1.3b | "B&R Assessment" — F1 Efficacy | Data-Team | F1 score | | | | | | | | | | | | | >= 85% |
| KR1.3c | "B&R Assessment" — Human work | Data-Team | Hours per step | | | | | | | | | | | | | < 4h |
| KR1.4a | "Data Analysis" — V0 | Data-Team | Shipped Y/N | | | | | | | | | | | | | Delivered |
| KR1.4b | "Data Analysis" — Human work | Data-Team | Hours per step | | | | | | | | | | | | | < 48h |
| KR1.5a | Code tested (Webapp + API) | App/Data-Team | Coverage % | | | | | | | | | | | | | 80% |
| KR1.5b | Critical/Major bugs in Prod | App/Data-Team | Count | | | | | | | | | | | | | 0 |
| KR1.5c | Platform availability | Devops-Team | Trailing 7d uptime % | | | | | | | | | | | | | 99% |
| KR1.5d | Ship time to Prod | Devops-Team | Minutes | | | | | | | | | | | | | 10 min |
| KR1.5e | APM data coverage | Devops-Team | % available | | | | | | | | | | | | | 100% |

---

## O1 Red Flags — Check Weekly

- [ ] Epics shipping on cadence? (If <2 by Week 4 → escalate to Charbel + Jeff)
- [ ] "Context" completeness improving? (If <50% by Week 4 → Data-Team sprint)
- [ ] F1 scores on B&R Assessment improving? (If <50% by Week 6 → calibration sprint)
- [ ] Uptime >95%? (If not in any 2-week window → war room)
- [ ] Active users >0 by Week 6? (If not → activation audit)
- [ ] APM data instrumentation started? (If 0% by Week 4 → Devops escalation)

---

## Cross-References

See also: [A2-Value-Chain](../Part-A-Present/A2-Value-Chain.md) | [B1-Master-OKR-Scorecard](../Part-B-Track/B1-Master-OKR-Scorecard.md) | [C2-Owner-Checklists](../Part-C-Execute/C2-Owner-Checklists.md) | [C8-12-Week-Timeline](../Part-C-Execute/C8-12-Week-Execution-Timeline.md)

---

*Extracted from ArcaScience OKR Execution Blueprint — O1 Strategy*
