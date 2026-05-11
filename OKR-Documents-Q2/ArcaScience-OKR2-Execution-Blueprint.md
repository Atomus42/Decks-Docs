# ArcaScience OKR2 Execution Blueprint — Q2 2026

## From Platform to Proof — A 6-Week Sprint

**Sprint Period:** Q2 2026 — 6 weeks
**Phases:** Finalize (Wk1–2) → Launch (Wk3–4) → Close (Wk5–6)

**Team:**
- **Charbel** — Product Lead (Workflow & UX)
- **Jeff** — CTO / Eng Lead (Reliability & Infra)
- **Vassili** — Clinical/Chem Lead (Benefit-Risk & Validation)
- **CEO (Tom)** — Revenue Engine

---

# STRATEGIES

---

## O1 — Finalize the BRA Platform End-to-End

> All BRA pipeline steps (Context, B&R Assessment, Data Analysis, Reporting, Decision-Support) fully developed, productionized, and observable end-to-end.

**Owners:** Charbel + Jeff + Vassili

| KR | Metric | Target | Owner |
|---|---|---|---|
| KR1.1 | Pipeline steps in Prod | 5/5 | App-Team + Data-Team |
| KR1.2a | F1 Risk/Safety | ≥ 90 % | Data-Team |
| KR1.2b | F1 Efficacy | ≥ 90 % | Data-Team |
| KR1.3 | Human work per BRA | < 1 h | Data-Team + App-Team |
| KR1.4a | Availability | 99.5 % | Devops-Team |
| KR1.4b | Code tested | ≥ 85 % | App/Data-Team |
| KR1.4c | Critical/Major bugs | 0 | App/Data-Team |
| KR1.4d | Ship time | < 10 min | Devops-Team |
| KR1.4e | APM coverage | 100 % | Devops-Team |

**Definition of Done:** Data Quality Validation | Data Traceability | Platform Usage Analysis | Platform Perf Monitoring | Code Quality Gate (SonarQube) | 85 % Code Tested | End-to-End Smoke Test

Full detail: [O1 Strategy](Strategies/O1-Finalized-Platform.md)

---

## O2 — Launch i-Demo on Chemical Analysis

> Public launch of i-Demo with chemical analysis: compound search, ADMET, mechanism, bioactivity, drug-target binding — integrated in BRA, with validated case studies and launch event.

**Owners:** Vassili + Charbel

| KR | Metric | Target | Owner |
|---|---|---|---|
| KR2.1 | Chem sub-modules deployed | 5/5 + BRA-callable | Data-Team + App-Team |
| KR2.2 | Validated case studies | ≥ 3 (ext + int + LLM) | Vassili + Data-Team |
| KR2.3 | Launch event executed | Yes | Vassili + CEO |
| KR2.4 | Qualified leads captured | ≥ 50 | CEO |

Full detail: [O2 Strategy](Strategies/O2-iDemo-Chemical-Analysis.md)

---

## O3 — Close ≥ €500k Signed Contracts with Biotechs & Top-10

> €500k signed. ≥ 3 of 10 named strategic accounts closed. Weighted pipeline ≥ €2M. ≥ 2 multi-year deals.

**Owner:** CEO (Tom)

| KR | Target | Stretch | Owner |
|---|---|---|---|
| Signed contracts | €500k | €700k | CEO |
| Top-10 closed | ≥ 3 | 5 | CEO |
| Weighted pipeline | ≥ €2M | ≥ €3M | CEO |
| Multi-year deals | ≥ 2 | 3 | CEO |
| Biotech long-tail | ≥ 3 | 5 | CEO |

**Top-10:** Sanofi | Roche | Novartis | AstraZeneca | GSK | Bayer | Boehringer Ingelheim | Servier | Ipsen | UCB

Full detail: [O3 Strategy](Strategies/O3-Revenue-500k-Top10.md)

---

# PART A — PRESENT

---

## A1 — Why This Sprint Matters

This is a **proof sprint**. 3 proof points: production-grade BRA, public chem launch, €500k signed.

If we prove all three → commercially validated. If two → strong momentum. If one → sprint failed.

Full detail: [A1](Part-A-Present/A1-Why-This-Sprint-Matters.md)

---

## A2 — Value Chain

O1 (Platform) → O2 (i-Demo Chem) → O3 (Revenue). Each enables the next. Critical path: platform in Prod by Wk2 → chem module demo-ready by Wk3 → launch Wk4 → leads feed Wk5–6 closes.

Full detail: [A2](Part-A-Present/A2-Value-Chain.md)

---

## A3 — Three Objectives Overview

Summary table of all 3 objectives with KRs. Full detail: [A3](Part-A-Present/A3-Three-Objectives-Overview.md)

---

## A4 — Revenue Math

| Scenario | Total |
|---|---|
| Conservative | €355k |
| Target | €495k |
| Aggressive | €700k |

Full detail: [A4](Part-A-Present/A4-Revenue-Math.md)

---

## A5 — Pricing Architecture

3 tiers (€75k–€300k) + Chem Module add-on (€30k–€50k) + i-Demo Bundle (€50k–€75k). 5 pricing rules.

Full detail: [A5](Part-A-Present/A5-Pricing-Architecture.md)

---

## A6 — 6-Week Rhythm

| Phase | Weeks | Focus |
|---|---|---|
| FINALIZE | 1–2 | 5 steps in Prod, F1 ≥ 85 %, scope frozen |
| LAUNCH | 3–4 | Chem module live, launch event, proposals sent |
| CLOSE | 5–6 | €500k signed, 3 Top-10, 2 multi-year |

Full detail: [A6](Part-A-Present/A6-6-Week-Rhythm.md)

---

## A7 — Risk Matrix

6 risks: thin pipeline, long cycles, module delay, F1 stall, no leads, custom trap. Cut list: drug-target binding sub-module first, 3rd case study second.

Full detail: [A7](Part-A-Present/A7-Risk-Matrix.md)

---

## A8 — Failure Modes

5 ways we lose: great launch no revenue, platform not ready, Top-10 mirage, custom quicksand, launch fatigue.

Full detail: [A8](Part-A-Present/A8-Failure-Modes.md)

---

# PART B — TRACK

---

## B1 — Master OKR Scorecard

Weekly scorecard for O1 (9 KRs), O2 (7 KRs), O3 (6 KRs) with Wk1–Wk6 columns.

Full detail: [B1](Part-B-Track/B1-Master-OKR-Scorecard.md)

---

## B2 — Weekly Revenue Dashboard

CEO fills every Friday. 18 metrics tracked Wk1–Wk6 including pipeline, forecast, meetings, proposals.

Full detail: [B2](Part-B-Track/B2-Weekly-Revenue-Dashboard.md)

---

## B3 — Pipeline Tracker

Two sections: Top-10 strategic accounts (named) + Biotech long-tail deal board. Stage summary + coverage tracker.

Full detail: [B3](Part-B-Track/B3-Pipeline-Tracker.md)

---

## B4 — Account Health Tracker

Health scores 1–10, expansion triggers from APM data, bi-weekly updates.

Full detail: [B4](Part-B-Track/B4-Account-Health-Tracker.md)

---

## B5 — Deal Review Template

Per-deal template with MEDDPIC qualification, forecast category, red flag checklist.

Full detail: [B5](Part-B-Track/B5-Deal-Review-Template.md)

---

## B6 — i-Demo Launch Tracker (NEW)

Launch milestones (D-30 to D+7), KPI dashboard (Wk1–Wk6), post-launch nurture tracker.

Full detail: [B6](Part-B-Track/B6-iDemo-Launch-Tracker.md)

---

# PART C — EXECUTE

---

## C1 — Weekly Operating Cadence

5 non-negotiable meetings: Mon Sprint Kickoff, Tue Pipeline Review, Wed Chem Standup, Thu Fixing, Fri Forecast.

Full detail: [C1](Part-C-Execute/C1-Weekly-Operating-Cadence.md)

---

## C2 — Owner Checklists

Week-by-week checklists for Charbel, Jeff, Vassili, CEO — phased by Finalize/Launch/Close.

Full detail: [C2](Part-C-Execute/C2-Owner-Checklists.md)

---

## C3 — Sales Operating System

Stage definitions (S0–S6/SX), MEDDPIC qualification, disqualification triggers (tighter for 6-week sprint), red flag playbook, forecast categories.

Full detail: [C3](Part-C-Execute/C3-Sales-Operating-System.md)

---

## C4 — Chemical-Analysis Monetization Playbook (NEW)

Positioning, pricing (3 packages), anti-custom rules, sales motion for chem module.

Full detail: [C4](Part-C-Execute/C4-Chemical-Analysis-Monetization-Playbook.md)

---

## C5 — Customer Expansion Playbook

Expansion triggers, conversation framework, revenue targets.

Full detail: [C5](Part-C-Execute/C5-Customer-Expansion-Playbook.md)

---

## C6 — Founder Revenue Playbook

CEO time allocation (≥ 15 h/week), Top-10 enterprise deal playbook, biotech long-tail blitz, warm intro template.

Full detail: [C6](Part-C-Execute/C6-Founder-Revenue-Playbook.md)

---

## C7 — Meeting Agendas

Ready-to-use agendas for all 5 weekly meetings.

Full detail: [C7](Part-C-Execute/C7-Meeting-Agendas.md)

---

## C8 — 6-Week Execution Timeline

Full checkbox timeline: Wk1–2 (Finalize), Wk3–4 (Launch), Wk5–6 (Close). Every deliverable, every owner.

Full detail: [C8](Part-C-Execute/C8-6-Week-Execution-Timeline.md)

---

## C9 — i-Demo Launch Runbook (NEW)

D-30 / D-14 / D-7 / D-0 / D+7 launch plan. Positioning, asset list, channels, demo script, post-launch nurture.

Full detail: [C9](Part-C-Execute/C9-iDemo-Launch-Runbook.md)

---

# APPENDIX

---

## Appendix A — Key Definitions

24 terms including all OKR1 vocabulary (ARR, F1, BRAT, CIOMS, APM, SonarQube) plus new chemistry terms (ADMET, MoA, Bioactivity, Compound, SMILES, InChI, Drug-Target Binding, IC50/EC50, i-Demo, Top-10, Biotech Long-Tail, Multi-Year Deal).

Full detail: [Appendix A](Appendix/Appendix-A-Key-Definitions.md)

---

## Appendix B — Structural Upgrade Recommendations

3 recommendations: split revenue tracking (Top-10 vs long-tail), formalize i-Demo → pipeline handoff, post-sprint continuity plan.

Full detail: [Appendix B](Appendix/Appendix-B-Structural-Upgrade-Recommendations.md)

---

## Appendix C — Target Account Profile

Qualification checklist (Top-10 criteria + Biotech Long-Tail criteria) + named Top-10 accounts with HQ, R&D budget, why selected.

Full detail: [Appendix C](Appendix/Appendix-C-Target-Account-Profile.md)

---

## Appendix D — i-Demo Chemical Analysis Spec (NEW)

5 sub-module specifications (Compound Search, ADMET, Mechanism, Bioactivity, Drug-Target Binding). Architecture diagram. API requirements. Validation requirements. Case study selection criteria.

Full detail: [Appendix D](Appendix/Appendix-D-iDemo-Chemical-Analysis-Spec.md)

---

*ArcaScience OKR2 Execution Blueprint — Q2 2026 — From Platform to Proof*
