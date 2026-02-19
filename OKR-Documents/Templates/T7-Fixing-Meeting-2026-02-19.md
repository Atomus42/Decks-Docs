# Fixing Meeting — Thursday 19 February 2026

## All Objectives: O1 / O2 / O3

**Duration:** 60 min
**Attendees:** Vassili + Charbel (core) | Jeff, CEO (as needed for O2/O3 items)
**Purpose:** Credibility, noise, calibration — maintain quality while moving fast. Today's session covers all three objectives.

---

## Pre-Meeting Prep Checklist

Before the meeting starts, each person must have ready:

- [ ] **Vassili:** Top 3 data quality / credibility issues from the week
- [ ] **Vassili:** Updated KR1.2 (Context) and KR1.3 (B&R Assessment) metrics
- [ ] **Vassili:** Updated KR2.1 / KR2.2 status (dataset + validation progress)
- [ ] **Charbel:** Top 3 UX / workflow issues from user feedback or testing
- [ ] **Charbel:** Updated KR1.1 (epics deployed, user count)
- [ ] **Jeff:** Current KR1.5 metrics (coverage, bugs, uptime, ship time, APM)
- [ ] **CEO:** Pipeline snapshot and any sales-side quality concerns

---

## PART 1: O1 — BRA Platform Quality (25 min)

### 1A. Credibility Check (10 min)

> Are the BRA outputs trustworthy this week?

| Pipeline Step | Quality Issue | Severity | Action |
|---|---|---|---|
| **Context** (KR1.2) | | | |
| Alt. T. options completeness | Current: ___%  (target: >= 90%) | _[Crit/High/Med/Low]_ | _[Fix / Investigate / Accept]_ |
| Human work per option | Current: ___h (target: < 4h) | _[Crit/High/Med/Low]_ | _[Fix / Investigate / Accept]_ |
| Study details V1 | Status: _[Delivered / In progress / Blocked]_ | | |
| Issue 1: | ___ | | |
| Issue 2: | ___ | | |
| **B&R Assessment** (KR1.3) | | | |
| F1 Risk/Safety endpoints | Current: ___% (target: >= 85%) | _[Crit/High/Med/Low]_ | _[Fix / Investigate / Accept]_ |
| F1 Efficacy endpoints | Current: ___% (target: >= 85%) | _[Crit/High/Med/Low]_ | _[Fix / Investigate / Accept]_ |
| Human work per step | Current: ___h (target: < 4h) | _[Crit/High/Med/Low]_ | _[Fix / Investigate / Accept]_ |
| Issue 1: | ___ | | |
| Issue 2: | ___ | | |
| **Data Analysis** (KR1.4) | | | |
| V0 status | _[Delivered / In progress / Blocked]_ | | |
| Human work | Current: ___h (target: < 48h) | | |

### 1B. Noise Reduction (8 min)

> Are we generating false positives, irrelevant outputs, or confusing results?

| Item | Description | Impact | Root Cause | Fix |
|---|---|---|---|---|
| 1 | ___ | _[Users confused / Wrong output / Wasted time]_ | ___ | ___ |
| 2 | ___ | _[Users confused / Wrong output / Wasted time]_ | ___ | ___ |
| 3 | ___ | _[Users confused / Wrong output / Wasted time]_ | ___ | ___ |

**F1 Score Trend:**

| Metric | Last Week | This Week | Delta | Direction |
|---|---|---|---|---|
| F1 Risk/Safety | ___% | ___% | ___ | Better / Same / Worse |
| F1 Efficacy | ___% | ___% | ___ | Better / Same / Worse |

**Precision vs Recall trade-off decisions:**
- _[Decision 1: ___]_
- _[Decision 2: ___]_

### 1C. Calibration (7 min)

> Are we producing outputs a regulator would trust?

| Test | Reference | Expected | Actual | Pass? |
|---|---|---|---|---|
| _[Endpoint / study]_ | _[Gold standard dataset]_ | _[Value]_ | _[Value]_ | _[Y/N]_ |
| _[Endpoint / study]_ | _[Gold standard dataset]_ | _[Value]_ | _[Value]_ | _[Y/N]_ |
| _[Endpoint / study]_ | _[Gold standard dataset]_ | _[Value]_ | _[Value]_ | _[Y/N]_ |

**Manual review findings:**
1. ___
2. ___

### 1D. Reliability Quick Check

| KR1.5 Metric | Value | Target | Status |
|---|---|---|---|
| Code coverage | ___% | 80% | On track / At risk / Behind |
| Critical/Major bugs | ___ | 0 | On track / At risk / Behind |
| Platform availability | ___% | 99% | On track / At risk / Behind |
| Ship time | ___ min | 10 min | On track / At risk / Behind |
| APM data coverage | ___% | 100% | On track / At risk / Behind |

---

## PART 2: O2 — Disease-Specific Platform Quality (20 min)

### 2A. Therapeutic Axis Progress

| Axis | Dataset (KR2.1) | Ext. Validation (KR2.2) | Int. Validation (KR2.2) | LLM Validation (KR2.2) | Platform (KR2.3) | Demo (KR2.3) | Status |
|---|---|---|---|---|---|---|---|
| Axis 1: _[Name]_ | ___% | ___ / 4 | ___ / 4 | ___ / 4 | ___% | _[Y/N]_ | _[On track / At risk / Behind]_ |
| Axis 2: _[Name]_ | ___% | ___ / 4 | ___ / 4 | ___ / 4 | ___% | _[Y/N]_ | _[On track / At risk / Behind]_ |
| Axis 3 (stretch): _[Name]_ | ___% | ___ / 4 | ___ / 4 | ___ / 4 | ___% | _[Y/N]_ | _[Go / No-go / TBD]_ |

### 2B. Dataset Quality Issues

| Axis | Issue | Type | Severity | Fix Needed |
|---|---|---|---|---|
| _[1/2/3]_ | ___ | _[Data gap / Quality / Scope]_ | _[Crit/High/Med]_ | ___ |
| _[1/2/3]_ | ___ | _[Data gap / Quality / Scope]_ | _[Crit/High/Med]_ | ___ |

### 2C. Validation Progress & Quality

**External Validation (KOLs):**
| KOL | Axis | Scheduled? | Completed? | Key Feedback | Integrated? |
|---|---|---|---|---|---|
| _[Name]_ | _[1/2]_ | _[Y/N]_ | _[Y/N]_ | ___ | _[Y/N]_ |
| _[Name]_ | _[1/2]_ | _[Y/N]_ | _[Y/N]_ | ___ | _[Y/N]_ |

**Internal Validation:**
| Test Dataset | Created? | Annotated? | Results | Feedback Integrated? |
|---|---|---|---|---|
| _[Name]_ | _[Y/N]_ | _[Y/N]_ | ___%  validated | _[Y/N]_ |

**LLM Validation:**
| Prompt | Validated? | Test Executed? | Results | Feedback Integrated? |
|---|---|---|---|---|
| _[Name]_ | _[Y/N]_ | _[Y/N]_ | ___% validated | _[Y/N]_ |

### 2D. O2 Red Flag Check

- [ ] Benchmark of 10 axes completed? (If not by Wk 2 → escalate)
- [ ] 2-3 axes selected? (If not by Wk 3 → escalate)
- [ ] Gap analysis completed? (If not by Wk 4 → escalate)
- [ ] First dataset structured? (If not by Wk 7 → escalate)
- [ ] KOL contacts initiated? (If not by Wk 5 → escalate)
- [ ] At least 1 functional demo ready? (If not by Wk 10 → escalate)

**Red flags triggered today:** _[None / List them]_

---

## PART 3: O3 — Revenue Quality & Pipeline Health (10 min)

### 3A. Pipeline Snapshot

| Metric | Value | Target | Gap |
|---|---|---|---|
| ARR closed (cumulative) | $___k | $500k | $___k |
| New logos signed | ___ | 5 | ___ |
| Expansions closed | ___ | 1 | ___ |
| Pipeline $ (qualified) | $___k | $1.5M (3x) | $___k |
| Win rate | ___% | 25% | ___% |
| Avg sales cycle | ___ days | <60 days | ___ days |
| CEO revenue hours (this week) | ___h | 12-15h | ___h |

### 3B. Sales-Side Quality Issues

> Are quality or credibility issues impacting sales?

| Issue | Source | Impact on Sales | Fix Owner | Priority |
|---|---|---|---|---|
| ___ | _[Demo / Output / Data]_ | _[Lost deal / Delayed / Concern raised]_ | _[Name]_ | _[P1/P2/P3]_ |
| ___ | _[Demo / Output / Data]_ | _[Lost deal / Delayed / Concern raised]_ | _[Name]_ | _[P1/P2/P3]_ |

### 3C. Demo Readiness

| Demo Component | Status | Issues | Fix By |
|---|---|---|---|
| BRA Platform Demo (generic) | _[Ready / Needs work / Broken]_ | ___ | _[Date]_ |
| Disease-Specific Demo (Axis 1) | _[Ready / Needs work / Not started]_ | ___ | _[Date]_ |
| Disease-Specific Demo (Axis 2) | _[Ready / Needs work / Not started]_ | ___ | _[Date]_ |

### 3D. O3 Red Flag Check

- [ ] Pipeline coverage >2x? (If not → CEO: 100% pipeline mode)
- [ ] Meetings booked >2/week? (If not → 15 outbounds/day)
- [ ] Proposals outstanding >0? (If 0 by Wk 5 → diagnose)
- [ ] Deals at S4+ >2? (If not by Wk 6 → quarter at risk)
- [ ] ARR >$0? (If $0 by Wk 8 → emergency)
- [ ] Avg deal size >$80k? (If not → packaging review)

**Red flags triggered today:** _[None / List them]_

---

## PART 4: Cross-Objective Issues & Action Plan (5 min)

### Cross-Cutting Quality Issues

| Issue | Affects | O1 Impact | O2 Impact | O3 Impact | Owner |
|---|---|---|---|---|---|
| ___ | _[What]_ | _[Y/N — how]_ | _[Y/N — how]_ | _[Y/N — how]_ | ___ |
| ___ | _[What]_ | _[Y/N — how]_ | _[Y/N — how]_ | _[Y/N — how]_ | ___ |

### O1 → O2 → O3 Value Chain Check

The value chain flows: **O1 (platform works) → O2 (disease-specific data) → O3 (revenue)**.

| Link | Healthy? | If not, what's breaking? |
|---|---|---|
| O1 → O2 (Platform supports dataset integration) | _[Y/N]_ | ___ |
| O2 → O3 (Disease-specific demos drive sales) | _[Y/N]_ | ___ |
| O1 → O3 (Platform reliability supports enterprise deals) | _[Y/N]_ | ___ |

---

## ACTION PLAN — Fix Items for Next Week

**Maximum 7 items. Each must have an owner and a deadline.**

| # | Fix Item | Objective | Owner | Due Date | Verification |
|---|---|---|---|---|---|
| 1 | ___ | O[_] | ___ | _[Date]_ | _[How we verify it's fixed]_ |
| 2 | ___ | O[_] | ___ | _[Date]_ | _[How we verify it's fixed]_ |
| 3 | ___ | O[_] | ___ | _[Date]_ | _[How we verify it's fixed]_ |
| 4 | ___ | O[_] | ___ | _[Date]_ | _[How we verify it's fixed]_ |
| 5 | ___ | O[_] | ___ | _[Date]_ | _[How we verify it's fixed]_ |
| 6 | ___ | O[_] | ___ | _[Date]_ | _[How we verify it's fixed]_ |
| 7 | ___ | O[_] | ___ | _[Date]_ | _[How we verify it's fixed]_ |

**Items deferred (acknowledged but not this week):**
1. ___
2. ___

---

## Meeting Close

| Question | Answer |
|---|---|
| Biggest quality risk right now? | ___ |
| Are we confident in what we're shipping? | _[Y/N — why not]_ |
| Anything that needs an escalation meeting? | _[Y/N — what]_ |
| Next Fixing session: | _[Thursday, Date]_ |

---

## Notes & Comments

_[Free-form notes from the session]_

---

*Template based on ArcaScience OKR Execution Blueprint — C1 Thursday "Fixing" Session, expanded for O1/O2/O3 full coverage*
