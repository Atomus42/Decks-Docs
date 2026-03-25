# ArcaScience BRA Platform - Risk Assessment (ICH Q9 Aligned)

| Field | Detail |
|---|---|
| Document ID | ARC-RA-2026-001 |
| Version | 1.0 |
| Effective Date | 2026-03-25 |
| Classification | Confidential |
| Author | ArcaScience Quality & Compliance Team |
| Regulatory Framework | ICH Q9(R1), GAMP 5, 21 CFR Part 11, EU Annex 11 |
| Platform | BRA (Benefit-Risk Assessment) |
| Review Cycle | Annual or upon significant change |
| Status | Draft - Pending Approval |

---

## Table of Contents

1. Purpose and Scope
2. Risk Assessment Methodology
3. Risk Categories for BRA Platform Deployment
4. Risk Scoring Matrix
5. Detailed Risk Register
6. Risk Control Measures
7. Residual Risk Evaluation
8. Risk Acceptance Criteria
9. Risk Communication Plan
10. Risk Review Schedule
11. FMEA Table for the SLM Pipeline
12. Roles and Responsibilities
13. Approval Signatures

---

## 1. Purpose and Scope

### 1.1 Purpose

This document establishes the formal risk assessment framework for ArcaScience's BRA (Benefit-Risk Assessment) platform in the context of big pharma client engagements. The assessment follows ICH Q9(R1) principles to systematically identify, analyze, evaluate, and control risks associated with the deployment, operation, and ongoing use of the BRA platform across regulated pharmaceutical environments.

The BRA platform leverages 24 specialized Small Language Models (SLMs), clinician-trained on over 10 million adverse event reports, 500,000+ clinical trials, 2 million+ scientific abstracts, and 100,000+ regulatory documents. Given the regulated nature of the outputs - which directly inform regulatory submissions, benefit-risk determinations, and patient safety decisions - a rigorous, documented risk management process is essential.

### 1.2 Scope

This risk assessment covers:

- All six BRA platform output types: Disease Analysis, Clinical Landscape, Clinical Endpoint Study, AE Reports, BRA, and BRA Summary
- The full SLM extraction and inference pipeline (24 models)
- Ontology normalization layers (MedDRA v27.0, SNOMED CT, ChEBI)
- Infrastructure components (Apache Airflow, S3, ElasticSearch, DocumentDB, QDrant, FastAPI, NestJS)
- Data ingestion, transformation, and delivery workflows
- Regulatory compliance mechanisms (FDA 21 CFR Part 11, EU Annex 11, GAMP 5 Category 5)
- Client-facing deliverables aligned to eCTD Module 2.5, PBRER, and BRAT/CIOMS XII frameworks
- Human factors associated with platform operation and output interpretation
- Change management processes for model updates, ontology version changes, and infrastructure modifications

### 1.3 Applicable Standards and Regulations

| Standard | Applicability |
|---|---|
| ICH Q9(R1) | Primary risk management framework |
| GAMP 5 (Category 5) | Software lifecycle and validation |
| FDA 21 CFR Part 11 | Electronic records and signatures |
| EU Annex 11 | Computerized systems in GxP |
| ICH E2E | Pharmacovigilance planning |
| ICH M4 | eCTD structure and content |
| CIOMS XII | Benefit-risk balance framework |
| ALCOA+ | Data integrity principles |
| ISO 14971 | Risk management (referenced methodology) |

### 1.4 Definitions

| Term | Definition |
|---|---|
| BRA | Benefit-Risk Assessment - the core platform product |
| SLM | Small Language Model - specialized AI model for a specific extraction or inference task |
| RPN | Risk Priority Number - composite risk score (Severity x Probability x Detectability) |
| FMEA | Failure Mode and Effects Analysis |
| AE | Adverse Event |
| F1 Score | Harmonic mean of precision and recall, used as primary accuracy metric |
| MedDRA | Medical Dictionary for Regulatory Activities |
| SNOMED CT | Systematized Nomenclature of Medicine - Clinical Terms |
| ChEBI | Chemical Entities of Biological Interest |
| ALCOA+ | Attributable, Legible, Contemporaneous, Original, Accurate + Complete, Consistent, Enduring, Available |

---

## 2. Risk Assessment Methodology

### 2.1 Overview

The risk assessment methodology follows the ICH Q9(R1) quality risk management process:

```
Risk Identification
        |
        v
Risk Analysis (estimate severity, probability, detectability)
        |
        v
Risk Evaluation (compare against acceptance criteria)
        |
        v
Risk Control (reduce or accept)
        |
        v
Risk Review (periodic reassessment)
        |
        v
Risk Communication (stakeholder reporting)
```

### 2.2 Risk Identification

Risk identification is conducted through the following methods:

1. **Hazard Analysis** - Systematic review of each platform component, data flow, and output type to identify potential failure modes
2. **Historical Incident Review** - Analysis of prior engagement data (50+ regulatory submissions across 12 therapeutic areas) to identify recurring failure patterns
3. **Regulatory Gap Analysis** - Comparison of platform capabilities against current regulatory expectations (FDA, EMA, PMDA)
4. **Stakeholder Consultation** - Input from clinical subject matter experts, data engineers, regulatory affairs specialists, and client pharmacovigilance teams
5. **FMEA** - Structured failure mode analysis for the SLM pipeline (see Section 11)

### 2.3 Risk Analysis

Each identified risk is analyzed across three dimensions:

- **Severity (S)** - The potential impact if the risk materializes
- **Probability (P)** - The likelihood of the risk event occurring
- **Detectability (D)** - The ability to detect the failure before it reaches the end user or regulatory authority

These three dimensions are combined to produce a Risk Priority Number (RPN):

**RPN = Severity x Probability x Detectability**

### 2.4 Risk Evaluation

Evaluated risks are classified into three action categories based on RPN thresholds:

| RPN Range | Classification | Required Action |
|---|---|---|
| 1 - 49 | Low | Accept with monitoring; document in risk register |
| 50 - 99 | Medium | Implement risk reduction measures; verify effectiveness |
| 100 - 125 | High | Mandatory risk mitigation before deployment; escalate to steering committee |

### 2.5 Risk Control

Risk control strategies follow the hierarchy:

1. **Elimination** - Remove the source of risk entirely
2. **Reduction** - Implement controls to lower severity, probability, or improve detectability
3. **Acceptance** - Accept residual risk with documented justification and monitoring plan

### 2.6 Risk Review

All risks are reviewed:

- On a scheduled annual basis
- Upon any significant change (model update, ontology version change, infrastructure modification)
- Following any quality event, deviation, or client-reported issue
- At each phase gate during client engagements

---

## 3. Risk Categories for BRA Platform Deployment

### 3.1 Data Integrity Risks

Risks related to the completeness, accuracy, and trustworthiness of data throughout its lifecycle within the platform. These risks are evaluated against ALCOA+ principles.

**Sub-categories:**

- Source data corruption during ingestion
- Unauthorized modification of processed records
- Incomplete audit trail coverage
- Loss of data attributability during transformation
- Failure to maintain contemporaneous records
- Backup and recovery integrity gaps

### 3.2 Extraction Accuracy Risks (Per SLM Module)

Risks associated with the performance of each of the 24 SLMs in extracting, classifying, and inferring clinical and regulatory information.

**Sub-categories:**

- AE extraction precision/recall degradation (baseline F1: 92%)
- Biomarker extraction errors (baseline F1: 90%)
- Risk signal classification failures (baseline F1: 88%)
- Benefit claim extraction errors (baseline F1: 92%)
- Entity relationship extraction inaccuracies
- Temporal relationship misattribution
- Dose-response extraction failures
- Population subgroup misclassification
- Cross-language extraction degradation

### 3.3 Ontology Mapping Risks

Risks related to the normalization of extracted entities to controlled terminologies.

**Sub-categories:**

- MedDRA v27.0 Preferred Term (PT) misassignment
- SNOMED CT concept mapping failures
- ChEBI compound normalization errors
- Ontology version mismatch between ingestion and reporting
- Ambiguous term resolution failures
- Missing mappings for novel entities

### 3.4 Infrastructure and Availability Risks

Risks related to the technical infrastructure that supports the platform.

**Sub-categories:**

- Apache Airflow DAG execution failures
- S3 storage availability or data loss
- ElasticSearch index corruption or query failures
- DocumentDB connection failures or data inconsistency
- QDrant vector store degradation
- FastAPI/NestJS service outages
- Network latency affecting real-time processing
- Scaling limitations under high-volume ingestion

### 3.5 Regulatory Compliance Risks

Risks related to maintaining compliance with applicable regulations and standards.

**Sub-categories:**

- 21 CFR Part 11 electronic signature non-compliance
- EU Annex 11 validation documentation gaps
- eCTD Module 2.5 formatting deviations
- PBRER content misalignment
- BRAT/CIOMS XII framework adherence failures
- Audit trail insufficiency for regulatory inspection
- GAMP 5 Category 5 validation lifecycle gaps

### 3.6 Data Privacy Risks

Risks related to the protection of patient data and proprietary client information.

**Sub-categories:**

- Patient re-identification from aggregated AE data
- Unauthorized access to client proprietary trial data
- Cross-client data leakage in multi-tenant environments
- GDPR/HIPAA non-compliance in data handling
- Data residency violations

### 3.7 Change-Related Risks

Risks arising from modifications to the platform, its components, or operating environment.

**Sub-categories:**

- SLM model retraining introducing performance regression
- Ontology version upgrade breaking existing mappings
- Infrastructure component upgrade causing service disruption
- Client-requested configuration changes introducing errors
- Regulatory requirement changes rendering outputs non-compliant

### 3.8 Human Factor Risks

Risks associated with human interaction with the platform and its outputs.

**Sub-categories:**

- Misinterpretation of BRA outputs by client regulatory teams
- Incorrect data preparation by client data stewards
- Over-reliance on automated risk signals without clinical review
- Inadequate training on platform capabilities and limitations
- Configuration errors during asset-specific setup

---

## 4. Risk Scoring Matrix

### 4.1 Severity Scale

| Score | Level | Description | Example |
|---|---|---|---|
| 1 | Negligible | No impact on output quality or compliance; cosmetic issue only | Minor formatting inconsistency in a non-critical field |
| 2 | Minor | Slight impact on output quality; easily correctable; no regulatory consequence | Synonym variant used instead of preferred MedDRA PT |
| 3 | Moderate | Measurable impact on output accuracy; requires rework; potential regulatory query | AE severity grade misclassified for a non-critical event |
| 4 | Major | Significant impact on output reliability; potential regulatory non-compliance; delay to submission | Critical safety signal missed in initial extraction |
| 5 | Critical | Direct patient safety implication; regulatory rejection; loss of data integrity | Systematic misclassification of serious AEs as non-serious |

### 4.2 Probability Scale

| Score | Level | Description | Estimated Frequency |
|---|---|---|---|
| 1 | Rare | Unlikely to occur in normal operation | Less than once per 100 engagements |
| 2 | Unlikely | Could occur but not expected | Once per 50 - 100 engagements |
| 3 | Possible | May occur under certain conditions | Once per 10 - 50 engagements |
| 4 | Likely | Expected to occur in some engagements | Once per 2 - 10 engagements |
| 5 | Almost Certain | Expected to occur in most engagements without controls | More than once per engagement |

### 4.3 Detectability Scale

| Score | Level | Description | Detection Mechanism |
|---|---|---|---|
| 1 | Almost Certain | Failure is detected automatically before output delivery | Automated validation with hard-stop rules |
| 2 | High | Failure is detected during standard QC review | Automated flagging with human review step |
| 3 | Moderate | Failure may be detected during expert review | Requires subject matter expert evaluation |
| 4 | Low | Failure is unlikely to be detected before delivery | Detected only through post-delivery audit or client feedback |
| 5 | Undetectable | Failure cannot be detected by current controls | No existing detection mechanism |

### 4.4 RPN Calculation Matrix (Example Cross-Reference)

| Severity | Probability | Detectability | RPN | Classification |
|---|---|---|---|---|
| 5 | 5 | 5 | 125 | High |
| 5 | 4 | 5 | 100 | High |
| 4 | 4 | 4 | 64 | Medium |
| 3 | 3 | 3 | 27 | Low |
| 2 | 2 | 2 | 8 | Low |
| 1 | 1 | 1 | 1 | Low |
| 5 | 2 | 5 | 50 | Medium |
| 4 | 5 | 3 | 60 | Medium |
| 5 | 3 | 4 | 60 | Medium |

---

## 5. Detailed Risk Register

### Risk Register Table

| ID | Category | Risk Description | S | P | D | RPN | Class | Control Measure | Residual RPN |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | Data Integrity | Source data corruption during file ingestion (truncated files, encoding errors) leading to incomplete AE extraction | 4 | 3 | 2 | 24 | Low | Automated checksum validation on ingestion; file integrity verification DAG step; rejection of malformed inputs | 8 |
| R-002 | Data Integrity | Unauthorized modification of processed records in DocumentDB bypassing audit trail | 5 | 2 | 2 | 20 | Low | Role-based access control; database-level audit logging; ALCOA+ compliance checks; 21 CFR Part 11 electronic signatures | 10 |
| R-003 | Data Integrity | Incomplete audit trail for data transformations between SLM pipeline stages | 5 | 3 | 3 | 45 | Low | End-to-end provenance tracking via Airflow metadata; immutable S3 versioning; audit trail completeness validation | 15 |
| R-004 | Data Integrity | Loss of data attributability when aggregating multi-source AE reports | 4 | 3 | 3 | 36 | Low | Source tagging at record level; persistent source identifiers through all pipeline stages; attributability audit | 12 |
| R-005 | Extraction Accuracy | AE extraction F1 score drops below 92% threshold due to novel terminology or atypical report formats | 5 | 3 | 2 | 30 | Low | Continuous F1 monitoring per engagement; automated performance alerts at 90% threshold; fallback to manual review queue | 10 |
| R-006 | Extraction Accuracy | Biomarker extraction SLM produces false positives, linking irrelevant biomarkers to disease endpoints | 4 | 3 | 3 | 36 | Low | Confidence scoring with threshold filtering; clinical SME review of biomarker-endpoint associations; gold standard benchmarking | 12 |
| R-007 | Extraction Accuracy | Risk signal classification SLM (F1 88%) fails to identify emerging safety signals in post-market data | 5 | 3 | 4 | 60 | Medium | Dual-model consensus requirement for critical risk signals; mandatory pharmacovigilance expert review; signal escalation protocol | 20 |
| R-008 | Extraction Accuracy | Benefit extraction model attributes benefits from comparator arm to investigational product | 5 | 2 | 3 | 30 | Low | Arm-level extraction validation; cross-reference with structured trial data; clinical reviewer sign-off | 10 |
| R-009 | Extraction Accuracy | Temporal relationship misattribution - AEs assigned to wrong treatment period | 4 | 3 | 3 | 36 | Low | Timeline validation against study protocol dates; temporal consistency checks; anomaly flagging | 12 |
| R-010 | Extraction Accuracy | Population subgroup misclassification leading to incorrect stratified risk estimates | 4 | 3 | 4 | 48 | Low | Demographic validation rules; cross-check with enrollment data; stratification QC step | 16 |
| R-011 | Ontology Mapping | MedDRA PT misassignment - adverse event mapped to incorrect Preferred Term | 4 | 3 | 2 | 24 | Low | Multi-level MedDRA validation (LLT to PT to HLT); confidence threshold enforcement; mapping audit log | 8 |
| R-012 | Ontology Mapping | MedDRA version mismatch between ingestion and reporting phases causes inconsistent coding | 4 | 2 | 2 | 16 | Low | Version pinning per engagement; version compatibility check at report generation; migration validation for version updates | 8 |
| R-013 | Ontology Mapping | ChEBI normalization failure for novel compounds not yet in the ontology | 3 | 3 | 3 | 27 | Low | Unmapped entity flagging; manual curation queue; client-provided compound dictionary as fallback | 9 |
| R-014 | Ontology Mapping | SNOMED CT concept mapping produces clinically inappropriate mappings for rare conditions | 4 | 3 | 3 | 36 | Low | Therapeutic area-specific mapping validation; clinical SME review for rare disease engagements; mapping confidence scoring | 12 |
| R-015 | Infrastructure | Apache Airflow DAG failure during critical batch processing, causing incomplete pipeline execution | 4 | 3 | 1 | 12 | Low | Airflow task retry logic (3 retries with exponential backoff); DAG failure alerting; checkpoint-based recovery | 4 |
| R-016 | Infrastructure | S3 data loss or unavailability during peak ingestion period | 5 | 1 | 1 | 5 | Low | Multi-AZ replication; versioned buckets; cross-region backup; RPO < 1 hour; automated failover | 5 |
| R-017 | Infrastructure | ElasticSearch index corruption leading to incomplete search results in Clinical Landscape output | 4 | 2 | 2 | 16 | Low | Index snapshot schedule; index health monitoring; automated reindex from source of truth; query result count validation | 8 |
| R-018 | Infrastructure | QDrant vector store degradation causing poor semantic similarity matching for evidence retrieval | 3 | 2 | 3 | 18 | Low | Vector store health monitoring; periodic re-indexing; similarity score threshold alerting; fallback to keyword search | 9 |
| R-019 | Regulatory Compliance | Platform outputs fail eCTD Module 2.5 structural requirements, causing submission rejection | 5 | 2 | 2 | 20 | Low | eCTD template validation engine; pre-submission structural check; regulatory affairs review gate | 10 |
| R-020 | Regulatory Compliance | PBRER content misalignment - missing required sections or incorrect data period coverage | 5 | 2 | 2 | 20 | Low | PBRER section completeness checker; data period validation; regulatory template enforcement | 10 |
| R-021 | Regulatory Compliance | 21 CFR Part 11 non-compliance - electronic signature implementation gap discovered during audit | 5 | 2 | 3 | 30 | Low | Annual Part 11 compliance audit; signature workflow validation; audit trail integrity testing | 15 |
| R-022 | Data Privacy | Patient re-identification from aggregated AE data in Disease Analysis output | 5 | 2 | 4 | 40 | Low | K-anonymity enforcement (k>=5); data minimization at ingestion; re-identification risk assessment per output; privacy impact assessment | 15 |
| R-023 | Data Privacy | Cross-client data leakage in multi-tenant infrastructure configuration | 5 | 2 | 2 | 20 | Low | Tenant isolation at storage, compute, and network levels; penetration testing; data segregation audit; access logging | 10 |
| R-024 | Change-Related | SLM model retraining introduces performance regression below validated thresholds | 4 | 3 | 2 | 24 | Low | Pre-deployment validation against gold standard datasets; A/B performance comparison; rollback procedure; change control board approval | 8 |
| R-025 | Change-Related | Ontology version upgrade (e.g., MedDRA v27.0 to v28.0) breaks existing mappings for active engagements | 4 | 3 | 2 | 24 | Low | Impact analysis before upgrade; parallel version support during transition; mapping migration validation; client notification protocol | 8 |
| R-026 | Change-Related | Regulatory requirement change renders existing output templates non-compliant | 4 | 2 | 3 | 24 | Low | Regulatory intelligence monitoring; quarterly compliance review; template update procedure; retroactive impact assessment | 12 |
| R-027 | Human Factor | Client regulatory team misinterprets BRA Summary output, leading to incorrect submission content | 5 | 3 | 4 | 60 | Medium | Mandatory output interpretation training; output confidence indicators; disclaimers on automated sections; joint review sessions | 20 |
| R-028 | Human Factor | Client data stewards provide incorrectly formatted or incomplete source data | 3 | 4 | 2 | 24 | Low | Data specification document; automated format validation; ingestion rejection with actionable error messages; data readiness checklist | 8 |
| R-029 | Human Factor | Over-reliance on automated risk signals without adequate clinical pharmacovigilance review | 5 | 3 | 4 | 60 | Medium | Mandatory human-in-the-loop for all safety-critical outputs; clear labeling of AI-generated vs. human-reviewed content; sign-off workflow | 20 |
| R-030 | Human Factor | Configuration errors during asset-specific BRA setup leading to incorrect therapeutic context | 4 | 3 | 2 | 24 | Low | Configuration validation checklist; dual-review for setup parameters; configuration audit trail; test run before production | 8 |

---

## 6. Risk Control Measures

### 6.1 Data Integrity Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-001 | Automated checksum validation on all ingested files | SHA-256 checksum computed at upload and verified post-transfer in Airflow DAG | Ingestion test suite; monthly integrity audit |
| C-002 | Immutable S3 object versioning with write-once policy | S3 Object Lock in compliance mode; versioning enabled on all buckets | AWS configuration audit; deletion attempt testing |
| C-003 | End-to-end provenance tracking | Airflow XCom metadata propagation; unique trace ID per document through pipeline | Provenance chain validation test; random sample audit |
| C-004 | ALCOA+ compliance enforcement | Automated ALCOA+ checklist validation at each pipeline stage; timestamps, user attribution, and change logging | Quarterly ALCOA+ audit; regulatory inspection readiness check |
| C-005 | Role-based access control with least privilege | NestJS RBAC middleware; DocumentDB role-based permissions; S3 bucket policies | Access review quarterly; penetration testing annually |

### 6.2 Extraction Accuracy Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-006 | Continuous F1 monitoring per SLM per engagement | Real-time F1 scoring against engagement-specific gold standard subset | Performance dashboard; threshold breach alerting |
| C-007 | Confidence score thresholding | All SLM outputs include confidence scores; outputs below threshold routed to manual review | Threshold calibration testing; false negative rate monitoring |
| C-008 | Dual-model consensus for safety-critical extractions | Risk and AE extraction validated by two independent SLMs; disagreements flagged | Consensus rate monitoring; disagreement root cause analysis |
| C-009 | Clinical SME review gate for high-impact outputs | BRA and BRA Summary outputs require clinical pharmacologist sign-off | Sign-off audit trail; reviewer qualification verification |
| C-010 | Gold standard benchmarking per therapeutic area | Curated benchmark datasets for each of 12 therapeutic areas; performance tested before engagement | Benchmark test reports; performance trend analysis |

### 6.3 Ontology Mapping Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-011 | Multi-level MedDRA validation | LLT-to-PT-to-HLT hierarchy validation; cross-check against MedDRA browser | Mapping accuracy audit; hierarchy consistency check |
| C-012 | Version pinning per engagement | Ontology version locked at engagement start; documented in configuration | Configuration audit; version consistency check across outputs |
| C-013 | Unmapped entity escalation | Entities without ontology mapping flagged and routed to curation queue | Unmapped entity rate monitoring; curation turnaround time tracking |
| C-014 | Client-provided dictionary integration | Custom compound and indication dictionaries ingested and validated at setup | Dictionary coverage testing; mapping completeness report |

### 6.4 Infrastructure Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-015 | Airflow task retry with exponential backoff | 3 automatic retries; backoff factor 2; dead-letter queue for persistent failures | Retry rate monitoring; failure root cause log |
| C-016 | Multi-AZ storage replication | S3 cross-AZ replication; DocumentDB replica set; ElasticSearch multi-node cluster | Failover testing quarterly; RPO/RTO validation |
| C-017 | Health monitoring and alerting | Prometheus/Grafana monitoring for all services; PagerDuty escalation | Uptime SLA tracking; alert response time audit |
| C-018 | Capacity planning and auto-scaling | Load-tested capacity models; auto-scaling policies for FastAPI and NestJS services | Load testing quarterly; capacity utilization review |

### 6.5 Regulatory Compliance Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-019 | eCTD template validation engine | Automated structural validation against eCTD v4.0 schema before output generation | Template validation test suite; submission dry-run |
| C-020 | 21 CFR Part 11 compliance framework | Electronic signatures, audit trails, system access controls, and validation documentation | Annual Part 11 audit; mock FDA inspection |
| C-021 | PBRER section completeness checker | Rule-based validation of all mandatory PBRER sections against ICH E2C(R2) | Completeness test suite; regulatory affairs review |
| C-022 | GAMP 5 validation lifecycle | IQ/OQ/PQ documentation; traceability matrix; periodic review | Validation status dashboard; periodic review schedule |

### 6.6 Data Privacy Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-023 | K-anonymity enforcement | Minimum k=5 for all aggregated patient data outputs; suppression of small-count cells | Re-identification risk assessment; privacy audit |
| C-024 | Tenant isolation | Dedicated storage namespaces; network segmentation; compute isolation per client | Penetration testing; isolation verification testing |
| C-025 | Data minimization at ingestion | Only required data fields ingested; PII stripped at earliest pipeline stage | Data inventory audit; PII scanning |

### 6.7 Change-Related Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-026 | Change control board (CCB) review | All model updates, ontology changes, and infrastructure modifications require CCB approval | CCB meeting minutes; change request log |
| C-027 | Pre-deployment validation testing | Gold standard regression testing before any production deployment | Test report review; go/no-go decision documentation |
| C-028 | Rollback procedure | Documented rollback for all deployable components; tested quarterly | Rollback drill results; recovery time validation |

### 6.8 Human Factor Controls

| Control ID | Control Description | Implementation | Verification Method |
|---|---|---|---|
| C-029 | Mandatory platform training | All client users complete training program before accessing outputs; certification tracked | Training completion records; competency assessment |
| C-030 | Human-in-the-loop for safety-critical outputs | All BRA and AE Report outputs require human review and sign-off before delivery | Sign-off audit trail; reviewer qualification records |
| C-031 | Output confidence labeling | All AI-generated content clearly labeled with confidence scores and methodology notes | Output format audit; user comprehension testing |
| C-032 | Configuration dual-review | Asset-specific configuration requires review by two qualified personnel | Configuration review records; error rate tracking |

---

## 7. Residual Risk Evaluation

### 7.1 Residual Risk Summary

After implementation of all control measures, the residual risk profile is as follows:

| Risk Classification | Count (Pre-Control) | Count (Post-Control) | Trend |
|---|---|---|---|
| High (RPN 100 - 125) | 0 | 0 | Stable |
| Medium (RPN 50 - 99) | 3 | 0 | Improved |
| Low (RPN 1 - 49) | 27 | 30 | Stable |

### 7.2 Residual Risk Distribution by Category

| Category | Average Pre-Control RPN | Average Post-Control RPN | Reduction % |
|---|---|---|---|
| Data Integrity | 31.3 | 11.3 | 63.9% |
| Extraction Accuracy | 40.0 | 13.3 | 66.7% |
| Ontology Mapping | 25.8 | 9.3 | 63.9% |
| Infrastructure | 12.8 | 6.5 | 49.2% |
| Regulatory Compliance | 23.3 | 11.7 | 49.8% |
| Data Privacy | 30.0 | 12.5 | 58.3% |
| Change-Related | 24.0 | 9.3 | 61.1% |
| Human Factor | 42.0 | 14.0 | 66.7% |

### 7.3 Residual Risks Requiring Ongoing Monitoring

The following residual risks remain above RPN 15 after control implementation and require active monitoring:

| ID | Risk Description | Residual RPN | Monitoring Approach |
|---|---|---|---|
| R-007 | Risk signal classification SLM failure to identify emerging safety signals | 20 | Continuous F1 tracking; pharmacovigilance expert review of all outputs |
| R-022 | Patient re-identification from aggregated AE data | 15 | Quarterly privacy impact assessment; re-identification testing |
| R-027 | Client misinterpretation of BRA Summary output | 20 | Post-delivery comprehension check; feedback survey |
| R-029 | Over-reliance on automated risk signals | 20 | Human-in-the-loop compliance monitoring; sign-off rate tracking |
| R-021 | 21 CFR Part 11 compliance gap | 15 | Annual audit; mock inspection readiness |
| R-003 | Incomplete audit trail for data transformations | 15 | Quarterly audit trail completeness review |

---

## 8. Risk Acceptance Criteria

### 8.1 Acceptance Thresholds

| Criterion | Threshold | Rationale |
|---|---|---|
| Maximum acceptable individual residual RPN | 49 (Low classification) | No individual risk may remain in Medium or High classification after controls |
| Maximum acceptable average residual RPN per category | 25 | No risk category may have a disproportionately high residual risk profile |
| Minimum risk reduction percentage | 40% | All control measures must demonstrate meaningful risk reduction |
| Maximum number of risks with residual RPN > 15 | 10 | Limits the active monitoring burden to a manageable number |
| SLM F1 score floor (all modules) | 85% | Below this threshold, the module is taken offline pending investigation |
| Data integrity compliance rate | 99.5% | Measured by ALCOA+ audit pass rate |
| System availability | 99.9% | Measured as monthly uptime for production services |

### 8.2 Acceptance Decision Process

1. Quality Lead compiles residual risk profile
2. All residual RPNs compared against acceptance thresholds
3. Risks exceeding thresholds escalated to Change Control Board
4. CCB determines whether additional controls are required or risk is formally accepted with justification
5. Formal risk acceptance signed by Quality Lead, Platform Director, and Chief Medical Officer
6. Risk acceptance documented in engagement-specific quality record

### 8.3 Conditional Acceptance

For engagements involving novel therapeutic areas or first-in-class compounds where historical benchmarking data is limited:

- F1 score thresholds may be conditionally relaxed to 82% with mandatory enhanced clinical review
- Conditional acceptance must be time-limited (maximum 90 days)
- Enhanced monitoring plan required during conditional acceptance period
- Formal review required at 45-day midpoint

---

## 9. Risk Communication Plan

### 9.1 Internal Communication

| Audience | Content | Frequency | Channel |
|---|---|---|---|
| Platform Engineering Team | Technical risk details, control implementation status, performance metrics | Weekly | Engineering stand-up; risk dashboard |
| Quality & Compliance Team | Full risk register, residual risk profile, audit findings | Bi-weekly | Quality review meeting |
| Clinical SME Team | Extraction accuracy metrics, clinical risk highlights, new therapeutic area risks | Weekly | Clinical review meeting |
| Executive Leadership | Risk summary, high-priority items, resource requirements | Monthly | Executive risk report |

### 9.2 External Communication (Client-Facing)

| Audience | Content | Frequency | Channel |
|---|---|---|---|
| Client Steering Committee | Engagement-specific risk summary, residual risk profile, mitigation status | Monthly | Steering committee meeting |
| Client Pharmacovigilance Team | AE extraction accuracy metrics, safety signal coverage, ontology mapping quality | Per deliverable | Deliverable quality report |
| Client Regulatory Affairs | Compliance status, output validation results, regulatory alignment confirmation | Per submission | Compliance certificate |
| Client IT/Security | Infrastructure security posture, data privacy controls, access management | Quarterly | Security review meeting |

### 9.3 Escalation Protocol

| Level | Trigger | Response Time | Escalation Target |
|---|---|---|---|
| Level 1 - Informational | New risk identified with RPN < 25 | 5 business days | Quality Lead |
| Level 2 - Attention | Risk RPN increases to 25 - 49 or new medium-risk identified | 2 business days | Quality Lead + Platform Director |
| Level 3 - Urgent | Risk RPN exceeds 50 or control failure detected | 4 hours | Platform Director + Chief Medical Officer |
| Level 4 - Critical | Patient safety implication or regulatory non-compliance detected | 1 hour | Executive Leadership + Client Steering Committee |

---

## 10. Risk Review Schedule

### 10.1 Scheduled Reviews

| Review Type | Frequency | Scope | Participants | Output |
|---|---|---|---|---|
| Engagement Risk Review | Per engagement phase gate | Engagement-specific risks | Project Manager, Quality Lead, Clinical Lead | Phase gate risk report |
| Quarterly Risk Review | Every 3 months | Full risk register | Quality Team, Platform Engineering, Clinical SMEs | Updated risk register |
| Annual Risk Assessment | Yearly | Comprehensive reassessment | All stakeholders | Annual risk report |
| Model Performance Review | Monthly | SLM F1 scores, accuracy metrics | Data Science Team, Clinical SMEs | Performance trend report |
| Infrastructure Risk Review | Quarterly | Availability, security, capacity | Platform Engineering, IT Security | Infrastructure risk report |

### 10.2 Triggered Reviews

| Trigger Event | Review Scope | Timeline | Responsible |
|---|---|---|---|
| SLM model retraining or update | Affected extraction accuracy risks | Before deployment | Data Science Lead |
| Ontology version upgrade | All ontology mapping risks | Before activation | Ontology Specialist |
| Infrastructure component change | Affected infrastructure risks | Before deployment | Platform Engineering Lead |
| Client-reported quality issue | Affected risk category | Within 5 business days | Quality Lead |
| Regulatory guidance update | All regulatory compliance risks | Within 30 days | Regulatory Affairs Lead |
| Security incident | Data privacy and integrity risks | Within 24 hours | IT Security Lead |
| New therapeutic area onboarding | Extraction accuracy and ontology risks | Before engagement start | Clinical Lead + Data Science Lead |

---

## 11. FMEA Table for the SLM Pipeline

The following FMEA covers the end-to-end BRA platform SLM pipeline, from source data ingestion through final output delivery.

### 11.1 Pipeline Stage Overview

```
Stage 1: Data Ingestion
    |
Stage 2: Document Preprocessing
    |
Stage 3: Entity Extraction (SLMs 1-8)
    |
Stage 4: Relationship Extraction (SLMs 9-14)
    |
Stage 5: Ontology Normalization
    |
Stage 6: Evidence Aggregation
    |
Stage 7: Benefit-Risk Scoring
    |
Stage 8: Report Generation
    |
Stage 9: Output Validation
    |
Stage 10: Delivery and Audit
```

### 11.2 FMEA Table

| Stage | Step | Failure Mode | Effect | S | P | D | RPN | Current Control | Recommended Action |
|---|---|---|---|---|---|---|---|---|---|
| 1 - Ingestion | File upload from client data package | File corruption during transfer | Incomplete or garbled source data enters pipeline | 4 | 2 | 1 | 8 | SHA-256 checksum validation; file size verification | Maintain current controls |
| 1 - Ingestion | Source format detection (PDF, XML, CSV, DOCX) | Incorrect format detection | Parser applied incorrectly; extraction failures downstream | 3 | 2 | 2 | 12 | Magic byte detection; format-specific parser selection | Add format validation test suite |
| 1 - Ingestion | Data deduplication check | Duplicate records not detected | Inflated AE counts; skewed risk estimates | 4 | 3 | 2 | 24 | Hash-based deduplication; fuzzy matching for near-duplicates | Enhanced fuzzy matching threshold tuning |
| 2 - Preprocessing | Document segmentation (section detection) | Incorrect section boundaries | Entity extraction from wrong context; misattributed data | 4 | 3 | 3 | 36 | Section header pattern matching; layout analysis | Add ML-based section classifier |
| 2 - Preprocessing | OCR for scanned documents | OCR errors in text extraction | Misspelled terms; entity extraction failures | 3 | 3 | 3 | 27 | OCR confidence scoring; low-confidence flagging | Dual OCR engine comparison |
| 2 - Preprocessing | Language detection and routing | Incorrect language assignment | Wrong SLM variant applied; degraded extraction | 4 | 2 | 2 | 16 | Statistical language detection; multi-language fallback | Add language confirmation step |
| 3 - Entity Extraction | Adverse event entity extraction (SLMs 1 - 3) | False negatives - AEs missed | Safety signals omitted from downstream analysis | 5 | 2 | 2 | 20 | F1 monitoring (92% baseline); confidence thresholding | Ensemble model voting for critical AEs |
| 3 - Entity Extraction | Adverse event entity extraction (SLMs 1 - 3) | False positives - non-AEs classified as AEs | Inflated AE counts; false safety signals | 3 | 3 | 2 | 18 | Precision monitoring; clinical review of flagged entities | Negative example augmentation in training |
| 3 - Entity Extraction | Biomarker extraction (SLMs 4 - 5) | Incorrect biomarker identification | Wrong biomarkers linked to endpoints; misleading clinical landscape | 4 | 2 | 3 | 24 | F1 monitoring (90% baseline); biomarker dictionary validation | Expand biomarker reference dictionary |
| 3 - Entity Extraction | Dose-response extraction (SLM 6) | Dose unit conversion errors | Incorrect dose-response relationships | 4 | 2 | 2 | 16 | Unit normalization rules; range validation | Add pharmacist review for novel compounds |
| 3 - Entity Extraction | Population demographics extraction (SLMs 7 - 8) | Age/sex/ethnicity misextraction | Incorrect subgroup risk stratification | 3 | 2 | 3 | 18 | Demographic validation rules; source cross-reference | Structured data preference over free-text extraction |
| 4 - Relationship Extraction | AE-drug causal relationship (SLMs 9 - 10) | Incorrect causality assignment | Wrong drug attributed to AE; distorted risk profile | 5 | 3 | 3 | 45 | Dual-model consensus; clinical reviewer validation | Add temporal plausibility check |
| 4 - Relationship Extraction | Biomarker-endpoint association (SLMs 11 - 12) | Spurious association detected | Misleading evidence in clinical landscape | 3 | 3 | 3 | 27 | Confidence scoring; literature evidence threshold | Add statistical significance filter |
| 4 - Relationship Extraction | Benefit claim extraction (SLMs 13 - 14) | Overstated benefit claims extracted | Inflated benefit profile in BRA | 5 | 2 | 3 | 30 | F1 monitoring (92% baseline); comparative analysis | Add claim strength calibration |
| 5 - Ontology Normalization | MedDRA PT assignment | Wrong PT assigned to extracted AE | Incorrect AE coding in regulatory reports | 4 | 3 | 2 | 24 | Multi-level hierarchy validation; mapping confidence | Add auto-suggest with human confirmation for low-confidence mappings |
| 5 - Ontology Normalization | SNOMED CT mapping | Unmapped or incorrectly mapped clinical concept | Gaps in structured clinical data | 3 | 3 | 3 | 27 | Unmapped entity flagging; curation queue | Expand SNOMED CT subset coverage per therapeutic area |
| 5 - Ontology Normalization | ChEBI compound normalization | Novel compound not in ChEBI | Unlinked compound references in output | 3 | 3 | 2 | 18 | Client dictionary fallback; manual curation | Pre-engagement compound dictionary enrichment |
| 6 - Evidence Aggregation | Cross-source evidence merging | Contradictory evidence not reconciled | Inconsistent risk estimates across sources | 4 | 3 | 3 | 36 | Contradiction detection rules; source quality weighting | Add evidence hierarchy framework (RCT > observational > case report) |
| 6 - Evidence Aggregation | QDrant vector similarity search | Semantically similar but clinically distinct evidence merged | Conflated clinical contexts | 3 | 2 | 4 | 24 | Similarity threshold tuning; clinical context filtering | Add therapeutic area-specific similarity boundaries |
| 7 - Benefit-Risk Scoring | BRAT framework scoring | Incorrect weighting of benefit vs. risk dimensions | Misleading BRA conclusion | 5 | 2 | 3 | 30 | CIOMS XII alignment validation; clinical reviewer sign-off | Add sensitivity analysis for weight parameters |
| 7 - Benefit-Risk Scoring | Confidence interval calculation | Statistical error in uncertainty quantification | Overconfident or underconfident risk estimates | 4 | 2 | 3 | 24 | Statistical validation suite; bootstrap verification | Add independent statistical review for critical submissions |
| 8 - Report Generation | eCTD Module 2.5 formatting | Structural non-compliance with eCTD schema | Regulatory submission rejection | 5 | 2 | 1 | 10 | eCTD template engine; schema validation | Maintain current controls |
| 8 - Report Generation | PBRER section population | Required section missing or incomplete | Regulatory query; submission delay | 4 | 2 | 2 | 16 | Section completeness checker; mandatory field enforcement | Add content sufficiency scoring |
| 8 - Report Generation | Narrative generation | Factual inconsistency between narrative and underlying data | Regulatory credibility risk | 5 | 2 | 3 | 30 | Fact-checking against source data; clinical reviewer review | Add automated fact-data concordance checker |
| 9 - Output Validation | Automated quality checks | Quality check fails to catch systematic error | Defective output delivered to client | 5 | 2 | 3 | 30 | Multi-layer validation (automated + manual); sampling-based deep audit | Expand automated check coverage |
| 9 - Output Validation | Clinical SME review | Reviewer fatigue causing oversight | Critical issue missed in review | 4 | 3 | 4 | 48 | Review time limits; dual-reviewer for high-risk outputs | Add structured review checklists; mandatory breaks |
| 10 - Delivery | Output package assembly | Incomplete deliverable package | Client receives partial output; rework required | 3 | 2 | 1 | 6 | Package completeness checklist; automated manifest generation | Maintain current controls |
| 10 - Delivery | Audit trail finalization | Audit trail gaps or inconsistencies | ALCOA+ non-compliance; regulatory finding | 5 | 2 | 2 | 20 | Audit trail completeness validation; immutable log storage | Add automated audit trail integrity verification |

---

## 12. Roles and Responsibilities

| Role | Name/Title | Risk Management Responsibilities |
|---|---|---|
| Chief Medical Officer | [Name - TBD] | Final risk acceptance authority for patient safety-related risks; clinical risk oversight |
| Platform Director | [Name - TBD] | Overall risk management program ownership; resource allocation for risk mitigation |
| Quality Lead | [Name - TBD] | Risk register maintenance; risk assessment facilitation; compliance monitoring; audit coordination |
| Data Science Lead | [Name - TBD] | SLM performance monitoring; model risk assessment; extraction accuracy controls |
| Clinical Lead | [Name - TBD] | Clinical risk evaluation; SME review coordination; therapeutic area-specific risk assessment |
| Platform Engineering Lead | [Name - TBD] | Infrastructure risk management; availability and security controls; change deployment oversight |
| Regulatory Affairs Lead | [Name - TBD] | Regulatory compliance risk monitoring; template and format compliance; regulatory intelligence |
| IT Security Lead | [Name - TBD] | Data privacy risk management; security controls; incident response |
| Project Manager | [Name - TBD] | Engagement-specific risk tracking; client communication; escalation management |
| Ontology Specialist | [Name - TBD] | Ontology mapping quality; version management; terminology risk assessment |

### RACI Matrix for Key Risk Management Activities

| Activity | CMO | Platform Dir | Quality Lead | Data Sci Lead | Clinical Lead | Eng Lead | Reg Lead | PM |
|---|---|---|---|---|---|---|---|---|
| Risk identification | C | A | R | C | C | C | C | I |
| Risk analysis | C | I | R | R | R | R | R | I |
| Risk evaluation | A | C | R | C | C | C | C | I |
| Control implementation | I | A | C | R | R | R | R | I |
| Residual risk assessment | A | C | R | C | C | C | C | I |
| Risk acceptance | A | R | R | I | C | I | C | I |
| Risk communication (internal) | I | I | R | I | I | I | I | C |
| Risk communication (client) | C | A | R | I | C | I | C | R |
| Risk register update | I | I | R | C | C | C | C | C |
| Triggered risk review | C | A | R | R | R | R | R | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 13. Approval Signatures

| Role | Name | Signature | Date |
|---|---|---|---|
| Chief Medical Officer | __________________ | __________________ | ____/____/________ |
| Platform Director | __________________ | __________________ | ____/____/________ |
| Quality Lead | __________________ | __________________ | ____/____/________ |
| Data Science Lead | __________________ | __________________ | ____/____/________ |
| Regulatory Affairs Lead | __________________ | __________________ | ____/____/________ |

---

## Document History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | 2026-03-25 | ArcaScience Quality & Compliance Team | Initial release |

---

*This document is the property of ArcaScience and contains confidential information. Unauthorized reproduction or distribution is prohibited.*
