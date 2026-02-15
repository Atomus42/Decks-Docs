# ArcaScience x MHRA: Collaboration Base Document

**Classification:** Source of truth for deck preparation and follow-up meeting
**Prepared:** 2026-02-15
**Status:** Internal -- not for external distribution without review

---

## 1. Executive Summary

### What MHRA asked

During an introductory meeting, three senior MHRA post-authorisation safety staff -- including Deputy Director Allison, assessment lead Steph, and governance lead Sharinto -- evaluated whether ArcaScience's evidence-structuring platform could support their benefit-risk assessment work. MHRA's post-authorisation function covers approximately 600 medicines and hundreds of thousands of medical devices, with roughly 80 concurrent safety investigations at any given time, staffed by approximately 100 benefit-risk assessors.

The MHRA participants raised the following requirements and concerns, in order of emphasis:

1. **Post-authorisation focus.** MHRA works exclusively in the post-authorisation space. Their data is messy, unstructured, observational, and heterogeneous. The platform must demonstrate utility with this reality, not with clean clinical trial datasets. ("How do you solve my problem rather than this problem?" -- Allison)
2. **Transparency and auditability.** The platform cannot operate as a "black box." Every output must be traceable to its source document and extraction step. ("That's fundamental for us to understand." -- Steph)
3. **Scalability without bespoke models.** MHRA cannot build a custom model for each of 80+ concurrent safety issues across 600+ drugs. The system must work generically. ("We can't develop an AI model for every use case. That's clearly not possible." -- Allison)
4. **Confidentiality.** Yellow Card patient-level data, CPRD records, and ongoing safety investigations cannot be shared externally. ("We can't give you our yellow card data because that's far too confidential." -- Allison)
5. **Value beyond general-purpose AI.** The platform must offer structured extraction, provenance, and synthesis capabilities that go beyond what ChatGPT or Copilot can do for literature search. ("It's beyond the literature search because I can get ChatGPT to do that." -- Allison)
6. **No funding available.** MHRA has no budget for a proof-of-concept engagement. ("It's not something that we could offer funding for at the moment." -- Allison)
7. **Messaging credibility.** Claims such as "benefit-risk in seconds" and "100% regulatory acceptance" triggered strong scepticism. ("My antibodies are going through the roof." -- Allison)

The senior decision-maker stated she is "not convinced yet" but is "really keen to look for ways to create efficiency" and needs to "see under the hood."

### What we propose next

A self-funded, public-domain proof of concept on a completed, publicly reported safety issue (recommended: SGLT2 inhibitors and diabetic ketoacidosis). ArcaScience runs its existing generic pipeline against publicly available evidence only, produces a structured evidence package with full traceability, and MHRA assessors compare the output against their own historical assessment of the same issue.

This is preceded by a 60-minute technical deep-dive meeting covering: use-case confirmation, under-the-hood architecture walkthrough, live demonstration on representative sources, output review with traceability challenge, and agreement on next steps.

**MHRA investment:** Approximately 3-4 hours of assessor time over 4 weeks. **Confidentiality risk:** Zero -- no MHRA data is involved at any stage.

---

## 2. What ArcaScience Is -- and What It Is NOT

### What ArcaScience is

ArcaScience is an evidence-structuring platform that uses 24 task-specific small language models arranged in a sequential pipeline to ingest, classify, extract, normalise, link, and template regulatory and scientific documents. The system processes published literature, clinical trial registries, regulatory documents, and (where authorised) client-provided private data. Its output is a structured, traceable evidence package -- not a finished assessment or regulatory conclusion. The platform is designed to reduce the manual effort of evidence assembly, cross-referencing, and template pre-population so that qualified human assessors can invest more time in critical appraisal, contextual judgment, and decision-making. The platform is inspired by the ICH E2C(R2) guideline and BRAT framework.

### What ArcaScience is NOT

| Boundary | Explanation |
|----------|-------------|
| **Not a decision-making system** | The platform does not render benefit-risk verdicts, determine causality, or produce regulatory recommendations. All judgment remains with the human assessor. |
| **Not a replacement for assessor expertise** | The system extracts and structures evidence. It does not assess study quality, evaluate methodology, or weigh competing evidence. |
| **Not a generative AI chatbot** | Outputs are structured, templated documents with traceable provenance -- not free-text generated answers. The system does not operate like ChatGPT or similar large language models. |
| **Not a tool that requires bespoke model-building per use case** | The 24 models are task-specific (e.g., adverse-event extraction, study-design classification), not therapeutic-area-specific. Adaptation to a new drug or safety question is achieved through pipeline configuration, not model retraining. |
| **Not a tool that processes imaging or omics data** | These data types are outside the current platform scope. Omics data is planned for a future R&D programme (BR-PREDICT, 2026-2029) and is not part of the current operational platform. |
| **Not a tool that handles the "full drug lifecycle" without qualification** | The system covers evidence structuring across pre-clinical through post-authorisation phases for semantic/textual data sources. It does not cover all data types or all analytical activities at every phase. |

---

## 3. MHRA Workflow Fit: Post-Authorisation Safety and Risk Management

### MHRA's post-authorisation workflow (as described in the meeting)

MHRA's post-authorisation safety function is issue-driven, not product-lifecycle-driven. The workflow proceeds through:

1. **Signal detection / intake.** A safety concern surfaces via Yellow Card spontaneous reports, published literature, stakeholder signals (MAHs, international regulators, patient groups), or the epidemiology team.
2. **Scoping and triage.** The assessor determines the nature of the issue: which drug(s) or device(s) are affected, what the proposed harm mechanism is, whether the signal is new or an evolution of a known risk.
3. **Evidence assembly.** The assessor gathers all relevant data: spontaneous reports, published observational studies, meta-analyses, clinical trial data (where available), real-world evidence from CPRD, PSUR/PBRER submissions from MAHs, and international regulatory intelligence.
4. **Critical appraisal.** The assessor evaluates each piece of evidence on its own terms: study methodology, confidence intervals, patient population representativeness, heterogeneity, sample size, duration, and potential confounders. This is a manual, expert-driven process tailored to the specific safety issue.
5. **Epidemiology team input.** For studies requiring specialist methodological review, the assessor requests formal input from the MHRA's epidemiology team.
6. **Benefit-risk judgment.** The assessor synthesises the evidence into an assessment report that weighs the identified risk against therapeutic benefit in the UK-specific context of use.
7. **Regulatory action.** Label update, Dear Healthcare Professional Communication, restriction, or (rarely) withdrawal.

This workflow is fundamentally different from pharmaceutical-company use cases. It is issue-driven rather than lifecycle-driven; it involves 600+ drugs simultaneously rather than one; it relies on messy observational data rather than structured trial outputs; and it requires UK-specific contextualisation that global data cannot provide.

### Where we help

| Workflow step | How the platform supports it |
|---------------|------------------------------|
| **Evidence assembly (Step 3)** | Automated identification, retrieval, and structuring of published literature and regulatory documents relevant to a specified safety question. Classification by study type, population, design, and key findings. Mechanism-of-action-based evidence surfacing across related compounds. |
| **Structured extraction (Step 3-4)** | Extracts study design, population characteristics, sample sizes, adverse event terms, temporal relationships, dosage information, effect sizes, confidence intervals, and limitations from unstructured sources into normalised, queryable formats. Each extraction linked to source sentence. |
| **Cross-referencing and evidence mapping (Step 3)** | Connects extracted entities across sources using standardised ontologies (MedDRA, SNOMED CT, ChEBI). Temporal mapping of when evidence became available relative to regulatory actions. |
| **Completeness checking (Step 3)** | Identifies evidence gaps: source types, geographic coverages, or time periods where expected evidence is absent. Surfaces what the evidence base lacks, not just what it contains. |
| **Signal triage support (Step 1-2)** | Organises candidate signals by frequency, co-occurrence, and source type, flagging areas of higher or lower confidence for assessor prioritisation. |
| **Template pre-population (Step 6)** | Pre-fills structured template sections (analogous to PSUR/DSUR safety evaluation sections) with extracted, sourced evidence for assessor review and completion. |

### Where we do NOT replace MHRA

| Function | Why it remains with the assessor |
|----------|----------------------------------|
| **Causality determination** | Establishing whether a drug caused an adverse event requires integrating biological plausibility, temporal relationships, dose-response, dechallenge/rechallenge evidence, and confounders. This is expert pharmacological and epidemiological judgment. |
| **Study quality and validity assessment** | The platform extracts the elements assessors use to judge quality (methodology, CIs, population, heterogeneity, limitations) but does not itself render a quality verdict. |
| **Benefit-risk conclusions** | The final weighing of benefits against risks is a regulatory act with legal, clinical, and ethical implications. It requires contextual judgment about UK-specific prescribing patterns, patient populations, therapeutic alternatives, and societal values. |
| **Policy and regulatory decisions** | Label changes, communications, restrictions, and withdrawals are institutional decisions informed by -- but not determined by -- evidence assembly. |
| **Real-world effectiveness estimation** | Translating efficacy data from controlled trials into UK-specific real-world effectiveness requires understanding of UK prescribing practice, formulary positioning, and patient demographics. MHRA works with effectiveness, not efficacy. |

---

## 4. "Under the Hood": System Overview and Auditability

### 4.1 High-level pipeline

The system processes documents through a sequential, chained pipeline. Each step produces auditable intermediate output before feeding the next step. The pipeline operates on 24 task-specific small language models (SLMs), not a single monolithic large language model.

```
INGEST --> CLASSIFY --> SECTION ID --> EXTRACT --> RELATE --> NORMALISE --> LINK --> TEMPLATE

Legend: --> = auditable handoff; intermediate output inspectable at each boundary
```

| Step | Function | Output |
|------|----------|--------|
| **Ingest** | Accepts PDF, XML, DOC, and other semantic sources | Raw document in standardised internal format |
| **Classify** | Determines document type (case report, clinical trial, observational study, meta-analysis, regulatory document) | Document classification label with study design metadata (randomised, blinded, arms, etc.) |
| **Section identification** | Identifies structural sections (abstract, methodology, results, discussion, safety) | Section boundaries with labels, routing downstream extraction to appropriate sections |
| **Extract** | Extracts entities: adverse events, temporal status, drug names, severity, outcomes, patient demographics, study design elements, dosage | Structured entity records with source sentence references |
| **Relate** | Links extracted entities within context (e.g., "myocardial infarction is related to adalimumab in this sentence") | Entity-relationship pairs with sentence-level provenance |
| **Normalise** | Maps extracted terms to standardised ontologies (restructured MedDRA, SNOMED CT, ChEBI, Disease Ontology) | Normalised entity codes |
| **Link** | Connects entities across documents in a knowledge graph | Cross-source entity connections within the Profiling Base |
| **Template** | Populates structured output formats | Assessor-ready structured evidence package (evidence maps, templated draft sections, traceability reports) |

**Key architectural principle:** Every arrow in this pipeline represents an auditable boundary. The output of each step can be independently inspected and verified before it feeds the next step. There is no single opaque model producing end-to-end results.

**Infrastructure:** Apache Airflow DAGs ("Data Forge" pipelines) orchestrate execution on AWS Kubernetes. Storage: S3 (raw and enriched data), ElasticSearch (full-content indexing and analysis outputs), DocumentDB (structured documents), QDrant (ontology vectors). BRA platform: ReactJS/Tailwind CSS frontend, Node.js/NestJS backend, PostgreSQL database. Authentication: Keycloak (OAuth 2.0, OpenID Connect) with JWT-based role-based access control.

### 4.2 Traceability: every extracted statement links back to source

Every extracted element in the platform output links back to its source document, section, and sentence. As stated by ArcaScience's CEO in the meeting: "The information that comes in and comes out is auditable at both ends, and then is used on the next step auditable at both ends. So there is no black box in between."

| Provenance element | Description | Current status |
|-------------------|-------------|----------------|
| **Source document** | Original document (with DOI/PMID/URL) | Operational |
| **Source location** | Section, page, and sentence within the document | Operational |
| **Extraction model** | Which of the 24 SLMs produced the extraction | Operational (architectural principle) |
| **Confidence score** | Per-element confidence level | Planned (OKR Initiative 3) -- not yet operational |
| **Disagreement flags** | Where models or sources disagree on the same entity | Planned (OKR Initiative 3) -- not yet operational |
| **Missing evidence indicators** | Where expected evidence is absent | Planned (OKR Initiative 3) -- not yet operational |
| **Evidence Provenance Layer** (first-class UI feature) | Integrated audit trail in the platform interface | Planned (OKR Initiative 2) -- not yet operational |

Confidence scoring, disagreement flags, and missing evidence indicators are critical features for regulatory trust and are honestly presented as in-development, not as current capabilities.

### 4.3 Model scope: "task-specific models" vs. "therapeutic-area models"

This distinction is central to the scalability question MHRA raised.

The 24 SLMs are trained for **specific tasks**, not for specific therapeutic areas. Each model performs one well-defined extraction or classification function regardless of the disease or drug under review.

| Model category | Example function | Scope |
|---------------|------------------|-------|
| Document classification | Determines study type (RCT, observational, case report, meta-analysis) | All therapeutic areas |
| Section identification | Identifies document structure (methodology, results, discussion) | All document types |
| Safety entity extraction | Extracts adverse event terms, temporal status, severity, outcomes | All drugs, all events |
| Efficacy endpoint extraction | 4-model chain: extract, structure, cluster, normalise | All therapeutic areas, phases 1-4 |
| Relation extraction | Links drug to event within sentence context | All drug-event combinations |
| Patient information | Extracts demographics (gender, age, population) | All study types |
| Study design extraction | Extracts sample size, duration, blinding, arms, placebo | All study designs |
| Drug/dosage extraction | Extracts dose, frequency, administration route | All drugs |
| Normalisation | Maps extracted terms to standardised ontologies | All therapeutic areas |

**No new model is trained** when a new therapeutic area is addressed. The same 24 models operate across all therapeutic areas. The models were trained on 10,000+ documents spanning all therapeutic areas and all clinical phases (1-4).

**Adaptation to a specific safety question** happens through pipeline configuration, not model retraining:
- Selecting which database subsets to query (reducing noise from irrelevant pathologies)
- Enabling/disabling specific model outputs (e.g., deactivating efficacy models when only safety is relevant)
- Defining which ontology subsets to prioritise
- Selecting the output template and format

This is architecturally distinct from training a separate model per disease, which would not scale to MHRA's 600+ drug portfolio with 80+ concurrent safety issues. An assessor investigating antidepressants and sexual dysfunction uses the same extraction models as one investigating SGLT2 inhibitors and DKA. Only the query scope differs.

### 4.4 Error localisation (how we detect where a mistake happened across chained steps)

Because each SLM performs a single, well-defined task and produces inspectable output at each step boundary, errors can be localised to the specific step where they occurred:

| Step | What goes wrong if this step errs | How the error is detected |
|------|----------------------------------|--------------------------|
| Document classification | All downstream extraction operates on wrong assumptions (e.g., treating an observational study as an RCT) | Reviewer verifies document type assignment against the actual document |
| Section identification | Extraction models look in wrong sections of the document | Reviewer verifies section boundaries |
| Entity extraction | Specific entities are missed or miscategorised | Reviewer compares extracted entities against source text |
| Relation extraction | Associations between drugs and events are incorrect | Reviewer verifies the relation against the source sentence |
| Normalisation | Terms are mapped to wrong ontology codes | Reviewer verifies ontology mapping |
| Knowledge graph linking | Cross-source associations may be spurious | Reviewer inspects link rationale |

**Error metrics from internal test sets:** Clinician-annotated test sets (dual-annotated independently by two clinicians) yield measurable error rates per step. Example metrics shared: approximately 10% missed data, approximately 5% miscategorised data, with clustering errors reported separately. Target F1 scores for safety and efficacy extraction pipelines: >= 85%.

**Items not yet documented (TBD / requires confirmation):**
- Formal error propagation analysis across the full chain (how a 5% error in Step 3 compounds through Steps 4-6)
- Automatic flagging when upstream errors may have affected downstream outputs
- Formal methodology for measuring inter-step error correlation
- Current measured F1 scores for each of the 24 models (targets are documented; actual performance values not published in reviewed materials)
- Precision/recall breakdown per model (critical for pharmacovigilance, where false negatives are more consequential than false positives)
- Inter-annotator agreement rate for the clinician-annotated test sets
- Whether there are therapeutic areas or document types where model performance is significantly lower
- Specific SLM architectures and parameter counts
- Model versioning and change control procedures
- Whether the system has undergone independent third-party audit or validation
- Formal quality management system compliance (ISO 13485, IEC 62304, GAMP 5)

---

## 5. Data Sources and Confidentiality Model (MHRA-Safe)

### 5.1 Public sources (Tier 1 -- no MHRA data required)

These sources are openly available and already indexed in ArcaScience's Profiling Base. No MHRA data or access is involved.

| Source | Access method | Notes |
|--------|--------------|-------|
| PubMed / MEDLINE | ArcaScience Profiling Base (already indexed) | Literature articles, systematic reviews, meta-analyses |
| ClinicalTrials.gov | ArcaScience Profiling Base (already indexed) | Trial registries, protocols, results |
| Product labels / SmPCs | Public regulatory databases (MHRA, EMA, FDA) | UK-specific labelling from MHRA public site |
| MHRA Public Assessment Reports (PARs) | MHRA public website | Historical assessments already in the public domain |
| MHRA Drug Safety Updates, alerts | MHRA public website | Only those already published by MHRA |
| WHO / Uppsala Monitoring Centre public signals | Publicly available | Published signal assessments |
| FAERS (FDA Adverse Event Reporting System) | Public download / API | US pharmacovigilance data; publicly available |
| EudraVigilance public aggregate data | EMA access portal | European ADR data at aggregate level |

### 5.2 Private sources (MHRA internal -- Tier 3, never leaves MHRA)

| Source | Classification | Handling rule |
|--------|---------------|---------------|
| **Yellow Card reports** (patient-level) | Strictly confidential | Must remain within MHRA infrastructure at all times. No extraction, no transmission, no external processing. "It's patient-level data; we're not allowed to share that." -- Allison |
| **CPRD** (30M patients, 30 years) | Restricted access | Any processing must occur in-situ within MHRA's secure environment. "We can't give you that." -- Allison |
| **Ongoing safety issue dossiers** | Highly confidential | Cannot be shared with external parties while under active review. "Most of the things that we do are actually highly confidential." -- Allison |
| **Company-submitted data** (PSURs, PBRERs, RMPs, safety variations) | Commercially confidential | Multi-company data under statutory confidentiality obligations |
| **Completed internal assessments** (unpublished) | Confidential | Available only if MHRA chooses to declassify or publish |

Design principle: MHRA handles data from multiple companies simultaneously. Data from Company A's product must never be visible in work on Company B's product. This multi-tenant confidentiality requirement is structurally different from single-company pharmaceutical client engagements.

### 5.3 "Data never leaves MHRA" approach

**Phase 1 (proof of concept): Public-domain data only.**

All processing occurs on ArcaScience infrastructure using Tier 1 sources. Zero MHRA data enters ArcaScience systems. MHRA selects the topic, ArcaScience produces the output, and MHRA evaluates internally against their own historical assessment. No confidentiality risk.

**Phase 2+ (future, if warranted): On-premises deployment within MHRA infrastructure.**

ArcaScience has described a client-side deployment model where "the data never leaves the client side." The 100% Kubernetes infrastructure is, in principle, portable to on-premises clusters. Under this model:

- ArcaScience models are deployed into MHRA's environment
- All data remains within MHRA's infrastructure boundary
- No data is transmitted to ArcaScience servers
- MHRA IT controls access, networking, and audit logging
- ArcaScience provides model artefacts and configuration support only

On-premises deployment is planned in the ArcaScience OKR documentation ("on-prem readiness assessment" as a deliverable, "non-negotiable on-premises readiness for enterprise" under Initiative 4) and is included in the Enterprise tier pricing. However, it is not yet confirmed as delivered.

**Feasibility items requiring confirmation (TBD / requires confirmation):**
- Whether all 24 SLMs can operate fully air-gapped (no outbound connectivity)
- Specific hardware requirements (GPU specifications, storage, network bandwidth)
- Containerisation and deployment packaging for MHRA infrastructure
- Licensing model for on-premises deployment
- Model update and maintenance procedures in an isolated environment
- Latency and performance benchmarks for on-prem vs. cloud
- Whether Keycloak can integrate with MHRA's identity infrastructure

On-premises deployment should be treated as a Phase 2+ objective, investigated only after the public-domain proof of concept has established trust.

### 5.4 Handling large RWD sources (e.g., CPRD)

CPRD (30 million patient records, 30 years) represents the most data-intensive scenario. The proposed pattern is **in-place query processing** ("bring the algorithm to the data"):

- ArcaScience extraction models are deployed inside the secure environment hosting CPRD
- Models query the data; data does not move
- Outputs are de-identified, statistical-level summaries only (incidence rates, relative risks, confidence intervals) -- no patient-level records extracted
- MHRA assessors define query parameters; models execute extraction; MHRA reviews aggregate output

**Critical items not yet built (TBD / requires confirmation):**
- CPRD-specific connector has not been developed
- Data schema mapping between CPRD structure and ArcaScience ingestion pipeline is undefined
- Performance characteristics at CPRD scale (30M patients) are untested
- Whether MHRA's CPRD access terms permit third-party algorithm execution is unknown
- CPRD has its own governance framework requiring independent approval

CPRD integration should not be discussed as a near-term deliverable.

### 5.5 Security controls and UK government compliance

**Documented ArcaScience security capabilities:**

| Control | Implementation |
|---------|---------------|
| Authentication | Keycloak with OAuth 2.0 and OpenID Connect |
| Authorisation | JWT-based Role-Based Access Control (RBAC) |
| API security | Rate limiting, request throttling, comprehensive structured logging |
| Infrastructure | 100% Kubernetes on AWS |
| Code quality | SonarQube quality gates enforced on all production deployments |

**Claimed certifications** (from ArcaScience public materials; independent verification not confirmed): ISO 27001, GDPR, FDA 21 CFR Part 11, HIPAA, HDS (French health data hosting). MHRA should request copies of relevant certificates and audit reports during any formal evaluation.

**UK government requirements likely needed (all TBD / requires confirmation):**

| Requirement | Description | Status |
|-------------|-------------|--------|
| Cyber Essentials Plus | UK government baseline cybersecurity certification | Not documented |
| NHS DSPT | Data Security and Protection Toolkit | Not documented |
| UK GDPR / DPA 2018 | UK-specific data protection provisions | Not documented (EU GDPR only) |
| G-Cloud listing | UK government cloud services marketplace | Not documented |
| Data residency | UK-based data centre hosting | AWS region not specified |
| DPIA | Data Protection Impact Assessment | Would need joint development |

---

## 6. Quality Control and Uncertainty Handling

### 6.1 What we can measure automatically

| Capability | How it works | Current status |
|-----------|-------------|----------------|
| **Missingness detection** | Identifies where expected data fields are absent from a source (e.g., no CIs reported, no follow-up duration stated) and flags the gap | Described as current capability |
| **Contradictory evidence flags** | Where sources disagree on the same drug-event association, both versions are preserved and presented side by side with full provenance | Described as current capability; formal conflict-resolution methodology TBD |
| **Provenance tracking** | Every extracted data element linked to source document, section, page/paragraph, and extraction step | Operational for source-to-statement linkage |
| **Extraction confidence** | Per-element scoring based on extraction certainty (explicit statement vs. inferred), source reliability (regulatory assessment > systematic review > primary study > case report), and cross-source consistency | Planned (OKR Initiative 3); not yet operational as first-class feature |
| **Data completeness metrics** | Percentage of expected data fields populated per source type | Described as measurable per analysis |
| **Evidence gap identification** | Systematic identification of missing evidence types, geographic coverage gaps, or temporal gaps in the assembled evidence base | Part of planned deliverables |

### 6.2 What we cannot "judge" automatically -- but we can extract the elements assessors use

| Dimension | What the system extracts | What the assessor determines |
|-----------|-------------------------|------------------------------|
| **Study validity** | Study design, population, sample size, methodology description, statistical methods, limitations acknowledged | Whether the methodology is adequate for the question being asked |
| **Clinical significance** | Effect sizes, confidence intervals, p-values where reported | Whether the effect is clinically meaningful in context |
| **Bias assessment** | Study design features indicating potential bias (unblinded, no placebo arm, single-centre, industry-funded) | The overall risk of bias and its implications for the findings |
| **Causality** | Temporal relationships, dose-response data, dechallenge/rechallenge data, mechanistic evidence where reported | Whether the association is causal |
| **UK applicability** | Geographic origin of study population, indication, dosing regimen | Whether the findings apply to UK prescribing patterns and patient demographics |

This distinction is the core of the system's regulatory positioning: it performs extraction and structuring, not evaluation and judgment. As stated in the meeting: "We don't assume if the study has quality or not. We tell you the sample size was 100. It was for 6 months."

### 6.3 How we support critical appraisal

For each source processed, the system extracts and presents the following critical appraisal elements (where reported in the source):

- **Study design classification** -- RCT, cohort, case-control, case series, case report, meta-analysis, systematic review
- **Population characteristics** -- age, sex, comorbidities, geographic setting, inclusion/exclusion criteria
- **Sample size and follow-up duration**
- **Outcome definitions and measurement methods**
- **Effect sizes with confidence intervals** -- odds ratios, hazard ratios, relative risks, p-values where reported
- **Confounders assessed** -- which confounders the study adjusted for (and, implicitly, which it did not)
- **Limitations** -- as acknowledged by the study authors
- **Funding and conflict of interest** -- sources and declared conflicts where reported
- **Bias signals** -- absence of blinding, short follow-up, highly selected populations, discrepancies between abstract conclusions and reported data

This is the critical differentiator from general-purpose tools such as ChatGPT or Copilot. Those tools can summarise a paper's conclusions. This system extracts the methodological components that allow the assessor to determine whether those conclusions are trustworthy -- then presents them in a structured, cross-study-comparable format with paragraph-level source traceability.

---

## 7. Addressing the Key Objections from the Meeting

### 7.1 "Fill BR in seconds" scepticism: reframing and human-in-the-loop

**MHRA concern (Allison):** "My antibodies are going through the roof just because it says fill your benefit risk in seconds. Don't spend months looking at it."

**Response:** We acknowledge this messaging is inappropriate for the regulatory context and counterproductive with expert audiences. The "in seconds" claim conflates data consolidation with expert judgment and sounds irresponsible to professionals who invest months in careful assessment.

**Corrected framing:** The evidence consolidation phase -- gathering, structuring, and cross-referencing published literature and regulatory data -- is accelerated. This frees assessor time for the interpretive and judgment work that only qualified experts can perform. The assessment itself proceeds on the assessor's timeline and under the assessor's authority.

The system is designed to produce pre-filled templated documents that a human assessor reviews, filters, and uses to build the final benefit-risk assessment. The assessor retains full responsibility for: evaluating study quality and limitations, deciding which evidence to include or exclude, weighing the relative importance of benefits versus risks, and rendering the final regulatory judgment.

All speed claims and marketing language identified in the positioning audit (see Appendix B) are being removed from any materials MHRA may see. The claim "currently under review by the MHRA" in the sales deck must be deleted immediately -- it misrepresents the exploratory nature of the engagement and would destroy trust if seen by MHRA.

### 7.2 Validation of many models in series and audit trail

**MHRA concern (Allison):** "When you've got such complex models that they're happening in series, how do you validate them? How do you identify where that error might have happened?"

**Response:** Each of the 24 SLMs performs a single, well-defined task and produces an inspectable intermediate output at every step boundary.

**Per-model validation:** Four complementary methods are used:
1. Clinician-annotated test sets (dual-annotated independently) with measured precision, recall, and F1. Target: >= 85% F1.
2. Statistical comparison against data known to contain noise, establishing performance bounds in realistic conditions.
3. Blind comparison against client's existing assessment (the client's independently created work product serves as ground truth).
4. Client-specific sampling on the particular therapeutic area to validate general-model performance on specific use cases.

**Per-step auditability:** Every intermediate output is inspectable. If an adverse event extraction is incorrect, the reviewer can see the source sentence, what was extracted, and at which step the error occurred. Errors in Step 1 (classification) propagate differently from errors in Step 5 (normalisation), and the chain's modular design enables the reviewer to identify the origin.

**Open item (TBD / requires confirmation):** Formal error propagation modelling across the full chain (quantifying how upstream errors compound through downstream steps) is not yet documented. This is acknowledged transparently as an area for development.

### 7.3 Managing incomplete, inconsistent, and noisy data

**MHRA concern (Sharinto):** "What we wouldn't want is a skewed view because of perhaps incomplete or inconsistent data. Does it come up with levels of uncertainty, or does it flag where there are issues?"

**Response:**
- **Gap flagging:** The system explicitly reports what expected data fields are missing per source and what evidence types are absent from the corpus.
- **Conflicting evidence:** When sources disagree, both versions are preserved and flagged with full provenance. The system does not silently resolve conflicts.
- **Source stratification:** Every extracted element is tagged with its source type, enabling assessors to filter by evidence reliability.
- **Confidence scoring (in development):** Per-element confidence indicators based on extraction certainty, source reliability, and cross-source consistency are planned but not yet operational as a first-class feature. This is presented honestly as in-development.
- **Data completeness metrics:** Measured as percentage of expected data fields populated per source type, reported per analysis.

The system does not present incomplete data as complete. It surfaces what is found, flags what is missing, and leaves the judgment of clinical significance to the assessor.

### 7.4 Applicability beyond new/rare products (long-marketed drugs, rare events, causality challenges)

**MHRA concern (Allison):** "Those are much easier questions than for drugs that have been on the market for a long time. And safety events emerge." And: "You may have a rare event, and you're trying to understand causality of that event across a lot of different data sources."

**Response:** The extraction pipeline does not depend on clinical trial data structure. It handles observational studies, meta-analyses, case series, and regulatory documents -- the primary evidence types for long-marketed drugs. The extraction tasks (identify adverse events, extract temporal relationships, extract study design, normalise terminology) are generic across medicine and do not change with product maturity.

For causality specifically, the system extracts the elements that assessors use in causal reasoning: temporal relationships between exposure and event, dose-response data where reported, dechallenge/rechallenge information, biological plausibility data from mechanistic studies, and confounders assessed in observational analyses. It does not render a causality judgment -- but it ensures the assessor has the relevant data elements organised and sourced.

To demonstrate this directly, the proof of concept is designed around a long-marketed drug class with a mature post-marketing safety signal and genuine causality complexity.

**Honest limitation:** The system has been primarily validated with pharmaceutical clients working on product-development use cases. Performance on post-authorisation scenarios with lower-quality, more heterogeneous data has not been demonstrated at scale to a regulatory audience. This is precisely what the proof of concept is designed to test.

### 7.5 Generalised usage without "bespoke model per safety issue"

**MHRA concern (Allison):** "What I can't see working is for every specific use case, I have to build a bespoke model." And: "How could you give out something generic? It's beyond the literature search because I can get ChatGPT to do that."

**Response:** No new model is developed per safety question. The 24 task-specific models are reused across all use cases. What changes per question is pipeline configuration (which sources, which ontology subsets, which output templates) -- analogous to defining a search strategy, not building a new analytical tool.

**Differentiation from ChatGPT/Copilot:** General-purpose LLMs can summarise papers and answer questions. They cannot:
- Systematically extract structured critical appraisal elements across hundreds of sources in a consistent schema
- Normalise extracted terms to standardised regulatory ontologies (MedDRA, SNOMED CT)
- Provide paragraph-level traceability from every output element to its source document and sentence
- Produce gap analyses identifying what evidence is absent from the assembled corpus
- Cross-reference findings across sources by mechanism of action in a knowledge graph
- Present assessors with structured, auditable evidence packages rather than generated prose

These capabilities constitute the value above general-purpose tools.

### 7.6 UK context differences (utilisation patterns, line of therapy, effectiveness vs. efficacy)

**MHRA concern (Allison):** "Usage of drugs is very different across the world... safety events do not necessarily translate across the world." And: "We don't do efficacy, of course, we do effectiveness."

**Response:** The system acknowledges but does not resolve UK-specific contextualisation:

- **What it can do:** Extract and tag evidence by geographic origin. Extract line-of-therapy information where reported. Filter evidence by population characteristics relevant to UK prescribing. Distinguish efficacy data (labelled as such) from effectiveness data.
- **What it cannot do:** Determine whether a non-UK study applies to UK clinical practice. Assess how UK prescribing patterns affect the benefit-risk balance. Translate efficacy to effectiveness.
- **What could be explored in Phase 2+:** Integration of UK-specific sources (NICE guidelines, BNF, published CPRD analyses) alongside extracted evidence.

For the proof of concept, UK-specific evidence sources (MHRA Drug Safety Updates, UK-authored studies) will be specifically included, and evidence from non-UK populations will be flagged.

---

## 8. Proposed Collaboration: A No-Funding, Public-Domain Proof of Concept

### 8.1 Criteria for selecting a public-domain safety issue

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | **Closed or publicly reported** | MHRA cannot share confidential ongoing assessments |
| 2 | **Long-marketed drug class** | New/rare product cases are "much easier" and would not demonstrate relevant capability |
| 3 | **Substantial public-domain evidence base** | Enough literature, PARs, safety communications, and observational studies for meaningful testing without proprietary MHRA data |
| 4 | **Messy, heterogeneous evidence** | Must include the evidence types MHRA works with: observational studies, case reports, meta-analyses, mechanistic studies -- not just clean RCTs |
| 5 | **Multi-regulator action** | Ideally MHRA, EMA (PRAC), and FDA all published independent assessments, enabling cross-referencing |
| 6 | **UK-specific considerations** | Issues where MHRA took distinct UK-specific action are preferred |
| 7 | **Causality complexity** | Genuine causality challenges: confounding, atypical presentations, difficulty distinguishing drug effect from underlying disease |
| 8 | **Sufficient volume** | At minimum 100+ relevant publications across study types to stress-test the pipeline at scale |

MHRA will have final selection authority. ArcaScience will also accept an alternative proposed by MHRA that meets these criteria.

### 8.2 Candidate PoC options

#### Option A: SGLT2 Inhibitors and Diabetic Ketoacidosis (DKA) -- RECOMMENDED

**Drug class:** Canagliflozin, dapagliflozin, empagliflozin (oral antidiabetics, first authorised EU 2012-2014).

**Safety issue:** Post-marketing identification of rare diabetic ketoacidosis, often presenting atypically with near-normal blood glucose ("euglycaemic DKA"). Coordinated regulatory action across MHRA, EMA, and FDA between 2015-2016, with follow-up through 2022.

**Why it fits:**
- Causality complexity: euglycaemic DKA was mechanistically unexpected; confounders (infection, surgery, fasting, insulin reduction) complicated the signal; initially controversial
- Evidence heterogeneity: spontaneous reporting data, clinical trial re-analyses, observational cohort studies, mechanistic hypotheses, case series, systematic reviews
- Post-marketing, long-marketed class by the time of reviews (millions of patient-years of exposure)
- Low political sensitivity -- well-bounded evidence base with clear regulatory endpoints
- Generic applicability: "Does this drug class cause this rare serious adverse event, and in what context?" is the archetypal post-marketing pharmacovigilance question

**Key public sources:**
- MHRA Drug Safety Update: SGLT2 inhibitors and DKA risk (2016): https://www.gov.uk/drug-safety-update/sglt2-inhibitors-updated-advice-on-the-risk-of-diabetic-ketoacidosis
- EMA Article 20 referral (full PRAC assessment report): https://www.ema.europa.eu/en/medicines/human/referrals/sglt2-inhibitors
- FDA Drug Safety Communication (2015): https://www.fda.gov/Drugs/DrugSafety/ucm446852.htm
- Frontiers in Pharmacology systematic review (2023): https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2023.1145587/full
- NEJM correspondence (2017): https://www.nejm.org/doi/full/10.1056/NEJMc1701990

#### Option B: Fluoroquinolone Antibiotics and Disabling Side Effects -- BACKUP

**Drug class:** Ciprofloxacin, levofloxacin, moxifloxacin, ofloxacin (marketed since late 1980s).

**Safety issue:** Disabling and potentially permanent side effects: tendon rupture, peripheral neuropathy, psychiatric effects, aortic aneurysm. EMA Article 31 referral (2017-2019), MHRA risk minimisation review (2023) with additional UK-specific restrictions (January 2024).

**Why it fits:**
- 35+ years on market; evidence spanning decades
- MHRA conducted its own risk minimisation review and published a Public Assessment Report with UK-specific restrictions going beyond EU-harmonised measures
- Multi-system adverse events testing pipeline breadth
- Risk minimisation effectiveness dimension (MHRA found prescribing had not changed despite 2019 restrictions)
- Higher complexity and larger evidence base than Option A

**Key public sources:**
- MHRA Drug Safety Update (Jan 2024): https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-must-now-only-be-prescribed-when-other-commonly-recommended-antibiotics-are-inappropriate
- MHRA Public Assessment Report: https://www.gov.uk/government/publications/review-of-risk-minimisation-for-disabling-and-potentially-long-lastingirreversible-side-effects-associated-with-fluoroquinolone-antibiotics
- EMA Article 31 referral: https://www.ema.europa.eu/en/medicines/human/referrals/quinolone-fluoroquinolone-containing-medicinal-products

#### Option C: Sodium Valproate and Pregnancy Risks -- RESERVE (propose only if MHRA requests)

**Drug class:** Sodium valproate (marketed since 1972 for epilepsy, 1990s for bipolar/migraine).

**Safety issue:** Teratogenicity (approximately 10% malformation rate), neurodevelopmental harm (30-40% of exposed children), evolving male-mediated risk. Culminated in MHRA Pregnancy Prevention Programme, EMA Article 31 referral, and the Cumberlege Review ("First Do No Harm," 2020).

**Why it fits:**
- Landmark UK safety issue; 50+ years on market; massive evidence base
- Cross-regulatory divergence (EMA mandatory PPP vs. FDA black box warning)
- Non-traditional evidence types (Cumberlege Review, patient testimony)

**Political sensitivity:** High -- the Cumberlege Review criticised MHRA directly. Do not propose first. Present only as a third option if requested.

**Key public sources:**
- MHRA Valproate safety review (2023): https://www.gov.uk/government/publications/valproate-review-of-safety-data-and-expert-advice-on-management-of-risks
- EMA Article 31 referral: https://www.ema.europa.eu/en/medicines/human/referrals/valproate-related-substances-0
- IMMDS "First Do No Harm" report: https://www.immdsreview.org.uk/Report.html

**Recommendation:** Option A as primary. Best balance of complexity and manageability for a first proof of concept. The question it addresses -- "Does this drug class cause this rare SAE, and under what circumstances?" -- is the generic post-marketing pharmacovigilance question Allison asked ArcaScience to solve.

### 8.3 Success metrics

**Quantitative:**

| Metric | Target | How measured |
|--------|--------|-------------|
| Source completeness | >= 90% of sources cited in published regulatory assessment identified by pipeline | Compare pipeline output to PRAC/MHRA report citation list |
| Extraction accuracy | >= 95% factual accuracy on audited sample (minimum 50 extractions spot-checked) | Blinded audit by MHRA assessor or independent reviewer comparing extracted elements to source |
| Traceability completeness | 100% of extracted elements with verifiable source link | Systematic check of source links in output |
| Critical appraisal coverage | >= 80% of applicable quality indicators extracted per source | Structured review against pre-defined checklist |
| Error rate | < 2% factual errors, hallucinations, or misattributions | Independent audit of randomly sampled extractions |
| False negatives | < 10% of sources in reference assessment missed by pipeline | Gap analysis comparing pipeline output to reference |

**Qualitative:**

| Metric | How measured |
|--------|-------------|
| Assessor satisfaction | Semi-structured feedback; assessors rate utility, trust, and usability on 5-point scale |
| "Beyond literature search" test | Direct comparison: "Could you have gotten this from PubMed + ChatGPT?" -- Yes/No with explanation |
| Assessor trust | Feedback on which output elements assessors would use vs. which they would re-verify independently |
| Actionability | Assessor judgment: "If this were a live signal, would this output accelerate your assessment?" |

### 8.4 Deliverables MHRA would receive

All deliverables produced by ArcaScience at its own expense using only public-domain data.

1. **Evidence map.** Comprehensive structured inventory of all relevant public-domain sources: full citation, document type (regulatory assessment, clinical trial publication, observational study, case report, meta-analysis, safety communication, mechanistic study), classification by evidence type/design/population/geography/date, temporal mapping showing when evidence became available relative to regulatory actions.

2. **Structured extraction output.** For each source: study characteristics (design, population, sample size, duration, setting, inclusion/exclusion criteria), key findings (primary outcomes, effect sizes with CIs, statistical significance, secondary findings), critical appraisal elements (confounders assessed, biases identified, limitations, quality indicators), and identification of which elements were cited in regulatory assessments.

3. **Templated draft sections.** Structured output organised analogously to PSUR/DSUR safety evaluation sections: summary of safety concern, clinical trial evidence, published spontaneous reporting data (aggregate only), observational/epidemiological studies, mechanistic evidence, regulatory actions taken (cross-jurisdictional comparison). These are draft structures for assessor review -- not finished regulatory documents.

4. **Traceability report.** Complete audit trail: every extracted element linked to source document, section, page/paragraph, pipeline step that produced the extraction, and confidence score. Conflicts between sources flagged with both versions preserved.

5. **Gap analysis.** Identification of: evidence types present in the published assessment that the pipeline could not access (e.g., unpublished sponsor data, confidential ICSR line listings); evidence types that should exist but were not found; geographic gaps (e.g., UK-specific incidence data present or absent); temporal gaps (e.g., no studies after a certain year). This demonstrates the system knows what it does not know.

### 8.5 Timeline with phases

| Phase | Duration | Activities | MHRA commitment |
|-------|----------|------------|-----------------|
| **Phase 0: Joint scoping** | Week 0 (1 meeting + 1 week for written confirmation) | ArcaScience presents candidate issues; MHRA selects one; joint agreement on scope, data boundaries, success criteria, assessor availability. Lightweight collaboration letter (no contract, no funding, no data exchange, no IP implications). | 1-2 assessors, one 60-minute meeting + email confirmation |
| **Phase 1: Evidence assembly and extraction** | Weeks 1-2 | Week 1: Pipeline ingestion, evidence map construction, source classification, extraction with traceability. Week 2: Internal QC, deliverable preparation, comparison of ArcaScience outputs vs. published regulatory assessment. | None (ArcaScience works independently) |
| **Phase 2: Joint review and feedback** | Week 3 | Deliverables sent to MHRA 2-3 days before review. 90-minute review session: walkthrough (15 min), assessor review of evidence map and extractions (30 min), traceability deep dive (20 min), feedback (15 min), next steps (10 min). | 1-2 assessors, 90-minute session + optional written feedback |

**Total elapsed time:** 4 weeks from kickoff to completion.
**Total MHRA time commitment:** Approximately 3-4 hours of assessor time across the entire PoC.
**Total ArcaScience cost:** Absorbed internally as strategic investment.

---

## 9. Next Meeting Agenda (60 Minutes)

This agenda is for the follow-up meeting to propose and scope the proof of concept.

| Time | Item | Purpose |
|------|------|---------|
| 0:00 - 0:10 | **Confirm use case and data boundaries** | Present candidate safety issues with rationale. MHRA confirms or modifies selection. Agree exact scope, data boundaries, and success criteria. |
| 0:10 - 0:25 | **Under-the-hood walkthrough** | Pipeline architecture, task-specific model explanation, validation approach, traceability mechanism. No marketing slides. Technical depth. Directly addresses: "I'd like to see under the hood." |
| 0:25 - 0:45 | **Live demo on chosen public safety issue** | Pipeline running on 3-5 representative sources for the agreed issue. Show extraction from an observational study (not just case reports -- addressing Allison's concern directly). Show how document classification and section identification work. Show confidence scoring. Show source traceability at the sentence level. |
| 0:45 - 0:55 | **Review outputs and traceability** | Walk through sample evidence map, structured extraction, and gap analysis. MHRA assessors select specific extracted elements and trace them back to source. Demonstrate what the system flags as missing. |
| 0:55 - 1:00 | **Agree next steps** | Confirm whether MHRA is comfortable proceeding with the PoC. Agree timeline, assessor availability, and communication channel. Confirm collaboration letter scope. |

**Preparation required before this meeting:**
- Working demo ready on at least the primary candidate issue (Option A, SGLT2/DKA) using exclusively public-domain sources
- Technical architecture walkthrough refined for non-marketing presentation
- Data governance framework ready to reference if confidentiality questions arise
- All marketing materials and website claims updated per positioning audit -- no "in seconds," "18 months to seconds," or "100% regulatory acceptance rate" language in any material MHRA may see
- "Currently under review by the MHRA" claim deleted from the deck

---

## 10. Appendix

### Appendix A: Glossary

| Term | Definition |
|------|-----------|
| **Benefit-risk assessment (BRA)** | Systematic evaluation of the favourable and unfavourable effects of a medicine in relation to a specific indication and population. In the MHRA context, this is a human-led regulatory judgment, not a computational output. |
| **BNF (British National Formulary)** | UK reference for prescribing, dispensing, and administering medicines. |
| **BRAT (Benefit-Risk Action Team) framework** | Structured framework for organising and displaying the key benefits and risks of a medicine, developed by CIRS. |
| **CIOMS (Council for International Organizations of Medical Sciences)** | International organisation producing guidance on pharmacovigilance and benefit-risk assessment. CIOMS Working Group XII produced a framework for benefit-risk assessment. |
| **CPRD (Clinical Practice Research Datalink)** | UK real-world research service providing anonymised patient data from GP practices. Approximately 30 million patient records spanning 30 years. Operated by MHRA. |
| **DSUR (Development Safety Update Report)** | Annual safety report for investigational medicinal products required under ICH E2F. |
| **Effectiveness** | Performance of a drug under real-world clinical conditions. MHRA works with effectiveness. Distinct from efficacy. |
| **Efficacy** | Performance of a drug under controlled, ideal conditions (clinical trials). |
| **EudraVigilance** | EMA's system for managing and analysing reports of suspected adverse reactions to medicines authorised in the EEA. |
| **FAERS (FDA Adverse Event Reporting System)** | US FDA database of adverse event reports and medication error reports. |
| **ICH E2C(R2)** | International Council for Harmonisation guideline on Periodic Benefit-Risk Evaluation Reports. |
| **MAH (Marketing Authorisation Holder)** | Company or organisation holding the authorisation to market a medicine. |
| **MedDRA** | Medical Dictionary for Regulatory Activities -- international medical terminology for regulatory communication. |
| **NICE** | National Institute for Health and Care Excellence -- UK body providing guidance on use of health technologies. |
| **PBRER (Periodic Benefit-Risk Evaluation Report)** | The ICH E2C(R2) equivalent of PSUR. |
| **PRAC (Pharmacovigilance Risk Assessment Committee)** | EMA committee responsible for assessing and monitoring the safety of human medicines. |
| **PSUR (Periodic Safety Update Report)** | Periodic report providing comprehensive evaluation of the benefit-risk balance of a marketed medicine. |
| **RMP (Risk Management Plan)** | Document describing pharmacovigilance activities and interventions to identify, characterise, prevent, or minimise risks. |
| **Signal** | Information from one or multiple sources suggesting a new potentially causal association, or new aspect of a known association, between a medicine and an adverse event. A signal is a hypothesis requiring evaluation, not a confirmed risk. |
| **SLM (Small Language Model)** | In ArcaScience's context, a task-specific ML model trained for a discrete extraction or classification function, distinct from large general-purpose language models (LLMs). |
| **SmPC (Summary of Product Characteristics)** | Regulatory document describing properties and approved conditions of use of a medicine. |
| **Yellow Card scheme** | UK system for collecting and monitoring information on suspected adverse reactions to medicines, vaccines, herbal products, and medical devices. Patient-level data; confidential. |

### Appendix B: "Claims We Will NOT Make" List

The following statements must never appear in any communication with MHRA -- written, verbal, slide deck, email, or demo walkthrough. This list is binding on all ArcaScience personnel involved in the MHRA engagement.

1. We will NOT claim that ArcaScience "performs," "conducts," or "completes" benefit-risk assessment. The system supports and informs the assessment. The assessment is performed by qualified human experts.

2. We will NOT claim that the system produces results "in seconds." We will describe what is accelerated (data retrieval, cross-referencing, initial structuring) and what proceeds at the assessor's pace (expert review, contextual judgment, committee deliberation).

3. We will NOT claim "100% regulatory acceptance rate" or any formulation implying that regulatory agencies have endorsed, certified, or validated the ArcaScience platform. Regulatory acceptance of a submission reflects the totality of the sponsor's data and arguments, not the tool used to assemble them. We will say: "Our outputs have been incorporated into N regulatory submissions by our pharmaceutical clients."

4. We will NOT claim that the system "replaces," "substitutes for," or "automates" assessor judgment. We will always frame the system as augmenting, supporting, and informing human decision-makers.

5. We will NOT claim that ArcaScience is "under review by the MHRA" or that MHRA is evaluating ArcaScience for endorsement. This claim must be deleted from the sales deck immediately. The engagement is accurately described as: "exploratory discussions about potential utility of structured evidence tools in post-authorisation safety assessment."

6. We will NOT claim "100% accuracy," "100% completeness," or "zero hallucination." We will provide validated performance metrics with error rates and known limitations for each model.

7. We will NOT use "world's largest" or any unverifiable superlative about database size, model count, or capability scope.

8. We will NOT claim the system handles the "full drug lifecycle" without immediately specifying which phases are covered and which data types are excluded (imaging, omics, CPRD-scale databases).

9. We will NOT claim that the system "detects insights" or "finds signals" without specifying these are candidate patterns requiring expert validation. An AI-identified pattern is not a clinical finding.

10. We will NOT cite metrics (60% faster, 9x more insights, 3x DDI boost, 80% time reduction) without providing the baseline, methodology, sample size, and client context. Uncontextualised metrics will not appear in regulator-facing materials.

11. We will NOT describe outputs as "generated documents" (e.g., "generates PSURs"). We will say: "pre-populates structured templates for expert review and completion."

12. We will NOT reference competitive win rates or commercial performance in regulator-facing communications.

13. We will NOT claim the system works for "any therapeutic area" or "all data types" without specifying exactly which have been validated and which are excluded.

14. We will NOT trivialise the difficulty of regulatory work. Phrases such as "Don't spend months looking for it," "so easy," or "in mere seconds" are permanently excluded from regulator-facing vocabulary.

15. We will NOT use the phrase "AI-Driven Benefit-Risk Analysis." The accurate description is "AI-supported evidence structuring for benefit-risk assessment."

### Appendix C: References

**Regulatory public sources (candidate PoC):**

- MHRA Drug Safety Update: SGLT2 inhibitors and DKA risk (2016). https://www.gov.uk/drug-safety-update/sglt2-inhibitors-updated-advice-on-the-risk-of-diabetic-ketoacidosis
- MHRA Drug Safety Update: Fluoroquinolone antibiotics -- new restrictions (Jan 2024). https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-must-now-only-be-prescribed-when-other-commonly-recommended-antibiotics-are-inappropriate
- MHRA Drug Safety Update: Fluoroquinolone antibiotics -- reminder of disabling side effects (Aug 2023). https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-reminder-of-the-risk-of-disabling-and-potentially-long-lasting-or-irreversible-side-effects
- MHRA Drug Safety Update: Fluoroquinolone antibiotics -- 2019 restrictions. https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-new-restrictions-and-precautions-for-use-due-to-very-rare-reports-of-disabling-and-potentially-long-lasting-or-irreversible-side-effects
- MHRA Public Assessment Report: Fluoroquinolone risk minimisation review. https://www.gov.uk/government/publications/review-of-risk-minimisation-for-disabling-and-potentially-long-lastingirreversible-side-effects-associated-with-fluoroquinolone-antibiotics
- MHRA: Valproate review of safety data (2023). https://www.gov.uk/government/publications/valproate-review-of-safety-data-and-expert-advice-on-management-of-risks
- MHRA Drug Safety Update: Valproate PPP. https://www.gov.uk/drug-safety-update/valproate-epilim-depakote-pregnancy-prevention-programme-updated-educational-materials
- MHRA Drug Safety Update: Valproate use in men (2024). https://www.gov.uk/drug-safety-update/valproate-use-in-men-as-a-precaution-men-and-their-partners-should-use-effective-contraception
- MHRA press release: Fluoroquinolone new restrictions. https://www.gov.uk/government/news/mhra-introduces-new-restrictions-for-fluoroquinolone-antibiotics
- EMA: SGLT2 inhibitors Article 20 referral. https://www.ema.europa.eu/en/medicines/human/referrals/sglt2-inhibitors
- EMA: PRAC Assessment Report -- SGLT2 inhibitors. https://www.ema.europa.eu/en/documents/referral/sglt2-inhibitors-article-20-procedure-assessment-report_en.pdf
- EMA: PRAC press release -- SGLT2 DKA recommendations (Feb 2016). https://www.ema.europa.eu/en/news/sglt2-inhibitors-prac-makes-recommendations-minimise-risk-diabetic-ketoacidosis
- EMA: Quinolone/fluoroquinolone Article 31 referral. https://www.ema.europa.eu/en/medicines/human/referrals/quinolone-fluoroquinolone-containing-medicinal-products
- EMA: PRAC Assessment Report -- quinolone/fluoroquinolone. https://www.ema.europa.eu/en/documents/referral/quinolone-and-fluoroquinolone-article-31-referral-assessment-report_en.pdf
- EMA: PRAC press release -- fluoroquinolone restrictions (Oct 2018). https://www.ema.europa.eu/en/news/fluoroquinolone-quinolone-antibiotics-prac-recommends-new-restrictions-use-following-review-disabling-potentially-long-lasting-side-effects
- EMA: Fluoroquinolone reminder (2023). https://www.ema.europa.eu/en/news/fluoroquinolone-antibiotics-reminder-measures-reduce-risk-long-lasting-disabling-potentially-irreversible-side-effects
- EMA: Valproate Article 31 referral. https://www.ema.europa.eu/en/medicines/human/referrals/valproate-related-substances-0
- EMA: PRAC Assessment Report -- valproate. https://www.ema.europa.eu/en/documents/referral/valproate-article-31-referral-prac-assessment-report_en.pdf
- EMA: Valproate pregnancy measures (Feb 2018). https://www.ema.europa.eu/en/news/prac-recommends-new-measures-avoid-valproate-exposure-pregnancy
- FDA: SGLT2 Drug Safety Communications. https://www.fda.gov/Drugs/DrugSafety/ucm446852.htm
- FDA: SGLT2 label revision (Dec 2015). https://www.fda.gov/files/drugs/published/FDA-revises-labels-of-SGLT2-inhibitors-for-diabetes-to-include-warnings-about-too-much-acid-in-the-blood-and-serious-urinary-tract-infections.pdf
- FDA: Fluoroquinolone Drug Safety Communication (July 2016). https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-updates-warnings-oral-and-injectable-fluoroquinolone-antibiotics
- FDA: Fluoroquinolone safety labelling changes. https://www.fda.gov/drugs/information-drug-class/fda-approves-safety-labeling-changes-fluoroquinolones
- IMMDS Review: "First Do No Harm" (July 2020). https://www.immdsreview.org.uk/Report.html

**Published literature:**

- Frontiers in Pharmacology: SGLT2 inhibitors and DKA systematic review and network meta-analysis (2023). https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2023.1145587/full
- NEJM: Risk of DKA after initiation of SGLT2 inhibitor (2017). https://www.nejm.org/doi/full/10.1056/NEJMc1701990
- PMC: FAERS data analysis -- SGLT2 and DKA (2017). https://pubmed.ncbi.nlm.nih.gov/28500396/
- PMC: "First do no harm: valproate and medicines safety in pregnancy" (2020). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7518898/

**ArcaScience internal documents used in preparation (not for external distribution):**

- MHRA Meeting transcript (January 2026)
- ArcaScience Deck 2026
- ArcaScience 2026 IT Roadmap
- ArcaScience i-Demo / BR-PREDICT project documentation
- ArcaScience OKR Execution Blueprint and Next-Quarter OKRs
- arcascience.ai (public website, reviewed February 2026)
- arcascienceval.live (public website, reviewed February 2026)

**Regulatory framework references:**

- ICH E2C(R2): Periodic Benefit-Risk Evaluation Reports
- CIOMS Working Group XII: Benefit-Risk Balance for Marketed Drugs
