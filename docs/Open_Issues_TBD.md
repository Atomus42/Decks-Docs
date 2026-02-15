# DELIVERABLE D: Open Issues and TBD Register

**Prepared by:** Agent 7 (Editor / Deck Strategist)
**Date:** 2026-02-15
**Classification:** INTERNAL -- ArcaScience Leadership Only
**Purpose:** Exhaustive register of every unresolved question, gap, and preparation item identified across all MHRA collaboration workstreams. This document tells leadership exactly what is not ready and what must be done before we re-engage.

---

## Quality Acceptance Checklist

Before any material is sent to MHRA or any meeting is scheduled, every item below must be checked off by the responsible owner:

- [ ] Every MHRA question has a direct answer + a proposed demo artifact
- [ ] Confidentiality concerns addressed with a concrete operating model
- [ ] "Bespoke model per issue" objection neutralized (explain task-models + configuration vs retraining)
- [ ] Clear separation between automation and assessor judgment
- [ ] Messaging toned down where needed (replace risky claims)
- [ ] PoC is feasible without sensitive MHRA internal data
- [ ] Slide outline matches base doc and is boardroom-clean

---

## How to Read This Document

Each item follows this structure:

| Field | Description |
|-------|-------------|
| **Question / Gap** | The specific issue or unanswered question |
| **Why MHRA Would Care** | Why this matters to regulators -- tied to specific meeting concerns where possible |
| **Documentation Status** | What we know, what is missing, and where the information lives (or does not) |
| **Owner** | ArcaScience Engineering, ArcaScience Legal, ArcaScience Commercial, MHRA, or Joint |
| **Priority** | **Before next meeting** / **Before PoC** / **Phase 2+** |

---

## 1. Model Architecture and Training

### 1.1 Specific architecture of each SLM is undocumented

**Question / Gap:** What is the specific architecture of each of the 24 small language models? Transformer variant? Parameter count? Training methodology (fine-tuned from what base)? What makes them "small"?

**Why MHRA Would Care:** Allison asked to see "under the hood" (38:54). Regulators need to understand model complexity to assess reliability claims. "24 small AI models" was met with disbelief by Allison (12:20): "How can you do that then?" Without architectural detail, the claim sounds implausible.

**Documentation Status:** Materials state "small language models" and "24" but do not specify architectures, parameter counts, or base models. The IT Roadmap references GPU compute and FastAPI model serving but no model cards.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 1.2 Training data provenance and curation methodology

**Question / Gap:** What are the exact training datasets for each model? How were they curated? What are the selection criteria? What potential biases exist in the training data?

**Why MHRA Would Care:** Data provenance for training is a regulatory concern. Steph (04:35) asked: "how are you ensuring the quality of those data sources?" This extends to the data used to train the models themselves, not just the data the models process.

**Documentation Status:** Known: 10,000+ documents, all therapeutic areas, all clinical phases (1-4). Unknown: exact dataset composition, selection criteria, geographic and temporal distribution, potential biases, whether post-authorization data types (observational studies, meta-analyses) are adequately represented.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 1.3 Model versioning and change control

**Question / Gap:** How is model versioning managed? What happens when a model is updated? Is there a formal change control process when a model is retrained or updated?

**Why MHRA Would Care:** Regulatory submissions need reproducibility. If the same query run on the same data produces different results after a model update, regulatory trust collapses. GxP compliance requires documented change control.

**Documentation Status:** No documented model versioning or change control process found in any reviewed materials (IT Roadmap, OKR documents, i-Demo).

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 1.4 How the system handles conflicting evidence across sources

**Question / Gap:** A drug may show different safety profiles in different studies. How does the system handle contradictions? Does it surface both sides? Does it attempt to reconcile? Does it flag the conflict?

**Why MHRA Would Care:** Post-authorization evidence is inherently contradictory. Allison described scenarios where "you're trying to understand causality of that event across a lot of different data sources" (35:04). If the system silently resolves contradictions, it biases the assessor.

**Documentation Status:** The system normalizes and links entities, but the handling of contradictions between sources is not documented. OKR Initiative 3 references "disagreement flags" as planned, not operational.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC

---

### 1.5 Ad-hoc query capability without pipeline configuration

**Question / Gap:** Can the system answer an ad hoc post-authorization question TODAY without new model development or pipeline configuration? Allison asked directly (25:44): "Could it do it today without, or would you need to build a model for it?"

**Why MHRA Would Care:** This is the litmus test. If the answer is "we need to set up a pipeline first," it confirms Allison's fear that the tool is not operationally viable for MHRA's 80 concurrent safety issues.

**Documentation Status:** The architecture documentation describes "statement of work" and "pipeline configuration" per engagement. It is unclear how much configuration is needed for a new safety question and how long that takes. The claim that "no retraining is needed" addresses model training but not pipeline setup time.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 1.6 Handling of observational studies and meta-analyses (not just case reports)

**Question / Gap:** ArcaScience demonstrated case report extraction in the meeting. Allison explicitly distinguished this from what she needs (47:22): "I'm not talking about case reports. I'm talking about big observational studies or meta-analyses." How do the models handle aggregate-level, complex study designs?

**Why MHRA Would Care:** Observational studies and meta-analyses are the primary evidence base for post-authorization safety assessment. If the models only handle case reports and clinical trials well, they miss the most important evidence types for MHRA.

**Documentation Status:** The pipeline documentation references document classification and section identification that should handle different study types. But no specific validation or performance data for observational study extraction or meta-analysis extraction has been documented. The meeting exchange on this topic (44:01-50:00) ended with Allison unconvinced.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting (must be demonstrated in next meeting's live demo)

---

## 2. Validation and Performance

### 2.1 Per-model F1 scores not published

**Question / Gap:** What are the current, measured F1 scores for each of the 24 models individually? The OKR targets >= 85% F1 for Risk/Safety and Efficacy endpoints, but actual measured values are not in any reviewed material.

**Why MHRA Would Care:** Allison asked about validation (13:07) and demanded to see "under the hood" (38:54). Targets are aspirations; MHRA needs measured performance. Without per-model metrics, there is no basis for trusting the chain.

**Documentation Status:** Targets documented (>= 85% F1). Example error categories described in transcript (10% missed, 5% miscategorized). Actual current performance values per model are not published in any reviewed material.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 2.2 Error propagation across chained steps

**Question / Gap:** How does error propagate across the 24 chained steps? If Step 3 has a 5% error rate, what is the cumulative error at Step 6? Is there a formal error propagation analysis?

**Why MHRA Would Care:** Allison asked this directly (13:07): "When you've got such complex models that they're happening in series, how do you validate them? How do you identify where that error might have happened?" This is a fundamental ML systems validation question.

**Documentation Status:** No formal error propagation analysis documented. The architecture allows per-step error localization (each step produces inspectable output), but cumulative error across the chain has not been quantified. No documentation of whether the system automatically flags cases where upstream errors may have affected downstream outputs. No methodology for measuring inter-step error correlation.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 2.3 Inter-annotator agreement for clinician test sets

**Question / Gap:** Two clinicians annotate test sets for validation. How were they selected? What is the inter-annotator agreement rate? What happens when they disagree?

**Why MHRA Would Care:** Annotation quality directly affects validation credibility. If two annotators have low agreement, the "gold standard" against which models are measured is unreliable. Regulators understand this.

**Documentation Status:** The process mentions two clinicians and "complete annotation guidelines" but does not specify selection criteria, inter-annotator agreement metrics, or disagreement resolution procedures.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 2.4 Performance variation across therapeutic areas and document types

**Question / Gap:** Are there therapeutic areas or document types where model performance is significantly lower? What are the failure modes?

**Why MHRA Would Care:** MHRA covers 600+ drugs across all therapeutic areas and hundreds of thousands of devices. Regulators need to know failure modes, not just averages. If the system performs well on oncology but poorly on psychiatry (relevant to the antidepressant example Allison raised), that is material information.

**Documentation Status:** Training data described as spanning "all therapeutic areas and all phases" but no per-area performance breakdown exists in reviewed materials.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC

---

### 2.5 False positive vs. false negative rate for safety signal extraction

**Question / Gap:** What is the precision/recall breakdown for safety entity extraction specifically? In pharmacovigilance, false negatives (missed safety signals) are more dangerous than false positives (spurious signals).

**Why MHRA Would Care:** F1 is the documented target metric, but F1 averages precision and recall equally. MHRA needs to know the false negative rate specifically. Missing a safety signal is a public health risk; surfacing a spurious one costs time but not lives.

**Documentation Status:** F1 is documented as the target metric. The precision/recall breakdown (which reveals the false negative rate) is not published in reviewed materials. The "100% concordance" claim from market validation exercises is not equivalent to a measured false negative rate on unseen data.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 2.6 Independent third-party validation

**Question / Gap:** Has the system undergone any independent third-party audit or validation? All documented validation is internal (clinician-annotated test sets) or client-performed (blind comparison with client's own BRA).

**Why MHRA Would Care:** Regulators distinguish self-validation from independent verification. A system that has only been validated by its own builders and paying clients has a conflict-of-interest problem.

**Documentation Status:** No independent third-party audit or validation documented. The i-Demo project (BR-PREDICT) may involve academic partners, but this is a future R&D program, not a current validation.

**Owner:** ArcaScience Engineering / ArcaScience Commercial (to commission if needed)

**Priority:** Before PoC

---

### 2.7 Study quality assessment capability gap

**Question / Gap:** The system extracts data from studies but does not assess study quality. Allison identified this as the fundamental gap (50:00): "That's extracting information into a structured form for you. It doesn't tell you about the quality of that study. Still."

**Why MHRA Would Care:** Data extraction without quality assessment is insufficient for regulatory use. MHRA assessors evaluate methodology, confidence intervals, population representativeness, heterogeneity, and study validity (44:01). If the system only extracts what a study says but not whether it is reliable, it does not meaningfully assist the assessor's core work.

**Documentation Status:** The system explicitly does NOT judge study quality (documented as a design choice). It extracts quality-relevant elements (sample size, duration, design) that help assessors make their own judgment. The gap is that no quality indicators, risk-of-bias flags, or study quality heuristics are surfaced alongside the extraction. OKR documents mention planned features (confidence scores, disagreement flags) but these are not operational.

**Owner:** ArcaScience Engineering (feature development) / ArcaScience Commercial (positioning decision)

**Priority:** Before next meeting (at minimum, must be addressed in positioning; feature development may be Before PoC)

---

## 3. Regulatory and Compliance

### 3.1 Quality management system certification

**Question / Gap:** Is the system developed under any quality management system (e.g., ISO 13485, IEC 62304, GAMP 5)?

**Why MHRA Would Care:** Software used in regulatory decision-making may need formal quality system compliance. MHRA will ask whether the development process is certified, not just whether the output looks correct.

**Documentation Status:** SonarQube quality gates and >= 80% code coverage are documented. No formal QMS, IEC 62304, or GAMP 5 compliance is referenced in any reviewed material.

**Owner:** ArcaScience Engineering / ArcaScience Legal

**Priority:** Before PoC

---

### 3.2 Formal Software Development Life Cycle (SDLC) documentation

**Question / Gap:** Is there a formal SDLC document? What development methodology is followed? How are requirements traced to testing?

**Why MHRA Would Care:** Standard regulatory expectation for software used in assessment. MHRA is itself a regulator and will apply regulatory thinking to any tool it considers adopting.

**Documentation Status:** SonarQube quality gates, code coverage targets, and weekly "Fixing" sessions are documented. No formal SDLC document or requirements traceability matrix is referenced.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC

---

### 3.3 Verification of claimed certifications

**Question / Gap:** ISO 27001, GDPR, FDA 21 CFR Part 11, HIPAA, and HDS (Hebergeur de Donnees de Sante) are claimed on the website. Are these independently verified? Can certificates and audit reports be provided?

**Why MHRA Would Care:** Claims on a website are not evidence of compliance. MHRA procurement and InfoSec will request copies of certificates and audit reports. If these cannot be produced, the claims become a credibility liability.

**Documentation Status:** All certifications sourced from ArcaScience's own marketing materials (website, deck). Independent audit reports or certification documents have not been reviewed. It is unknown whether these are current, self-declared, or independently audited.

**Owner:** ArcaScience Legal / ArcaScience Commercial

**Priority:** Before next meeting (at minimum, internal verification; certificates ready to share Before PoC)

---

## 4. Uncertainty and Confidence

### 4.1 Confidence scoring per insight is planned, not operational

**Question / Gap:** Sharinto asked specifically (18:42): "Does it come up with levels of uncertainty, or does it flag where there are issues?" The answer must be honest: confidence scoring is planned (OKR Initiative 3) but not yet operational.

**Why MHRA Would Care:** Presenting incomplete data as if it were complete would be a regulatory red flag. MHRA needs the system to surface what it does not know, not just what it finds. Without confidence scores, every extraction looks equally reliable, which is false.

**Documentation Status:** OKR Initiative 3 describes "confidence scores, disagreement flags, and missing evidence indicators" as planned. The i-Demo project describes "Quantification de l'Incertitude" via Bayesian/ensemble approaches. Neither is documented as currently operational. The Evidence Provenance Layer (OKR Initiative 2) is also planned, not delivered.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC (must be at least partially operational for the PoC deliverables, which promise confidence scoring)

---

### 4.2 Disagreement flags between sources not yet implemented

**Question / Gap:** When multiple sources provide conflicting data about the same drug-event association, does the system flag the disagreement?

**Why MHRA Would Care:** Post-authorization evidence is inherently contradictory. If the system silently picks one source over another, or averages conflicting data, the assessor is misled.

**Documentation Status:** Planned under OKR Initiative 3. Not operational. The PoC plan (scratch/06) lists "conflicts between sources flagged with both versions preserved" as a deliverable -- this implies the feature must be built before the PoC.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC

---

### 4.3 Missing evidence indicators not yet implemented

**Question / Gap:** Does the system identify when expected evidence is absent? For example, if no UK-specific incidence data exists for a drug-event combination, does the system flag this gap?

**Why MHRA Would Care:** Knowing what evidence is missing is as important as knowing what evidence exists. Allison described scenarios where data is simply not available (31:45): "I don't believe that data is available easily or with any confidence."

**Documentation Status:** Planned under OKR Initiative 3. The PoC plan includes a "Gap Analysis" deliverable (Section 4.6 of scratch/06) that explicitly requires this capability.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC

---

### 4.4 Handling of missing data and incomplete documents

**Question / Gap:** How does the system handle incomplete input documents? What happens when a study report is truncated, a table is unreadable, or key sections are missing?

**Why MHRA Would Care:** Sharinto reinforced this (18:30): "the information is going to be variable. Some forms of information may not necessarily be complete." Post-authorization data is routinely incomplete. The system must not produce confident-looking output from garbage input.

**Documentation Status:** The meeting discussed data quality management conceptually, but no formal methodology for handling missing data, incomplete documents, or unreadable content is documented.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC

---

## 5. Post-Marketing Specific

### 5.1 ICSR processing capability at scale

**Question / Gap:** Can the system process individual case safety reports (ICSRs) at scale? FAERS is mentioned as a data source, but the system's ability to ingest and structure thousands of spontaneous reports (the format Yellow Card data comes in) is not explicitly documented.

**Why MHRA Would Care:** ICSR processing is core to MHRA's post-authorization work. If the system can handle FAERS (US equivalent), it should be able to handle Yellow Card data structurally -- but this has not been demonstrated or documented.

**Documentation Status:** FAERS is listed as a data source. Yellow Card data was discussed as too confidential to share. The system's specific capability with ICSR-format data at scale (thousands of reports per drug) is not documented.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC (at least demonstrate FAERS ICSR processing)

---

### 5.2 Causality assessment methodology

**Question / Gap:** How does the system handle causality assessment? Allison specifically asked about understanding "causality of that event across a lot of different data sources" (35:04). This is fundamentally different from association detection.

**Why MHRA Would Care:** Causality determination is the core analytical challenge of post-authorization pharmacovigilance. The system extracts associations (drug X linked to event Y) but causality assessment methodology (Bradford Hill criteria, WHO-UMC system, Naranjo algorithm) is not documented.

**Documentation Status:** The system extracts temporal relationships, dose information, and co-occurrence patterns. No documented framework for supporting causality reasoning. The "Under the Hood" document (scratch/03) explicitly lists causality determination under "What the system does NOT do." This is honest, but the positioning must be carefully managed -- MHRA needs the system to at least organize the evidence that supports causality reasoning, even if the judgment itself is human.

**Owner:** ArcaScience Engineering (feature positioning) / ArcaScience Commercial (messaging)

**Priority:** Before next meeting (positioning); Before PoC (demonstrate evidence organization that supports causality reasoning)

---

### 5.3 CPRD-scale structured database handling

**Question / Gap:** Can the system handle real-world databases with billions of records? Allison mentioned "30 million patient records over 30 years" (42:42). The system is documented to handle semantic/textual data. Its capacity for structured epidemiological databases at that scale is not documented.

**Why MHRA Would Care:** CPRD is one of MHRA's most important evidence sources. Even if CPRD data cannot be shared now, MHRA needs to know the system could eventually process it in an on-premises deployment.

**Documentation Status:** The system's documented data sources are primarily text-based (PubMed, literature, regulatory documents). Processing structured tabular databases at CPRD scale (billions of data points) is architecturally different from NLP on documents. No performance benchmarks for structured database processing exist. The CPRD connector has not been built, the data schema mapping is undefined, and performance at scale is untested. CPRD has its own governance framework; third-party algorithm execution may need separate approval from CPRD itself.

**Owner:** ArcaScience Engineering

**Priority:** Phase 2+ (explicitly defer; not needed for public-domain PoC)

---

### 5.4 Efficacy vs. effectiveness distinction in the platform

**Question / Gap:** Does the platform operationalize the distinction between efficacy (clinical trial performance) and effectiveness (real-world performance)? Allison drew a hard line (26:31): "We don't do efficacy -- we do effectiveness."

**Why MHRA Would Care:** If the platform presents clinical trial efficacy data as if it represents real-world effectiveness, it misleads the assessor. UK-specific prescribing patterns, comorbidities, and population demographics affect effectiveness in ways that trial data does not capture.

**Documentation Status:** The platform extracts efficacy endpoints from clinical trials. No documented mechanism for flagging efficacy data as distinct from effectiveness data, or for integrating real-world effectiveness evidence separately.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC

---

### 5.5 UK-specific prescribing context and line-of-therapy positioning

**Question / Gap:** Can the system contextualize benefit-risk by UK-specific prescribing patterns, line of therapy, and available alternatives? Allison (26:59, 27:25) made clear that global data is insufficient -- UK-specific treatment pathways materially change the benefit-risk calculus.

**Why MHRA Would Care:** A drug used third-line with no alternative has a fundamentally different benefit-risk profile than the same drug used first-line with alternatives. The system must support this contextual analysis or it produces misleading output for UK regulatory purposes.

**Documentation Status:** No documented integration of UK-specific prescribing data (NICE guidelines, BNF, NHS prescribing data). The system processes whatever sources are ingested, but UK contextualization is not a built-in feature.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC (at least demonstrate awareness; full integration Phase 2+)

---

## 6. Data Governance and UK Compliance

### 6.1 Cyber Essentials Plus certification

**Question / Gap:** Does ArcaScience hold Cyber Essentials Plus certification? This is the UK government baseline cybersecurity certification, typically required for suppliers handling sensitive data.

**Why MHRA Would Care:** UK government procurement typically requires Cyber Essentials Plus for any supplier handling sensitive information. Without it, MHRA procurement cannot proceed to any formal vendor relationship.

**Documentation Status:** Not documented in any reviewed material. Not mentioned on the website or in the IT Roadmap.

**Owner:** ArcaScience Engineering / ArcaScience Legal

**Priority:** Before PoC (if any formal agreement is needed); Phase 2+ (if the PoC proceeds without formal vendor status)

---

### 6.2 NHS Data Security and Protection Toolkit (DSPT)

**Question / Gap:** Has ArcaScience completed the NHS DSPT? This is the standard for organizations processing NHS or health data in the UK.

**Why MHRA Would Care:** Processing any UK health data requires DSPT compliance. Even for the PoC, MHRA may require evidence that ArcaScience meets basic UK health data standards.

**Documentation Status:** Not documented in any reviewed material.

**Owner:** ArcaScience Legal / ArcaScience Engineering

**Priority:** Phase 2+ (not required for public-domain-only PoC, but should begin investigation now)

---

### 6.3 UK GDPR compliance (post-Brexit specific provisions)

**Question / Gap:** ArcaScience references EU GDPR compliance. Does this extend to UK GDPR under the Data Protection Act 2018? The UK has its own implementation with specific provisions.

**Why MHRA Would Care:** MHRA operates under UK GDPR, not EU GDPR. While largely overlapping, there are specific UK provisions (ICO oversight, UK adequacy decisions, UK-specific lawful bases) that must be addressed.

**Documentation Status:** EU GDPR claimed on website. UK-specific provisions not addressed in any reviewed material.

**Owner:** ArcaScience Legal

**Priority:** Before PoC

---

### 6.4 Data residency -- UK-based data centers

**Question / Gap:** ArcaScience uses AWS. Which region? Does data remain in UK-based data centers? Can UK data residency be guaranteed?

**Why MHRA Would Care:** UK government data processing may require data to remain within UK borders. AWS eu-west-2 (London) would satisfy this, but the current configuration is not documented.

**Documentation Status:** AWS is documented as the cloud provider (migrated from Azure in 2025). Specific region configuration is not documented.

**Owner:** ArcaScience Engineering / ArcaScience DevOps

**Priority:** Before PoC (confirm and document current region; configure UK residency if not already in place)

---

### 6.5 Air-gapped / fully isolated deployment capability

**Question / Gap:** Can ArcaScience models operate fully air-gapped (no outbound connectivity) within MHRA infrastructure? This would be required for any future Tier 3 data integration (Yellow Card, CPRD).

**Why MHRA Would Care:** Yellow Card and CPRD data cannot leave MHRA systems. An on-premises deployment that phones home to ArcaScience servers is not acceptable.

**Documentation Status:** On-premises deployment is described as "planned" in the OKR Execution Blueprint (Weeks 5-6 readiness assessment) and listed as a Tier 3 pricing feature. The 100% Kubernetes architecture is in principle portable. However: (a) whether all 24 SLMs can run on-premises is unconfirmed; (b) GPU hardware requirements for on-prem are unspecified; (c) whether the system can operate without any outbound connectivity is unconfirmed; (d) containerization and deployment packaging for MHRA's specific infrastructure is undefined.

**Owner:** ArcaScience Engineering

**Priority:** Phase 2+ (not needed for public-domain PoC, but must be scoped before any proposal involving MHRA data)

---

### 6.6 Crown Commercial Service (CCS) framework / G-Cloud listing

**Question / Gap:** Is ArcaScience listed on any UK government procurement framework (CCS, G-Cloud, Digital Outcomes)?

**Why MHRA Would Care:** UK government procurement of technology services typically routes through approved frameworks. Without listing, procurement becomes more complex and time-consuming.

**Documentation Status:** Not documented. ArcaScience is a French company; UK government framework listing may not have been considered.

**Owner:** ArcaScience Commercial / ArcaScience Legal

**Priority:** Phase 2+ (not required for unfunded PoC; critical for any paid engagement)

---

### 6.7 Data Protection Impact Assessment (DPIA)

**Question / Gap:** A DPIA is required for processing that is likely to result in high risk to individuals. Any future processing involving UK health data would trigger this requirement.

**Why MHRA Would Care:** Legal requirement under UK GDPR. Must be conducted jointly before any data processing begins.

**Documentation Status:** Not initiated. Would need to be conducted jointly by MHRA and ArcaScience.

**Owner:** Joint (MHRA + ArcaScience Legal)

**Priority:** Phase 2+ (not required for public-domain-only PoC)

---

### 6.8 Supply chain security assurance (NCSC guidance)

**Question / Gap:** Does ArcaScience meet UK National Cyber Security Centre (NCSC) supply chain security guidance?

**Why MHRA Would Care:** UK government bodies are expected to assess supply chain security for technology vendors. NCSC provides specific guidance that MHRA InfoSec will apply.

**Documentation Status:** Not addressed in any reviewed material.

**Owner:** ArcaScience Engineering / ArcaScience Legal

**Priority:** Phase 2+

---

### 6.9 Keycloak integration with MHRA identity infrastructure

**Question / Gap:** ArcaScience uses Keycloak for authentication (OAuth 2.0, OpenID Connect). Can this integrate with MHRA's existing identity and access management infrastructure?

**Why MHRA Would Care:** Any on-premises or integrated deployment would need to authenticate MHRA users through MHRA's own identity provider. Keycloak supports federation, but specific compatibility with MHRA's systems has not been assessed.

**Documentation Status:** Keycloak documented as the authentication system. Integration with external identity providers is architecturally supported but not tested with MHRA or any UK government identity infrastructure.

**Owner:** ArcaScience Engineering

**Priority:** Phase 2+

---

### 6.10 Memorandum of Understanding (MoU) or collaboration agreement

**Question / Gap:** What legal framework governs the PoC? Even a zero-data, zero-cost PoC may require a lightweight collaboration letter or MoU to protect both parties.

**Why MHRA Would Care:** MHRA internal governance may prevent even a public-data collaboration without some formal agreement covering: scope, IP, liability, use of outputs, confidentiality of MHRA's feedback, and restrictions on ArcaScience referencing the engagement publicly.

**Documentation Status:** The PoC plan (scratch/06) proposes a "lightweight collaboration letter" but no draft exists.

**Owner:** Joint (ArcaScience Legal + MHRA Legal)

**Priority:** Before PoC

---

## 7. Knowledge Graph and Future Capabilities

### 7.1 Current status of the knowledge graph

**Question / Gap:** The i-Demo materials target >100K entities and >1M relations. What is the current state of the knowledge graph? How populated is it? What therapeutic areas are covered?

**Why MHRA Would Care:** The knowledge graph is central to the "beyond literature search" value proposition (cross-source linking, mechanism-of-action-based evidence surfacing). If it is aspirational rather than operational, the differentiation from ChatGPT weakens.

**Documentation Status:** Target documented in i-Demo materials. Current state of population is not specified. The Profiling Base is described as containing "100B+ data points" but the knowledge graph's entity and relation counts are not published.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting (must know what to claim honestly)

---

### 7.2 "World Model" (WP6 / BR-PREDICT) timeline and scope

**Question / Gap:** The i-Demo/BR-PREDICT project includes a multi-year R&D program (2026-2029) for a "World Model" integrating all prediction modules. What is current vs. aspirational? What capabilities exist now vs. on the roadmap?

**Why MHRA Would Care:** If ArcaScience presents roadmap features as current capabilities, MHRA will discover the gap during the PoC and trust will be destroyed. The line between "what we have" and "what we are building" must be crystal clear.

**Documentation Status:** WP6 is a documented multi-year R&D program. It is explicitly not part of the current operational platform. The boundary between operational features and BR-PREDICT research outputs needs to be clearly communicated.

**Owner:** ArcaScience Engineering / ArcaScience Commercial

**Priority:** Before next meeting

---

### 7.3 Uncertainty quantification via Bayesian/ensemble approaches

**Question / Gap:** The i-Demo project describes "Quantification de l'Incertitude" using Bayesian and ensemble approaches. Is any of this operational, or is it entirely a research objective?

**Why MHRA Would Care:** Sharinto (18:42) specifically asked about uncertainty levels and gap flagging. If the answer is "we plan to build this in our 2026-2029 research program," it answers the question honestly but reveals that the current platform lacks this critical capability.

**Documentation Status:** Described in i-Demo project documents as a research objective. Not documented as operational in the current platform.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting (must know what to claim honestly; must not present as operational)

---

### 7.4 Omics and imaging data integration

**Question / Gap:** The i-Demo project includes omics and imaging data integration in future work packages. These are explicitly excluded from current capabilities.

**Why MHRA Would Care:** Low immediate concern for MHRA's post-authorization text-based work. But if ArcaScience's marketing materials claim "full lifecycle" support, MHRA may ask about these capabilities and discover they do not exist.

**Documentation Status:** Explicitly excluded from current capabilities. Documented as future research objectives.

**Owner:** ArcaScience Commercial (messaging only)

**Priority:** Before next meeting (ensure marketing materials do not overclaim)

---

## 8. Messaging and Positioning

### 8.1 CRITICAL: Remove "currently under review by the MHRA" from Deck 2026

**Question / Gap:** The deck states ArcaScience is "currently under review by the MHRA." This is false and potentially trust-destroying. MHRA is not reviewing ArcaScience for endorsement. The engagement is an exploratory conversation.

**Why MHRA Would Care:** If Allison's team sees this claim, the engagement will likely terminate immediately. It misrepresents the nature of the relationship and implies MHRA endorsement that does not exist.

**Documentation Status:** Present in ArcaScience Deck 2026 (identified in scratch/05, item #16, rated HIGH risk).

**Owner:** ArcaScience Commercial (IMMEDIATE action required)

**Priority:** Before next meeting -- IMMEDIATE

---

### 8.2 CRITICAL: Remove all "in seconds" language

**Question / Gap:** "Fill your benefit risk in seconds," "18 months of work done in mere seconds," and variants appear across arcascience.ai, arcascienceval.live, and Deck 2026. Allison stated (11:58): "My antibodies are going through the roof just because it says fill your benefit risk in seconds."

**Why MHRA Would Care:** This language was the single most negatively received element of the entire meeting. It trivializes a process MHRA takes extremely seriously and suggests the system automates judgment, which is anathema to the regulatory mindset.

**Documentation Status:** Present on website and in deck. Replacement language provided in scratch/05 Section 3.1. Safer alternative: "The evidence consolidation phase -- gathering, structuring, and cross-referencing published literature and clinical data -- is reduced from weeks to hours, freeing assessor time for the interpretive and judgment work that only qualified experts can perform."

**Owner:** ArcaScience Commercial (IMMEDIATE action required)

**Priority:** Before next meeting -- IMMEDIATE

---

### 8.3 CRITICAL: Remove "100% regulatory acceptance rate" claim

**Question / Gap:** The claim that ArcaScience has "100% regulatory acceptance rate with FDA, EMA, PMDA" implies that regulatory agencies have endorsed or validated the platform. In reality, agencies accept submissions from sponsors -- they do not certify the tools sponsors used.

**Why MHRA Would Care:** MHRA will immediately recognize this as a misattribution of agency authority. It suggests using ArcaScience guarantees approval, which is false and could be seen as misleading. This is rated as "the single most dangerous claim for MHRA engagement" in the positioning audit (scratch/05, item #12).

**Documentation Status:** Present on arcascience.ai and arcascienceval.live. Replacement: "Outputs from the ArcaScience platform have been incorporated into regulatory submissions by [N] pharmaceutical clients to FDA, EMA, and PMDA. Regulatory acceptance reflects the quality of the sponsor's overall submission, not an endorsement of any individual tool."

**Owner:** ArcaScience Commercial (IMMEDIATE action required)

**Priority:** Before next meeting -- IMMEDIATE

---

### 8.4 Remove or reframe "9x more insights detected"

**Question / Gap:** "Insights" is subjective. "9x more" than what? "Detected" implies the system makes clinical determinations. This claim sounds arrogant and unverifiable to regulators.

**Why MHRA Would Care:** Allison (32:28): "You make it sound so easy, and it's so so hard." Volume claims without quality context are counterproductive. "Insights detected" sounds like the system replaces the assessor's judgment.

**Documentation Status:** Present on arcascience.ai. Replacement language provided in scratch/05 Section 3.2.

**Owner:** ArcaScience Commercial

**Priority:** Before next meeting

---

### 8.5 Remove or reframe "Reduce BRA Project Time by 80%"

**Question / Gap:** 80% reduction in "BRA project time" is both extreme and vague. Regulators will ask: 80% of what? Data gathering? Analysis? Committee deliberation?

**Why MHRA Would Care:** Without the baseline, methodology, sample size, and scope, this is a marketing statistic that damages credibility with a scientific audience.

**Documentation Status:** Present in Deck 2026. Replacement language provided in scratch/05 Section 3.1.

**Owner:** ArcaScience Commercial

**Priority:** Before next meeting

---

### 8.6 Reframe "AI-Driven Benefit-Risk Analysis" language

**Question / Gap:** "AI-Driven Benefit-Risk Analysis" implies the AI performs the analysis. For regulators, benefit-risk analysis is a human judgment activity. "Full Drug Lifecycle" is an overstatement given current capabilities.

**Why MHRA Would Care:** Allison explicitly challenged this framing throughout the meeting. The positioning must be "AI-supported evidence structuring for benefit-risk assessment," with the human assessor always as the subject.

**Documentation Status:** Present on arcascienceval.live and throughout marketing materials. Replacement language and messaging principles provided in scratch/05 Sections 3.4 and 4.

**Owner:** ArcaScience Commercial

**Priority:** Before next meeting

---

### 8.7 Remove expired IDC prediction

**Question / Gap:** "By 2025, 80% of pharma will have adopted AI benefit-risk-enabled solutions" (IDC quote). It is now 2026 and this prediction did not materialize. Using it undermines credibility.

**Why MHRA Would Care:** Regulators notice details. Citing an expired prediction signals that materials have not been updated and reduces trust in attention to accuracy.

**Documentation Status:** Present on arcascience.ai. Flagged in scratch/05, item #20.

**Owner:** ArcaScience Commercial

**Priority:** Before next meeting

---

### 8.8 Reframe "generates" language for regulatory documents

**Question / Gap:** Claims that the system "generates" PSURs, PBRERs, RMPs, etc. imply finished regulatory documents produced by AI. In reality, the system pre-populates templates that require expert review.

**Why MHRA Would Care:** Regulators who sign off on these documents will not accept that they were "generated" by a machine. The word "generates" implies a finished product, not a draft.

**Documentation Status:** Present on arcascience.ai. Replacement: "pre-populates structured templates" or "assembles draft evidence summaries for expert review and completion."

**Owner:** ArcaScience Commercial

**Priority:** Before next meeting

---

### 8.9 Establish internal claims review process for all MHRA communications

**Question / Gap:** There is no documented internal review process for ensuring that MHRA-facing communications comply with the messaging principles and "Claims We Will NOT Make" list (scratch/05, Section 2).

**Why MHRA Would Care:** If one ArcaScience team member makes a prohibited claim in a meeting or email, it undoes all preparation. Consistency requires process. The "Claims We Will NOT Make" list includes 15 specific prohibitions that every team member must know.

**Documentation Status:** The "Claims We Will NOT Make" list exists (scratch/05 Section 2) and messaging principles are defined (scratch/05 Section 4) but there is no documented process for enforcing compliance across personnel, checking slides before meetings, or reviewing emails before sending.

**Owner:** ArcaScience Commercial

**Priority:** Before next meeting

---

## 9. Collaboration and PoC

### 9.1 Working demo on candidate PoC issue must be prepared

**Question / Gap:** The PoC plan (scratch/06) proposes three candidate safety issues (SGLT2/DKA recommended as primary). A working demo on at least the primary candidate must be ready before the next meeting. The demo must show ingestion, classification, extraction, and traceability on representative sources (including at least 2 observational studies and 1 meta-analysis).

**Why MHRA Would Care:** Allison said (38:54): "I need to see under the hood." She wants a live demonstration, not another slide deck. If ArcaScience shows up to the next meeting with slides instead of a working system, the engagement ends.

**Documentation Status:** The PoC plan defines the scope, deliverables, and timeline. The demo itself has not been built. Pipeline configuration for SGLT2/DKA has not been initiated. Public-domain source URLs are documented in scratch/06 (MHRA Drug Safety Update, EMA PRAC assessment, FDA safety communications, literature).

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting

---

### 9.2 Beta platform must be independently navigable

**Question / Gap:** Allison stated (58:06): "We'll try and think through working through the beta version." MHRA plans to independently explore the beta to find a use case themselves. The beta must be compelling and navigable without ArcaScience hand-holding.

**Why MHRA Would Care:** If MHRA staff try the beta and cannot figure out how to use it, or encounter marketing-heavy landing pages with "in seconds" claims instead of functional tools, they will disengage. Steph confirmed she already looked at the "latest version" (03:44) and found it "interesting" with "utility" -- this positive impression must not be undermined by unresolved UX issues or misleading messaging on the beta platform itself.

**Documentation Status:** Beta access was previously provided to MHRA. Current state of beta UX, onboarding flow, and post-authorization-relevant content is unknown. The beta platform (arcascienceval.live) is one of the sites where risky claims appear.

**Owner:** ArcaScience Engineering / ArcaScience Commercial (UX and messaging)

**Priority:** Before next meeting

---

### 9.3 Collaboration letter / MoU draft needed

**Question / Gap:** Even a zero-data, zero-cost PoC may require a formal agreement. MHRA internal governance may prevent participation without one. No draft exists.

**Why MHRA Would Care:** MHRA is a UK government body. Internal approval processes may require documented terms before assessors can spend official time on an external evaluation. The agreement must cover: scope, no data exchange, no funding, no IP implications, evaluation purposes only, MHRA's full discretion to discontinue, and restrictions on ArcaScience referencing the engagement publicly.

**Documentation Status:** The PoC plan proposes a "lightweight collaboration letter" covering these terms. No draft has been prepared.

**Owner:** ArcaScience Legal (draft) / Joint (agreement)

**Priority:** Before PoC

---

### 9.4 MHRA's internal deliberation timeline is unknown

**Question / Gap:** Allison stated (57:51): "Let us take it away and think about it. We'll have an internal conversation. Come back to you." ArcaScience does not know MHRA's internal timeline or decision process.

**Why MHRA Would Care:** This is an MHRA-owned item. ArcaScience should not push for a meeting before MHRA is ready, but should prepare all materials so they are ready the moment MHRA re-engages.

**Documentation Status:** No timeline provided. The risk is bilateral: ArcaScience prepares for months while MHRA decides not to proceed, or MHRA re-engages before ArcaScience is ready.

**Owner:** MHRA (decision) / ArcaScience Commercial (relationship management, preparation)

**Priority:** Before next meeting (prepare everything; wait for MHRA to initiate)

---

### 9.5 MHRA assessor availability for PoC review

**Question / Gap:** The PoC plan requires approximately 3-4 hours of MHRA assessor time across 4 weeks (1 scoping meeting + document review + 1 review session). Which assessors will participate? Are they available?

**Why MHRA Would Care:** Assessors are busy (80 concurrent safety issues, 600+ drugs). Committing assessor time to an external evaluation is a resource allocation decision that MHRA leadership must approve.

**Documentation Status:** The PoC plan estimates time commitment but specific assessors have not been identified or committed.

**Owner:** MHRA

**Priority:** Before PoC (to be agreed during scoping meeting)

---

### 9.6 PoC data sourcing burden -- who does the work?

**Question / Gap:** Sharinto asked (40:08): "You're very much reliant on us to provide you with all of the sources." The PoC must make explicitly clear that ArcaScience does all data sourcing from public-domain sources. MHRA provides only the safety question and the evaluative judgment at the end.

**Why MHRA Would Care:** If MHRA has to do the data sourcing AND use the platform, the efficiency gain is zero. The value proposition must include data sourcing as ArcaScience's responsibility.

**Documentation Status:** The PoC plan (scratch/06) specifies "MHRA resource commitment: None during Phase 1" and "ArcaScience works independently." This must be communicated clearly and early.

**Owner:** ArcaScience Commercial (communication) / ArcaScience Engineering (execution)

**Priority:** Before next meeting

---

### 9.7 Differentiation from ChatGPT / Copilot must be demonstrated

**Question / Gap:** Allison (53:36): "It's beyond the literature search because I can get ChatGPT to do that." The PoC must demonstrate capabilities that go beyond what an assessor can achieve with general-purpose AI tools.

**Why MHRA Would Care:** If the output looks like a well-formatted ChatGPT response, MHRA has no reason to engage with ArcaScience. The differentiators must be concrete and demonstrable: structured extraction of critical appraisal elements, source-level traceability to page and paragraph, confidence scoring, gap analysis, cross-source reconciliation by mechanism of action, and normalized ontology mapping (not just free-text summaries).

**Documentation Status:** Differentiators are conceptually defined (scratch/06 Section 3.2: "'Beyond literature search' test"). They have not been demonstrated in a working product against the MHRA use case.

**Owner:** ArcaScience Engineering

**Priority:** Before next meeting (must be the centerpiece of the next demo)

---

### 9.8 PoC success criteria must be agreed jointly with MHRA

**Question / Gap:** The PoC plan defines quantitative and qualitative success metrics (scratch/06 Section 3). These have not been agreed with MHRA. If MHRA has different expectations, the PoC may succeed by ArcaScience's metrics but fail by MHRA's.

**Why MHRA Would Care:** MHRA's evaluation criteria may differ from ArcaScience's. Joint agreement on "what success looks like" before the PoC begins prevents misaligned expectations.

**Documentation Status:** Metrics defined in scratch/06 but not validated with MHRA. The PoC plan proposes agreeing metrics during Phase 0 scoping.

**Owner:** Joint (to be agreed during Phase 0 scoping)

**Priority:** Before PoC

---

### 9.9 On-premises licensing and support model undefined

**Question / Gap:** If the PoC succeeds and MHRA wants to proceed to a deployment involving internal data, what is the licensing model for on-premises deployment? Is there a separate pricing tier? What does ongoing support look like?

**Why MHRA Would Care:** MHRA stated there is no budget currently (54:47). But if the PoC succeeds, the next conversation will involve cost. ArcaScience needs a clear answer for "what would it cost to deploy this on our infrastructure?"

**Documentation Status:** Enterprise tier (Tier 3) pricing references "on-prem" as a feature. Specific pricing for a government/regulatory client is not documented. The commercial model for MHRA engagement (free PoC leading to paid license? strategic partnership? public sector pricing?) is undefined.

**Owner:** ArcaScience Commercial

**Priority:** Before PoC (have a framework ready, even if exact pricing is negotiable)

---

### 9.10 Confidence scoring must be at least partially built for PoC deliverables

**Question / Gap:** The PoC plan (scratch/06, Section 4.5) promises confidence scoring as a deliverable: "Each extracted element receives a confidence score based on source reliability, extraction certainty, and consistency." This feature is currently listed as planned, not operational (OKR Initiative 3).

**Why MHRA Would Care:** If the PoC promises confidence scoring and then delivers output without it, MHRA loses trust. Either build it before the PoC or explicitly scope it out of the PoC deliverables and explain the timeline.

**Documentation Status:** Promised in PoC deliverables (scratch/06 Section 4.5). Not yet operational per OKR documentation. This is a direct conflict between what has been planned for delivery and what has been built.

**Owner:** ArcaScience Engineering

**Priority:** Before PoC (build at least a basic version, or rescope the PoC deliverables)

---

## Summary Priority Matrix

### IMMEDIATE (Before Any External Communication)

| # | Item | Owner |
|---|------|-------|
| 8.1 | Remove "currently under review by the MHRA" from deck | ArcaScience Commercial |
| 8.2 | Remove all "in seconds" language from all materials | ArcaScience Commercial |
| 8.3 | Remove "100% regulatory acceptance rate" claim | ArcaScience Commercial |

### Before Next Meeting

| # | Item | Owner |
|---|------|-------|
| 1.1 | Document SLM architectures (model cards) | Engineering |
| 1.2 | Document training data provenance | Engineering |
| 1.3 | Document model versioning and change control | Engineering |
| 1.5 | Clarify ad-hoc query capability (no bespoke setup) | Engineering |
| 1.6 | Demonstrate observational study / meta-analysis handling | Engineering |
| 2.1 | Publish per-model F1 scores | Engineering |
| 2.2 | Produce error propagation analysis | Engineering |
| 2.3 | Document inter-annotator agreement | Engineering |
| 2.5 | Publish precision/recall breakdown for safety extraction | Engineering |
| 2.7 | Address study quality assessment gap (positioning at minimum) | Engineering / Commercial |
| 3.3 | Verify claimed certifications internally | Legal / Commercial |
| 5.2 | Position causality support honestly | Engineering / Commercial |
| 7.1 | Determine and document current knowledge graph status | Engineering |
| 7.2 | Clarify operational vs. roadmap boundary | Engineering / Commercial |
| 7.3 | Clarify uncertainty quantification status | Engineering |
| 8.4 | Reframe "9x more insights" claim | Commercial |
| 8.5 | Reframe "80% time reduction" claim | Commercial |
| 8.6 | Reframe "AI-Driven BRA" language | Commercial |
| 8.7 | Remove expired IDC prediction | Commercial |
| 8.8 | Reframe "generates" language | Commercial |
| 8.9 | Establish internal claims review process | Commercial |
| 9.1 | Build working demo on SGLT2/DKA (or selected PoC issue) | Engineering |
| 9.2 | Ensure beta platform is independently navigable | Engineering / Commercial |
| 9.4 | Prepare all materials; wait for MHRA to initiate | Commercial |
| 9.6 | Clarify that ArcaScience does all data sourcing for PoC | Commercial |
| 9.7 | Demonstrate differentiation from ChatGPT in live demo | Engineering |

### Before PoC

| # | Item | Owner |
|---|------|-------|
| 1.4 | Document handling of conflicting evidence | Engineering |
| 2.4 | Assess performance variation across therapeutic areas | Engineering |
| 2.6 | Consider independent third-party validation | Engineering / Commercial |
| 3.1 | Assess QMS certification needs | Engineering / Legal |
| 3.2 | Produce formal SDLC documentation | Engineering |
| 4.1 | Make confidence scoring at least partially operational | Engineering |
| 4.2 | Implement disagreement flags between sources | Engineering |
| 4.3 | Implement missing evidence indicators | Engineering |
| 4.4 | Document handling of incomplete / missing data | Engineering |
| 5.1 | Demonstrate ICSR processing (at least FAERS) | Engineering |
| 5.4 | Operationalize efficacy vs. effectiveness distinction | Engineering |
| 5.5 | Demonstrate UK-specific prescribing context awareness | Engineering |
| 6.1 | Assess Cyber Essentials Plus requirement | Legal / Engineering |
| 6.3 | Address UK GDPR compliance | Legal |
| 6.4 | Confirm and document AWS region / data residency | Engineering / DevOps |
| 6.10 | Draft collaboration letter / MoU | Legal (Joint) |
| 9.3 | Finalize collaboration agreement | Legal (Joint) |
| 9.5 | Agree MHRA assessor availability | MHRA |
| 9.8 | Agree PoC success criteria jointly | Joint |
| 9.9 | Define on-premises licensing and support model | Commercial |
| 9.10 | Build or scope out confidence scoring for PoC | Engineering |

### Phase 2+

| # | Item | Owner |
|---|------|-------|
| 5.3 | CPRD-scale database handling capability | Engineering |
| 6.2 | NHS DSPT completion | Legal / Engineering |
| 6.5 | Air-gapped deployment capability | Engineering |
| 6.6 | CCS / G-Cloud framework listing | Commercial / Legal |
| 6.7 | Joint DPIA | Joint |
| 6.8 | NCSC supply chain security assurance | Engineering / Legal |
| 6.9 | Keycloak / MHRA identity integration | Engineering |
| 7.4 | Omics / imaging (do not overclaim in messaging) | Commercial |

---

## Total Open Item Count

| Category | Count |
|----------|-------|
| Model Architecture and Training | 6 |
| Validation and Performance | 7 |
| Regulatory and Compliance | 3 |
| Uncertainty and Confidence | 4 |
| Post-Marketing Specific | 5 |
| Data Governance and UK Compliance | 10 |
| Knowledge Graph and Future Capabilities | 4 |
| Messaging and Positioning | 9 |
| Collaboration and PoC | 10 |
| **TOTAL** | **58** |

| Priority Level | Count |
|----------------|-------|
| IMMEDIATE | 3 |
| Before next meeting | 26 |
| Before PoC | 21 |
| Phase 2+ | 8 |

---

*This document is exhaustive by design. It is an internal preparation register, not a document for MHRA. Its purpose is to ensure ArcaScience leadership has full visibility into the preparation gap between where we are and where we need to be before re-engaging with MHRA. Items marked as gaps are not accusations of failure -- they are preparation tasks that must be completed for the engagement to succeed.*

*Compiled from: scratch/01_questions.json, scratch/01_quotes.md, scratch/02_mhra_workflow.md, scratch/03_under_the_hood.md, scratch/04_data_governance.md, scratch/05_positioning_findings.md, scratch/06_poc_plan.md*
