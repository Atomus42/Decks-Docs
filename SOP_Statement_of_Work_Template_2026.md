# ArcaScience BRA Platform - Statement of Work Template

| Field | Detail |
|---|---|
| Document ID | ARC-SOW-2026-TPL-001 |
| Version | 1.0 |
| Effective Date | 2026-03-25 |
| Classification | Confidential |
| Author | ArcaScience Commercial & Delivery Team |
| Template Applicability | PoC Engagements and Platform License Agreements |
| Status | Draft - Pending Approval |

---

## Table of Contents

1. Engagement Overview
2. Scope of Work
3. Deliverables Schedule and Milestones
4. Asset-Specific Configuration Scope
5. Data Requirements
6. Acceptance Criteria
7. Platform Outputs to Be Delivered
8. Regulatory Alignment Specifications
9. Project Governance
10. Resource Plan
11. Timeline and Phases
12. Pricing and Payment Schedule
13. Change Order Procedure
14. Intellectual Property Provisions
15. Confidentiality Requirements
16. Warranty and Support
17. Termination Provisions
18. Signature Block

---

## 1. Engagement Overview

### 1.1 Parties

| Party | Details |
|---|---|
| Service Provider | ArcaScience SAS, [Address], hereinafter "ArcaScience" |
| Client | [Client Legal Entity Name], [Address], hereinafter "Client" |

### 1.2 Engagement Type

This SOW covers the following engagement type (select one):

- [ ] **Proof of Concept (PoC)** - Time-bound evaluation of the BRA platform on a single asset over 6 - 8 weeks
- [ ] **Platform License** - Annual subscription to the BRA platform with ongoing access and support

### 1.3 Engagement Summary

| Parameter | PoC | Platform License |
|---|---|---|
| Duration | 6 - 8 weeks | 12 months (renewable) |
| Assets in scope | 1 | Per tier agreement |
| Outputs | Up to 6 output types | All 6 output types |
| Investment range | EUR 75,000 - EUR 150,000 | USD 75,000 - USD 300,000/year (tier-dependent) |
| Support model | Dedicated project team | Tiered support (see Section 16) |
| Validation | PoC-level validation | Full GAMP 5 Category 5 validation |

### 1.4 Platform Overview

The ArcaScience BRA (Benefit-Risk Assessment) platform is a clinician-trained AI system comprising 24 specialized Small Language Models (SLMs) trained on:

- 10,000,000+ adverse event (AE) reports
- 500,000+ clinical trial records
- 2,000,000+ scientific abstracts
- 100,000+ regulatory documents

The platform is GAMP 5 Category 5 validated, ALCOA+ compliant, and meets FDA 21 CFR Part 11 and EU Annex 11 requirements. It has been deployed across 50+ regulatory submissions spanning 12 therapeutic areas.

### 1.5 Reference Engagement

ArcaScience's prior engagement with a top-10 pharma company (hidradenitis suppurativa BRA) demonstrated:

- 18 months of manual work completed in 2 weeks
- 5 previously undocumented safety risks identified
- Total cost of USD 100,000 vs. estimated CRO cost of USD 1,200,000
- Full regulatory acceptance of outputs

---

## 2. Scope of Work

### 2.1 In-Scope Activities

| # | Activity | Description | Responsible |
|---|---|---|---|
| 2.1.1 | Therapeutic area configuration | Configure BRA platform SLMs for the target therapeutic area, including disease ontology, standard-of-care context, and relevant clinical endpoints | ArcaScience |
| 2.1.2 | Asset-specific setup | Configure platform for the specific investigational product, including compound profile, mechanism of action, clinical development stage, and target indication | ArcaScience |
| 2.1.3 | Data ingestion and processing | Ingest client-provided data packages and publicly available data sources; perform preprocessing, deduplication, and quality checks | ArcaScience |
| 2.1.4 | SLM extraction pipeline | Execute the 24-SLM extraction and inference pipeline across all ingested data sources | ArcaScience |
| 2.1.5 | Ontology normalization | Normalize all extracted entities to MedDRA v27.0, SNOMED CT, and ChEBI controlled terminologies | ArcaScience |
| 2.1.6 | Benefit-risk analysis | Generate BRAT/CIOMS XII framework-aligned benefit-risk assessment with quantified scoring | ArcaScience |
| 2.1.7 | Output generation | Produce all agreed-upon deliverable outputs (see Section 7) | ArcaScience |
| 2.1.8 | Quality assurance | Internal clinical SME review of all outputs; automated and manual validation | ArcaScience |
| 2.1.9 | Validation documentation | Provide GAMP 5-aligned validation documentation including IQ/OQ/PQ summaries | ArcaScience |
| 2.1.10 | Client training | Deliver platform training and output interpretation sessions to Client team | ArcaScience |
| 2.1.11 | Regulatory alignment review | Joint review of outputs against Client's regulatory submission requirements | Joint |
| 2.1.12 | Data provision | Provide required source data packages per the data requirements specification (Section 5) | Client |
| 2.1.13 | Subject matter expert access | Make clinical and regulatory SMEs available for configuration and validation activities | Client |
| 2.1.14 | Acceptance review | Conduct formal acceptance review of deliverables per acceptance criteria (Section 6) | Client |

### 2.2 Out-of-Scope Activities

The following activities are explicitly excluded from this SOW unless added via a Change Order (Section 13):

| # | Exclusion | Notes |
|---|---|---|
| 2.2.1 | Regulatory submission filing | ArcaScience provides submission-ready outputs but does not file with regulatory authorities |
| 2.2.2 | Clinical study design | Platform provides clinical landscape analysis; study protocol design is excluded |
| 2.2.3 | Pharmacovigilance case processing | Platform analyzes aggregate AE data; individual case safety report (ICSR) processing is excluded |
| 2.2.4 | GxP system validation of Client infrastructure | Validation covers the ArcaScience platform only |
| 2.2.5 | Translation services | Outputs are delivered in English; translation to other languages is excluded |
| 2.2.6 | Comparator product BRA | Unless explicitly listed as an in-scope asset |
| 2.2.7 | Post-market surveillance setup | Platform can inform surveillance strategy but does not implement ongoing monitoring systems |
| 2.2.8 | Legacy data migration | Migration of data from Client's existing systems to ArcaScience platform is excluded |
| 2.2.9 | Custom model development | SLM customization beyond therapeutic area configuration is excluded |
| 2.2.10 | On-premises deployment | Platform is delivered as a cloud-hosted service; on-premises installation is excluded |

### 2.3 Assumptions

1. Client will provide all required data packages within 5 business days of the Phase 2 kickoff
2. Client SMEs will be available for a minimum of 4 hours per week during the engagement
3. Client data will be in one of the supported formats: PDF, XML (E2B), CSV, DOCX, or structured JSON
4. The target therapeutic area is within the 12 therapeutic areas currently supported by ArcaScience
5. No more than 2 rounds of revision per deliverable are included in the base scope
6. Client will designate a single point of contact with decision-making authority for day-to-day matters
7. All data shared by Client is appropriately de-identified or Client has obtained necessary consents for sharing
8. ArcaScience infrastructure will maintain 99.9% availability during the engagement period

---

## 3. Deliverables Schedule and Milestones

### 3.1 PoC Engagement Milestones

| Milestone | Description | Target Week | Deliverable | Acceptance Event |
|---|---|---|---|---|
| M1 | Project kickoff and configuration plan | Week 1 | Signed project charter; configuration specification | Client sign-off on configuration spec |
| M2 | Data ingestion complete | Week 2 | Data ingestion report; quality assessment | Client confirmation of data completeness |
| M3 | Extraction pipeline execution complete | Week 3 - 4 | Extraction quality report; F1 scores per module | Review of F1 scores against thresholds |
| M4 | Draft outputs delivered | Week 5 | Draft of all 6 output types | Client SME review initiated |
| M5 | Final outputs delivered | Week 6 - 7 | Finalized outputs; validation documentation | Formal acceptance review |
| M6 | Engagement closeout | Week 8 | Closeout report; lessons learned; transition plan | Client sign-off on closeout |

### 3.2 Platform License Milestones (Year 1)

| Milestone | Description | Target Month | Deliverable | Acceptance Event |
|---|---|---|---|---|
| M1 | Contract execution and onboarding | Month 1 | Signed contract; onboarding plan; access credentials | Client sign-off on onboarding |
| M2 | First asset configuration and delivery | Month 2 - 3 | Full BRA output suite for first asset | Formal acceptance per Section 6 |
| M3 | Second asset configuration (if applicable) | Month 4 - 5 | Full BRA output suite for second asset | Formal acceptance per Section 6 |
| M4 | Mid-year review | Month 6 | Performance report; usage analytics; roadmap review | Steering committee sign-off |
| M5 | Additional assets (per schedule) | Month 7 - 11 | BRA outputs per agreed schedule | Per-asset acceptance |
| M6 | Annual review and renewal | Month 12 | Annual performance report; renewal proposal | Renewal decision |

### 3.3 Deliverable Format Specifications

| Deliverable | Format | Regulatory Alignment |
|---|---|---|
| Disease Analysis | PDF + structured JSON | ICH E2E; MedDRA-coded |
| Clinical Landscape | PDF + structured JSON + interactive dashboard | ICH E8; SNOMED CT-coded |
| Clinical Endpoint Study | PDF + structured CSV | ICH E9; statistical standards |
| AE Reports | PDF + E2B(R3) XML | ICH E2B(R3); MedDRA v27.0 |
| BRA (Full) | PDF + structured JSON | BRAT/CIOMS XII; eCTD Module 2.5 |
| BRA Summary | PDF | PBRER Section 16 alignment |
| Validation Documentation | PDF | GAMP 5 Category 5; IQ/OQ/PQ |

---

## 4. Asset-Specific Configuration Scope

### 4.1 Configuration Parameters

For each in-scope asset, ArcaScience will configure the platform based on the following parameters provided by the Client:

| Parameter | Description | Client Input Required |
|---|---|---|
| Compound identifier | INN, trade name, internal compound code | Yes - provided at kickoff |
| Mechanism of action | Pharmacological class and mechanism | Yes - provided at kickoff |
| Target indication(s) | Primary and secondary indications per regulatory strategy | Yes - provided at kickoff |
| Development stage | Phase I, II, III, IV, or post-market | Yes - provided at kickoff |
| Comparator(s) | Active comparators and standard-of-care treatments | Yes - provided at kickoff |
| Clinical endpoints | Primary, secondary, and exploratory endpoints per protocol | Yes - provided at kickoff |
| Safety focus areas | Known and suspected risks; class effects; target organ toxicity | Yes - provided at kickoff |
| Regulatory target | FDA, EMA, PMDA, Health Canada, or multi-regional | Yes - provided at kickoff |
| Therapeutic area | Must align to one of ArcaScience's 12 supported areas | Yes - confirmed at kickoff |
| Data cutoff date | Date up to which data should be included in the analysis | Yes - provided at kickoff |

### 4.2 Configuration Activities

| Step | Activity | Duration | Output |
|---|---|---|---|
| 4.2.1 | Therapeutic area SLM configuration | 2 - 3 days | Configured model ensemble for therapeutic area |
| 4.2.2 | Compound-specific ontology setup | 1 - 2 days | Compound dictionary; synonym mapping |
| 4.2.3 | Endpoint library configuration | 1 - 2 days | Endpoint taxonomy mapped to clinical protocols |
| 4.2.4 | Safety profile seeding | 1 day | Known risk catalog; class effect library |
| 4.2.5 | Regulatory template selection | 1 day | Output templates configured for target authority |
| 4.2.6 | Configuration validation | 2 - 3 days | Configuration test report; QC sign-off |

### 4.3 Supported Therapeutic Areas

| # | Therapeutic Area | SLM Modules Available | Notes |
|---|---|---|---|
| 1 | Oncology (solid tumors) | Full 24-SLM suite | Includes immuno-oncology |
| 2 | Oncology (hematologic) | Full 24-SLM suite | Includes CAR-T and BiTE contexts |
| 3 | Immunology / Inflammation | Full 24-SLM suite | Including dermatology sub-specialties |
| 4 | Neurology / CNS | Full 24-SLM suite | Including neurodegenerative and psychiatric |
| 5 | Cardiovascular | Full 24-SLM suite | Including heart failure, arrhythmia |
| 6 | Metabolic / Endocrine | Full 24-SLM suite | Including diabetes, obesity |
| 7 | Respiratory | Full 24-SLM suite | Including asthma, COPD, fibrosis |
| 8 | Infectious disease | Full 24-SLM suite | Including antiviral, antibacterial |
| 9 | Rare diseases | Full 24-SLM suite | Enhanced small-population analytics |
| 10 | Gastroenterology | Full 24-SLM suite | Including IBD, liver disease |
| 11 | Nephrology | Full 24-SLM suite | Including CKD, transplant |
| 12 | Ophthalmology | Full 24-SLM suite | Including retinal diseases |

---

## 5. Data Requirements

### 5.1 Data Provided by Client

| # | Data Type | Format | Required/Optional | Purpose |
|---|---|---|---|---|
| 5.1.1 | Clinical study reports (CSRs) | PDF or structured XML | Required | Primary efficacy and safety data source |
| 5.1.2 | Individual case safety reports (ICSRs) | E2B(R3) XML or structured CSV | Required | AE-level data for safety analysis |
| 5.1.3 | Clinical study protocols | PDF | Required | Endpoint definitions, study design context |
| 5.1.4 | Investigator brochure (current version) | PDF | Required | Compound profile, known safety information |
| 5.1.5 | Summary of clinical efficacy (SCE) | PDF | Optional | Pre-existing efficacy summaries for validation |
| 5.1.6 | Summary of clinical safety (SCS) | PDF | Optional | Pre-existing safety summaries for validation |
| 5.1.7 | PSUR/PBRER (most recent) | PDF | Optional | Historical benefit-risk context |
| 5.1.8 | Risk management plan (RMP) | PDF | Optional | Known and potential risks; risk minimization measures |
| 5.1.9 | Compound-specific dictionary | CSV or JSON | Optional | Custom terminology for proprietary compound naming |
| 5.1.10 | Regulatory submission history | PDF or structured summary | Optional | Prior regulatory interactions context |

### 5.2 Data Sourced by ArcaScience

| # | Data Type | Source | Coverage | Update Frequency |
|---|---|---|---|---|
| 5.2.1 | Published literature | PubMed, Embase, Cochrane Library | 2,000,000+ abstracts; full text where available | Weekly |
| 5.2.2 | Clinical trial registries | ClinicalTrials.gov, EudraCT, WHO ICTRP | 500,000+ trials | Daily |
| 5.2.3 | Regulatory documents | FDA (Drugs@FDA, FAERS), EMA (EPAR), PMDA | 100,000+ documents | Weekly |
| 5.2.4 | Spontaneous AE reports | FDA FAERS, EudraVigilance (public access), WHO VigiBase (if licensed) | 10,000,000+ reports | Monthly |
| 5.2.5 | Medical ontologies | MedDRA v27.0, SNOMED CT (current release), ChEBI (current release) | Full ontology coverage | Per release cycle |
| 5.2.6 | Clinical guidelines | Professional society guidelines relevant to therapeutic area | Major guidelines (NCCN, ESC, ADA, etc.) | Quarterly |

### 5.3 Data Quality Requirements

| Requirement | Specification | Verification |
|---|---|---|
| Completeness | All mandatory data types must be provided; missing data documented | Ingestion quality report |
| Format compliance | Data in specified formats; encoding UTF-8 | Automated format validation |
| De-identification | All patient data must be de-identified per applicable regulations | Client attestation; ArcaScience PII scan |
| Currency | Data must reflect the agreed data cutoff date | Data cutoff verification |
| Authorization | Client confirms right to share all provided data | Data sharing agreement |
| Integrity | Files must be uncorrupted and complete | Checksum validation |

### 5.4 Data Transfer Mechanism

| Method | Security | Use Case |
|---|---|---|
| ArcaScience Secure Upload Portal | TLS 1.3; AES-256 at rest; access-controlled | Standard data transfer (recommended) |
| SFTP | SSH key authentication; AES-256 in transit | Large file transfers (> 10 GB) |
| Client-designated secure platform | Per client security requirements | When client policy mandates specific transfer tools |

---

## 6. Acceptance Criteria

### 6.1 Performance Thresholds

| Metric | Threshold | Measurement Method | Failure Action |
|---|---|---|---|
| AE extraction F1 score | >= 92% | Measured against client-provided gold standard subset (minimum 200 annotated AEs) | Remediation cycle; re-extraction; root cause analysis |
| Biomarker extraction F1 score | >= 90% | Measured against annotated biomarker dataset | Remediation cycle; model adjustment |
| Risk signal classification F1 score | >= 88% | Measured against expert-classified risk signals | Enhanced clinical review; model recalibration |
| Benefit claim extraction F1 score | >= 92% | Measured against annotated benefit claims | Remediation cycle; re-extraction |
| MedDRA coding accuracy | >= 95% | Measured by PT-level agreement with expert coding | Mapping review and correction |
| Data coverage (literature) | >= 90% of relevant publications identified | Measured against Client's reference bibliography | Gap analysis; supplementary search |
| Data coverage (trials) | >= 95% of relevant registered trials captured | Measured against Client's trial inventory | Supplementary registry search |
| Report completeness | 100% of required sections populated | Automated section completeness check | Section-level remediation |

### 6.2 Auditability Requirements

| Requirement | Specification |
|---|---|
| Provenance tracing | Every data point in the output must be traceable to its source document(s) |
| Audit trail | Complete, immutable audit trail for all data transformations per ALCOA+ |
| Version control | All outputs versioned; change history maintained |
| Reproducibility | Pipeline execution must be reproducible given the same inputs and configuration |
| Validation documentation | IQ/OQ/PQ documentation provided per GAMP 5 Category 5 |

### 6.3 Acceptance Process

| Step | Activity | Timeline | Responsible |
|---|---|---|---|
| 6.3.1 | Deliverable submission by ArcaScience | Per milestone schedule | ArcaScience PM |
| 6.3.2 | Client acknowledgment of receipt | Within 2 business days | Client PM |
| 6.3.3 | Client technical review (F1 metrics, data coverage) | 5 business days | Client Data/Analytics Team |
| 6.3.4 | Client clinical review (content accuracy, clinical relevance) | 5 business days | Client Clinical/Regulatory SMEs |
| 6.3.5 | Acceptance decision communicated | Within 10 business days of submission | Client PM |
| 6.3.6 | Remediation (if applicable) | 5 business days per remediation cycle | ArcaScience |
| 6.3.7 | Re-submission and re-review (if applicable) | Per steps 6.3.1 - 6.3.5 | Joint |

### 6.4 Acceptance Outcomes

| Outcome | Definition | Consequence |
|---|---|---|
| Accepted | All acceptance criteria met | Milestone considered complete; payment triggered |
| Conditionally Accepted | Minor issues identified; outputs usable with noted caveats | ArcaScience addresses issues within agreed timeline; milestone provisionally complete |
| Rejected | Major acceptance criteria not met | Remediation cycle initiated; timeline impact assessed; escalation to steering committee |

---

## 7. Platform Outputs to Be Delivered

### 7.1 Output Type Descriptions

#### 7.1.1 Disease Analysis

| Attribute | Detail |
|---|---|
| Description | Comprehensive analysis of the target disease, including epidemiology, pathophysiology, disease burden, current treatment landscape, and unmet medical need |
| SLMs involved | Disease ontology SLM, epidemiology extraction SLM, treatment landscape SLM |
| Key content | Disease prevalence/incidence, natural history, severity classification, comorbidity profile, existing treatments and their limitations |
| Regulatory use | eCTD Module 2.5 (Section 2.5.1 - overview and context); PBRER disease background |
| Typical length | 30 - 60 pages |

#### 7.1.2 Clinical Landscape

| Attribute | Detail |
|---|---|
| Description | Mapping of all relevant clinical evidence including completed and ongoing trials, published literature, and comparative effectiveness data |
| SLMs involved | Trial extraction SLMs, literature analysis SLMs, comparative effectiveness SLM |
| Key content | Trial inventory (completed, ongoing, planned), efficacy outcomes by comparator, safety outcomes by comparator, evidence gaps, competitive landscape |
| Regulatory use | eCTD Module 2.5 (Section 2.5.4 - literature references); BRAT evidence mapping |
| Typical length | 50 - 100 pages + interactive dashboard |

#### 7.1.3 Clinical Endpoint Study

| Attribute | Detail |
|---|---|
| Description | Detailed analysis of clinical endpoints used across the clinical development program, including endpoint selection rationale, measurement properties, and cross-trial comparability |
| SLMs involved | Endpoint extraction SLM, statistical methodology SLM, outcome measurement SLM |
| Key content | Primary/secondary/exploratory endpoint inventory, endpoint definitions, measurement instruments, responder definitions, cross-trial endpoint alignment |
| Regulatory use | eCTD Module 2.5 (Section 2.5.4 - overview of efficacy); ICH E9 alignment |
| Typical length | 20 - 40 pages |

#### 7.1.4 AE Reports

| Attribute | Detail |
|---|---|
| Description | Comprehensive adverse event analysis across all data sources, including incidence, severity, seriousness, causality, and time-to-onset analysis |
| SLMs involved | AE extraction SLMs (3), severity classification SLM, causality assessment SLM, temporal analysis SLM |
| Key content | AE incidence tables, serious AE listing, AE severity distribution, comparative safety analysis, time-to-onset analysis, population subgroup analysis |
| Regulatory use | eCTD Module 2.7.4 (summary of clinical safety); PBRER Section 8-14; CIOMS risk characterization |
| Typical length | 60 - 120 pages |

#### 7.1.5 BRA (Full Benefit-Risk Assessment)

| Attribute | Detail |
|---|---|
| Description | Integrated benefit-risk assessment per BRAT/CIOMS XII framework, combining all evidence into a structured, quantified evaluation |
| SLMs involved | All 24 SLMs contribute; benefit scoring SLM, risk scoring SLM, integration SLM |
| Key content | Benefit-risk framework, key benefit outcomes, key risk outcomes, benefit-risk balance by indication, sensitivity analyses, uncertainty characterization |
| Regulatory use | eCTD Module 2.5 (Section 2.5.6 - benefit-risk conclusions); PBRER Section 16; BRAT framework |
| Typical length | 40 - 80 pages |

#### 7.1.6 BRA Summary

| Attribute | Detail |
|---|---|
| Description | Executive-level summary of the benefit-risk assessment, suitable for regulatory authority communication and internal decision-making |
| SLMs involved | Summary generation SLM, key finding extraction SLM |
| Key content | Benefit-risk conclusion, key benefit drivers, key risk drivers, risk minimization measures, overall recommendation, uncertainty summary |
| Regulatory use | PBRER Section 16 summary; regulatory briefing document |
| Typical length | 5 - 15 pages |

### 7.2 Output Selection Matrix

| Output Type | PoC (Standard) | PoC (Extended) | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|---|
| Disease Analysis | Included | Included | Included | Included | Included |
| Clinical Landscape | Included | Included | Included | Included | Included |
| Clinical Endpoint Study | Optional | Included | Optional | Included | Included |
| AE Reports | Included | Included | Included | Included | Included |
| BRA (Full) | Included | Included | Included | Included | Included |
| BRA Summary | Included | Included | Included | Included | Included |
| Interactive Dashboard | Not included | Optional add-on | Not included | Included | Included |
| Custom Analytics | Not included | Not included | Not included | Optional add-on | Included |

---

## 8. Regulatory Alignment Specifications

### 8.1 eCTD Module 2.5 Alignment

| eCTD Section | BRA Platform Output Mapping | Content Source |
|---|---|---|
| 2.5.1 - Product Overview | Disease Analysis + compound context | Disease Analysis output |
| 2.5.2 - Overview of Quality | Not in scope (CMC) | N/A |
| 2.5.3 - Overview of Non-clinical | Referenced but not primary scope | Literature extraction |
| 2.5.4 - Overview of Clinical | Clinical Landscape + Clinical Endpoint Study | Clinical Landscape + Endpoint Study outputs |
| 2.5.5 - Non-clinical Overview | Not in scope | N/A |
| 2.5.6 - Benefit-Risk Conclusions | BRA (Full) + BRA Summary | BRA + BRA Summary outputs |

### 8.2 PBRER Alignment

| PBRER Section | BRA Platform Output Mapping |
|---|---|
| Section 4 - Worldwide Marketing Approval Status | Not in scope - Client-provided |
| Section 5 - Actions Taken for Safety Reasons | Not in scope - Client-provided |
| Section 6 - Changes to Reference Safety Information | Not in scope - Client-provided |
| Section 7 - Patient Exposure | Derived from Clinical Landscape and AE Reports |
| Section 8 - Presentation of Individual Case Histories | AE Reports (aggregate, not individual case level) |
| Section 9 - Studies | Clinical Landscape |
| Section 10 - Other Clinical Trial Information | Clinical Endpoint Study |
| Section 11 - Literature | Clinical Landscape (literature component) |
| Section 12 - Other Post-Market Experience | AE Reports (post-market data sources) |
| Section 13 - Non-clinical Data | Referenced from literature; not primary scope |
| Section 14 - Literature (published only) | Clinical Landscape |
| Section 15 - Other Information | Disease Analysis (disease context updates) |
| Section 16 - Overall Benefit-Risk Analysis | BRA (Full) + BRA Summary |
| Section 17 - Conclusion | BRA Summary |

### 8.3 BRAT/CIOMS XII Framework Mapping

| BRAT Component | BRA Platform Implementation |
|---|---|
| Define the decision context | Disease Analysis + asset configuration parameters |
| Identify outcomes | Clinical Endpoint Study + AE Reports (outcome identification) |
| Identify and select data sources | Clinical Landscape (evidence inventory) |
| Customize the framework | Asset-specific BRAT tree configured at setup |
| Assess outcome importance | Clinical SME input + ArcaScience scoring algorithm |
| Display key B-R metrics | BRA (Full) - benefit-risk tables and visualizations |
| Interpret and communicate | BRA Summary - executive interpretation |

### 8.4 Ontology Standards

| Ontology | Version | Application | Update Policy |
|---|---|---|---|
| MedDRA | v27.0 | AE coding, indication coding, medical history coding | Updated per MSSO release; version pinned per engagement |
| SNOMED CT | Current International Edition | Clinical concept normalization, procedure coding | Updated per SNOMED International release |
| ChEBI | Current release | Chemical compound normalization, drug substance identification | Updated per EBI release |
| ATC | WHO ATC/DDD 2026 | Drug classification | Updated annually |

---

## 9. Project Governance

### 9.1 Governance Structure

```
Executive Sponsors
(Client VP + ArcaScience CEO)
        |
Steering Committee
(Monthly - strategic decisions)
        |
Working Group
(Weekly - operational execution)
        |
Project Teams
(Daily - task execution)
```

### 9.2 Steering Committee

| Attribute | Detail |
|---|---|
| Purpose | Strategic oversight, risk management, issue escalation, scope change approval |
| Frequency | Monthly (or as needed for escalated issues) |
| Membership | Client: VP Regulatory Affairs or delegate, Head of Pharmacovigilance or delegate; ArcaScience: CEO or delegate, Platform Director |
| Quorum | At least one representative from each party |
| Decision authority | Scope changes, timeline extensions, budget modifications, risk acceptance |
| Minutes | Documented and distributed within 3 business days |

### 9.3 Working Group

| Attribute | Detail |
|---|---|
| Purpose | Operational coordination, progress tracking, issue identification, deliverable review |
| Frequency | Weekly |
| Membership | Client: Project Manager, Clinical Lead, Data Lead; ArcaScience: Project Manager, Clinical Lead, Technical Lead |
| Decision authority | Day-to-day operational decisions within approved scope |
| Minutes | Documented and distributed within 1 business day |

### 9.4 Escalation Path

| Level | Issue Type | Response Time | Escalation To |
|---|---|---|---|
| Level 1 | Operational issue (task delay, minor quality issue) | 1 business day | Working Group leads |
| Level 2 | Project issue (milestone at risk, resource conflict) | 2 business days | Project Managers |
| Level 3 | Strategic issue (scope change, budget impact, timeline risk) | 5 business days | Steering Committee |
| Level 4 | Critical issue (data breach, regulatory non-compliance, safety concern) | 4 hours | Executive Sponsors |

### 9.5 Communication Plan

| Communication | Audience | Frequency | Format | Owner |
|---|---|---|---|---|
| Daily status update | Project teams | Daily (during active phases) | Email or Slack/Teams message | ArcaScience PM |
| Weekly progress report | Working Group | Weekly | Written report + meeting | ArcaScience PM |
| Monthly steering report | Steering Committee | Monthly | Slide deck + meeting | Joint PMs |
| Deliverable notification | Client review team | Per milestone | Email with deliverable package | ArcaScience PM |
| Risk/issue alert | Relevant stakeholders | As needed | Email with escalation form | Identifying party |
| Closeout report | All stakeholders | End of engagement | Written report | ArcaScience PM |

---

## 10. Resource Plan

### 10.1 ArcaScience Team

| Role | Allocation (PoC) | Allocation (Platform) | Responsibilities |
|---|---|---|---|
| Project Manager | 50% for 8 weeks | 25% ongoing | Project planning, status reporting, client communication, issue management |
| Clinical Lead (MD/PharmD) | 30% for 8 weeks | 20% ongoing | Clinical configuration, output review, SME validation, regulatory alignment |
| Data Science Lead | 40% for 8 weeks | 15% ongoing | SLM pipeline configuration, performance monitoring, model optimization |
| Data Engineer | 60% for 8 weeks | 20% ongoing | Data ingestion, pipeline execution, infrastructure management |
| Ontology Specialist | 20% for 8 weeks | 10% ongoing | MedDRA/SNOMED CT/ChEBI mapping, ontology configuration |
| Quality Assurance Analyst | 20% for 8 weeks | 10% ongoing | Validation documentation, QC checks, audit trail verification |
| Regulatory Affairs Specialist | 15% for 8 weeks | 10% ongoing | eCTD/PBRER/BRAT alignment, regulatory template compliance |

### 10.2 Client Team

| Role | Allocation (PoC) | Allocation (Platform) | Responsibilities |
|---|---|---|---|
| Project Manager | 25% for 8 weeks | 15% ongoing | Client-side coordination, acceptance management, internal stakeholder alignment |
| Clinical SME (indication expert) | 15% for 8 weeks | 10% ongoing | Clinical input for configuration, output review, clinical validation |
| Pharmacovigilance Lead | 10% for 8 weeks | 10% ongoing | Safety data validation, AE report review, signal assessment |
| Regulatory Affairs Lead | 10% for 8 weeks | 10% ongoing | Regulatory submission requirements, output format review |
| Data Steward | 20% for weeks 1 - 3 | 10% during ingestion phases | Data package preparation, data quality support, format compliance |
| IT/Security Representative | 5% for week 1 | 5% as needed | Data transfer setup, security review, technical prerequisites |

### 10.3 Resource Escalation

If resource availability issues arise:

1. The affected party notifies the other party's Project Manager within 1 business day
2. Impact assessment provided within 2 business days
3. Mitigation options (substitute resource, timeline adjustment) presented to Working Group
4. If timeline impact exceeds 5 business days, escalation to Steering Committee

---

## 11. Timeline and Phases

### 11.1 PoC Engagement Timeline

#### Phase 1: Setup (Week 1)

| Activity | Duration | Predecessor | Output |
|---|---|---|---|
| 1.1 Project kickoff meeting | Day 1 | Contract execution | Meeting minutes, action items |
| 1.2 Access provisioning (secure upload portal, communication channels) | Day 1 - 2 | 1.1 | Access credentials, channel setup |
| 1.3 Asset configuration specification review | Day 2 - 3 | 1.1 | Approved configuration specification |
| 1.4 Therapeutic area SLM configuration | Day 3 - 5 | 1.3 | Configured SLM ensemble |
| 1.5 Data requirements specification and transfer setup | Day 2 - 4 | 1.1 | Data specification document; transfer mechanism ready |

#### Phase 2: Ingestion (Week 2)

| Activity | Duration | Predecessor | Output |
|---|---|---|---|
| 2.1 Client data package receipt and validation | Day 6 - 7 | 1.5 + client data delivery | Ingestion validation report |
| 2.2 Public data source ingestion (literature, trials, AE databases) | Day 6 - 8 | 1.4 | Public data ingestion report |
| 2.3 Data deduplication and quality assessment | Day 8 - 9 | 2.1, 2.2 | Data quality report |
| 2.4 Data ingestion milestone review | Day 10 | 2.3 | Approved data corpus |

#### Phase 3: Configuration (Week 3)

| Activity | Duration | Predecessor | Output |
|---|---|---|---|
| 3.1 Compound-specific ontology configuration | Day 11 - 12 | 2.4 | Compound dictionary; synonym mapping |
| 3.2 Endpoint library configuration | Day 12 - 13 | 2.4 | Endpoint taxonomy |
| 3.3 Safety profile seeding | Day 13 | 2.4 | Known risk catalog |
| 3.4 Regulatory output template configuration | Day 14 | 1.3 | Configured output templates |
| 3.5 Configuration validation (test run) | Day 14 - 15 | 3.1 - 3.4 | Configuration test report |

#### Phase 4: Validation (Weeks 4 - 5)

| Activity | Duration | Predecessor | Output |
|---|---|---|---|
| 4.1 Full SLM pipeline execution | Day 16 - 20 | 3.5 | Raw extraction results |
| 4.2 Ontology normalization | Day 20 - 22 | 4.1 | Normalized entity database |
| 4.3 Evidence aggregation and cross-source reconciliation | Day 22 - 23 | 4.2 | Aggregated evidence base |
| 4.4 F1 score validation against gold standard | Day 23 - 24 | 4.1, 4.2 | F1 validation report |
| 4.5 Clinical SME review of extraction quality | Day 24 - 25 | 4.4 | Clinical quality assessment |

#### Phase 5: Delivery (Weeks 6 - 8)

| Activity | Duration | Predecessor | Output |
|---|---|---|---|
| 5.1 Output generation (all 6 types) | Day 26 - 30 | 4.3, 4.5 | Draft output package |
| 5.2 Internal QA review | Day 30 - 32 | 5.1 | QA-reviewed output package |
| 5.3 Draft delivery to Client | Day 33 | 5.2 | Draft deliverable package |
| 5.4 Client review period | Day 33 - 37 | 5.3 | Client feedback |
| 5.5 Remediation and finalization | Day 37 - 39 | 5.4 | Final output package |
| 5.6 Final delivery and acceptance review | Day 39 - 40 | 5.5 | Accepted deliverables |
| 5.7 Validation documentation delivery | Day 40 | 5.6 | GAMP 5 validation pack |
| 5.8 Engagement closeout | Day 40 | 5.6, 5.7 | Closeout report |

### 11.2 Platform License Timeline (Year 1 - First Asset)

| Phase | Duration | Key Activities |
|---|---|---|
| Phase 1: Setup | Weeks 1 - 2 | Contract onboarding, platform access, training, first asset configuration |
| Phase 2: Ingestion | Weeks 3 - 4 | Data transfer, public data ingestion, quality validation |
| Phase 3: Configuration | Weeks 5 - 6 | Asset-specific configuration, test runs, configuration validation |
| Phase 4: Validation | Weeks 7 - 8 | Full pipeline execution, F1 validation, clinical review |
| Phase 5: Delivery | Weeks 9 - 12 | Output generation, client review, remediation, acceptance |

Subsequent assets follow a compressed 6 - 8 week cycle leveraging established infrastructure.

---

## 12. Pricing and Payment Schedule

### 12.1 PoC Engagement Pricing

| Component | Price Range | Notes |
|---|---|---|
| Standard PoC (1 asset, 6 outputs, 6 - 8 weeks) | EUR 75,000 - EUR 100,000 | Single indication; standard therapeutic area |
| Extended PoC (1 asset, 6 outputs + enhanced validation) | EUR 100,000 - EUR 150,000 | Complex indication; rare disease; multi-regional |

#### PoC Payment Schedule

| Payment | Amount | Trigger |
|---|---|---|
| Payment 1 - Initiation | 40% of total | Upon SOW execution |
| Payment 2 - Mid-point | 30% of total | Upon completion of Phase 3 (Configuration) and M3 milestone |
| Payment 3 - Completion | 30% of total | Upon formal acceptance of final deliverables (M5 milestone) |

### 12.2 Platform License Pricing

| Tier | Annual Fee (USD) | Assets Included | Outputs | Support Level |
|---|---|---|---|---|
| Tier 1 - Essentials | $75,000 - $100,000/year | 2 assets/year | 5 core outputs | Standard (business hours) |
| Tier 2 - Professional | $125,000 - $175,000/year | 4 assets/year | All 6 outputs + dashboard | Enhanced (extended hours) |
| Tier 3 - Enterprise | $200,000 - $300,000/year | 8 assets/year | All outputs + custom analytics | Premium (24/5) |

#### Platform License Payment Schedule

| Payment | Amount | Trigger |
|---|---|---|
| Payment 1 - Annual license fee | 50% of annual fee | Upon contract execution |
| Payment 2 - Balance | 50% of annual fee | 6 months after contract execution |

### 12.3 Add-On Services

| Add-On | Price Range (USD) | Description |
|---|---|---|
| Additional therapeutic axis | $50,000 - $100,000/year | Expand platform to cover an additional therapeutic area beyond the configured areas |
| Additional assets (beyond tier) | $25,000 - $40,000/asset | Per-asset pricing for assets beyond the tier allowance |
| Expedited delivery | 25% surcharge | Compressed timeline (50% reduction in standard timeline) |
| Custom SLM training | $75,000 - $150,000 | Client-specific SLM fine-tuning with proprietary training data |
| On-site training workshop | $15,000/day | Full-day on-site training for up to 20 participants |
| Enhanced validation package | $25,000 - $50,000 | Extended GAMP 5 documentation, additional IQ/OQ/PQ cycles |

### 12.4 Payment Terms

- All invoices are payable within 30 calendar days of invoice date
- Late payments accrue interest at 1.5% per month
- All prices are exclusive of applicable taxes (VAT, withholding tax, etc.)
- PoC prices quoted in EUR; Platform License prices quoted in USD
- Currency conversions at ECB reference rate on the date of invoice
- Travel and expenses (if applicable) billed at cost with prior approval

---

## 13. Change Order Procedure

### 13.1 Change Order Process

| Step | Activity | Timeline | Responsible |
|---|---|---|---|
| 13.1.1 | Change request submission | Anytime during engagement | Requesting party |
| 13.1.2 | Impact assessment (scope, timeline, cost) | 5 business days | ArcaScience PM (with technical leads) |
| 13.1.3 | Change order proposal preparation | 3 business days after assessment | ArcaScience PM |
| 13.1.4 | Client review and negotiation | 5 business days | Client PM + Steering Committee (if material) |
| 13.1.5 | Change order approval or rejection | Per client decision authority | Client authorized signatory |
| 13.1.6 | Change order execution | Per agreed timeline | Both parties |

### 13.2 Change Order Classification

| Classification | Criteria | Approval Authority |
|---|---|---|
| Minor | No cost impact; timeline impact < 5 business days; no scope change | Project Managers (both parties) |
| Moderate | Cost impact < 15% of SOW value; timeline impact 5 - 15 business days | Working Group leads + ArcaScience Platform Director |
| Major | Cost impact >= 15% of SOW value; timeline impact > 15 business days; material scope change | Steering Committee |

### 13.3 Change Order Template

| Field | Description |
|---|---|
| Change Order ID | Sequential identifier (CO-001, CO-002, etc.) |
| Date submitted | Date of change request |
| Requested by | Name and role of requestor |
| Description of change | Detailed description of the proposed change |
| Rationale | Business or technical justification |
| Impact - Scope | Description of scope additions or removals |
| Impact - Timeline | Estimated impact on project timeline |
| Impact - Cost | Estimated cost impact (additional or reduced) |
| Impact - Risk | Any new risks introduced by the change |
| Recommendation | ArcaScience recommendation (approve, modify, reject) |
| Decision | Approved / Rejected / Deferred |
| Approved by | Name, role, and date of approver |

---

## 14. Intellectual Property Provisions

### 14.1 Pre-Existing IP

| Owner | IP Description | Rights Granted |
|---|---|---|
| ArcaScience | BRA platform, 24 SLMs, extraction algorithms, scoring methodologies, infrastructure architecture, ontology mapping logic | License to use outputs; no transfer of platform IP |
| Client | Source data, clinical study reports, compound-specific information, regulatory submission content | Right to process for the purpose of this SOW only |

### 14.2 Engagement-Generated IP

| IP Type | Ownership | Rights |
|---|---|---|
| Platform outputs (6 output types) | Client | Full ownership upon acceptance and payment; ArcaScience retains no copy |
| Asset-specific configuration files | Joint | ArcaScience may retain de-identified configuration patterns; Client owns asset-specific parameters |
| Aggregate performance metrics (de-identified) | ArcaScience | Used for platform improvement; no client-identifiable information |
| Custom training data (if Client provides) | Client | ArcaScience may use for model improvement only with explicit written consent |
| Methodological improvements | ArcaScience | Platform methodology improvements remain ArcaScience IP |

### 14.3 Restrictions

1. Neither party may reverse-engineer the other party's pre-existing IP
2. Client may not attempt to extract, replicate, or decompile ArcaScience SLMs or algorithms
3. ArcaScience may not use Client data for any purpose other than performing this SOW without written consent
4. All outputs are intended for Client's internal regulatory and business use only; redistribution prohibited without ArcaScience consent
5. ArcaScience may reference the engagement in marketing materials (client name and indication) only with prior written consent

---

## 15. Confidentiality Requirements

### 15.1 Confidential Information Definition

"Confidential Information" means any non-public information disclosed by either party, including but not limited to:

- Clinical data, study results, and regulatory strategies
- Platform architecture, algorithms, and model specifications
- Business terms, pricing, and commercial strategies
- Personnel information and organizational details
- Trade secrets and proprietary methodologies

### 15.2 Obligations

| Obligation | Specification |
|---|---|
| Non-disclosure | Neither party shall disclose Confidential Information to any third party without prior written consent |
| Use restriction | Confidential Information shall be used solely for the purpose of performing this SOW |
| Access limitation | Access limited to personnel with a need-to-know basis; all such personnel bound by confidentiality obligations |
| Standard of care | Each party shall protect Confidential Information with at least the same degree of care used for its own confidential information, but no less than reasonable care |
| Duration | Confidentiality obligations survive termination for a period of 5 years |
| Return/destruction | Upon termination, each party shall return or destroy all Confidential Information upon request; certification of destruction provided within 30 days |

### 15.3 Exceptions

Confidential Information does not include information that:

1. Is or becomes publicly available through no fault of the receiving party
2. Was already known to the receiving party prior to disclosure
3. Is independently developed by the receiving party without use of Confidential Information
4. Is disclosed pursuant to a legal or regulatory requirement (with prompt notice to the disclosing party)

### 15.4 Data Security Measures

| Measure | Implementation |
|---|---|
| Encryption in transit | TLS 1.3 for all data transfers |
| Encryption at rest | AES-256 for all stored data |
| Access control | Role-based access control; multi-factor authentication |
| Audit logging | All data access logged with user identity, timestamp, and action |
| Penetration testing | Annual third-party penetration testing |
| SOC 2 Type II | ArcaScience maintains SOC 2 Type II certification |
| Data residency | Data stored in [EU/US - per client preference] data centers |

---

## 16. Warranty and Support

### 16.1 Warranty

| Warranty | Duration | Scope |
|---|---|---|
| Output accuracy warranty | 90 days from acceptance | Outputs will meet the F1 thresholds specified in Section 6 when re-validated against the same gold standard |
| Completeness warranty | 90 days from acceptance | Outputs will contain all required sections as specified in Section 7 |
| Compliance warranty | 90 days from acceptance | Outputs will conform to the regulatory alignment specifications in Section 8 |
| Platform availability warranty (license only) | Duration of license term | 99.9% uptime measured monthly (excluding scheduled maintenance) |

### 16.2 Warranty Remediation

If a warranty claim is validated:

1. ArcaScience will remediate the deficiency at no additional cost
2. Remediation will commence within 5 business days of validated claim
3. Remediation timeline agreed on a case-by-case basis, not to exceed 15 business days
4. If remediation is not achievable, a pro-rata credit will be issued

### 16.3 Support Tiers (Platform License Only)

| Support Level | Standard (Tier 1) | Enhanced (Tier 2) | Premium (Tier 3) |
|---|---|---|---|
| Hours | Monday - Friday, 9:00 - 18:00 CET | Monday - Friday, 7:00 - 22:00 CET | Monday - Friday, 24 hours |
| Response time - Critical | 4 hours | 2 hours | 1 hour |
| Response time - High | 8 hours | 4 hours | 2 hours |
| Response time - Medium | 2 business days | 1 business day | 4 hours |
| Response time - Low | 5 business days | 3 business days | 1 business day |
| Named support contacts | 1 | 2 | 3 |
| Quarterly business review | No | Yes | Yes |
| Dedicated account manager | No | No | Yes |
| Platform update priority | Standard release cycle | Early access to updates | Priority access + input on roadmap |

### 16.4 Issue Severity Classification

| Severity | Definition | Example |
|---|---|---|
| Critical | Platform unavailable or outputs contain errors impacting patient safety determinations | Systematic AE misclassification; platform outage during submission deadline |
| High | Major feature unavailable or significant accuracy degradation | F1 score drop below threshold; output generation failure for one output type |
| Medium | Minor feature issue or cosmetic defect with workaround available | Formatting issue in output; non-critical field mapping error |
| Low | Enhancement request or minor inconvenience | UI improvement suggestion; documentation clarification |

---

## 17. Termination Provisions

### 17.1 Termination for Convenience

Either party may terminate this SOW by providing 30 calendar days' written notice to the other party.

**Financial implications:**

| Termination Timing | Client Obligation | ArcaScience Obligation |
|---|---|---|
| Before Phase 2 start | Payment 1 retained by ArcaScience | Deliver all work completed to date |
| During Phase 2 or 3 | Payment 1 retained; Payment 2 pro-rated | Deliver all work completed to date |
| During Phase 4 or 5 | Payments 1 and 2 retained; Payment 3 pro-rated | Deliver all work completed to date; complete in-progress outputs |
| Platform License (mid-term) | Remaining balance of current payment period | Continue service through paid period; transition assistance |

### 17.2 Termination for Cause

Either party may terminate immediately upon written notice if the other party:

1. Commits a material breach that remains uncured for 30 calendar days after written notice
2. Becomes subject to bankruptcy, insolvency, or similar proceedings
3. Is found to be in violation of applicable laws or regulations
4. Commits a data breach involving the other party's Confidential Information

### 17.3 Effect of Termination

Upon termination:

1. ArcaScience will deliver all completed and in-progress work products within 15 business days
2. Client will pay all fees due for work completed up to the termination date
3. Each party will return or destroy the other party's Confidential Information per Section 15
4. ArcaScience will securely delete all Client data from its systems within 30 calendar days and provide a certification of deletion
5. Survival clauses: Sections 14 (IP), 15 (Confidentiality), 16 (Warranty - for accepted deliverables), and this Section 17 survive termination

### 17.4 Transition Assistance

Upon termination of a Platform License agreement, ArcaScience will provide the following transition assistance for up to 30 calendar days:

| Activity | Description | Included |
|---|---|---|
| Data export | Export all Client data in structured formats (JSON, CSV, XML) | Yes - at no additional cost |
| Output archive | Provide complete archive of all generated outputs and audit trails | Yes - at no additional cost |
| Knowledge transfer | Up to 3 sessions (2 hours each) to transfer operational knowledge to Client or successor | Yes - at no additional cost |
| Extended access | Continued read-only platform access during transition period | Yes - at no additional cost |
| Custom data migration | Migration of data to Client-designated system | At cost - quoted separately |

---

## 18. Signature Block

### 18.1 Agreement Execution

By signing below, the authorized representatives of both parties agree to the terms and conditions set forth in this Statement of Work.

---

**ArcaScience SAS**

| Field | Detail |
|---|---|
| Name | ________________________________ |
| Title | ________________________________ |
| Signature | ________________________________ |
| Date | ____/____/________ |

---

**[Client Legal Entity Name]**

| Field | Detail |
|---|---|
| Name | ________________________________ |
| Title | ________________________________ |
| Signature | ________________________________ |
| Date | ____/____/________ |

---

### 18.2 Witness (if required by Client policy)

| Field | ArcaScience Witness | Client Witness |
|---|---|---|
| Name | ________________________________ | ________________________________ |
| Title | ________________________________ | ________________________________ |
| Signature | ________________________________ | ________________________________ |
| Date | ____/____/________ | ____/____/________ |

---

## Appendix A: Document Control

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | 2026-03-25 | ArcaScience Commercial & Delivery Team | Initial template release |

---

## Appendix B: Referenced Documents

| Document ID | Title | Relevance |
|---|---|---|
| ARC-RA-2026-001 | BRA Platform Risk Assessment (ICH Q9 Aligned) | Risk context for engagement planning |
| ARC-VAL-2026-001 | BRA Platform GAMP 5 Validation Master Plan | Validation framework for deliverables |
| ARC-SOP-2026-001 | BRA Platform Standard Operating Procedures | Operational procedures for platform use |
| ARC-DPA-TPL-001 | Data Processing Agreement Template | GDPR-compliant data processing terms |
| ARC-MSA-TPL-001 | Master Services Agreement Template | Overarching contractual framework |

---

## Appendix C: Glossary

| Term | Definition |
|---|---|
| AE | Adverse Event |
| ALCOA+ | Attributable, Legible, Contemporaneous, Original, Accurate + Complete, Consistent, Enduring, Available |
| BRA | Benefit-Risk Assessment |
| BRAT | Benefit-Risk Action Team (framework) |
| ChEBI | Chemical Entities of Biological Interest |
| CIOMS | Council for International Organizations of Medical Sciences |
| CRO | Contract Research Organization |
| CSR | Clinical Study Report |
| eCTD | Electronic Common Technical Document |
| F1 Score | Harmonic mean of precision and recall |
| GAMP | Good Automated Manufacturing Practice |
| ICSR | Individual Case Safety Report |
| MedDRA | Medical Dictionary for Regulatory Activities |
| PBRER | Periodic Benefit-Risk Evaluation Report |
| PoC | Proof of Concept |
| RPN | Risk Priority Number |
| SLM | Small Language Model |
| SNOMED CT | Systematized Nomenclature of Medicine - Clinical Terms |
| SOW | Statement of Work |

---

*This document is a template and must be customized for each specific engagement. All bracketed fields must be completed before execution. This document is the property of ArcaScience and contains confidential information. Unauthorized reproduction or distribution is prohibited.*
