# Standard Operating Procedure - Training and Competency Management

**Document ID:** SOP-TRAIN-COMP-2026-001
**Version:** 1.0
**Effective Date:** 2026-03-25
**Review Date:** 2027-03-25
**Classification:** Confidential - Internal Use Only
**Owner:** ArcaScience Quality Assurance
**Approved By:** Head of Quality / Head of Operations
**Applicable To:** All ArcaScience personnel (14 FTEs, 20 collaborators total) involved in the BRA platform, including newly onboarded staff (e.g., Maria-Lola post-1code.dev training)

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Scope](#2-scope)
3. [Definitions](#3-definitions)
4. [References](#4-references)
5. [Training Requirements by Role](#5-training-requirements-by-role)
6. [Training Curriculum by Role](#6-training-curriculum-by-role)
7. [Onboarding Training Plan](#7-onboarding-training-plan)
8. [Competency Assessment Methods](#8-competency-assessment-methods)
9. [Training Record Documentation Requirements](#9-training-record-documentation-requirements)
10. [Refresher Training Schedule and Triggers](#10-refresher-training-schedule-and-triggers)
11. [Client-Specific Training](#11-client-specific-training)
12. [Training Effectiveness Evaluation](#12-training-effectiveness-evaluation)
13. [Training Material Management](#13-training-material-management)
14. [Roles and Responsibilities](#14-roles-and-responsibilities)
15. [Appendix A - Training Record Template](#appendix-a---training-record-template)
16. [Appendix B - Competency Assessment Form Template](#appendix-b---competency-assessment-form-template)
17. [Appendix C - Training Matrix Summary](#appendix-c---training-matrix-summary)
18. [Revision History](#revision-history)

---

## 1. Purpose

This SOP establishes the requirements, procedures, and documentation standards for training and competency management across all ArcaScience personnel who develop, validate, operate, or demonstrate the Benefit-Risk Assessment (BRA) platform. It ensures that:

- Every team member possesses documented, verified competence before performing GxP-relevant tasks
- Training records satisfy FDA 21 CFR Part 11, EU Annex 11, and GAMP 5 Category 5 audit requirements
- Competency is assessed objectively through written tests, practical demonstrations, and supervised execution
- Client-specific requirements (e.g., Sanofi RAISE framework) are incorporated into role-based curricula
- Newly trained staff (including those completing external programs such as 1code.dev) receive structured onboarding that enables independent task execution within defined timelines

**Regulatory Basis:** ICH Q10 (Pharmaceutical Quality System), EU GMP Annex 15, FDA 21 CFR 211.25, GAMP 5 Category 5 validation lifecycle requirements.

---

## 2. Scope

### 2.1 In Scope

- All ArcaScience FTEs (14 personnel) and collaborators (20 total headcount)
- All roles: Data Engineer, ML Engineer, Regulatory SME, QA Lead, Demo Lead, DevOps, Medical/Clinical
- Initial training, onboarding, refresher training, and client-specific training
- Competency assessment, documentation, and record retention
- Training on the BRA platform's 6 outputs: Disease Analysis, Clinical Landscape, Clinical Endpoint Study, AE Reports, BRA, BRA Summary
- Training on all platform infrastructure components: Apache Airflow, S3, ElasticSearch, DocumentDB, QDrant, FastAPI, NestJS
- Training on ontology systems: MedDRA, SNOMED CT, ChEBI, Disease Ontology
- Training on regulatory frameworks: BRAT/CIOMS XII, eCTD Module 2.5, PBRER

### 2.2 Out of Scope

- Client employee training (covered under separate client engagement SOPs)
- General IT security awareness training (covered under SOP-ITSEC-2026)
- External vendor qualification training

---

## 3. Definitions

| Term | Definition |
|------|-----------|
| **GxP Training** | Training related to Good Practice regulations (GMP, GLP, GCP, GDP) that directly impacts the quality, integrity, or regulatory compliance of BRA platform outputs |
| **Competency Assessment** | A documented evaluation confirming that a trainee can independently perform assigned tasks to the required standard, measured through written tests, practical demonstrations, or supervised execution |
| **Training Matrix** | A cross-reference document mapping each role to its required training modules, assessment methods, completion deadlines, and refresher intervals |
| **Training Record** | A controlled document capturing the trainee's name, role, training module completed, date, trainer, assessment result, and sign-off |
| **SLM** | Specialized Language Model - one of 24 clinician-trained models within the BRA platform, each designed for specific extraction or analysis tasks |
| **F1 Score** | The harmonic mean of precision and recall, used as the primary metric for SLM extraction validation. Minimum threshold varies by module (typically >= 0.85) |
| **ALCOA+** | Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, Available - the standard for data integrity in GxP environments |
| **GAMP 5 Category 5** | The highest GAMP software classification for custom-built applications, requiring full lifecycle validation including requirements, design, code review, testing, and release |
| **BRAT** | Benefit-Risk Action Team framework - a structured approach to benefit-risk assessment endorsed by FDA |
| **CIOMS XII** | Council for International Organizations of Medical Sciences Working Group XII guidance on benefit-risk assessment |
| **eCTD** | Electronic Common Technical Document - the standardized format for regulatory submissions |
| **PBRER** | Periodic Benefit-Risk Evaluation Report - an ICH E2C(R2) pharmacovigilance deliverable |
| **RAISE** | Responsible AI at Sanofi for Everyone - Sanofi's AI governance framework with five pillars: Accountable, Fair & Ethical, Robust & Safe, Transparent & Explainable, Eco-Responsible |
| **CAPA** | Corrective and Preventive Action |
| **OJT** | On-the-Job Training - supervised practical training performed in the live or staging environment |
| **SME** | Subject Matter Expert |

---

## 4. References

| Reference | Description |
|-----------|-------------|
| ICH Q10 | Pharmaceutical Quality System |
| FDA 21 CFR Part 11 | Electronic Records; Electronic Signatures |
| EU Annex 11 | Computerised Systems |
| GAMP 5 (2nd Edition) | A Risk-Based Approach to Compliant GxP Computerized Systems |
| ICH E2C(R2) | Periodic Benefit-Risk Evaluation Report |
| CIOMS XII | Benefit-Risk Balance for Marketed Drugs |
| FDA BRAT Framework | Benefit-Risk Assessment Framework |
| SOP-SANOFI-DEMO-2026-001 | Sanofi Demo Instance Setup & Configuration |
| SOP-VAL-2026 | Platform Validation Master Plan |
| SOP-ITSEC-2026 | IT Security and Access Control |

---

## 5. Training Requirements by Role

### 5.1 Data Engineer

**Primary Responsibilities:** Data ingestion pipeline development, infrastructure management, ETL/ELT processes, data quality assurance.

| Training Area | Required Modules | Priority |
|---------------|-----------------|----------|
| Platform Architecture | BRA platform overview, data flow architecture, 6 output types | Mandatory |
| Data Ingestion | Clinical data source types, ingestion pipeline design, Apache Airflow DAG configuration | Mandatory |
| Infrastructure | S3 bucket management, ElasticSearch indexing, DocumentDB operations, QDrant vector store configuration | Mandatory |
| Data Integrity | ALCOA+ principles applied to data pipelines, audit trail requirements, 21 CFR Part 11 electronic records | Mandatory |
| Ontologies | MedDRA hierarchy (SOC/HLGT/HLT/PT/LLT), SNOMED CT basics, ChEBI chemical entity mapping, Disease Ontology structure | Mandatory |
| Quality Systems | GxP awareness, deviation reporting, change control process | Mandatory |
| Security | Access control configuration, encryption standards, data classification | Mandatory |
| Client Systems | Sanofi ARTEMIS integration points, client data format requirements | Role-Specific |

**Minimum Competency Threshold:** Must demonstrate ability to independently configure a complete ingestion pipeline from a new clinical data source through to indexed, searchable output with full audit trail, verified by QA Lead.

### 5.2 ML Engineer

**Primary Responsibilities:** SLM module training, extraction validation, F1 score measurement, model performance monitoring.

| Training Area | Required Modules | Priority |
|---------------|-----------------|----------|
| Platform Architecture | BRA platform overview, ML pipeline architecture, 24 SLM module inventory | Mandatory |
| SLM Modules | Individual SLM architecture, clinician training methodology, module-specific extraction targets | Mandatory |
| Extraction Validation | F1 score calculation, precision/recall analysis, threshold configuration per output type | Mandatory |
| Ontology Normalization | MedDRA coding for AE extraction, SNOMED CT mapping for clinical terms, ChEBI for chemical entities, Disease Ontology for indication mapping | Mandatory |
| Output Generation | Disease Analysis generation, Clinical Landscape assembly, Clinical Endpoint Study compilation, AE Report structuring, BRA synthesis, BRA Summary generation | Mandatory |
| GAMP 5 Validation | Software development lifecycle for Category 5 systems, IQ/OQ/PQ requirements, test script development | Mandatory |
| Data Integrity | ALCOA+ applied to ML outputs, traceability from source to extraction, audit trail for model versioning | Mandatory |
| Quality Systems | GxP awareness, deviation reporting, change control for model updates | Mandatory |
| Performance Monitoring | F1 score drift detection, extraction quality dashboards, alert thresholds | Mandatory |

**Minimum Competency Threshold:** Must demonstrate ability to validate an SLM module end-to-end, including F1 score measurement against a gold-standard dataset, with documented results meeting or exceeding the defined threshold (>= 0.85 for critical modules, >= 0.80 for non-critical modules).

### 5.3 Regulatory SME

**Primary Responsibilities:** eCTD mapping, PBRER alignment, BRAT framework configuration, regulatory output quality review.

| Training Area | Required Modules | Priority |
|---------------|-----------------|----------|
| Platform Architecture | BRA platform overview, regulatory output workflow, 6 output types with regulatory context | Mandatory |
| eCTD Module 2.5 | Clinical overview structure, benefit-risk section mapping, BRA platform output-to-eCTD field alignment | Mandatory |
| PBRER Alignment | ICH E2C(R2) requirements, PBRER section mapping, AE report integration into PBRER structure | Mandatory |
| BRAT/CIOMS XII | BRAT framework configuration within BRA platform, benefit-risk matrix setup, CIOMS XII weighting methodology | Mandatory |
| Ontologies | MedDRA coding conventions for regulatory submissions, SNOMED CT for clinical narrative, Disease Ontology for indication classification | Mandatory |
| Platform Operations | BRA output review workflow, extraction verification for regulatory accuracy, source citation validation | Mandatory |
| Data Integrity | ALCOA+ applied to regulatory outputs, electronic signature requirements (21 CFR Part 11), EU Annex 11 compliance for computerized systems | Mandatory |
| Quality Systems | GxP training, change control, validation lifecycle, audit readiness | Mandatory |
| Client Requirements | Sanofi regulatory submission standards, RAISE framework regulatory implications | Role-Specific |

**Minimum Competency Threshold:** Must demonstrate ability to independently review a complete BRA output against eCTD Module 2.5 requirements and PBRER structure, identifying and documenting any gaps or misalignments, with results verified by QA Lead.

### 5.4 QA Lead

**Primary Responsibilities:** ALCOA+ verification, audit trail testing, validation protocol execution, quality oversight.

| Training Area | Required Modules | Priority |
|---------------|-----------------|----------|
| Platform Architecture | BRA platform complete architecture, all 6 output types, all 24 SLM modules overview | Mandatory |
| ALCOA+ Verification | Attributable - user identification and electronic signatures; Legible - output readability and format standards; Contemporaneous - timestamp verification; Original - source data traceability; Accurate - extraction accuracy validation; Complete - gap analysis methods; Consistent - cross-output consistency checks; Enduring - data retention validation; Available - accessibility testing | Mandatory |
| Audit Trail Testing | Audit trail configuration verification, completeness testing, tamper-evidence validation, 21 CFR Part 11 compliance checks | Mandatory |
| GAMP 5 Validation | Category 5 validation lifecycle, validation master plan execution, IQ/OQ/PQ protocol development and execution, traceability matrix management | Mandatory |
| Regulatory Compliance | 21 CFR Part 11 requirements checklist, EU Annex 11 requirements checklist, combined compliance verification procedures | Mandatory |
| Data Integrity | Complete ALCOA+ audit methodology, data integrity risk assessment, remediation procedures | Mandatory |
| Deviation Management | Deviation detection, classification, investigation, CAPA linkage (cross-reference SOP-INC-DEV-2026-001) | Mandatory |
| Quality Systems | Document control, change control, supplier qualification, training record management | Mandatory |
| Client Audit Preparation | Sanofi audit expectations, RAISE framework compliance evidence preparation, audit response procedures | Role-Specific |

**Minimum Competency Threshold:** Must demonstrate ability to independently execute a full ALCOA+ verification cycle on any BRA platform output, including audit trail review, and produce a compliant verification report suitable for regulatory inspection.

### 5.5 Demo Lead

**Primary Responsibilities:** Client-facing platform walkthroughs, demo instance preparation, stakeholder communication.

| Training Area | Required Modules | Priority |
|---------------|-----------------|----------|
| Platform Architecture | BRA platform complete overview, 6 output types with business context, value proposition per output | Mandatory |
| Platform Navigation | End-to-end platform walkthrough, UI/UX features, search and filter capabilities, output visualization | Mandatory |
| Demo Preparation | Demo instance configuration (per SOP-SANOFI-DEMO-2026-001), test data loading, environment verification, fallback procedures | Mandatory |
| Output Interpretation | Disease Analysis interpretation and talking points, Clinical Landscape narrative, Clinical Endpoint Study key metrics, AE Report structure and significance, BRA framework explanation, BRA Summary executive overview | Mandatory |
| Regulatory Context | High-level eCTD/PBRER/BRAT awareness (sufficient to explain platform alignment), GAMP 5 validation messaging, ALCOA+ compliance messaging | Mandatory |
| Client Communication | Stakeholder management, technical question handling, escalation to SMEs, follow-up procedures | Mandatory |
| Data Integrity Messaging | ALCOA+ explanation for non-technical audiences, audit trail demonstration, traceability walkthrough | Mandatory |
| Client-Specific | Sanofi RAISE framework alignment messaging, ARTEMIS integration overview, Sanofi stakeholder profiles and concerns | Role-Specific |

**Minimum Competency Threshold:** Must successfully deliver a complete platform walkthrough (all 6 outputs) to an internal audience acting as client stakeholders, handling at least 5 unscripted technical questions, with performance evaluated by the Regulatory SME and QA Lead.

### 5.6 DevOps

**Primary Responsibilities:** Infrastructure management, deployment, access control, performance monitoring, security.

| Training Area | Required Modules | Priority |
|---------------|-----------------|----------|
| Platform Architecture | BRA platform infrastructure architecture, component dependencies, deployment topology | Mandatory |
| Infrastructure Management | Apache Airflow administration, S3 lifecycle policies, ElasticSearch cluster management, DocumentDB administration, QDrant operations | Mandatory |
| Application Stack | FastAPI backend operations, NestJS frontend operations, API gateway configuration, load balancing | Mandatory |
| Access Control | Role-based access control (RBAC) configuration, 21 CFR Part 11 electronic signature infrastructure, user provisioning/deprovisioning, access review procedures | Mandatory |
| Performance Monitoring | System health dashboards, alerting thresholds, capacity planning, SLA monitoring | Mandatory |
| Security | Encryption at rest and in transit, network segmentation, vulnerability scanning, incident response | Mandatory |
| GAMP 5 Infrastructure | Infrastructure qualification (IQ), environment separation (dev/staging/prod/demo), configuration management, change control for infrastructure | Mandatory |
| Audit Trail Infrastructure | Audit log storage and retention, log integrity verification, backup and recovery of audit data | Mandatory |
| Disaster Recovery | Backup procedures, recovery time objectives (RTO), recovery point objectives (RPO), failover testing | Mandatory |
| Client Environments | Sanofi demo instance infrastructure, network connectivity requirements, ARTEMIS integration infrastructure | Role-Specific |

**Minimum Competency Threshold:** Must demonstrate ability to independently deploy a complete BRA platform instance from scratch, configure access controls compliant with 21 CFR Part 11, and verify all monitoring and alerting is operational, with results documented in an IQ protocol.

### 5.7 Medical/Clinical

**Primary Responsibilities:** Ontology configuration, extraction review, clinical validation of outputs.

| Training Area | Required Modules | Priority |
|---------------|-----------------|----------|
| Platform Architecture | BRA platform overview with clinical context, 6 output types clinical significance, SLM module clinical training methodology | Mandatory |
| Ontology Configuration | MedDRA hierarchy management (SOC through LLT), SNOMED CT clinical term mapping, ChEBI chemical entity classification, Disease Ontology therapeutic area alignment | Mandatory |
| Extraction Review | Clinical accuracy assessment of SLM extractions, gold-standard dataset development, inter-rater reliability methodology, false positive/negative clinical impact assessment | Mandatory |
| Clinical Validation | Disease Analysis clinical accuracy review, Clinical Landscape completeness assessment, Clinical Endpoint Study statistical validity, AE Report clinical significance grading, BRA clinical judgment integration, BRA Summary clinical narrative review | Mandatory |
| Regulatory Knowledge | eCTD Module 2.5 clinical content requirements, PBRER clinical sections, BRAT benefit-risk clinical weighting | Mandatory |
| Data Integrity | ALCOA+ applied to clinical data, clinical data quality standards, source verification methodology | Mandatory |
| Quality Systems | GxP awareness, deviation reporting for clinical findings, clinical change control | Mandatory |
| Pharmacovigilance | Signal detection basics, AE coding conventions, safety data interpretation | Mandatory |

**Minimum Competency Threshold:** Must demonstrate ability to independently review the clinical accuracy of all 6 BRA platform outputs for a given therapeutic indication, including ontology coding verification and extraction accuracy assessment, producing a documented clinical validation report.

---

## 6. Training Curriculum by Role

### 6.1 Core Curriculum (All Roles)

All personnel must complete the following core modules before role-specific training:

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| CORE-001 | ArcaScience Company & Mission | 2 hours | Understand company mission, BRA platform value proposition, team structure, client landscape | Written quiz (80% pass) |
| CORE-002 | BRA Platform Overview | 4 hours | Identify all 6 outputs, describe data flow from ingestion to output, explain 24 SLM architecture at high level | Written quiz (80% pass) |
| CORE-003 | GxP Fundamentals | 4 hours | Define GxP, explain relevance to software platforms, identify GxP-critical activities in daily work | Written quiz (85% pass) |
| CORE-004 | Data Integrity & ALCOA+ | 4 hours | Define each ALCOA+ element, identify data integrity risks, apply ALCOA+ to platform activities | Written quiz (85% pass) + scenario exercise |
| CORE-005 | 21 CFR Part 11 & EU Annex 11 | 3 hours | Explain key requirements of both regulations, identify compliance controls in BRA platform, describe electronic signature requirements | Written quiz (85% pass) |
| CORE-006 | GAMP 5 Category 5 Awareness | 3 hours | Explain GAMP 5 categories, describe Category 5 validation requirements, identify validation lifecycle stages | Written quiz (80% pass) |
| CORE-007 | Quality System Essentials | 3 hours | Navigate document control system, submit deviation reports, understand change control, locate SOPs | Written quiz (80% pass) + practical demo |
| CORE-008 | Information Security | 2 hours | Apply data classification, use access controls, report security incidents, handle client data appropriately | Written quiz (80% pass) |
| CORE-009 | SOP Navigation & Compliance | 2 hours | Locate relevant SOPs, follow SOP procedures, understand SOP revision process | Practical demonstration |

**Total Core Curriculum:** 27 hours

### 6.2 Data Engineer Curriculum

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| DE-001 | Data Source Taxonomy | 4 hours | Classify clinical data sources (trials, literature, registries, PV databases), map source types to BRA outputs | Written quiz (85% pass) |
| DE-002 | Apache Airflow Pipeline Design | 8 hours | Design DAGs for clinical data ingestion, configure task dependencies, implement error handling and retry logic, set up monitoring | Practical: Build a complete DAG |
| DE-003 | S3 Data Lake Management | 4 hours | Configure bucket policies, implement lifecycle rules, manage data partitioning, enforce encryption, audit access logs | Practical: Configure compliant S3 environment |
| DE-004 | ElasticSearch Indexing | 6 hours | Design index mappings for clinical data, configure analyzers for medical terminology, optimize search performance, manage index lifecycle | Practical: Build index for clinical dataset |
| DE-005 | DocumentDB Operations | 4 hours | Design document schemas for BRA data models, configure replication, implement backup strategies, manage access controls | Practical: Deploy compliant DocumentDB |
| DE-006 | QDrant Vector Store | 4 hours | Configure vector collections for SLM embeddings, manage similarity search parameters, optimize retrieval performance | Practical: Configure vector store for SLM module |
| DE-007 | Ontology Data Integration | 6 hours | Ingest MedDRA hierarchy data, map SNOMED CT relationships, integrate ChEBI chemical entities, load Disease Ontology structure | Practical: Complete ontology integration |
| DE-008 | Data Quality & Validation | 4 hours | Implement data quality checks, validate ingested data completeness, verify ontology mapping accuracy, document quality metrics | Practical: Execute data quality protocol |
| DE-009 | Audit Trail Implementation | 4 hours | Implement audit logging for all data operations, verify ALCOA+ compliance of audit records, test audit trail completeness | Practical: Audit trail verification |

**Total Data Engineer Curriculum:** 44 hours (+ 27 hours core = 71 hours)

### 6.3 ML Engineer Curriculum

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| ML-001 | SLM Architecture Deep Dive | 8 hours | Understand architecture of all 24 SLMs, explain clinician training methodology, describe model versioning and governance | Written exam (85% pass) + architecture diagram |
| ML-002 | Extraction Pipeline Design | 6 hours | Design extraction pipelines for each output type, configure SLM chaining for complex extractions, implement fallback strategies | Practical: Build extraction pipeline |
| ML-003 | F1 Score Measurement | 4 hours | Calculate F1, precision, and recall; configure thresholds per module; design gold-standard evaluation datasets; interpret results | Practical: Complete F1 evaluation cycle |
| ML-004 | Ontology Normalization in ML | 6 hours | Implement MedDRA coding in extraction output, configure SNOMED CT term normalization, apply ChEBI entity resolution, map Disease Ontology classifications | Practical: Normalize extraction output |
| ML-005 | Output Generation - Disease Analysis | 4 hours | Configure Disease Analysis generation pipeline, validate output structure, verify ontology alignment | Practical: Generate and validate output |
| ML-006 | Output Generation - Clinical Landscape | 4 hours | Configure Clinical Landscape assembly, validate literature coverage, verify citation accuracy | Practical: Generate and validate output |
| ML-007 | Output Generation - Clinical Endpoint Study | 4 hours | Configure endpoint extraction, validate statistical data accuracy, verify study design classification | Practical: Generate and validate output |
| ML-008 | Output Generation - AE Reports | 4 hours | Configure AE extraction pipeline, validate MedDRA coding, verify signal detection alignment | Practical: Generate and validate output |
| ML-009 | Output Generation - BRA & Summary | 6 hours | Configure BRA synthesis, validate BRAT framework application, verify benefit-risk weighting, generate executive summary | Practical: Generate and validate both outputs |
| ML-010 | Model Performance Monitoring | 4 hours | Implement F1 drift detection, configure performance dashboards, set up alerting for threshold breaches, manage model retraining triggers | Practical: Configure monitoring suite |
| ML-011 | GAMP 5 for ML Systems | 4 hours | Apply Category 5 validation to ML models, document model validation protocols, execute IQ/OQ/PQ for ML components | Written exam (85% pass) + protocol review |

**Total ML Engineer Curriculum:** 54 hours (+ 27 hours core = 81 hours)

### 6.4 Regulatory SME Curriculum

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| REG-001 | eCTD Module 2.5 Deep Dive | 8 hours | Map every BRA output field to eCTD Module 2.5 sections, identify gaps, configure platform mapping rules | Written exam (90% pass) + mapping exercise |
| REG-002 | PBRER Alignment | 6 hours | Map BRA outputs to PBRER sections per ICH E2C(R2), configure periodic report generation, validate section completeness | Written exam (90% pass) + mapping exercise |
| REG-003 | BRAT Framework Configuration | 6 hours | Configure BRAT benefit-risk matrices in platform, define weighting methodologies, set up stakeholder-specific views | Practical: Configure complete BRAT assessment |
| REG-004 | CIOMS XII Implementation | 4 hours | Apply CIOMS XII guidance within platform, configure risk categorization, implement benefit-risk communication templates | Written exam (85% pass) |
| REG-005 | Regulatory Output Review | 8 hours | Execute end-to-end review of all 6 outputs for regulatory accuracy, identify and document non-conformances, recommend corrections | Practical: Complete review cycle |
| REG-006 | Source Citation Validation | 4 hours | Verify publication references in outputs, validate clinical trial citations, confirm data source traceability | Practical: Validate citations for one output set |
| REG-007 | Submission Readiness Assessment | 4 hours | Evaluate BRA outputs for submission readiness, identify remediation needs, prepare submission gap analysis | Practical: Complete readiness assessment |

**Total Regulatory SME Curriculum:** 40 hours (+ 27 hours core = 67 hours)

### 6.5 QA Lead Curriculum

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| QA-001 | ALCOA+ Verification Methodology | 8 hours | Execute complete ALCOA+ verification on each output type, document findings using standardized templates, classify non-conformances | Practical: Full ALCOA+ audit |
| QA-002 | Audit Trail Testing | 6 hours | Design audit trail test protocols, execute completeness testing, verify tamper-evidence, document results | Practical: Execute audit trail test suite |
| QA-003 | GAMP 5 Validation Execution | 8 hours | Develop IQ/OQ/PQ protocols for BRA platform, execute validation protocols, manage traceability matrix, document results | Practical: Execute full validation cycle |
| QA-004 | 21 CFR Part 11 Compliance Audit | 4 hours | Execute Part 11 compliance checklist, identify gaps, recommend remediation, document findings | Practical: Complete compliance audit |
| QA-005 | EU Annex 11 Compliance Audit | 4 hours | Execute Annex 11 compliance checklist, identify gaps, recommend remediation, document findings | Practical: Complete compliance audit |
| QA-006 | Deviation Investigation | 4 hours | Classify deviations, conduct root cause analysis, link to CAPA, track to closure | Practical: Investigate sample deviation |
| QA-007 | Training Record Management | 3 hours | Manage training records system, verify completeness, prepare training status reports, support audit requests | Practical: Audit training records |
| QA-008 | Client Audit Preparation | 4 hours | Prepare audit response packages, organize evidence, conduct mock audits, manage audit findings | Practical: Prepare mock audit package |

**Total QA Lead Curriculum:** 41 hours (+ 27 hours core = 68 hours)

### 6.6 Demo Lead Curriculum

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| DM-001 | Platform Navigation Mastery | 8 hours | Navigate all platform features, demonstrate all 6 outputs, explain UI/UX elements, perform common workflows | Practical: Timed navigation exercise |
| DM-002 | Demo Instance Setup | 6 hours | Execute SOP-SANOFI-DEMO-2026-001 end-to-end, configure demo data, verify environment, execute pre-demo checklist | Practical: Set up demo instance |
| DM-003 | Output Interpretation & Storytelling | 8 hours | Explain each output's clinical/regulatory significance, construct narrative flow across outputs, handle "so what?" questions | Practical: Deliver narrative to panel |
| DM-004 | Technical Q&A Handling | 4 hours | Answer common technical questions about SLMs, ontologies, validation; escalate appropriately; manage "I'll follow up" responses | Role-play: Handle 20 unscripted questions |
| DM-005 | Regulatory Messaging | 4 hours | Explain GAMP 5, ALCOA+, 21 CFR Part 11, eCTD alignment in client-appropriate language | Role-play: Explain compliance to non-technical audience |
| DM-006 | Stakeholder Communication | 4 hours | Manage different stakeholder personas (regulatory, clinical, IT, executive), adapt messaging, handle objections | Role-play: Multi-persona session |
| DM-007 | Fallback & Recovery Procedures | 3 hours | Handle demo failures gracefully, switch to backup environments, manage technical issues during live demos | Practical: Simulate failure scenarios |

**Total Demo Lead Curriculum:** 37 hours (+ 27 hours core = 64 hours)

### 6.7 DevOps Curriculum

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| DO-001 | Infrastructure Architecture | 6 hours | Map complete infrastructure topology, identify all component dependencies, understand scaling requirements | Written exam (85% pass) + architecture diagram |
| DO-002 | Apache Airflow Administration | 6 hours | Administer Airflow instance, manage DAG deployments, configure worker scaling, troubleshoot failures | Practical: Administration scenarios |
| DO-003 | Storage & Database Administration | 6 hours | Administer S3, ElasticSearch, DocumentDB, QDrant; manage backups, replication, performance tuning | Practical: Administration scenarios |
| DO-004 | Application Stack Management | 6 hours | Deploy and manage FastAPI backend, NestJS frontend; configure API gateway, manage SSL/TLS, implement health checks | Practical: Deployment exercise |
| DO-005 | Access Control & 21 CFR Part 11 | 6 hours | Configure RBAC, implement electronic signature infrastructure, manage user lifecycle, conduct access reviews | Practical: Configure compliant access controls |
| DO-006 | Monitoring & Alerting | 4 hours | Configure system monitoring, set up alert thresholds, create dashboards, implement SLA tracking | Practical: Build monitoring suite |
| DO-007 | Disaster Recovery & Business Continuity | 4 hours | Execute backup procedures, test recovery processes, validate RTO/RPO, manage failover | Practical: DR drill execution |
| DO-008 | Environment Management | 4 hours | Manage dev/staging/prod/demo environments, implement configuration management, enforce environment separation | Practical: Environment provisioning |
| DO-009 | Infrastructure Qualification (IQ) | 4 hours | Execute IQ protocols for all infrastructure components, document results, manage deviations | Practical: Execute IQ protocol |

**Total DevOps Curriculum:** 46 hours (+ 27 hours core = 73 hours)

### 6.8 Medical/Clinical Curriculum

| Module ID | Module Name | Duration | Learning Objectives | Assessment |
|-----------|-------------|----------|-------------------|------------|
| MC-001 | MedDRA Mastery | 8 hours | Navigate full MedDRA hierarchy (SOC/HLGT/HLT/PT/LLT), apply coding conventions, identify miscoding, configure platform MedDRA settings | Written exam (90% pass) + coding exercise |
| MC-002 | SNOMED CT Clinical Mapping | 6 hours | Map clinical terms using SNOMED CT, validate term relationships, configure platform SNOMED CT integration | Written exam (85% pass) + mapping exercise |
| MC-003 | ChEBI & Disease Ontology | 4 hours | Classify chemical entities using ChEBI, map indications using Disease Ontology, validate ontology alignment | Written exam (85% pass) |
| MC-004 | SLM Extraction Review | 8 hours | Review SLM extractions for clinical accuracy, develop gold-standard datasets, calculate inter-rater reliability, assess false positive/negative clinical impact | Practical: Review extraction set |
| MC-005 | Clinical Output Validation | 8 hours | Validate clinical accuracy of all 6 outputs, assess completeness against source data, verify clinical narrative quality | Practical: Validate complete output set |
| MC-006 | Pharmacovigilance Context | 4 hours | Understand AE coding conventions, assess signal detection output, validate safety data interpretation | Written exam (85% pass) |
| MC-007 | Clinical Judgment Documentation | 4 hours | Document clinical review decisions with rationale, maintain audit trail for clinical judgments, apply ALCOA+ to clinical assessments | Practical: Document review decisions |

**Total Medical/Clinical Curriculum:** 42 hours (+ 27 hours core = 69 hours)

---

## 7. Onboarding Training Plan

### 7.1 Overview

All new team members follow a structured 8-week onboarding program. The plan is organized into phases, with each phase building on the previous. No team member may perform unsupervised GxP-relevant work until completing Phase 3 assessment.

### 7.2 Pre-Arrival (Before Day 1)

| Item | Responsible | Deadline |
|------|------------|----------|
| Create user accounts (platform, email, document control system) | DevOps | 3 business days before start |
| Assign training mentor (same role, senior) | Hiring Manager | 5 business days before start |
| Prepare training schedule (role-specific) | Training Coordinator | 3 business days before start |
| Provision workstation with required software and access | DevOps | 1 business day before start |
| Send welcome package with reading materials (company overview, role description, SOP index) | HR/Training Coordinator | 3 business days before start |

### 7.3 Week 1 - Orientation and Core Foundations

**Goal:** Company orientation, GxP awareness, platform introduction.

| Day | Activity | Duration | Trainer/Resource | Deliverable |
|-----|----------|----------|-----------------|-------------|
| Mon | Company orientation, team introductions, workspace setup | 4 hours | HR / Hiring Manager | Signed onboarding checklist |
| Mon | IT security briefing, account verification, MFA setup | 2 hours | DevOps | Access confirmed, MFA active |
| Mon | CORE-001: ArcaScience Company & Mission | 2 hours | Training Coordinator | Quiz completed |
| Tue | CORE-002: BRA Platform Overview | 4 hours | ML Engineer (mentor) | Quiz completed |
| Tue | Guided platform tour (observation only) | 2 hours | Demo Lead | Observation log signed |
| Wed | CORE-003: GxP Fundamentals | 4 hours | QA Lead | Quiz completed (85% min) |
| Wed | Document control system orientation | 2 hours | QA Lead | Navigate and locate 5 SOPs |
| Thu | CORE-004: Data Integrity & ALCOA+ | 4 hours | QA Lead | Quiz completed (85% min) + scenario |
| Thu | SOP reading time (role-relevant SOPs) | 2 hours | Self-directed | Reading log signed |
| Fri | CORE-005: 21 CFR Part 11 & EU Annex 11 | 3 hours | QA Lead | Quiz completed (85% min) |
| Fri | Week 1 review with mentor | 1 hour | Mentor | Week 1 checklist signed |
| Fri | CORE-008: Information Security | 2 hours | DevOps | Quiz completed (80% min) |

**Week 1 Gate:** All core quizzes passed at required thresholds. If any quiz fails, retake within 2 business days.

### 7.4 Week 2 - Core Completion and Role Introduction

**Goal:** Complete core curriculum, begin role-specific training.

| Day | Activity | Duration | Trainer/Resource | Deliverable |
|-----|----------|----------|-----------------|-------------|
| Mon | CORE-006: GAMP 5 Category 5 Awareness | 3 hours | QA Lead | Quiz completed (80% min) |
| Mon | CORE-007: Quality System Essentials | 3 hours | QA Lead | Quiz + practical demo completed |
| Tue | CORE-009: SOP Navigation & Compliance | 2 hours | QA Lead | Practical demonstration passed |
| Tue | Begin role-specific Module 1 | 4 hours | Role SME | Per curriculum |
| Wed | Role-specific Module 1 continuation | 4 hours | Role SME | Per curriculum |
| Wed | Mentor shadowing (observe role tasks) | 2 hours | Mentor | Observation log signed |
| Thu | Role-specific Module 2 | 4 hours | Role SME | Per curriculum |
| Thu | Guided hands-on (staging environment) | 2 hours | Mentor | Hands-on log signed |
| Fri | Role-specific Module 2 continuation | 4 hours | Role SME | Per curriculum |
| Fri | Week 2 review with mentor | 1 hour | Mentor | Week 2 checklist signed |

**Week 2 Gate:** All core modules completed and passed. Role-specific Modules 1-2 in progress.

### 7.5 Weeks 3-4 - Role-Specific Training (Intensive)

**Goal:** Complete majority of role-specific curriculum modules.

| Week | Focus | Daily Structure | Assessment |
|------|-------|-----------------|------------|
| Week 3 | Role-specific Modules 3-5 | Morning: Instructor-led (4 hours), Afternoon: Hands-on practice in staging (2 hours) + mentor shadowing (1 hour) | Module assessments per curriculum |
| Week 4 | Role-specific Modules 6 through completion | Morning: Instructor-led (4 hours), Afternoon: Supervised hands-on in staging (3 hours) | Module assessments per curriculum |

**Weeks 3-4 Gate:** All role-specific modules completed. All assessments passed at required thresholds. Any failed assessment must be retaken within 3 business days.

### 7.6 Weeks 5-6 - Supervised Execution

**Goal:** Perform real tasks under direct supervision.

| Activity | Frequency | Supervisor | Documentation |
|----------|-----------|-----------|---------------|
| Execute assigned tasks with mentor present | Daily | Mentor | Task execution log, co-signed |
| End-of-day review with mentor | Daily | Mentor | Review notes documented |
| Mid-week check-in with Training Coordinator | 2x per week | Training Coordinator | Progress update documented |
| Practice with staging/demo environment | As needed | Self-directed (mentor available) | Practice log maintained |

**Supervised Execution Rules:**
1. Mentor must be physically or virtually present during all GxP-relevant task execution
2. Mentor must co-sign all work products
3. Any errors discovered during supervised execution are documented as training observations (not deviations) unless they affect validated output
4. Trainee may not approve, release, or sign off on any deliverable during this phase

**Weeks 5-6 Gate:** Mentor confirms trainee can execute all assigned task types correctly and consistently. Training Coordinator reviews task execution logs for completeness.

### 7.7 Weeks 7-8 - Competency Assessment and Certification

**Goal:** Formal competency assessment, independent work authorization.

| Activity | Timing | Assessor | Deliverable |
|----------|--------|---------|-------------|
| Written competency examination (role-specific) | Week 7, Day 1-2 | Training Coordinator + Role SME | Exam score documented |
| Practical competency demonstration | Week 7, Day 3-4 | Role SME + QA Lead | Assessment form completed |
| Supervised independent execution (assessor observes but does not assist) | Week 7, Day 5 - Week 8, Day 3 | Role SME | Execution log, assessor notes |
| Final competency review meeting | Week 8, Day 4 | Training Coordinator + Mentor + Role SME | Competency determination |
| Training completion sign-off | Week 8, Day 5 | Training Coordinator + QA Lead + Hiring Manager | Training record finalized |

**Final Certification Criteria:**
- All core module assessments passed at required thresholds
- All role-specific module assessments passed at required thresholds
- Written competency examination score >= 85%
- Practical demonstration rated "Competent" or "Exceeds Expectations" on all critical tasks
- Supervised independent execution completed without critical errors
- All training records complete and signed

**If certification criteria not met:** Extend supervised execution by 2 weeks with targeted remediation plan. Reassess at end of extension period. If still not met, escalate to Head of Operations for determination.

---

## 8. Competency Assessment Methods

### 8.1 Assessment Types

| Method | When Used | Pass Criteria | Documentation |
|--------|-----------|--------------|---------------|
| **Written Test** | After each training module and at final competency assessment | Module-specific threshold (80-90% depending on criticality) | Scored test with answer key, retained in training record |
| **Practical Demonstration** | After hands-on training modules and at final competency assessment | Assessed against standardized checklist; all critical steps must be completed correctly | Completed assessment checklist with assessor notes and sign-off |
| **Supervised Execution** | During Weeks 5-8 of onboarding and for high-risk task authorization | Task completed independently with no critical errors; assessor present but not assisting | Execution log with assessor observations and sign-off |
| **Oral Examination** | Supplementary assessment for regulatory and clinical roles | Assessor panel of 2+ SMEs confirms adequate knowledge depth | Examination notes signed by all panel members |
| **Portfolio Review** | For experienced hires and role transfers | Review of prior work products demonstrates equivalent competency | Portfolio assessment form with reviewer notes |

### 8.2 Competency Levels

| Level | Definition | Authorization |
|-------|-----------|---------------|
| **Level 0 - Untrained** | No training completed for the task | No task execution permitted |
| **Level 1 - Awareness** | Core training completed; understands concepts but not yet hands-on trained | May observe but not execute GxP tasks |
| **Level 2 - Supervised** | Role-specific training completed; assessment pending or in supervised execution phase | May execute tasks only under direct supervision with co-signature |
| **Level 3 - Competent** | All assessments passed; competency certified | May execute tasks independently; may not train others |
| **Level 4 - Expert** | Level 3 plus 6+ months of independent execution with no significant deviations, plus Train-the-Trainer certification | May execute tasks independently and train/assess others |

### 8.3 Assessment Scoring

**Written Tests:**
- Multiple choice, short answer, and scenario-based questions
- Minimum 20 questions per module assessment
- Minimum 40 questions for final competency examination
- Scored automatically where possible; short answer scored by SME with answer rubric
- Results documented within 2 business days

**Practical Demonstrations:**
- Standardized checklist with critical and non-critical steps
- Critical steps: Must all be completed correctly for a pass
- Non-critical steps: 80% completion rate required
- Assessor completes checklist in real-time during demonstration
- Results documented same day

**Supervised Execution:**
- Assessed over minimum 3 complete task cycles
- Assessor documents observations using standardized form
- Critical error during any cycle requires remediation and restart of that cycle
- Non-critical errors documented as training observations

### 8.4 Reassessment Procedure

1. If a trainee fails any assessment, the Training Coordinator schedules a remediation session within 3 business days
2. Remediation focuses on identified knowledge or skill gaps
3. Reassessment is scheduled no sooner than 2 business days after remediation
4. A maximum of 2 reassessment attempts are permitted per module
5. If the trainee fails after 2 reassessment attempts, the matter is escalated to the Head of Operations and QA Lead for determination (options include: extended training, role reassignment, or performance management)
6. All reassessment attempts and outcomes are documented in the training record

---

## 9. Training Record Documentation Requirements

### 9.1 Required Records

For each training event, the following must be documented and retained:

| Record Element | Format | Responsible |
|---------------|--------|------------|
| Trainee full name and employee ID | Training Record Form (Appendix A) | Training Coordinator |
| Role and department | Training Record Form | Training Coordinator |
| Training module ID and title | Training Record Form | Trainer |
| Training date(s) and duration | Training Record Form | Trainer |
| Trainer name and qualifications | Training Record Form | Trainer |
| Training method (classroom, e-learning, OJT, self-study) | Training Record Form | Trainer |
| Assessment type and result (score, pass/fail) | Training Record Form + Assessment Form | Assessor |
| Trainee signature (electronic or wet ink) | Training Record Form | Trainee |
| Trainer signature | Training Record Form | Trainer |
| Assessor signature (if different from trainer) | Assessment Form (Appendix B) | Assessor |
| Training Coordinator sign-off | Training Record Form | Training Coordinator |
| Competency level assigned (0-4) | Training Record Form | Training Coordinator |

### 9.2 Record Retention

- All training records must be retained for the lifetime of the BRA platform plus 5 years, or as required by client contracts, whichever is longer
- Electronic records must comply with 21 CFR Part 11 (audit trail, electronic signatures, access controls)
- Paper records (if any) must be scanned and stored electronically within 5 business days
- Training records must be available for client audits within 24 hours of request
- Backup copies must be maintained per the disaster recovery SOP

### 9.3 Training Record Review

- Training Coordinator reviews all training records for completeness monthly
- QA Lead audits training records quarterly (sample-based, minimum 25% of records)
- Non-conformances in training records are documented as deviations per SOP-INC-DEV-2026-001
- Training record status is reported to management monthly

---

## 10. Refresher Training Schedule and Triggers

### 10.1 Scheduled Refresher Training

| Training Category | Refresher Interval | Assessment Required |
|------------------|--------------------|--------------------|
| GxP Fundamentals (CORE-003) | Annual | Written quiz (85% pass) |
| Data Integrity & ALCOA+ (CORE-004) | Annual | Written quiz (85% pass) + scenario |
| 21 CFR Part 11 & EU Annex 11 (CORE-005) | Annual | Written quiz (85% pass) |
| GAMP 5 Awareness (CORE-006) | Annual | Written quiz (80% pass) |
| Information Security (CORE-008) | Annual | Written quiz (80% pass) |
| Role-specific critical modules | Every 18 months | Practical demonstration |
| Client-specific training | Per client contract (annually at minimum) | Per client requirements |

### 10.2 Event-Triggered Refresher Training

The following events trigger mandatory refresher training regardless of scheduled intervals:

| Trigger Event | Affected Roles | Training Scope | Timeline |
|--------------|---------------|----------------|----------|
| Regulatory change (new guidance, updated regulation) | All affected roles | Updated regulation content, impact on platform operations | Within 30 days of regulatory effective date |
| Platform major version release | All roles | New features, changed workflows, updated validation status | Before first use of new version |
| SLM module update or retraining | ML Engineer, Medical/Clinical, QA Lead | Updated module behavior, new extraction patterns, F1 score changes | Before module deployment to production |
| Ontology version update (MedDRA, SNOMED CT, etc.) | Medical/Clinical, ML Engineer, Regulatory SME, Data Engineer | Updated terminology, changed mappings, migration procedures | Before deployment of updated ontology |
| Significant deviation or CAPA | Roles involved in deviation | Root cause-specific remediation training | As specified in CAPA plan |
| New client onboarding | Demo Lead, Regulatory SME, QA Lead | Client-specific requirements, frameworks, integration points | Before first client interaction |
| Return from extended absence (> 90 days) | Returning employee | Role-specific refresher based on changes during absence | Before resuming GxP-relevant work |
| Audit finding related to training | Affected roles | Finding-specific remediation | Within 15 business days of finding |
| Organizational role change | Employee changing roles | Full training curriculum for new role | Per onboarding plan (may be accelerated based on prior competency) |

### 10.3 Refresher Training Process

1. Training Coordinator maintains a refresher training calendar and sends reminders 30 days before due dates
2. Employee completes refresher training and assessment by the due date
3. If refresher training is overdue by more than 15 business days, the employee's authorization to perform affected GxP-relevant tasks is suspended until training is completed
4. Suspension of authorization is documented and communicated to the employee's manager
5. Completed refresher training is documented in the training record using the same forms as initial training

---

## 11. Client-Specific Training

### 11.1 Sanofi-Specific Training

All personnel involved in Sanofi engagements must complete the following additional training:

| Module ID | Module Name | Duration | Learning Objectives | Required Roles |
|-----------|-------------|----------|-------------------|----------------|
| CS-SAN-001 | Sanofi RAISE Framework | 4 hours | Understand all 5 RAISE pillars (Accountable to Outcomes, Fair & Ethical, Robust & Safe, Transparent & Explainable, Eco-Responsible); map BRA platform features to each pillar; articulate compliance in client-facing settings | All Sanofi-facing roles |
| CS-SAN-002 | ARTEMIS Integration Awareness | 3 hours | Understand ARTEMIS system architecture (at overview level), identify integration touchpoints with BRA platform, understand data flow between systems, know escalation paths for integration issues | Data Engineer, DevOps, ML Engineer |
| CS-SAN-003 | Sanofi Demo Delivery | 4 hours | Execute SOP-SANOFI-DEMO-2026-001, understand Sanofi stakeholder profiles (regulatory, clinical, IT, executive), practice Sanofi-specific messaging, handle Sanofi-specific questions | Demo Lead, Regulatory SME |
| CS-SAN-004 | Sanofi Data Requirements | 3 hours | Understand Sanofi data formats, classification standards, data handling requirements, privacy and confidentiality obligations | Data Engineer, ML Engineer, DevOps |
| CS-SAN-005 | Sanofi Audit Preparation | 2 hours | Understand Sanofi audit methodology, prepare evidence packages aligned to RAISE framework, practice audit interview responses | QA Lead, all role leads |

**RAISE Framework Pillar Mapping for Training:**

| RAISE Pillar | BRA Platform Alignment | Training Focus |
|-------------|----------------------|----------------|
| Accountable to Outcomes | Every output traceable to source data; no hallucination; 24 SLMs with documented accuracy metrics | Trainee must demonstrate source traceability for any output element |
| Fair & Ethical | No bias in subpopulation analyses; transparent methodology; equitable data representation | Trainee must identify potential bias vectors and mitigation strategies |
| Robust & Safe | GAMP 5 Category 5 validation; F1 thresholds enforced; ALCOA+ compliance | Trainee must execute validation protocols and verify F1 thresholds |
| Transparent & Explainable | Full audit trail; extraction rationale documented; methodology published | Trainee must explain any platform decision or output to a non-technical stakeholder |
| Eco-Responsible | Infrastructure efficiency; resource optimization; minimal unnecessary computation | Trainee must understand resource utilization metrics and optimization practices |

### 11.2 Generic Client-Specific Training Process

For each new big pharma client engagement, the following process applies:

1. **Pre-Engagement Assessment (Week -4):** Identify client-specific requirements, frameworks, systems, and stakeholder expectations
2. **Curriculum Development (Week -3):** Develop client-specific training modules based on assessment findings
3. **Material Review (Week -2):** QA Lead reviews training materials for accuracy and completeness
4. **Training Delivery (Week -1):** Deliver client-specific training to all assigned personnel
5. **Assessment (Week -1):** Assess competency for client-specific requirements
6. **Documentation (Before Engagement Start):** Complete all training records before first client interaction
7. **Ongoing Updates:** Update client-specific training as requirements evolve; document changes in training records

---

## 12. Training Effectiveness Evaluation

### 12.1 Evaluation Levels (Kirkpatrick Model)

| Level | What is Measured | Method | Frequency |
|-------|-----------------|--------|-----------|
| **Level 1 - Reaction** | Trainee satisfaction with training quality, relevance, and delivery | Post-training survey (5-point scale) | After every training module |
| **Level 2 - Learning** | Knowledge and skill acquisition | Written tests, practical demonstrations (as defined in curriculum) | After every training module |
| **Level 3 - Behavior** | Application of training to job performance | Manager observation, peer review, task execution quality metrics | 90 days post-training |
| **Level 4 - Results** | Impact on organizational outcomes | Deviation rates, audit findings, client satisfaction, F1 score trends | Quarterly |

### 12.2 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Method | Review Frequency |
|-----|--------|-------------------|-----------------|
| Training completion rate (on-time) | >= 95% | Training records vs. schedule | Monthly |
| First-attempt assessment pass rate | >= 85% | Assessment records | Monthly |
| Average assessment score | >= 88% | Assessment records | Quarterly |
| Training-related deviations (post-training) | <= 2 per quarter | Deviation tracking system | Quarterly |
| Client audit findings related to training | 0 critical, <= 1 major per year | Audit reports | Per audit |
| Trainee satisfaction (Level 1) | >= 4.0 / 5.0 | Survey results | Quarterly |
| Time to competency (onboarding) | <= 8 weeks | Training records | Per new hire |
| Refresher training overdue rate | <= 5% | Training calendar | Monthly |

### 12.3 Evaluation Process

1. Training Coordinator compiles KPI data monthly and reports to Head of Quality
2. Quarterly management review includes training effectiveness analysis
3. KPIs below target trigger a root cause investigation and corrective action plan
4. Corrective actions may include: curriculum revision, trainer requalification, delivery method change, additional resource allocation
5. Annual training program review assesses overall effectiveness and incorporates lessons learned

---

## 13. Training Material Management

### 13.1 Version Control

- All training materials are stored in the document control system with version numbers
- Version numbering follows the format: Major.Minor (e.g., 1.0, 1.1, 2.0)
- Major version changes (content changes affecting learning objectives or assessment criteria) require QA Lead approval
- Minor version changes (formatting, clarifications, typo corrections) require Training Coordinator approval
- Every version includes an effective date and supersedes the previous version
- Superseded versions are archived (not deleted) and marked "SUPERSEDED - DO NOT USE"

### 13.2 Material Development and Review

| Step | Responsible | Timeline | Deliverable |
|------|------------|----------|-------------|
| Draft training material | Subject Matter Expert | Per project plan | Draft document |
| Technical accuracy review | Peer SME (different from author) | 5 business days | Review comments |
| Incorporate review comments | Author | 3 business days | Revised draft |
| QA review (GxP alignment, ALCOA+ compliance) | QA Lead | 5 business days | QA review comments |
| Final revision | Author | 3 business days | Final draft |
| Approval | Training Coordinator + QA Lead | 3 business days | Approved material with signatures |
| Release to document control system | Training Coordinator | 1 business day | Controlled document |

### 13.3 Material Update Triggers

- Regulatory change affecting training content
- Platform version update changing workflows or features
- SLM module update changing extraction behavior
- Ontology version update
- Audit finding identifying training material gap
- Assessment results indicating content is unclear or insufficient (>20% failure rate on specific questions)
- Trainee feedback indicating content improvement needed
- Client-specific requirement change

### 13.4 Material Types and Standards

| Material Type | Format Standard | Review Cycle |
|---------------|----------------|-------------|
| Instructor-led presentations | Branded template, maximum 40 slides per module, speaker notes required | Annual + trigger-based |
| Hands-on exercise guides | Step-by-step format with screenshots, expected results documented | Per platform version change |
| Assessment question banks | Minimum 3x questions per assessment (rotation), answer key with rationale | Annual + trigger-based |
| Reference guides | Searchable PDF or web-based, version-controlled | Per content change |
| Video recordings (if used) | Maximum 15 minutes per segment, captioned, version labeled | Per content change |

---

## 14. Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Head of Quality** | Approve training SOP and major revisions; review training KPIs quarterly; authorize training suspension decisions; sponsor training program resources |
| **Head of Operations** | Ensure adequate staffing for training delivery; authorize training schedules; escalation point for competency concerns; approve extended onboarding decisions |
| **Training Coordinator** | Maintain training matrix and calendar; schedule training sessions; track completion and overdue items; compile KPI reports; manage training records; coordinate assessments; issue training completion certificates |
| **QA Lead** | Review training materials for GxP compliance; audit training records quarterly; assess training-related deviations; approve training material content changes; participate in competency assessments for all roles |
| **Subject Matter Experts (per role)** | Develop role-specific training materials; deliver instructor-led training; develop assessment questions; conduct practical assessments; mentor trainees during supervised execution |
| **Mentor (assigned per trainee)** | Guide trainee during onboarding; supervise task execution during Weeks 5-6; provide daily feedback; co-sign trainee work products; report readiness for competency assessment |
| **Trainee** | Complete assigned training on schedule; pass assessments at required thresholds; maintain personal training log; report training gaps or concerns; comply with competency level restrictions |
| **Hiring Manager** | Assign training mentor; ensure new hire begins training on Day 1; support training schedule adherence; participate in final competency review |
| **DevOps** | Provision training environment access; maintain staging/demo environments for hands-on training; support IT security training delivery |

---

## Appendix A - Training Record Template

### TRAINING RECORD FORM

**Form ID:** TRF-2026-[Sequential Number]
**Controlled Document - Do Not Reproduce Without Authorization**

---

**Section 1: Trainee Information**

| Field | Entry |
|-------|-------|
| Trainee Full Name | _________________________ |
| Employee ID | _________________________ |
| Role / Title | _________________________ |
| Department | _________________________ |
| Hire Date | _________________________ |
| Current Competency Level | [ ] Level 0 [ ] Level 1 [ ] Level 2 [ ] Level 3 [ ] Level 4 |

---

**Section 2: Training Event Details**

| Field | Entry |
|-------|-------|
| Training Module ID | _________________________ |
| Training Module Title | _________________________ |
| Training Type | [ ] Initial [ ] Refresher [ ] Remediation [ ] Client-Specific [ ] Triggered |
| Training Method | [ ] Instructor-Led [ ] E-Learning [ ] OJT [ ] Self-Study [ ] Blended |
| Training Date(s) | From: _____________ To: _____________ |
| Total Duration (hours) | _________________________ |
| Training Location / Platform | _________________________ |
| Trainer Name | _________________________ |
| Trainer Qualification | _________________________ |

---

**Section 3: Assessment Results**

| Field | Entry |
|-------|-------|
| Assessment Type | [ ] Written Test [ ] Practical Demo [ ] Supervised Execution [ ] Oral Exam [ ] Portfolio Review |
| Assessment Date | _________________________ |
| Assessor Name | _________________________ |
| Score / Result | _________________________ |
| Pass Threshold | _________________________ |
| Result | [ ] PASS [ ] FAIL |
| If FAIL - Reassessment Number | [ ] 1st [ ] 2nd |
| Reassessment Date (if applicable) | _________________________ |
| Reassessment Result | _________________________ |

---

**Section 4: Competency Determination**

| Field | Entry |
|-------|-------|
| New Competency Level Assigned | [ ] Level 0 [ ] Level 1 [ ] Level 2 [ ] Level 3 [ ] Level 4 |
| Authorized Tasks (list or reference role matrix) | _________________________ |
| Restrictions (if any) | _________________________ |
| Next Refresher Training Due | _________________________ |

---

**Section 5: Signatures**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Trainee | _____________ | _____________ | _____________ |
| Trainer | _____________ | _____________ | _____________ |
| Assessor (if different) | _____________ | _____________ | _____________ |
| Training Coordinator | _____________ | _____________ | _____________ |

---

**Section 6: Comments / Notes**

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

---

## Appendix B - Competency Assessment Form Template

### COMPETENCY ASSESSMENT FORM

**Form ID:** CAF-2026-[Sequential Number]
**Controlled Document - Do Not Reproduce Without Authorization**

---

**Section 1: Assessment Information**

| Field | Entry |
|-------|-------|
| Trainee Full Name | _________________________ |
| Employee ID | _________________________ |
| Role / Title | _________________________ |
| Assessment Type | [ ] Initial Competency [ ] Refresher [ ] Reassessment [ ] Role Change |
| Assessment Date | _________________________ |
| Assessor(s) | _________________________ |

---

**Section 2: Written Examination (if applicable)**

| Field | Entry |
|-------|-------|
| Exam ID / Version | _________________________ |
| Number of Questions | _________________________ |
| Correct Answers | _________________________ |
| Score (%) | _________________________ |
| Pass Threshold (%) | _________________________ |
| Result | [ ] PASS [ ] FAIL |

**Questions Answered Incorrectly (list question numbers and topics for remediation tracking):**

| Question # | Topic Area | Correct Answer Provided in Review |
|-----------|-----------|----------------------------------|
| _________ | _________ | [ ] Yes [ ] No |
| _________ | _________ | [ ] Yes [ ] No |
| _________ | _________ | [ ] Yes [ ] No |

---

**Section 3: Practical Demonstration (if applicable)**

**Instructions:** Assess each task against the criteria below. Mark each step as Satisfactory (S), Unsatisfactory (U), or Not Applicable (N/A). All items marked with an asterisk (*) are critical steps - all critical steps must be marked Satisfactory for an overall pass.

| Step # | Task Description | Critical | S / U / N/A | Assessor Notes |
|--------|-----------------|----------|-------------|----------------|
| 1 | _________________________ | [ ]* | _______ | _________________________ |
| 2 | _________________________ | [ ]* | _______ | _________________________ |
| 3 | _________________________ | [ ]* | _______ | _________________________ |
| 4 | _________________________ | [ ]* | _______ | _________________________ |
| 5 | _________________________ | [ ]* | _______ | _________________________ |
| 6 | _________________________ | [ ]* | _______ | _________________________ |
| 7 | _________________________ | [ ]* | _______ | _________________________ |
| 8 | _________________________ | [ ]* | _______ | _________________________ |
| 9 | _________________________ | [ ]* | _______ | _________________________ |
| 10 | _________________________ | [ ]* | _______ | _________________________ |

| Summary | Count |
|---------|-------|
| Total Steps Assessed | _______ |
| Critical Steps - Satisfactory | _______ / _______ |
| Non-Critical Steps - Satisfactory | _______ / _______ |
| Overall Practical Result | [ ] PASS [ ] FAIL |

---

**Section 4: Supervised Execution (if applicable)**

| Execution Cycle | Date | Task Performed | Critical Errors | Non-Critical Errors | Assessor Initials |
|----------------|------|---------------|-----------------|---------------------|-------------------|
| Cycle 1 | _______ | _________________________ | _______ | _______ | _______ |
| Cycle 2 | _______ | _________________________ | _______ | _______ | _______ |
| Cycle 3 | _______ | _________________________ | _______ | _______ | _______ |

| Supervised Execution Summary | Entry |
|-----------------------------|-------|
| Total Cycles Completed | _______ |
| Cycles with Critical Errors | _______ |
| Overall Supervised Execution Result | [ ] PASS [ ] FAIL |

---

**Section 5: Overall Competency Determination**

| Component | Result | Weight |
|-----------|--------|--------|
| Written Examination | [ ] PASS [ ] FAIL [ ] N/A | _______ |
| Practical Demonstration | [ ] PASS [ ] FAIL [ ] N/A | _______ |
| Supervised Execution | [ ] PASS [ ] FAIL [ ] N/A | _______ |

| Overall Determination | Entry |
|----------------------|-------|
| **OVERALL RESULT** | [ ] COMPETENT [ ] NOT YET COMPETENT [ ] COMPETENT WITH RESTRICTIONS |
| Competency Level Assigned | [ ] Level 0 [ ] Level 1 [ ] Level 2 [ ] Level 3 [ ] Level 4 |
| Restrictions (if any) | _________________________ |
| Remediation Required | [ ] Yes [ ] No |
| Remediation Plan (if yes) | _________________________ |
| Reassessment Date (if applicable) | _________________________ |

---

**Section 6: Assessor Recommendation and Comments**

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

---

**Section 7: Signatures**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Primary Assessor | _____________ | _____________ | _____________ |
| Secondary Assessor (if applicable) | _____________ | _____________ | _____________ |
| Trainee (acknowledgment) | _____________ | _____________ | _____________ |
| Training Coordinator | _____________ | _____________ | _____________ |
| QA Lead (for Level 3/4 certifications) | _____________ | _____________ | _____________ |

---

## Appendix C - Training Matrix Summary

### Role-to-Module Mapping

| Module | Data Engineer | ML Engineer | Reg SME | QA Lead | Demo Lead | DevOps | Med/Clinical |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CORE-001 through CORE-009 | M | M | M | M | M | M | M |
| DE-001 through DE-009 | M | - | - | - | - | - | - |
| ML-001 through ML-011 | - | M | - | - | - | - | - |
| REG-001 through REG-007 | - | - | M | - | - | - | - |
| QA-001 through QA-008 | - | - | - | M | - | - | - |
| DM-001 through DM-007 | - | - | - | - | M | - | - |
| DO-001 through DO-009 | - | - | - | - | - | M | - |
| MC-001 through MC-007 | - | - | - | - | - | - | M |
| CS-SAN-001 (RAISE) | R | R | M | M | M | R | R |
| CS-SAN-002 (ARTEMIS) | M | M | - | - | - | M | - |
| CS-SAN-003 (Demo) | - | - | M | - | M | - | - |
| CS-SAN-004 (Data Req) | M | M | - | - | - | M | - |
| CS-SAN-005 (Audit Prep) | - | - | - | M | - | - | - |

**Key:** M = Mandatory, R = Recommended, - = Not Required

---

## Revision History

| Version | Date | Author | Change Description | Approved By |
|---------|------|--------|-------------------|-------------|
| 1.0 | 2026-03-25 | ArcaScience Quality Assurance | Initial release | Head of Quality / Head of Operations |

---

**END OF DOCUMENT**

*This document is the property of ArcaScience. Unauthorized reproduction or distribution is prohibited. This is a controlled document - verify current version before use.*
