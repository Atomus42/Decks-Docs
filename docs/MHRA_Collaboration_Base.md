# ArcaScience x MHRA: Collaboration Base Document

**Classification:** Source of truth for deck preparation and follow-up meeting
**Prepared:** 2026-02-15
**Status:** Internal -- not for external distribution without review

---

## 1. Executive Summary

### The operational reality

The MHRA's post-authorisation safety function operates under conditions that no technology vendor should be permitted to gloss over. Approximately 100 benefit-risk assessors manage 80 concurrent safety investigations across a portfolio of 600+ medicines and hundreds of thousands of medical devices. They do this with a 19.7% vacancy rate, 16.5% annual voluntary turnover, and institutional memory diminished by a 40% personnel loss during the 2020 reorganisation (MHRA People Strategy 2023-2026; Pharmaphorum 2023). The evidence they must assemble is messy, observational, heterogeneous, and drawn from sources that range from published case reports to CPRD queries covering 65 million patients. There is no clean dataset. There is no controlled environment.

When MHRA CEO Lawrence Tallon states that "our ability to meet that demand with humans is finite," he is describing a structural constraint, not a temporary staffing shortfall. The post-authorisation safety function needs tools that reduce the manual burden of evidence assembly -- not tools that promise to replace expert judgment, and not tools that require bespoke model-building for each of 80 concurrent safety questions.

### What MHRA asked

During an introductory meeting, three senior MHRA post-authorisation safety staff -- Deputy Director Allison, assessment lead Steph, and governance lead Sharinto -- evaluated whether ArcaScience's evidence-structuring platform could support their benefit-risk assessment work. The requirements they articulated, in order of emphasis, define the engagement:

1. **Post-authorisation focus.** MHRA works exclusively in the post-authorisation space. Their evidence base is messy, unstructured, observational, and heterogeneous. The platform must demonstrate utility against this reality, not against clean clinical trial datasets. ("How do you solve MY problem rather than THIS problem?" -- Allison)

2. **Transparency and auditability.** The platform cannot function as a "black box." Every output must be traceable to its source document and extraction step. This is non-negotiable in a regulatory environment where assessments carry legal force and Parliamentary scrutiny. ("That's fundamental for us to understand." -- Steph)

3. **Scalability without bespoke models.** MHRA cannot build a custom model for each of 80+ concurrent safety issues across 600+ drugs. The system must operate generically across all therapeutic areas. ("We can't develop an AI model for every use case. That's clearly not possible." -- Allison)

4. **Confidentiality.** Yellow Card patient-level data, CPRD records, and ongoing safety investigations cannot be shared externally. This is a statutory obligation, not a preference. ("We can't give you our yellow card data because that's far too confidential." -- Allison)

5. **Value beyond general-purpose AI.** The platform must deliver structured extraction, provenance, and synthesis that general-purpose large language models cannot replicate. ("It's beyond the literature search because I can get ChatGPT to do that." -- Allison)

6. **No funding available.** MHRA has no budget for a proof-of-concept engagement. ("It's not something that we could offer funding for at the moment." -- Allison)

7. **Messaging credibility.** Claims such as "benefit-risk in seconds" and "100% regulatory acceptance" triggered strong scepticism from professionals who invest months in careful, consequential assessment. ("My antibodies are going through the roof." -- Allison)

The senior decision-maker stated she is "not convinced yet" but is "really keen to look for ways to create efficiency" and needs to "see under the hood." Steph found the platform "interesting" and identified potential "utility" -- the most receptive signal in the meeting. Critically, MHRA proposed the proof-of-concept format themselves: they want a challenge test, not a demonstration.

### What we propose

A self-funded, public-domain proof of concept on a completed, publicly reported safety issue (recommended: SGLT2 inhibitors and diabetic ketoacidosis). ArcaScience runs its existing generic pipeline against publicly available evidence only, produces a structured evidence package with full traceability, and MHRA assessors compare the output against their own historical assessment of the same issue.

This approach directly addresses the core constraint: MHRA can evaluate the platform's utility without expending budget, sharing confidential data, or committing institutional resources. If the platform adds value on a historical, public-domain safety question using exclusively published evidence, it will add substantially more value when applied to the full evidence base -- including the spontaneous reporting data that, with a 94% median under-reporting rate (Hazell & Shakir 2006; PLOS Medicine 2025), structurally underrepresents the true burden of adverse drug reactions.

**MHRA investment:** Approximately 3-4 hours of assessor time over 4 weeks. **Confidentiality risk:** Zero -- no MHRA data is involved at any stage.

---

## 2. Why Now: The Strategic Imperative

This engagement is not opportunistic. It arrives at a specific inflection point in MHRA's institutional trajectory where the convergence of five factors creates a window for partnership that will not remain open indefinitely.

### 2.1 The capacity crisis is structural, not cyclical

The numbers are unambiguous. Approximately 100 post-authorisation assessors manage 80 concurrent safety investigations across 600+ drugs. The 19.7% vacancy rate and 16.5% annual voluntary turnover mean that the effective operational workforce is substantially smaller than the nominal headcount. The 40% personnel loss during the 2020 "One Agency Transformation Programme" -- which cost the agency many of its most experienced staff -- has not been fully recovered.

This capacity constraint has measurable downstream consequences. National route approvals reached 333 days against a 210-day statutory target in January 2024. Out of 154 innovative medicines studied, MHRA achieved only 1 first approval compared to FDA's 70, with FDA approvals averaging 360 days faster (PMC 2025). The MHRA used expedited pathways for only 11% of approvals versus FDA's 64%. Eighty percent of ABPI respondents reported that MHRA's lack of capacity was undermining industry trust and deterring domestic investment (ABPI, December 2024). Parliament held a major debate on MHRA performance in January 2025, raising pointed questions about safety monitoring adequacy.

These are not statistics an external partner should weaponise. They are the operational context that any serious collaborator must understand. The post-authorisation safety function -- the function we are engaging with -- operates at the sharp end of this capacity constraint. Every hour an assessor spends manually gathering, formatting, and cross-referencing published literature is an hour not spent on the expert appraisal and judgment that only qualified humans can perform.

### 2.2 The technology gap is real and recently demonstrated

The MHRA's RegulatoryConnect platform was cancelled in November 2025, less than two years after launch, because "the cost to complete the programme was considered too high for a solution which did not enable delivery of the aspirations of the agency." Before SafetyConnect/HALO, the agency's pharmacovigilance infrastructure included Lotus Notes and Excel spreadsheets. The institutional experience of a major failed technology investment creates both a heightened need for credible technology partners and a justified wariness of vendors who overpromise.

The SafetyConnect/HALO partnership with Insife addresses PV case management: ingesting Yellow Card reports, managing case workflows, feeding signal detection software. This is critical infrastructure. But it covers a different layer of the assessment process. HALO manages the cases. It does not structure the published scientific evidence -- the literature, observational studies, meta-analyses, mechanistic data, and cross-jurisdictional regulatory intelligence -- that assessors must assemble, appraise, and synthesise into benefit-risk judgments. That evidence-structuring layer is the gap ArcaScience addresses.

### 2.3 MHRA leadership explicitly prioritises digital enablement

Lawrence Tallon assumed the CEO role in April 2025, coming from an NHS operational background at Guy's and St Thomas'. His stated priorities include a "world-class, digitally enabled system for safety and surveillance" and his observation that "our ability to meet that demand with humans is finite" is not a soundbite -- it is an institutional thesis. His operational background (rather than purely regulatory) may make him more receptive to practical efficiency tools than to theoretical regulatory science propositions.

### 2.4 The strategic planning window is open

The MHRA is currently developing a new multi-year strategy through 2030, expected to launch in early 2026. This strategy will define the agency's technology partnerships, AI investment priorities, and operational modernisation agenda for the next half-decade. The MHRA Data Strategy 2024-2027 already explicitly calls for leveraging AI and advanced analytics throughout the product lifecycle. The Pilot RWE Dialogue Programme (launched January 2025), the AI Airlock regulatory sandbox (world-first, May 2024-April 2025), and the National Commission on AI in Healthcare (September 2025) all signal an institution actively seeking to integrate AI into its regulatory operations -- but seeking to do so responsibly, with transparency and demonstrated utility.

Partnerships that demonstrate value before the 2030 strategy crystallises have a structural advantage over those that arrive after strategic commitments are already locked.

### 2.5 The under-reporting problem strengthens the case for literature-based evidence

The Yellow Card system captures a fraction of actual adverse drug reactions. The median under-reporting rate across 37 studies is 94% (IQR 82-98%). Only an estimated 10% of serious reactions and 2-4% of non-serious reactions are reported. The IMMDS 2020 review ("First Do No Harm") concluded that the Yellow Card system is "too complex and too diffuse to allow early signal detection." Parliament echoed this criticism in January 2025, stating that the system has "no process for following up on serious or fatal reactions."

This under-reporting reality means that published literature -- case reports, observational cohort studies, registry analyses, meta-analyses, pharmacoepidemiological studies, and mechanistic investigations -- is not merely supplementary to spontaneous reporting. It is a structurally essential evidence stream that partially compensates for the known, quantified gap in spontaneous reporting data. Any system that can accelerate the systematic identification, extraction, and structuring of this published evidence directly addresses a documented weakness in the UK's drug safety surveillance architecture.

---

## 3. What ArcaScience Is -- and What It Is NOT

### What ArcaScience is

ArcaScience is an evidence-structuring platform built on 24 task-specific small language models arranged in a sequential, auditable pipeline. The system ingests, classifies, extracts, normalises, links, and templates regulatory and scientific documents. It processes published literature, clinical trial registries, regulatory documents, and (where authorised) client-provided private data, producing structured, traceable evidence packages -- not finished assessments, not regulatory conclusions, and not AI-generated opinions.

The platform has been validated across six peer-reviewed publications:

| Publication | Key finding | Journal |
|-------------|-------------|---------|
| AE extraction accuracy | 92% precision for adverse event extraction vs. 67% for GPT-4 | AI in Medicine, 2025 |
| Early signal detection | 3x improvement in early signal detection vs. manual processes | Journal of Pharmacoepidemiology, 2024 |
| NLP extraction performance | 94% F1 score for NLP adverse event extraction | BMC Medical Informatics, 2024 |
| PSUR generation efficiency | 60% reduction in PSUR generation time | Therapeutic Innovation & Regulatory Science, 2023 |

These are not marketing claims. They are independently reviewed, published findings with defined methodologies, sample sizes, and limitations that any assessor can examine.

The platform currently processes over 100 billion data points and achieves aggregate performance metrics of 94% accuracy, 91% precision, 89% recall, and an F1 score of 0.90 across its extraction pipeline. It holds GAMP 5, ISO 27001, and SOC 2 Type II certifications, and is FDA 21 CFR Part 11 compliant.

The system is designed to reduce the manual burden of evidence assembly, cross-referencing, and template pre-population so that qualified human assessors can invest their finite time in the work that only they can do: critical appraisal, contextual judgment, causality reasoning, and benefit-risk decision-making. The platform architecture is informed by the ICH E2C(R2) guideline and BRAT framework.

### What ArcaScience is NOT

| Boundary | Explanation |
|----------|-------------|
| **Not a decision-making system** | The platform does not render benefit-risk verdicts, determine causality, or produce regulatory recommendations. All judgment remains with the human assessor. In a regulatory system where assessments carry legal force and Parliamentary accountability, this is an architectural principle, not a disclaimer. |
| **Not a replacement for assessor expertise** | The system extracts and structures evidence. It does not assess study quality, evaluate methodology, or weigh competing evidence. An assessor evaluating whether a signal of euglycaemic DKA in SGLT2 inhibitors is confounded by concurrent illness brings decades of pharmacological judgment that no extraction pipeline can replicate. |
| **Not a generative AI chatbot** | Outputs are structured, templated documents with traceable provenance -- not free-text generated answers. The system does not hallucinate conclusions. It extracts what is stated in sources and flags what is absent. |
| **Not a tool that requires bespoke model-building per use case** | The 24 models are task-specific (e.g., adverse-event extraction, study-design classification), not therapeutic-area-specific. The same pipeline that processes cardiovascular literature processes oncology literature, neurology literature, and endocrinology literature. Adaptation to a new safety question is achieved through pipeline configuration, not model retraining. This is what makes it viable for an agency managing 80+ concurrent investigations simultaneously. |
| **Not a tool that processes imaging or omics data** | These data types are outside the current platform scope. Omics data is planned for a future R&D programme (BR-PREDICT, 2026-2029). We state this boundary clearly because "handles everything" claims from vendors should trigger the same scepticism Allison expressed about "benefit-risk in seconds." |
| **Not a tool that handles the "full drug lifecycle" without qualification** | The system covers evidence structuring across pre-clinical through post-authorisation phases for semantic and textual data sources. It does not cover all data types or all analytical activities at every phase. Precision about scope is a feature, not a limitation. |

---

## 4. MHRA Workflow Fit: Post-Authorisation Safety and Risk Management

### MHRA's post-authorisation workflow (as described in the meeting and corroborated by public documentation)

MHRA's post-authorisation safety function is issue-driven, not product-lifecycle-driven. This is a fundamental distinction from pharmaceutical-company use cases, where the workflow follows a single product through its lifecycle. MHRA assessors face the inverse problem: multiple drugs, multiple safety signals, multiple evidence bases, simultaneously, with finite human capacity.

The workflow proceeds through:

1. **Signal detection / intake.** A safety concern surfaces via Yellow Card spontaneous reports, published literature, stakeholder signals (MAHs, international regulators, patient groups), or the epidemiology team. Given the 94% under-reporting rate for ADRs via Yellow Card, published literature is not a secondary source -- it is a primary detection mechanism for signals that spontaneous reporting structurally misses.

2. **Scoping and triage.** The assessor determines the nature of the issue: which drug(s) or device(s) are affected, what the proposed harm mechanism is, whether the signal is new or an evolution of a known risk. With 80 concurrent investigations across 600+ drugs, triage decisions directly determine how the agency's finite assessor capacity is allocated.

3. **Evidence assembly.** The assessor gathers all relevant data: spontaneous reports, published observational studies, meta-analyses, clinical trial data (where available), real-world evidence from CPRD (65 million patients), PSUR/PBRER submissions from MAHs, and international regulatory intelligence from EMA, FDA, and other reference regulators. This is the most time-intensive manual step in the workflow. It involves searching multiple databases, reading and evaluating individual publications, extracting relevant data points, and organising them into a format suitable for appraisal. For a mature safety signal with extensive literature, this can involve hundreds of sources across multiple study types, geographies, and time periods.

4. **Critical appraisal.** The assessor evaluates each piece of evidence on its own terms: study methodology, confidence intervals, patient population representativeness, heterogeneity, sample size, duration, and potential confounders. This is expert-driven, manual, and irreducibly human. It is also where assessor time is most valuable and where the capacity crisis most directly impacts the quality and timeliness of safety decisions.

5. **Epidemiology team input.** For studies requiring specialist methodological review, the assessor requests formal input from the MHRA's epidemiology team.

6. **Benefit-risk judgment.** The assessor synthesises the evidence into an assessment report that weighs the identified risk against therapeutic benefit in the UK-specific context of use. MHRA works with effectiveness, not efficacy -- real-world UK prescribing patterns, patient demographics, and therapeutic alternatives, not idealised clinical trial populations.

7. **Regulatory action.** Label update, Dear Healthcare Professional Communication, restriction, or (rarely) withdrawal.

### Where ArcaScience fits: the evidence assembly bottleneck

The platform targets Steps 1-3 of this workflow -- signal triage support, evidence assembly, and structured extraction -- which together represent the highest-volume manual work in the assessment process. This is deliberate. We do not target the appraisal and judgment steps (Steps 4-6) because those require the expert pharmacological, epidemiological, and clinical reasoning that justifies the existence of a regulatory agency.

| Workflow step | Platform capability | Validated performance |
|---------------|---------------------|----------------------|
| **Signal triage support (Steps 1-2)** | Organises candidate signals by frequency, co-occurrence, and source type, flagging areas of higher or lower confidence for assessor prioritisation. Surfaces mechanism-of-action-based patterns across related compounds. | 3x improvement in early signal detection (Journal of Pharmacoepidemiology, 2024) |
| **Evidence assembly (Step 3)** | Automated identification, retrieval, classification, and structuring of published literature and regulatory documents relevant to a specified safety question. Classification by study type, population, design, and key findings. | 92% precision for AE extraction vs. 67% for GPT-4 (AI in Medicine, 2025); 94% F1 for NLP extraction (BMC Medical Informatics, 2024) |
| **Structured extraction (Steps 3-4 boundary)** | Extracts study design, population characteristics, sample sizes, adverse event terms, temporal relationships, dosage information, effect sizes, confidence intervals, and limitations from unstructured sources into normalised, queryable formats. Each extraction linked to source sentence. | 94% accuracy, 91% precision, 89% recall, F1=0.90 across pipeline |
| **Cross-referencing and evidence mapping (Step 3)** | Connects extracted entities across sources using standardised ontologies (MedDRA, SNOMED CT, ChEBI). Temporal mapping of when evidence became available relative to regulatory actions. | Operational; validated across 10,000+ documents |
| **Completeness checking (Step 3)** | Identifies evidence gaps: source types, geographic coverages, or time periods where expected evidence is absent. Surfaces what the evidence base lacks, not just what it contains. | Described as current capability; formally measured in PoC |
| **Template pre-population (Step 6 preparation)** | Pre-fills structured template sections (analogous to PSUR/DSUR safety evaluation sections) with extracted, sourced evidence for assessor review and completion. | 60% reduction in PSUR generation time (TIRS, 2023) |

### Where we do NOT replace MHRA

| Function | Why it remains with the assessor |
|----------|----------------------------------|
| **Causality determination** | Establishing whether a drug caused an adverse event requires integrating biological plausibility, temporal relationships, dose-response, dechallenge/rechallenge evidence, and confounders. This is expert pharmacological and epidemiological judgment that carries legal and clinical consequence. The Bradford Hill criteria cannot be algorithmically applied; they require contextual interpretation that only experienced assessors can provide. |
| **Study quality and validity assessment** | The platform extracts the elements assessors use to judge quality (methodology, CIs, population, heterogeneity, limitations) but does not itself render a quality verdict. Whether a 500-patient UK cohort study outweighs a 50,000-patient US registry analysis depends on context that the assessor determines. |
| **Benefit-risk conclusions** | The final weighing of benefits against risks is a regulatory act with legal, clinical, and ethical implications. It requires contextual judgment about UK-specific prescribing patterns, patient populations, therapeutic alternatives, and societal values. This is what Parliamentary accountability attaches to. |
| **Policy and regulatory decisions** | Label changes, communications, restrictions, and withdrawals are institutional decisions informed by -- but not determined by -- evidence assembly. |
| **Real-world effectiveness estimation** | Translating efficacy data from controlled trials into UK-specific real-world effectiveness requires understanding of UK prescribing practice, BNF positioning, NICE guidance implications, and patient demographics. MHRA works with effectiveness, not efficacy -- and this distinction is one that general-purpose AI tools systematically fail to respect. |

---

## 5. "Under the Hood": System Architecture and Auditability

This section is written to answer Allison's direct requirement: "I need to see under the hood." It is intended to be technically specific, not promotional.

### 5.1 High-level pipeline

The system processes documents through a sequential, chained pipeline. Each step produces auditable intermediate output before feeding the next step. The pipeline operates on 24 task-specific small language models (SLMs), not a single monolithic large language model. This architectural choice is deliberate: monolithic models are opaque, difficult to debug, and produce outputs that cannot be decomposed into verifiable intermediate steps. A pipeline of specialised models enables the granular traceability that regulatory use demands.

```
INGEST --> CLASSIFY --> SECTION ID --> EXTRACT --> RELATE --> NORMALISE --> LINK --> TEMPLATE

Legend: --> = auditable handoff; intermediate output inspectable at each boundary
```

| Step | Function | Output | Why it matters for MHRA |
|------|----------|--------|------------------------|
| **Ingest** | Accepts PDF, XML, DOC, and other semantic sources | Raw document in standardised internal format | Handles the heterogeneous document types MHRA assessors receive: published papers, regulatory documents, safety communications, SmPCs |
| **Classify** | Determines document type (case report, clinical trial, observational study, meta-analysis, regulatory document) | Document classification label with study design metadata (randomised, blinded, arms, etc.) | Enables automatic stratification by evidence type -- critical when an assessor reviewing 200+ sources for a safety signal needs to distinguish RCTs from case series from meta-analyses |
| **Section identification** | Identifies structural sections (abstract, methodology, results, discussion, safety) | Section boundaries with labels, routing downstream extraction to appropriate sections | Ensures adverse event data is extracted from results sections, not discussion speculation; methodology from methods sections, not abstract summaries |
| **Extract** | Extracts entities: adverse events, temporal status, drug names, severity, outcomes, patient demographics, study design elements, dosage | Structured entity records with source sentence references | This is the core value step. Published performance: 92% precision for AE extraction vs. 67% for GPT-4 (AI in Medicine, 2025) |
| **Relate** | Links extracted entities within context (e.g., "myocardial infarction is related to adalimumab in this sentence") | Entity-relationship pairs with sentence-level provenance | Preserves the associative context that distinguishes "Drug X was co-administered with Drug Y when Event Z occurred" from "Drug X caused Event Z" |
| **Normalise** | Maps extracted terms to standardised ontologies (restructured MedDRA, SNOMED CT, ChEBI, Disease Ontology) | Normalised entity codes | Enables cross-source comparison: "DKA," "diabetic ketoacidosis," "ketoacidosis in type 2 diabetes" all map to a single ontology node |
| **Link** | Connects entities across documents in a knowledge graph | Cross-source entity connections within the Profiling Base | Surfaces patterns across the full evidence corpus: mechanism-of-action-based associations, temporal evolution of evidence, geographic distribution |
| **Template** | Populates structured output formats | Assessor-ready structured evidence package (evidence maps, templated draft sections, traceability reports) | Delivers output in formats aligned with regulatory assessment structure, not as unstructured prose |

**Key architectural principle:** Every arrow in this pipeline represents an auditable boundary. The output of each step can be independently inspected and verified before it feeds the next step. There is no single opaque model producing end-to-end results. When Steph traces an extracted adverse event back through the pipeline, she can see: which document it came from, which section the system identified it in, what the extraction model produced, how the relation model linked it, and what ontology code the normalisation model assigned. If any step is wrong, the error is localisable.

**Infrastructure:** Apache Airflow DAGs ("Data Forge" pipelines) orchestrate execution on AWS Kubernetes. Storage: S3 (raw and enriched data), ElasticSearch (full-content indexing and analysis outputs), DocumentDB (structured documents), QDrant (ontology vectors). BRA platform: ReactJS/Tailwind CSS frontend, Node.js/NestJS backend, PostgreSQL database. Authentication: Keycloak (OAuth 2.0, OpenID Connect) with JWT-based role-based access control.

### 5.2 Traceability: every extracted statement links back to source

Every extracted element in the platform output links back to its source document, section, and sentence. This is not a supplementary feature -- it is the foundational architectural principle. In a regulatory environment where an assessor must be able to defend every statement in a benefit-risk assessment to PRAC, to Parliament, and to patients, unattributed assertions are worthless regardless of their accuracy.

| Provenance element | Description | Current status |
|-------------------|-------------|----------------|
| **Source document** | Original document (with DOI/PMID/URL) | Operational |
| **Source location** | Section, page, and sentence within the document | Operational |
| **Extraction model** | Which of the 24 SLMs produced the extraction | Operational (architectural principle) |
| **Confidence score** | Per-element confidence level | Planned (OKR Initiative 3) -- not yet operational |
| **Disagreement flags** | Where models or sources disagree on the same entity | Planned (OKR Initiative 3) -- not yet operational |
| **Missing evidence indicators** | Where expected evidence is absent | Planned (OKR Initiative 3) -- not yet operational |
| **Evidence Provenance Layer** (first-class UI feature) | Integrated audit trail in the platform interface | Planned (OKR Initiative 2) -- not yet operational |

**Honest disclosure:** Confidence scoring, disagreement flags, and missing evidence indicators are in development, not operational. We present this transparently because MHRA has been burned by vendors who present planned features as current capabilities -- most recently with RegulatoryConnect, which was shut down because it "did not enable delivery of the aspirations of the agency." We would rather demonstrate trust through honesty about development status than risk discovery of a gap during the PoC.

### 5.3 Model scope: task-specific models vs. therapeutic-area models

This distinction directly answers Allison's scalability concern: "We can't develop an AI model for every use case."

The 24 SLMs are trained for **specific tasks**, not for specific therapeutic areas. Each model performs one well-defined extraction or classification function regardless of the disease or drug under review. They were trained on 10,000+ documents spanning all therapeutic areas and all clinical phases (1-4).

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

**No new model is trained** when a new therapeutic area is addressed. The same 24 models operate across all therapeutic areas.

**Adaptation to a specific safety question** happens through pipeline configuration, not model retraining:
- Selecting which database subsets to query (reducing noise from irrelevant pathologies)
- Enabling/disabling specific model outputs (e.g., deactivating efficacy models when only safety is relevant)
- Defining which ontology subsets to prioritise
- Selecting the output template and format

This is analogous to an assessor defining a literature search strategy -- different scope, same analytical tools. An assessor investigating antidepressants and sexual dysfunction uses the same extraction models as one investigating SGLT2 inhibitors and DKA. Only the query scope differs. This is what makes the system viable for an agency running 80+ concurrent safety investigations: it does not require 80 separate model-development projects.

### 5.4 Error localisation

Because each SLM performs a single, well-defined task and produces inspectable output at each step boundary, errors can be localised to the specific step where they occurred:

| Step | What goes wrong if this step errs | How the error is detected |
|------|----------------------------------|--------------------------|
| Document classification | All downstream extraction operates on wrong assumptions (e.g., treating an observational study as an RCT) | Reviewer verifies document type assignment against the actual document |
| Section identification | Extraction models look in wrong sections of the document | Reviewer verifies section boundaries |
| Entity extraction | Specific entities are missed or miscategorised | Reviewer compares extracted entities against source text |
| Relation extraction | Associations between drugs and events are incorrect | Reviewer verifies the relation against the source sentence |
| Normalisation | Terms are mapped to wrong ontology codes | Reviewer verifies ontology mapping |
| Knowledge graph linking | Cross-source associations may be spurious | Reviewer inspects link rationale |

**Published error metrics:** Clinician-annotated test sets (dual-annotated independently by two clinicians) yield measurable error rates per step. The aggregate pipeline achieves 94% accuracy, 91% precision, 89% recall, and F1 = 0.90. For adverse event extraction specifically, published precision is 92% versus 67% for GPT-4 (AI in Medicine, 2025). For NLP adverse event extraction, published F1 is 94% (BMC Medical Informatics, 2024).

**Items not yet documented (presented transparently):**
- Formal error propagation analysis across the full chain (how a 5% error in Step 3 compounds through Steps 4-6)
- Automatic flagging when upstream errors may have affected downstream outputs
- Precision/recall breakdown per individual model (aggregate pipeline metrics are documented; per-model breakdowns are not published)
- Whether there are therapeutic areas or document types where model performance is significantly lower
- Specific SLM architectures and parameter counts
- Whether the system has undergone independent third-party audit or validation beyond peer-reviewed publications

These items are flagged as areas for investigation during the PoC, not concealed as non-issues.

---

## 6. Data Sources and Confidentiality Model

### Design philosophy

We designed this confidentiality architecture because we understand multi-regulator data sensitivity. MHRA handles data from multiple pharmaceutical companies simultaneously. Data from Company A's product must never be visible in work on Company B's product. Yellow Card patient-level data carries statutory confidentiality obligations. CPRD data operates under its own governance framework. Ongoing safety investigations are highly confidential until regulatory action is taken. This is not a typical enterprise data sensitivity challenge -- it is a multi-party, multi-classification, legally enforced confidentiality regime.

Our response to this reality is not to request exceptions. It is to design an engagement model where MHRA data never enters ArcaScience systems at any stage of the initial engagement, and where any future integration operates on a "bring the algorithm to the data" principle.

### 6.1 Public sources (Tier 1 -- no MHRA data required)

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

**Relevance to the under-reporting gap:** With a 94% median ADR under-reporting rate via Yellow Card, the published literature indexed in these sources represents a structurally essential evidence stream. Case reports, observational studies, and registry analyses published in peer-reviewed journals capture adverse events that never reach spontaneous reporting systems. Systematic extraction from these sources does not replace Yellow Card data -- it compensates for its documented quantitative limitations.

### 6.2 Private sources (MHRA internal -- never leaves MHRA infrastructure)

| Source | Classification | Handling rule |
|--------|---------------|---------------|
| **Yellow Card reports** (patient-level) | Strictly confidential | Must remain within MHRA infrastructure at all times. No extraction, no transmission, no external processing. |
| **CPRD** (65 million patients) | Restricted access | Any processing must occur in-situ within MHRA's secure environment under CPRD's own governance framework. |
| **Ongoing safety issue dossiers** | Highly confidential | Cannot be shared with external parties while under active review. |
| **Company-submitted data** (PSURs, PBRERs, RMPs, safety variations) | Commercially confidential | Multi-company data under statutory confidentiality obligations. The multi-tenant isolation requirement is structurally different from single-company pharmaceutical client engagements. |
| **Completed internal assessments** (unpublished) | Confidential | Available only if MHRA chooses to declassify or publish. |

### 6.3 Phased approach: public data first, on-premises later

**Phase 1 (proof of concept): Public-domain data only.**

All processing occurs on ArcaScience infrastructure using Tier 1 sources. Zero MHRA data enters ArcaScience systems. MHRA selects the topic, ArcaScience produces the output, and MHRA evaluates internally against their own historical assessment. No confidentiality risk exists because no confidential data is involved.

**Phase 2+ (future, if warranted): On-premises deployment within MHRA infrastructure.**

ArcaScience's 100% Kubernetes-based infrastructure is architecturally portable to on-premises deployment. Under this model:

- ArcaScience models are deployed into MHRA's environment
- All data remains within MHRA's infrastructure boundary
- No data is transmitted to ArcaScience servers
- MHRA IT controls access, networking, and audit logging
- ArcaScience provides model artefacts and configuration support only

This "bring the algorithm to the data" architecture is how we serve enterprise pharmaceutical clients who operate under comparable (though not identical) data sensitivity requirements. AstraZeneca, Novartis, Sanofi, and Roche have each engaged with deployment models that reflect their own data governance constraints.

On-premises deployment is planned in the ArcaScience OKR documentation and is included in the Enterprise tier pricing. However, we present it as a Phase 2+ objective, not a near-term deliverable, because trust must be established through the public-domain PoC before infrastructure integration discussions are warranted.

**Feasibility items requiring confirmation for Phase 2+:**
- Whether all 24 SLMs can operate fully air-gapped (no outbound connectivity)
- Specific hardware requirements (GPU specifications, storage, network bandwidth)
- Whether Keycloak can integrate with MHRA's identity infrastructure
- Licensing model for on-premises deployment
- Model update and maintenance procedures in an isolated environment

### 6.4 Handling CPRD at scale

CPRD (65 million patient records) represents the most data-intensive future scenario. The proposed pattern is **in-place query processing** ("bring the algorithm to the data"):

- ArcaScience extraction models are deployed inside the secure environment hosting CPRD
- Models query the data; data does not move
- Outputs are de-identified, statistical-level summaries only (incidence rates, relative risks, confidence intervals) -- no patient-level records extracted
- MHRA assessors define query parameters; models execute extraction; MHRA reviews aggregate output

**Honest status:** A CPRD-specific connector has not been developed. Data schema mapping, performance characteristics at CPRD scale, and whether MHRA's CPRD access terms permit third-party algorithm execution are all unresolved. CPRD integration is a future research objective, not a near-term deliverable. We raise it here to demonstrate we have thought about the eventual architecture, not to imply it is ready.

### 6.5 Security controls and compliance

**Current ArcaScience certifications and compliance:**

| Control | Status |
|---------|--------|
| ISO 27001 | Certified |
| SOC 2 Type II | Certified |
| GAMP 5 | Compliant |
| FDA 21 CFR Part 11 | Compliant |
| GDPR (EU) | Compliant |
| HIPAA | Compliant |
| HDS (French health data hosting) | Compliant |
| Authentication | Keycloak with OAuth 2.0 and OpenID Connect |
| Authorisation | JWT-based Role-Based Access Control (RBAC) |
| API security | Rate limiting, request throttling, comprehensive structured logging |
| Infrastructure | 100% Kubernetes on AWS |
| Code quality | SonarQube quality gates enforced on all production deployments |

**UK government requirements likely needed for Phase 2+ (all require confirmation):**

| Requirement | Description | Status |
|-------------|-------------|--------|
| Cyber Essentials Plus | UK government baseline cybersecurity certification | Not yet obtained |
| NHS DSPT | Data Security and Protection Toolkit | Not yet obtained |
| UK GDPR / DPA 2018 | UK-specific data protection provisions | EU GDPR compliant; UK-specific compliance to be confirmed |
| G-Cloud listing | UK government cloud services marketplace | Not yet listed |
| Data residency | UK-based data centre hosting | AWS UK region to be confirmed |
| DPIA | Data Protection Impact Assessment | Would need joint development |

These UK-specific compliance items are Phase 2+ requirements. For the Phase 1 PoC using only public-domain data, they are not triggered.

---

## 7. Quality Control and Uncertainty Handling

### 7.1 What the system measures and flags

| Capability | How it works | Current status | Relevance to MHRA |
|-----------|-------------|----------------|-------------------|
| **Missingness detection** | Identifies where expected data fields are absent from a source (e.g., no CIs reported, no follow-up duration stated) and flags the gap | Operational | When an assessor is reviewing 200+ sources for a safety signal, knowing which studies lack key data elements before reading them prioritises review time |
| **Contradictory evidence flags** | Where sources disagree on the same drug-event association, both versions are preserved and presented side by side with full provenance | Operational; formal conflict-resolution methodology in development | Particularly relevant for post-marketing signals where observational studies frequently disagree due to differences in population, confounders, and methodology |
| **Provenance tracking** | Every extracted data element linked to source document, section, page/paragraph, and extraction step | Operational for source-to-statement linkage | The bedrock requirement. Without this, no regulatory assessor should trust any output. |
| **Extraction confidence** | Per-element scoring based on extraction certainty (explicit statement vs. inferred), source reliability, and cross-source consistency | Planned (OKR Initiative 3); not yet operational | Will enable assessors to prioritise review of lower-confidence extractions |
| **Data completeness metrics** | Percentage of expected data fields populated per source type | Operational per analysis | Quantifies how complete the evidence base is before the assessor begins appraisal |
| **Evidence gap identification** | Systematic identification of missing evidence types, geographic coverage gaps, or temporal gaps | Part of planned deliverables | Shows the assessor what the evidence base lacks -- not just what it contains |

### 7.2 What requires human judgment -- and what we extract to support it

| Dimension | What the system extracts | What the assessor determines |
|-----------|-------------------------|------------------------------|
| **Study validity** | Study design, population, sample size, methodology description, statistical methods, limitations acknowledged | Whether the methodology is adequate for the question being asked |
| **Clinical significance** | Effect sizes, confidence intervals, p-values where reported | Whether the effect is clinically meaningful in the UK context of use |
| **Bias assessment** | Study design features indicating potential bias (unblinded, no placebo arm, single-centre, industry-funded) | The overall risk of bias and its implications for the findings |
| **Causality** | Temporal relationships, dose-response data, dechallenge/rechallenge data, mechanistic evidence where reported | Whether the association is causal -- the judgment that Bradford Hill criteria inform but do not determine algorithmically |
| **UK applicability** | Geographic origin of study population, indication, dosing regimen | Whether the findings apply to UK prescribing patterns and patient demographics |

This distinction is the core of the system's regulatory positioning. As stated in the meeting: "We don't assume if the study has quality or not. We tell you the sample size was 100. It was for 6 months." The system performs extraction and structuring, not evaluation and judgment.

### 7.3 Critical appraisal element extraction

For each source processed, the system extracts and presents the following critical appraisal elements (where reported in the source):

- **Study design classification** -- RCT, cohort, case-control, case series, case report, meta-analysis, systematic review
- **Population characteristics** -- age, sex, comorbidities, geographic setting, inclusion/exclusion criteria
- **Sample size and follow-up duration**
- **Outcome definitions and measurement methods**
- **Effect sizes with confidence intervals** -- odds ratios, hazard ratios, relative risks, p-values where reported
- **Confounders assessed** -- which confounders the study adjusted for (and, critically, which it did not)
- **Limitations** -- as acknowledged by the study authors
- **Funding and conflict of interest** -- sources and declared conflicts where reported
- **Bias signals** -- absence of blinding, short follow-up, highly selected populations, discrepancies between abstract conclusions and reported data

This is the critical differentiator from general-purpose tools. ChatGPT or Copilot can summarise a paper's conclusions. This system extracts the methodological components that allow the assessor to determine whether those conclusions are trustworthy -- then presents them in a structured, cross-study-comparable format with paragraph-level source traceability. When an assessor is reviewing 150 publications on a safety signal, the difference between reading 150 abstracts and reviewing 150 structured extractions with flagged limitations and missing data fields is the difference between days of work and hours of review.

---

## 8. Addressing the Key Objections from the Meeting

### 8.1 "Fill BR in seconds" scepticism

**MHRA concern (Allison):** "My antibodies are going through the roof just because it says fill your benefit risk in seconds."

**Our response:** That messaging was wrong. Not merely inappropriate for the regulatory context -- wrong. Benefit-risk assessment is not a task that can be completed "in seconds" because it is not fundamentally a speed problem. It is a judgment problem that requires time, expertise, and deliberation. What can be accelerated is the evidence consolidation that precedes that judgment: the gathering, structuring, and cross-referencing of published literature and regulatory data across hundreds of sources.

When AstraZeneca used the platform, they achieved a 68% reduction in benefit-risk assessment cycle time. When Sanofi used it, they achieved 52% faster regulatory submissions. When Novartis deployed it across 300+ products, they realised $12M in annual savings. These are evidence assembly efficiencies, not judgment compression. The assessment itself proceeds at the assessor's pace, under the assessor's authority, on the assessor's timeline.

All speed claims and marketing language have been removed from any materials MHRA may see. The claim "currently under review by the MHRA" has been deleted from the sales deck. We take this seriously because Allison's reaction was not merely a communication preference -- it was a signal that the credibility of the entire engagement depends on our willingness to be honest about what the system does and does not do.

### 8.2 Validation of chained models and audit trail

**MHRA concern (Allison):** "When you've got such complex models that they're happening in series, how do you validate them?"

**Response:** Four complementary validation methods are used:

1. **Clinician-annotated test sets.** Dual-annotated independently by two clinicians, yielding measured precision, recall, and F1 per extraction task. Published aggregate: 94% F1 for NLP AE extraction (BMC Medical Informatics, 2024). Published AE-specific precision: 92% vs. 67% for GPT-4 (AI in Medicine, 2025).

2. **Noise-injected testing.** Statistical comparison against data known to contain noise, establishing performance bounds under realistic, messy-data conditions -- precisely the conditions MHRA assessors work in.

3. **Blind comparison against independent assessment.** The client's existing, independently created work product serves as ground truth. The system's output is compared against what experienced assessors already produced. This is the validation method the PoC employs: MHRA's historical assessment of the chosen safety issue is the benchmark.

4. **Client-specific sampling.** Validation on the particular therapeutic area to confirm general-model performance on specific use cases.

**Per-step auditability:** Every intermediate output is inspectable. If an adverse event extraction is incorrect, the reviewer can see the source sentence, what was extracted, and at which step the error occurred. Errors in classification (Step 1) propagate differently from errors in normalisation (Step 5), and the chain's modular design enables the reviewer to identify the origin.

**Open item:** Formal error propagation modelling across the full chain (quantifying how upstream errors compound through downstream steps) is not yet documented. This is acknowledged transparently.

### 8.3 Managing incomplete and inconsistent data

**MHRA concern (Sharinto):** "What we wouldn't want is a skewed view because of perhaps incomplete or inconsistent data."

**Response:** This concern is particularly acute in the post-authorisation context. Unlike clinical trial data, post-marketing evidence is characterised by heterogeneous study designs, inconsistent outcome definitions, variable populations, and missing data. The system's design addresses this directly:

- **Gap flagging:** The system explicitly reports what expected data fields are missing per source and what evidence types are absent from the corpus. It tells the assessor "no UK-specific incidence data was found" or "no mechanistic studies were identified" -- surfacing what is not there, which is as important as surfacing what is.
- **Conflicting evidence preservation:** When sources disagree, both versions are preserved and flagged with full provenance. The system does not silently resolve conflicts. If one cohort study reports increased DKA risk with SGLT2 inhibitors and another finds no significant association, both appear with their respective methodologies, populations, and confidence intervals intact.
- **Source stratification:** Every extracted element is tagged with its source type, enabling assessors to filter by evidence hierarchy.
- **Data completeness metrics:** Measured as percentage of expected data fields populated per source type, reported per analysis.

The system does not present incomplete data as complete. It surfaces what is found, flags what is missing, and leaves the judgment of significance to the assessor.

### 8.4 Applicability to long-marketed drugs and rare events

**MHRA concern (Allison):** "Those are much easier questions than for drugs that have been on the market for a long time."

**Response:** This is the correct challenge to pose, and it is why the proof of concept deliberately targets a long-marketed drug class, not a novel product. The extraction pipeline does not depend on clean clinical trial data. It handles observational studies, meta-analyses, case series, spontaneous reporting analyses, and regulatory documents -- the evidence types that dominate post-marketing surveillance for mature products with decades of exposure data.

For causality assessment in particular, the system extracts the elements assessors use in causal reasoning: temporal relationships, dose-response data, dechallenge/rechallenge information, biological plausibility evidence from mechanistic studies, and confounders assessed in observational analyses. It does not render a causality judgment -- but it ensures the relevant data elements are organised, sourced, and ready for expert interpretation.

**Case study evidence:** The platform has been deployed across enterprises managing mature product portfolios. Novartis used the platform across 300+ products -- not exclusively novel compounds, but the full portfolio including mature, long-marketed medicines where the evidence base is large, heterogeneous, and accumulated over decades.

**Honest limitation:** The system has been primarily validated with pharmaceutical clients working on product-development and lifecycle-management use cases. Performance on the specific pattern of post-authorisation regulatory assessment -- where the assessor serves the public interest rather than the sponsor's interest, and where the evidence is assembled from scratch rather than from a company dossier -- has not been demonstrated at scale to a regulatory audience. This is precisely what the proof of concept is designed to test.

### 8.5 Generalised usage without bespoke models

**MHRA concern (Allison):** "What I can't see working is for every specific use case, I have to build a bespoke model."

**Response:** No new model is developed per safety question. The 24 task-specific models are reused across all use cases. What changes per question is pipeline configuration -- which sources to query, which ontology subsets to prioritise, which output templates to use. This is analogous to defining a literature search strategy, not building a new analytical tool.

**Differentiation from ChatGPT/Copilot at the level Allison demanded:**

General-purpose LLMs can summarise papers and answer questions. They cannot:
- Systematically extract structured critical appraisal elements across hundreds of sources in a consistent schema with 92% precision (vs. their own 67%)
- Normalise extracted terms to MedDRA and SNOMED CT with ontology-level precision
- Provide paragraph-level traceability from every output element to its source document and sentence
- Produce gap analyses identifying what evidence types are absent from the assembled corpus
- Cross-reference findings across sources by mechanism of action in a knowledge graph
- Present assessors with structured, auditable evidence packages rather than generated prose
- Maintain performance consistency across hundreds of documents (LLM output quality degrades with context length; pipeline architecture does not)

The published data substantiates this: 92% AE extraction precision for ArcaScience's pipeline versus 67% for GPT-4, tested on the same corpus (AI in Medicine, 2025). The gap is not marginal.

### 8.6 UK context: effectiveness, not efficacy

**MHRA concern (Allison):** "Usage of drugs is very different across the world... We don't do efficacy, of course, we do effectiveness."

**Response:**

- **What the system can do:** Extract and tag evidence by geographic origin. Extract line-of-therapy information where reported. Filter evidence by population characteristics relevant to UK prescribing. Distinguish efficacy data (labelled as such) from effectiveness data. Flag when evidence is drawn exclusively from non-UK populations.
- **What the system cannot do:** Determine whether a non-UK study applies to UK clinical practice. Assess how UK prescribing patterns affect the benefit-risk balance. Translate efficacy to effectiveness. These translations require understanding of BNF positioning, NICE guidance context, and UK-specific prescribing culture.
- **What could be explored in Phase 2+:** Integration of UK-specific sources (NICE guidelines, BNF, published CPRD analyses) alongside extracted evidence. Systematic flagging of evidence geographic origin as a standard output feature.

For the proof of concept, UK-specific evidence sources (MHRA Drug Safety Updates, UK-authored studies) will be specifically highlighted, and the geographic origin of all evidence will be tagged and filterable.

---

## 9. Proposed Collaboration: A Self-Funded, Public-Domain Proof of Concept

### 9.1 Design rationale

This PoC is designed to answer one question: **Does this platform add meaningful value to the evidence assembly phase of an MHRA post-authorisation safety assessment?**

It is not designed to demonstrate the system at its best (which would use proprietary data sources and company-curated dossiers). It is designed to demonstrate the system under the constraints MHRA actually faces: no budget, no data sharing, no institutional commitment -- and to deliver evidence of utility compelling enough to justify the next step.

The format was proposed by MHRA themselves. They want a challenge test, not a demonstration. We welcome this framing because it aligns with how we have validated the platform with pharmaceutical clients: blind comparison against independently produced assessments.

### 9.2 Criteria for selecting a public-domain safety issue

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | **Closed or publicly reported** | MHRA cannot share confidential ongoing assessments |
| 2 | **Long-marketed drug class** | Novel-product cases are "much easier" and would not demonstrate relevant capability |
| 3 | **Substantial public-domain evidence base** | Enough literature, PARs, safety communications, and observational studies for meaningful testing |
| 4 | **Messy, heterogeneous evidence** | Must include observational studies, case reports, meta-analyses, mechanistic studies -- not just clean RCTs |
| 5 | **Multi-regulator action** | MHRA, EMA (PRAC), and FDA all published independent assessments, enabling cross-referencing |
| 6 | **UK-specific considerations** | Issues where MHRA took distinct UK-specific action are preferred |
| 7 | **Causality complexity** | Genuine causality challenges: confounding, atypical presentations, difficulty distinguishing drug effect from underlying disease |
| 8 | **Sufficient volume** | At minimum 100+ relevant publications across study types to stress-test the pipeline at scale |

MHRA will have final selection authority.

### 9.3 Candidate PoC options

#### Option A: SGLT2 Inhibitors and Diabetic Ketoacidosis (DKA) -- RECOMMENDED

**Drug class:** Canagliflozin, dapagliflozin, empagliflozin (oral antidiabetics, first authorised EU 2012-2014).

**Safety issue:** Post-marketing identification of rare diabetic ketoacidosis, often presenting atypically with near-normal blood glucose ("euglycaemic DKA"). Coordinated regulatory action across MHRA, EMA, and FDA between 2015-2016, with follow-up through 2022.

**Why it is the right test for MHRA's requirements:**
- **Causality complexity directly relevant to post-authorisation assessment:** Euglycaemic DKA was mechanistically unexpected; confounders (infection, surgery, fasting, insulin reduction) complicated the signal; the association was initially controversial. This is the archetypal post-marketing causality challenge Allison described: a rare event in a long-marketed drug class where the assessor must disentangle drug effect from underlying disease and concurrent risk factors.
- **Evidence heterogeneity matching MHRA's operational reality:** Spontaneous reporting analyses, clinical trial re-analyses, observational cohort studies, mechanistic hypotheses, case series, systematic reviews, and cross-jurisdictional regulatory intelligence. Precisely the evidence mix an MHRA assessor faces.
- **Post-marketing, long-marketed class** with millions of patient-years of exposure by the time of regulatory review.
- **Generic applicability:** "Does this drug class cause this rare serious adverse event, and in what context?" is the archetypal question across all 80 of MHRA's concurrent safety investigations. Demonstrating pipeline performance on this question template has implications for the full portfolio.
- **Low political sensitivity** -- well-bounded evidence base with clear regulatory endpoints.

**What the PoC will specifically demonstrate against MHRA's 80-investigation workload:**

If the pipeline can assemble, structure, and cross-reference the evidence base for SGLT2/DKA -- identifying sources, extracting critical appraisal elements, flagging contradictions, mapping evidence evolution, and highlighting gaps -- in days rather than the weeks an assessor would typically invest, this translates directly to capacity recovery across all 80 concurrent investigations. At 60% PSUR generation time reduction (demonstrated; TIRS 2023) and 3x improvement in early signal detection (demonstrated; Journal of Pharmacoepidemiology 2024), the compound effect across 80 simultaneous workstreams is transformative for an agency operating at structural capacity deficit.

**Key public sources:**
- MHRA Drug Safety Update: SGLT2 inhibitors and DKA risk (2016)
- EMA Article 20 referral (full PRAC assessment report)
- FDA Drug Safety Communication (2015)
- Frontiers in Pharmacology systematic review (2023)
- NEJM correspondence (2017)

#### Option B: Fluoroquinolone Antibiotics and Disabling Side Effects -- BACKUP

**Drug class:** Ciprofloxacin, levofloxacin, moxifloxacin, ofloxacin (marketed since late 1980s).

**Safety issue:** Disabling and potentially permanent side effects: tendon rupture, peripheral neuropathy, psychiatric effects, aortic aneurysm. EMA Article 31 referral (2017-2019), MHRA risk minimisation review (2023) with additional UK-specific restrictions (January 2024).

**Why it fits:**
- 35+ years on market; evidence spanning decades
- MHRA conducted its own risk minimisation review and published a Public Assessment Report with UK-specific restrictions going beyond EU-harmonised measures
- Multi-system adverse events testing pipeline breadth
- Risk minimisation effectiveness dimension (MHRA found prescribing had not changed despite 2019 restrictions)
- Higher complexity and larger evidence base than Option A

#### Option C: Sodium Valproate and Pregnancy Risks -- RESERVE (propose only if MHRA requests)

**Drug class:** Sodium valproate (marketed since 1972).

**Safety issue:** Teratogenicity (~10% malformation rate), neurodevelopmental harm (30-40% of exposed children), evolving male-mediated risk. MHRA Pregnancy Prevention Programme, EMA Article 31 referral, Cumberlege Review ("First Do No Harm," 2020).

**Political sensitivity:** High -- the Cumberlege Review criticised MHRA directly. This case also touches on the Yellow Card system's documented failure to detect signals early enough. Do not propose first. Present only as a third option if requested.

**Recommendation:** Option A as primary. It is the best balance of complexity and manageability for a first proof of concept. The question it addresses -- "Does this drug class cause this rare SAE, and under what circumstances?" -- is the generic post-marketing pharmacovigilance question that recurs across MHRA's entire 80-investigation portfolio.

### 9.4 Success metrics

**Quantitative:**

| Metric | Target | How measured | Why this target |
|--------|--------|-------------|-----------------|
| Source completeness | >= 90% of sources cited in published regulatory assessment identified by pipeline | Compare pipeline output to PRAC/MHRA report citation list | Demonstrates the pipeline finds what the assessor found -- the baseline utility test |
| Extraction accuracy | >= 95% factual accuracy on audited sample (minimum 50 extractions spot-checked) | Blinded audit by MHRA assessor comparing extracted elements to source | Above the aggregate 94% accuracy; establishes that precision does not degrade on regulatory-specific content |
| Traceability completeness | 100% of extracted elements with verifiable source link | Systematic check of source links in output | Non-negotiable for regulatory use; any unattributed extraction is a failure |
| Critical appraisal coverage | >= 80% of applicable quality indicators extracted per source | Structured review against pre-defined checklist | Demonstrates value beyond ChatGPT-level summarisation |
| Error rate | < 2% factual errors, hallucinations, or misattributions | Independent audit of randomly sampled extractions | Hallucination rate must be negligible for regulatory trust |
| False negatives | < 10% of sources in reference assessment missed by pipeline | Gap analysis comparing pipeline output to reference | Measures whether the system finds what matters, not just what is easy |
| Time comparison | Evidence assembly in days vs. estimated weeks for manual process | Comparison of pipeline runtime to MHRA's estimate of manual evidence assembly time for comparable issue | Demonstrates the capacity-recovery value proposition |

**Qualitative:**

| Metric | How measured |
|--------|-------------|
| Assessor satisfaction | Semi-structured feedback; assessors rate utility, trust, and usability on 5-point scale |
| "Beyond literature search" test | Direct comparison: "Could you have gotten this from PubMed + ChatGPT?" -- Yes/No with explanation |
| Assessor trust | Feedback on which output elements assessors would use vs. which they would re-verify independently |
| Actionability | Assessor judgment: "If this were a live signal, would this output accelerate your assessment?" |
| Gap analysis value | Assessor judgment: "Did the gap analysis identify evidence types we should have looked for but didn't?" |

### 9.5 Deliverables MHRA would receive

All deliverables produced by ArcaScience at its own expense using only public-domain data.

1. **Evidence map.** Comprehensive structured inventory of all relevant public-domain sources: full citation, document type (regulatory assessment, clinical trial publication, observational study, case report, meta-analysis, safety communication, mechanistic study), classification by evidence type/design/population/geography/date, temporal mapping showing when evidence became available relative to regulatory actions taken by MHRA, EMA, and FDA. This temporal dimension surfaces whether evidence existed before regulatory action was taken -- a question with direct relevance to MHRA's accountability for timeliness of safety response.

2. **Structured extraction output.** For each source: study characteristics (design, population, sample size, duration, setting, inclusion/exclusion criteria), key findings (primary outcomes, effect sizes with CIs, statistical significance, secondary findings), critical appraisal elements (confounders assessed, biases identified, limitations, quality indicators), adverse event data (extracted at 92% precision with full sentence-level provenance), and identification of which elements were cited in regulatory assessments.

3. **Templated draft sections.** Structured output organised analogously to PSUR/DSUR safety evaluation sections: summary of safety concern, clinical trial evidence, published spontaneous reporting data (aggregate only), observational/epidemiological studies, mechanistic evidence, regulatory actions taken (cross-jurisdictional comparison). These are draft structures for assessor review -- not finished regulatory documents. The 60% PSUR generation time reduction demonstrated in TIRS (2023) reflects this template pre-population capability.

4. **Traceability report.** Complete audit trail: every extracted element linked to source document, section, page/paragraph, pipeline step that produced the extraction. Conflicts between sources flagged with both versions preserved. This is the deliverable that directly addresses "I need to see under the hood" -- every assertion can be traced back to its origin.

5. **Gap analysis.** Identification of: evidence types present in the published assessment that the pipeline could not access (e.g., unpublished sponsor data, confidential ICSR line listings); evidence types that should exist but were not found; geographic gaps (e.g., UK-specific incidence data present or absent); temporal gaps (e.g., no studies after a certain year). This demonstrates the system knows what it does not know -- a capability that directly addresses Sharinto's concern about presenting incomplete evidence as complete.

6. **Cross-jurisdictional regulatory comparison.** Side-by-side comparison of MHRA, EMA, and FDA regulatory actions on the same safety issue: timing of actions, scope of label changes, risk minimisation measures, and any divergent conclusions. This demonstrates the platform's utility for the international regulatory intelligence dimension of MHRA's work.

### 9.6 Timeline

| Phase | Duration | Activities | MHRA commitment |
|-------|----------|------------|-----------------|
| **Phase 0: Joint scoping** | Week 0 (1 meeting + 1 week for written confirmation) | ArcaScience presents candidate issues; MHRA selects one; joint agreement on scope, data boundaries, success criteria, assessor availability. Lightweight collaboration letter (no contract, no funding, no data exchange, no IP implications). | 1-2 assessors, one 60-minute meeting + email confirmation |
| **Phase 1: Evidence assembly and extraction** | Weeks 1-2 | Week 1: Pipeline ingestion, evidence map construction, source classification, extraction with traceability. Week 2: Internal QC, deliverable preparation, comparison of ArcaScience outputs vs. published regulatory assessment. | None (ArcaScience works independently) |
| **Phase 2: Joint review and feedback** | Week 3 | Deliverables sent to MHRA 2-3 days before review. 90-minute review session: walkthrough (15 min), assessor review of evidence map and extractions (30 min), traceability deep dive (20 min), feedback and gap analysis review (15 min), next steps (10 min). | 1-2 assessors, 90-minute session + optional written feedback |

**Total elapsed time:** 4 weeks from kickoff to completion.
**Total MHRA time commitment:** Approximately 3-4 hours of assessor time across the entire PoC.
**Total ArcaScience cost:** Absorbed internally as strategic investment.

---

## 10. Next Meeting Agenda (60 Minutes)

This agenda is for the follow-up meeting to propose and scope the proof of concept.

| Time | Item | Purpose | What MHRA will see |
|------|------|---------|-------------------|
| 0:00 - 0:10 | **Confirm use case and data boundaries** | Present candidate safety issues with rationale. MHRA confirms or modifies selection. Agree exact scope, data boundaries, and success criteria. | Candidate options with selection criteria; transparent discussion of boundaries |
| 0:10 - 0:25 | **Under-the-hood walkthrough** | Pipeline architecture, task-specific model explanation, validation approach, traceability mechanism. No marketing slides. Technical depth appropriate for Steph and Allison. | Architecture diagram; model inventory; validation methodology; published performance data |
| 0:25 - 0:45 | **Live demonstration on chosen safety issue** | Pipeline running on 3-5 representative sources for the agreed issue. Show extraction from an observational study (not just case reports). Show document classification. Show source traceability at the sentence level. Show how conflicting evidence is preserved. | Working system with real documents; live traceability drill-down; comparison of extraction quality vs. what GPT-4 produces on the same source |
| 0:45 - 0:55 | **Review outputs and traceability challenge** | Walk through sample evidence map, structured extraction, and gap analysis. MHRA assessors select specific extracted elements and trace them back to source. Demonstrate what the system flags as missing. | Assessor-controlled traceability verification; system output for interrogation |
| 0:55 - 1:00 | **Agree next steps** | Confirm whether MHRA is comfortable proceeding with the PoC. Agree timeline, assessor availability, and communication channel. | Clear, low-commitment next step with defined scope |

**Preparation required before this meeting:**
- Working demo ready on at least the primary candidate issue (SGLT2/DKA) using exclusively public-domain sources
- Architecture walkthrough prepared for non-marketing, technically detailed presentation
- Data governance framework ready to reference if confidentiality questions arise
- All marketing materials and website claims updated per positioning audit -- no speed claims, no superlatives, no "under review by MHRA" language in any material accessible to MHRA
- Side-by-side comparison prepared: ArcaScience extraction vs. GPT-4 extraction on the same 3 sources, to substantiate the published 92% vs. 67% precision differential
- Prepared to address: "What happens when the system gets it wrong?" with specific error examples and localisation demonstrations

---

## 11. Appendix

### Appendix A: "Claims We Will NOT Make" -- A Statement of Scientific Integrity

The following commitments are not defensive caveats. They are a statement of the scientific and professional standards ArcaScience applies to regulatory engagement. In a sector where vendors routinely overstate capabilities, these commitments should increase confidence in the claims we do make. Every vendor promises accuracy; the ones worth trusting are those who publicly define what they will not claim and accept the accountability that creates.

These commitments are binding on all ArcaScience personnel involved in the MHRA engagement.

1. **We will NOT claim that ArcaScience "performs" or "completes" benefit-risk assessment.** The system supports and informs the assessment. The assessment is performed by qualified human experts whose judgment carries legal, clinical, and Parliamentary accountability.

2. **We will NOT claim that the system produces results "in seconds."** We will describe what is accelerated (data retrieval, cross-referencing, initial structuring) and what proceeds at the assessor's pace (expert review, contextual judgment, committee deliberation). The 60% PSUR generation time reduction (TIRS, 2023) reflects evidence assembly efficiency, not assessment compression.

3. **We will NOT claim "100% regulatory acceptance rate."** Regulatory acceptance of a submission reflects the totality of the sponsor's data and arguments, not the tool used to assemble them. We will say: "Our outputs have been incorporated into regulatory submissions by pharmaceutical clients including AstraZeneca, Sanofi, Novartis, Roche, and ICON."

4. **We will NOT claim that the system "replaces" or "automates" assessor judgment.** The system augments human capacity. Tallon's observation that "our ability to meet that demand with humans is finite" describes the problem; our system addresses the evidence assembly dimension of that problem, not the judgment dimension.

5. **We will NOT claim that ArcaScience is "under review by the MHRA" or that MHRA is evaluating ArcaScience for endorsement.** The engagement is accurately described as: "exploratory discussions about potential utility of structured evidence tools in post-authorisation safety assessment."

6. **We will NOT claim "100% accuracy" or "zero hallucination."** We will provide validated performance metrics with defined error rates and known limitations: 94% accuracy, 91% precision, 89% recall, F1 = 0.90 aggregate; 92% AE extraction precision; 94% NLP F1. These are strong metrics. They are not perfect. We report the gap because the gap matters in pharmacovigilance, where false negatives can mean missed safety signals.

7. **We will NOT use "world's largest" or any unverifiable superlative** about database size, model count, or capability scope.

8. **We will NOT claim the system handles the "full drug lifecycle" without immediately specifying** which phases are covered, which data types are excluded (imaging, omics, CPRD-scale databases), and where future development is planned versus operational today.

9. **We will NOT claim that the system "detects insights" or "finds signals" without qualification.** AI-identified patterns are candidate observations requiring expert validation. A pattern is not a signal; a signal is not a confirmed risk. The distinction matters because premature signal escalation wastes assessor time, and missed signals harm patients.

10. **We will NOT cite metrics without methodology.** Every performance claim will include baseline, methodology, sample size, and context. The 92% vs. 67% AE extraction precision comparison (AI in Medicine, 2025) has a defined corpus, methodology, and peer review process. Uncontextualised metrics will not appear in regulator-facing materials.

11. **We will NOT describe outputs as "generated documents."** We will say: "pre-populates structured templates for expert review and completion."

12. **We will NOT reference competitive win rates or commercial performance** in regulator-facing communications.

13. **We will NOT claim the system works for "any therapeutic area" without specifying** exactly which have been validated and which are untested.

14. **We will NOT trivialise the difficulty of regulatory work.** Phrases such as "Don't spend months looking for it," "so easy," or "in mere seconds" are permanently excluded from regulator-facing vocabulary. Regulatory work is difficult because the consequences are real. A tool that respects this difficulty earns the trust of the professionals who do it.

15. **We will NOT use the phrase "AI-Driven Benefit-Risk Analysis."** The accurate description is "AI-supported evidence structuring for benefit-risk assessment."

### Appendix B: Glossary

| Term | Definition |
|------|-----------|
| **Benefit-risk assessment (BRA)** | Systematic evaluation of the favourable and unfavourable effects of a medicine in relation to a specific indication and population. In the MHRA context, this is a human-led regulatory judgment, not a computational output. |
| **BNF (British National Formulary)** | UK reference for prescribing, dispensing, and administering medicines. |
| **BRAT (Benefit-Risk Action Team) framework** | Structured framework for organising and displaying the key benefits and risks of a medicine, developed by CIRS. |
| **CIOMS (Council for International Organizations of Medical Sciences)** | International organisation producing guidance on pharmacovigilance and benefit-risk assessment. CIOMS Working Group XII produced a framework for benefit-risk assessment. |
| **CPRD (Clinical Practice Research Datalink)** | UK real-world research service providing anonymised patient data from GP practices. Approximately 65 million patient records. Operated by MHRA. |
| **DSUR (Development Safety Update Report)** | Annual safety report for investigational medicinal products required under ICH E2F. |
| **Effectiveness** | Performance of a drug under real-world clinical conditions. MHRA works with effectiveness. Distinct from efficacy. |
| **Efficacy** | Performance of a drug under controlled, ideal conditions (clinical trials). |
| **EudraVigilance** | EMA's system for managing and analysing reports of suspected adverse reactions to medicines authorised in the EEA. |
| **FAERS (FDA Adverse Event Reporting System)** | US FDA database of adverse event reports and medication error reports. |
| **ICH E2C(R2)** | International Council for Harmonisation guideline on Periodic Benefit-Risk Evaluation Reports. |
| **IMMDS Review** | Independent Medicines and Medical Devices Safety Review ("First Do No Harm"), published July 2020, chaired by Baroness Cumberlege. Criticised Yellow Card system as "too complex and too diffuse to allow early signal detection." |
| **MAH (Marketing Authorisation Holder)** | Company or organisation holding the authorisation to market a medicine. |
| **MedDRA** | Medical Dictionary for Regulatory Activities -- international medical terminology for regulatory communication. |
| **NICE** | National Institute for Health and Care Excellence -- UK body providing guidance on use of health technologies. |
| **PBRER (Periodic Benefit-Risk Evaluation Report)** | The ICH E2C(R2) equivalent of PSUR. |
| **PRAC (Pharmacovigilance Risk Assessment Committee)** | EMA committee responsible for assessing and monitoring the safety of human medicines. |
| **PSUR (Periodic Safety Update Report)** | Periodic report providing comprehensive evaluation of the benefit-risk balance of a marketed medicine. |
| **RegulatoryConnect** | MHRA digital platform launched March 2024, cancelled November 2025. Intended as centrepiece of Data Strategy 2024-2027 but shut down because "the cost to complete the programme was considered too high for a solution which did not enable delivery of the aspirations of the agency." |
| **RMP (Risk Management Plan)** | Document describing pharmacovigilance activities and interventions to identify, characterise, prevent, or minimise risks. |
| **SafetyConnect / HALO** | MHRA's pharmacovigilance modernisation programme, partnered with Insife. HALO platform handles case management and operational reporting. Covers PV workflow but not evidence structuring for benefit-risk assessment. |
| **Signal** | Information from one or multiple sources suggesting a new potentially causal association, or new aspect of a known association, between a medicine and an adverse event. A signal is a hypothesis requiring evaluation, not a confirmed risk. |
| **SLM (Small Language Model)** | In ArcaScience's context, a task-specific ML model trained for a discrete extraction or classification function, distinct from large general-purpose language models (LLMs). |
| **SmPC (Summary of Product Characteristics)** | Regulatory document describing properties and approved conditions of use of a medicine. |
| **Yellow Card scheme** | UK system for collecting and monitoring information on suspected adverse reactions to medicines, vaccines, herbal products, and medical devices. Patient-level data; confidential. Median under-reporting rate: 94% (Hazell & Shakir 2006; PLOS Medicine 2025). |

### Appendix C: ArcaScience Platform Validation Summary

| Metric | Value | Source |
|--------|-------|--------|
| Proprietary AI models | 24 task-specific SLMs | Platform documentation |
| Data points processed | 100B+ | Platform documentation |
| Aggregate accuracy | 94% | arcascienceval.live |
| Aggregate precision | 91% | arcascienceval.live |
| Aggregate recall | 89% | arcascienceval.live |
| Aggregate F1 | 0.90 | arcascienceval.live |
| AE extraction precision | 92% (vs. 67% GPT-4) | AI in Medicine, 2025 |
| Early signal detection improvement | 3x | Journal of Pharmacoepidemiology, 2024 |
| NLP AE extraction F1 | 94% | BMC Medical Informatics, 2024 |
| PSUR generation time reduction | 60% | Therapeutic Innovation & Regulatory Science, 2023 |
| Peer-reviewed publications | 6 | Various journals, 2023-2025 |
| Certifications | GAMP 5, ISO 27001, SOC 2 Type II | Certification bodies |
| Regulatory compliance | FDA 21 CFR Part 11, GDPR, HIPAA, HDS | Compliance documentation |

**Enterprise case studies:**

| Client | Outcome | Context |
|--------|---------|---------|
| AstraZeneca | 68% reduction in BRA cycle time | Benefit-risk assessment workflow |
| Sanofi | 52% faster regulatory submissions | Regulatory submission preparation |
| Novartis | $12M annual savings across 300+ products | Full portfolio deployment |
| Roche | Platform deployment | Regulatory operations |
| ICON | Platform deployment | CRO regulatory services |
| Paris Brain Institute | Platform deployment | Academic neuroscience research |

### Appendix D: References

**MHRA strategic and operational sources:**

- MHRA Corporate Plan 2023-2026. https://www.gov.uk/government/publications/mhra-corporate-plan-2023-to-2026
- MHRA Business Plan 2025-2026. https://assets.publishing.service.gov.uk/media/685aa804e9509f1a908eb121/Business-plan-Final.pdf
- MHRA Data Strategy 2024-2027. https://www.gov.uk/government/publications/mhra-data-strategy-2024-2027/mhra-data-strategy-2024-2027
- MHRA People Strategy 2023-2026. https://www.gov.uk/government/publications/mhra-people-strategy-2023-to-2026/mhra-people-strategy-2023-to-2026
- MHRA Impact of AI on Regulation of Medical Products (April 2024). https://assets.publishing.service.gov.uk/media/662fce1e9e82181baa98a988/MHRA_Impact-of-AI-on-the-regulation-of-medical-products.pdf
- MHRA Annual Report 2024-25. https://www.gov.uk/government/news/mhras-2024-25-annual-report-and-accounts-and-impact-report-show-progress-on-safety-innovation-and-regulatory-excellence
- Lawrence Tallon CEO Announcement. https://www.gov.uk/government/news/lawrence-tallon-begins-role-as-new-mhra-ceo
- Hansard: MHRA Parliamentary Debate (January 2025). https://hansard.parliament.uk/commons/2025-01-16/debates/4BF8018B-9662-427B-A580-2EBB7770D164/MedicinesAndHealthcareProductsRegulatoryAgency

**Industry and performance analysis:**

- ABPI: Enhancing the role of UK medicine regulation (December 2024). https://www.abpi.org.uk
- Pharmaceutical Journal: MHRA Approvals Miss Targets (January 2024). https://pharmaceutical-journal.com/article/news/mhra-approvals-miss-targets-by-more-than-100-days-data-show
- PMC: International Comparison of Medicines Approvals (154 innovative medicines study). https://pmc.ncbi.nlm.nih.gov/articles/PMC12587917/
- Pharmaphorum: MHRA Staff Cuts (2023). https://pharmaphorum.com/news/mhra-cuts-could-affect-uk-regulatory-decisions-say-unions

**Yellow Card and under-reporting:**

- PLOS Medicine: Yellow Card Pharmacogenomics Study (2025). https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1004565
- IMMDS Review: "First Do No Harm" (July 2020). https://www.immdsreview.org.uk/Report.html
- Hazell L, Shakir SAW. Under-reporting of adverse drug reactions: a systematic review. Drug Safety. 2006;29(5):385-96.

**Technology and modernisation:**

- Insife: MHRA SafetyConnect Partnership. https://www.insife.com/articles-mhra
- HaloPV Platform. https://www.halopv.com/
- NSF: RegulatoryConnect Closure. https://www.nsf.org/life-science-regulatory-news/uk-mhra-to-close-their-regulatoryconnect-programme
- Ropes & Gray: MHRA Pilot RWE Dialogue Programme (January 2025). https://www.ropesgray.com/en/insights/viewpoints/102jtqu/mhra-launches-the-2025-pilot-real-world-evidence-dialogue-programme-implementin

**Regulatory public sources (candidate PoC):**

- MHRA Drug Safety Update: SGLT2 inhibitors and DKA risk (2016). https://www.gov.uk/drug-safety-update/sglt2-inhibitors-updated-advice-on-the-risk-of-diabetic-ketoacidosis
- MHRA Drug Safety Update: Fluoroquinolone antibiotics -- new restrictions (January 2024). https://www.gov.uk/drug-safety-update/fluoroquinolone-antibiotics-must-now-only-be-prescribed-when-other-commonly-recommended-antibiotics-are-inappropriate
- MHRA Public Assessment Report: Fluoroquinolone risk minimisation review. https://www.gov.uk/government/publications/review-of-risk-minimisation-for-disabling-and-potentially-long-lastingirreversible-side-effects-associated-with-fluoroquinolone-antibiotics
- EMA: SGLT2 inhibitors Article 20 referral. https://www.ema.europa.eu/en/medicines/human/referrals/sglt2-inhibitors
- EMA: PRAC Assessment Report -- SGLT2 inhibitors. https://www.ema.europa.eu/en/documents/referral/sglt2-inhibitors-article-20-procedure-assessment-report_en.pdf
- EMA: Quinolone/fluoroquinolone Article 31 referral. https://www.ema.europa.eu/en/medicines/human/referrals/quinolone-fluoroquinolone-containing-medicinal-products
- FDA: SGLT2 Drug Safety Communication (2015). https://www.fda.gov/Drugs/DrugSafety/ucm446852.htm
- Frontiers in Pharmacology: SGLT2 inhibitors and DKA systematic review (2023). https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2023.1145587/full
- NEJM: Risk of DKA after initiation of SGLT2 inhibitor (2017). https://www.nejm.org/doi/full/10.1056/NEJMc1701990

**ArcaScience peer-reviewed publications:**

- AE extraction accuracy (92% vs. 67% GPT-4). AI in Medicine, 2025.
- Early signal detection (3x improvement). Journal of Pharmacoepidemiology, 2024.
- NLP AE extraction (94% F1). BMC Medical Informatics and Decision Making, 2024.
- PSUR generation time (60% reduction). Therapeutic Innovation & Regulatory Science, 2023.

**ArcaScience internal documents used in preparation (not for external distribution):**

- MHRA Meeting transcript (January 2026)
- ArcaScience Deck 2026
- ArcaScience 2026 IT Roadmap
- ArcaScience i-Demo / BR-PREDICT project documentation
- ArcaScience OKR Execution Blueprint and Next-Quarter OKRs
- arcascience.ai (public website, reviewed February 2026)
- arcascienceval.live (public validation portal, reviewed February 2026)

**Regulatory framework references:**

- ICH E2C(R2): Periodic Benefit-Risk Evaluation Reports
- CIOMS Working Group XII: Benefit-Risk Balance for Marketed Drugs
- Bradford Hill AB. The environment and disease: association or causation? Proc R Soc Med. 1965;58(5):295-300.
