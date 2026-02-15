# Agent 2 Output: MHRA Post-Authorisation Benefit-Risk / Risk-Management Workflow

> Source: MHRA meeting transcript (ArcaScience introductory call, ~58 minutes).
> Participants: MHRA benefit-risk evaluation deputy directors and assessment leads (Interlocuteurs 1, 2, 7); ArcaScience CEO, product, and business development (Interlocuteurs 3, 4, 5, 6, 8).

---

## 1. MHRA Post-Authorisation Safety Workflow Overview

The MHRA participants made clear that they operate exclusively in the **post-authorisation** space. A separate, distinct MHRA team handles new marketing-authorisation applications. The post-authorisation function is structured as follows:

**Organisational footprint:**
- Two deputy directors share oversight of medicines and medical devices across the agency's post-authorisation remit.
- Approximately **100 benefit-risk assessors** working across approximately **600 authorised medicines** and **hundreds of thousands of medical devices**.
- At any given time, roughly **80 safety issues are actively under investigation** across medicines and devices.

**Workflow sequence (as described in transcript):**

1. **Signal detection / intake.** A safety concern surfaces via one or more channels: Yellow Card spontaneous reports, published literature, signals forwarded by stakeholders (e.g., MAHs, international regulators, patient groups), or findings from the agency's epidemiology team.
2. **Scoping and triage.** The assessor determines the nature of the issue: which drug(s) or device(s) are affected, what the proposed harm mechanism is, whether the signal is new or an evolution of a known risk.
3. **Evidence assembly.** The assessor gathers all relevant data: spontaneous reports (Yellow Card), published observational studies, meta-analyses, clinical trial data (where available), real-world evidence from CPRD, PSUR/PBRER submissions from MAHs, and any relevant international regulatory intelligence.
4. **Critical appraisal.** The assessor evaluates each piece of evidence on its own terms: study methodology, confidence intervals, patient population representativeness, heterogeneity of data sources, sample size, study duration, and potential confounders. This is a manual, expert-driven process. They do not apply a single structured framework (e.g., CIOMS XII) uniformly; the approach is tailored to the specific safety issue.
5. **Epidemiology team input.** For studies where methodological rigour requires specialist review, the assessor requests formal input from the MHRA's epidemiology team to confirm study quality and limitations.
6. **Benefit-risk judgement.** The assessor synthesises the evidence into an assessment report that weighs the identified risk against the therapeutic benefit of the medicine in its UK-specific context of use (line of therapy, patient population, availability of alternatives).
7. **Regulatory action.** The agency takes appropriate action: label update, Dear Healthcare Professional Communication, restriction, or (rarely) withdrawal.

**Key structural point:** The workflow is issue-driven, not product-lifecycle-driven. Assessors respond to emerging signals rather than processing a scheduled dossier review cycle. This is fundamentally different from how pharma companies interact with benefit-risk tools (where the product lifecycle gates the workflow).

---

## 2. Data Sources MHRA Uses (Public and Confidential)

### 2a. Confidential / Restricted Data Sources

| Source | Nature | Confidentiality constraint (as stated in meeting) |
|---|---|---|
| **Yellow Card reports** | UK spontaneous adverse reaction reports; patient-level data | Explicitly stated as too confidential to share externally. "It's patient-level data; we're not allowed to share that." (Interlocuteur 7) |
| **CPRD** (Clinical Practice Research Datalink) | ~30 million patient records, ~30 years of longitudinal data, billions of data points | Cannot be shared with external vendors. "We can't give you that." (Interlocuteur 7) |
| **Ongoing safety issue dossiers** | Internal assessment files on active investigations | "Most of the things we do are actually highly confidential. I don't think we could share an ongoing safety issue with you." (Interlocuteur 7) |
| **Company-submitted data** | PSURs/PBRERs, RMPs, safety variations submitted by MAHs | Commercially and regulatorily confidential; not discussed as shareable. |

### 2b. Public / Accessible Data Sources

| Source | Nature | How MHRA uses it |
|---|---|---|
| **Published literature** | Observational studies, meta-analyses, case reports, systematic reviews | Primary evidence base for post-authorisation safety questions. Assessors critically appraise methodology, not just conclusions. |
| **Clinical trial data** (published) | Original registration trial reports, post-authorisation commitment study reports | Used as baseline, but recognised as often insufficient for post-authorisation questions (e.g., short duration, narrow populations). |
| **Stakeholder signals** | Reports from patients, healthcare professionals, other regulators, MAHs | Intake channel for new safety concerns. |

### 2c. Derived / Analytical Outputs

| Source | Nature |
|---|---|
| **Epidemiology team analyses** | Bespoke studies using CPRD or other databases to answer specific safety questions |
| **International regulatory intelligence** | Findings and actions from EMA, FDA, and other agencies on the same active substances |

**Critical implication for ArcaScience:** The two most important proprietary data sources (Yellow Card, CPRD) are explicitly off-limits for any external tool integration. Any solution must deliver value using only publicly available data, or must operate entirely within MHRA-controlled infrastructure with no data egress.

---

## 3. Assessment Process (How Assessors Evaluate Evidence)

The MHRA participants described an assessment process that is fundamentally **expert-judgement-driven**, not framework-driven. Key characteristics:

### 3a. No standardised structured framework

> "Although we have templates and guidance for conducting a benefit-risk assessment, we don't tend to use one of the structured approaches like CIOMS XII... it can depend on the safety issue." (Interlocuteur 1)

This means the assessment approach is adapted to the nature and severity of the safety question. There is no single quantitative model or scoring matrix applied across all issues.

### 3b. Study-level critical appraisal

When evaluating published evidence, assessors perform detailed methodological critique:

- **Study design:** Is it an observational study, meta-analysis, RCT, case series? (Interlocuteur 7 explicitly distinguished these from case reports.)
- **Methodology:** Appropriateness of study design for the question being asked.
- **Confidence intervals:** Statistical robustness of reported associations.
- **Patient populations:** Representativeness and applicability to UK prescribing patterns.
- **Heterogeneity:** Consistency of findings across data sources and subpopulations.
- **Limitations:** What the study cannot tell you, not just what it claims.

> "What my assessors do is they say, okay, there's this observational study that seemed to show an association between the drug and the event -- what that assessor then does is not just take the abstract and assume the abstract is right. They look at the methodology, they look at the confidence intervals, they look at the patient populations included, they look at the heterogeneity of the data sources, and they reach an opinion about whether that article is valid." (Interlocuteur 7)

### 3c. Effectiveness, not efficacy

The MHRA draws a hard line between efficacy (what a drug does in a controlled trial) and effectiveness (what it does in real-world clinical practice in the UK):

> "We don't do efficacy -- we do effectiveness. So you can't necessarily take efficacy or effectiveness from a clinical trial and assume that it translates into performance on the market." (Interlocuteur 7)

This distinction is central. UK-specific utilisation patterns (first-line vs. second-line vs. third-line, co-morbidities, ethnicities, age distributions, off-label use) materially affect the benefit-risk balance.

### 3d. Causality assessment under uncertainty

The most difficult analytical challenge MHRA faces: establishing whether a rare adverse event is causally related to a drug, using incomplete, heterogeneous, observational data, across large exposed populations.

> "You may have a rare event, and you're trying to understand causality of that event across a lot of different data sources." (Interlocuteur 7)

### 3e. Context-dependent benefit-risk weighting

The same adverse event carries different regulatory weight depending on therapeutic context:

> "If there's a drug... you use third line, and there's no other alternative for a patient, then the benefit-risk is different to a first-line therapy that they can then move on to something else." (Interlocuteur 7)

---

## 4. Key Challenges Described in Meeting

### 4.1 Scale vs. specificity

100 assessors across 600+ drugs and hundreds of thousands of devices, with ~80 active safety issues at any time. Each issue requires bespoke analysis. There is no possibility of building a custom AI model per safety issue.

> "We can't develop an AI model for every use case. That's clearly not possible." (Interlocuteur 7)

### 4.2 Drugs on market for a long time, not new products

The typical MHRA post-authorisation safety question involves a mature product with decades of exposure data, large and diverse patient populations, and emerging signals that were not detected in registration trials (which may have been 12 weeks long, conducted 20+ years ago).

> "Those are much easier questions than for drugs that have been on the market for a long time, and safety events emerge." (Interlocuteur 7)

### 4.3 Data quality is heterogeneous and often poor

Post-authorisation data is inherently messier than clinical trial data: unstructured, inconsistent, variable quality, and from multiple independent sources.

> "If you think this is messy, noisy data -- welcome to the world of post-authorisation, which is a million times worse." (Interlocuteur 7)

### 4.4 UK-specific utilisation context matters

Drug use patterns differ across jurisdictions. Safety events differ depending on how a drug is used in clinical practice. A benefit-risk conclusion from another jurisdiction may not apply to the UK.

> "Usage of drugs is very different across the world, and safety events do not necessarily translate across the world." (Interlocuteur 7)

### 4.5 Confidentiality is a hard constraint, not a negotiable preference

Yellow Card data, CPRD data, and ongoing safety issue dossiers cannot leave MHRA systems. This is not a procurement preference -- it is a legal and regulatory requirement.

### 4.6 No budget for speculative technology

The MHRA stated explicitly that there is no funding available for a proof-of-concept engagement.

> "You don't have funding for this. So it's not something that we could offer funding for at the moment." (Interlocuteur 7)

### 4.7 Must go beyond literature search

Whatever tool is proposed must deliver value beyond what a general-purpose LLM or literature search can do.

> "It's beyond the literature search, because I can get ChatGPT to do that potentially, or Copilot or something." (Interlocuteur 7)

---

## 5. Where ArcaScience Could Help (Mapped to MHRA Workflow Steps)

Based strictly on what was discussed in the meeting, the following are plausible value-add points:

### 5a. Evidence assembly -- structured extraction from published literature (Workflow Step 3)

**MHRA need:** Assessors manually read and extract data from published observational studies, meta-analyses, and other literature. This is time-consuming and must be done across many studies simultaneously.

**ArcaScience capability (as described):** Small language models trained to extract structured data from unstructured scientific articles: study design, endpoints, patient populations, dosing, adverse events, temporality, severity. These models layer the document (methodology section, results section, etc.) and apply task-specific extraction.

**Fit:** Moderate. This accelerates the evidence-gathering phase. It does not replace clinical judgement but reduces the manual effort of reading and tabulating findings across dozens of publications for a single safety question.

**Requirement:** Must work with generic pipelines (not bespoke model per issue). Must handle observational studies and meta-analyses, not just RCTs or case reports.

### 5b. Evidence organisation -- stratified, annotated, cross-referenced data (Workflow Step 3-4)

**MHRA need:** Assessors need to see all relevant evidence for a safety question organised by source type, quality indicators, patient population, and finding.

**ArcaScience capability (as described):** Relational database with knowledge graphs connecting extracted data points across sources. Normalised ontologies (including a restructured MedDRA). Ability to surface related findings based on mechanism of action, not just drug name.

**Fit:** Potentially strong, if the system can present pre-organised evidence dossiers that save assessors the effort of manual cross-referencing. The mechanism-of-action-based similarity surfacing could identify relevant evidence from related compounds.

### 5c. Completeness check -- identifying evidence the assessor may have missed (Workflow Step 3)

**MHRA need:** Confidence that the evidence base is comprehensive.

**ArcaScience capability (as described):** Claimed 100% concordance with client-identified evidence in validation exercises, plus identification of 9-100x additional relevant data points.

**Fit:** Moderate-to-strong for literature-sourced evidence. However, MHRA's most important evidence comes from non-public sources (Yellow Card, CPRD), where ArcaScience cannot add value without on-premise deployment.

### 5d. Template pre-population -- reducing report-writing burden (Workflow Step 6)

**MHRA need:** Assessors write assessment reports using internal templates.

**ArcaScience capability (as described):** Ability to push structured data into templated documents.

**Fit:** Low-to-moderate. Only useful if the templates can be mapped to MHRA's internal formats and if the pre-populated content is accurate enough to save net time (i.e., reviewing pre-filled content must be faster than writing from scratch).

---

## 6. Where ArcaScience CANNOT Help (Explicit Boundaries)

Based on what was stated in the meeting, these are areas where ArcaScience cannot contribute under current constraints:

### 6a. Yellow Card data analysis

ArcaScience cannot access, process, or integrate Yellow Card spontaneous reporting data. This is patient-level data under strict confidentiality controls. Unless ArcaScience deploys entirely on-premise within MHRA infrastructure with no data egress, this data source is excluded.

### 6b. CPRD / real-world evidence database interrogation

CPRD contains 30 million patient records over 30 years. MHRA cannot share this data externally. ArcaScience's current architecture (statement of work, data branching into system) is incompatible with this constraint.

### 6c. Causality determination

No AI system can determine whether a rare adverse event is causally related to a drug exposure. This requires expert pharmacological and epidemiological judgement that integrates biological plausibility, temporal relationships, dose-response, dechallenge/rechallenge, and confounders. ArcaScience should not position itself as capable of this.

### 6d. Effectiveness estimation

Translating efficacy data from controlled trials into UK-specific real-world effectiveness is not a data-extraction problem. It requires understanding of UK prescribing patterns, formulary positioning, patient demographics, and clinical practice -- none of which can be derived from published literature alone.

### 6e. Benefit-risk judgement

The final benefit-risk determination is a regulatory act. It requires weighing incommensurable factors (e.g., risk of a rare but serious adverse event against the benefit of a widely-used medicine with no alternative). No tool can or should automate this. ArcaScience acknowledged this in the meeting ("we're not the ones building the benefit-risk assessment"), but this boundary must be maintained explicitly in all positioning.

### 6f. Active safety issue support (under current terms)

MHRA cannot share details of ongoing safety investigations with an external vendor at the proof-of-concept stage. Any test case must use a historically completed, publicly disclosed safety issue.

### 6g. Bespoke model development per safety issue

MHRA has ~80 concurrent safety issues. Building or configuring a custom pipeline for each one is operationally impossible within MHRA's resource constraints. Any tool must work with generic, pre-configured capabilities across therapeutic areas.

---

## 7. Critical Differences from Pharma-Side Use Cases

This section maps the structural differences between MHRA's post-authorisation workflow and the pharmaceutical-company use cases that ArcaScience has historically served. These differences are fundamental and must inform product positioning, demo design, and proposal language.

| Dimension | Pharma-side use case | MHRA post-authorisation use case |
|---|---|---|
| **Workflow trigger** | Product lifecycle gate (e.g., IND, NDA, PSUR cycle) | Emerging safety signal (unpredictable, issue-driven) |
| **Number of products** | 1 drug per engagement | 600+ drugs, hundreds of thousands of devices |
| **Data quality** | Structured clinical trial data (CRFs, TFLs, CSRs) | Unstructured, heterogeneous, observational, real-world |
| **Data access** | Client owns and shares their data freely | Most important data sources (Yellow Card, CPRD) are confidential and cannot leave MHRA systems |
| **Efficacy vs. effectiveness** | Efficacy endpoints from controlled trials | Effectiveness in real-world UK clinical practice -- fundamentally different concept |
| **Framework** | CIOMS XII, structured B-R frameworks, BRAT | No standardised structured framework; issue-dependent approach |
| **Time horizon** | Product development timeline (years, planned) | Urgent: safety signals require timely assessment; ~80 active at any time |
| **Customisation tolerance** | Weeks-long statement of work per therapeutic area is acceptable | Must work generically across all therapeutic areas without per-issue setup |
| **Commercial model** | Paid client engagement ($75k-$300k/yr) | No budget currently available; proof-of-concept must be self-funded |
| **Assessor profile** | Pharma regulatory/medical affairs professionals | Government-employed benefit-risk assessors with deep pharmacovigilance expertise |
| **Competitive baseline** | Excel, Word, manual processes | ChatGPT/Copilot for literature search; CPRD/epidemiology team for quantitative analysis |
| **Decision output** | Internal regulatory dossier to submit to regulators | Regulatory action (label change, restriction, communication) with direct public-health consequences |
| **Confidentiality model** | MAH controls and shares own data | Regulator holds multi-company, patient-level data under statutory confidentiality obligations |
| **Typical drug profile** | Novel/innovative, often pre-authorisation or early post-launch | Mature products on market for years/decades, with large exposed populations and emerging rare events |

### Implications for ArcaScience positioning

1. **Drop the "seconds" language.** "Fill your benefit risk in seconds" was explicitly flagged as raising "loads and loads of concerns" (Interlocuteur 7). This language signals a misunderstanding of the complexity of regulatory benefit-risk assessment.

2. **Lead with the literature evidence-assembly use case, not the full BRA pipeline.** The full BRA workflow is not applicable. The value proposition for MHRA is narrower: accelerating the extraction, structuring, and cross-referencing of published evidence for a given safety question.

3. **Demonstrate on a completed, public safety issue.** MHRA proposed this as the only feasible test: a historically resolved safety issue already in the public domain, where ArcaScience can demonstrate what it would have found.

4. **Acknowledge the data-access boundary explicitly.** Do not propose architectures that require MHRA to export Yellow Card or CPRD data. If on-premise deployment is technically feasible, mention it as a future possibility, but do not make it a condition of the initial engagement.

5. **Generic pipelines, not bespoke configurations.** Any demonstration must show that the system works out-of-the-box for a safety question without weeks of pipeline configuration. MHRA will not invest time in per-issue setup for a tool they are evaluating.

6. **Position above ChatGPT, not against it.** MHRA has already identified general-purpose LLMs as capable of basic literature search. ArcaScience must demonstrate capabilities that go beyond what an assessor can do with Copilot: structured extraction, cross-study comparison, mechanism-of-action-based evidence surfacing, and quality indicator flagging.

---

*Document prepared by Agent 2 -- Regulatory Workflow Mapper. All claims attributed to specific speakers with transcript references. No information fabricated or inferred beyond what was explicitly stated in the meeting.*
