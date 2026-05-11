# OKR2 Launch Deck — Full Slide Content

> Paste this entire document into Gamma's "Generate from text" flow. Slides separated by `---`.

---

## Slide 1 — Cover

**OKR2 · Q2 2026 · From Platform to Proof — A 6-Week Sprint**

- ArcaScience
- Finalize. Launch. Close.
- 6 weeks to production-grade BRA, chemical-analysis i-Demo launch, and €500k signed

---

## Slide 2 — Why This Sprint Is Different

**This is a proof sprint — 6 weeks to validate the commercial model.**

- Q1 built the platform. Q2 proves it sells
- 3 objectives, 3 phases, 6 weeks — no room for drift
- Success = production BRA + public chem launch + €500k signed contracts
- Failure = great technology, no revenue, no next round

---

## Slide 3 — The Arc: Finalize → Launch → Close

**Three phases, two weeks each — every week counts.**

| Phase | Weeks | Focus |
|---|---|---|
| **FINALIZE** | 1–2 | All 5 BRA steps in Prod. F1 ≥ 85 %. Scope frozen |
| **LAUNCH** | 3–4 | i-Demo chem module live. Launch event. 50+ leads |
| **CLOSE** | 5–6 | ≥ 3 Top-10 signed. €500k. ≥ 2 multi-year deals |

- O1 (platform) enables O2 (launch) enables O3 (revenue)
- Phase gates at Wk2 and Wk4 — no gate pass, no next phase

---

## Slide 4 — Objective 1: Finalize the BRA Platform

**100 % of platform steps live in Prod, F1 ≥ 90 %, < 1 h human work, 99.5 % availability.**

| KR | Target | Owner |
|---|---|---|
| Pipeline steps in Prod | 5/5 | Charbel + Jeff |
| F1 Safety / Efficacy | ≥ 90 % | Data-Team |
| Human work per BRA | < 1 h | Data-Team + App-Team |
| Availability | 99.5 % | Devops-Team |

- Owners: Charbel (Product), Jeff (Infra), Vassili (Validation)

---

## Slide 5 — O1: How We Finish the Platform

**5 pipeline steps, each with a Definition of Done.**

| Step | What It Does | DoD Gate |
|---|---|---|
| Context | Therapeutic options, alternatives | ≥ 90 % completeness |
| B&R Assessment | Safety + efficacy endpoint extraction | F1 ≥ 90 % |
| Data Analysis | Quantitative analysis of endpoints | Delivered + < 15 min human work |
| Reporting | Structured BRA report generation | Audit-ready output |
| Decision-Support | Benefit-risk balance + recommendations | End-to-end smoke test |

- SonarQube Quality Gate on every deployment
- 85 % code coverage minimum

---

## Slide 6 — Objective 2: Launch i-Demo on Chemical Analysis

**Chemical-analysis module publicly launched, ≥ 3 validated case studies, ≥ 50 leads captured.**

| KR | Target | Owner |
|---|---|---|
| Chem sub-modules deployed | 5/5 | Data-Team |
| Validated case studies | ≥ 3 | Vassili |
| Launch event executed | Yes | Vassili + CEO |
| Qualified leads captured | ≥ 50 | CEO |

- Owners: Vassili (Clinical/Chem), Charbel (Product)

---

## Slide 7 — O2: What Chemical Analysis Unlocks

**5 sub-modules that plug compound-level intelligence into the BRA workflow.**

| Sub-Module | What It Does | BRA Integration |
|---|---|---|
| Compound Search | Name/SMILES/InChI → structure + properties | Context step |
| ADMET Prediction | Safety profile: absorption, metabolism, toxicity | B&R Assessment |
| Mechanism of Action | Drug-target interaction, pathway mapping | Context + B&R |
| Bioactivity Analysis | IC50/EC50, dose-response, selectivity | Data Analysis |
| Drug-Target Binding | Binding affinity, off-target risks | Decision-Support |

- Removes the need for 5 separate tools — everything in one platform

---

## Slide 8 — O2: Launch Runbook (D-30 → D+7)

**A 30-day countdown to public launch.**

| Milestone | When | Key Actions |
|---|---|---|
| D-30 | Wk1 | Positioning defined, assets listed, channels mapped |
| D-14 | Wk2 | Demo asset functional, invitations sent, script rehearsed |
| D-7 | Wk3 | All sub-modules in Prod, demo live, press outreach sent |
| D-0 | Wk4 | **Launch event executed**, LinkedIn + press published |
| D+7 | Wk5 | Follow-up sent, demos booked, leads in pipeline |

- Target: ≥ 30 event attendees, ≥ 50 leads, ≥ 20 demo requests

---

## Slide 9 — Objective 3: Close ≥ €500k with Top-10 + Biotechs

**€500k signed, ≥ 3 of 10 named strategic accounts closed, pipeline ≥ €2M.**

| KR | Target | Stretch | Owner |
|---|---|---|---|
| Signed contracts | €500k | €700k | CEO |
| Top-10 closed | ≥ 3 | 5 | CEO |
| Multi-year deals | ≥ 2 | 3 | CEO |
| Biotech long-tail | ≥ 3 | 5 | CEO |

- Owner: CEO (Tom)

---

## Slide 10 — O3: Pipeline Coverage & Deal Map

**Top-10 strategic accounts + biotech long-tail = two pipelines, one target.**

| Top-10 Targets | Est. ACV |
|---|---|
| Sanofi, Roche, Novartis, AstraZeneca | €125k–€250k |
| GSK, Bayer, Boehringer Ingelheim | €100k–€175k |
| Servier, Ipsen, UCB | €75k–€125k |

- Top-10: 3 deals × €125k avg = €375k
- Biotech long-tail: 3 deals × €40k avg = €120k
- Combined: €495k → target achieved

---

## Slide 11 — Revenue Math: Three Scenarios

**Conservative / Target / Aggressive.**

| Scenario | Top-10 Deals | Long-Tail Deals | Total € |
|---|---|---|---|
| Conservative | 2 × €125k | 3 × €35k | €355k |
| **Target** | **3 × €125k** | **3 × €40k** | **€495k** |
| Aggressive | 4 × €125k | 5 × €40k | €700k |

- Pipeline coverage required: 3x target at all times
- Iron Rule: Wk1–2 pipeline, Wk3–4 proposals, Wk5–6 close

---

## Slide 12 — Pricing Architecture

**Platform tiers + chemical-analysis module + i-Demo upsell.**

| Tier | Includes | Price |
|---|---|---|
| BRA Essentials | Platform (5 seats), BRAT/CIOMS exports | €75k–€100k/yr |
| BRA Professional | Platform (15 seats) + 1 therapeutic axis | €125k–€175k/yr |
| BRA Enterprise | Unlimited seats, 3+ axes, dedicated CSM | €200k–€300k/yr |
| **Chem Module** | 5 sub-modules, BRA-integrated | **€30k–€50k/yr add-on** |
| **i-Demo Bundle** | Chem Module + 2 case studies + demo | **€50k–€75k/yr** |

---

## Slide 13 — 6-Week Rhythm

**Finalize / Launch / Close — no phase overlap.**

| Phase | Wk | O1 (Platform) | O2 (i-Demo) | O3 (Revenue) |
|---|---|---|---|---|
| FINALIZE | 1–2 | 5 steps in Prod | Sub-modules deployed | Pipeline to 3x |
| LAUNCH | 3–4 | F1 ≥ 90 % | Event executed | Proposals sent |
| CLOSE | 5–6 | DoD met | 3 case studies | €500k signed |

---

## Slide 14 — Risk Matrix: Top 6 Risks

**What could kill the sprint — and how we prevent it.**

| Risk | Impact | Mitigation |
|---|---|---|
| Pipeline too thin | Fatal | CEO: 15+ outbounds/day Wk1–2 |
| Top-10 cycles > 6 weeks | Severe | Kill deals without champion by Wk3 |
| Chem module not ready | Severe | Scope-cut to 3 core sub-modules |
| F1 stalls below 90 % | High | Weekly Fixing sessions + calibration |
| Launch = buzz, no leads | High | Pre-seed 20+ invitees from Top-10 |
| Custom work trap | Severe | Platform-first. No custom < €50k |

---

## Slide 15 — Failure Modes: 5 Ways We Lose

**Name the failures to prevent them.**

| # | Mode | What Happens |
|---|---|---|
| 1 | Great launch, no revenue | Buzz but no contracts. Marketing win, commercial fail |
| 2 | Platform isn't ready | Demos show incomplete product. Everything stalls |
| 3 | Top-10 mirage | All in discovery, none close. €500k depends on long-tail alone |
| 4 | Custom work quicksand | Deals become consulting. Margins crater |
| 5 | Launch fatigue | Team focused on event, pipeline and platform deprioritized |

---

## Slide 16 — Weekly Cadence & Rituals

**Five non-negotiable meetings every week.**

| Day | Ritual | Duration | Who |
|---|---|---|---|
| Monday | Sprint Week Kickoff | 15 min | All |
| Tuesday | Pipeline Review | 30 min | CEO + team |
| Wednesday | Chem Analysis Standup | 30 min | Vassili + Charbel + Jeff |
| Thursday | Fixing Session | 60 min | Vassili + Charbel |
| Friday | Forecast + Week-Ahead | 15 min | CEO |

- Rule: no rescheduling, no exceptions for 6 weeks

---

## Slide 17 — Owner Commitments

**One tile per owner — what they personally commit to.**

| Owner | Commitment |
|---|---|
| **Charbel** | All 5 BRA steps in Prod by Wk2. Demo asset live by Wk3. DoD met by Wk6 |
| **Jeff** | 99.5 % uptime. 85 % code coverage. Ship time < 10 min. APM at 100 % |
| **Vassili** | F1 ≥ 90 %. 3 validated case studies. Launch event co-presented. < 1 h human work |
| **CEO (Tom)** | ≥ 15 h/week on revenue. €500k signed. ≥ 3 Top-10 closed. ≥ 50 leads from launch |

---

## Slide 18 — Closing: The 6-Week Scoreboard

**This is the scoreboard we hold ourselves to.**

| Metric | Target | Owner |
|---|---|---|
| BRA pipeline steps in Prod | 5/5 | Charbel + Jeff |
| F1 Safety + Efficacy | ≥ 90 % | Data-Team + Vassili |
| Human work per BRA | < 1 h | Data-Team |
| Platform availability | 99.5 % | Jeff |
| Chem sub-modules deployed | 5/5 | Data-Team |
| Case studies validated | ≥ 3 | Vassili |
| Launch event executed | Yes | Vassili + CEO |
| Qualified leads | ≥ 50 | CEO |
| Signed contracts | €500k | CEO |
| Top-10 accounts closed | ≥ 3 | CEO |
| Multi-year deals | ≥ 2 | CEO |

- **6 weeks. No excuses. Let's go.**
