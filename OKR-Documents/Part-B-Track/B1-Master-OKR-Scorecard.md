# B1 — Master OKR Scorecard (Update Weekly)

> Copy these tables into Notion, Airtable, or a shared spreadsheet. Fill them in weekly. Review them in your Tuesday + Friday rituals.

---

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

### O2 — Disease-Specific Platform Version (Owner: Vassili — Medical Team)

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

### O3 — Revenue Engine: $500k Income (60% ARR/40% non-ARR) (Owner: CEO, supported by all)

| KR | Metric | Owner | Weekly KPI | Wk1 | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Wk7 | Wk8 | Wk9 | Wk10 | Wk11 | Wk12 | Target | Stretch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KR1 | ARR closed (cumulative $) | CEO | New ARR this week | | | | | | | | | | | | | $500k | $650k |
| KR2 | New logos (cumulative) | CEO | Logos signed | | | | | | | | | | | | | 5 | 7 |
| KR3 | Expansions (cumulative) | CEO/Prod | Expansions closed | | | | | | | | | | | | | 1 | 4 |
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

**Cross-references:**
- See [O1 — BRA Platform Strategy](/OKR-Documents/Strategies/O1-BRA-Platform.md)
- See [O2 — Disease-Specific Platform Strategy](/OKR-Documents/Strategies/O2-Disease-Specific-Platform.md)
- See [O3 — Revenue Engine Strategy](/OKR-Documents/Strategies/O3-Revenue-Engine.md)

---

*Extracted from ArcaScience OKR Execution Blueprint — Part B*
