# ArcaScience — Next Quarter OKR Execution Blueprint

> **Three-in-one document:**
> - **PART A — PRESENT:** Slide-ready sections for team kickoff and board communication
> - **PART B — TRACK:** Weekly scorecards and dashboards each owner fills in
> - **PART C — EXECUTE:** Operating manual with weekly checklists, playbooks, and templates

**Quarter Narrative:**
*"Deliver the V1 BRA platform with real client usage, create disease-specific versions for 2 therapeutic axes, and validate traction with $500k ARR."*

**Team:** Charbel (Product Lead — Workflow & UX) | Jeff (CTO/Eng Lead — Reliability & Infra) | Vassili (Clinical Lead / Medical Strategy — Benefit-Risk & Validation) | CEO (Revenue + Strategy)

---
---

# PART A — PRESENT

> Use this section for your team kickoff, investor updates, and board presentations.
> Each numbered section maps to one "slide" or talking point.

---

## A1. WHY THIS QUARTER IS DIFFERENT

This is a **leverage quarter**. We have a working platform, differentiated tech, and early traction. Now we prove three things:

| Proof Point | What It Means |
|---|---|
| **Production-ready BRA platform** | V1 deployed with 5 epics, real client usage (10-50 users), full BRA pipeline (Context, B&R Assessment, Data Analysis), 99% uptime |
| **Disease-specific platform versions** | 2 therapeutic axes with structured, validated datasets integrated in the platform + functional demos |
| **Repeatable revenue engine** | We can sell $500k ARR through a disciplined, disease-specific motion |

If we prove all three, we become the global standard. If we prove two out of three, we have a strong company. If we prove one, we're a science project.

---

## A2. THE VALUE CHAIN — HOW THE THREE OBJECTIVES CONNECT

```
O1 (Platform)  ──►  O2 (Therapeutic Packs)  ──►  O3 (Revenue)
   ENGINE              ACCELERATOR                OUTCOME
```

| Link | Mechanism | What Breaks if It Fails |
|---|---|---|
| **O1 → O2** | Platform BRA pipeline (Context, B&R Assessment, Data Analysis) enables disease-specific dataset integration | Disease-specific versions can't be built — no data foundation |
| **O2 → O3** | Disease-specific platform versions compress sales cycles by 40-60% | We're selling a generic platform — longer cycles, lower win rate, lower ACV |
| **O3 → O1** | Revenue funds next engineering round | Platform roadmap stalls. No on-prem. No enterprise scale |
| **O1 → O3** | Real client usage (10-50 users) creates internal champions | Expansion revenue = $0 without adoption |

**Critical path:** BRA Step 1 "Context" must reach >= 90% completeness by **Week 4**. First therapeutic axis dataset must be structured by **Week 7**. These are hard dependencies for O3.

---

## A3. THE THREE OBJECTIVES — AT A GLANCE

### O1 — Make the BRA Platform the Reference Way to Do Benefit-Risk

> *Deliver the V1 of the BRA-Platform validated by real client usage, with a fully operational BRA pipeline (Context, Benefit & Risk Assessment, Data Analysis), production-grade reliability, and complete observability.*

**Owners:** Charbel (Product Lead — Workflow & UX) | Jeff (CTO/Eng Lead — Reliability & Infra) | Vassili (Clinical Lead — Benefit-Risk & Validation)

**Weekly Ritual:**
- **Every day — 30 min:** "BRA OKR Scoreboard" review: time-to-output, insights, acceptance, bugs, uptime
- **Every Thursday — 60 min:** "Fixing" session: credibility, noise, calibration — maintains quality while moving fast

#### KR 1.1 — Deliver the V1 of the BRA-Platform validated by real client usage

| Metric | Current | Target | Owner |
|---|---|---|---|
| Main epics deployed and usable in Production | 1 | 5 | App-Team |
| Users from companies using the platform | 0 users from 0 companies | 10-50 users from 1-5 companies | App-Team, Sales-Team |

#### ~~KR 1.2 — Deliver a Prod-ready V1 BRAT workflow~~ *(deprecated — replaced by KR 1.2, 1.3, 1.4 below)*

#### KR 1.2 — BRA Step 1: "Context" up and running

| Metric | Current | Target | Owner |
|---|---|---|---|
| Completeness of "alternative T. options" validated on a set of 10 known studies | 0 | >= 90% | Data-Team |
| Human work for Therapeutic option | 0 | < 4h | Data-Team |
| Study details V1 | 0 | Delivered | Data-Team |

#### KR 1.3 — BRA Step 2: "Benefit & Risk Assessment" up and running

| Metric | Current | Target | Owner |
|---|---|---|---|
| F1 on Risk/Safety endpoints pipeline for drug and comparator on a ref dataset | 0% | >= 85% | Data-Team |
| F1 on Efficacy endpoints data extraction | 0% | >= 85% | Data-Team |
| Human work for this step | 0 | < 4h | Data-Team |

#### KR 1.4 — BRA Step 3: "Data Analysis" up and running

| Metric | Current | Target | Owner |
|---|---|---|---|
| V0 implemented | 0 | Delivered | Data-Team |
| Human work for this step | 0 | < 48h | Data-Team |

#### KR 1.5 — Reliability

| Metric | Current | Target | Owner |
|---|---|---|---|
| Code tested (Webapp + API) | 80% | 80% | App-Team, Data-Team |
| Critical / Major bugs in Prod | 0 | 0 | App-Team, Data-Team |
| Availability of Platform and Services | 95% | 99% | Devops-Team |
| Time to ship any modification in Prod | 30 min | 10 min | Devops-Team |
| APM data available (User actions, Errors, Treatment time, Cost) | 0% | 100% | Devops-Team |

#### O1 — Definition of Done

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

### O2 — Creation of a Disease-Specific Platform Version

> *Structure, validate, and integrate disease-specific datasets for 2 therapeutic axes/diseases into the BRA platform, with functional demos ready for each axis.*

#### KR 2.1 — Structuring of all relevant Data (Landscape, Disease, Benefit, Risk) for 2 therapeutic axes/Diseases

| Metric | Current | Target | Owner |
|---|---|---|---|
| Generation of relevant Datasets for 2 Therapeutic axis/diseases | 0 | 2 | Data-Team |

**Main Tasks:**
1. Benchmark 10 different Therapeutic axes/diseases for their: business potential, platform fit
2. Select 2-3 (2 main, 1 optional/stretch) Therapeutic axes/diseases to be executed within current capabilities
3. Identify the gaps to be addressed in terms of: Quality and use case (address to R&D and Clinical development teams) — specify to which output it belongs
4. Listing of all needed improvements: are they disease-specific or could be addressed in a generic approach?
5. Assess the feasibility and define an action plan to address each of these gaps
6. Execute the plan
7. Quality control and further improvements

*Needed Resources: TO BE DEFINED*
*Dependencies and Interactions with Other KRs: TO BE DEFINED*

#### KR 2.2 — Internal and external Validation of the generated Datasets

| Metric | Current | Target | Owner |
|---|---|---|---|
| Outputs validated using external validation based on defined criteria | 0 | 4 | Data-Team |
| Outputs validated using internal validation based on defined criteria | 0 | 4 | Data-Team |
| Outputs validated using LLM validation based on defined criteria | 0 | 4 | Data-Team |

**Main Tasks — External Validation:**
- Identification and contact of 5 relevant KOLs
- Questionnaire/interview guide developed for each platform output
- Deliver analysis of results as % data validated
- Integrate 100% of the feedback to improve the dataset

**Main Tasks — Internal Validation:**
- Generation of the test Datasets
- Creation of the Test Datasets
- Creation of the test requirements
- Annotation of the test data
- Deliver analysis of results as % data validated
- Integrate 100% of the feedback to improve the dataset

**Main Tasks — Validation by an LLM:**
- Creation of the test prompt
- Validation of the test prompt
- Test execution
- Deliver analysis of results as % data validated
- Integrate 100% of the feedback to improve the dataset

*Needed Resources: TO BE DEFINED*
*Dependencies and Interactions with Other KRs: TO BE DEFINED*

#### KR 2.3 — Integration of the Final Datasets inside the Platform BRA

| Metric | Current | Target | Owner |
|---|---|---|---|
| % of added data fully accessible and displayed on the platform | 0 | 100% | Data-Team |
| Functional Demo ready for each therapeutic axis | 0 | 2 | Data-Team |

**Main Tasks:**
1. Anticipation of the display for the therapeutic verticals: Sales, Marketing, Product dependency
2. Align to the product roadmap
3. Selection of adapted features (specific / generic)
4. Modification of the UX
5. Test the UX
6. Creation of the Demo Storytelling

*Needed Resources: TO BE DEFINED*
*Dependencies and Interactions with Other KRs: TO BE DEFINED*

---

### O3 — Reach $500k ARR Run-Rate

> *Build a repeatable revenue engine through disease-specific-first enterprise subscriptions, disciplined pipeline management, and systematic expansion — proving ArcaScience is a scalable commercial entity.*

| KR | Target | Stretch | Owner |
|---|---|---|---|
| ARR run-rate | $500k | $650k | CEO |
| New logos signed | 3 | 5 | CEO |
| Accounts expanded | 2 | 4 | CEO + Product |
| Pipeline coverage (qualified pipe / target) | 3x ($1.5M) | 4x ($2M) | CEO |
| Win rate on qualified opps | 25% | 35% | CEO |
| Average sales cycle | <60 days | <45 days | CEO |

---

## A4. REVENUE MATH — THREE PATHS TO $500K

### Target Scenario

| Source | Deals | ACV | Total ARR |
|---|---|---|---|
| New logos (enterprise) | 1 | $175k | $175k |
| New logos (mid-market) | 2 | $100k | $200k |
| Expansion (existing) | 2 | $40k | $80k |
| Pilot conversion | 1 | $45k | $45k |
| **Total** | **6** | **$83k avg** | **$500k** |

### Conservative ($350k — 70% = success)

| Source | Deals | ACV | Total |
|---|---|---|---|
| Enterprise | 1 | $150k | $150k |
| Mid-market | 1 | $100k | $100k |
| Expansion | 1 | $50k | $50k |
| Pilot | 1 | $50k | $50k |
| **Total** | **4** | | **$350k** |

### Aggressive ($650k — stretch)

| Source | Deals | ACV | Total |
|---|---|---|---|
| Enterprise | 2 | $175k | $350k |
| Mid-market | 2 | $75k | $150k |
| Expansion | 3 | $50k | $150k |
| **Total** | **7** | | **$650k** |

**The Iron Rule:** Weeks 1-6 = pipeline weeks. Weeks 7-12 = closing weeks.

---

## A5. PRICING ARCHITECTURE

| Tier | Name | Includes | Price | For |
|---|---|---|---|---|
| Tier 1 | BRA Essentials | Platform (5 seats), 1 disease-specific version, standard onboarding | $75k-$100k/yr | Mid-market biotech |
| Tier 2 | BRA Professional | Platform (15 seats), 2 disease-specific versions, guided onboarding, BRAT/CIOMS exports | $125k-$175k/yr | Mid-to-large pharma |
| Tier 3 | BRA Enterprise | Unlimited seats, all disease-specific versions, dedicated CSM, on-prem, SLA | $200k-$300k/yr | Top-20 pharma |
| Add-on | Therapeutic Axis | Additional disease-specific version | $25k-$40k/yr | Any tier |

**Five pricing rules:**
1. Never sell platform without a disease-specific version — "Platform + Therapeutic Axis" is the minimum unit
2. Never do custom work for <$50k — price consulting at $2,500/day
3. Annual contracts only — no monthly, no quarterly
4. Multi-year discount: 10% (2yr), 15% (3yr) — only to accelerate close
5. Pilots: 3 months at 40% of annual, with defined success criteria upfront

---

## A6. 12-WEEK RHYTHM — THE ARC OF THE QUARTER

| Weeks | Phase | Build (O1 + O2) | Sell (O3) | Validate |
|---|---|---|---|---|
| **1-2** | Foundation | Baselines documented, SonarQube enforced, APM plan, 10 axes benchmarked, 2-3 axes selected | 10 outbounds, 5 warm intros, 3 meetings booked | Demo-ability check, gap analysis started |
| **3-4** | Pipeline acceleration | Epic 2 shipped, Context at 50%+, test datasets generated, gap action plan | 3-5 discovery calls, 2-3 demos, first proposal | BRA pipeline demo-able? Pilot criteria tested? |
| **5-6** | Pipeline peak | Epic 3 shipped, Context at 75%+, F1 at 60%+, Dataset 1 at 50%+, 2+ KOL sessions | Pipeline $1M+, 2-3 proposals out, first negotiation | KOL validation, sales pace check |
| **7-8** | Closing mode | Epic 4 shipped, Context >= 90%, F1 >= 85%, Dataset 1 complete, LLM prompts validated | First logo closed, pipeline $1.2M+, expansion proposed | Disease-specific demo in live sales, cycle data |
| **9-10** | Acceleration | Epic 5 shipped, Data Analysis V0, Dataset 2 complete, all validations done | 2nd-3rd logos, first expansion, pipeline $1.5M+ | Repeatable motion? Disease-specific close correlation? |
| **11-12** | Close sprint | All 5 epics, all datasets integrated, 2 demos ready, all materials finalized | $500k ARR, next-quarter pipeline $500k+ | Full metrics, sales motion documented |

---

## A7. RISK MATRIX — WHAT COULD KILL THE QUARTER

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Insufficient pipeline Weeks 1-6 | High | Fatal | CEO: 30%+ time on revenue. Pipeline <2x = emergency mode |
| Sales cycles >60 days | High | Severe | Disease-specific demos. Champion acceleration. Kill >90 day deals |
| Custom work trap | Medium | Severe | "Disease-specific version first." Executive triage for any custom request |
| BRA pipeline F1 scores too low | Medium | High | Weekly "Fixing" sessions. Calibration sprints. Data-Team focus |
| Demo not compelling | Medium | High | Demo-ability gate at Week 2. Ship 80% quality over 100% late |
| Dataset structuring delays | Medium | High | Parallelize axes. Reduce scope to 2 axes. Cut stretch axis early |
| Expansion = $0 | Medium | Moderate | APM instrumentation by Week 4. Account health reviews monthly |
| ACV erosion (<$80k avg) | Medium | Moderate | Pricing discipline. No discounts — offer multi-year or scope instead |
| Deals slip to next quarter | High | Moderate | Focus warm pipeline. Compress procurement. Mid-market backup plan |

**Cut list (in order of priority if spread too thin):**
1. Cut Axis 3 (stretch) — optional, not core
2. Cut KR1.5d stretch (10 min ship time — accept 15 min)
3. Cut conference attendance (unless 3+ qualified prospects there)
4. Cut internal process improvements mid-quarter
5. **NEVER cut:** Pipeline reviews, demo prep, proposal speed, Thursday "Fixing" sessions

---

## A8. FAILURE MODES — THE FIVE WAYS WE LOSE

| # | Mode | Description |
|---|---|---|
| 1 | **"Great product, no revenue"** | O1 and O2 succeed, O3 misses. Board loses GTM confidence. Next round doesn't happen |
| 2 | **"Custom project trap"** | Deals devolve into bespoke consulting. Looks like $500k but it's services, not ARR. Margins crater |
| 3 | **"Pipeline desert"** | So focused on closing that nobody builds new pipe. Quarter ends with $300k and an empty funnel |
| 4 | **"Founder bottleneck"** | Every deal needs CEO from call 1 to close. No system. No scale. CEO burns out |
| 5 | **"Expansion amnesia"** | Existing customers ignored. No APM data. Easiest ARR left on the table |

---
---

# PART B — TRACK

> Use this section as your **live operating system**. Copy these tables into Notion, Airtable, or a shared spreadsheet. Fill them in weekly. Review them in your Tuesday + Friday rituals.

---

## B1. MASTER OKR SCORECARD — UPDATE WEEKLY

### O1 — BRA Platform (Owners: Charbel, Jeff, Vassili)

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

**O1 Red Flags — Check Weekly:**
- [ ] Epics shipping on cadence? (If <2 by Week 4 → escalate to Charbel + Jeff)
- [ ] "Context" completeness improving? (If <50% by Week 4 → Data-Team sprint)
- [ ] F1 scores on B&R Assessment improving? (If <50% by Week 6 → calibration sprint)
- [ ] Uptime >95%? (If not in any 2-week window → war room)
- [ ] Active users >0 by Week 6? (If not → activation audit)
- [ ] APM data instrumentation started? (If 0% by Week 4 → Devops escalation)

---

### O2 — Disease-Specific Platform Version (Owners: Vassili, Data-Team, CEO)

| KR | Metric | Owner | Weekly KPI | Wk1 | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Wk7 | Wk8 | Wk9 | Wk10 | Wk11 | Wk12 | Target |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KR2.1 | Relevant Datasets generated for therapeutic axes | Data-Team | Datasets completed | | | | | | | | | | | | | 2 |
| KR2.2a | Outputs validated — external | Data-Team | Validations completed | | | | | | | | | | | | | 4 |
| KR2.2b | Outputs validated — internal | Data-Team | Validations completed | | | | | | | | | | | | | 4 |
| KR2.2c | Outputs validated — LLM | Data-Team | Validations completed | | | | | | | | | | | | | 4 |
| KR2.3a | Added data accessible on platform | Data-Team | % displayed | | | | | | | | | | | | | 100% |
| KR2.3b | Functional Demos ready | Data-Team | Demos delivered | | | | | | | | | | | | | 2 |

**Therapeutic Axis Tracker:**

| Axis | Dataset Structured (KR2.1)? | External Validation (KR2.2)? | Internal Validation (KR2.2)? | LLM Validation (KR2.2)? | Integrated in Platform (KR2.3)? | Demo Ready (KR2.3)? | Status |
|---|---|---|---|---|---|---|---|
| Axis 1 — TBD | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | __ % done |
| Axis 2 — TBD | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | __ % done |
| Axis 3 (stretch) — TBD | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | __ % done |

**O2 Red Flags — Check Bi-Weekly:**
- [ ] Benchmark of 10 therapeutic axes completed by end of Week 2?
- [ ] 2-3 axes selected by Week 3?
- [ ] Gap analysis completed by Week 4?
- [ ] First dataset structured by Week 7?
- [ ] KOL contacts initiated for external validation by Week 5?
- [ ] At least 1 functional demo ready by Week 10?

---

### O3 — Revenue Engine (Owner: CEO, supported by all)

| KR | Metric | Owner | Weekly KPI | Wk1 | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Wk7 | Wk8 | Wk9 | Wk10 | Wk11 | Wk12 | Target | Stretch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KR1 | ARR closed (cumulative $) | CEO | New ARR this week | | | | | | | | | | | | | $500k | $650k |
| KR2 | New logos (cumulative) | CEO | Logos signed | | | | | | | | | | | | | 3 | 5 |
| KR3 | Expansions (cumulative) | CEO/Prod | Expansions closed | | | | | | | | | | | | | 2 | 4 |
| KR4 | Pipeline $ (qualified) | CEO | Total pipe $ | | | | | | | | | | | | | $1.5M | $2M |
| KR5 | Win rate % | CEO | Rolling % | | | | | | | | | | | | | 25% | 35% |
| KR6 | Sales cycle (days avg) | CEO | Rolling avg days | | | | | | | | | | | | | <60 | <45 |

**O3 Red Flags — Check Weekly:**
- [ ] Pipeline coverage >2x? (If not → CEO: 100% pipeline mode)
- [ ] Meetings booked >2/week by Week 3? (If not → 15 outbounds/day)
- [ ] Proposals outstanding >0 by Week 5? (If 0 → diagnose)
- [ ] Deals at S4+ >2 by Week 6? (If not → quarter at risk)
- [ ] ARR >$0 by Week 8? (If $0 → emergency bridge/pilot conversion)
- [ ] Avg deal size >$80k? (If not → packaging review)
- [ ] CEO revenue hours >10/week? (If not → restructure calendar)

---

## B2. WEEKLY REVENUE DASHBOARD — CEO FILLS IN EVERY FRIDAY

| Metric | Wk1 | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Wk7 | Wk8 | Wk9 | Wk10 | Wk11 | Wk12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ARR Closed (cumulative $) | | | | | | | | | | | | |
| ARR Target This Week | $0 | $0 | $0 | $0 | $0-100k | $100-200k | $200-300k | $200-300k | $300-400k | $350-400k | $400-500k | $500k |
| Pipeline $ (qualified total) | | | | | | | | | | | | |
| Pipeline Target | $500k | $500k | $700k | $900k | $1M | $1.2M | $1.2M | $1.5M | $1.5M | $1.5M | $1.5M+ | $1.5M+ |
| Coverage Ratio (pipe/target) | | | | | | | | | | | | |
| Meetings Held | | | | | | | | | | | | |
| Demos Delivered | | | | | | | | | | | | |
| Proposals Sent (cumulative) | | | | | | | | | | | | |
| Deals at S3+ (demo done) | | | | | | | | | | | | |
| Deals at S4+ (proposal out) | | | | | | | | | | | | |
| Deals at S5 (negotiation) | | | | | | | | | | | | |
| Deals Closed This Week | | | | | | | | | | | | |
| Expansion Conversations | | | | | | | | | | | | |
| Warm Intros Received | | | | | | | | | | | | |
| CEO Revenue Hours | | | | | | | | | | | | |
| Forecast: Commit $ | | | | | | | | | | | | |
| Forecast: Best Case $ | | | | | | | | | | | | |
| Forecast: Upside $ | | | | | | | | | | | | |
| Weighted Forecast | | | | | | | | | | | | |
| Red Flag Deals (count) | | | | | | | | | | | | |

**Forecast formula:** Weighted = (Commit x 0.9) + (Best Case x 0.5) + (Upside x 0.2)
**Rule:** Weighted forecast must exceed $500k by Week 8. If not → escalation meeting.

---

## B3. PIPELINE TRACKER — UPDATE EVERY TUESDAY

### Active Deal Board

| Deal # | Company | Stage | Tier | Therapeutic Axis | ACV | Champion | Last Contact | Next Action | Due Date | Forecast | Red Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | S_ | _ | | $ | | | | | | |
| 2 | | S_ | _ | | $ | | | | | | |
| 3 | | S_ | _ | | $ | | | | | | |
| 4 | | S_ | _ | | $ | | | | | | |
| 5 | | S_ | _ | | $ | | | | | | |
| 6 | | S_ | _ | | $ | | | | | | |
| 7 | | S_ | _ | | $ | | | | | | |
| 8 | | S_ | _ | | $ | | | | | | |
| 9 | | S_ | _ | | $ | | | | | | |
| 10 | | S_ | _ | | $ | | | | | | |
| 11 | | S_ | _ | | $ | | | | | | |
| 12 | | S_ | _ | | $ | | | | | | |

### Stage Summary (auto-calculate or fill manually)

| Stage | Definition | Count | Total $ | Avg Days | Advancing? | Stalled? |
|---|---|---|---|---|---|---|
| S0 — Target Identified | Fits profile, contact found | | | | | |
| S1 — Meeting Booked | Responded, call scheduled | | | | | |
| S2 — Discovery Complete | Pain + budget + process confirmed | | | | | |
| S3 — Demo Delivered | Disease-specific demo shown, tech Q&A done | | | | | |
| S4 — Proposal Sent | SOW delivered, timeline agreed | | | | | |
| S5 — Negotiation | Terms in progress, legal involved | | | | | |
| S6 — Closed-Won | Signed contract | | | | | |
| SX — Closed-Lost | Dead, reason documented | | | | | |

---

## B4. ACCOUNT HEALTH TRACKER — UPDATE MONTHLY (or when trigger fires)

| Account | Health Score /100 | Active Users | Power Users | BRA Workflows/Mo | Packs Active | Expansion Trigger? | Next Action | Owner | Next Review Date |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | [ ] Yes [ ] No | | | |
| | | | | | | [ ] Yes [ ] No | | | |
| | | | | | | [ ] Yes [ ] No | | | |
| | | | | | | [ ] Yes [ ] No | | | |
| | | | | | | [ ] Yes [ ] No | | | |

**Health Score Formula:**
- Usage frequency (25%): Daily=25, Weekly=15, Monthly=5, None=0
- Feature breadth (20%): 80%+=20, 50-80%=12, <50%=5
- Power user count (20%): 3+=20, 2=12, 1=5, 0=0
- Support health (15%): Low tickets + positive=15, High tickets=5, None=0
- Champion strength (20%): Active advocate=20, Passive=10, None=0

| Score | Health | Required Action |
|---|---|---|
| 80-100 | GREEN | Expansion conversation this month |
| 60-79 | YELLOW | Engagement campaign, check-in call |
| 40-59 | ORANGE | Onboarding refresh, executive check-in |
| 0-39 | RED | Churn risk. CEO involvement immediately |

---

## B5. DEAL REVIEW TEMPLATE — USE EVERY TUESDAY FOR EACH DEAL

```
DEAL REVIEW — [Company Name] — [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. STAGE:      [S0-S6] → Advanced since last review? [Y/N]
2. DEAL VALUE:  $[X]k — Tier [1/2/3] — Therapeutic Axis: [which]
3. CHAMPION:   [Name, Title] — Last contact: [date]
4. NEXT ACTION: [Specific] — by [date] — by [who]
5. RISK FLAGS:  [Ghost champion / Happy ears / Scope creep /
                Procurement black hole / No-show / None]
6. NEED FROM TEAM: [Product? Clinical? CTO? None?]
7. FORECAST:   [Commit / Best Case / Upside]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DECISION: [Advance / Hold / Escalate / Disqualify]
```

---
---

# PART C — EXECUTE

> This is the **operating manual**. Each person reads their section, knows what to do every week, and uses the playbooks when needed.

---

## C1. WEEKLY OPERATING CADENCE — THE NON-NEGOTIABLE RHYTHM

| Day | Ritual | Duration | Who | What Happens |
|---|---|---|---|---|
| **Every day** | BRA OKR Scoreboard | 30 min | All | Review: time-to-output, insights, acceptance, bugs, uptime. Blockers? |
| **Tuesday** | Pipeline Review | 30 min | CEO + team | Every deal reviewed (B5 template). Coverage check. Next actions assigned |
| **Wednesday** | Therapeutic Axis Standup | 30 min | Vassili + Charbel + Jeff + Data-Team | Dataset structuring progress. Validation status. Blockers. KOL scheduling |
| **Thursday** | "Fixing" Session | 60 min | Vassili + Charbel | Credibility, noise, calibration — maintains quality while moving fast |
| **Friday** | Sales Forecast + Week-Ahead | 15 min | CEO | Forecast update (B2). Kill list. Next week's meetings prepped |

**Rule:** These meetings happen every week. No exceptions. No rescheduling. They are the heartbeat of the quarter.

---

## C2. OWNER CHECKLISTS — WHAT EACH PERSON DOES EVERY WEEK

### CHARBEL (Product Lead — Workflow & UX) — Weekly Checklist

| Week | Ongoing | Key Deliverables |
|---|---|---|
| **Every week** | | |
| | [ ] Update KR1.1a (epics deployed) in scorecard | |
| | [ ] Update KR1.1b (user count / companies) in scorecard | |
| | [ ] Report user activation numbers at daily BRA OKR Scoreboard (30 min) | |
| | [ ] Ensure demo environment is stable for sales calls | |
| | [ ] Attend Thu "Fixing" session (60 min) — credibility, noise, calibration | |
| **Wk 1-2** | | [ ] Assess demo-ability of BRA platform V1 (Y/N gate) |
| | | [ ] Identify top 3 UX blockers for workflow improvement |
| | | [ ] Platform usage instrumentation plan (for KR1.5e APM) |
| **Wk 3-4** | | [ ] Epic 2 deployed in Production |
| | | [ ] Post-demo feedback form created and deployed |
| | | [ ] UX modifications for disease-specific display (O2 KR2.3 support) |
| **Wk 5-6** | | [ ] Epic 3 deployed in Production |
| | | [ ] Demo environment stable for prospect demos |
| **Wk 7-8** | | [ ] Epic 4 deployed in Production |
| | | [ ] Account health scores calculated for all customers |
| **Wk 9-10** | | [ ] Epic 5 deployed in Production |
| | | [ ] Usage data compiled for expansion conversations |
| **Wk 11-12** | | [ ] All 5 epics deployed — KR1.1a target met |
| | | [ ] Full quarter product metrics compiled |
| | | [ ] Activation + retention data for board report |

---

### JEFF (CTO / Eng Lead — Reliability & Infra) — Weekly Checklist

| Week | Ongoing | Key Deliverables |
|---|---|---|
| **Every week** | | |
| | [ ] Update KR1.5a (code coverage %) in scorecard | |
| | [ ] Update KR1.5b (critical/major bugs) in scorecard | |
| | [ ] Update KR1.5c (platform availability %) in scorecard | |
| | [ ] Update KR1.5d (ship time to Prod) in scorecard | |
| | [ ] Update KR1.5e (APM data coverage %) in scorecard | |
| | [ ] Monitor MLOps pipeline stability | |
| | [ ] Attend daily BRA OKR Scoreboard (30 min) | |
| **Wk 1-2** | | [ ] Baseline uptime, bug count, ship time, APM documented |
| | | [ ] SonarQube Quality Gate enforced on all deployments |
| | | [ ] Pipeline dashboard in CRM operational (support CEO) |
| | | [ ] APM instrumentation plan defined and started |
| **Wk 3-4** | | [ ] Performance benchmarks on real BRA cases documented |
| | | [ ] Ship time reduced toward 10 min target |
| | | [ ] Any enterprise security/compliance questions from deals → answered <48h |
| **Wk 5-6** | | [ ] Platform availability at 97%+ trailing 30 days |
| | | [ ] APM data at 50%+ coverage |
| | | [ ] On-prem readiness assessment (if enterprise deal requires) |
| **Wk 7-8** | | [ ] Platform availability at 99%+ trailing 30 days |
| | | [ ] 0 critical/major bugs in Prod |
| | | [ ] Support CEO with security/compliance for negotiation-stage deals |
| **Wk 9-10** | | [ ] Ship time at 10 min target |
| | | [ ] APM data at 100% coverage |
| **Wk 11-12** | | [ ] All KR1.5 targets met |
| | | [ ] Infrastructure metrics for board report |
| | | [ ] Capacity plan for next quarter based on deal volume |

---

### VASSILI (Clinical Lead / Medical Strategy — Benefit-Risk & Validation) — Weekly Checklist

| Week | Ongoing | Key Deliverables |
|---|---|---|
| **Every week** | | |
| | [ ] Update KR1.2 ("Context" completeness + human work) in scorecard | |
| | [ ] Update KR1.3 (B&R Assessment F1 scores + human work) in scorecard | |
| | [ ] Update KR2.1 (dataset generation progress) in scorecard | |
| | [ ] Update KR2.2 (validation progress — external, internal, LLM) in scorecard | |
| | [ ] Lead Thu "Fixing" session (60 min) — credibility, noise, calibration | |
| | [ ] Attend daily BRA OKR Scoreboard (30 min) | |
| | [ ] Available for sales demos (clinical Q&A) on 24h notice | |
| **Wk 1-2** | | [ ] Benchmark 10 therapeutic axes for business potential + platform fit (O2 KR2.1) |
| | | [ ] Select 2-3 therapeutic axes (2 main, 1 stretch) |
| | | [ ] Identify gaps in Quality and use case per output |
| | | [ ] Schedule first KOL contacts for external validation (O2 KR2.2) |
| | | [ ] Leverage KOL network for 2+ warm intros to pharma contacts |
| **Wk 3-4** | | [ ] Gap analysis + action plan completed for selected axes |
| | | [ ] "Context" step — Alt. T. options at 50%+ completeness |
| | | [ ] Internal validation: test datasets generated (O2 KR2.2) |
| | | [ ] Clinical positioning language for one-pager |
| **Wk 5-6** | | [ ] Dataset 1 structuring in progress — 50%+ complete |
| | | [ ] "Context" completeness at 75%+ |
| | | [ ] B&R Assessment F1 scores at 60%+ |
| | | [ ] 2+ KOL interview sessions completed (external validation) |
| | | [ ] Reference story v1: clinical outcome data for sales use |
| **Wk 7-8** | | [ ] Dataset 1 structured — KR2.1 first axis complete |
| | | [ ] "Context" at >= 90% completeness (KR1.2 target) |
| | | [ ] B&R Assessment F1 at >= 85% (KR1.3 target) |
| | | [ ] External validation: 2+ outputs validated |
| | | [ ] LLM validation: test prompts created + validated |
| **Wk 9-10** | | [ ] Dataset 2 structured — KR2.1 target met |
| | | [ ] Internal validation: 4 outputs validated (KR2.2 target) |
| | | [ ] LLM validation: 4 outputs validated (KR2.2 target) |
| | | [ ] Data Analysis V0 delivered (KR1.4 target) |
| **Wk 11-12** | | [ ] All validation documentation finalized |
| | | [ ] All datasets integrated in platform (KR2.3 — 100%) |
| | | [ ] 2 functional demos ready (KR2.3 target) |
| | | [ ] Validation + dataset performance data for board report |

---

### CEO — Weekly Checklist

| Week | Ongoing | Key Deliverables |
|---|---|---|
| **Every week (non-negotiable)** | | |
| | [ ] 5+ outbound prospecting actions (emails, LinkedIn, calls) per day | |
| | [ ] Update pipeline tracker (B3) every Tuesday | |
| | [ ] Update revenue dashboard (B2) every Friday | |
| | [ ] Run deal review with team (B5 template) every Tuesday | |
| | [ ] Update forecast (Commit/Best Case/Upside) every Friday | |
| | [ ] Check pipeline coverage ratio — if <2x, cancel non-revenue meetings | |
| | [ ] 1 LinkedIn post on BRA / regulatory topics | |
| | [ ] Log CEO revenue hours (target: 12-15 hrs/week, minimum 10) | |
| **Wk 1-2** | | [ ] Build target account list: 50 accounts identified + researched |
| | | [ ] Finalize pricing sheet (3 tiers + add-ons) |
| | | [ ] Draft 3 outbound email sequences (cold, warm, re-engage) |
| | | [ ] Request warm intros: 2 per investor, 3 per advisor |
| | | [ ] Review all existing pipeline against new stage criteria |
| | | [ ] Pull existing customer usage data, identify expansion candidates |
| | | [ ] Implement deal review template (B5) |
| **Wk 3-4** | | [ ] Deliver 3-5 discovery calls |
| | | [ ] Deliver 2-3 demos (with Vassili for clinical content) |
| | | [ ] Send first proposal or pilot agreement |
| | | [ ] Pipeline: $500k+ qualified |
| | | [ ] Create one-pager per therapeutic area |
| | | [ ] Create pilot proposal template with success criteria |
| **Wk 5-6** | | [ ] Pipeline: $1.0M+ qualified |
| | | [ ] 2-3 proposals outstanding |
| | | [ ] First deal enters S5 (negotiation) |
| | | [ ] Initiate first expansion conversation with existing customer |
| | | [ ] Create "Why we win" competitive positioning doc |
| | | [ ] Reference story v1 drafted |
| **Wk 7-8** | | [ ] Close first new logo ($100k-$175k) |
| | | [ ] Pipeline: $1.2M+ (replenished after closes) |
| | | [ ] 2-3 more deals in S4/S5 |
| | | [ ] First expansion deal proposed |
| | | [ ] GTM bundle for Axis 1 finalized |
| | | [ ] Reference story v2 with quantified outcomes |
| **Wk 9-10** | | [ ] Close deals 2-3 (new logos) |
| | | [ ] Close first expansion deal |
| | | [ ] Pipeline: $1.5M+ (including next-quarter opps) |
| | | [ ] GTM bundle for Axis 2 finalized |
| | | [ ] ARR target: $350k-$400k cumulative |
| **Wk 11-12** | | [ ] Push every Commit-category deal to signature |
| | | [ ] Close remaining expansion deals |
| | | [ ] Target: $500k ARR achieved |
| | | [ ] Next-quarter pipeline: $500k+ qualified |
| | | [ ] Prepare board report: ARR, pipeline, unit economics |
| | | [ ] Document sales motion: what worked, what didn't |

---

## C3. SALES OPERATING SYSTEM — REFERENCE PLAYBOOKS

### C3.1 Stage Definitions

| Stage | Name | Entry Criteria | Exit Criteria | Max Duration | Close Probability |
|---|---|---|---|---|---|
| S0 | Target Identified | Fits target profile. Contact found | First outreach sent | — | 5% |
| S1 | Meeting Booked | Positive response. Call scheduled | Discovery call completed | 1-2 weeks | 10% |
| S2 | Discovery Complete | Pain confirmed. Budget discussed. Process known | Agreed to demo | 1-2 weeks | 20% |
| S3 | Demo Delivered | Disease-specific demo shown. Tech Q&A done | Champion confirmed. Proposal requested | 1-2 weeks | 40% |
| S4 | Proposal Sent | SOW/pricing delivered. Timeline agreed | Verbal yes or negotiation started | 1-3 weeks | 60% |
| S5 | Negotiation | Terms being finalized. Legal/procurement active | Signed contract | 1-4 weeks | 80% |
| S6 | Closed-Won | Contract signed. Payment terms agreed | Onboarding starts | — | 100% |
| SX | Closed-Lost | Dead. Reason documented | Post-mortem done | — | 0% |

### C3.2 Qualification Criteria (MEDDPIC for BRA)

**A deal is "qualified" (S2+) only when ALL confirmed:**

| Letter | Criteria | Must-Have Answer |
|---|---|---|
| **M** | Metrics — cost of current BRA process | Can quantify: "$X per assessment" or "Y months per report" |
| **E** | Economic Buyer — who signs | Named individual, VP+ level |
| **D** | Decision Criteria — what they evaluate | Speed, auditability, compliance (at least 2 of 3) |
| **D** | Decision Process — procurement steps | Steps + timeline documented |
| **P** | Pain — what's broken | Specific: failed audit / behind schedule / lost submission |
| **I** | Identify Champion — internal advocate | Named person who will fight for us |
| **C** | Competition — who else they evaluate | Known: no one, consultants, or named competitor |

### C3.3 Disqualification Triggers — Kill the Deal If:

1. No budget confirmed AND no budget cycle within 60 days
2. No identifiable pain — they're "exploring" without urgency
3. Decision maker 3+ levels removed from contact
4. Therapeutic area outside our launched disease-specific versions (unless >$200k enterprise)
5. Want free pilot with no defined success criteria
6. Procurement timeline >90 days
7. Want custom work that doesn't map to a therapeutic axis
8. Gone silent >14 days despite 3 follow-up attempts

### C3.4 Red Flag Playbook

| Red Flag | How to Detect | What to Do |
|---|---|---|
| **Ghost champion** | No response in 7 days | Multi-thread: contact a 2nd person. If no response in 14 days → disqualify |
| **Happy ears** | "Sounds great!" but no next step scheduled | Force it: "Can we schedule the next step right now?" |
| **Infinite pilot** | Pilot >30 days, no evaluation criteria met | Set 48-hour deadline for evaluation call. Kill if no engagement |
| **Procurement black hole** | In legal with no named contact or timeline | Get named procurement contact + expected date. No name = not real |
| **Scope creep** | Asks for features outside therapeutic axis during sales | Acknowledge, document, do NOT commit. Offer as future roadmap |
| **No-show pattern** | 2+ reschedules or no-shows | Downgrade priority. Written follow-up. 3rd no-show → disqualify |

### C3.5 Forecast Categories

| Category | Definition | How to Count |
|---|---|---|
| **Commit** | Verbal yes. In negotiation/procurement. >80% confidence | 90% of value |
| **Best Case** | Demo done. Champion active. Decision this quarter. >50% | 50% of value |
| **Upside** | Qualified. In discovery/demo. Possible this quarter | 20% of value |

**Weighted Forecast = (Commit x 0.9) + (Best Case x 0.5) + (Upside x 0.2)**

---

## C4. DISEASE-SPECIFIC VERSION MONETIZATION PLAYBOOK

### C4.1 How Disease-Specific Versions Accelerate Revenue (show this to the team)

| Without Disease-Specific Version | With Disease-Specific Version | Impact |
|---|---|---|
| Generic demo → buyer must imagine their use case | Their therapeutic area, their endpoints, their drug class — validated data | **-3 weeks** discovery-to-conviction |
| "Does it work for oncology?" → need proof-of-concept | Validated datasets with KOL sign-off → proof exists | **-4 weeks** PoC phase eliminated |
| "What exactly are we buying?" → scope negotiation | Defined scope: structured datasets + functional demo + success criteria | **-2 weeks** proposal-to-signature |
| Platform = commodity pricing ($50k-$75k) | "Platform + Lung Cancer version" = specialized ($100k-$125k) | **+$25k-$50k ACV** |
| No upsell path | "Add Immunology version" = $25k-$40k | **Built-in expansion** |

**Net effect:** 40-60% shorter sales cycle. +10-15pp win rate. +$25-50k ACV. Built-in expansion.

### C4.2 Default Offer Positioning — Always Use This

**Rule:** Never sell naked platform. Every proposal = Platform + at least 1 disease-specific version.

**Positioning script (memorize this):**
> "ArcaScience isn't a generic analytics tool. We deliver ready-to-use benefit-risk assessment for your specific therapeutic area. When you buy BRA for Lung Cancer, you get structured datasets (Landscape, Disease, Benefit, Risk), validated by KOLs and internal benchmarks, a functional demo your team can follow, and a complete BRA pipeline (Context, Assessment, Analysis) — all on day one. The platform is the engine. The disease-specific version is what makes it drive."

**Proposal structure:**
1. Lead with the therapeutic area story (problem → BRA output → regulatory value)
2. Show the functional demo for their disease area
3. Present pricing as "Platform + [Area] Version"
4. Offer second therapeutic axis as expansion (plant the seed)
5. Never show platform-only pricing. It doesn't exist as an offer

### C4.3 Anti-Custom-Work Playbook

| Customer Request | Response |
|---|---|
| "Add a custom endpoint for our molecule" | "Our disease-specific version covers [X] standard endpoints. Custom endpoints are Professional Services at $2,500/day, min 5 days. If broadly relevant, we may add to roadmap — no timeline commitment." |
| "BRA for a rare disease you don't cover" | "Not on roadmap yet. We can discuss a Design Partner arrangement: 50% co-funded dataset development, early access." |
| "Build an integration with our system" | "Enterprise tier includes integration support. Scoped and estimated in contract. Tier 1-2 are standard only." |
| "Bespoke report format" | "BRAT + CIOMS formats included. Bespoke = add-on Professional Services. We recommend standard formats — regulators already accept them." |

**The rule:** Every hour of custom work = 1x value. Every hour of disease-specific dataset work = Nx value. Protect the N.

---

## C5. CUSTOMER EXPANSION PLAYBOOK

### C5.1 Expansion Triggers — When to Initiate Conversation

| Signal | Threshold | What It Means | Action |
|---|---|---|---|
| Active users exceed tier | >5 (Tier 1) or >15 (Tier 2) | Need more seats → upgrade | Propose tier upgrade |
| BRA workflows >10/month | Consistent high usage | Tool is embedded → add area | Propose new therapeutic axis |
| Exploring non-purchased area | Any query outside current axis | Organic interest in expansion | Initiate conversation within 1 week |
| Power users >3 | 3+ people at 3+/sessions/week | Account is sticky → lock in | Propose multi-year + new axis |
| Export downloads >5/month | Active regulatory use | Critical workflow tool | Multi-year lock-in conversation |
| Support ticket re: uncovered area | Any | Explicit expansion signal | Propose new therapeutic axis within 48 hours |

### C5.2 Expansion Motion (Step-by-Step)

1. **Detect trigger** → usage dashboard flags it (or you notice manually)
2. **Schedule "Value Review"** → call with champion within 1 week. Agenda: their usage data, their wins, other therapeutic areas in their pipeline
3. **Present options** → additional therapeutic axis ($25-40k), tier upgrade, multi-year discount
4. **Send proposal** → within 48 hours of interest. 1-page amendment to existing contract
5. **Close** → target 2 weeks (no new procurement cycle — amendment, not new contract)

### C5.3 Timeline

| Month After Signing | Activity |
|---|---|
| Month 1 | Activate all users. Ensure 1+ workflow per user completed |
| Month 2 | ID power users. First Value Review call |
| Month 3 | Expansion proposal if health score >70 |

**This quarter:** Customer signed Wk 1-4 = expansion candidate Wk 8-12.

---

## C6. FOUNDER REVENUE PLAYBOOK

### C6.1 CEO Time Allocation

**Minimum 30% of CEO time on revenue activities. Non-negotiable.**

| Activity | Frequency | Hours/Week |
|---|---|---|
| Outbound (email, LinkedIn, warm intros) | Daily | 5 |
| Discovery + demo calls | 3-5x/week | 3-5 |
| Pipeline review (internal) | 2x/week | 1 |
| Proposal writing | As needed | 2 |
| Warm intro requests to investors/advisors | 2x/week | 0.5 |
| Reference customer calls | As needed | 1 |
| **Total minimum** | | **12-15 hrs/week** |

**Calendar rule:** Revenue activities go on the calendar first. Everything else fills gaps.

### C6.2 Enterprise Deal Playbook (>$150k ACV)

| Phase | CEO Does | Support From |
|---|---|---|
| **Prospecting** | Sends first email / makes warm intro. Enterprise buyers respond to founders | — |
| **Discovery** | Runs the call. Understands their BRA pain, regulatory pressure, internal politics | Vassili on standby for clinical questions |
| **Demo** | Sets strategic context ("why BRA matters now"). Hands to Vassili for clinical demo | Charbel ensures demo env is stable |
| **Proposal** | Presents pricing as "partnership," not vendor sale | — |
| **Negotiation** | Handles objections. Offers multi-year or expanded scope. NOT discounts | Jeff if security/compliance questions |
| **Exec Alignment** | CEO-to-VP call with economic buyer. Builds relationship beyond the deal | — |
| **Close** | Calls champion day before decision. Reinforces urgency | — |

### C6.3 Warm Intro Mining Plan

| Source | What to Ask | When | Target Intros |
|---|---|---|---|
| Investors | "Intro to 2 portfolio pharma companies" | Week 1, follow up monthly | 2 per investor |
| Advisors/Board | "3 intros to pharma contacts this quarter" | Week 1, follow up Week 5 | 3 per advisor |
| Existing customers | "1 intro to a peer company" | After every milestone win | 1 per customer |
| Conference contacts | Follow up within 48h with BRA value prop | Per event | 3-5 per event |
| Vassili's KOL network | Clinical intros to pharma contacts | Ongoing | 2-3 per month |

**Every intro request → logged in CRM. Follow up within 72 hours.**

### C6.4 Reference Story Deployment

**Use these stories in:**
- Discovery calls: "Can I share how [Company X] used BRA to cut assessment time from 3 months to 2 days?"
- Proposals: 1-page case study as appendix (problem → BRA output → time saved)
- Procurement: "Who else uses this?" → named references close deals
- Expansion: "Your oncology team saw [X result]. Your immunology team has the same pain."

**Story must include:** Quantified time savings + regulatory acceptance + named therapeutic area + customer approval for external use.

---

## C7. MEETING AGENDAS — READY TO USE

### Tuesday Pipeline Review (30 min)

```
AGENDA — PIPELINE REVIEW — [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PIPELINE HEALTH (5 min)
   - Coverage ratio: ___x (target: 3x)
   - Total qualified pipeline: $___k
   - Net change vs last week: +/-$___k

2. DEAL-BY-DEAL (15 min)
   [Run B5 template for each active deal]
   - Which deals advanced?
   - Which deals stalled?
   - Which deals to disqualify?

3. NEW PIPELINE (5 min)
   - Meetings booked this week: ___
   - Outbounds sent: ___
   - Warm intros received: ___

4. BLOCKERS (5 min)
   - What's stuck?
   - What does CEO need from Product / Clinical / CTO?
   - Decisions required?

ACTION ITEMS:
1. ___
2. ___
3. ___
```

### Friday Forecast Update (15 min)

```
AGENDA — FORECAST UPDATE — [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. FORECAST (5 min)
   - Commit: $___k (deals: ___)
   - Best Case: $___k (deals: ___)
   - Upside: $___k (deals: ___)
   - Weighted: $___k (target: must exceed $500k by Wk 8)

2. WEEK-AHEAD PREP (5 min)
   - Meetings next week: ___
   - Materials needed: ___
   - Demos scheduled: ___

3. KILL LIST (5 min)
   - Deals to disqualify: ___
   - Reason: ___
   - Time recovered → redirect to: ___

CEO REVENUE HOURS THIS WEEK: ___h (target: 12-15h)
```

### Wednesday Disease-Specific Version Standup (30 min)

```
AGENDA — THERAPEUTIC AXIS STANDUP — [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. AXIS 1 — [TBD] — 10 min
   - Dataset structuring %: ___
   - Validation progress (ext/int/LLM): ___
   - Platform integration %: ___
   - Blockers: ___
   - KOL sessions scheduled: ___

2. AXIS 2 — [TBD] — 10 min
   - Dataset structuring %: ___
   - Validation progress (ext/int/LLM): ___
   - Platform integration %: ___
   - Blockers: ___
   - KOL sessions scheduled: ___

3. AXIS 3 (stretch) — [TBD] — 5 min
   - Go/no-go status: ___
   - If go: structuring %: ___

4. CROSS-DEPENDENCIES — 5 min
   - BRA pipeline (O1) features blocking dataset work?
   - Clinical content needed from Vassili?
   - Demo readiness for sales?
```

---

## C8. 12-WEEK EXECUTION TIMELINE — FULL DETAIL

### WEEKS 1-2: FOUNDATION + PIPELINE BUILD

**BUILD (O1):**
- [ ] CRM pipeline configured (S0-S6 stages + required fields) — **Jeff supports, CEO owns**
- [ ] Baseline documented: uptime, bugs, ship time, APM coverage — **Jeff**
- [ ] SonarQube Quality Gate enforced on deployments — **Jeff**
- [ ] APM instrumentation plan defined and started — **Jeff**
- [ ] Platform usage instrumentation plan created — **Charbel**
- [ ] BRA platform V1 demo-ability assessed (Y/N gate) — **Charbel**

**BUILD (O2):**
- [ ] Benchmark 10 therapeutic axes for business potential + platform fit — **Vassili**
- [ ] Select 2-3 therapeutic axes (2 main, 1 stretch) — **Vassili**
- [ ] Gap analysis started: Quality and use case per output — **Vassili**
- [ ] First KOL contacts scheduled for external validation — **Vassili**

**SELL:**
- [ ] Target account list: 50 accounts identified + researched — **CEO**
- [ ] Pricing sheet finalized (3 tiers + add-ons) — **CEO**
- [ ] 10 outbound emails sent to top targets — **CEO**
- [ ] 5 warm intro requests to investors/advisors — **CEO**
- [ ] 3 discovery meetings booked for Weeks 3-4 — **CEO**
- [ ] All existing pipeline reviewed + restaged — **CEO**
- [ ] Outbound email sequences drafted (cold, warm, re-engage) — **CEO**
- [ ] 2+ warm intros requested via Vassili's KOL network — **Vassili**

**INSTRUMENT:**
- [ ] Weekly OKR scoreboard live (B1 tables) — **All owners**
- [ ] Pipeline dashboard operational (B3) — **CEO + Jeff**
- [ ] Daily BRA OKR Scoreboard (30 min) cadence started — **All**
- [ ] Thursday "Fixing" session (60 min) cadence started — **Vassili + Charbel**
- [ ] Weekly cadence calendar invites sent (C1) — **CEO**

---

### WEEKS 3-4: PIPELINE ACCELERATION + FIRST DEMOS

**BUILD (O1):**
- [ ] Epic 2 deployed in Production — **Charbel + Jeff**
- [ ] "Context" Alt. T. options at 50%+ completeness — **Data-Team + Vassili**
- [ ] Ship time improvements in progress — **Jeff**

**BUILD (O2):**
- [ ] Gap analysis + action plan completed for selected axes — **Vassili**
- [ ] Internal validation: test datasets generated — **Data-Team**
- [ ] One-pager per therapeutic area (sales collateral) — **CEO + Vassili**

**SELL:**
- [ ] 3-5 discovery calls completed — **CEO**
- [ ] 2-3 demos delivered — **CEO + Vassili**
- [ ] First pilot or proposal sent — **CEO**
- [ ] Pipeline reaches $500k+ qualified — **CEO**
- [ ] 5 additional warm intros received + converted to meetings — **CEO**
- [ ] Pilot proposal template (3 months, defined success criteria) — **CEO**
- [ ] Customer expansion proposal template — **CEO**

**VALIDATE:**
- [ ] BRA pipeline speed demonstrable in live demo? (Y/N) — **Charbel**
- [ ] Pilot success criteria template tested with 1 prospect — **CEO**
- [ ] Demo feedback collected from prospects — **CEO**

**INSTRUMENT:**
- [ ] Post-demo feedback form deployed — **Charbel**
- [ ] Pipeline coverage auto-tracking operational — **CEO**

---

### WEEKS 5-6: PIPELINE PEAK + FIRST CLOSE ATTEMPTS

**BUILD (O1):**
- [ ] Epic 3 deployed in Production — **Charbel + Jeff**
- [ ] "Context" completeness at 75%+ — **Data-Team + Vassili**
- [ ] B&R Assessment F1 scores at 60%+ — **Data-Team**
- [ ] Platform availability at 97%+ — **Jeff**
- [ ] APM data at 50%+ coverage — **Jeff**

**BUILD (O2):**
- [ ] Dataset 1 structuring in progress — 50%+ complete — **Vassili + Data-Team**
- [ ] 2+ KOL interview sessions completed (external validation) — **Vassili**
- [ ] Reference story v1 (clinical outcome data for sales) — **Vassili + CEO**

**SELL:**
- [ ] Pipeline reaches $1.0M+ qualified — **CEO**
- [ ] 2-3 proposals outstanding — **CEO**
- [ ] First deal enters S5 (negotiation) — **CEO**
- [ ] First expansion conversation initiated — **CEO + Charbel**
- [ ] Target: $0-$100k ARR closed or in Commit forecast — **CEO**
- [ ] Sales deck v2 (incorporating Wk 3-4 demo feedback) — **CEO**
- [ ] "Why we win" competitive positioning document — **CEO**

**VALIDATE:**
- [ ] Deals progressing at expected pace? (check cycle time) — **CEO**
- [ ] If pipeline coverage <2x → CEO enters 100% pipeline mode — **CEO**

**INSTRUMENT:**
- [ ] Forecast model operational (Commit / Best Case / Upside) — **CEO**
- [ ] Win/loss tracking initiated — **CEO**

---

### WEEKS 7-8: CLOSING MODE + DATASET VALIDATION

**BUILD (O1):**
- [ ] Epic 4 deployed in Production — **Charbel + Jeff**
- [ ] "Context" at >= 90% completeness — KR1.2 target — **Data-Team + Vassili**
- [ ] B&R Assessment F1 at >= 85% — KR1.3 target — **Data-Team**
- [ ] Platform availability at 99%+ — KR1.5c target — **Jeff**
- [ ] 0 critical/major bugs in Prod — KR1.5b target — **Jeff**

**BUILD (O2):**
- [ ] Dataset 1 structured — KR2.1 first axis complete — **Vassili + Data-Team**
- [ ] External validation: 2+ outputs validated — **Vassili**
- [ ] LLM validation: test prompts created + validated — **Data-Team**
- [ ] GTM bundle for first therapeutic axis complete — **CEO + Vassili**
- [ ] Reference story v2 (quantified outcomes) — **CEO**

**SELL:**
- [ ] **First new logo closed ($100k-$175k)** — **CEO**
- [ ] Pipeline maintained at $1.2M+ (replenished) — **CEO**
- [ ] 2-3 additional deals at S4/S5 — **CEO**
- [ ] First expansion deal proposed — **CEO**
- [ ] Target: $200k-$300k ARR (closed or Commit) — **CEO**

**VALIDATE:**
- [ ] Disease-specific demo used in live sales demo → customer reaction validated — **CEO + Vassili**
- [ ] Sales cycle data: tracking to <60 day average? — **CEO**

**INSTRUMENT:**
- [ ] Account health scores calculated for all active customers — **Charbel**
- [ ] Expansion trigger alerts configured — **Charbel + Jeff**

---

### WEEKS 9-10: ACCELERATION + SECOND WAVE CLOSES

**BUILD (O1):**
- [ ] Epic 5 deployed in Production — **Charbel + Jeff**
- [ ] Data Analysis V0 delivered — KR1.4 target — **Data-Team**
- [ ] Ship time at 10 min — KR1.5d target — **Jeff**
- [ ] APM data at 100% coverage — KR1.5e target — **Jeff**

**BUILD (O2):**
- [ ] Dataset 2 structured — KR2.1 target met (2 axes) — **Vassili + Data-Team**
- [ ] Internal validation: 4 outputs validated — KR2.2 target — **Data-Team**
- [ ] LLM validation: 4 outputs validated — KR2.2 target — **Data-Team**
- [ ] GTM bundle for second therapeutic axis complete — **CEO + Vassili**
- [ ] Updated reference stories with first axis customer outcomes — **CEO**

**SELL:**
- [ ] **2nd and 3rd new logos closed** — **CEO**
- [ ] **First expansion deal closed** — **CEO**
- [ ] Pipeline: $1.5M+ (including next-quarter opps) — **CEO**
- [ ] Target: $350k-$400k ARR cumulative — **CEO**

**VALIDATE:**
- [ ] Repeatable sales motion: 2 deals followed same playbook? — **CEO**
- [ ] Disease-specific demo vs generic: faster close correlation? — **CEO**
- [ ] Expansion playbook tested on 1+ account — **CEO + Charbel**

**INSTRUMENT:**
- [ ] Next-quarter pipeline tracking initiated — **CEO**
- [ ] Sales velocity calculated (deal value x win rate x deals / cycle) — **CEO**

---

### WEEKS 11-12: CLOSE SPRINT + QUARTER WRAP

**BUILD (O1):**
- [ ] All 5 epics deployed — KR1.1a target met — **Charbel + Jeff**
- [ ] All KR1.5 reliability targets met — **Jeff**
- [ ] 10-50 users from 1-5 companies on platform — KR1.1b target — **App-Team + Sales-Team**

**BUILD (O2):**
- [ ] All datasets integrated in platform — KR2.3 at 100% — **Data-Team**
- [ ] 2 functional demos ready — KR2.3 target — **Data-Team + Vassili**
- [ ] All validation documentation finalized — **Vassili**
- [ ] All GTM materials finalized — **CEO + Vassili**

**SELL:**
- [ ] Every Commit deal pushed to signature — **CEO**
- [ ] Remaining expansion deals closed — **CEO**
- [ ] **Target: $500k ARR achieved** — **CEO**
- [ ] Next-quarter pipeline: $500k+ qualified — **CEO**

**VALIDATE:**
- [ ] Final quarter metrics compiled against all OKRs (O1 + O2 + O3) — **All owners**
- [ ] Sales motion documented: what worked, what repeats — **CEO**
- [ ] Disease-specific version vs generic deal comparison — **CEO**
- [ ] Quarter retrospective template — **CEO**
- [ ] Next-quarter OKR draft — **CEO + all**

**INSTRUMENT:**
- [ ] Full quarter dashboard finalized — **All owners**
- [ ] Board report: ARR + pipeline + unit economics + next-quarter plan — **CEO**

---
---

# APPENDIX

## A. KEY DEFINITIONS

| Term | Definition |
|---|---|
| **ARR Run-Rate** | Annualized value of all active subscriptions at quarter end. $125k contract in Week 10 = $125k ARR (not prorated) |
| **Qualified Opportunity** | Deal at S2+ with confirmed pain, champion, process, and budget discussion |
| **BRA Pipeline** | The three-step process: Step 1 "Context" → Step 2 "Benefit & Risk Assessment" → Step 3 "Data Analysis" |
| **Therapeutic Axis / Disease-Specific Version** | A structured dataset (Landscape, Disease, Benefit, Risk) for a specific disease area, validated and integrated into the platform with a functional demo |
| **Definition of Done (O1)** | Data Quality Validation + Data Traceability + Platform Usage Analysis + Platform Perf Monitoring + Code Quality Gate + 80% Code Tested — all six criteria |
| **Definition of Done (O2 — per Axis)** | Dataset Structured (KR2.1) + External Validation + Internal Validation + LLM Validation (KR2.2) + Integrated in Platform + Demo Ready (KR2.3) |
| **F1 Score** | Harmonic mean of precision and recall — used to measure accuracy of endpoint extraction pipelines |
| **Pipeline Coverage** | Qualified pipeline $ / remaining ARR target. Minimum 3x |
| **BRAT** | Benefit-Risk Action Team framework (regulatory standard) |
| **CIOMS** | Council for International Organizations of Medical Sciences |
| **APM** | Application Performance Monitoring — tracks user actions, errors, treatment time, cost |
| **SonarQube Quality Gate** | Automated code quality check that all Prod deployments must pass |

## B. STRUCTURAL UPGRADE RECOMMENDATIONS

### B.1 Add "Revenue Readiness" Gate to O2
Add a 7th criterion to the O2 Definition of Done: **"First qualified opportunity generated using this disease-specific version."** A therapeutic axis isn't launched until it has produced a sales conversation.

### B.2 Split O3 into Two Sub-Objectives
- **O3a: New Business ($350k)** — hunting. CEO-driven. Prospecting, demos, closes
- **O3b: Expansion ($150k)** — farming. Product/CS-driven. Usage data, health scores, upsell

Different owners, different cadences, different skills. Separating them creates clearer accountability.

### B.3 Elevate Pipeline Generation
Pipeline coverage is a KR, but it's actually the leading precondition for all revenue. Consider making "Maintain 3x coverage every week" an operating discipline with its own escalation protocol (this document provides one above).

---

## C. TARGET ACCOUNT PROFILE (TAP)

Use this to qualify whether an account belongs on the target list:

- [ ] Pharma/biotech with 3+ active clinical programs
- [ ] Has pharmacovigilance or benefit-risk function
- [ ] Currently doing BRA manually (Excel, Word, consultants)
- [ ] Budget authority at VP/Director level accessible
- [ ] In a therapeutic area where we have/are building disease-specific versions
- [ ] Annual R&D budget >$50M (mid-market) or >$500M (enterprise)

**If 5 of 6 boxes checked → add to target list. If <4 → pass.**

---

*This document is a living operating system.*
*Update Part B scorecards weekly.*
*Review Part C checklists in your rituals.*
*Present Part A to the team at kickoff and to the board at quarter-end.*

*If execution discipline is respected, $500k ARR is not aspirational — it is arithmetically inevitable.*
