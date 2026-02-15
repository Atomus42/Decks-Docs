# Proof-of-Concept Collaboration Plan: ArcaScience x MHRA

**Prepared by Agent 6 (Collaboration Designer)**
**Date: 2026-02-15**
**Classification: For internal preparation only -- draft for ArcaScience leadership review before any MHRA submission**

---

## 0. Design Principles

This plan is built around six hard constraints drawn directly from the MHRA meeting transcript:

1. **Public-domain data only.** Allison stated: "most of the things that we do are actually highly confidential" and "I don't think we could share an ongoing safety issue with you." The only path is a safety issue "already in the public domain that we've already reported on."
2. **Zero funding required.** "You don't have funding for this... it's not something that we could offer funding for." ArcaScience bears all cost. MHRA contributes assessor time for review and feedback only.
3. **Not bespoke.** "We can't develop an AI model for every use case... how could you give out something generic?" The demonstration must use ArcaScience's existing pipeline and generic algorithms, not a custom model trained for the chosen safety issue.
4. **Post-authorisation focus.** Allison wants to see performance on "long-marketed drugs, rare events, causality challenges, noisy/incomplete data." New drug authorisation cases are "much easier" and would not impress.
5. **Beyond literature search.** The system must go "beyond a literature search" and "beyond what ChatGPT could do." This means structured extraction, critical appraisal, traceability, and evidence synthesis -- not keyword retrieval.
6. **Proof of concept, not production deployment.** "It really would be a proof of concept where we were just testing or challenging your system." The deliverable is an evaluation, not an operational tool.

---

## 1. PoC Selection Criteria

Any candidate safety issue must satisfy all of the following:

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | **Closed or publicly reported** | MHRA cannot share confidential ongoing assessments. The issue must have been publicly reported with regulatory conclusions already published. |
| 2 | **Long-marketed drug class** | Allison explicitly stated that new/rare product authorization is "much easier." The test must involve drugs with decades of post-marketing exposure. |
| 3 | **Substantial public-domain evidence base** | There must be enough accessible literature, regulatory public assessment reports, safety communications, and observational studies to build a meaningful evidence map without any proprietary MHRA data. |
| 4 | **Messy, heterogeneous evidence** | The evidence base must include the types MHRA deals with daily: spontaneous reports (aggregated/published), observational studies, case reports, meta-analyses, mechanistic studies, and real-world data analyses -- not just clean RCTs. |
| 5 | **Multi-regulator action** | Ideally MHRA, EMA (PRAC), and FDA all published independent assessments, allowing cross-referencing and demonstrating the system's ability to reconcile different regulatory conclusions. |
| 6 | **UK-specific considerations** | Issues where MHRA took distinct UK-specific action (different timing, different restrictions, or additional measures beyond EU harmonisation) are preferred because they are most relevant to the audience. |
| 7 | **Causality complexity** | The issue should involve genuine causality challenges -- confounding, reverse causation, or difficulty distinguishing drug effect from underlying disease -- reflecting the "hard part" Allison described. |
| 8 | **Sufficient volume to stress-test extraction** | At minimum 100+ relevant publications across study types to demonstrate the pipeline handles scale, not just a handful of pivotal papers. |

---

## 2. Three Candidate PoC Options

### Option A: SGLT2 Inhibitors and Diabetic Ketoacidosis (DKA)

**RECOMMENDED as primary candidate**

#### Drug class and safety issue

Sodium-glucose co-transporter 2 (SGLT2) inhibitors -- canagliflozin, dapagliflozin, empagliflozin -- are oral antidiabetics first authorised in the EU in 2012-2014. Post-marketing surveillance identified a rare but serious risk of diabetic ketoacidosis (DKA), often presenting atypically with near-normal blood glucose levels ("euglycaemic DKA"). This atypical presentation delayed diagnosis in multiple cases and led to coordinated regulatory action across MHRA, EMA, and FDA between 2015 and 2016, with follow-up safety communications extending to 2022.

#### Why it is a good test case for MHRA

- **Causality complexity:** The DKA signal involved distinguishing drug-induced ketoacidosis from disease-related events in a population (type 2 diabetes) already at baseline risk. Multiple precipitating factors (infection, surgery, fasting, insulin reduction) confounded the picture. Euglycaemic presentation was mechanistically unexpected and initially controversial.
- **Evidence heterogeneity:** The evidence base spans spontaneous reporting data (Yellow Card, FAERS), clinical trial re-analyses, observational cohort studies, mechanistic hypotheses, case series, systematic reviews, and real-world database studies. This is precisely the messy mix MHRA assessors work with.
- **Evolving signal:** The signal emerged gradually. Initial FDA communication (May 2015) was based on just 20 cases. EMA triggered a formal Article 20 procedure (June 2015). MHRA published updated advice (April 2016). Further perioperative guidance followed (2022). This evolution tests the system's ability to map a signal across time.
- **Post-marketing, long-marketed class:** By the time of the reviews, SGLT2 inhibitors had accumulated millions of patient-years of exposure. The signal emerged from post-authorisation use, not clinical trials.
- **Generic applicability:** The question -- "Does this drug class cause this rare serious adverse event, and in what context?" -- is the archetypal post-marketing pharmacovigilance question. Demonstrating capability here directly addresses Allison's request for generic pathways.

#### Key public-domain sources

| Source | Document | URL |
|--------|----------|-----|
| **MHRA** | Drug Safety Update: SGLT2 inhibitors -- updated advice on the risk of diabetic ketoacidosis (April 2016) | https://www.gov.uk/drug-safety-update/sglt2-inhibitors-updated-advice-on-the-risk-of-diabetic-ketoacidosis |
| **EMA** | SGLT2 inhibitors -- Article 20 referral page (includes PRAC assessment report, scientific conclusions, and CHMP opinion) | https://www.ema.europa.eu/en/medicines/human/referrals/sglt2-inhibitors |
| **EMA** | PRAC Assessment Report -- SGLT2 inhibitors Article 20 procedure (full assessment) | https://www.ema.europa.eu/en/documents/referral/sglt2-inhibitors-article-20-procedure-assessment-report_en.pdf |
| **EMA** | PRAC press release: recommendations to minimise risk of DKA (Feb 2016) | https://www.ema.europa.eu/en/news/sglt2-inhibitors-prac-makes-recommendations-minimise-risk-diabetic-ketoacidosis |
| **FDA** | SGLT2 Inhibitors: Drug Safety Communications and safety page (May 2015 onward) | https://www.fda.gov/Drugs/DrugSafety/ucm446852.htm |
| **FDA** | Label revision notice: warnings about too much acid in the blood (Dec 2015) | https://www.fda.gov/files/drugs/published/FDA-revises-labels-of-SGLT2-inhibitors-for-diabetes-to-include-warnings-about-too-much-acid-in-the-blood-and-serious-urinary-tract-infections.pdf |
| **Literature** | Frontiers in Pharmacology systematic review and network meta-analysis (2023) | https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2023.1145587/full |
| **Literature** | NEJM: Risk of DKA after initiation of SGLT2 inhibitor (2017) | https://www.nejm.org/doi/full/10.1056/NEJMc1701990 |
| **Literature** | PMC: FAERS data analysis -- SGLT2 and DKA (2017) | https://pubmed.ncbi.nlm.nih.gov/28500396/ |

#### What ArcaScience would demonstrate

1. Automated identification and classification of all publicly available evidence sources (literature, regulatory documents, safety communications) relevant to SGLT2-DKA across multiple regulators.
2. Structured extraction of critical appraisal elements from each source: study design, population, sample size, outcome definitions, confounders assessed, effect sizes, confidence intervals, limitations acknowledged by authors.
3. Evidence map showing the temporal evolution of the signal from first reports through regulatory action.
4. Cross-source reconciliation: how MHRA, EMA, and FDA assessed the same evidence and where their conclusions aligned or diverged.
5. Traceability: every extracted data element linked back to its source document, section, and page.
6. Gap analysis: identification of evidence types present vs. absent (e.g., UK-specific incidence data, mechanism-of-action confirmation studies).

#### Complexity level

**Medium-High.** Rich evidence base, genuine causality complexity, multi-regulator involvement, atypical clinical presentation complicating signal detection. Not the most politically sensitive topic (unlike valproate), which reduces friction for a first collaboration.

---

### Option B: Fluoroquinolone Antibiotics and Disabling/Irreversible Side Effects

#### Drug class and safety issue

Fluoroquinolone antibiotics (ciprofloxacin, levofloxacin, moxifloxacin, ofloxacin) have been marketed since the late 1980s. Over decades, a pattern of disabling and potentially permanent side effects emerged -- tendonitis and tendon rupture, peripheral neuropathy, psychiatric effects (depression, psychosis, suicidal ideation), and aortic aneurysm. These effects can persist for months or years after drug discontinuation and may be irreversible. Regulatory action culminated in EMA's Article 31 referral (2017-2019), MHRA's risk minimisation review (2023), and multiple FDA safety communications and boxed warnings (2008-2018).

#### Why it is a good test case for MHRA

- **UK-specific regulatory action:** MHRA conducted its own risk minimisation review in 2023, published a Public Assessment Report, and introduced additional UK-specific restrictions (January 2024) going beyond the 2019 EU-harmonised measures. This makes it directly relevant to MHRA's own recent work.
- **Evidence spanning decades:** The signal evolved from initial tendon-related warnings in the 2000s through to the "FQAD" (Fluoroquinolone-Associated Disability) concept in 2015, with multiple waves of regulatory action. The literature spans 30+ years.
- **Patient involvement:** The MHRA review incorporated patient and carer testimony (February and May 2023 CHM meetings) and received 53 public consultation responses. The evidence includes patient-reported outcomes and lived-experience data alongside clinical evidence.
- **Risk minimisation effectiveness question:** MHRA found that despite 2019 restrictions, prescribing patterns had not changed. This is an ongoing effectiveness question that the evidence synthesis must address.
- **Multiple organ systems:** The side effect profile spans musculoskeletal, neurological, psychiatric, cardiovascular, and sensory systems -- testing the extraction pipeline's ability to handle multi-system adverse events.

#### Key public-domain sources

| Source | Document | URL |
|--------|----------|-----|
| **MHRA** | Drug Safety Update: Fluoroquinolone antibiotics -- must now only be prescribed when other commonly recommended antibiotics are inappropriate (Jan 2024) | https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-must-now-only-be-prescribed-when-other-commonly-recommended-antibiotics-are-inappropriate |
| **MHRA** | Drug Safety Update: Reminder of disabling and potentially long-lasting or irreversible side effects (Aug 2023) | https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-reminder-of-the-risk-of-disabling-and-potentially-long-lasting-or-irreversible-side-effects |
| **MHRA** | Drug Safety Update: New restrictions and precautions for use (2019) | https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-new-restrictions-and-precautions-for-use-due-to-very-rare-reports-of-disabling-and-potentially-long-lasting-or-irreversible-side-effects |
| **MHRA** | Public Assessment Report: Review of risk minimisation for fluoroquinolone antibiotics | https://www.gov.uk/government/publications/review-of-risk-minimisation-for-disabling-and-potentially-long-lastingirreversible-side-effects-associated-with-fluoroquinolone-antibiotics |
| **MHRA** | Press release: MHRA introduces new restrictions for fluoroquinolone antibiotics | https://www.gov.uk/government/news/mhra-introduces-new-restrictions-for-fluoroquinolone-antibiotics |
| **EMA** | Quinolone and fluoroquinolone referral page (Article 31, full documentation) | https://www.ema.europa.eu/en/medicines/human/referrals/quinolone-fluoroquinolone-containing-medicinal-products |
| **EMA** | PRAC Assessment Report -- Article 31 referral | https://www.ema.europa.eu/en/documents/referral/quinolone-and-fluoroquinolone-article-31-referral-assessment-report_en.pdf |
| **EMA** | Press release: PRAC recommends new restrictions on use (Oct 2018) | https://www.ema.europa.eu/en/news/fluoroquinolone-quinolone-antibiotics-prac-recommends-new-restrictions-use-following-review-disabling-potentially-long-lasting-side-effects |
| **EMA** | Reminder: Measures to reduce risk of long-lasting side effects (2023) | https://www.ema.europa.eu/en/news/fluoroquinolone-antibiotics-reminder-measures-reduce-risk-long-lasting-disabling-potentially-irreversible-side-effects |
| **FDA** | Drug Safety Communication: FDA updates warnings for fluoroquinolones due to disabling side effects (July 2016) | https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-updates-warnings-oral-and-injectable-fluoroquinolone-antibiotics |
| **FDA** | FDA approves safety labeling changes for fluoroquinolones | https://www.fda.gov/drugs/information-drug-class/fda-approves-safety-labeling-changes-fluoroquinolones |

#### What ArcaScience would demonstrate

1. Everything listed for Option A, plus:
2. Longitudinal evidence mapping across 30+ years of accumulating safety signals, showing how the evidence base grew and how regulatory actions escalated.
3. Multi-system adverse event extraction: demonstrating the pipeline can handle a drug class linked to effects across musculoskeletal, neurological, psychiatric, cardiovascular, and sensory domains simultaneously.
4. Risk minimisation effectiveness assessment: extracting and synthesising evidence on whether previous regulatory interventions changed prescribing behaviour (directly relevant to the 2023 MHRA review finding that they did not).
5. Integration of qualitative evidence (patient testimony, public consultation responses) alongside quantitative clinical data.

#### Complexity level

**High.** Very large evidence base spanning decades, multiple organ system effects, evolving regulatory position, patient advocacy involvement, and the added dimension of risk minimisation effectiveness assessment. This would be the most ambitious demonstration but also the most impressive if executed well.

---

### Option C: Sodium Valproate and Pregnancy Risks (Teratogenicity and Neurodevelopmental Harm)

#### Drug class and safety issue

Sodium valproate (Epilim, Depakote) has been marketed since 1972 for epilepsy and since the 1990s for bipolar disorder and migraine prophylaxis. Evidence of teratogenicity (congenital malformations in approximately 10% of exposed pregnancies) accumulated from the 1980s onward. Evidence of neurodevelopmental harm (developmental delay, reduced IQ, autism spectrum disorder in up to 30-40% of exposed children) emerged more gradually through the 2000s and 2010s. This culminated in one of the most significant UK drug safety actions in recent history: the MHRA's Pregnancy Prevention Programme, the EMA's Article 31 referral (2017-2018), and the Independent Medicines and Medical Devices Safety Review ("First Do No Harm" report, July 2020, chaired by Baroness Cumberlege).

#### Why it is a good test case for MHRA

- **Landmark UK safety issue:** Valproate is arguably the most prominent UK drug safety issue of the past decade. The Cumberlege Review criticised the healthcare system as "disjointed, siloed, unresponsive and defensive" and recommended substantial MHRA reform. Demonstrating capability on this issue would resonate deeply with MHRA assessors.
- **Massive, heterogeneous evidence base:** The literature includes pregnancy registry data (across multiple countries), birth defect surveillance studies, neurodevelopmental cohort studies, mechanistic research, case reports, systematic reviews, and meta-analyses. Real-world data from UK Clinical Practice Research Datalink (CPRD) and other databases has been published.
- **Evolving risk characterisation:** The signal moved from physical malformations (established by 1984) to neurodevelopmental harm (established by 2010s) to male-mediated reproductive risk (emerging 2024). This tests the system's ability to track an evolving evidence landscape.
- **Regulatory divergence:** EMA mandated a Pregnancy Prevention Programme (2018). MHRA adopted this and then strengthened it further. FDA issued a black box warning but has no mandatory REMS program, creating a regulatory divergence the system could map.

#### Key public-domain sources

| Source | Document | URL |
|--------|----------|-----|
| **MHRA** | Valproate: review of safety data and expert advice on management of risks (Public Assessment Report, Nov 2023) | https://www.gov.uk/government/publications/valproate-review-of-safety-data-and-expert-advice-on-management-of-risks |
| **MHRA** | Drug Safety Update: Valproate Pregnancy Prevention Programme -- updated educational materials | https://www.gov.uk/drug-safety-update/valproate-epilim-depakote-pregnancy-prevention-programme-updated-educational-materials |
| **MHRA** | Drug Safety Update: Valproate use in men -- precautionary contraception advice (2024) | https://www.gov.uk/drug-safety-update/valproate-use-in-men-as-a-precaution-men-and-their-partners-should-use-effective-contraception |
| **EMA** | Valproate and related substances -- Article 31 referral page (full documentation) | https://www.ema.europa.eu/en/medicines/human/referrals/valproate-related-substances-0 |
| **EMA** | PRAC Assessment Report -- Valproate Article 31 referral | https://www.ema.europa.eu/en/documents/referral/valproate-article-31-referral-prac-assessment-report_en.pdf |
| **EMA** | Press release: PRAC recommends new measures to avoid valproate exposure in pregnancy (Feb 2018) | https://www.ema.europa.eu/en/news/prac-recommends-new-measures-avoid-valproate-exposure-pregnancy |
| **EMA** | Press release: New measures to avoid valproate exposure in pregnancy endorsed (Mar 2018) | https://www.ema.europa.eu/en/news/new-measures-avoid-valproate-exposure-pregnancy-endorsed |
| **IMMDS Review** | "First Do No Harm" -- full report (July 2020) | https://www.immdsreview.org.uk/Report.html |
| **IMMDS Review** | "First Do No Harm" -- downloadable PDF | https://www.immdsreview.org.uk/downloads/IMMDSReview_Web.pdf |
| **Literature** | PMC: "First do no harm: valproate and medicines safety in pregnancy" (2020) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7518898/ |

#### What ArcaScience would demonstrate

1. Everything listed for Option A, plus:
2. Long-horizon evidence mapping: tracking the accumulation of evidence from 1984 to present across multiple risk dimensions (malformations, neurodevelopment, male-mediated risk).
3. Cross-regulatory divergence analysis: mapping how MHRA/EMA/FDA assessed the same evidence but took different regulatory actions (mandatory PPP vs. black box warning only).
4. Integration of non-traditional evidence: the Cumberlege Review is not a standard pharmacovigilance document -- it is a system-wide safety review. Demonstrating extraction from this type of source shows versatility.
5. Risk minimisation effectiveness: extracting published data on whether the Pregnancy Prevention Programme has achieved its objectives (prescribing trend studies, pregnancy register data).

#### Complexity level

**Very High.** The largest and most politically sensitive evidence base of the three options. The Cumberlege Review's criticism of MHRA itself adds a dimension of institutional sensitivity. While this would be the most powerful demonstration, it carries higher risk of MHRA discomfort if the system surfaces evidence critical of the agency's own past performance.

---

## 2.1 Recommendation

**Primary recommendation: Option A (SGLT2 inhibitors and DKA).**

Rationale:
- Best balance of complexity and manageability for a first proof of concept.
- Rich, well-bounded evidence base with clear regulatory endpoints (the 2016 MHRA/EMA/FDA actions).
- Genuine causality complexity (euglycaemic DKA, confounders, off-label use in T1DM) that will test the system meaningfully.
- Low political sensitivity -- unlike valproate, there is no history of MHRA being publicly criticised on this issue.
- Multi-regulator public documentation allows cross-referencing without any proprietary data.
- The question it addresses ("Does this drug class cause this rare SAE, and under what circumstances?") is the generic post-marketing pharmacovigilance question Allison asked ArcaScience to solve.

**Backup: Option B (Fluoroquinolones)** if MHRA prefers a case with deeper UK-specific action and a larger evidence base.

**Reserve: Option C (Valproate)** only if MHRA specifically requests it. Do not propose this first -- it risks surfacing institutional sensitivity about the Cumberlege Review.

---

## 3. Success Metrics

### 3.1 Quantitative Metrics

| Metric | Definition | Target | How Measured |
|--------|-----------|--------|-------------|
| **Time savings** | Wall-clock time for ArcaScience pipeline to produce evidence map + structured extraction vs. estimated manual effort for equivalent output | Report pipeline completion time; benchmark against MHRA estimate of manual effort for similar scope | ArcaScience timestamps pipeline stages; MHRA assessors estimate manual equivalent |
| **Source completeness** | Percentage of key evidence sources independently identified by ArcaScience pipeline, benchmarked against the reference list in the published MHRA/EMA/PRAC assessment report | >= 90% of sources cited in the published regulatory assessment are identified by the pipeline | Independent comparison of pipeline output against citation list in published PRAC/MHRA assessment report |
| **Extraction accuracy** | Percentage of extracted data elements (study design, sample size, effect size, outcome definition, limitations) that match source document when independently audited | >= 95% factual accuracy on audited sample (minimum 50 extractions spot-checked) | Blinded audit by MHRA assessor or independent reviewer comparing extracted elements to source |
| **Traceability completeness** | Percentage of extracted elements with a verifiable link to source document, section, and page/paragraph | 100% -- every extracted element must have a traceable source reference | Systematic check of source links in output |
| **Critical appraisal coverage** | Percentage of the following study quality indicators extracted when present in source: study design, population description, sample size, follow-up duration, outcome definitions, confounders assessed, statistical methods, effect sizes with CIs, limitations, funding/COI disclosure | >= 80% of applicable quality indicators extracted per source | Structured review of extraction output against a pre-defined checklist of critical appraisal elements |
| **Error rate** | Proportion of extracted elements containing factual errors, hallucinations, or misattributions | < 2% on audited sample | Independent audit of randomly sampled extractions |
| **False negatives** | Relevant sources present in the public evidence base but missed by the pipeline | < 10% of sources cited in reference assessment | Gap analysis comparing pipeline output to reference |

### 3.2 Qualitative Metrics

| Metric | Definition | How Measured |
|--------|-----------|-------------|
| **Assessor satisfaction** | MHRA assessors' subjective assessment of whether the output would be useful in their actual work | Semi-structured feedback session at end of Phase 2; assessors rate utility, trust, and usability on a 5-point scale |
| **"Beyond literature search" test** | Whether the output provides structured, synthesised value that assessors could not achieve with a standard literature search or ChatGPT query | Direct assessor comparison: "Could you have gotten this from PubMed + ChatGPT?" Yes/No with explanation |
| **Assessor trust** | Whether assessors feel comfortable relying on any element of the output without independent verification | Feedback on which output elements they would use vs. which they would re-verify |
| **Actionability** | Whether the evidence map and structured output could plausibly inform a real regulatory assessment if it were an active (not historical) issue | Assessor judgment: "If this were a live signal, would this output accelerate your assessment?" |

---

## 4. Deliverables MHRA Would Receive

All deliverables are produced by ArcaScience at its own expense using only public-domain data. MHRA receives outputs for evaluation purposes only.

### 4.1 Evidence Map

A comprehensive, structured inventory of all relevant public-domain sources identified for the chosen safety issue, including:

- **Source identification:** Full citation, document type (regulatory assessment, clinical trial publication, observational study, case report, meta-analysis, safety communication, mechanistic study, real-world data analysis).
- **Classification:** Each source tagged by evidence type, study design, population, geographic scope, and date.
- **Temporal mapping:** Visualisation of when evidence became available relative to regulatory actions.
- **Relevance scoring:** Each source scored for direct relevance to the safety question, with justification.

### 4.2 Structured Extraction Output

For each identified source, a structured extraction of:

- **Study characteristics:** Design, population, sample size, follow-up duration, setting, inclusion/exclusion criteria.
- **Key findings:** Primary outcomes, effect sizes, confidence intervals, statistical significance, secondary findings.
- **Critical appraisal elements:** Confounders assessed, biases identified by authors, limitations, quality indicators (e.g., Newcastle-Ottawa scale score for observational studies, Cochrane risk-of-bias for RCTs where applicable).
- **Regulatory relevance:** Which elements of the study were cited in regulatory assessments and how they were interpreted.

### 4.3 Templated Draft Sections

Structured output organised in a format analogous to PSUR/DSUR safety evaluation sections:

- Summary of the safety concern
- Clinical trial evidence
- Spontaneous reporting data (published aggregate data only)
- Observational/epidemiological studies
- Mechanistic evidence
- Regulatory actions taken (cross-jurisdictional comparison)

These are draft structures populated from extracted evidence, not finished regulatory documents. They demonstrate how the pipeline organises evidence, not how it replaces assessor judgment.

### 4.4 Traceability Report

A complete audit trail showing:

- Every extracted data element linked to its source document, section, and page/paragraph.
- The pipeline step that produced the extraction (which model, which processing stage).
- Confidence score for each extraction (see below).
- Any conflicts between sources flagged with both versions preserved.

### 4.5 Confidence Scoring

Each extracted element receives a confidence score based on:

- **Source reliability:** Regulatory assessment > peer-reviewed systematic review > peer-reviewed primary study > case report > grey literature.
- **Extraction certainty:** Was the element explicitly stated in the source or inferred? Direct quotation vs. paraphrase vs. interpretation.
- **Consistency:** Does this element agree or conflict with other sources?

Scores are transparent and auditable. Low-confidence extractions are flagged for human review.

### 4.6 Gap Analysis

Identification of:

- Evidence types present in the published regulatory assessment that the pipeline could not access (e.g., unpublished sponsor data, confidential ICSR line listings).
- Evidence types that should exist based on the safety question but were not found in the public literature.
- Geographic gaps (e.g., UK-specific incidence data available or missing).
- Temporal gaps (e.g., no studies covering the period after 2020).

This gap analysis is critical because it demonstrates the system knows what it does not know -- a key trust signal for regulators.

---

## 5. Timeline

### Phase 0: Joint Scoping (Week 0)

**Duration:** 1 meeting (60 minutes) + 1 week for written confirmation of scope.

**Activities:**
- ArcaScience presents the three candidate safety issues with rationale (this document).
- MHRA selects one (or proposes an alternative that meets the selection criteria).
- Joint agreement on:
  - Exact scope of the safety question (e.g., "SGLT2 inhibitors and risk of DKA in type 2 diabetes patients, focused on the period 2013-2022").
  - Data boundaries: confirm public-domain only; enumerate specific source types in scope.
  - Success criteria: agree on the metrics in Section 3 and any MHRA additions.
  - MHRA assessor(s) who will review Phase 1 outputs and their availability for Phase 2.
- ArcaScience and MHRA sign a lightweight collaboration letter (not a contract) confirming:
  - No confidential MHRA data will be shared.
  - No funding changes hands.
  - All outputs are for evaluation purposes and not for regulatory use.
  - MHRA retains full discretion over whether to continue beyond Phase 2.

**ArcaScience resource commitment:** Project lead + 1 scientist for scoping.
**MHRA resource commitment:** 1-2 assessors for a single 60-minute meeting + email confirmation of scope.

### Phase 1: Evidence Assembly and Extraction (Weeks 1-2)

**Duration:** 2 weeks.

**Activities:**
- **Week 1:** Pipeline ingestion and evidence map construction.
  - Identify and ingest all public-domain sources for the chosen safety issue.
  - Classify sources by type, design, population, geography, and date.
  - Produce draft evidence map.
  - Run extraction pipeline on all ingested sources.
  - Generate structured extraction output with traceability links and confidence scores.
- **Week 2:** Quality review and deliverable preparation.
  - Internal QC: ArcaScience scientists review extraction accuracy on a sample of sources.
  - Produce templated draft sections, traceability report, confidence scoring summary, and gap analysis.
  - Package all deliverables for MHRA review.
  - Prepare comparison: ArcaScience outputs vs. the published regulatory assessment (which elements match, which are missing, which are additional).

**ArcaScience resource commitment:** Project lead, 2 scientists, engineering support for pipeline configuration.
**MHRA resource commitment:** None during this phase (ArcaScience works independently).

### Phase 2: Joint Review and Feedback (Week 3)

**Duration:** 1 week, centred on a single 90-minute review session.

**Activities:**
- ArcaScience delivers all outputs to MHRA assessors 2-3 business days before the review session.
- **Review session (90 minutes):**
  - 15 min: ArcaScience walks through outputs and methodology.
  - 30 min: MHRA assessors review evidence map and structured extractions, comparing to their historical assessment of the same issue.
  - 20 min: Deep dive on traceability -- assessors select specific extracted elements and trace them back to source.
  - 15 min: Assessors provide feedback on utility, accuracy, trust, and gaps.
  - 10 min: Discuss whether there is a basis for continued collaboration and, if so, what form it would take.
- ArcaScience documents all feedback and produces a summary report.

**ArcaScience resource commitment:** Project lead + 2 scientists for the session; 1 scientist for feedback documentation.
**MHRA resource commitment:** 1-2 assessors for the 90-minute session + optional written feedback afterward.

### Total elapsed time: 4 weeks from kickoff to completion.

### Total MHRA time commitment: approximately 3-4 hours of assessor time across the entire PoC.

---

## 6. Next Meeting Agenda (60 Minutes)

This agenda is for the follow-up meeting with MHRA to propose and scope the PoC. It is designed to address Allison's stated concerns and demonstrate ArcaScience's seriousness and preparation.

| Time | Item | Purpose | Lead |
|------|------|---------|------|
| 0:00-0:10 | **Confirm use case and data boundaries** | Present the three candidate safety issues. Ask MHRA to confirm or modify selection. Agree on exact scope, data boundaries, and what "success" looks like. | ArcaScience (present) / MHRA (decide) |
| 0:10-0:25 | **Under-the-hood walkthrough** | Walk through the pipeline architecture (Document 03), model cards, validation approach, and traceability mechanism. This directly addresses Allison's request to understand "what's under the bonnet" and her concern about "loads and loads of concerns" with opaque AI claims. No marketing slides. Technical depth. | ArcaScience |
| 0:25-0:45 | **Live demo on chosen public safety issue** | Show the pipeline running on the agreed public safety issue in real time. Demonstrate ingestion, classification, extraction, and traceability on 3-5 representative sources. Show how the system handles a case report differently from a systematic review. Show a confidence score calculation. This is the "show, don't tell" moment. | ArcaScience |
| 0:45-0:55 | **Review outputs and traceability** | Walk through sample outputs: evidence map, structured extraction, traceability report. Invite assessors to pick any extracted element and trace it back to source. Demonstrate the gap analysis -- what the system knows it does not know. | ArcaScience (present) / MHRA (challenge) |
| 0:55-1:00 | **Agree next steps** | Confirm whether MHRA is comfortable proceeding with the PoC. Agree on timeline, assessor availability, and communication channel. Confirm the lightweight collaboration letter scope. | Joint |

### Preparation required before this meeting

- ArcaScience must have a working demo ready on at least one of the candidate safety issues (ideally Option A, SGLT2/DKA) using exclusively public-domain sources.
- ArcaScience must have the technical architecture walkthrough (Document 03) refined and ready to present.
- ArcaScience must have the data governance framework (Document 04) ready to reference if MHRA raises data handling questions.
- All marketing materials and website claims must be updated per Document 05 recommendations before the meeting. Under no circumstances should the meeting materials contain "in seconds," "18 months to seconds," or "100% regulatory acceptance rate" language.

---

## 7. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| MHRA declines all three options and proposes an alternative we have not prepared for | Medium | Medium | Selection criteria (Section 1) are designed to apply to any candidate. ArcaScience pipeline is generic -- it can be redirected to a different safety issue within 1 week. Ask MHRA at the scoping meeting to propose alternatives early. |
| Pipeline extraction accuracy falls below target on messy observational study data | Medium | High | Run internal dry runs on all three candidate issues before the scoping meeting. Identify weakest evidence types and pre-configure extraction templates. Be transparent about limitations in the demo -- Allison values honesty over polish. |
| MHRA assessors find the output "not beyond what ChatGPT could do" | Medium | Critical | The differentiators are: (a) structured extraction of critical appraisal elements, not just summaries; (b) traceability to source at the paragraph level; (c) confidence scoring; (d) gap analysis; (e) cross-source reconciliation. Ensure the demo foregrounds these, not the evidence retrieval step. |
| MHRA internal governance prevents even a public-data collaboration without formal agreement | Low | High | Propose the lightest possible structure: a collaboration letter (not a contract), no data exchange, no funding, no IP implications. If needed, frame it as "MHRA reviewing a publicly available report" rather than "collaboration." |
| Valproate option triggers institutional sensitivity about Cumberlege Review | Medium | Medium | Do not propose valproate first. Present it as a third option only. If MHRA raises it, acknowledge the sensitivity and frame the demo as "evidence synthesis support" not "re-assessment of MHRA's historical decisions." |
| ArcaScience marketing materials visible online contradict the measured tone of the PoC proposal | High | High | Implement Document 05 recommendations before the meeting. Assume MHRA has already reviewed the website and deck. Any discrepancy between what is said in the meeting and what is on the website will destroy credibility. |

---

## 8. What This PoC Is and Is Not

### It IS:

- A test of whether ArcaScience's generic pipeline can add value to the evidence assembly and critical appraisal steps of a post-marketing safety assessment.
- A demonstration of traceability, structured extraction, and evidence synthesis -- capabilities that go beyond literature search.
- A low-cost, low-risk way for MHRA to evaluate the system without committing data, funding, or institutional endorsement.
- A foundation for a relationship built on transparency and demonstrated value, not marketing claims.

### It IS NOT:

- A replacement for assessor judgment. The system assembles and structures evidence. Assessors evaluate it.
- A product demonstration or sales pitch. There is no commercial ask attached to this PoC.
- An attempt to access confidential MHRA data. All inputs are public domain.
- A bespoke model. The pipeline is the same one that would be used for any safety issue. The only configuration is the safety question and source corpus.
- A finished regulatory output. The templated sections are illustrative, not submission-ready.

---

## Appendix A: Comparison of the Three Options

| Criterion | Option A: SGLT2/DKA | Option B: Fluoroquinolones | Option C: Valproate |
|-----------|---------------------|---------------------------|---------------------|
| Drug class age | 10+ years on market | 35+ years on market | 50+ years on market |
| Evidence volume | ~200-300 publications | ~500+ publications | ~1000+ publications |
| Evidence heterogeneity | High (RCTs, observational, case reports, FAERS, mechanistic) | Very high (adds patient testimony, risk minimisation studies, prescribing data) | Very high (adds pregnancy registries, neurodevelopmental cohorts, system-wide review) |
| Multi-regulator documentation | MHRA + EMA + FDA public documents available | MHRA + EMA + FDA public documents available | MHRA + EMA + FDA + Cumberlege Review |
| UK-specific action | MHRA Drug Safety Update (2016, 2022) | MHRA Public Assessment Report + additional restrictions (2023-2024) | MHRA PPP + Public Assessment Report + Cumberlege Review |
| Causality complexity | High (euglycaemic presentation, confounders) | High (delayed onset, multi-system, dose-duration relationship unclear) | Moderate (teratogenicity well-established; neurodevelopmental dose-response more complex) |
| Political sensitivity | Low | Medium (patient advocacy groups active) | High (Cumberlege Review criticised MHRA directly) |
| Manageability for first PoC | Best | Good | Challenging |
| **Overall recommendation** | **Primary** | **Backup** | **Reserve** |
