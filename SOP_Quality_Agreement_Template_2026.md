# Quality Agreement

## BRA Platform Services - ArcaScience SAS

---

| Field | Value |
|---|---|
| **Document ID** | QA-ARCA-BRA-2026-001 |
| **Version** | 1.0 |
| **Effective Date** | 2026-03-25 |
| **Review Date** | 2027-03-25 |
| **Classification** | Confidential - GxP Regulated |
| **Document Type** | Quality Agreement (Pharmaceutical Services) |
| **Regulatory Basis** | EU GMP Annex 16, ICH Q10, FDA 21 CFR Part 11, GAMP 5 |
| **Prepared By** | ArcaScience Quality Assurance |
| **Status** | Draft - For Mutual Execution |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Reference Documents and Regulatory Framework](#2-reference-documents-and-regulatory-framework)
3. [Definitions and Abbreviations](#3-definitions-and-abbreviations)
4. [Roles and Responsibilities](#4-roles-and-responsibilities)
5. [Quality Management System Requirements](#5-quality-management-system-requirements)
6. [Change Control Procedures](#6-change-control-procedures)
7. [Deviation and CAPA Management](#7-deviation-and-capa-management)
8. [Data Integrity Requirements (ALCOA+)](#8-data-integrity-requirements-alcoa)
9. [Audit Rights and Inspection Support](#9-audit-rights-and-inspection-support)
10. [Validation Requirements (GAMP 5 Category 5)](#10-validation-requirements-gamp-5-category-5)
11. [Training Requirements](#11-training-requirements)
12. [Document and Record Management](#12-document-and-record-management)
13. [Subcontractor Management](#13-subcontractor-management)
14. [Complaints Handling](#14-complaints-handling)
15. [Regulatory Notification Obligations](#15-regulatory-notification-obligations)
16. [Termination and Transition](#16-termination-and-transition)
17. [Signature Block](#17-signature-block)
18. [Appendices](#18-appendices)

---

## 1. Purpose and Scope

### 1.1 Purpose

This Quality Agreement ("Agreement") defines the quality-related roles, responsibilities, and obligations between the Sponsor (hereinafter "Sponsor" or "Client") and ArcaScience SAS (hereinafter "ArcaScience" or "Service Provider") in relation to the provision of the Benefit-Risk Assessment (BRA) platform and associated services.

This Agreement ensures that all GxP-regulated activities performed by ArcaScience on behalf of the Sponsor are conducted in compliance with applicable regulatory requirements, industry standards, and the quality expectations of both parties.

### 1.2 Scope

This Agreement covers the following ArcaScience BRA Platform services and deliverables:

| Service Component | Description |
|---|---|
| **Document Ingestion** | Automated intake of clinical, regulatory, and safety documents |
| **Classification and Section ID** | AI-driven classification using 24 task-specific Small Language Models (SLMs) |
| **Entity Extraction** | Clinician-trained NLP extraction of clinical entities |
| **Relation Extraction** | Identification of entity relationships from source documents |
| **Terminology Normalization** | Mapping to MedDRA, SNOMED CT, and ChEBI controlled vocabularies |
| **Knowledge Graph Assembly** | Construction of structured knowledge representations |
| **Templated Output Generation** | Production of standardized deliverables |

**Platform Output Types Covered:**

1. Disease Analysis Reports
2. Clinical Landscape and Efficacy Reports
3. Clinical Endpoint Studies
4. Adverse Event (AE) Reports
5. Benefit-Risk Assessment (BRA) Reports
6. BRA Summary Reports

**Framework Alignment:** All outputs are aligned with the BRAT (Benefit-Risk Action Team) and CIOMS XII (Council for International Organizations of Medical Sciences) frameworks for structured benefit-risk assessment.

### 1.3 Out of Scope

This Agreement does not cover:

- [ ] Clinical trial conduct or patient-facing activities
- [ ] Regulatory submission filing (unless explicitly contracted)
- [ ] Medical decision-making or clinical judgment
- [ ] Pharmacovigilance case processing (ArcaScience provides data extraction only)
- [ ] Activities performed by the Sponsor's internal teams using exported data

### 1.4 Relationship to Other Agreements

This Quality Agreement supplements and is incorporated by reference into the Master Services Agreement (MSA) between the parties. In the event of a conflict between this Quality Agreement and the MSA on quality-related matters, the terms of this Quality Agreement shall prevail.

---

## 2. Reference Documents and Regulatory Framework

### 2.1 Regulatory References

| Reference | Title | Applicability |
|---|---|---|
| FDA 21 CFR Part 11 | Electronic Records; Electronic Signatures | Electronic records, audit trails, access controls |
| EU GMP Annex 11 | Computerised Systems | Computerized system validation and operation |
| ICH Q10 | Pharmaceutical Quality System | Quality management system framework |
| ICH Q9 | Quality Risk Management | Risk-based approach to quality decisions |
| ICH E9(R1) | Statistical Principles - Estimands | Clinical endpoint analysis methodology |
| ICH M4E(R2) | Common Technical Document - Efficacy | Efficacy data presentation standards |
| EU GMP Annex 16 | Certification by a Qualified Person and Batch Release | Qualified Person responsibilities |
| GAMP 5 (2nd Ed.) | A Risk-Based Approach to Compliant GxP Computerized Systems | Software validation framework |
| ISPE Data Integrity Guide | Data Integrity by Design | ALCOA+ principles and implementation |
| CIOMS XII | Benefit-Risk Balance for Marketed Drugs | Benefit-risk assessment framework |

### 2.2 ArcaScience Internal References

| Document ID | Title |
|---|---|
| ARCA-QMS-001 | ArcaScience Quality Management System Manual |
| ARCA-SOP-VAL-001 | Computer System Validation Master Plan |
| ARCA-SOP-DI-001 | Data Integrity Policy and Procedures |
| ARCA-SOP-CHG-001 | Change Control Procedure |
| ARCA-SOP-DEV-001 | Deviation and CAPA Management |
| ARCA-SOP-TRN-001 | Training Management Procedure |
| ARCA-SOP-DOC-001 | Document and Record Control |
| ARCA-SOP-AUD-001 | Audit Management Procedure |
| ARCA-SOP-SUB-001 | Subcontractor Qualification and Oversight |
| ARCA-VMP-BRA-001 | BRA Platform Validation Master Plan |

---

## 3. Definitions and Abbreviations

### 3.1 Definitions

| Term | Definition |
|---|---|
| **GxP** | A general abbreviation for "Good Practice" regulations and guidelines. Includes GMP (Good Manufacturing Practice), GCP (Good Clinical Practice), GLP (Good Laboratory Practice), GVP (Good Pharmacovigilance Practice), and GDP (Good Distribution Practice). |
| **ALCOA+** | An acronym for data integrity principles: Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, and Available. |
| **GAMP 5** | Good Automated Manufacturing Practice, 5th edition. An ISPE guide providing a risk-based approach to compliant GxP computerized systems. ArcaScience's BRA platform is classified as Category 5 (Custom Software). |
| **GAMP 5 Category 5** | Custom (Bespoke) Software - software designed to meet the specific needs of a regulated business process. Requires full lifecycle validation including requirements specification, design specification, code review, and testing at unit, integration, and system levels. |
| **21 CFR Part 11** | FDA regulation establishing criteria for acceptance of electronic records and electronic signatures. Requires controls including audit trails, access controls, authority checks, and electronic signature authentication. |
| **Small Language Model (SLM)** | A task-specific, purpose-trained language model designed for a defined NLP task (e.g., named entity recognition, relation extraction). ArcaScience deploys 24 SLMs, each clinician-trained for specific clinical and regulatory extraction tasks. |
| **CAPA** | Corrective and Preventive Action. A systematic approach to investigating, understanding, and correcting discrepancies while preventing their recurrence. |
| **Deviation** | A departure from an approved instruction, standard operating procedure, specification, or established standard. |
| **Change Control** | A formal process for proposing, documenting, evaluating, approving, implementing, and reviewing changes to validated systems, processes, or documents. |
| **Audit Trail** | A secure, computer-generated, time-stamped electronic record that allows reconstruction of the course of events relating to creation, modification, or deletion of an electronic record. |
| **Cryptographic Hash Chaining** | A method of securing audit trail integrity by computing a cryptographic hash of each record that includes the hash of the preceding record, creating a tamper-evident chain. Used by ArcaScience for ALCOA+ compliance. |
| **Knowledge Graph** | A structured representation of entities and their relationships extracted from source documents, used by the BRA platform to synthesize benefit-risk information. |
| **Qualified Person (QP)** | An individual responsible for certification of regulatory compliance within the Sponsor's organization. |
| **Critical Quality Attribute (CQA)** | A characteristic of a system output that must be within an appropriate limit, range, or distribution to ensure desired quality. |
| **BRAT Framework** | Benefit-Risk Action Team framework for structured, transparent benefit-risk assessment. |
| **CIOMS XII** | A report by the Council for International Organizations of Medical Sciences providing a framework for benefit-risk balance evaluation of marketed drugs. |
| **RAISE Framework** | Responsible AI framework with five pillars: Accountable, Fair and Ethical, Robust and Safe, Transparent and Explainable, Eco-Responsible. Referenced for engagements requiring responsible AI compliance. |

### 3.2 Abbreviations

| Abbreviation | Full Term |
|---|---|
| AE | Adverse Event |
| BRA | Benefit-Risk Assessment |
| CAPA | Corrective and Preventive Action |
| ChEBI | Chemical Entities of Biological Interest |
| DAG | Directed Acyclic Graph (Apache Airflow workflow) |
| DI | Data Integrity |
| DQ | Design Qualification |
| FAT | Factory Acceptance Testing |
| FDA | U.S. Food and Drug Administration |
| FTE | Full-Time Equivalent |
| GAMP | Good Automated Manufacturing Practice |
| GxP | Good "x" Practice (collective) |
| IQ | Installation Qualification |
| ISPE | International Society for Pharmaceutical Engineering |
| MedDRA | Medical Dictionary for Regulatory Activities |
| MSA | Master Services Agreement |
| NLP | Natural Language Processing |
| OQ | Operational Qualification |
| PQ | Performance Qualification |
| QA | Quality Assurance |
| QMS | Quality Management System |
| SAT | Site Acceptance Testing |
| SLM | Small Language Model |
| SNOMED CT | Systematized Nomenclature of Medicine - Clinical Terms |
| SOP | Standard Operating Procedure |
| URS | User Requirements Specification |
| VMP | Validation Master Plan |

---

## 4. Roles and Responsibilities

### 4.1 Responsibility Matrix (RACI)

The following matrix assigns responsibilities using the RACI model:
- **R** = Responsible (performs the work)
- **A** = Accountable (ultimate authority and decision-maker)
- **C** = Consulted (provides input before action)
- **I** = Informed (notified after action)

| Activity | Sponsor | ArcaScience |
|---|---|---|
| **Quality Management** | | |
| Maintain Quality Management System for BRA platform | I | R/A |
| Define GxP requirements for platform outputs | R/A | C |
| Approve Quality Agreement and amendments | R/A | R |
| Annual Quality Agreement review | R/A | R |
| **Validation** | | |
| Maintain BRA Platform Validation Master Plan | C | R/A |
| Execute IQ/OQ/PQ for platform releases | I | R/A |
| Approve validation summary reports | R/A | R |
| Maintain validated state of infrastructure | I | R/A |
| Define User Acceptance Testing (UAT) criteria | R/A | C |
| Execute UAT | R/A | C |
| **Change Control** | | |
| Initiate change requests (platform-side) | I | R/A |
| Initiate change requests (requirements-side) | R/A | I |
| Assess change impact on validated state | C | R/A |
| Approve changes affecting GxP outputs | R/A | C |
| Implement approved changes | I | R/A |
| **Deviation and CAPA** | | |
| Report deviations affecting Sponsor data/outputs | A | R |
| Investigate root cause of deviations | C | R/A |
| Implement CAPAs | I | R/A |
| Verify CAPA effectiveness | C | R/A |
| **Data Integrity** | | |
| Maintain ALCOA+ compliance for platform records | I | R/A |
| Maintain cryptographic hash chain integrity | I | R/A |
| Define data integrity requirements for outputs | R/A | C |
| Perform periodic data integrity assessments | C | R/A |
| **Audit and Inspection** | | |
| Conduct supplier audits of ArcaScience | R/A | R |
| Support regulatory inspections | R/A | R |
| Provide audit trail extracts on request | A | R |
| **Training** | | |
| Train ArcaScience personnel on platform SOPs | I | R/A |
| Train Sponsor users on platform operation | C | R/A |
| Maintain training records for ArcaScience staff | I | R/A |
| **Document Management** | | |
| Maintain platform documentation (SOPs, specs) | I | R/A |
| Archive GxP records per retention policy | R | R/A |
| Provide records upon Sponsor request | A | R |
| **Subcontractor Oversight** | | |
| Qualify and monitor subcontractors | I | R/A |
| Notify Sponsor of subcontractor changes | A | R |
| **Regulatory** | | |
| Notify Sponsor of regulatory findings | A | R |
| Respond to regulatory authority queries | R/A | R |
| File regulatory submissions | R/A | I |

### 4.2 Key Contacts

| Role | Sponsor | ArcaScience |
|---|---|---|
| Quality Agreement Owner | [Name / Title] | [Name / Title] |
| Quality Assurance Lead | [Name / Title] | [Name / Title] |
| Technical Lead | [Name / Title] | [Name / Title] |
| Data Protection Officer | [Name / Title] | [Name / Title] |
| Regulatory Affairs Contact | [Name / Title] | [Name / Title] |
| Escalation Contact (L1) | [Name / Title] | [Name / Title] |
| Escalation Contact (L2 - Executive) | [Name / Title] | [Name / Title] |

### 4.3 Communication and Escalation

**Routine Communications:**
- Joint Quality Review Meetings: Quarterly (minimum)
- Operational Status Calls: As defined in the MSA
- Quality Metrics Reporting: Monthly

**Escalation Path:**

| Level | Timeframe | Trigger | Participants |
|---|---|---|---|
| Level 1 - Operational | Within 2 business days | Minor deviations, routine quality queries | QA Leads from both parties |
| Level 2 - Management | Within 5 business days | Major deviations, CAPA disagreements, audit findings | Quality Directors / Heads of Quality |
| Level 3 - Executive | Within 10 business days | Critical quality failures, regulatory findings, unresolved Level 2 issues | Executive sponsors from both parties |

**Critical Notification Timelines:**

| Event Type | Notification Deadline | Method |
|---|---|---|
| Data breach or integrity failure | Within 24 hours | Phone + written confirmation |
| Regulatory inspection notification | Within 48 hours | Email to Quality Agreement Owner |
| Critical deviation impacting Sponsor data | Within 24 hours | Phone + written confirmation |
| Major system outage affecting GxP data | Within 4 hours | Phone + email |

---

## 5. Quality Management System Requirements

### 5.1 ArcaScience QMS Overview

ArcaScience maintains a Quality Management System compliant with ICH Q10 principles, adapted for a computational platform services organization. The QMS encompasses the following elements:

| QMS Element | Requirement | Evidence |
|---|---|---|
| Quality Policy | Documented, communicated, reviewed annually | ARCA-QMS-001 |
| Quality Objectives | Measurable, tracked, reported quarterly | Quality Management Review minutes |
| Management Review | Conducted at minimum annually | Management Review meeting minutes |
| Internal Audits | Conducted at minimum annually per audit schedule | Internal audit reports |
| Risk Management | ICH Q9-based risk assessments for all GxP processes | Risk assessment records |
| Document Control | Controlled document system with version management | Document control system |
| Training Management | Role-based training curricula, competency verification | Training records |
| Supplier Management | Qualification, monitoring, and re-evaluation of suppliers | Supplier qualification files |

### 5.2 Quality Metrics

ArcaScience shall track and report the following quality metrics to the Sponsor on a monthly basis:

| Metric | Target | Measurement Method |
|---|---|---|
| AE Extraction F1 Score | >= 92% | Automated benchmarking against gold-standard annotated corpus |
| NLP Pipeline F1 Score | >= 94% | Automated benchmarking against gold-standard annotated corpus |
| Signal Detection Improvement | >= 3x vs. manual baseline | Comparative analysis per validated protocol |
| Open Deviation Count | <= 5 at any time | Deviation tracking system |
| CAPA On-Time Closure Rate | >= 95% | CAPA tracking system |
| System Availability (GxP services) | >= 99.5% | Infrastructure monitoring |
| Audit Trail Integrity (hash chain) | 100% | Automated cryptographic verification |
| Change Control On-Time Completion | >= 90% | Change control tracking system |
| Training Compliance Rate | >= 98% | Training management system |

### 5.3 Management Review

ArcaScience shall conduct management reviews at minimum annually, covering:

- [ ] Quality metric trends and analysis
- [ ] Deviation and CAPA summary and trend analysis
- [ ] Change control summary
- [ ] Audit findings (internal and external)
- [ ] Regulatory intelligence and impact assessment
- [ ] Customer complaint summary
- [ ] Resource adequacy assessment (current team: 14 FTEs)
- [ ] Risk register review and updates
- [ ] Validation status and revalidation needs
- [ ] Training compliance status

The Sponsor shall receive a summary of the management review within 30 calendar days of its completion.

### 5.4 Continuous Improvement

ArcaScience is committed to continual improvement of the BRA platform quality. Improvement initiatives may be triggered by:

- Trend analysis of quality metrics
- Audit observations
- CAPA effectiveness reviews
- Regulatory guidance updates
- Client feedback and complaint analysis
- Advances in NLP and SLM methodologies
- Updates to MedDRA, SNOMED CT, or ChEBI terminologies

---

## 6. Change Control Procedures

### 6.1 Scope of Change Control

All changes to the validated BRA platform that may impact GxP-regulated outputs are subject to formal change control. This includes but is not limited to:

| Change Category | Examples |
|---|---|
| **Software Changes** | SLM retraining or model updates, NLP pipeline modifications, API changes (FastAPI/NestJS), output template modifications |
| **Infrastructure Changes** | Apache Airflow DAG modifications, S3 bucket configuration, ElasticSearch cluster changes, DocumentDB schema updates, QDrant vector DB configuration, compute resource scaling |
| **Terminology Updates** | MedDRA version upgrades, SNOMED CT release updates, ChEBI ontology updates |
| **Process Changes** | SOP revisions, workflow modifications, role/responsibility changes |
| **Configuration Changes** | Extraction thresholds, classification parameters, normalization rules, Knowledge Graph schema changes |

### 6.2 Change Classification

| Classification | Definition | Approval Authority | Sponsor Notification |
|---|---|---|---|
| **Critical** | Change that directly affects the validated state of GxP outputs, data integrity controls, or regulatory compliance | ArcaScience QA Head + Sponsor QA Lead | Prior written approval required |
| **Major** | Change that may indirectly affect GxP output quality, system performance, or audit trail functionality | ArcaScience QA Head | Notification with 10 business days advance notice |
| **Minor** | Change with no impact on GxP outputs, data integrity, or compliance (e.g., cosmetic UI changes, non-GxP documentation updates) | ArcaScience QA Manager | Included in monthly quality report |
| **Emergency** | Urgent change required to address an active data integrity risk, security vulnerability, or regulatory non-compliance | ArcaScience QA Head (verbal) + retrospective written approval | Immediate notification (within 4 hours) |

### 6.3 Change Control Process

**Step-by-step procedure:**

1. **Initiation**
   - Change requester completes Change Request Form (ARCA-FORM-CHG-001)
   - Includes description, rationale, classification proposal, and risk assessment

2. **Impact Assessment**
   - [ ] Impact on validated state (IQ/OQ/PQ implications)
   - [ ] Impact on 24 SLM model performance metrics
   - [ ] Impact on ALCOA+ data integrity controls
   - [ ] Impact on audit trail (cryptographic hash chain)
   - [ ] Impact on 21 CFR Part 11 compliance
   - [ ] Impact on terminology normalization accuracy
   - [ ] Impact on Knowledge Graph integrity
   - [ ] Impact on output template compliance (BRAT/CIOMS XII)
   - [ ] Regression risk to existing validated functions
   - [ ] Training requirements for affected personnel

3. **Classification and Routing**
   - QA classifies the change per Section 6.2
   - Critical changes routed to Sponsor for review and approval
   - Major changes communicated to Sponsor with implementation timeline

4. **Approval**
   - All approvals documented with electronic signatures (21 CFR Part 11 compliant)
   - Critical changes require joint approval from both parties

5. **Implementation**
   - Changes implemented per approved plan
   - All code, configuration, and infrastructure changes version-controlled
   - Implementation documented with before/after evidence

6. **Verification and Validation**
   - Appropriate re-validation activities performed (see Section 10)
   - Regression testing executed and documented
   - Performance metrics verified against established thresholds

7. **Closure**
   - Implementation verified by QA
   - Documentation updated (SOPs, specifications, training materials)
   - Change record closed with effectiveness review date set

### 6.4 Change Control Records

All change control records shall be maintained for the duration of this Agreement plus the retention period specified in Section 12. Records shall include:

- Change Request Form with unique identifier
- Impact assessment documentation
- Approval signatures with timestamps
- Implementation evidence
- Validation/verification test results
- Updated documentation list
- Closure sign-off

---

## 7. Deviation and CAPA Management

### 7.1 Deviation Classification

| Classification | Definition | Investigation Deadline | Sponsor Notification |
|---|---|---|---|
| **Critical** | Deviation that results in or may result in incorrect GxP output data, loss of data integrity, breach of ALCOA+ principles, or regulatory non-compliance | 5 business days (root cause) | Within 24 hours of detection |
| **Major** | Deviation that may affect the quality of platform outputs but does not compromise data integrity or regulatory compliance | 15 business days (root cause) | Within 3 business days |
| **Minor** | Deviation with no direct impact on output quality, data integrity, or compliance | 30 business days (root cause) | Included in monthly quality report |

### 7.2 Deviation Management Process

**Step-by-step procedure:**

1. **Detection and Reporting**
   - Any ArcaScience team member identifies and reports the deviation
   - Deviation logged in the deviation tracking system with unique identifier
   - Initial classification assigned
   - Sponsor notified per timelines in Section 7.1

2. **Containment**
   - Immediate containment actions defined and implemented
   - Affected outputs identified and quarantined if necessary
   - Impact assessment on previously delivered outputs completed
   - Sponsor notified if previously delivered outputs may be affected

3. **Investigation**
   - Root cause analysis conducted using appropriate methodology:
     - [ ] 5 Whys Analysis
     - [ ] Fishbone (Ishikawa) Diagram
     - [ ] Fault Tree Analysis
     - [ ] Timeline / Event Mapping
   - Contributing factors identified
   - Extent of impact determined

4. **CAPA Determination**
   - Corrective actions defined to address the root cause
   - Preventive actions defined to prevent recurrence
   - CAPA plan documented with responsible parties and deadlines

5. **CAPA Implementation**
   - CAPAs implemented per approved plan
   - Implementation evidence documented
   - Affected SOPs, specifications, and configurations updated

6. **Effectiveness Check**
   - Effectiveness verification performed after defined period
   - Verification criteria established at time of CAPA approval
   - If ineffective, deviation re-opened and additional CAPA defined

7. **Closure**
   - Deviation and CAPA records reviewed and closed by QA
   - Trend data updated
   - Lessons learned documented

### 7.3 Deviation and CAPA Examples Specific to BRA Platform

| Example Scenario | Classification | Typical CAPA |
|---|---|---|
| SLM model produces AE extraction F1 below 92% threshold | Critical | Model retraining, validation re-execution, output re-generation for affected period |
| Cryptographic hash chain integrity check failure | Critical | Root cause analysis of chain break, integrity restoration, affected records flagged, security audit |
| MedDRA term mapping error in normalized output | Major | Terminology dictionary update, regression testing, affected output re-generation |
| Apache Airflow DAG failure causing incomplete processing | Major | DAG repair, re-processing of affected documents, pipeline monitoring enhancement |
| Minor UI display issue in report formatting | Minor | Frontend fix, regression testing |
| Training record gap identified during audit | Major | Retrospective training completion, training process SOP update |

### 7.4 Trending and Reporting

ArcaScience shall perform trend analysis of deviations on a quarterly basis, covering:

- Total deviation count by classification
- Deviation trends by category (software, infrastructure, process, human error)
- Root cause category distribution
- CAPA timeliness and effectiveness rates
- Repeat deviation analysis

Trend reports shall be shared with the Sponsor during quarterly quality review meetings.

---

## 8. Data Integrity Requirements (ALCOA+)

### 8.1 ALCOA+ Principle Implementation

ArcaScience implements ALCOA+ data integrity principles across the BRA platform as follows:

| ALCOA+ Principle | Definition | BRA Platform Implementation |
|---|---|---|
| **Attributable** | Data must be attributable to the person or system that generated it | All records linked to authenticated user accounts or system process IDs. Electronic signatures per 21 CFR Part 11. |
| **Legible** | Data must be readable and permanent throughout its lifecycle | Standardized output formats (PDF, structured JSON). No manual overwriting. Archived copies in immutable S3 storage. |
| **Contemporaneous** | Data must be recorded at the time of the activity | Automated timestamps on all processing steps (Airflow DAG execution logs). NTP-synchronized server clocks. |
| **Original** | Data must be the first recording or a certified true copy | Source documents retained in original format in S3. Processing outputs flagged as "derived" with lineage to originals. |
| **Accurate** | Data must be correct, truthful, and reflective of the observation | Validated NLP pipeline (F1 >= 94%). AE extraction validated (F1 >= 92%). Output verification against source enabled. |
| **Complete** | All data must be present, including any re-processing or corrections | Complete processing logs retained. No deletion of records without audit trail entry. Versioning of all outputs. |
| **Consistent** | Data must be self-consistent and consistent across related records | Cross-referencing between Knowledge Graph entities. Terminology normalization to controlled vocabularies (MedDRA, SNOMED CT, ChEBI). |
| **Enduring** | Data must be recorded on approved, durable media | Records stored in redundant cloud infrastructure (S3 with versioning, DocumentDB with replication). Backup and disaster recovery procedures in place. |
| **Available** | Data must be accessible for review throughout its retention period | On-demand access via authenticated APIs. Audit trail extracts exportable. Archive retrieval within defined SLA. |

### 8.2 Cryptographic Hash Chain for Audit Trails

ArcaScience implements cryptographic hash chaining to ensure tamper-evident audit trails:

**How it works:**

1. Each audit trail record is assigned a unique sequential identifier
2. A SHA-256 (or equivalent) cryptographic hash is computed for each record
3. The hash computation includes the content of the current record AND the hash of the immediately preceding record
4. This creates a chain where any modification to a historical record would invalidate the hash of that record and all subsequent records
5. Periodic integrity verification is performed automatically by the system

**Verification Schedule:**

| Verification Type | Frequency | Responsible Party |
|---|---|---|
| Automated hash chain integrity check | Daily (automated) | BRA Platform (Airflow DAG) |
| Manual integrity audit | Quarterly | ArcaScience QA |
| Independent integrity verification | Annually or upon Sponsor request | ArcaScience QA (with Sponsor observer rights) |

**In Case of Integrity Failure:**
- Immediately classified as a Critical Deviation (Section 7.1)
- Sponsor notified within 24 hours
- Affected records quarantined
- Forensic investigation initiated
- Regulatory notification assessed per Section 15

### 8.3 Access Controls

| Control | Implementation |
|---|---|
| **Authentication** | Multi-factor authentication required for all GxP system access |
| **Authorization** | Role-based access control (RBAC) with least-privilege principle |
| **Password Policy** | Minimum 12 characters, complexity requirements, 90-day rotation |
| **Session Management** | Automatic timeout after 15 minutes of inactivity |
| **Access Reviews** | Quarterly review of all user access rights |
| **Privileged Access** | Separate administrative accounts, additional approval required |
| **Deprovisioning** | Access removed within 24 hours of role change or departure |

### 8.4 Electronic Records and Electronic Signatures

Per FDA 21 CFR Part 11, the BRA platform implements:

- [ ] Closed system controls with validated access mechanisms
- [ ] Audit trails for all record creation, modification, and deletion
- [ ] Authority checks ensuring only authorized users can perform specific functions
- [ ] Device checks to verify source of data input where applicable
- [ ] Electronic signatures linked to their respective electronic records
- [ ] Electronic signatures containing the printed name, date/time, and meaning of the signature
- [ ] Electronic signature components (user ID + password) not shared or reused
- [ ] Signature manifestation displayed in human-readable form

### 8.5 Data Integrity Risk Assessment

ArcaScience performs a periodic data integrity risk assessment covering:

| Assessment Area | Frequency | Key Risk Factors Evaluated |
|---|---|---|
| NLP Pipeline Outputs | Semi-annually | Extraction accuracy drift, model degradation, terminology version conflicts |
| Audit Trail System | Annually | Hash chain integrity, timestamp accuracy, completeness of logging |
| Data Storage | Annually | Backup integrity, redundancy, access control effectiveness |
| Data Transfer | Annually | Encryption in transit, completeness verification, integrity checks |
| User Access | Quarterly | Privilege creep, orphaned accounts, shared credentials |

---

## 9. Audit Rights and Inspection Support

### 9.1 Sponsor Audit Rights

The Sponsor retains the right to audit ArcaScience at any time during the term of this Agreement, subject to the following provisions:

| Audit Type | Frequency | Notice Period | Duration |
|---|---|---|---|
| **Routine On-Site Audit** | Once per calendar year (included in agreement) | 30 calendar days written notice | Up to 3 business days |
| **For-Cause Audit** | As needed (triggered by critical deviation, data integrity concern, or regulatory requirement) | 5 business days written notice (or shorter if regulatory urgency) | As needed |
| **Remote/Document Audit** | Twice per calendar year | 15 business days written notice | Up to 2 business days |
| **Follow-Up Audit** | As needed following CAPA verification | 15 business days written notice | Up to 1 business day |

### 9.2 Audit Scope

The Sponsor may audit the following areas:

- [ ] Quality Management System and SOPs
- [ ] BRA Platform validation documentation (IQ/OQ/PQ)
- [ ] SLM training and validation records
- [ ] Data integrity controls and audit trail system
- [ ] Cryptographic hash chain verification records
- [ ] Change control records
- [ ] Deviation and CAPA records
- [ ] Training records for GxP-trained personnel
- [ ] Infrastructure qualification records
- [ ] Subcontractor qualification files
- [ ] Security and access control documentation
- [ ] Disaster recovery and business continuity plans
- [ ] Complaint handling records relevant to Sponsor

### 9.3 Audit Process

1. **Pre-Audit**
   - Sponsor provides written audit notification with scope and agenda
   - ArcaScience confirms dates and assigns audit host
   - Confidentiality agreements signed by all auditors (if not already covered by MSA)

2. **On-Site Conduct**
   - Opening meeting with ArcaScience QA Lead and relevant SMEs
   - Document review and system demonstrations as per agenda
   - Personnel interviews (with appropriate notice)
   - Daily wrap-up meetings to discuss preliminary observations
   - Closing meeting with preliminary findings summary

3. **Post-Audit**
   - Sponsor issues formal audit report within 30 calendar days
   - ArcaScience provides written response with CAPA plan within 20 business days
   - CAPA implementation timelines agreed between both parties
   - CAPA effectiveness verified by Sponsor (remotely or during follow-up audit)

### 9.4 Regulatory Inspection Support

In the event that a regulatory authority (FDA, EMA, MHRA, ANSM, or other competent authority) requests inspection of ArcaScience facilities or records in connection with Sponsor activities:

| Obligation | Responsible Party | Timeline |
|---|---|---|
| Notify other party of inspection | Party receiving inspection notice | Within 48 hours of notification |
| Provide access to relevant facilities and records | ArcaScience | As required by regulatory authority |
| Make knowledgeable personnel available | ArcaScience | During inspection |
| Share inspection report/observations with Sponsor | ArcaScience | Within 5 business days of receipt |
| Develop response to observations (if applicable) | ArcaScience (with Sponsor review for critical findings) | Per regulatory timeline |
| Submit inspection response | ArcaScience (with Sponsor review/approval for critical findings) | Per regulatory timeline |

### 9.5 Audit Trail Access

ArcaScience shall provide the Sponsor with the ability to:

- Request audit trail extracts for specific records, time periods, or users
- Receive audit trail extracts within 5 business days of request
- Verify cryptographic hash chain integrity upon request
- Access a read-only audit trail dashboard (if provisioned under the MSA)

---

## 10. Validation Requirements (GAMP 5 Category 5)

### 10.1 Validation Strategy

The ArcaScience BRA platform is classified as GAMP 5 Category 5 (Custom/Bespoke Software). The validation strategy follows a risk-based lifecycle approach per GAMP 5 Second Edition.

**Validation Lifecycle:**

```
User Requirements Specification (URS)
        |
        v
Functional Requirements Specification (FRS)
        |
        v
Design Specification (DS)
        |
        v
Build / Configuration
        |
        v
Unit Testing <---> Design Specification
        |
        v
Integration Testing <---> Functional Requirements Specification
        |
        v
Operational Qualification (OQ) <---> Functional Requirements Specification
        |
        v
Performance Qualification (PQ) <---> User Requirements Specification
        |
        v
Validation Summary Report
        |
        v
Ongoing Validated State (Periodic Review)
```

### 10.2 Validation Documentation

The following documentation is maintained for the BRA platform:

| Document | Purpose | Approval Authority |
|---|---|---|
| Validation Master Plan (VMP) | Defines overall validation approach, scope, roles, and acceptance criteria | ArcaScience QA Head |
| User Requirements Specification (URS) | Defines what the system must do from a user/regulatory perspective | Joint (Sponsor + ArcaScience) |
| Functional Requirements Specification (FRS) | Defines system functions that satisfy URS | ArcaScience Technical Lead + QA |
| Design Specification (DS) | Defines how the system implements the FRS | ArcaScience Technical Lead |
| Traceability Matrix | Maps URS to FRS to DS to Test Cases | ArcaScience QA |
| Risk Assessment | Identifies and mitigates risks per ICH Q9 | ArcaScience QA + Technical Lead |
| IQ Protocol and Report | Verifies correct installation and configuration | ArcaScience QA |
| OQ Protocol and Report | Verifies system operates per FRS under normal and boundary conditions | ArcaScience QA |
| PQ Protocol and Report | Verifies system performs as intended in the production environment per URS | ArcaScience QA (Sponsor witness/review) |
| Validation Summary Report (VSR) | Summarizes validation activities, results, and residual risks | ArcaScience QA Head |
| Periodic Review Report | Confirms ongoing validated state, identifies revalidation needs | ArcaScience QA |

### 10.3 Validation of BRA Platform Components

| Component | Validation Approach | Key Acceptance Criteria |
|---|---|---|
| **24 SLMs (Task-Specific Models)** | Performance validation against gold-standard annotated datasets. Clinician review of model outputs. | AE Extraction F1 >= 92%. NLP F1 >= 94%. Precision and recall within defined thresholds per model. |
| **Document Ingestion Pipeline** | End-to-end testing with representative document types (PDF, Word, structured/unstructured) | 100% successful ingestion of compliant documents. Error handling for non-compliant formats. |
| **Classification Module** | Testing against pre-classified document corpus | Classification accuracy >= defined threshold per document type |
| **Entity Extraction** | Testing against gold-standard annotated corpus | Entity-level F1, precision, recall per entity type |
| **Relation Extraction** | Testing against gold-standard annotated corpus | Relation-level F1, precision, recall per relation type |
| **Normalization Engine** | Testing mapping accuracy to MedDRA, SNOMED CT, ChEBI | Mapping accuracy >= defined threshold. Correct version-specific mappings. |
| **Knowledge Graph** | Structural integrity testing. Query result validation. | Graph completeness, consistency, and queryability per defined test cases |
| **Templated Output Generation** | Output comparison against expected templates for each of 6 output types | Format compliance, content completeness, traceability to source |
| **Audit Trail System** | End-to-end audit trail capture testing. Hash chain verification. | 100% capture of auditable events. Hash chain integrity verified. |
| **Infrastructure (Airflow, S3, ES, DocumentDB, QDrant)** | IQ for installation. OQ for operational parameters. | All components installed per specifications. Operational parameters within defined ranges. |

### 10.4 Revalidation Triggers

Revalidation (full or partial) shall be triggered by:

- [ ] Major software release or SLM model retraining
- [ ] Infrastructure migration or major configuration change
- [ ] Terminology version upgrade (MedDRA, SNOMED CT, ChEBI)
- [ ] Critical deviation indicating potential validation gap
- [ ] Regulatory requirement change affecting validated functions
- [ ] Periodic review finding indicating drift from validated state
- [ ] Change in hosting environment or cloud service provider
- [ ] Addition of new output type or major modification to existing output templates

### 10.5 Periodic Review

ArcaScience shall conduct a periodic review of the BRA platform's validated state at minimum annually. The review shall cover:

| Review Area | Assessment |
|---|---|
| Validation documentation currency | Are all validation documents current and reflective of the system's present state? |
| Change history impact | Do accumulated changes since last validation warrant revalidation? |
| Deviation and CAPA impact | Have any deviations or CAPAs identified validation gaps? |
| Performance metric trends | Are performance metrics (F1 scores, accuracy) stable or trending? |
| Regulatory landscape | Have new regulations or guidance been issued that affect validation requirements? |
| Infrastructure changes | Have infrastructure components been updated or patched in ways that affect validated state? |
| Model performance drift | Have SLM models shown performance degradation over time? |

The periodic review report shall be available to the Sponsor upon request.

---

## 11. Training Requirements

### 11.1 ArcaScience Personnel Training

All ArcaScience personnel involved in GxP-regulated activities shall be trained and qualified for their assigned roles.

**Training Categories:**

| Category | Content | Frequency | Assessment Method |
|---|---|---|---|
| **GxP Fundamentals** | GMP, GCP, GLP, GVP overview. Regulatory framework. Data integrity principles. | Upon hire + annual refresher | Written assessment (pass >= 80%) |
| **ALCOA+ and Data Integrity** | ALCOA+ principles, 21 CFR Part 11, audit trails, electronic records/signatures | Upon hire + annual refresher | Written assessment (pass >= 80%) |
| **GAMP 5 and Validation** | GAMP 5 lifecycle, Category 5 requirements, IQ/OQ/PQ | Upon assignment to validation role + as needed | Written assessment (pass >= 80%) |
| **SOP-Specific Training** | Each applicable SOP (change control, deviation, CAPA, etc.) | Upon SOP issuance/revision | Read-and-understand acknowledgment + comprehension check |
| **BRA Platform Technical** | Platform architecture, pipeline components, SLM operations, infrastructure | Upon assignment + as needed | Practical demonstration |
| **Quality Agreement Awareness** | Contents and obligations of this Quality Agreement | Upon Agreement execution + annual refresher | Read-and-understand acknowledgment |
| **Information Security** | Access controls, data protection, incident reporting | Upon hire + annual refresher | Written assessment (pass >= 80%) |
| **Responsible AI Principles** | Fair and ethical AI, transparency, explainability, robustness (aligned with RAISE framework where applicable) | Upon hire + annual refresher | Written assessment (pass >= 80%) |

### 11.2 Training Records

ArcaScience shall maintain training records that include:

- [ ] Employee name and unique identifier
- [ ] Training course title and version
- [ ] Date of training completion
- [ ] Trainer name and qualifications
- [ ] Assessment results (where applicable)
- [ ] Training curriculum version
- [ ] Acknowledgment signature (electronic, 21 CFR Part 11 compliant)

### 11.3 Training for Sponsor Users

Where ArcaScience provides training to Sponsor users on platform operation:

| Training Type | Delivery Method | Materials Provided | Records |
|---|---|---|---|
| Initial Platform Training | On-site or remote, instructor-led | User manual, quick reference guide | Attendance record provided to Sponsor |
| Output Interpretation Training | Remote, instructor-led | Output specification documents | Attendance record provided to Sponsor |
| Refresher Training | Remote or self-paced | Updated materials as applicable | Attendance record provided to Sponsor |
| Train-the-Trainer | On-site or remote | Comprehensive training package | Certification record |

### 11.4 Competency Assurance

ArcaScience shall ensure that:

- Personnel are not assigned GxP tasks until training is complete and documented
- Competency is reassessed when significant system or process changes occur
- Training gaps identified during audits or deviations are addressed within 30 calendar days
- A current training matrix is maintained showing personnel, required training, and completion status

---

## 12. Document and Record Management

### 12.1 Document Control

All GxP documents shall be controlled per the following requirements:

| Requirement | Implementation |
|---|---|
| **Unique Identification** | All documents assigned a unique document ID with version number |
| **Version Control** | Sequential version numbering. Only the current approved version is in effect. |
| **Review and Approval** | All GxP documents reviewed and approved by QA before issuance. Approval documented with electronic signatures. |
| **Distribution** | Controlled distribution via document management system. Superseded versions clearly marked. |
| **Periodic Review** | All SOPs and specifications reviewed at minimum every 2 years |
| **Obsolescence** | Superseded documents archived with clear "SUPERSEDED" marking. Retained per retention policy. |

### 12.2 Record Retention

| Record Type | Minimum Retention Period | Storage Requirements |
|---|---|---|
| Validation documentation (VMP, URS, FRS, DS, protocols, reports) | Duration of Agreement + 15 years or per Sponsor requirement, whichever is longer | Secure, backed-up, version-controlled |
| Audit trails and electronic records | Duration of Agreement + 15 years or per Sponsor requirement, whichever is longer | Immutable storage with cryptographic hash chain verification |
| Change control records | Duration of Agreement + 10 years | Secure, backed-up |
| Deviation and CAPA records | Duration of Agreement + 10 years | Secure, backed-up |
| Training records | Duration of employment + 10 years | Secure, backed-up |
| Audit reports (internal and external) | Duration of Agreement + 10 years | Secure, backed-up |
| Batch/processing records (platform output generation logs) | Duration of Agreement + 15 years or per Sponsor requirement | Immutable storage with audit trail |
| Quality metrics and trend reports | Duration of Agreement + 5 years | Secure, backed-up |
| Correspondence and meeting minutes | Duration of Agreement + 5 years | Secure, backed-up |

### 12.3 Record Format and Integrity

- All GxP records shall be maintained in a format that ensures legibility and accessibility throughout the retention period
- Electronic records shall comply with 21 CFR Part 11 and EU GMP Annex 11
- Backup copies shall be verified for integrity and restorability on a quarterly basis
- Format migration (e.g., from one electronic format to another) shall be validated and documented

### 12.4 Record Access and Retrieval

- Sponsor may request copies of records related to their activities
- ArcaScience shall provide requested records within 10 business days (routine) or 3 business days (urgent/regulatory)
- Access shall be provided in a format agreed upon by both parties
- Confidentiality of records belonging to other ArcaScience clients shall be maintained at all times

---

## 13. Subcontractor Management

### 13.1 Subcontractor Qualification

ArcaScience shall qualify all subcontractors performing GxP-relevant activities per the following process:

| Step | Activity | Evidence |
|---|---|---|
| 1 | Risk assessment of subcontracted activity | Risk assessment document |
| 2 | Subcontractor capability evaluation (questionnaire and/or audit) | Completed qualification questionnaire or audit report |
| 3 | Quality agreement or quality addendum with subcontractor | Executed quality agreement |
| 4 | Approval by ArcaScience QA | Approval record in supplier qualification file |
| 5 | Ongoing monitoring per defined schedule | Performance review records |

### 13.2 Notification and Approval

| Event | Notification Requirement |
|---|---|
| Engagement of new subcontractor for GxP activities | Written notification to Sponsor at least 30 calendar days prior to engagement, with Sponsor right to object |
| Change of existing subcontractor | Written notification to Sponsor at least 30 calendar days prior, with rationale and qualification evidence |
| Subcontractor non-conformance affecting Sponsor data | Notification per deviation management timelines (Section 7.1) |
| Subcontractor audit findings (critical or major) | Notification within 10 business days of audit report issuance |

### 13.3 Current Subcontractor Overview

ArcaScience shall maintain and share with the Sponsor (upon request and subject to confidentiality) a list of qualified subcontractors performing GxP-relevant activities, including:

- [ ] Subcontractor name and location
- [ ] Scope of subcontracted activity
- [ ] Current qualification status and date of last assessment
- [ ] Applicable quality agreement reference
- [ ] Next scheduled re-evaluation date

### 13.4 Cloud Service Provider Management

Given the BRA platform's reliance on cloud infrastructure (S3, ElasticSearch, DocumentDB, QDrant), ArcaScience shall:

- Maintain qualification records for cloud service providers
- Ensure cloud infrastructure meets GxP data integrity requirements
- Monitor cloud service provider compliance certifications (SOC 2, ISO 27001)
- Maintain documented disaster recovery and business continuity plans
- Ensure data residency requirements are met per Sponsor specifications

---

## 14. Complaints Handling

### 14.1 Complaint Classification

| Classification | Definition | Response Timeline |
|---|---|---|
| **Critical** | Complaint relating to potential data integrity failure, incorrect GxP output that may affect patient safety or regulatory decision, or suspected regulatory non-compliance | Acknowledgment within 4 hours. Initial assessment within 24 hours. |
| **Major** | Complaint relating to output quality, system performance degradation, or non-critical compliance concern | Acknowledgment within 1 business day. Initial assessment within 5 business days. |
| **Minor** | Complaint relating to usability, documentation, or non-GxP system aspects | Acknowledgment within 3 business days. Initial assessment within 15 business days. |

### 14.2 Complaint Process

1. **Receipt and Logging**
   - Sponsor submits complaint via designated email or ticketing system
   - ArcaScience logs complaint with unique identifier, date, description, and classification

2. **Acknowledgment**
   - ArcaScience acknowledges receipt per timelines in Section 14.1
   - Assigned complaint owner and preliminary classification communicated to Sponsor

3. **Investigation**
   - Root cause investigation conducted
   - Impact assessment performed (including assessment of other potentially affected outputs)
   - Investigation linked to deviation process if GxP impact confirmed (Section 7)

4. **Resolution**
   - Corrective actions defined and implemented
   - Affected outputs re-generated if necessary
   - Sponsor informed of resolution and corrective actions taken

5. **Closure**
   - Sponsor confirms satisfaction with resolution (or escalates per Section 4.3)
   - Complaint record closed with full documentation

6. **Trending**
   - Complaint trends analyzed quarterly
   - Trends shared with Sponsor during quarterly quality review meetings

---

## 15. Regulatory Notification Obligations

### 15.1 Obligations of ArcaScience

ArcaScience shall promptly notify the Sponsor of:

| Event | Notification Timeline | Method |
|---|---|---|
| Receipt of regulatory authority inquiry or inspection relating to Sponsor activities | Within 48 hours | Email to Quality Agreement Owner |
| Receipt of regulatory warning letter, Form 483, or equivalent | Within 48 hours | Email + phone call to Quality Agreement Owner |
| Any regulatory action that may affect ArcaScience's ability to provide services | Within 48 hours | Email to Quality Agreement Owner |
| Changes in ArcaScience's regulatory status or certifications | Within 10 business days | Written notification |
| Changes in applicable regulations or guidance that may affect BRA platform compliance | Within 30 calendar days of ArcaScience becoming aware | Written notification with impact assessment |
| Discovery of any condition that may affect the integrity, reliability, or compliance of GxP outputs delivered to Sponsor | Within 24 hours | Phone + written confirmation |

### 15.2 Obligations of the Sponsor

The Sponsor shall promptly notify ArcaScience of:

| Event | Notification Timeline | Method |
|---|---|---|
| Regulatory authority inquiry specifically about BRA platform or ArcaScience services | Within 48 hours | Email to Quality Agreement Owner |
| Changes in Sponsor's regulatory requirements applicable to BRA platform outputs | Within 30 calendar days | Written notification |
| Changes in the intended use of BRA platform outputs that may affect classification or validation requirements | Within 15 business days | Written notification |

### 15.3 Joint Obligations

Both parties agree to:

- Cooperate fully in responding to regulatory inquiries and inspections
- Not communicate with regulatory authorities about the other party's activities without prior notification (except where legally compelled)
- Share relevant portions of regulatory correspondence that affect the other party
- Jointly develop responses to regulatory observations where both parties are involved

---

## 16. Termination and Transition

### 16.1 Termination Provisions

This Quality Agreement may be terminated:

| Scenario | Notice Period | Process |
|---|---|---|
| **Expiration of MSA** | Per MSA terms | Quality Agreement terminates concurrent with MSA, subject to transition obligations |
| **Termination by mutual agreement** | As mutually agreed | Written agreement signed by both Quality Agreement Owners |
| **Termination for cause (material breach)** | 30 calendar days written notice with opportunity to cure | Non-breaching party issues written notice specifying the breach. Breaching party has 30 days to cure. If not cured, termination effective. |
| **Termination for regulatory non-compliance** | Immediate, if required by regulatory authority | Written notice with supporting regulatory documentation |

### 16.2 Transition Plan

Upon termination or expiration, ArcaScience shall:

**Phase 1 - Notification and Planning (Days 1-15)**
- [ ] Acknowledge termination notice
- [ ] Appoint transition lead
- [ ] Develop detailed transition plan with milestones and responsibilities
- [ ] Identify all Sponsor data and records held by ArcaScience

**Phase 2 - Data and Record Transfer (Days 16-60)**
- [ ] Export all Sponsor data in agreed-upon format
- [ ] Provide complete audit trail exports with cryptographic hash chain verification
- [ ] Transfer all validation documentation relevant to Sponsor's use
- [ ] Provide copies of all quality records (deviations, CAPAs, change controls, complaints) related to Sponsor activities
- [ ] Transfer Knowledge Graph data and associated metadata
- [ ] Provide all output records (Disease Analysis, Clinical Landscape, Endpoint Studies, AE Reports, BRA, BRA Summary)

**Phase 3 - Verification and Closure (Days 61-90)**
- [ ] Sponsor verifies completeness and integrity of transferred data
- [ ] ArcaScience confirms secure deletion of Sponsor data from all systems (primary and backup) per agreed timeline
- [ ] Certificate of data destruction issued to Sponsor
- [ ] Final quality metrics report provided
- [ ] Transition closure meeting conducted
- [ ] Transition completion documented and signed by both parties

### 16.3 Surviving Obligations

The following obligations survive termination:

- Record retention per Section 12.2
- Confidentiality obligations per the MSA
- Regulatory inspection support for records within retention period
- Cooperation in regulatory investigations related to activities performed during the Agreement term

---

## 17. Signature Block

### 17.1 Agreement Execution

By signing below, the authorized representatives of each party confirm that they have read, understood, and agree to be bound by the terms of this Quality Agreement.

---

**FOR THE SPONSOR:**

| Field | Value |
|---|---|
| Company Name | ________________________________________ |
| Authorized Representative (Print Name) | ________________________________________ |
| Title | ________________________________________ |
| Signature | ________________________________________ |
| Date | ________________________________________ |

**Sponsor Quality Assurance Approval:**

| Field | Value |
|---|---|
| QA Representative (Print Name) | ________________________________________ |
| Title | ________________________________________ |
| Signature | ________________________________________ |
| Date | ________________________________________ |

---

**FOR ARCASCIENCE SAS:**

| Field | Value |
|---|---|
| Company Name | ArcaScience SAS |
| Authorized Representative (Print Name) | ________________________________________ |
| Title | ________________________________________ |
| Signature | ________________________________________ |
| Date | ________________________________________ |

**ArcaScience Quality Assurance Approval:**

| Field | Value |
|---|---|
| QA Representative (Print Name) | ________________________________________ |
| Title | ________________________________________ |
| Signature | ________________________________________ |
| Date | ________________________________________ |

---

### 17.2 Amendment History

| Version | Date | Description of Change | Approved By (Sponsor) | Approved By (ArcaScience) |
|---|---|---|---|---|
| 1.0 | 2026-03-25 | Initial release | [Pending] | [Pending] |
| | | | | |
| | | | | |

---

## 18. Appendices

### Appendix A - Quality Agreement Review Checklist

This checklist shall be used during the annual review of this Quality Agreement.

| Item | Review Question | Status | Comments |
|---|---|---|---|
| 1 | Are all contact details in Section 4.2 current? | [ ] Yes [ ] No | |
| 2 | Have there been any changes to the regulatory framework requiring updates? | [ ] Yes [ ] No | |
| 3 | Have there been any changes to ArcaScience's QMS that affect this Agreement? | [ ] Yes [ ] No | |
| 4 | Have there been any changes to the BRA platform scope (new output types, new models)? | [ ] Yes [ ] No | |
| 5 | Are all quality metrics and targets still appropriate? | [ ] Yes [ ] No | |
| 6 | Have there been any unresolved audit findings? | [ ] Yes [ ] No | |
| 7 | Have there been any critical or major deviations indicating Agreement gaps? | [ ] Yes [ ] No | |
| 8 | Have there been any subcontractor changes requiring updates? | [ ] Yes [ ] No | |
| 9 | Is the record retention schedule still aligned with current requirements? | [ ] Yes [ ] No | |
| 10 | Are training requirements still adequate? | [ ] Yes [ ] No | |
| 11 | Is the escalation path still current? | [ ] Yes [ ] No | |
| 12 | Are the notification timelines still achievable and appropriate? | [ ] Yes [ ] No | |

**Review Conducted By:**

| Party | Name | Date | Signature |
|---|---|---|---|
| Sponsor | | | |
| ArcaScience | | | |

### Appendix B - BRA Platform Architecture Overview (For Reference)

**Processing Pipeline:**

```
Document Ingestion
      |
      v
Classification (SLM-based)
      |
      v
Section Identification (SLM-based)
      |
      v
Entity Extraction (Clinician-trained SLMs)
      |
      v
Relation Extraction (SLM-based)
      |
      v
Normalization (MedDRA / SNOMED CT / ChEBI)
      |
      v
Knowledge Graph Assembly
      |
      v
Templated Output Generation
      |
      +---> Disease Analysis
      +---> Clinical Landscape + Efficacy Report
      +---> Clinical Endpoint Study
      +---> AE Reports
      +---> BRA Report
      +---> BRA Summary
```

**Infrastructure Components:**

| Component | Technology | GxP Role |
|---|---|---|
| Workflow Orchestration | Apache Airflow (DAGs) | Pipeline execution, scheduling, monitoring |
| Object Storage | Amazon S3 | Document storage, output storage, backup |
| Search and Analytics | ElasticSearch | Document indexing, search, retrieval |
| Document Database | DocumentDB | Structured data storage, metadata management |
| Vector Database | QDrant | Embedding storage for similarity search |
| API Layer | FastAPI (Python) + NestJS (TypeScript) | Service endpoints, authentication, authorization |
| Audit Trail | Custom (cryptographic hash chaining) | ALCOA+ compliance, 21 CFR Part 11 |

**Performance Benchmarks:**

| Metric | Value | Benchmark Basis |
|---|---|---|
| AE Extraction F1 | 92% | Gold-standard annotated corpus |
| NLP Pipeline F1 | 94% | Gold-standard annotated corpus |
| Signal Detection Improvement | 3x vs. manual | Comparative study against manual review |

### Appendix C - Responsible AI Alignment

Where the Sponsor operates under a Responsible AI framework (e.g., Sanofi's RAISE framework), ArcaScience aligns its BRA platform practices as follows:

| RAISE Pillar | ArcaScience Alignment |
|---|---|
| **Accountable** | Clear RACI matrix (Section 4.1). Defined escalation paths. Documented decision-making through audit trails. Named responsible parties for all quality activities. |
| **Fair and Ethical** | Clinician-trained SLMs to reduce bias. Validated extraction processes to ensure balanced representation of benefit and risk data. No autonomous clinical decision-making. |
| **Robust and Safe** | GAMP 5 Category 5 validation. Continuous performance monitoring (F1 scores). Regression testing. Deviation and CAPA management. Business continuity planning. |
| **Transparent and Explainable** | Full audit trails with cryptographic hash chaining. Traceability from output to source document. Knowledge Graph provides explainable entity-relationship pathways. Output templates reference source evidence. |
| **Eco-Responsible** | Task-specific SLMs (not large general-purpose models) designed for computational efficiency. Optimized pipeline to minimize redundant processing. Infrastructure right-sizing practices. |

---

**END OF DOCUMENT**

*Document ID: QA-ARCA-BRA-2026-001 | Version: 1.0 | Classification: Confidential - GxP Regulated*
