# Standard Operating Procedure — Sanofi Demo Instance Setup & Configuration

**Document ID:** SOP-SANOFI-DEMO-2026-001
**Version:** 1.0
**Date:** 2026-03-25
**Classification:** Confidential — Internal Use Only
**Owner:** ArcaScience Operations
**Applicable To:** All team members involved in Sanofi demo preparation (including Maria-Lola post-1code.dev training)

---

## Purpose

This SOP defines the step-by-step process for setting up, configuring, validating, and delivering five proposed demo instances of the ArcaScience Benefit-Risk Assessment (BRA) platform for Sanofi. It serves as both a **quality gate** (no demo opens to Sanofi without passing every checkpoint) and a **configuration guide** (any trained team member can execute it).

**Context:** On March 11, 2026, ArcaScience presented its Benefit-Risk Intelligence platform to Sanofi's cross-functional team (Claire Brulle-Wohlhueter, Brandon Rufino — Director of AI for Development, Andreas Hohlbaum, Ford Parker, Hervé Béjoint, Sapna Elzer, William Hurst, Karissa Adkins, Stéphanie Tcherny-Lessenot, Sylvain Nicolas). Brandon Rufino called the meeting "very productive and insightful" and requested additional understanding of platform capabilities, including publication links backing validated results. This SOP ensures each demo instance is properly configured before Sanofi access.

**RAISE Framework Alignment:** Every step in this SOP is designed to demonstrate compliance with Sanofi's RAISE (Responsible AI at Sanofi for Everyone) framework across all five pillars:
1. **Accountable to Outcomes** — Every output traceable to source data; no hallucination
2. **Fair & Ethical** — No bias in subpopulation analyses; transparent methodology
3. **Robust & Safe** — GAMP 5 Category 5 validation; F1 thresholds enforced
4. **Transparent & Explainable** — Full ALCOA+ audit trail; per-step intermediate outputs inspectable
5. **Eco-Responsible** — SLM-based architecture (24 task-specific models, not monolithic LLMs) with lower compute footprint

---

## Scope

Five proposed demo instances, presented to Sanofi for prioritization:

| # | Asset | Mechanism | Demo Type | Priority Signal |
|---|-------|-----------|-----------|-----------------|
| 1 | **Tolebrutinib** | BTK inhibitor | Post-CRL BRA Rebuild | High — active regulatory crisis |
| 2 | **Dupixent** (dupilumab) | Anti-IL-4Rα | Multi-Indication B/R Monitoring | High — operational urgency (COPD expansion) |
| 3 | **Amlitelimab** | Anti-OX40L mAb | Phase 3 Competitive B/R Positioning | Medium-High — Phase 3 data expected |
| 4 | **Rilzabrutinib** | BTK inhibitor | Cross-Indication Hematology B/R | Medium — concurrent submissions |
| 5 | **Duvakitug** | TL1A/IL-23 bispecific | Dual-Mechanism IBD B/R | Lighter demo |

---

## General Prerequisites (All Instances)

Before beginning any instance-specific configuration, complete the following:

### Step G1: Infrastructure Readiness

- [ ] Verify platform deployment environment is operational (FastAPI backend, NestJS BRA platform, ElasticSearch, DocumentDB, QDrant vector DB)
- [ ] Confirm Data Forge pipelines (Apache Airflow DAGs) are running without errors
- [ ] Verify S3 storage buckets (raw + enriched) have sufficient capacity for all five instances
- [ ] Confirm API layer (FastAPI + NestJS) response times are within benchmark (see Step V3)

### Step G2: Ontology Baseline Configuration

- [ ] Load MedDRA v27.0 (latest version) — restructured ArcaScience format
- [ ] Load SNOMED CT (latest international release)
- [ ] Load ChEBI ontology (latest release)
- [ ] Load Disease Ontology (latest release)
- [ ] Verify all ontology normalization models are pointing to the correct versions
- [ ] **Note for Sanofi:** If Sanofi uses a proprietary ontology extension or MedDRA customization, request mapping documentation before demo opening. Flag this to Carlo during Sanofi communication.

### Step G3: ALCOA+ Audit Trail Activation

- [ ] Confirm cryptographic hash chaining is active on all audit trail entries
- [ ] Verify immutable audit trail write operations are functioning (test: create entry, attempt modification, confirm rejection)
- [ ] Confirm per-step intermediate output logging is enabled for all 24 SLM pipeline modules
- [ ] Generate test audit report and verify: Attributable, Legible, Contemporaneous, Original, Accurate, Complete, Consistent, Enduring, Available

### Step G4: Role-Based Access Control Setup

- [ ] Create Sanofi reviewer role with read-only access to demo outputs
- [ ] Create Sanofi evaluator role with read + export permissions
- [ ] Create ArcaScience demo admin role with full configuration access
- [ ] Assign specific access credentials for each Sanofi stakeholder (up to 10 reviewers per the March 11 meeting attendees)
- [ ] Verify session logging captures all user actions for audit purposes
- [ ] If EU data residency is required: confirm demo instance runs on EU-hosted infrastructure; verify no data egress to non-EU regions

### Step G5: HS Baseline Reference Load

- [ ] Load the validated HS (Hidradenitis Suppurativa) BRA as the reference baseline — PROJECT-08B | PRJ-SEC-HS
- [ ] Confirm all HS extraction metrics are accessible for comparison:
  - Biomarker extraction: F1 = 90.05%, 92% coverage of top 30 biomarkers
  - Risk extraction: F1 = 88.1%, 96% data coverage
  - Benefit extraction: F1 = 92%, 97% data coverage
- [ ] This baseline serves as the "known good" against which all new demo instance outputs will be spot-checked

---

## DEMO INSTANCE 1: Tolebrutinib — Post-CRL BRA Rebuild

### Context

FDA issued a Complete Response Letter (CRL) in December 2025 for tolebrutinib due to unfavorable B/R profile. Severe DILI (drug-induced liver injury) risk including one fatal case and one liver transplant across ~2,700 patients. Sanofi needs evidence reframing for resubmission.

### 1.1 Pre-Configuration Checklist

#### Data Sources & Availability

| Source | Type | Availability | Action Required |
|--------|------|--------------|-----------------|
| Tolebrutinib Phase 3 publications (GEMINI 1, GEMINI 2, HERCULES) | Clinical trial publications | ✅ Public (PubMed, journal sites) | Ingest |
| FDA CRL documentation (December 2025) | Regulatory | ✅ Public (FDA.gov) | Ingest |
| FDA Briefing Documents (AADAC/ODAC if available) | Regulatory | ✅ Public (FDA.gov) | Ingest |
| DILI-related safety databases (LiverTox, FAERS) | Safety DB | ✅ Public | Configure FAERS query for tolebrutinib + BTK inhibitor class |
| MedDRA-coded AE reports from publications | Clinical safety | ✅ Extractable from publications | Extract via SLM pipeline |
| Sanofi internal clinical data | Proprietary | ⚠️ NOT AVAILABLE for demo — requires Sanofi data sharing agreement | **Use public data only; flag limitation to Sanofi** |
| BTK inhibitor class safety comparator data (ibrutinib, acalabrutinib, zanubrutinib, evobrutinib, fenebrutinib) | Published literature | ✅ Public | Ingest for comparative context |

**⚠️ DATA FLAG:** This demo will operate on publicly available data only. The CRL-specific clinical datasets are Sanofi proprietary. The demo will demonstrate the *methodology and workflow* for evidence reframing using public data, with the understanding that a PoC engagement would incorporate Sanofi's full dataset.

#### Ontology Configuration

- [ ] MedDRA v27.0: Activate SOCs relevant to hepatotoxicity — Hepatobiliary disorders, Investigations (liver function tests), General disorders (fatigue, malaise as DILI prodrome)
- [ ] ChEBI: Map tolebrutinib (ChEBI ID to be confirmed), BTK inhibitor class
- [ ] Configure DILI-specific MedDRA SMQ (Standardised MedDRA Query): "Drug-related hepatic disorders — comprehensive"
- [ ] Activate Hy's Law calculation template (ALT >3× ULN + bilirubin >2× ULN)

#### SLM Pipeline Modules to Activate

| Module | Activate | Rationale |
|--------|----------|-----------|
| Document type classifier | ✅ | Classify CRL, publications, safety reports |
| Section identification | ✅ | Route to safety/efficacy sections |
| Safety event extractor | ✅ | Primary — DILI signal extraction |
| Relation extraction | ✅ | Link DILI events to tolebrutinib, dose, timing |
| Patient information extraction | ✅ | Subpopulation analysis (age, sex, comorbidities) |
| Study design extraction | ✅ | Characterize trial designs for evidence weighting |
| Drug/dosage extraction | ✅ | Dose-response for DILI signal |
| Efficacy endpoint extraction | ✅ | Capture MS efficacy data for B/R balance |
| Ontology normalization | ✅ | MedDRA/ChEBI mapping |
| Knowledge graph linking | ✅ | Cross-source entity resolution |

**Modules NOT needed:** None — full pipeline required for comprehensive BRA rebuild.

#### Therapeutic Area Vertical

- [ ] No pre-existing vertical for neurology/MS — configure from scratch
- [ ] Reference HS vertical for pipeline configuration patterns

### 1.2 Data Ingestion & Harmonization

#### Step 1.2.1: Source Document Collection

1. Search PubMed for: `"tolebrutinib" AND ("multiple sclerosis" OR "DILI" OR "hepatotoxicity" OR "liver")`
2. Retrieve all Phase 2 and Phase 3 trial publications (GEMINI 1, GEMINI 2, HERCULES)
3. Download FDA CRL letter and any associated briefing documents from FDA.gov
4. Query FAERS for tolebrutinib adverse event reports (MedDRA PT: Drug-induced liver injury, Hepatotoxicity, Hepatic failure, Liver transplant, Alanine aminotransferase increased, Aspartate aminotransferase increased, Blood bilirubin increased)
5. Retrieve LiverTox entry for tolebrutinib (if available) and BTK inhibitor class
6. Collect BTK inhibitor comparator publications: ibrutinib hepatotoxicity, acalabrutinib hepatotoxicity, zanubrutinib hepatotoxicity safety profiles
7. Retrieve EMA assessment reports for approved BTK inhibitors (for comparative DILI rates)

#### Step 1.2.2: Ingestion

1. Upload all collected documents to S3 raw bucket under path: `sanofi-demo/tolebrutinib/raw/`
2. Trigger Data Forge ingestion DAG: `sanofi_tolebrutinib_ingest`
3. Verify document count post-ingestion matches expected count
4. Check ingestion log for parsing errors — resolve any PDF extraction failures

#### Step 1.2.3: Normalization Parameters

- MedDRA coding level: **Preferred Term (PT)** with roll-up to **High Level Term (HLT)** and **System Organ Class (SOC)**
- Apply Hy's Law composite endpoint mapping
- Harmonize DILI grading across sources (CTCAE grading vs. FDA DILI classification)
- Normalize dose units to mg/day
- Harmonize time-to-event data to days from treatment initiation

#### Step 1.2.4: Quality Thresholds

After extraction pipeline completes, verify:

| Extraction Type | Minimum F1 | Action if Below |
|-----------------|-----------|-----------------|
| Adverse event extraction | ≥ 92% | Re-run with expanded context window; manual review of misses |
| Biomarker extraction | ≥ 90% | Check liver enzyme biomarker coverage specifically |
| Risk extraction | ≥ 88% | Verify DILI-specific risk entities are captured |
| Benefit extraction | ≥ 92% | Verify MS efficacy endpoints (relapse rate, disability progression) |

**Measurement method:** Spot-check 20 randomly selected documents. Compare SLM extractions against manual clinician review. Calculate precision, recall, F1.

### 1.3 Platform Configuration

#### Output Types to Enable

| Output Type | Enable | Configuration Notes |
|-------------|--------|-------------------|
| Disease Analysis | ✅ | MS disease landscape with DILI risk overlay |
| Clinical Landscape | ✅ | BTK inhibitor competitive landscape |
| AE Report | ✅ | **Primary output** — DILI-focused structured AE report |
| BRA (Benefit-Risk Assessment) | ✅ | **Primary output** — Full tolebrutinib B/R with subpopulation stratification |
| BRA Summary | ✅ | Executive summary for regulatory resubmission framing |

#### Regulatory Alignment

- [ ] Configure eCTD Module 2.5 (Clinical Overview) section mapping for BRA outputs
- [ ] Align BRA structure to PBRER (Periodic Benefit-Risk Evaluation Report) Section 16 — Benefit-Risk Analysis
- [ ] Pre-load FDA CRL response template structure for output alignment

#### BRAT Framework Configuration

- [ ] Configure BRAT Value Tree:
  - **Benefits:** Relapse rate reduction, disability progression delay, MRI lesion reduction, patient-reported outcomes
  - **Risks:** DILI (fatal, liver transplant, Grade 3+, any grade), infections, other serious AEs
  - **Risk Context:** Dose-response, time-to-onset, risk factors (age, baseline liver function, concomitant hepatotoxins)
- [ ] Enable BRAT Steps 0-6: Configuration → Context → Outcomes Identification → Data Analysis → Customize → Weighting → Display
- [ ] Configure subpopulation stratification: age groups, sex, baseline ALT, concomitant medications

### 1.4 Demo Environment Setup

- [ ] Create isolated instance: `sanofi-demo-tolebrutinib`
- [ ] Apply role-based access per Step G4
- [ ] Verify data residency settings (EU if required)
- [ ] Run performance benchmark:
  - Full pipeline execution on ingested corpus: target < 15 minutes
  - Single document extraction: target < 30 seconds
  - BRA generation: target < 5 minutes
  - UI page load: target < 3 seconds

### 1.5 Validation & QA

- [ ] **Extraction accuracy spot-check:** Select 10 documents at random. For each, manually verify 5 extracted safety entities and 5 extracted benefit entities. Record precision/recall. All must meet F1 thresholds above.
- [ ] **Auditability check:** Select 5 statements from the generated BRA. For each, trace back through: BRA output → knowledge graph → normalized entity → extracted entity → source document + page/section. Every link must resolve. Zero orphaned claims.
- [ ] **Regulatory output alignment:** Verify BRA output section headers map to eCTD 2.5 structure. Export a sample PBRER Section 16 and confirm alignment.
- [ ] **Baseline comparison:** Compare extraction metrics (F1, precision, recall) against the HS baseline (Step G5). Tolebrutinib metrics should be within 5 percentage points of HS baseline for comparable extraction types. If not, investigate and document the gap.
- [ ] **End-to-end user access test:** Log in as a Sanofi reviewer. Navigate the full demo. Verify all outputs render correctly. Test export functionality. Confirm audit trail records the session.

### 1.6 Demo Walkthrough Script

**Suggested navigation path (20-25 minutes):**

1. **Open with context** (2 min): Show the Disease Analysis for MS — establish that the platform understands the therapeutic landscape
2. **DILI signal deep-dive** (5 min): Navigate to AE Report — show structured DILI extraction across all ingested sources. Highlight: temporal patterns, dose-response signal, Hy's Law cases identified
3. **Subpopulation analysis** (5 min): Show BRA with subpopulation stratification — demonstrate which patient segments have favorable vs. unfavorable B/R. This directly addresses the resubmission strategy
4. **Evidence reframing** (5 min): Show BRA Summary — demonstrate how the platform structures the evidence narrative for regulatory resubmission, mapping to eCTD 2.5
5. **Auditability demonstration** (3 min): Click through from a BRA claim → source document. Show the ALCOA+ audit trail. Emphasize: zero hallucination, every claim traceable
6. **Comparative context** (3 min): Show BTK inhibitor class comparison — DILI rates across ibrutinib, acalabrutinib, zanubrutinib to contextualize tolebrutinib's profile
7. **Q&A** (5 min)

**Key data points to highlight:**
- Number of sources ingested and structured
- DILI cases identified with severity grading
- Subpopulations identified with differential B/R profiles
- Time to generate full BRA vs. manual CRO process (reference HS: "18 months in 2 weeks")
- Auditability: every statement traced to source

**Anticipated Sanofi questions:**
- *"How does this compare to what a CRO would produce?"* → Reference HS: $100K vs. CRO $1.2M, 18 months → 2 weeks, 5 undocumented risks found
- *"Can you handle our internal clinical data?"* → Yes, in PoC engagement with data sharing agreement. Demo uses public data only. Client data stays on client infrastructure.
- *"Where are the publications backing your validated results?"* (Brandon's specific request) → Show F1 metrics with methodology, reference peer-reviewed validation papers
- *"How does this align with ARTEMIS?"* → Complementary: ARTEMIS processes AE cases, ArcaScience analyzes the resulting data into continuous B/R intelligence. We sit on top of ARTEMIS, not alongside it.

---

## DEMO INSTANCE 2: Dupixent (dupilumab) — Multi-Indication B/R Monitoring

### Context

Dupixent has 9 approved indications (atopic dermatitis, asthma, CRSwNP, EoE, prurigo nodularis, CSU, bullous pemphigoid, COPD, and others). The COPD expansion introduces ~300,000 US adults with fundamentally different comorbidity/polypharmacy profiles. Peak revenue target EUR 22B by 2030.

### 2.1 Pre-Configuration Checklist

#### Data Sources & Availability

| Source | Type | Availability | Action Required |
|--------|------|--------------|-----------------|
| Dupixent FDA label (all approved indications) | Regulatory | ✅ Public | Ingest current USPI |
| EMA SmPC (dupilumab) | Regulatory | ✅ Public | Ingest |
| Phase 3 publications per indication (LIBERTY AD, LIBERTY ASTHMA, SINUS, BOREAS, NOTUS) | Clinical trial | ✅ Public | Ingest — high volume (~200+ publications) |
| FAERS data for dupilumab | Safety DB | ✅ Public | Configure broad query across all indications |
| COPD-specific RWD publications | RWE | ✅ Public | Search for COPD comorbidity landscape papers |
| Published safety profiles per indication | Published literature | ✅ Public | Ingest |
| Sanofi internal PV data (ARTEMIS output) | Proprietary | ⚠️ NOT AVAILABLE | **Flag: demo shows methodology; PoC would integrate ARTEMIS data** |

#### Ontology Configuration

- [ ] MedDRA v27.0: Activate SOCs across all 9 indications — broad activation required
- [ ] COPD-specific MedDRA SMQs: Cardiac disorders, Ischaemic heart disease, Infections, Lower respiratory tract infections
- [ ] ChEBI: Map dupilumab
- [ ] Configure indication-specific baseline event rate profiles for: atopic dermatitis, asthma, CRSwNP, EoE, PN, CSU, BP, COPD
- [ ] **Sanofi-specific note:** If Sanofi has custom COPD comorbidity ontology mappings, request before PoC

#### SLM Pipeline Modules to Activate

All 24 modules — full pipeline required for multi-indication analysis.

#### Therapeutic Area Vertical

- [ ] Immunology/Dermatology: reference HS vertical configuration
- [ ] Respiratory (COPD): configure as new sub-vertical
- [ ] Ensure cross-indication query architecture supports simultaneous analysis across all 9 indications

### 2.2 Data Ingestion & Harmonization

#### Step 2.2.1: Source Document Collection

1. Retrieve Dupixent publications per indication — use PubMed structured search:
   - `"dupilumab" AND "atopic dermatitis"` (LIBERTY AD trials)
   - `"dupilumab" AND "asthma"` (LIBERTY ASTHMA trials)
   - `"dupilumab" AND "chronic rhinosinusitis"` (SINUS trials)
   - `"dupilumab" AND "eosinophilic esophagitis"`
   - `"dupilumab" AND "prurigo nodularis"`
   - `"dupilumab" AND "chronic spontaneous urticaria"`
   - `"dupilumab" AND "bullous pemphigoid"`
   - `"dupilumab" AND "COPD"` (BOREAS, NOTUS trials)
2. Download current FDA USPI and EMA SmPC
3. Query FAERS for dupilumab — all reported AEs, stratified by indication if reporter provides
4. Collect COPD comorbidity landscape publications (cardiovascular, renal, diabetes prevalence in COPD)
5. Retrieve published long-term safety data (LIBERTY AD CHRONOS, open-label extensions)

**Expected corpus size:** 200-400 documents

#### Step 2.2.2: Ingestion

1. Upload to `sanofi-demo/dupixent/raw/`
2. Trigger DAG: `sanofi_dupixent_ingest`
3. Verify count and check for errors
4. **Critical:** Ensure documents are tagged by indication at ingestion for downstream stratification

#### Step 2.2.3: Normalization Parameters

- MedDRA coding: PT with roll-up to HLT and SOC
- Indication tagging: Each document and extraction tagged to the relevant Dupixent indication
- Normalize patient demographics for cross-indication comparison (age groups, comorbidity prevalence)
- COPD-specific: Apply cardiovascular and renal comorbidity flags

#### Step 2.2.4: Quality Thresholds

Same F1 thresholds as Instance 1. Additional check:
- Cross-indication consistency: Verify the same AE term extracted from different indication sources maps to the same MedDRA PT. Flag any inconsistencies.

### 2.3 Platform Configuration

#### Output Types to Enable

| Output Type | Enable | Configuration Notes |
|-------------|--------|-------------------|
| Disease Analysis | ✅ | Per-indication disease landscape |
| Clinical Landscape | ✅ | Dupixent vs. competitors per indication |
| AE Report | ✅ | Cross-indication AE report with stratification |
| BRA | ✅ | **Primary output** — Multi-indication B/R with COPD-specific overlay |
| BRA Summary | ✅ | Per-indication executive B/R summary |

#### Regulatory Alignment

- [ ] Configure PBRER section alignment — Dupixent has an active PBRER cycle
- [ ] eCTD Module 2.5 mapping for each indication
- [ ] Configure aggregate safety data presentation aligned to ICH E2C(R2)

#### BRAT Framework Configuration

- [ ] Configure multi-indication Value Tree:
  - **Benefits per indication:** Indication-specific primary efficacy endpoints (EASI for AD, FEV1 for asthma/COPD, NPS for CRSwNP, etc.)
  - **Risks (cross-indication):** Injection site reactions, conjunctivitis, eosinophilia, infections, hypersensitivity
  - **COPD-specific risks:** Cardiovascular events (in comorbid population), lower respiratory infections, drug interactions with COPD polypharmacy
- [ ] Enable cross-indication comparison view
- [ ] Configure COPD population overlay highlighting differential risk profile vs. existing indications

### 2.4 Demo Environment Setup

- [ ] Create isolated instance: `sanofi-demo-dupixent`
- [ ] Apply access controls per Step G4
- [ ] Performance benchmark: Allow extended pipeline time due to corpus size — target < 30 minutes for full pipeline
- [ ] Verify cross-indication query performance (filtering by indication should return < 5 seconds)

### 2.5 Validation & QA

- [ ] Extraction accuracy spot-check: 20 documents (at least 2 per indication where available)
- [ ] Auditability check: 5 cross-indication BRA claims traced to source
- [ ] **Cross-indication consistency check:** Select 3 AEs that appear across multiple indications. Verify the platform correctly aggregates evidence from all relevant indications and flags any inconsistencies in reported rates
- [ ] Regulatory output alignment: Verify PBRER Section 16 mapping
- [ ] Baseline comparison against HS reference
- [ ] End-to-end user access test

### 2.6 Demo Walkthrough Script

**Suggested navigation path (25-30 minutes):**

1. **Portfolio overview** (3 min): Show the 9-indication landscape. Highlight the different patient populations and how B/R profiles diverge.
2. **COPD deep-dive** (7 min): Navigate to the COPD-specific BRA. Show how the COPD comorbidity profile (cardiovascular, renal, polypharmacy) creates a different risk landscape vs. atopic dermatitis patients. This is the core demonstration — continuous B/R monitoring adapting to a new population.
3. **Cross-indication safety profiling** (5 min): Show AE Report across indications. Demonstrate how the platform identifies AEs that are enriched in one indication vs. another (e.g., conjunctivitis signal difference between AD and COPD).
4. **Consistency checking** (5 min): Show how the platform flags inconsistencies in safety reporting across indications. Demonstrate value for PBRER preparation.
5. **Auditability** (3 min): Trace a COPD-specific safety claim back to source.
6. **Q&A** (5 min)

**Anticipated Sanofi questions:**
- *"Can this replace our PBRER workflow?"* → Augments it — structures the evidence for PBRER Section 16; final medical judgment remains with Sanofi's safety team
- *"How would this integrate with ARTEMIS data?"* → In PoC: ARTEMIS-processed case data ingested as a source alongside literature. The platform harmonizes both.
- *"What about the EUR 22B peak sales risk?"* → Frame: the higher the commercial value, the higher the cost of a safety surprise in COPD. Continuous B/R monitoring is risk mitigation at scale.

---

## DEMO INSTANCE 3: Amlitelimab (anti-OX40L mAb) — Phase 3 Competitive B/R Positioning

### Context

Novel mechanism (anti-OX40L), Kaposi's sarcoma (KS) signal flagged in Phase 2 ATLANTIS study. Phase 3 COAST-1 data expected. Needs differentiation B/R framework vs. Dupixent.

### 3.1 Pre-Configuration Checklist

#### Data Sources & Availability

| Source | Type | Availability | Action Required |
|--------|------|--------------|-----------------|
| Amlitelimab Phase 2 ATLANTIS publications | Clinical trial | ✅ Public | Ingest |
| COAST-1 Phase 3 data | Clinical trial | ⚠️ **NOT YET AVAILABLE** — data expected but not published | **Flag: demo will use Phase 2 data only; update when Phase 3 publishes** |
| OX40L mechanism-of-action literature | Mechanistic | ✅ Public | Search PubMed for OX40/OX40L biology and immunosuppression |
| Kaposi's sarcoma and immunosuppression literature | Safety context | ✅ Public | Ingest — critical for KS signal contextualization |
| Dupixent comparative safety data | Published literature | ✅ Public (already ingested for Instance 2) | Cross-reference |
| HHV-8 / Kaposi's sarcoma epidemiology | Published literature | ✅ Public | Ingest for KS background rate estimation |

**⚠️ DATA FLAG:** Phase 3 COAST-1 data is not yet publicly available. This demo will demonstrate the competitive B/R positioning framework using Phase 2 data, with the architecture ready to ingest Phase 3 data as soon as it publishes. Communicate this clearly to Sanofi.

#### Ontology Configuration

- [ ] MedDRA v27.0: Activate SOCs for dermatology (Skin and subcutaneous tissue disorders), infections (Infections and infestations — specifically viral infections, HHV-8), neoplasms (Neoplasms benign/malignant — Kaposi's sarcoma)
- [ ] ChEBI: Map amlitelimab, dupilumab (comparator)
- [ ] Configure OX40L pathway ontology mapping (custom if needed)

#### SLM Pipeline Modules to Activate

All modules activated. Emphasis on:
- Safety event extractor (KS signal)
- Relation extraction (mechanism-specific safety associations)
- Efficacy endpoint extraction (for head-to-head B/R vs. Dupixent)

### 3.2 Data Ingestion & Harmonization

#### Step 3.2.1: Source Document Collection

1. PubMed: `"amlitelimab" OR "KY1005" OR "anti-OX40L"`
2. PubMed: `"OX40L" AND ("mechanism" OR "immunology" OR "T cell")`
3. PubMed: `"Kaposi sarcoma" AND ("immunosuppression" OR "biologic" OR "monoclonal antibody")`
4. PubMed: `"HHV-8" AND ("prevalence" OR "reactivation" OR "immunosuppression")`
5. Retrieve Dupixent atopic dermatitis safety data (from Instance 2 corpus — reuse, do not re-ingest)
6. Retrieve competitor atopic dermatitis biologics safety data: tralokinumab, lebrikizumab, nemolizumab

**Expected corpus size:** 80-150 documents

#### Step 3.2.2: Ingestion

1. Upload to `sanofi-demo/amlitelimab/raw/`
2. Trigger DAG: `sanofi_amlitelimab_ingest`
3. Verify and check for errors
4. Tag documents by category: amlitelimab clinical, OX40L mechanism, KS context, Dupixent comparator

#### Step 3.2.3: Normalization

- MedDRA coding: PT level
- Map KS signal using MedDRA PT "Kaposi's sarcoma" and related terms
- Normalize HHV-8 seroprevalence data for background rate contextualization
- Harmonize efficacy endpoints across amlitelimab and Dupixent (EASI, IGA, pruritus NRS)

#### Step 3.2.4: Quality Thresholds

Standard thresholds apply. Additional:
- KS-specific extraction: manually verify all KS-related entities are captured from ATLANTIS data
- Mechanism literature: verify OX40L pathway entities extracted correctly

### 3.3 Platform Configuration

#### Output Types

| Output Type | Enable | Notes |
|-------------|--------|-------|
| Disease Analysis | ✅ | Atopic dermatitis landscape |
| Clinical Landscape | ✅ | **Primary** — Competitive landscape: amlitelimab vs. Dupixent vs. other biologics |
| AE Report | ✅ | KS signal-focused |
| BRA | ✅ | **Primary** — Comparative B/R: amlitelimab vs. Dupixent |
| BRA Summary | ✅ | Regulatory positioning summary |

#### BRAT Framework Configuration

- [ ] Configure comparative Value Tree:
  - **Amlitelimab Benefits:** EASI improvement, IGA response, subcutaneous administration advantages, novel mechanism differentiation
  - **Amlitelimab Risks:** KS signal (with context: HHV-8 background rate, mechanism plausibility), infection risk, other Phase 2 AEs
  - **Dupixent comparator arm:** Mirror benefit/risk structure for head-to-head comparison
- [ ] Enable comparative B/R visualization (side-by-side)
- [ ] Configure KS signal contextualization module: background KS rates by geography, HHV-8 seroprevalence, mechanism-of-action plausibility assessment

### 3.4 Demo Environment Setup

- [ ] Create isolated instance: `sanofi-demo-amlitelimab`
- [ ] Access controls per Step G4
- [ ] Performance benchmark: target < 15 minutes full pipeline

### 3.5 Validation & QA

- [ ] Extraction spot-check: 10 documents
- [ ] Auditability check: 5 claims traced to source
- [ ] **KS signal validation:** Manually verify every KS-related extraction from ATLANTIS data. Zero misses acceptable — this is the critical safety signal.
- [ ] **Comparative B/R check:** Verify amlitelimab vs. Dupixent comparison outputs are balanced and methodologically sound
- [ ] Baseline comparison against HS reference
- [ ] End-to-end user access test

### 3.6 Demo Walkthrough Script

**Suggested navigation path (20-25 minutes):**

1. **Competitive landscape** (3 min): Show atopic dermatitis biologic landscape — Dupixent dominance, emerging competitors
2. **KS signal contextualization** (7 min): This is the key demonstration. Show how the platform structures the KS signal: cases identified, mechanism plausibility (OX40L → T cell modulation → HHV-8 reactivation hypothesis), background rates, geographic variation. Demonstrate that the platform provides *context*, not just signal detection.
3. **Comparative B/R framework** (7 min): Show side-by-side amlitelimab vs. Dupixent BRA. Demonstrate how the platform structures the differentiation narrative for regulatory and commercial positioning.
4. **Auditability** (3 min): Trace a KS-related claim back to the ATLANTIS publication
5. **Phase 3 readiness** (3 min): Show how the framework is ready to ingest COAST-1 data — the Value Tree, the comparator arm, the extraction pipeline are all configured. When Phase 3 data publishes, BRA updates in hours, not months.
6. **Q&A** (5 min)

**Anticipated Sanofi questions:**
- *"What about the COAST-1 data?"* → Framework is ready. Upon publication, data is ingested and BRA updates automatically. Demo shows the methodology and structure.
- *"How does this help with regulatory submission?"* → The comparative B/R framework maps directly to eCTD Module 2.5 and supports the differentiation narrative for health authority discussions
- *"Is the KS signal a concern for approval?"* → Platform doesn't make that judgment — it structures the evidence so Sanofi's team can make an informed decision with full traceability

---

## DEMO INSTANCE 4: Rilzabrutinib — Cross-Indication Hematology B/R

### Context

Multiple Phase 3 programs across ITP (immune thrombocytopenia), IgG4-RD (IgG4-related disease), wAIHA (warm autoimmune hemolytic anemia), and Sickle Cell Disease. Cross-indication complexity with concurrent submissions.

### 4.1 Pre-Configuration Checklist

#### Data Sources & Availability

| Source | Type | Availability | Action Required |
|--------|------|--------------|-----------------|
| Rilzabrutinib Phase 2/3 publications (LUNA 3 for ITP, others) | Clinical trial | ✅ Public (published Phase 2; Phase 3 publications emerging) | Ingest all available |
| BTK inhibitor class safety data (cross-reference with tolebrutinib Instance 1) | Published literature | ✅ Public (partially ingested for Instance 1) | Cross-reference; add hematology-specific BTK data |
| ITP treatment landscape (romiplostim, eltrombopag, avatrombopag, fostamatinib) | Published literature | ✅ Public | Ingest for comparative context |
| IgG4-RD treatment landscape | Published literature | ✅ Public (limited — rare disease) | Ingest available publications |
| wAIHA treatment landscape | Published literature | ✅ Public (limited) | Ingest |
| Sickle Cell Disease treatment safety data | Published literature | ✅ Public | Ingest |
| Rare disease comparator safety databases | Published/FAERS | ✅ Public | Configure FAERS queries per indication |

**⚠️ DATA FLAG:** IgG4-RD and wAIHA are rare indications with limited published data. The demo will show the platform's capability with available data and highlight where evidence gaps exist — this is itself a valuable demo feature (gap analysis).

#### Ontology Configuration

- [ ] MedDRA v27.0: Activate SOCs for Blood and lymphatic system disorders, Immune system disorders, Infections
- [ ] ChEBI: Map rilzabrutinib, plus comparators per indication
- [ ] Configure indication-specific MedDRA queries: ITP-related terms, hemolysis-related terms, IgG4-RD-related terms

#### SLM Pipeline Modules

All modules activated. Emphasis on cross-indication entity resolution.

### 4.2 Data Ingestion & Harmonization

#### Step 4.2.1: Source Document Collection

1. PubMed: `"rilzabrutinib" OR "PRN1008"`
2. PubMed per indication: `"immune thrombocytopenia" AND "BTK"`, `"IgG4-related disease" AND "treatment"`, `"warm autoimmune hemolytic anemia" AND "treatment"`, `"sickle cell" AND "BTK"`
3. FAERS queries for rilzabrutinib (if available) and comparators per indication
4. Retrieve BTK inhibitor hematology-specific safety data
5. Collect rare disease natural history publications for each indication (for baseline event rate estimation)

**Expected corpus size:** 100-200 documents

#### Step 4.2.2-4.2.4: Ingestion, Normalization, Quality

- Upload to `sanofi-demo/rilzabrutinib/raw/`
- Trigger DAG: `sanofi_rilzabrutinib_ingest`
- Tag documents by indication (ITP, IgG4-RD, wAIHA, Sickle Cell)
- Standard normalization and quality thresholds apply
- **Additional check:** For rare indications (IgG4-RD, wAIHA), document evidence density. If fewer than 10 publications per indication, flag as "limited evidence base" in demo outputs.

### 4.3 Platform Configuration

#### Output Types

| Output Type | Enable | Notes |
|-------------|--------|-------|
| Disease Analysis | ✅ | Per-indication disease landscape |
| Clinical Landscape | ✅ | Cross-indication competitive landscape |
| AE Report | ✅ | Cross-program safety signal report |
| BRA | ✅ | **Primary** — Per-indication BRA + cross-indication safety overlay |
| BRA Summary | ✅ | Per-indication regulatory submission summary |

#### BRAT Framework Configuration

- [ ] Configure per-indication Value Trees (4 separate trees)
- [ ] Configure cross-indication safety overlay: identify AEs that appear across multiple rilzabrutinib indications (BTK inhibitor class effects)
- [ ] Enable concurrent submission view: show regulatory readiness status per indication
- [ ] Configure comparator arms per indication (fostamatinib for ITP, rituximab for wAIHA, etc.)

### 4.4-4.5 Demo Environment Setup & Validation

- [ ] Instance: `sanofi-demo-rilzabrutinib`
- [ ] Standard access controls, performance benchmarks, QA checks
- [ ] **Cross-indication validation:** Verify BTK class safety signals are consistently identified across all indications
- [ ] **Evidence gap reporting:** Verify the platform correctly identifies and flags evidence gaps in rare indications

### 4.6 Demo Walkthrough Script

**Suggested navigation path (20-25 minutes):**

1. **Cross-indication overview** (3 min): Show the 4-indication landscape simultaneously
2. **Cross-program safety signal detection** (7 min): Demonstrate how the platform identifies BTK inhibitor class effects that manifest across all indications vs. indication-specific signals
3. **Per-indication BRA** (5 min): Deep-dive into ITP BRA as the most data-rich indication
4. **Evidence gap analysis** (5 min): Show how the platform identifies and flags evidence gaps in rare indications (IgG4-RD, wAIHA) — this is a feature, not a limitation
5. **Concurrent submission readiness** (3 min): Show how BRA outputs map to regulatory submission requirements per indication
6. **Q&A** (5 min)

**Anticipated Sanofi questions:**
- *"How do you handle the small sample sizes in rare indications?"* → Platform explicitly flags evidence density. Probabilistic B/R modeling is especially valuable here — contextualizes limited data against class effects and natural history.
- *"Can this support concurrent submissions to multiple regulators?"* → Yes — outputs align to eCTD structure. Each indication gets its own BRA with cross-indication safety context.

---

## DEMO INSTANCE 5: Duvakitug (TL1A/IL-23 bispecific) — Dual-Mechanism IBD B/R (Lighter Demo)

### Context

Phase 3 for UC (ulcerative colitis) and Crohn's disease. Dual mechanism (TL1A + IL-23 targeting) introduces novel safety considerations. This is a lighter demo.

### 5.1 Pre-Configuration Checklist

#### Data Sources & Availability

| Source | Type | Availability | Action Required |
|--------|------|--------------|-----------------|
| Duvakitug Phase 2 publications | Clinical trial | ✅ Public (if published) / ⚠️ Limited | Search and ingest available |
| TL1A mechanism literature | Mechanistic | ✅ Public | Ingest |
| IL-23 inhibitor safety data (risankizumab, guselkumab, mirikizumab) | Published literature | ✅ Public | Ingest for single-mechanism comparator |
| IBD treatment landscape (adalimumab, infliximab, vedolizumab, ustekinumab, tofacitinib) | Published literature | ✅ Public | Ingest for competitive context |
| Dual-mechanism safety literature (bispecific antibody safety profiles) | Published literature | ✅ Public (limited for this mechanism) | Ingest available |

**⚠️ DATA FLAG:** Duvakitug is early in clinical development. Limited published safety data. This demo is intentionally lighter — focused on the dual-mechanism safety mapping methodology rather than comprehensive BRA.

#### Ontology, Pipeline, Configuration

- [ ] MedDRA v27.0: Gastrointestinal disorders, Immune system disorders, Infections
- [ ] ChEBI: Map duvakitug, IL-23 inhibitors, TL1A-targeting agents
- [ ] All SLM modules activated (lighter corpus means faster pipeline)
- [ ] IBD vertical: configure from scratch (no existing vertical)

### 5.2 Data Ingestion

1. PubMed: `"duvakitug" OR "anti-TL1A" AND "IL-23"`, `"TL1A" AND ("IBD" OR "Crohn" OR "ulcerative colitis")`, `"IL-23" AND ("safety" OR "adverse events") AND ("IBD" OR "Crohn")`
2. Ingest IL-23 inhibitor safety data as comparator baseline
3. Upload to `sanofi-demo/duvakitug/raw/`
4. Trigger DAG: `sanofi_duvakitug_ingest`

**Expected corpus size:** 50-100 documents

### 5.3 Platform Configuration

| Output Type | Enable | Notes |
|-------------|--------|-------|
| Disease Analysis | ✅ | IBD landscape |
| Clinical Landscape | ✅ | IBD biologic competitive landscape |
| AE Report | ✅ | Dual-mechanism safety mapping |
| BRA | ✅ | IBD-focused B/R with mechanism-specific safety |
| BRA Summary | ❌ | Not needed for lighter demo |

#### BRAT Configuration

- [ ] Value Tree: UC and Crohn's efficacy endpoints + dual-mechanism safety risks
- [ ] Map TL1A-specific safety signals vs. IL-23-specific signals vs. combined/novel signals
- [ ] Configure mechanism-of-action safety hypothesis layer

### 5.4-5.5 Setup & Validation

- [ ] Instance: `sanofi-demo-duvakitug`
- [ ] Standard access controls
- [ ] Lighter QA: 5-document spot-check, 3 claims traced to source
- [ ] Baseline comparison against HS reference

### 5.6 Demo Walkthrough Script

**Suggested navigation path (15 minutes):**

1. **IBD landscape** (3 min): Competitive biologics landscape for UC/Crohn's
2. **Dual-mechanism safety mapping** (5 min): Show how the platform separates TL1A-attributable vs. IL-23-attributable vs. novel combined safety signals
3. **IBD B/R framework** (4 min): Show BRA for UC with mechanism-specific risk layers
4. **Auditability** (3 min): Quick trace-to-source demonstration

---

## Post-Demo Handoff (All Instances)

### Export & Sharing

1. **Export formats available:** PDF (regulatory-grade), Excel (data tables), JSON (API integration)
2. **For each completed demo:** Generate a PDF export of the BRA and BRA Summary outputs
3. **Share via:** Secure file transfer (encrypted) — confirm Sanofi's preferred method
4. **Retain all demo outputs** in ArcaScience archive for reference during PoC scoping

### Transition to PoC Engagement

| Item | Detail |
|------|--------|
| **PoC scope** | 1 priority asset (Sanofi selects from the 5 demo instances) |
| **PoC pricing** | 75K€ – 150K€ (depending on asset complexity and data integration scope) |
| **PoC duration** | 6-8 weeks |
| **PoC deliverable** | Full BRA on priority asset using Sanofi's internal + public data |
| **Data integration** | During PoC: Sanofi provides internal clinical data under NDA; data stays on Sanofi infrastructure if required |
| **Success criteria** | Define jointly: F1 thresholds, coverage metrics, auditability verification, comparison to existing BRA process |
| **Expansion path** | PoC → Platform license (Tier 1: $75K-$100K/year per asset; Tier 2: $125K-$175K/year professional; Tier 3: $200K-$300K/year enterprise) |

### Follow-Up Actions

- [ ] Send Brandon Rufino the requested publication links backing validated results (HS metrics, peer-reviewed validation papers)
- [ ] Prepare RAISE alignment pre-assessment document for Sanofi's IRAG review
- [ ] Schedule follow-up with Sanofi to present demo instances and receive prioritization
- [ ] Confirm data residency requirements with Sanofi legal/IT

---

## Sanofi-Facing Summary (To Share with Sanofi for Prioritization)

### Proposed Demo Instances for Sanofi Evaluation

ArcaScience has prepared five tailored demo instances of its Benefit-Risk Assessment platform, each configured for a specific Sanofi pipeline asset. We invite the Sanofi team to review and prioritize which demos to explore first.

| # | Asset | What the Demo Showcases | Why It Matters for Sanofi |
|---|-------|------------------------|--------------------------|
| 1 | **Tolebrutinib** | Post-CRL evidence reframing: subpopulation B/R analysis, DILI signal structuring, regulatory resubmission workflow | Supports the resubmission strategy following the December 2025 CRL. Identifies patient segments with favorable B/R profiles using structured evidence. |
| 2 | **Dupixent** | Multi-indication B/R monitoring: cross-indication safety profiling, COPD-specific risk modeling, consistency checking | Addresses the scaling challenge of monitoring B/R across 9 indications as the COPD population (~300K US adults) introduces fundamentally different risk profiles. |
| 3 | **Amlitelimab** | Competitive B/R positioning: KS signal contextualization, head-to-head B/R framework vs. Dupixent, mechanism-specific safety structuring | Supports Phase 3 regulatory and commercial positioning with structured evidence differentiating amlitelimab's novel mechanism. |
| 4 | **Rilzabrutinib** | Cross-indication hematology B/R: cross-program signal detection, per-indication BRA, concurrent submission readiness | Manages the complexity of 4 concurrent Phase 3 programs with shared BTK class signals and indication-specific profiles. |
| 5 | **Duvakitug** | Dual-mechanism IBD B/R: mechanism-specific safety mapping, TL1A/IL-23 signal separation | Early-stage B/R framework for a novel bispecific mechanism in UC/Crohn's. |

**Our validated track record with Sanofi:** ArcaScience previously delivered a BRA for a Sanofi biologic in Phase 2 (inflammatory dermatology), completing 18 months of manual work in 2 weeks, identifying 5 previously undocumented risks, and achieving F1 scores of 88-92% across extraction types — validated by Sanofi's own team. All outputs were fully auditable and traceable to source.

**Next step:** Please indicate which 1-2 demo instances you'd like to explore first, and we will schedule a guided walkthrough.

---

## Appendix A: Quality Gate Checklist (Sign-Off Required Before Demo Opening)

For each demo instance, the following must be signed off by the responsible team member before Sanofi access is granted:

| # | Check | Responsible | Sign-Off |
|---|-------|-------------|----------|
| 1 | All source documents ingested without errors | Data Engineer | ☐ |
| 2 | Extraction F1 meets thresholds (AE ≥92%, Biomarker ≥90%, Risk ≥88%, Benefit ≥92%) | ML Engineer | ☐ |
| 3 | All BRA outputs trace to source (auditability verified) | QA Lead | ☐ |
| 4 | Regulatory output alignment verified (eCTD 2.5 / PBRER) | Regulatory SME | ☐ |
| 5 | Baseline comparison against HS reference completed | ML Engineer | ☐ |
| 6 | ALCOA+ audit trail functioning (tested) | QA Lead | ☐ |
| 7 | Role-based access configured and tested | DevOps | ☐ |
| 8 | Performance benchmarks met | DevOps | ☐ |
| 9 | Demo walkthrough rehearsed internally | Demo Lead | ☐ |
| 10 | RAISE alignment documentation prepared | Compliance | ☐ |

**No demo instance may be opened to Sanofi until all 10 checks are signed off.**

---

## Appendix B: SLM Pipeline Module Reference

The ArcaScience platform operates 24 task-specific Small Language Models (SLMs), trained by clinicians on 10M+ AE case reports, 500K+ clinical trial records, 2M+ PubMed abstracts, and 100K+ regulatory documents. No model retraining is needed for new therapeutic areas — adaptation happens through pipeline configuration.

| Category | Models | Function |
|----------|--------|----------|
| Document classification | Document type classifier | Categorizes input (case report, clinical trial, observational study, etc.) |
| Section identification | Section layering model | Identifies structural sections (abstract, methodology, results, discussion) |
| Safety entity extraction | Safety event extractor | Extracts AE terms, temporal status, severity, outcomes, drug names |
| Relation extraction | Relation extraction model | Links entities within context (drug X causes event Y) |
| Efficacy endpoint extraction | 4-model chain (extract, structure, cluster, normalize) | Identifies and standardizes efficacy endpoints |
| Patient information extraction | Patient information models | Extracts demographics (gender, age, population characteristics) |
| Study design extraction | Study design extractor | Extracts sample size, duration, blinding, arm structure |
| Drug/dosage extraction | Drug and dosage models | Extracts dose, frequency, administration route |
| Normalization | Ontology normalization models | Maps terms to MedDRA, SNOMED CT, ChEBI, Disease Ontology |
| Knowledge graph | Linking and resolution models | Connects entities across sources into the Profiling Base |

**Performance benchmarks:**
- AE extraction precision: 92% (vs. 67% for GPT-4)
- NLP extraction F1: 94%
- Signal detection: 3x improvement vs. manual review
- PSUR cycle time reduction: 60%

---

*Document prepared: 2026-03-25*
*Next review: Upon Sanofi prioritization response*
*GAMP 5 Category 5 — All outputs validated per ArcaScience quality management system*
