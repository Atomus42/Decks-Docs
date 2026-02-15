# Under the Hood: ArcaScience Technical Architecture, Validation, and Auditability

**Prepared for MHRA follow-up -- Agent 3 (Technical Explainer)**
**Date: 2026-02-15**
**Classification: For internal preparation only**

---

## 1. High-Level Pipeline

The ArcaScience system processes documents through a sequential, chained pipeline. Each step produces auditable intermediate output before feeding the next step. The pipeline operates on 24 task-specific small language models (SLMs), not a single monolithic large language model.

```
 INGEST             CLASSIFY           SECTION ID          EXTRACT
+----------------+ +----------------+ +----------------+ +-------------------+
| Document       | | Document Type  | | Section        | | Entity Extraction |
| Ingestion      |-->  Classification |-->  Identification |-->                   |
| (PDF, XML,     | | (case report,  | | (methodology,  | | - Safety events   |
|  DOC, any       | |  clinical trial,|  |  abstract,      | | - Temporal status  |
|  semantic src)  | |  observational  | |  results, etc.) | | - Drug names      |
+----------------+ |  study, etc.)  | +----------------+ | - Severity        |
                   +----------------+                    | - Outcomes        |
                                                         | - Patient info    |
                                                         |   (gender, age,   |
                                                         |    population)    |
                                                         | - Study design    |
                                                         |   (sample size,   |
                                                         |    duration,      |
                                                         |    arms, blinding)|
                                                         | - Drug/dosage     |
                                                         |   (dose, freq,    |
                                                         |    admin route)   |
                                                         +-------------------+
                                                                  |
                                                                  v
 TEMPLATE           LINK              NORMALIZE            RELATE
+----------------+ +----------------+ +----------------+ +-------------------+
| Templated      | | Knowledge      | | Normalization  | | Relation          |
| Output         |<--  Graph /       |<--  Against        |<--  Extraction       |
| Generation     | | Linking        | | Ontologies     | |                   |
|                | |                | |                | | E.g. "myocardial  |
| 6 output types:| | Entities       | | - MedDRA       | |  infarction" is   |
| - Disease      | |   connected    | |   (restructured| |  related to       |
|   Analysis     | |   across       | |    by AS)      | |  "adalimumab"     |
| - Clinical     | |   sources,     | | - SNOMED CT    | |  in this sentence |
|   Landscape +  | |   drugs,       | | - ChEBI        | |                   |
|   Efficacy Rpt | |   events,      | | - Disease      | | Identifies which  |
| - Clinical     | |   patients     | |   Ontology     | |  drug causes      |
|   Endpoint     | |                | |                | |  which event in   |
|   Study        | | Profiling Base | +----------------+ |  which context    |
| - Adverse      | | (100B+ data   |                    +-------------------+
|   Events Rpts  | |  points)       |
| - Benefit Risk | +----------------+
|   Assessment   |
| - Benefit Risk |
|   Summary      |
+----------------+

Legend:
  --> = auditable handoff; intermediate output inspectable at each boundary
  SLM = Small Language Model (task-specific, clinician-trained)
```

**Data sources ingested** (as documented):
- Public: PubMed, MEDLINE, ClinicalTrials.gov, FAERS/VAERS, institutional databases
- Private/client: preclinical data systems, proprietary databases (e.g., Pharmapendium, FX), internal study data
- Client data remains on the client's infrastructure when confidentiality requires it

**Infrastructure executing this pipeline** (from IT Roadmap):
- "Data Forge" pipelines orchestrated by Apache Airflow DAGs
- Storage: S3 (raw and enriched), ElasticSearch (full-content indexing and analysis outputs), DocumentDB, QDrant vector database (ontologies)
- Analysis DAGs: SShield, KOL, COA, DDI, PICOS, BRA -- each as separate Airflow DAGs
- API layer: FastAPI (Python) for data pipeline services; Node.js/NestJS for BRA platform backend

---

## 2. Task-Specific Models vs. Therapeutic-Area Models

This distinction is critical for the MHRA's concern about scalability across hundreds of drugs and diverse safety questions.

### What ArcaScience does

The 24 SLMs are trained for **specific tasks**, not for specific therapeutic areas. Each model performs one well-defined extraction or classification function regardless of the disease or drug under review.

| Model task category | Example models (documented) | What the model does |
|---|---|---|
| Document classification | Document type classifier | Determines whether input is a case report, clinical trial, observational study, etc. Stratifies study design (randomized, blinded, arms, etc.) |
| Section identification | Section layering model | Identifies structural sections of a document (abstract, methodology, results, discussion) to route downstream extraction |
| Safety entity extraction | Safety event extractor | Extracts adverse event terms, temporal status ("two weeks after"), severity, outcomes ("hospitalized"), drug names from sentences |
| Relation extraction | Relation extraction model | Links extracted entities within context (e.g., "myocardial infarction is related to adalimumab in this sentence") |
| Efficacy endpoint extraction | 4-model chain: extract, structure, cluster, normalize | Identifies and standardizes efficacy endpoints across all therapeutic areas and all clinical phases |
| Patient information extraction | Patient information models | Extracts demographics: gender ratios, age ranges, population characteristics |
| Study design extraction | Study design extractor | Extracts sample size, duration, placebo presence, arm structure, blinding status |
| Drug/dosage extraction | Drug and dosage models | Extracts dose, frequency, administration route (e.g., "40 mg subcutaneous, once every two weeks") |
| Normalization | Ontology normalization models | Maps extracted terms to standardized ontologies (restructured MedDRA, SNOMED CT, ChEBI, Disease Ontology) |

### What this means in practice

- **No new model is trained** when a new therapeutic area is addressed. The same 24 models operate across all therapeutic areas.
- **Adaptation to a specific disease** happens through pipeline configuration, not model retraining: selecting which database subsets to query, enabling/disabling specific model outputs (e.g., deactivating efficacy models when only safety is relevant), and defining which classes of information to surface.
- The models were trained on **10,000+ documents spanning all therapeutic areas and all clinical phases (1-4)**, making the training data deliberately cross-therapeutic.
- The Ensemble Model architecture described in ArcaScience's materials states: **"No retraining needed"** for adaptation to new therapeutic areas or use cases.

### What the MHRA should understand

The system does not require building a "bespoke model" for each safety question or each drug. The extraction tasks (identify adverse events, extract temporal relationships, extract study design, etc.) are generic across medicine. The specificity to a therapeutic area comes from:

1. The **statement of work / pipeline configuration** (which sources, which ontology subsets, which models enabled)
2. The **database subset** screened (reducing noise from irrelevant pathologies)
3. The **template and output format** selected

This is architecturally distinct from an approach that trains a separate model per disease, which would not scale to the MHRA's 600+ drugs and hundreds of thousands of devices.

---

## 3. Traceability and Audit Trail

### Documented traceability mechanisms

**Per-step auditability (from meeting transcript):**
> "The information that comes in and comes out is auditable at both ends, and then is used on the next step auditable at both ends. So there is no black box in between."
> -- Romain Clement, CEO, MHRA meeting

This means each of the chained SLM steps produces an intermediate output that can be inspected before it feeds the next step.

**Evidence Provenance Layer (from OKR documents):**
The OKR materials describe a planned first-class feature called the "Evidence Provenance Layer," defined as:
> "Audit trail linking every statement to source, extraction, confidence, and timestamp."

This layer is designed to allow an auditor to trace any claim in the output back to:

| Provenance element | Description | Status |
|---|---|---|
| Source document | The original document from which data was extracted | Documented as operational |
| Extraction step | Which model performed the extraction | Documented as architectural principle |
| Confidence score | Per-insight confidence level | Described in OKRs as planned (Initiative 3 under O1) |
| Timestamp | When the extraction occurred | Described in OKRs as planned (Initiative 2 under O1) |
| Disagreement flags | Where models or sources disagree | Described in OKRs as planned (Initiative 3 under O1) |
| Missing evidence indicators | Where expected evidence is absent | Described in OKRs as planned (Initiative 3 under O1) |

**Definition of Done (from OKR Execution Blueprint):**
All platform deliverables must satisfy six criteria, including:
- **Data Traceability:** "Each intermediate stage of the BRA pipeline generates fully auditable output"
- **Data Quality Validation:** "Each data output is validated by the medical team with a representative panel of tests"

**BRAT/CIOMS-ready exports (from OKR documents):**
The platform is designed to produce regulator-ready exports aligned to the BRAT (Benefit-Risk Action Team) framework and CIOMS (Council for International Organizations of Medical Sciences) standards, requiring no additional formatting. The system is explicitly inspired by ICH Working Group XII and Guideline E2C(R2).

### What is operational vs. planned

| Capability | Status |
|---|---|
| Per-step auditable intermediate outputs | Operational (described as current architecture) |
| Source-to-statement linkage | Operational (described in meeting as current capability) |
| Confidence scoring per insight | Planned (OKR Initiative 3) |
| Disagreement flags | Planned (OKR Initiative 3) |
| Missing evidence indicators | Planned (OKR Initiative 3) |
| Evidence Provenance Layer as a first-class UI feature | Planned (OKR Initiative 2) |
| BRAT/CIOMS-ready exports | In development (KR target for flagship runs) |

---

## 4. Error Localization Across Chained Steps

The MHRA raised this concern directly in the meeting:
> "When you've got such complex models that they're happening in series, how do you validate them? ... How do you identify where that error might have happened?"
> -- Allison (Interlocuteur 7), MHRA

### How the chained architecture enables error localization

Because each of the 24 SLMs performs a single, well-defined task and produces inspectable output at each step boundary, errors can be localized to the specific step where they occurred:

```
Step 1: Document Classification
  Output: "This is a randomized clinical trial, Phase 3, double-blind"
  --> If wrong here, all downstream extraction operates on wrong assumptions
  --> Auditable: reviewer can verify document type assignment

Step 2: Section Identification
  Output: "Lines 1-45 = Abstract, Lines 46-120 = Methodology, ..."
  --> If wrong here, extraction models look in wrong sections
  --> Auditable: reviewer can verify section boundaries

Step 3: Entity Extraction (safety, efficacy, patient, drug)
  Output: Extracted entities with source sentence references
  --> If wrong here, specific entities are missed or miscategorized
  --> Auditable: reviewer can compare extracted entities against source text

Step 4: Relation Extraction
  Output: "Entity A is related to Entity B in sentence X"
  --> If wrong here, associations between drugs and events are incorrect
  --> Auditable: reviewer can verify the relation against the sentence

Step 5: Normalization
  Output: "Extracted term X maps to MedDRA PT Y"
  --> If wrong here, terms are mapped to wrong ontology codes
  --> Auditable: reviewer can verify ontology mapping

Step 6: Linking / Knowledge Graph Population
  Output: Connected entities across documents
  --> If wrong here, cross-source associations may be spurious
  --> Auditable: reviewer can inspect link rationale
```

### Quantified error categories (from meeting transcript)

ArcaScience reports errors in discrete, measurable categories:
- **Missed data:** percentage of relevant data points not extracted (reported as approximately 10% in example metrics shared)
- **Miscategorized data:** percentage of data points assigned to wrong category (reported as approximately 5% in example metrics shared)
- **Clustering errors:** percentage of data points grouped incorrectly

These metrics are generated per model, per task, enabling identification of which step in the chain contributes which type and magnitude of error.

### What is NOT documented

- **TBD:** Formal error propagation analysis across the full chain (i.e., how a 5% error in Step 3 compounds through Steps 4-6)
- **TBD:** Whether the system automatically flags cases where upstream errors may have affected downstream outputs
- **TBD:** Formal methodology for measuring inter-step error correlation

---

## 5. Model Validation Approach

Four distinct validation methods are documented, each addressing a different concern:

### Validation Method 1: Clinician-Annotated Test Sets

| Aspect | Detail |
|---|---|
| What | Test sets annotated independently by two clinicians with complete annotation guidelines |
| How | Model outputs are compared against the dual-clinician gold standard |
| Metrics reported | Percentage of missed data, percentage of miscategorized data, percentage of clustering errors |
| Documented example | "We skipped 10% of the data, we have 10% of miscategorized data, we have 5% of data that has been clustered in a different place" |
| Metric framework | F1 score (harmonic mean of precision and recall) targeted at >= 85% for both Risk/Safety endpoint extraction and Efficacy endpoint extraction |

### Validation Method 2: Statistical Comparison Against Noisy Data

| Aspect | Detail |
|---|---|
| What | The system's extraction is compared statistically against data known to contain noise |
| How | Known expected outputs are compared to model outputs on real-world, imperfect data |
| Purpose | Establishes performance bounds in realistic conditions, not just on clean test data |

### Validation Method 3: Market Validation (Blind Comparison)

| Aspect | Detail |
|---|---|
| What | Client provides their existing benefit-risk assessment (created independently). ArcaScience generates its own output from public data only. The two are compared blind |
| How | Client evaluates whether ArcaScience's output covers everything their manual assessment found |
| Results claimed | "100% of the time ... we were able to highlight everything that the clients have had highlighted on his end. ... And we brought between 9 times and 100 times more relevant insight" |
| Purpose | Validates comprehensiveness against real-world regulatory work product |

### Validation Method 4: Client-Specific Sampling

| Aspect | Detail |
|---|---|
| What | After the statement of work is defined and the pipeline is configured for a specific client's disease/drug, targeted sampling is performed |
| How | Samples drawn from the client's specific disease context are evaluated for the same error metrics (missed, miscategorized, etc.) |
| Purpose | Validates that the general model performs adequately on the client's specific therapeutic area and use case |

### Validation governance (from OKR documents)

The OKR Execution Blueprint specifies additional validation layers:
- **Internal validation:** Generation of test datasets, creation of test requirements, annotation of test data, analysis of results as percentage of data validated
- **External validation:** Identification and contact of 5 relevant KOLs per therapeutic area, questionnaire/interview guides developed, results analyzed as percentage of data validated
- **LLM validation:** Test prompts created, validated, executed, and results analyzed as percentage of data validated
- **Weekly "Fixing" sessions:** 60-minute weekly sessions focused on credibility, noise, and calibration

### Metrics targets (from OKR documents)

| Metric | Target |
|---|---|
| F1 on Risk/Safety endpoints pipeline | >= 85% |
| F1 on Efficacy endpoints data extraction | >= 85% |
| "Context" completeness on 10 known studies | >= 90% |
| Code test coverage (Webapp + API) | >= 80% |
| Platform availability | >= 99% |

---

## 6. What the System Extracts vs. What It Does NOT Judge

This distinction was explicitly clarified in the MHRA meeting and is fundamental to understanding the system's role.

### What the system DOES (extraction and structuring)

| Extraction category | Specific outputs |
|---|---|
| Study design elements | Study type (RCT, observational, case report), randomization status, blinding, number of arms, sample size, duration, presence of placebo |
| Safety information | Adverse event terms, temporal relationship to drug administration, severity classification, outcomes (e.g., hospitalization), incidence data where reported |
| Efficacy information | Efficacy endpoints, endpoint measurements, response rates where reported |
| Drug information | Drug name, dosage, frequency, administration route |
| Patient information | Gender distribution, age ranges, population characteristics |
| Relation mapping | Which adverse event is linked to which drug in which sentence/context |
| Cross-source linking | Connecting the same entities across multiple documents and data sources |
| Normalization | Mapping all extracted terms to standardized ontologies (MedDRA, SNOMED CT, ChEBI) |

### What the system does NOT do

| Excluded function | Explanation from meeting |
|---|---|
| **Judge study quality** | "We don't assume ... if the study has quality or not. We tell you the sample size was 100. It was for 6 months." The system extracts the elements that allow the human assessor to judge quality, but does not itself render a quality judgment |
| **Render benefit-risk verdicts** | The system does not produce a definitive statement such as "the risk of X is 20%." It surfaces and structures the evidence for human assessment |
| **Replace clinical judgment** | "It's the ultimate solution for providing you the comprehensive source of information properly stratified, properly annotated, connected and sourced, and after that, then you're absolutely sure that you haven't missed anything" |
| **Generate free-text conclusions** | "The solution will not provide you a generated answer. It's not going to be like ChatGPT stuff, it's going to be a set of templated documents" |
| **Process imaging or omics data** | Explicitly excluded from current capabilities. Omics data planned for future development (i-Demo / BR-PREDICT project) |

### The human-in-the-loop requirement

The system is designed to produce pre-filled templated documents (aligned to BRAT framework) that a human assessor then reviews, filters, and uses to build the final benefit-risk assessment. The assessor retains responsibility for:
- Evaluating study quality and limitations
- Deciding which evidence to include or exclude
- Weighing the relative importance of benefits vs. risks
- Rendering the final regulatory judgment

---

## 7. Infrastructure and Deployment Options

### Current production infrastructure (from IT Roadmap)

| Component | Technology | Notes |
|---|---|---|
| Cloud provider | AWS | Migrated from Azure in 2025 |
| Container orchestration | Kubernetes (100%) | Scalable, microservices architecture |
| Pipeline orchestration | Apache Airflow | Python-based DAGs for each analysis type |
| Data pipeline framework | "Data Forge" (proprietary) | Rewritten in 2025 for high-performance daily processing |
| Primary data storage | S3 | Raw data (XML), enriched data (JSON), output data |
| Search and indexing | ElasticSearch | Full-content indexing, analysis outputs |
| Document database | DocumentDB | Structured document storage |
| Vector database | QDrant | Ontology storage and semantic search |
| BRA platform frontend | ReactJS + Tailwind CSS | Web-based user interface |
| BRA platform backend | Node.js + Express / NestJS | RESTful API with GraphQL support |
| BRA platform database | PostgreSQL | Primary relational database (projects, users, outcomes, configuration) |
| Authentication | Keycloak | OAuth 2.0, OpenID Connect |
| Authorization | RBAC | JWT-based, role-based access control |
| Real-time updates | WebSockets | Project update notifications |
| Background processing | Redis Queue | Document generation jobs |
| Caching | Redis | Session management, query cache, rate limiting |
| ML/AI services | FastAPI (Python) | Model serving and data pipeline API |
| GPU compute | Model GPU (dedicated) | For SLM inference |
| Report generation | Puppeteer/wkhtmltopdf (PDF), python-pptx (PPTX) | Regulatory report and presentation generation |
| Code quality | SonarQube | Quality gate enforced on all production deployments |
| API architecture | RESTful with versioning + MCP Layer | Rate limiting, request throttling, comprehensive logging |

### On-premises feasibility

| Consideration | Assessment |
|---|---|
| Documented mention | The OKR Execution Blueprint includes "on-prem readiness assessment" as a deliverable for Weeks 5-6, and "non-negotiable on-premises readiness for enterprise" under Initiative 4 (Performance & MLOps Hardening). Enterprise tier (Tier 3) pricing explicitly includes "on-prem" as a feature |
| Architecture compatibility | The 100% Kubernetes infrastructure is, in principle, portable to on-premises Kubernetes clusters |
| Client data isolation | Documented: "The data never leaves the client side." The architecture supports client-side data processing, with structuring engines running on client infrastructure |
| Current status | On-prem readiness is explicitly planned but not yet confirmed as delivered. The OKR lists it as a target, not a completed capability |
| **TBD** | Specific hardware requirements for on-prem deployment (GPU specifications, storage requirements, network bandwidth) |
| **TBD** | Whether all 24 SLMs can run on-premises or whether some processing requires cloud-based GPU infrastructure |
| **TBD** | Latency and performance benchmarks for on-prem vs. cloud deployment |
| **TBD** | Whether Keycloak authentication can integrate with MHRA's existing identity infrastructure |

### Data confidentiality architecture

- Client private data runs alongside public data but within the client's own environment
- The system supports a configuration where ArcaScience does not access client data directly -- the client's own data team operates the data branching
- Public data (PubMed, ClinicalTrials.gov, etc.) is indexed in ArcaScience's Profiling Base

---

## 8. Open Items (TBD) -- Questions MHRA Would Likely Ask That Are Not Documented

### Model architecture and training

| # | Question | Why MHRA would ask | Current documentation status |
|---|---|---|---|
| 1 | What is the specific architecture of each SLM? (Transformer variant? Parameter count? Training methodology?) | Regulators need to understand model complexity to assess reliability claims | **TBD.** Materials state "small language models" and "24" but do not specify architectures or parameter counts |
| 2 | What are the exact training datasets for each model? How were they curated? | Data provenance for training is a regulatory concern | **TBD.** Known: 10,000+ documents, all therapeutic areas, all phases. Unknown: exact dataset composition, selection criteria, potential biases |
| 3 | How is model versioning managed? What happens when a model is updated? | Regulatory submissions need reproducibility | **TBD.** No documented model versioning or change control process found |
| 4 | What is the formal change control process when a model is retrained or updated? | GxP compliance requirement | **TBD** |

### Validation and performance

| # | Question | Why MHRA would ask | Current documentation status |
|---|---|---|---|
| 5 | What are the current, measured F1 scores for each of the 24 models? | Claimed metrics exist but specific per-model performance data not provided in reviewed materials | **TBD.** Targets (>= 85% F1) are documented. Actual current performance values are not published in reviewed materials |
| 6 | How does error propagate across chained steps? If Step 3 has 5% error, what is the cumulative error at Step 6? | Chained model validation is a known challenge in ML systems | **TBD.** No formal error propagation analysis documented |
| 7 | How were the two annotating clinicians selected? What is the inter-annotator agreement rate? | Annotation quality directly affects validation credibility | **TBD.** The process mentions two clinicians but does not specify selection criteria or inter-annotator agreement metrics |
| 8 | Are there therapeutic areas or document types where model performance is significantly lower? | Regulators need to know failure modes, not just averages | **TBD** |
| 9 | What is the false positive rate vs. false negative rate for safety signal extraction specifically? | In pharmacovigilance, false negatives (missed safety signals) are more dangerous than false positives | **TBD.** F1 is documented as the target metric, but the precision/recall breakdown (which reveals the false negative rate) is not published |

### Regulatory and compliance

| # | Question | Why MHRA would ask | Current documentation status |
|---|---|---|---|
| 10 | Is the system developed under any quality management system (e.g., ISO 13485, IEC 62304, GAMP 5)? | Software used in regulatory decision-making may need formal quality system compliance | **TBD** |
| 11 | Has the system undergone any independent third-party audit or validation? | Regulators distinguish self-validation from independent verification | **TBD.** All documented validation is internal or client-performed |
| 12 | How does the system handle conflicting evidence across sources? | A drug may show different safety profiles in different studies | **TBD.** The system normalizes and links, but the handling of contradictions is not documented |
| 13 | Is there a formal Software Development Life Cycle (SDLC) document? | Standard regulatory expectation for software used in assessment | **TBD.** SonarQube quality gates and 80% code coverage are documented, but no formal SDLC document is referenced |

### Uncertainty and confidence

| # | Question | Why MHRA would ask | Current documentation status |
|---|---|---|---|
| 14 | How is uncertainty quantified at the output level? | MHRA asked about "levels of uncertainty" and "flags where there are issues" during the meeting | **Planned.** The i-Demo project describes "Quantification de l'Incertitude" (uncertainty quantification) via Bayesian/ensemble approaches. The OKR documents describe "confidence scores, disagreement flags, and missing evidence indicators" as a planned initiative. Neither is documented as currently operational |
| 15 | How does the system handle missing data or incomplete documents? | Common in post-marketing surveillance data | **TBD.** The meeting discussed data quality management conceptually, but no formal methodology for handling missing data is documented |

### Post-marketing specific

| # | Question | Why MHRA would ask | Current documentation status |
|---|---|---|---|
| 16 | Can the system process spontaneous adverse event reports (e.g., Yellow Card equivalents)? | Core to MHRA's post-authorization work | **TBD.** FAERS is mentioned as a data source. Yellow Card data was discussed in the meeting as too confidential to share. The system's ability to process individual case safety reports (ICSRs) at scale is not explicitly documented |
| 17 | How does the system handle causality assessment? | MHRA specifically asked about understanding "causality of that event across a lot of different data sources" | **TBD.** The system extracts associations (drug X linked to event Y) but causality assessment methodology is not documented |
| 18 | Can the system handle real-world databases with billions of records (e.g., CPRD)? | MHRA mentioned "30 million patient records over 30 years" | **TBD.** The system is documented to handle semantic/textual data. Its capacity for structured epidemiological databases at that scale is not documented |

### Knowledge graph and future capabilities

| # | Question | Why MHRA would ask | Current documentation status |
|---|---|---|---|
| 19 | What is the current status of the knowledge graph (>100K entities, >1M relations target)? | Distinguishes current capability from roadmap | **TBD.** The target is documented in the i-Demo materials. Current state of population is not specified |
| 20 | What is the timeline and validation plan for the "World Model" (WP6) that integrates all prediction modules? | Understanding what is current vs. aspirational | **In development.** WP6 is a multi-year R&D program (2026-2029) under the i-Demo/BR-PREDICT project. Not part of the current operational platform |

---

## Summary: What to Tell the MHRA

When presenting the "under the hood" view to the MHRA, the following points should be made with precision:

1. **The system is an extraction and structuring engine, not a decision-making system.** It extracts, normalizes, links, and templates. It does not judge study quality or render benefit-risk verdicts. The human assessor retains full authority.

2. **The 24 models are task-specific, not therapeutic-area-specific.** This is the key to scalability. No new model is needed for each drug or disease. Adaptation happens through pipeline configuration.

3. **Each step produces auditable output.** There is no single black box. Each SLM's input and output can be inspected, and errors can be localized to specific steps.

4. **Validation uses four complementary methods:** clinician-annotated test sets, statistical comparison against noisy data, blind comparison against client's existing work, and client-specific sampling.

5. **Confidence scoring, disagreement flags, and missing evidence indicators are planned but not yet operational.** These are critical features for regulatory trust and should be presented honestly as in-development, not as current capabilities.

6. **On-premises deployment is architecturally feasible and planned** but not yet confirmed as delivered.

7. **Several questions MHRA is likely to ask (see Section 8) cannot yet be answered from documented materials** and will need to be addressed before or during the next meeting.

---

*This document uses only information from: MHRA Meeting minutes.txt, 2026 IT Roadmap PDF, ARCASCIENCE i-Demo PDF, ArcaScience Deck 2026 PDF, ArcaScience OKR Execution Blueprint, and Next-Quarter OKRs PDF. All items marked TBD reflect gaps in the reviewed documentation, not necessarily gaps in ArcaScience's capabilities.*
