# Vendor Qualification and Due Diligence Assessment
# ArcaScience SAS - Benefit-Risk Assessment Platform

**Document ID:** VQA-ARCA-2026-001
**Version:** 1.0
**Effective Date:** 2026-03-25
**Review Date:** 2027-03-25
**Classification:** Confidential - Restricted Distribution
**Prepared For:** Sponsor Quality Assurance / Vendor Management Office
**Vendor Under Assessment:** ArcaScience SAS
**Assessment Type:** Initial Qualification (GxP-Critical Vendor)

---

## Document Control

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 0.1 | 2026-02-15 | ArcaScience Quality Assurance | Initial draft |
| 0.2 | 2026-03-01 | ArcaScience Quality Assurance | Internal review comments incorporated |
| 1.0 | 2026-03-25 | ArcaScience Quality Assurance | Issued for sponsor qualification review |

---

## Scoring Rubric

Throughout this document, assessment criteria are scored using the following rubric:

| Rating | Definition | Scoring |
|--------|-----------|---------|
| **Pass (P)** | Requirement fully met with objective evidence provided | 3 points |
| **Pass with Observation (PO)** | Requirement met; minor improvement opportunity identified | 2 points |
| **Fail (F)** | Requirement not met; corrective action required before qualification | 0 points |
| **N/A** | Requirement not applicable to this vendor type or scope | Not scored |

**Qualification Thresholds:**

| Overall Score | Decision |
|---------------|----------|
| >= 90% | Approved - Low Risk |
| 75% - 89% | Approved with Conditions - Medium Risk |
| 60% - 74% | Conditional Approval - High Risk (CAPA required within 90 days) |
| < 60% | Not Approved - Re-assessment required |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Vendor Classification](#2-vendor-classification)
3. [Company Overview and Organizational Structure](#3-company-overview-and-organizational-structure)
4. [Quality Management System Assessment](#4-quality-management-system-assessment)
5. [Personnel and Training Evaluation](#5-personnel-and-training-evaluation)
6. [Facility and Infrastructure Assessment](#6-facility-and-infrastructure-assessment)
7. [Information Security Assessment](#7-information-security-assessment)
8. [Data Integrity and Electronic Records Assessment](#8-data-integrity-and-electronic-records-assessment)
9. [Validation Capabilities Assessment](#9-validation-capabilities-assessment)
10. [Change Management Assessment](#10-change-management-assessment)
11. [CAPA and Deviation Management](#11-capa-and-deviation-management)
12. [Regulatory Compliance History](#12-regulatory-compliance-history)
13. [Business Continuity and Disaster Recovery](#13-business-continuity-and-disaster-recovery)
14. [Subcontractor Management](#14-subcontractor-management)
15. [Financial Stability Assessment](#15-financial-stability-assessment)
16. [Client References and Track Record](#16-client-references-and-track-record)
17. [RAISE Framework Alignment Assessment](#17-raise-framework-alignment-assessment)
18. [Qualification Decision and Risk Rating](#18-qualification-decision-and-risk-rating)
19. [Re-qualification Schedule](#19-re-qualification-schedule)
20. [Approval Signatures](#20-approval-signatures)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document provides a standardized, comprehensive Vendor Qualification and Due Diligence Assessment for ArcaScience SAS in its capacity as a GxP-critical technology vendor providing Benefit-Risk Assessment (BRA) platform services to pharmaceutical sponsors. The assessment is designed to satisfy the qualification requirements of major pharmaceutical companies evaluating ArcaScience as a vendor whose products and services directly impact regulated activities, including but not limited to:

- Benefit-risk analyses supporting regulatory submissions (eCTD Module 2.5)
- Adverse event extraction and signal detection contributing to pharmacovigilance obligations
- Periodic Benefit-Risk Evaluation Reports (PBRERs) and Development Safety Update Reports (DSURs)
- Regulatory intelligence supporting Health Authority interactions

This document is structured to align with ICH Q10 Pharmaceutical Quality System principles, GAMP 5 vendor assessment guidance, and the specific requirements of large pharmaceutical vendor management programs.

### 1.2 Scope

**In Scope:**

- ArcaScience BRA platform (SaaS and dedicated instance deployments)
- Data Forge ingestion and enrichment pipeline
- All 24 task-specific Small Language Models (SLMs) used in the BRA workflow
- Supporting infrastructure (cloud, database, vector search, orchestration)
- Personnel involved in platform development, validation, and support
- Quality management system governing platform lifecycle
- Information security controls protecting sponsor data

**Out of Scope:**

- Sponsor-side systems and infrastructure
- Third-party data sources accessed by the platform (e.g., PubMed, ClinicalTrials.gov) - assessed separately under subcontractor management
- Sponsor-specific custom configurations performed post-qualification

### 1.3 Applicable Regulations and Standards

| Regulation / Standard | Applicability |
|-----------------------|---------------|
| FDA 21 CFR Part 11 | Electronic records and electronic signatures |
| EU Annex 11 | Computerised systems |
| ICH Q10 | Pharmaceutical quality system |
| ICH E2E | Pharmacovigilance planning |
| GAMP 5 (2nd Edition) | Computerised system validation |
| ISO 27001:2022 | Information security management |
| ISO 9001:2015 | Quality management systems |
| CIOMS XII / BRAT Framework | Benefit-risk assessment methodology |
| EU AI Act (2024/1689) | AI system requirements (where applicable) |
| Sanofi RAISE Framework | Responsible AI governance (sponsor-specific) |

### 1.4 References

| Document | ID |
|----------|----|
| ArcaScience Quality Manual | QM-ARCA-2025-001 |
| ArcaScience Validation Master Plan | VMP-ARCA-2025-001 |
| ArcaScience Information Security Policy | ISP-ARCA-2025-001 |
| ArcaScience Business Continuity Plan | BCP-ARCA-2025-001 |
| ArcaScience SOP Index | SOP-IDX-ARCA-2025-001 |

---

## 2. Vendor Classification

### 2.1 Classification Determination

| Criterion | Assessment | Result |
|-----------|-----------|--------|
| Does the vendor provide a product or service that directly impacts product quality, patient safety, or data integrity? | BRA platform outputs feed directly into regulatory submissions (eCTD Module 2.5), PBRERs, and pharmacovigilance signal assessments. Adverse event extraction outputs may influence safety labeling decisions. | **Yes** |
| Does the vendor generate, process, store, or transmit GxP-regulated data? | The platform processes clinical trial data, adverse event reports, regulatory documents, and produces benefit-risk analysis outputs that become part of the regulatory record. | **Yes** |
| Could a failure of the vendor's product or service result in patient harm, regulatory non-compliance, or product recall? | Errors in AE extraction, signal detection, or benefit-risk quantification could lead to incorrect safety conclusions in regulatory submissions. | **Yes** |
| Does the vendor's product require validation under GAMP 5? | Category 5 - Custom (Bespoke) Application with AI/ML components. Requires full lifecycle validation including model performance qualification. | **Yes** |

### 2.2 Classification Result

| Field | Value |
|-------|-------|
| **Vendor Category** | GxP-Critical |
| **GAMP 5 Category** | Category 5 - Custom (Bespoke) Application |
| **Risk Level** | High |
| **Qualification Type** | Full Qualification (Questionnaire + Document Review + On-Site/Remote Audit) |
| **Re-qualification Frequency** | Annual |

### 2.3 Risk Assessment Matrix

| Risk Factor | Weight | Score (1-5) | Weighted Score |
|-------------|--------|-------------|----------------|
| Impact on patient safety | 5 | 4 | 20 |
| Impact on data integrity | 5 | 5 | 25 |
| Impact on regulatory compliance | 5 | 4 | 20 |
| Complexity of product/service | 4 | 5 | 20 |
| Availability of alternative vendors | 3 | 4 | 12 |
| Vendor maturity/track record | 3 | 3 | 9 |
| Geographic/regulatory risk | 2 | 2 | 4 |
| **Total** | | | **110 / 135** |

**Risk Classification:** High (score > 80) - Full qualification required.

---

## 3. Company Overview and Organizational Structure

### 3.1 Company Information

| Field | Response |
|-------|----------|
| Legal Name | ArcaScience SAS |
| Registered Address | France |
| Year Established | 2024 |
| Legal Structure | Societe par Actions Simplifiee (SAS) |
| Registration Number | [To be provided by ArcaScience] |
| Website | [To be provided by ArcaScience] |
| Primary Contact for Qualification | [Name, Title, Email, Phone] |
| Quality Contact | [Name, Title, Email, Phone] |

### 3.2 Organizational Structure

| Role / Function | Name / Count | Reporting Line |
|----------------|-------------|----------------|
| Chief Executive Officer / Founder | [Name] | Board of Directors |
| Chief Technology Officer | [Name] | CEO |
| Head of Quality Assurance | [Name] | CEO (independent of development) |
| Head of Data Science / AI | [Name] | CTO |
| Head of Regulatory Affairs | [Name] | CEO |
| Head of Information Security | [Name] | CTO |
| Full-Time Employees (Total) | 14 FTEs | Various |
| Collaborators / Contractors | 20 | Various |

### 3.3 Scientific Advisory Committee

| Name | Title / Affiliation | Role |
|------|---------------------|------|
| Philippe Peyre | Senior VP, Sanofi | Scientific Committee Member |
| [Additional members] | [Affiliations] | [Roles] |

### 3.4 Organizational Assessment

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 3.4.1 | Is the organizational structure documented and current? | P / PO / F / NA | |
| 3.4.2 | Is the Quality function independent from Development/Operations? | P / PO / F / NA | |
| 3.4.3 | Are roles and responsibilities clearly defined for GxP-impacting activities? | P / PO / F / NA | |
| 3.4.4 | Is there a designated person responsible for regulatory compliance? | P / PO / F / NA | |
| 3.4.5 | Is the organizational size adequate for the scope of contracted services? | P / PO / F / NA | 14 FTEs + 20 collaborators; assess capacity relative to committed deliverables |
| 3.4.6 | Is there a succession plan for key personnel? | P / PO / F / NA | |
| 3.4.7 | Does the scientific advisory committee include relevant domain expertise? | P / PO / F / NA | Includes senior pharma industry leadership |

---

## 4. Quality Management System Assessment

### 4.1 QMS Overview Questionnaire

| Ref | Question | Vendor Response | Evidence Provided |
|-----|----------|----------------|-------------------|
| 4.1.1 | Is there a documented Quality Management System (QMS)? | | |
| 4.1.2 | Is the QMS aligned with ISO 9001:2015 or equivalent? | | |
| 4.1.3 | Is there a Quality Manual that defines the QMS scope and policy? | | QM-ARCA-2025-001 |
| 4.1.4 | Are quality objectives defined, measurable, and reviewed periodically? | | |
| 4.1.5 | Is there a documented SOP index covering all GxP-relevant processes? | | SOP-IDX-ARCA-2025-001 |
| 4.1.6 | Are SOPs reviewed and approved at defined intervals? | | |
| 4.1.7 | Is there a management review process for the QMS? | | |
| 4.1.8 | Is there a process for handling quality complaints from clients? | | |
| 4.1.9 | Are internal audits conducted? If so, at what frequency? | | |
| 4.1.10 | Is there a document control system ensuring only current versions are in use? | | |

### 4.2 QMS Assessment Scoring

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 4.2.1 | Quality policy is documented, approved, and communicated | P / PO / F / NA | |
| 4.2.2 | SOP system covers all GxP-critical processes | P / PO / F / NA | |
| 4.2.3 | Document control ensures version management and controlled distribution | P / PO / F / NA | |
| 4.2.4 | Internal audit program exists with defined frequency and scope | P / PO / F / NA | |
| 4.2.5 | Management review process includes quality metrics and trend analysis | P / PO / F / NA | |
| 4.2.6 | Quality records are maintained, retrievable, and retention periods defined | P / PO / F / NA | |
| 4.2.7 | Continuous improvement process is documented and active | P / PO / F / NA | |
| 4.2.8 | Client complaint handling process is documented with defined timelines | P / PO / F / NA | |

**Section Score:** ___ / 24 (___%)

---

## 5. Personnel and Training Evaluation

### 5.1 Training Program Questionnaire

| Ref | Question | Vendor Response | Evidence Provided |
|-----|----------|----------------|-------------------|
| 5.1.1 | Is there a documented training program covering GxP requirements? | | |
| 5.1.2 | Are training records maintained for all personnel performing GxP-impacting activities? | | |
| 5.1.3 | Is there role-based training matrix that maps required competencies to each role? | | |
| 5.1.4 | Are personnel trained on data integrity principles (ALCOA+)? | | |
| 5.1.5 | Are personnel trained on FDA 21 CFR Part 11 and EU Annex 11 requirements? | | |
| 5.1.6 | Is there a process for assessing training effectiveness? | | |
| 5.1.7 | Are contractors/collaborators subject to the same training requirements as FTEs? | | 20 collaborators - confirm equivalent training |
| 5.1.8 | Is there GxP onboarding training for new personnel? | | |
| 5.1.9 | Are personnel trained on the specific therapeutic areas relevant to BRA outputs? | | 12 therapeutic areas currently supported |
| 5.1.10 | Is there ongoing training on pharmacovigilance and regulatory intelligence? | | |

### 5.2 Key Personnel Qualifications

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 5.2.1 | Key personnel have documented qualifications relevant to their roles | P / PO / F / NA | |
| 5.2.2 | Data scientists/ML engineers have demonstrated expertise in NLP and clinical data | P / PO / F / NA | Clinician-trained SLM development on 10M+ AE reports |
| 5.2.3 | Regulatory affairs personnel have experience with benefit-risk frameworks | P / PO / F / NA | BRAT/CIOMS XII, eCTD Module 2.5 |
| 5.2.4 | Quality personnel have formal GxP training and experience | P / PO / F / NA | |
| 5.2.5 | Training records are current, complete, and retrievable | P / PO / F / NA | |
| 5.2.6 | Competency assessments are performed and documented | P / PO / F / NA | |
| 5.2.7 | Contractor onboarding includes GxP-specific training requirements | P / PO / F / NA | |

### 5.3 Clinician Training of AI Models

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 5.3.1 | Clinical subject matter experts are involved in model training and validation | P / PO / F / NA | Clinician-trained on 10M+ AE reports, 500K+ trial records |
| 5.3.2 | Training data provenance is documented and traceable | P / PO / F / NA | 2M+ abstracts, 100K+ regulatory documents |
| 5.3.3 | Clinical review of model outputs is performed by qualified personnel | P / PO / F / NA | |
| 5.3.4 | Inter-annotator agreement metrics are tracked for training data quality | P / PO / F / NA | |

**Section Score:** ___ / 33 (___%)

---

## 6. Facility and Infrastructure Assessment

### 6.1 Infrastructure Architecture Overview

ArcaScience operates a cloud-native platform architecture. The following components constitute the production environment:

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Workflow Orchestration | Apache Airflow | DAG-based pipeline management for Data Forge ingestion and enrichment |
| Object Storage | Amazon S3 | Raw and enriched data storage with versioning and encryption |
| Search Engine | ElasticSearch | Full-text search and indexing of regulatory and clinical documents |
| Document Database | Amazon DocumentDB | Structured data storage for BRA records, metadata, and configurations |
| Vector Database | QDrant | Embedding storage and similarity search for SLM-powered retrieval |
| API Layer (Core) | FastAPI (Python) | Backend services, model inference endpoints, data processing APIs |
| API Layer (Platform) | NestJS (TypeScript) | BRA platform application layer, user-facing services |
| AI/ML Models | 24 task-specific SLMs | Clinician-trained small language models for BRA pipeline stages |

### 6.2 Infrastructure Assessment Criteria

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 6.2.1 | Cloud hosting provider is qualified (AWS, Azure, GCP) with relevant certifications (SOC 2, ISO 27001) | P / PO / F / NA | |
| 6.2.2 | Production environment is logically separated from development and testing | P / PO / F / NA | |
| 6.2.3 | Infrastructure as Code (IaC) is used for environment provisioning | P / PO / F / NA | |
| 6.2.4 | Network architecture includes appropriate segmentation and firewalling | P / PO / F / NA | |
| 6.2.5 | Data residency requirements can be met (EU, US, or other as required) | P / PO / F / NA | |
| 6.2.6 | Monitoring and alerting systems are in place for all critical components | P / PO / F / NA | |
| 6.2.7 | Logging infrastructure captures operational events with defined retention | P / PO / F / NA | |
| 6.2.8 | Capacity planning process exists and is reviewed periodically | P / PO / F / NA | |
| 6.2.9 | High availability configuration is documented (redundancy, failover) | P / PO / F / NA | |
| 6.2.10 | Performance benchmarks are defined and monitored for all platform components | P / PO / F / NA | |

### 6.3 Environment Management

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 6.3.1 | Separate environments exist for development, testing, staging, and production | P / PO / F / NA | |
| 6.3.2 | Production data is not used in non-production environments without anonymization | P / PO / F / NA | |
| 6.3.3 | Environment promotion process is documented and controlled | P / PO / F / NA | |
| 6.3.4 | Access to production environment is restricted and logged | P / PO / F / NA | |

**Section Score:** ___ / 42 (___%)

---

## 7. Information Security Assessment

### 7.1 ISO 27001 Alignment Status

| Field | Response |
|-------|----------|
| ISO 27001 Certification Status | Target certification - implementation in progress |
| Target Certification Date | [To be provided by ArcaScience] |
| Certification Body | [To be confirmed] |
| Current ISMS Maturity Level | [Self-assessment result] |

**Note:** ArcaScience is currently implementing an Information Security Management System (ISMS) aligned with ISO 27001:2022 requirements. While formal certification is in progress, the assessment below evaluates the current state of security controls against ISO 27001 Annex A requirements.

### 7.2 Information Security Policy and Governance

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 7.2.1 | Information security policy is documented, approved by management, and communicated | P / PO / F / NA | ISP-ARCA-2025-001 |
| 7.2.2 | Information security roles and responsibilities are defined | P / PO / F / NA | |
| 7.2.3 | Risk assessment methodology is documented and applied | P / PO / F / NA | |
| 7.2.4 | Risk treatment plan exists with defined controls and owners | P / PO / F / NA | |
| 7.2.5 | Security awareness training is provided to all personnel | P / PO / F / NA | |

### 7.3 Access Control

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 7.3.1 | Access control policy defines authorization and authentication requirements | P / PO / F / NA | |
| 7.3.2 | Role-based access control (RBAC) is implemented across all systems | P / PO / F / NA | |
| 7.3.3 | Multi-factor authentication (MFA) is enforced for all privileged access | P / PO / F / NA | |
| 7.3.4 | User access reviews are conducted at defined intervals | P / PO / F / NA | |
| 7.3.5 | Offboarding process includes timely access revocation | P / PO / F / NA | |
| 7.3.6 | Privileged access management (PAM) controls are in place | P / PO / F / NA | |
| 7.3.7 | Service account management follows least-privilege principle | P / PO / F / NA | |

### 7.4 Data Protection and Encryption

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 7.4.1 | Data classification scheme is defined and applied | P / PO / F / NA | |
| 7.4.2 | Encryption at rest is applied to all sensitive/GxP data (AES-256 or equivalent) | P / PO / F / NA | S3, DocumentDB, QDrant |
| 7.4.3 | Encryption in transit is enforced (TLS 1.2+ minimum) | P / PO / F / NA | |
| 7.4.4 | Key management procedures are documented | P / PO / F / NA | |
| 7.4.5 | Data retention and disposal procedures are documented | P / PO / F / NA | |
| 7.4.6 | Sponsor data segregation is enforced at the application and infrastructure level | P / PO / F / NA | Multi-tenant isolation |

### 7.5 Vulnerability and Incident Management

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 7.5.1 | Vulnerability scanning is performed regularly (frequency defined) | P / PO / F / NA | |
| 7.5.2 | Penetration testing is conducted at least annually by an independent party | P / PO / F / NA | |
| 7.5.3 | Patch management process is documented with defined SLAs by severity | P / PO / F / NA | |
| 7.5.4 | Security incident response plan is documented and tested | P / PO / F / NA | |
| 7.5.5 | Security incidents are reported to affected clients within defined timeframes | P / PO / F / NA | |
| 7.5.6 | Security event monitoring (SIEM or equivalent) is operational | P / PO / F / NA | |

### 7.6 Physical and Network Security

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 7.6.1 | Cloud provider physical security certifications are current (SOC 2 Type II, ISO 27001) | P / PO / F / NA | |
| 7.6.2 | Network segmentation isolates production from non-production | P / PO / F / NA | |
| 7.6.3 | Web application firewall (WAF) is deployed | P / PO / F / NA | |
| 7.6.4 | DDoS protection is implemented | P / PO / F / NA | |
| 7.6.5 | Endpoint security is deployed on all developer workstations | P / PO / F / NA | |

**Section Score:** ___ / 72 (___%)

---

## 8. Data Integrity and Electronic Records Assessment

### 8.1 FDA 21 CFR Part 11 Compliance

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 8.1.1 | System generates records that meet the definition of electronic records under Part 11 | P / PO / F / NA | BRA outputs, audit trails, extraction records |
| 8.1.2 | Electronic signatures are implemented where required (unique to individual, not reused) | P / PO / F / NA | |
| 8.1.3 | Electronic signatures are linked to their respective electronic records | P / PO / F / NA | |
| 8.1.4 | Signature manifestations include printed name, date/time, and meaning of signature | P / PO / F / NA | |
| 8.1.5 | System enforces authority checks - users can only sign within their authorized scope | P / PO / F / NA | |
| 8.1.6 | Audit trail captures creation, modification, and deletion of electronic records | P / PO / F / NA | |
| 8.1.7 | Audit trail entries are computer-generated and cannot be modified by users | P / PO / F / NA | Cryptographic hash chaining |
| 8.1.8 | System includes controls to ensure record completeness and accuracy | P / PO / F / NA | |

### 8.2 ALCOA+ Compliance Assessment

ArcaScience asserts ALCOA+ compliance with cryptographic hash chaining for audit trail integrity. The following assessment evaluates each ALCOA+ principle:

| Ref | ALCOA+ Principle | Criterion | Rating | Evidence / Notes |
|-----|-----------------|-----------|--------|-----------------|
| 8.2.1 | **Attributable** | Every data entry, modification, and output is linked to the person or system that generated it | P / PO / F / NA | User authentication, API-level attribution |
| 8.2.2 | **Legible** | All records are readable, permanent, and reproducible throughout the retention period | P / PO / F / NA | |
| 8.2.3 | **Contemporaneous** | Data is recorded at the time the activity is performed (timestamps are system-generated) | P / PO / F / NA | NTP-synchronized timestamps |
| 8.2.4 | **Original** | The first recording of the data is preserved or a verified copy exists | P / PO / F / NA | |
| 8.2.5 | **Accurate** | Data is correct, truthful, and free from errors; any corrections preserve the original | P / PO / F / NA | |
| 8.2.6 | **Complete** | All data is present, including repeat or reanalysis results | P / PO / F / NA | |
| 8.2.7 | **Consistent** | Data elements are logically consistent across related records (timestamps, sequences) | P / PO / F / NA | |
| 8.2.8 | **Enduring** | Records are maintained throughout the required retention period on durable media | P / PO / F / NA | |
| 8.2.9 | **Available** | Records are accessible and retrievable throughout the retention period for review or inspection | P / PO / F / NA | |

### 8.3 Cryptographic Hash Chaining Assessment

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 8.3.1 | Hash algorithm used is cryptographically secure (SHA-256 or stronger) | P / PO / F / NA | |
| 8.3.2 | Each audit trail entry includes the hash of the previous entry (chain integrity) | P / PO / F / NA | |
| 8.3.3 | Chain integrity verification can be performed on demand | P / PO / F / NA | |
| 8.3.4 | Tampering with any entry in the chain is detectable | P / PO / F / NA | |
| 8.3.5 | Hash chain verification is included in periodic data integrity checks | P / PO / F / NA | |

### 8.4 AI/ML-Specific Data Integrity

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 8.4.1 | Training data provenance is documented and traceable | P / PO / F / NA | 10M+ AE reports, 500K+ trial records, 2M+ abstracts, 100K+ regulatory docs |
| 8.4.2 | Model versioning ensures reproducibility of outputs | P / PO / F / NA | |
| 8.4.3 | Model inference results include confidence scores and source attribution | P / PO / F / NA | |
| 8.4.4 | Intermediate outputs from each pipeline stage are preserved and auditable | P / PO / F / NA | 24-stage SLM pipeline |
| 8.4.5 | Model drift monitoring is implemented with defined alert thresholds | P / PO / F / NA | |
| 8.4.6 | No "black box" outputs - all conclusions are traceable to source evidence | P / PO / F / NA | |

**Section Score:** ___ / 69 (___%)

---

## 9. Validation Capabilities Assessment

### 9.1 GAMP 5 Category 5 Validation

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 9.1.1 | A Validation Master Plan (VMP) exists and is current | P / PO / F / NA | VMP-ARCA-2025-001 |
| 9.1.2 | The system is classified as GAMP 5 Category 5 (Custom/Bespoke) with documented rationale | P / PO / F / NA | |
| 9.1.3 | User Requirements Specification (URS) is documented and approved | P / PO / F / NA | |
| 9.1.4 | Functional Specification (FS) is documented and traceable to URS | P / PO / F / NA | |
| 9.1.5 | Design Specification (DS) is documented and traceable to FS | P / PO / F / NA | |
| 9.1.6 | Requirements traceability matrix (RTM) links URS through to test execution | P / PO / F / NA | |
| 9.1.7 | Installation Qualification (IQ) protocols and reports are available | P / PO / F / NA | |
| 9.1.8 | Operational Qualification (OQ) protocols and reports are available | P / PO / F / NA | |
| 9.1.9 | Performance Qualification (PQ) protocols and reports are available | P / PO / F / NA | |
| 9.1.10 | Validation Summary Report is documented with all deviations resolved or justified | P / PO / F / NA | |

### 9.2 AI/ML Model Validation

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 9.2.1 | Model validation protocol defines acceptance criteria prior to testing | P / PO / F / NA | |
| 9.2.2 | Predefined performance thresholds are documented for each model | P / PO / F / NA | AE extraction F1: 92%, NLP F1: 94% |
| 9.2.3 | Test datasets are independent from training datasets | P / PO / F / NA | |
| 9.2.4 | Model performance is validated across relevant therapeutic areas | P / PO / F / NA | 12 therapeutic areas |
| 9.2.5 | Edge case and boundary testing is included in validation protocols | P / PO / F / NA | |
| 9.2.6 | Ongoing performance monitoring is defined with revalidation triggers | P / PO / F / NA | |
| 9.2.7 | Model retraining triggers and revalidation requirements are documented | P / PO / F / NA | |
| 9.2.8 | Each of the 24 SLMs has individual validation documentation | P / PO / F / NA | |
| 9.2.9 | End-to-end pipeline validation covers the full BRA workflow (not just individual models) | P / PO / F / NA | |
| 9.2.10 | Validation includes assessment of model behavior on out-of-distribution inputs | P / PO / F / NA | |

### 9.3 Performance Benchmarks

| Metric | Target | Validated Result | Evidence |
|--------|--------|-----------------|----------|
| Adverse Event Extraction F1 Score | >= 90% | 92% | [Validation Report Ref] |
| NLP Pipeline F1 Score | >= 90% | 94% | [Validation Report Ref] |
| BRA Report Generation Accuracy | [Defined per use case] | [Result] | [Validation Report Ref] |
| Source Attribution Accuracy | [Defined per use case] | [Result] | [Validation Report Ref] |
| Processing Throughput (documents/hour) | [Defined per SLA] | [Result] | [Validation Report Ref] |

**Section Score:** ___ / 60 (___%)

---

## 10. Change Management Assessment

### 10.1 Change Control Process

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 10.1.1 | A documented change control SOP exists | P / PO / F / NA | |
| 10.1.2 | All changes to the validated system are managed through the change control process | P / PO / F / NA | |
| 10.1.3 | Changes are classified by risk level (critical, major, minor) | P / PO / F / NA | |
| 10.1.4 | Impact assessment is performed and documented for each change | P / PO / F / NA | |
| 10.1.5 | Changes require appropriate approval before implementation | P / PO / F / NA | |
| 10.1.6 | Regression testing is performed commensurate with change risk | P / PO / F / NA | |
| 10.1.7 | Change history is maintained and auditable | P / PO / F / NA | |
| 10.1.8 | Emergency change procedure exists with retrospective documentation requirements | P / PO / F / NA | |
| 10.1.9 | Clients are notified of changes that may impact their use of the system | P / PO / F / NA | |
| 10.1.10 | Release notes are provided to clients for each system update | P / PO / F / NA | |

### 10.2 AI/ML-Specific Change Management

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 10.2.1 | Model updates (retraining, fine-tuning) are managed under change control | P / PO / F / NA | |
| 10.2.2 | Training data changes are managed under change control | P / PO / F / NA | |
| 10.2.3 | Model version rollback capability exists | P / PO / F / NA | |
| 10.2.4 | Impact of model changes on downstream outputs is assessed | P / PO / F / NA | 24 SLMs in pipeline - cascade impact analysis |
| 10.2.5 | Shadow deployment / A-B testing is used for model updates where appropriate | P / PO / F / NA | |

**Section Score:** ___ / 45 (___%)

---

## 11. CAPA and Deviation Management

### 11.1 CAPA Process Assessment

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 11.1.1 | A documented CAPA SOP exists | P / PO / F / NA | |
| 11.1.2 | Root cause analysis methodology is defined (e.g., 5-Why, Ishikawa, FMEA) | P / PO / F / NA | |
| 11.1.3 | CAPA records include description, root cause, corrective action, preventive action, and effectiveness check | P / PO / F / NA | |
| 11.1.4 | CAPAs are tracked to closure with defined timelines | P / PO / F / NA | |
| 11.1.5 | Effectiveness of CAPAs is verified and documented | P / PO / F / NA | |
| 11.1.6 | CAPA trends are reviewed during management reviews | P / PO / F / NA | |

### 11.2 Deviation Management

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 11.2.1 | A documented deviation/non-conformance handling SOP exists | P / PO / F / NA | |
| 11.2.2 | Deviations are classified by severity (critical, major, minor) | P / PO / F / NA | |
| 11.2.3 | Impact assessment on GxP data/outputs is performed for each deviation | P / PO / F / NA | |
| 11.2.4 | Deviations impacting client data or outputs are communicated to affected clients | P / PO / F / NA | |
| 11.2.5 | Recurring deviations trigger CAPA initiation | P / PO / F / NA | |

### 11.3 AI/ML-Specific Deviations

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 11.3.1 | Model performance degradation below validated thresholds is treated as a deviation | P / PO / F / NA | F1 scores below 90% threshold |
| 11.3.2 | Unexpected model outputs (hallucinations, unsupported conclusions) are investigated as deviations | P / PO / F / NA | |
| 11.3.3 | Data quality issues in input data are documented and assessed for impact on outputs | P / PO / F / NA | |

**Section Score:** ___ / 42 (___%)

---

## 12. Regulatory Compliance History

### 12.1 Regulatory Track Record

| Ref | Question | Vendor Response |
|-----|----------|----------------|
| 12.1.1 | Has the company been subject to any regulatory inspection (FDA, EMA, MHRA, other)? If yes, provide details and outcomes. | |
| 12.1.2 | Has the company received any warning letters, Form 483 observations, or equivalent regulatory findings? | |
| 12.1.3 | Has the company been subject to any consent decree, debarment, or exclusion action? | |
| 12.1.4 | Has any client audit resulted in critical findings in the past 3 years? If yes, describe findings and remediation. | |
| 12.1.5 | Has the company been involved in any data integrity-related regulatory action? | |

### 12.2 Submission Support History

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 12.2.1 | Platform outputs have been included in regulatory submissions without regulatory deficiency | P / PO / F / NA | 50+ regulatory submissions supported |
| 12.2.2 | Platform supports required regulatory formats (eCTD Module 2.5, PBRER, DSUR) | P / PO / F / NA | |
| 12.2.3 | Regulatory submission support spans multiple Health Authorities (FDA, EMA, PMDA, etc.) | P / PO / F / NA | |
| 12.2.4 | No regulatory rejections or deficiency letters attributable to platform output quality | P / PO / F / NA | |

### 12.3 Framework Alignment

| Framework | Alignment Status | Evidence |
|-----------|-----------------|----------|
| BRAT (Benefit-Risk Action Team) Framework | Aligned | [Documentation reference] |
| CIOMS XII (Benefit-Risk Balance for Marketed Products) | Aligned | [Documentation reference] |
| eCTD Module 2.5 (Clinical Overview - B/R Section) | Aligned | [Documentation reference] |
| PBRER (ICH E2C(R2)) | Aligned | [Documentation reference] |
| FDA Benefit-Risk Framework (PDUFA VI) | Aligned | [Documentation reference] |

**Section Score:** ___ / 12 (___%)

---

## 13. Business Continuity and Disaster Recovery

### 13.1 Business Continuity Planning

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 13.1.1 | A documented Business Continuity Plan (BCP) exists | P / PO / F / NA | BCP-ARCA-2025-001 |
| 13.1.2 | Business Impact Analysis (BIA) has been performed identifying critical processes | P / PO / F / NA | |
| 13.1.3 | Recovery Time Objective (RTO) is defined for platform services | P / PO / F / NA | |
| 13.1.4 | Recovery Point Objective (RPO) is defined for all GxP data stores | P / PO / F / NA | |
| 13.1.5 | BCP has been tested within the past 12 months | P / PO / F / NA | |
| 13.1.6 | Communication plan exists for notifying clients during business disruptions | P / PO / F / NA | |
| 13.1.7 | Key person dependency risk is mitigated (cross-training, documentation) | P / PO / F / NA | 14 FTEs - assess single points of failure |

### 13.2 Disaster Recovery

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 13.2.1 | Disaster Recovery Plan (DRP) is documented and approved | P / PO / F / NA | |
| 13.2.2 | Automated backups are performed for all critical data stores | P / PO / F / NA | S3, DocumentDB, ElasticSearch, QDrant |
| 13.2.3 | Backup integrity is verified through periodic restore testing | P / PO / F / NA | |
| 13.2.4 | Backups are stored in a geographically separate location | P / PO / F / NA | |
| 13.2.5 | DR failover has been tested within the past 12 months | P / PO / F / NA | |
| 13.2.6 | DR procedures include validation of restored system state | P / PO / F / NA | |

### 13.3 Service Level Commitments

| Metric | Commitment | Evidence |
|--------|-----------|----------|
| Platform Availability (uptime) | [___]% | |
| Planned Maintenance Window | [Defined schedule] | |
| Incident Response Time (Critical) | [___] hours | |
| Incident Response Time (Major) | [___] hours | |
| Incident Resolution Time (Critical) | [___] hours | |
| Data Backup Frequency | [___] | |
| RTO | [___] hours | |
| RPO | [___] hours | |

**Section Score:** ___ / 39 (___%)

---

## 14. Subcontractor Management

### 14.1 Subcontractor Overview

| Subcontractor / Service | Type | GxP Impact | Qualification Status |
|------------------------|------|-----------|---------------------|
| AWS (Cloud Infrastructure) | IaaS | High - hosts all GxP data and computation | [Qualified / In Progress] |
| [Data source providers] | Data Services | Medium - source data quality | [Qualified / In Progress] |
| [Collaborators - 20 individuals] | Professional Services | Variable - depends on role | [Qualified / In Progress] |

### 14.2 Subcontractor Management Assessment

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 14.2.1 | A documented subcontractor/supplier management SOP exists | P / PO / F / NA | |
| 14.2.2 | GxP-critical subcontractors are identified and risk-assessed | P / PO / F / NA | |
| 14.2.3 | Quality agreements or technical agreements exist with GxP-critical subcontractors | P / PO / F / NA | |
| 14.2.4 | Subcontractor qualifications are reviewed periodically | P / PO / F / NA | |
| 14.2.5 | Cloud provider (AWS) qualification includes review of SOC 2 Type II report | P / PO / F / NA | |
| 14.2.6 | Subcontractor changes that may impact the sponsor are communicated | P / PO / F / NA | |
| 14.2.7 | Right to audit clause exists in agreements with GxP-critical subcontractors | P / PO / F / NA | |
| 14.2.8 | The 20 collaborators are subject to equivalent confidentiality and quality obligations | P / PO / F / NA | |

**Section Score:** ___ / 24 (___%)

---

## 15. Financial Stability Assessment

### 15.1 Financial Information

| Ref | Question | Vendor Response |
|-----|----------|----------------|
| 15.1.1 | What is the company's annual revenue for the past 2 fiscal years? | |
| 15.1.2 | What is the company's current funding status (bootstrapped, seed, Series A, etc.)? | |
| 15.1.3 | What is the current cash runway (months)? | |
| 15.1.4 | Are there any pending or threatened legal proceedings that could materially affect operations? | |
| 15.1.5 | Does the company carry professional liability / errors and omissions insurance? | |
| 15.1.6 | Does the company carry cyber liability insurance? | |
| 15.1.7 | What percentage of total revenue is derived from the top 3 clients? | |

### 15.2 Financial Stability Assessment

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 15.2.1 | Financial statements or audited accounts are available for review | P / PO / F / NA | |
| 15.2.2 | The company demonstrates sufficient financial resources to fulfill contractual obligations | P / PO / F / NA | |
| 15.2.3 | Revenue diversification reduces dependency risk on any single client | P / PO / F / NA | |
| 15.2.4 | Insurance coverage is adequate for the scope of services | P / PO / F / NA | |
| 15.2.5 | No material legal proceedings that could impact service delivery | P / PO / F / NA | |
| 15.2.6 | Business model supports long-term viability | P / PO / F / NA | |

### 15.3 Escrow and Continuity Provisions

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 15.3.1 | Source code escrow arrangement is available or can be established | P / PO / F / NA | |
| 15.3.2 | Data portability provisions exist in the event of contract termination | P / PO / F / NA | |
| 15.3.3 | Transition assistance provisions are defined in the service agreement | P / PO / F / NA | |

**Section Score:** ___ / 27 (___%)

---

## 16. Client References and Track Record

### 16.1 Client Reference Summary

| Client | Therapeutic Area | Engagement Type | Key Outcome | Reference Available |
|--------|-----------------|----------------|-------------|-------------------|
| AstraZeneca | [Multiple] | BRA Platform Deployment | 68% BRA cycle time reduction | Yes / No |
| Novartis | [Multiple] | BRA Platform Deployment | $12M cost savings | Yes / No |
| ICON (CRO) | [Multiple] | QC Automation | 90% QC task reduction | Yes / No |
| Sanofi | Dermatology (Hidradenitis Suppurativa) | BRA Pilot | 18 months of work in 2 weeks; 5 undocumented risks identified; $100K vs. CRO estimate $1.2M | Yes / No |

### 16.2 Track Record Metrics

| Metric | Value | Evidence |
|--------|-------|----------|
| Total regulatory submissions supported | 50+ | [Submission log reference] |
| Therapeutic areas covered | 12 | [List available on request] |
| Average BRA cycle time reduction | [___]% | [Client outcome data] |
| Regulatory deficiency letters attributable to platform | 0 (to be confirmed) | [Quality records] |

### 16.3 Sanofi Prior Engagement - HS BRA Pilot Assessment

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 16.3.1 | Prior engagement delivered within agreed timeline and scope | P / PO / F / NA | 18 months of manual work completed in 2 weeks |
| 16.3.2 | Deliverables met quality acceptance criteria | P / PO / F / NA | |
| 16.3.3 | Platform identified risks not found by prior methods | P / PO / F / NA | 5 undocumented risks identified |
| 16.3.4 | Cost-effectiveness was demonstrated | P / PO / F / NA | $100K vs. CRO estimate of $1.2M (92% cost reduction) |
| 16.3.5 | Stakeholder feedback was positive | P / PO / F / NA | |
| 16.3.6 | Data handling met Sanofi's security and confidentiality requirements | P / PO / F / NA | |

### 16.4 Reference Assessment

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 16.4.1 | At least 3 client references are available from comparable organizations | P / PO / F / NA | AstraZeneca, Novartis, ICON |
| 16.4.2 | References confirm quality of deliverables | P / PO / F / NA | |
| 16.4.3 | References confirm responsiveness and communication | P / PO / F / NA | |
| 16.4.4 | References confirm adherence to timelines and budgets | P / PO / F / NA | |
| 16.4.5 | No negative references or unresolved disputes | P / PO / F / NA | |

**Section Score:** ___ / 33 (___%)

---

## 17. RAISE Framework Alignment Assessment

This section is specific to Sanofi's Responsible AI at Sanofi for Everyone (RAISE) framework and evaluates ArcaScience's alignment with its five pillars. This section is mandatory for Sanofi vendor qualification and optional for other sponsors.

### 17.1 Pillar 1 - Accountable to Outcomes

*AI systems must produce outcomes that are traceable, reliable, and subject to human oversight.*

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 17.1.1 | Every BRA output is traceable to specific source documents and data points | P / PO / F / NA | ALCOA+ audit trail with cryptographic hash chaining |
| 17.1.2 | The system does not generate hallucinated content - all conclusions are evidence-backed | P / PO / F / NA | 24 task-specific SLMs vs. generalist LLMs; source attribution enforced |
| 17.1.3 | Human-in-the-loop review is integrated at defined quality gates | P / PO / F / NA | |
| 17.1.4 | Accountability for AI-generated outputs is clearly assigned (human owner identified) | P / PO / F / NA | |
| 17.1.5 | Performance metrics are continuously monitored with defined escalation thresholds | P / PO / F / NA | AE extraction F1: 92%, NLP F1: 94% |
| 17.1.6 | Outcome accountability extends to downstream regulatory decisions informed by platform outputs | P / PO / F / NA | 50+ submissions supported |

### 17.2 Pillar 2 - Fair and Ethical

*AI systems must avoid bias and ensure equitable outcomes across populations.*

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 17.2.1 | Training data is assessed for demographic and geographic bias | P / PO / F / NA | |
| 17.2.2 | Subpopulation analyses do not exhibit systematic bias in AE extraction or risk quantification | P / PO / F / NA | |
| 17.2.3 | Model performance is validated across diverse patient populations | P / PO / F / NA | 12 therapeutic areas |
| 17.2.4 | Ethical review process exists for new use cases or therapeutic areas | P / PO / F / NA | |
| 17.2.5 | No use of patient-level data without appropriate consent and de-identification | P / PO / F / NA | |
| 17.2.6 | Fair access principles are considered in platform pricing and availability | P / PO / F / NA | |

### 17.3 Pillar 3 - Robust and Safe

*AI systems must be technically sound, validated, and resilient.*

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 17.3.1 | GAMP 5 Category 5 validation is complete and current | P / PO / F / NA | |
| 17.3.2 | Model performance thresholds are enforced - outputs below threshold are flagged or blocked | P / PO / F / NA | F1 thresholds enforced per SLM |
| 17.3.3 | System handles edge cases gracefully (incomplete data, novel terminology, unexpected inputs) | P / PO / F / NA | |
| 17.3.4 | Adversarial robustness testing has been performed | P / PO / F / NA | |
| 17.3.5 | Failsafe mechanisms prevent propagation of errors through the 24-stage pipeline | P / PO / F / NA | |
| 17.3.6 | System degradation is detected and communicated before impacting output quality | P / PO / F / NA | |
| 17.3.7 | Security controls protect against data poisoning and model manipulation | P / PO / F / NA | |

### 17.4 Pillar 4 - Transparent and Explainable

*AI decision-making must be understandable and inspectable by stakeholders.*

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 17.4.1 | Full ALCOA+ audit trail is available for every BRA output | P / PO / F / NA | Cryptographic hash chaining |
| 17.4.2 | Per-step intermediate outputs are inspectable across all 24 SLM pipeline stages | P / PO / F / NA | |
| 17.4.3 | Confidence scores are provided for all model-generated outputs | P / PO / F / NA | |
| 17.4.4 | Source attribution links every conclusion to specific evidence (documents, sections, data points) | P / PO / F / NA | |
| 17.4.5 | Model methodology documentation is available for regulatory and scientific review | P / PO / F / NA | |
| 17.4.6 | Non-technical stakeholders can understand how conclusions were reached | P / PO / F / NA | |
| 17.4.7 | Limitations and uncertainty are explicitly communicated in outputs | P / PO / F / NA | |

### 17.5 Pillar 5 - Eco-Responsible

*AI systems should minimize environmental impact and computational waste.*

| Ref | Criterion | Rating | Evidence / Notes |
|-----|-----------|--------|-----------------|
| 17.5.1 | Architecture uses task-specific SLMs rather than monolithic large language models | P / PO / F / NA | 24 SLMs vs. single LLM - lower compute footprint |
| 17.5.2 | Computational resource usage is monitored and optimized | P / PO / F / NA | |
| 17.5.3 | Carbon footprint of model training and inference is measured or estimated | P / PO / F / NA | |
| 17.5.4 | Cloud infrastructure uses renewable energy or carbon-neutral data centers where available | P / PO / F / NA | AWS sustainability commitments |
| 17.5.5 | Model efficiency is considered in architecture decisions (SLM vs. LLM trade-off documented) | P / PO / F / NA | |
| 17.5.6 | Unnecessary reprocessing is avoided through caching and incremental processing | P / PO / F / NA | |

### 17.6 RAISE Alignment Summary

| Pillar | Max Score | Score | Percentage | Rating |
|--------|-----------|-------|-----------|--------|
| Accountable to Outcomes | 18 | ___ | ___% | P / PO / F |
| Fair and Ethical | 18 | ___ | ___% | P / PO / F |
| Robust and Safe | 21 | ___ | ___% | P / PO / F |
| Transparent and Explainable | 21 | ___ | ___% | P / PO / F |
| Eco-Responsible | 18 | ___ | ___% | P / PO / F |
| **RAISE Total** | **96** | **___** | **___%** | |

**RAISE Qualification Threshold:** Minimum 75% per pillar and 80% overall for Sanofi qualification.

**Section Score:** ___ / 96 (___%)

---

## 18. Qualification Decision and Risk Rating

### 18.1 Section Score Summary

| Section | Max Score | Score | Percentage |
|---------|-----------|-------|-----------|
| 3. Company Overview and Organizational Structure | 21 | ___ | ___% |
| 4. Quality Management System | 24 | ___ | ___% |
| 5. Personnel and Training | 33 | ___ | ___% |
| 6. Facility and Infrastructure | 42 | ___ | ___% |
| 7. Information Security | 72 | ___ | ___% |
| 8. Data Integrity and Electronic Records | 69 | ___ | ___% |
| 9. Validation Capabilities | 60 | ___ | ___% |
| 10. Change Management | 45 | ___ | ___% |
| 11. CAPA and Deviation Management | 42 | ___ | ___% |
| 12. Regulatory Compliance History | 12 | ___ | ___% |
| 13. Business Continuity and Disaster Recovery | 39 | ___ | ___% |
| 14. Subcontractor Management | 24 | ___ | ___% |
| 15. Financial Stability | 27 | ___ | ___% |
| 16. Client References and Track Record | 33 | ___ | ___% |
| 17. RAISE Framework Alignment (Sanofi-specific) | 96 | ___ | ___% |
| **Overall Total** | **639** | **___** | **___%** |

### 18.2 Critical Findings Summary

| Finding # | Section | Description | Severity | CAPA Required |
|-----------|---------|-------------|----------|---------------|
| | | | Critical / Major / Minor | Yes / No |
| | | | Critical / Major / Minor | Yes / No |
| | | | Critical / Major / Minor | Yes / No |

### 18.3 Observations and Recommendations

| Observation # | Section | Description | Priority |
|---------------|---------|-------------|----------|
| | | | High / Medium / Low |
| | | | High / Medium / Low |
| | | | High / Medium / Low |

### 18.4 Risk Mitigation Measures

For any identified risks, the following mitigation measures are recommended or required:

| Risk | Mitigation Measure | Owner | Target Date | Status |
|------|-------------------|-------|-------------|--------|
| ISO 27001 certification in progress (not yet achieved) | Monitor certification progress; interim controls assessment; annual reassessment until certified | Sponsor QA | [Date] | Open |
| Small organization (14 FTEs) - key person dependency | Review succession planning, cross-training matrix, and knowledge management practices | Sponsor QA | [Date] | Open |
| Startup financial profile - long-term viability | Review financial statements annually; establish source code escrow; define exit/transition plan | Sponsor QA | [Date] | Open |

### 18.5 Qualification Decision

| Field | Value |
|-------|-------|
| **Overall Score** | ___% |
| **Risk Rating** | Low / Medium / High |
| **Qualification Decision** | Approved / Approved with Conditions / Conditional Approval / Not Approved |
| **Conditions (if applicable)** | [List any conditions that must be met] |
| **CAPA Due Date (if applicable)** | [Date] |
| **Effective Date** | [Date] |
| **Expiration Date** | [Date - typically 12 months] |

### 18.6 Decision Criteria Applied

| Criterion | Met? |
|-----------|------|
| No critical findings remain open | Yes / No |
| Overall score meets threshold (>= 60%) | Yes / No |
| No section scored below 50% | Yes / No |
| RAISE framework minimum thresholds met (Sanofi only) | Yes / No / NA |
| Financial stability assessment does not indicate unacceptable risk | Yes / No |
| Adequate references from comparable organizations | Yes / No |

---

## 19. Re-qualification Schedule

### 19.1 Re-qualification Frequency

| Vendor Risk Level | Re-qualification Frequency | Trigger-Based Re-qualification |
|------------------|--------------------------|-------------------------------|
| High (current classification) | Annual | Any of the triggers below |
| Medium | Every 2 years | Any of the triggers below |
| Low | Every 3 years | Any of the triggers below |

### 19.2 Trigger-Based Re-qualification Events

The following events shall trigger an unscheduled re-qualification assessment regardless of the scheduled re-qualification date:

| Trigger | Scope of Re-assessment |
|---------|----------------------|
| Material change in vendor ownership or management | Full re-qualification |
| Significant quality event impacting sponsor data or outputs | Targeted assessment (affected sections) |
| Regulatory inspection finding (warning letter, 483, etc.) | Targeted assessment + regulatory compliance section |
| Material change in the platform architecture or technology stack | Validation and infrastructure sections |
| Security breach affecting sponsor data | Information security section + full incident review |
| Failure to maintain agreed service levels for 3+ consecutive months | Service delivery and BCP sections |
| Change in vendor financial status (e.g., funding round, acquisition, financial distress) | Financial stability section |
| ISO 27001 certification achieved or lapsed | Information security section |
| Major version release of the BRA platform | Validation, change management, and performance sections |
| Addition of new AI/ML models to the pipeline | AI/ML validation and RAISE alignment sections |

### 19.3 Re-qualification Schedule

| Assessment Cycle | Type | Planned Date | Assessor | Status |
|-----------------|------|-------------|----------|--------|
| Initial Qualification | Full | 2026-03-25 | [Assessor Name] | In Progress |
| Annual Re-qualification | Full | 2027-03-25 | [TBD] | Scheduled |
| Annual Re-qualification | Full | 2028-03-25 | [TBD] | Planned |

### 19.4 Ongoing Monitoring Between Re-qualifications

| Monitoring Activity | Frequency | Responsible Party |
|--------------------|-----------|-------------------|
| Review of vendor-provided quality metrics (KPIs) | Quarterly | Sponsor QA |
| Review of security incident reports | As reported + quarterly summary | Sponsor IT Security |
| Review of change notifications | As received | Sponsor QA |
| Review of service level performance reports | Monthly | Sponsor Operations |
| Review of CAPA status for open findings | Monthly until closure | Sponsor QA |
| Vendor management review meeting | Semi-annual | Sponsor Vendor Management |

---

## 20. Approval Signatures

### 20.1 Vendor Acknowledgment

By signing below, ArcaScience SAS acknowledges that the information provided in this Vendor Qualification Assessment is accurate and complete to the best of its knowledge. ArcaScience commits to notifying the sponsor of any material changes to the information provided herein.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CEO, ArcaScience SAS | _________________ | _________________ | ____/____/________ |
| Head of Quality Assurance, ArcaScience SAS | _________________ | _________________ | ____/____/________ |
| Head of Information Security, ArcaScience SAS | _________________ | _________________ | ____/____/________ |

### 20.2 Sponsor Assessment Team

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Auditor / Assessor | _________________ | _________________ | ____/____/________ |
| Subject Matter Expert - IT/Security | _________________ | _________________ | ____/____/________ |
| Subject Matter Expert - Data Integrity | _________________ | _________________ | ____/____/________ |
| Subject Matter Expert - AI/ML Validation | _________________ | _________________ | ____/____/________ |

### 20.3 Sponsor Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Head of Vendor Quality Management | _________________ | _________________ | ____/____/________ |
| Head of Quality Assurance | _________________ | _________________ | ____/____/________ |
| Head of Procurement | _________________ | _________________ | ____/____/________ |
| RAISE Framework Compliance Officer (Sanofi only) | _________________ | _________________ | ____/____/________ |

---

## Appendices

### Appendix A - Document Request Checklist

The following documents should be requested from ArcaScience and reviewed as part of this qualification:

| # | Document | Requested | Received | Reviewed | Acceptable |
|---|----------|-----------|----------|----------|-----------|
| A1 | Quality Manual (QM-ARCA-2025-001) | [ ] | [ ] | [ ] | [ ] |
| A2 | Validation Master Plan (VMP-ARCA-2025-001) | [ ] | [ ] | [ ] | [ ] |
| A3 | Information Security Policy (ISP-ARCA-2025-001) | [ ] | [ ] | [ ] | [ ] |
| A4 | Business Continuity Plan (BCP-ARCA-2025-001) | [ ] | [ ] | [ ] | [ ] |
| A5 | SOP Index (SOP-IDX-ARCA-2025-001) | [ ] | [ ] | [ ] | [ ] |
| A6 | Organizational Chart | [ ] | [ ] | [ ] | [ ] |
| A7 | Training Matrix and Sample Training Records | [ ] | [ ] | [ ] | [ ] |
| A8 | GAMP 5 Category 5 Validation Summary Report | [ ] | [ ] | [ ] | [ ] |
| A9 | Model Validation Reports (24 SLMs) | [ ] | [ ] | [ ] | [ ] |
| A10 | Change Control SOP and Sample Records | [ ] | [ ] | [ ] | [ ] |
| A11 | CAPA SOP and Open CAPA Log | [ ] | [ ] | [ ] | [ ] |
| A12 | Deviation Handling SOP and Sample Records | [ ] | [ ] | [ ] | [ ] |
| A13 | Most Recent Internal Audit Report | [ ] | [ ] | [ ] | [ ] |
| A14 | Most Recent Management Review Minutes | [ ] | [ ] | [ ] | [ ] |
| A15 | Cloud Provider Qualification / SOC 2 Type II Report | [ ] | [ ] | [ ] | [ ] |
| A16 | Penetration Test Report (Executive Summary) | [ ] | [ ] | [ ] | [ ] |
| A17 | Disaster Recovery Test Report | [ ] | [ ] | [ ] | [ ] |
| A18 | Financial Statements (Past 2 Years) | [ ] | [ ] | [ ] | [ ] |
| A19 | Professional Liability Insurance Certificate | [ ] | [ ] | [ ] | [ ] |
| A20 | Cyber Liability Insurance Certificate | [ ] | [ ] | [ ] | [ ] |
| A21 | Data Processing Agreement (DPA) Template | [ ] | [ ] | [ ] | [ ] |
| A22 | Service Level Agreement (SLA) Template | [ ] | [ ] | [ ] | [ ] |
| A23 | RAISE Framework Self-Assessment (Sanofi-specific) | [ ] | [ ] | [ ] | [ ] |
| A24 | ALCOA+ Compliance Evidence Package | [ ] | [ ] | [ ] | [ ] |
| A25 | 21 CFR Part 11 Compliance Assessment | [ ] | [ ] | [ ] | [ ] |

### Appendix B - Glossary

| Term | Definition |
|------|-----------|
| ALCOA+ | Attributable, Legible, Contemporaneous, Original, Accurate, Complete, Consistent, Enduring, Available |
| BRA | Benefit-Risk Assessment |
| BRAT | Benefit-Risk Action Team (framework for structured benefit-risk assessment) |
| CAPA | Corrective Action and Preventive Action |
| CIOMS | Council for International Organizations of Medical Sciences |
| DRP | Disaster Recovery Plan |
| DSUR | Development Safety Update Report |
| eCTD | Electronic Common Technical Document |
| GAMP | Good Automated Manufacturing Practice |
| GxP | Good Practice (collective term for GCP, GLP, GMP, GVP, etc.) |
| ISMS | Information Security Management System |
| PBRER | Periodic Benefit-Risk Evaluation Report |
| RAISE | Responsible AI at Sanofi for Everyone |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SLM | Small Language Model |
| SOP | Standard Operating Procedure |
| URS | User Requirements Specification |
| VMP | Validation Master Plan |

### Appendix C - Revision History

| Version | Date | Section(s) Changed | Change Description | Author |
|---------|------|--------------------|--------------------|--------|
| 1.0 | 2026-03-25 | All | Initial release | ArcaScience QA |

---

**End of Document**

**Document ID:** VQA-ARCA-2026-001 | **Version:** 1.0 | **Page Count:** [Auto-generated] | **Classification:** Confidential - Restricted Distribution
