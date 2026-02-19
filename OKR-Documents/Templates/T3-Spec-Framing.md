# T3 — Spec Framing Template

> Use this template before any engineering, data, or clinical work begins. A spec is the contract between the requester and the builder. No spec = no start.

---

## Spec Identity

| Field | Value |
|---|---|
| **Spec Title** | _[Clear, descriptive title]_ |
| **Spec ID** | SPEC-O[1/2/3]-[sequential#] (e.g., SPEC-O1-012) |
| **Author** | _[Name]_ |
| **Reviewer(s)** | _[Name(s)]_ |
| **Created** | _[YYYY-MM-DD]_ |
| **Last Updated** | _[YYYY-MM-DD]_ |
| **Status** | Draft / In Review / Approved / In Progress / Done |

---

## OKR Alignment

| Field | Value |
|---|---|
| **Objective** | O1 / O2 / O3 |
| **Key Result(s)** | KR _[X.X]_ |
| **KR Metric Moved** | _[Which metric and by how much]_ |
| **12-Week Phase** | Wk _[X-Y]_ — _[Phase name]_ |
| **Owner Checklist Reference** | _[C2 checklist item this maps to]_ |

---

## Problem Statement

### What is the problem?
_[2-3 sentences. Be specific. Quantify the pain.]_

### Who experiences this problem?
_[User persona: Regulatory affairs team / Clinical team / Data team / End user on platform]_

### What happens if we don't solve it?
_[Impact on KR, revenue, credibility, or user experience]_

---

## Proposed Solution

### Summary (1 paragraph)
_[What we are building and how it solves the problem]_

### Approach

| Component | Description |
|---|---|
| **Frontend / UX** | _[What changes in the UI]_ |
| **Backend / API** | _[What changes in the services]_ |
| **Data Pipeline** | _[What changes in the BRA pipeline: Context / B&R Assessment / Data Analysis]_ |
| **Infrastructure** | _[What changes in DevOps / hosting / monitoring]_ |
| **Clinical / Medical** | _[What changes in validation, datasets, or medical logic]_ |

### What is explicitly OUT of scope?
- _[Item 1]_
- _[Item 2]_
- _[Item 3]_

---

## Acceptance Criteria

| # | Criterion | Measurable? | Verification Method |
|---|---|---|---|
| 1 | _[Description]_ | _[Y/N — metric]_ | _[How we verify]_ |
| 2 | _[Description]_ | _[Y/N — metric]_ | _[How we verify]_ |
| 3 | _[Description]_ | _[Y/N — metric]_ | _[How we verify]_ |
| 4 | _[Description]_ | _[Y/N — metric]_ | _[How we verify]_ |

---

## Definition of Done (O1 Gate)

If this spec is under O1, all six criteria must be met:

- [ ] **Data Quality Validation** — Output validated by medical team with representative panel
- [ ] **Data Traceability** — Intermediate stages generate auditable output
- [ ] **Platform Usage Analysis** — App instrumented for usage analysis
- [ ] **Platform Perf Monitoring** — Performance monitoring active
- [ ] **Code Quality Gate** — Passes SonarQube Quality Gate
- [ ] **80% Code Tested** — Coverage minimum met + UI test cases

If this spec is under O2, the per-axis Definition of Done applies:

- [ ] **Dataset Structured** (KR2.1)
- [ ] **External Validation** (KR2.2)
- [ ] **Internal Validation** (KR2.2)
- [ ] **LLM Validation** (KR2.2)
- [ ] **Integrated in Platform** (KR2.3)
- [ ] **Demo Ready** (KR2.3)

---

## Dependencies

| Dependency | Type | Owner | Status | Risk if Late |
|---|---|---|---|---|
| _[Description]_ | Blocks / Blocked-by / Informs | _[Name]_ | _[Open/Resolved]_ | _[Impact]_ |
| _[Description]_ | Blocks / Blocked-by / Informs | _[Name]_ | _[Open/Resolved]_ | _[Impact]_ |

### Cross-OKR Dependencies

| This Spec (O[X]) | Depends On / Enables | Other OKR Item |
|---|---|---|
| _[This deliverable]_ | _[depends on / enables]_ | _[O[Y] KR[Y.X] — description]_ |

---

## Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| _[Description]_ | High / Med / Low | High / Med / Low | _[What we do]_ |
| _[Description]_ | High / Med / Low | High / Med / Low | _[What we do]_ |

Reference the A7 Risk Matrix for quarter-level risks that may apply.

---

## Technical Design (Optional — for engineering specs)

### Architecture Diagram
_[Insert or link to diagram]_

### Data Flow
_[Input → Processing → Output]_

### API Changes
| Endpoint | Method | Change Type | Description |
|---|---|---|---|
| _[/path]_ | _[GET/POST/PUT/DELETE]_ | _[New/Modified/Deprecated]_ | _[What changes]_ |

### Database Changes
| Table/Collection | Change Type | Description |
|---|---|---|
| _[Name]_ | _[New/Modified/Deprecated]_ | _[What changes]_ |

---

## Validation Plan

### How will we know this works?

| Validation Type | Method | Dataset / Scenario | Pass Criteria |
|---|---|---|---|
| Unit Tests | _[Automated]_ | _[Coverage target]_ | 80%+ coverage |
| Integration Tests | _[Automated]_ | _[Scenarios]_ | All pass |
| Clinical Validation | _[Manual — Vassili]_ | _[Reference dataset]_ | _[F1 / accuracy target]_ |
| User Acceptance | _[Manual — Charbel]_ | _[User scenarios]_ | _[Acceptance criteria met]_ |

---

## Milestones

| Milestone | Description | Target Date | Status |
|---|---|---|---|
| M1 | _[First checkpoint]_ | _[YYYY-MM-DD]_ | _[Not started / In progress / Done]_ |
| M2 | _[Second checkpoint]_ | _[YYYY-MM-DD]_ | _[Not started / In progress / Done]_ |
| M3 | _[Delivery]_ | _[YYYY-MM-DD]_ | _[Not started / In progress / Done]_ |

---

## Sign-Off

| Role | Name | Approved? | Date |
|---|---|---|---|
| Product Lead | Charbel | _[Y/N]_ | _[Date]_ |
| CTO / Eng Lead | Jeff | _[Y/N]_ | _[Date]_ |
| Clinical Lead | Vassili | _[Y/N]_ | _[Date]_ |
| CEO | _[Name]_ | _[Y/N]_ | _[Date]_ |

---

*Template based on ArcaScience OKR Execution Blueprint*
