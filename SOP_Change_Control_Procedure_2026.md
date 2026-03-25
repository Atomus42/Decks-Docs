# Change Control Procedure

**Document ID:** ARC-SOP-CC-2026-001
**Version:** 1.0
**Effective Date:** 2026-03-25
**Classification:** Confidential - Internal
**Document Owner:** ArcaScience GmbH, Quality Assurance
**Review Cycle:** Annual
**Applicable Standards:** GAMP 5, ICH Q10, FDA 21 CFR Part 11, EU Annex 11, ISO 27001:2022

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Definitions](#2-definitions)
3. [Change Classification Matrix](#3-change-classification-matrix)
4. [Change Request Initiation Procedure](#4-change-request-initiation-procedure)
5. [Impact Assessment Process](#5-impact-assessment-process)
6. [Risk Assessment for Proposed Changes](#6-risk-assessment-for-proposed-changes)
7. [Review and Approval Workflow](#7-review-and-approval-workflow)
8. [Implementation Planning](#8-implementation-planning)
9. [Testing Requirements per Change Type](#9-testing-requirements-per-change-type)
10. [Documentation Requirements](#10-documentation-requirements)
11. [Communication to Clients](#11-communication-to-clients)
12. [Post-Implementation Review](#12-post-implementation-review)
13. [Emergency Change Procedure](#13-emergency-change-procedure)
14. [Change Log Maintenance](#14-change-log-maintenance)
15. [Metrics and KPIs for Change Management](#15-metrics-and-kpis-for-change-management)
16. [Roles and Responsibilities Matrix](#16-roles-and-responsibilities-matrix)

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the formal change control process for the ArcaScience BRA (Benefit-Risk Assessment) Platform. It ensures that all changes to the validated platform - including its 24 clinician-trained Specialized Language Models (SLMs), infrastructure components, ontology libraries, and supporting systems - are evaluated, approved, implemented, and documented in a controlled and traceable manner.

This procedure is designed to:

- Maintain the GAMP 5 Category 5 validated state of the BRA Platform
- Preserve ALCOA+ compliant data integrity throughout all changes
- Ensure continued compliance with FDA 21 CFR Part 11 and EU Annex 11
- Protect the accuracy and reliability of benefit-risk assessments delivered to pharma clients
- Provide transparency to clients regarding changes that may affect their data or outputs

### 1.2 Scope

This SOP applies to all changes affecting:

| Scope Area | Examples |
|-----------|---------|
| **SLM Modules** | Any modification to the 24 SLMs, including model retraining, parameter tuning, prompt template changes, input/output schema modifications, threshold adjustments |
| **Ontology Libraries** | Updates to MedDRA (including version upgrades beyond v27.0), SNOMED CT, ChEBI, Disease Ontology normalization mappings |
| **Infrastructure** | Changes to Apache Airflow workflows, S3 bucket configurations, ElasticSearch cluster settings, DocumentDB schemas, QDrant collections, FastAPI/NestJS services |
| **Security Controls** | Modifications to access controls, encryption settings, network configurations, audit trail mechanisms, authentication systems |
| **Regulatory Alignment** | Changes driven by updates to BRAT/CIOMS XII framework, eCTD Module 2.5 specifications, PBRER format requirements |
| **Integration Interfaces** | API changes, data ingestion pipeline modifications, export format changes, client-facing dashboard updates |
| **Documentation** | Changes to SOPs, validation protocols, training materials, and system documentation |
| **Third-Party Components** | Updates to libraries, frameworks, operating systems, and cloud service configurations |

### 1.3 Out of Scope

The following are not covered by this SOP:

- Routine system administration tasks that do not affect the validated state (e.g., log rotation, monitoring threshold adjustments)
- Changes to non-production environments (development, sandbox) that have no pathway to production without a separate change request
- Client-specific configuration changes that operate within pre-validated parameter ranges (governed by the Client Configuration SOP, ARC-SOP-CFG-2026-001)

### 1.4 Related Documents

| Document ID | Title |
|------------|-------|
| ARC-VMP-2026-001 | Validation Master Plan |
| ARC-SOP-VAL-2026-001 | System Validation SOP |
| ARC-SOP-INC-2026-001 | Incident Management SOP |
| ARC-SOP-REL-2026-001 | Release Management SOP |
| ARC-DPA-2026-001 | Data Processing Agreement Template |
| ARC-SOP-CFG-2026-001 | Client Configuration SOP |
| ARC-SOP-TRN-2026-001 | Training Management SOP |

---

## 2. Definitions

### 2.1 Change Categories

| Category | Definition | Examples |
|----------|-----------|---------|
| **Emergency** | A change required to address an immediate threat to data integrity, patient safety, regulatory compliance, or platform availability. Emergency changes bypass the standard approval workflow but require retrospective review within 5 business days. | Critical security vulnerability exploitation; data corruption affecting active client assessments; regulatory authority-mandated immediate action; complete platform outage |
| **Standard** | A pre-planned change that follows the full change control workflow including impact assessment, risk assessment, approval, testing, and post-implementation review. | SLM retraining with new training data; MedDRA version upgrade; infrastructure scaling changes; new feature deployment; API version updates |
| **Minor** | A low-risk change with limited scope that follows a streamlined approval process. Minor changes must not affect the validated state of any SLM, alter data processing logic, or impact client outputs. | UI text corrections; non-functional configuration updates; documentation corrections; monitoring dashboard changes; log level adjustments |

### 2.2 Key Terms

| Term | Definition |
|------|-----------|
| **Change Request (CR)** | A formal, documented proposal to modify any component within the scope of this SOP. Each CR is assigned a unique identifier and tracked through its lifecycle. |
| **Change Advisory Board (CAB)** | The cross-functional body responsible for reviewing and approving Standard and Emergency changes. Composition defined in Section 16. |
| **Validated State** | The condition in which a system has been demonstrated, through documented evidence, to consistently produce results meeting predetermined specifications and quality attributes (per GAMP 5). |
| **GxP Impact** | The potential for a change to affect compliance with Good Practice regulations (GLP, GCP, GMP, GVP) that govern the data processed by the BRA Platform. |
| **Data Integrity Impact** | The potential for a change to affect the Attributability, Legibility, Contemporaneousness, Originality, Accuracy, Completeness, Consistency, Endurance, or Availability (ALCOA+) of data within the BRA Platform. |
| **Regression** | Unintended degradation of existing functionality or performance resulting from a change. |
| **Back-Out Plan** | A documented procedure for reversing a change and restoring the system to its pre-change state in the event of implementation failure. |
| **Change Freeze** | A period during which no changes (except Emergency) are permitted, typically aligned with client deliverable deadlines or regulatory submission windows. |
| **Configuration Item (CI)** | Any component under change management control, including SLMs, infrastructure components, ontologies, configurations, and documentation. |

---

## 3. Change Classification Matrix

### 3.1 Classification Criteria

Each change request shall be classified against the following dimensions:

| Dimension | Low Impact | Medium Impact | High Impact |
|-----------|-----------|---------------|-------------|
| **Validated State** | No effect on validated state; change operates within pre-validated parameters | Potential effect requiring partial re-validation (e.g., single SLM re-qualification) | Definite effect requiring full or substantial re-validation (e.g., multiple SLMs, infrastructure changes affecting processing logic) |
| **GxP Impact** | No GxP-relevant data or processes affected | GxP-relevant processes indirectly affected (e.g., supporting systems) | Direct impact on GxP-relevant data processing, audit trails, or electronic signatures |
| **Data Integrity Impact** | No ALCOA+ attributes affected | One or more ALCOA+ attributes potentially affected; mitigations identified | Direct impact on data integrity controls, audit trail integrity, or cryptographic hash chain |
| **Client Impact** | No visible change to client-facing outputs or interfaces | Minor change to client experience; no impact on data accuracy | Change to output format, data content, assessment methodology, or API contracts |
| **Security Impact** | No change to security posture | Change to non-critical security controls with equivalent alternatives | Change to critical security controls (encryption, access control, audit trails) |
| **Reversibility** | Immediately reversible with no data loss | Reversible within 4 hours with defined back-out procedure | Complex reversal; potential for data loss; extended back-out procedure |

### 3.2 Classification Decision Matrix

| Validated State | GxP Impact | Data Integrity | Client Impact | Classification | Approval Level |
|----------------|-----------|----------------|---------------|---------------|---------------|
| Low | Low | Low | Low | Minor | Technical Lead |
| Low | Low | Low | Medium | Standard | Technical Lead + Product Owner |
| Low | Medium | Low | Low | Standard | CAB (Quorum) |
| Medium | Any | Low | Any | Standard | CAB (Full) |
| Any | High | Any | Any | Standard | CAB (Full) + QA Director |
| Any | Any | High | Any | Standard | CAB (Full) + QA Director |
| Any | Any | Any | High | Standard | CAB (Full) + Client Notification |
| Critical Threat | Critical Threat | Critical Threat | Any | Emergency | Emergency CAB + Retrospective Full CAB |

### 3.3 Change Freeze Windows

| Window Type | Trigger | Duration | Exceptions |
|------------|---------|----------|-----------|
| Client Deliverable Freeze | 5 business days before client deliverable due date | Until deliverable acceptance | Emergency changes only |
| Regulatory Submission Freeze | 10 business days before regulatory submission | Until submission confirmation | Emergency changes only |
| Quarterly Close Freeze | Last 3 business days of each calendar quarter | 3 business days | Emergency changes only |
| Holiday Freeze | December 20 through January 2 | As defined | Emergency changes only |

---

## 4. Change Request Initiation Procedure

### 4.1 Who May Initiate a Change Request

Any ArcaScience employee or authorized contractor may initiate a Change Request. Client-requested changes shall be submitted through the designated Client Success Manager.

### 4.2 Step-by-Step Initiation Process

**Step 1: Identify the Need for Change**

The requestor identifies a need for change based on one or more of the following triggers:

- [ ] Defect or incident resolution
- [ ] Regulatory requirement update
- [ ] Ontology version update (MedDRA, SNOMED CT, ChEBI, Disease Ontology)
- [ ] SLM performance improvement or retraining need
- [ ] Security vulnerability remediation
- [ ] Client feature request
- [ ] Infrastructure optimization
- [ ] Third-party component update (library, framework, cloud service)
- [ ] Internal process improvement
- [ ] Audit finding remediation

**Step 2: Create the Change Request**

The requestor completes the Change Request Form with the following mandatory fields:

| Field | Description | Required |
|-------|-----------|----------|
| CR Title | Brief, descriptive title | Yes |
| Requestor Name | Full name and role | Yes |
| Requestor Department | Organizational unit | Yes |
| Date of Request | Submission date | Yes (auto-populated) |
| Priority | Critical / High / Medium / Low | Yes |
| Change Trigger | Reason for the change (from Step 1 list) | Yes |
| Description of Change | Detailed description of what is being changed, including current state and proposed future state | Yes |
| Justification | Business or technical rationale for the change | Yes |
| Affected Components | List of Configuration Items affected (SLMs, infrastructure, ontologies, etc.) | Yes |
| Proposed Classification | Requestor's proposed change category (Emergency / Standard / Minor) | Yes |
| Proposed Implementation Date | Target date for implementation | Yes |
| Dependencies | Other CRs, projects, or external factors this change depends on | If applicable |
| Attachments | Supporting documentation, design documents, test plans | If applicable |

**Step 3: Submit the Change Request**

1. The requestor submits the CR through the ArcaScience Change Management System (CMS)
2. The system auto-assigns a unique CR identifier in the format: `CR-YYYY-NNNN` (e.g., CR-2026-0042)
3. The system auto-assigns the CR to the Change Coordinator for initial triage
4. The requestor receives an acknowledgement with the CR identifier and expected triage timeline

**Step 4: Initial Triage**

The Change Coordinator performs initial triage within the following timelines:

| Priority | Triage SLA |
|----------|-----------|
| Critical | 2 hours |
| High | 4 hours |
| Medium | 1 business day |
| Low | 3 business days |

During triage, the Change Coordinator:

1. Validates completeness of the CR form
2. Confirms or adjusts the proposed classification against the matrix in Section 3.2
3. Assigns the CR to the appropriate impact assessment team
4. Sets the approval workflow based on classification
5. Returns incomplete CRs to the requestor with a list of required information

**Step 5: Assignment for Impact Assessment**

The Change Coordinator assigns the CR to the relevant subject matter experts for impact assessment (Section 5). The following roles are assigned based on affected components:

| Affected Component | Primary Assessor | Secondary Assessor |
|-------------------|-----------------|-------------------|
| SLM Modules | ML Engineering Lead | Clinical Validation Lead |
| Ontology Libraries | Ontology Manager | Clinical Validation Lead |
| Infrastructure (Airflow, S3, ES, DocumentDB, QDrant) | DevOps Lead | Security Engineer |
| API Layer (FastAPI, NestJS) | Backend Engineering Lead | QA Lead |
| Security Controls | Security Engineer | Compliance Officer |
| Regulatory Alignment | Regulatory Affairs Lead | QA Director |

---

## 5. Impact Assessment Process

### 5.1 Assessment Dimensions

Each assigned assessor evaluates the change against their domain of responsibility. The collective assessment covers the following dimensions:

### 5.2 SLM Module Impact Assessment

When a change affects one or more of the 24 Specialized Language Models:

| Assessment Item | Evaluation Criteria | Documentation Required |
|----------------|-------------------|----------------------|
| Model affected | Which specific SLM(s) are impacted? | List of SLM identifiers and names |
| Training data change | Does the change involve new, modified, or removed training data? | Training data change log; data provenance documentation |
| Model architecture change | Are there changes to model architecture, hyperparameters, or inference configuration? | Architecture comparison document |
| Performance impact | What is the expected impact on F1 scores (AE extraction >= 92%, Biomarker >= 90%, Risk >= 88%, Benefit >= 92%)? | Baseline performance metrics; projected post-change metrics |
| Input/output schema change | Are input or output data formats affected? | Schema diff; backward compatibility assessment |
| Clinician validation | Does the change require clinician re-validation? | Clinician validation protocol reference |
| Cross-model dependencies | Do other SLMs depend on the output of the affected SLM(s)? | Dependency map; cascade impact analysis |
| Prompt template change | Are prompt templates being modified? | Template diff; rationale for change |

### 5.3 Ontology Change Impact Assessment

When a change involves MedDRA, SNOMED CT, ChEBI, or Disease Ontology:

| Assessment Item | Evaluation Criteria | Documentation Required |
|----------------|-------------------|----------------------|
| Ontology version | Which ontology and what version transition? | Version comparison notes from ontology provider |
| Term changes | New terms added, terms deprecated, terms modified? | Term change list with affected counts |
| Mapping impact | How do term changes affect existing coded data? | Migration impact analysis; affected record counts |
| Backward compatibility | Can existing assessments be maintained with new coding? | Compatibility analysis; re-coding requirements |
| Client data impact | Which clients have data coded with affected terms? | Client-by-client impact summary |
| Regulatory alignment | Do term changes affect regulatory submission content? | Regulatory impact assessment |
| SLM retraining | Do SLMs need retraining or re-calibration for new terms? | SLM impact assessment cross-reference |

### 5.4 Infrastructure Change Impact Assessment

When a change affects Apache Airflow, S3, ElasticSearch, DocumentDB, QDrant, FastAPI, or NestJS:

| Assessment Item | Evaluation Criteria | Documentation Required |
|----------------|-------------------|----------------------|
| Component affected | Which infrastructure components are impacted? | Component inventory with versions |
| Data path impact | Does the change affect how data flows through the platform? | Updated data flow diagram |
| Performance impact | Expected impact on latency, throughput, or resource consumption? | Performance baseline; projected post-change metrics |
| Availability impact | Is there planned downtime? Duration? | Maintenance window proposal; client notification plan |
| Data migration | Does the change require data migration? | Migration plan; rollback procedure; data verification steps |
| Security impact | Does the change affect network topology, access controls, or encryption? | Security impact assessment |
| Compliance impact | Does the change affect 21 CFR Part 11, EU Annex 11, or ALCOA+ compliance? | Compliance impact matrix |
| EU data residency | Does the change affect data residency in the EU? | Data residency confirmation |
| Disaster recovery | Does the change affect DR capability? | Updated DR plan if applicable |

### 5.5 Impact Assessment Report

The assessors compile their findings into an Impact Assessment Report containing:

1. **Summary of Findings** - One-paragraph executive summary of the overall impact
2. **Component-by-Component Assessment** - Detailed findings per affected component
3. **Cumulative Risk Rating** - Low / Medium / High / Critical, based on the matrix in Section 3
4. **Recommended Classification** - Confirmation or adjustment of the CR classification
5. **Testing Requirements** - Recommended testing scope (referencing Section 9)
6. **Resource Requirements** - Estimated effort (person-hours), infrastructure resources, and timeline
7. **Dependencies and Constraints** - Identified dependencies on other CRs, external factors, or change freeze windows
8. **Recommendation** - Proceed / Proceed with conditions / Defer / Reject

The Impact Assessment Report shall be completed within the following timelines:

| CR Priority | Assessment SLA |
|------------|---------------|
| Critical | 4 hours |
| High | 2 business days |
| Medium | 5 business days |
| Low | 10 business days |

---

## 6. Risk Assessment for Proposed Changes

### 6.1 Risk Assessment Methodology

All Standard and Emergency changes shall undergo a formal risk assessment using the following framework.

### 6.2 Risk Identification

For each change, the following risk categories shall be evaluated:

| Risk Category | Risk Questions |
|--------------|---------------|
| **Patient Safety** | Could this change affect the accuracy of adverse event detection, risk signal identification, or benefit assessment in a way that could indirectly impact patient safety decisions? |
| **Data Integrity** | Could this change compromise any ALCOA+ attribute? Could it affect audit trail integrity or cryptographic hash chain validity? |
| **Regulatory Compliance** | Could this change affect compliance with FDA 21 CFR Part 11, EU Annex 11, GDPR, or GxP requirements? |
| **Validated State** | Could this change invalidate the GAMP 5 Category 5 validation of any SLM or platform component? |
| **Client Deliverables** | Could this change affect the accuracy, timeliness, or format of client deliverables (BRAT/CIOMS XII, eCTD Module 2.5, PBRER)? |
| **Service Availability** | Could this change cause unplanned downtime, performance degradation, or data loss? |
| **Security** | Could this change introduce vulnerabilities, weaken access controls, or expose data to unauthorized access? |
| **Reversibility** | If the change fails, can it be reversed? What is the complexity and duration of reversal? |

### 6.3 Risk Scoring Matrix

Each identified risk shall be scored on two dimensions:

**Likelihood:**

| Score | Level | Definition |
|-------|-------|-----------|
| 1 | Rare | Less than 1% probability of occurrence |
| 2 | Unlikely | 1% to 10% probability |
| 3 | Possible | 10% to 50% probability |
| 4 | Likely | 50% to 90% probability |
| 5 | Almost Certain | Greater than 90% probability |

**Severity:**

| Score | Level | Definition |
|-------|-------|-----------|
| 1 | Negligible | No impact on data integrity, compliance, or client deliverables; cosmetic only |
| 2 | Minor | Minor impact; workaround available; no regulatory or data integrity concern |
| 3 | Moderate | Moderate impact on one or more areas; requires intervention; potential for client notification |
| 4 | Major | Significant impact on data integrity, compliance, or client deliverables; regulatory reporting may be required |
| 5 | Critical | Severe impact on patient safety, data integrity, or regulatory compliance; immediate regulatory reporting required |

**Risk Rating Matrix:**

| | Negligible (1) | Minor (2) | Moderate (3) | Major (4) | Critical (5) |
|---|---|---|---|---|---|
| **Almost Certain (5)** | Medium | High | High | Critical | Critical |
| **Likely (4)** | Low | Medium | High | Critical | Critical |
| **Possible (3)** | Low | Medium | Medium | High | Critical |
| **Unlikely (2)** | Low | Low | Medium | Medium | High |
| **Rare (1)** | Low | Low | Low | Medium | High |

### 6.4 Risk Response Actions

| Risk Rating | Required Actions |
|------------|-----------------|
| **Critical** | Change cannot proceed without executive-level approval. All identified risks must have documented mitigations that reduce the residual risk to Medium or below. Enhanced back-out plan required. |
| **High** | CAB approval required with documented risk mitigations. Residual risk must be reduced to Medium or below. Comprehensive back-out plan required. Additional testing scope. |
| **Medium** | Standard CAB approval. Documented mitigations for each Medium-rated risk. Standard back-out plan. Standard testing scope. |
| **Low** | Standard approval per classification. Mitigations documented where practical. Standard back-out plan. Standard testing scope. |

### 6.5 Risk Assessment Documentation

The Risk Assessment shall be documented as part of the Change Request and include:

- [ ] Risk identification worksheet (all categories evaluated)
- [ ] Risk scoring for each identified risk (likelihood and severity)
- [ ] Risk mitigation plan for each Medium, High, or Critical risk
- [ ] Residual risk rating after mitigations
- [ ] Risk owner assignment for each identified risk
- [ ] Acceptance signature from the CAB Chairperson (for High and Critical residual risks)

---

## 7. Review and Approval Workflow

### 7.1 Approval Authority Matrix

| Change Classification | Impact Level | Approval Authority | Quorum Requirements |
|----------------------|-------------|-------------------|-------------------|
| Minor | Low across all dimensions | Technical Lead of affected area | Single approver |
| Minor | Low with Medium client impact | Technical Lead + Product Owner | Both must approve |
| Standard | Medium in any dimension | Change Advisory Board (CAB) | Minimum 3 CAB members including QA representative |
| Standard | High in validated state or GxP | CAB (Full) + QA Director | All CAB members + QA Director |
| Standard | High in data integrity | CAB (Full) + QA Director | All CAB members + QA Director |
| Standard | High client impact | CAB (Full) + Client notification | All CAB members; client acknowledges notification |
| Emergency | Any | Emergency CAB (minimum 2 members) | Emergency CAB Chair + one additional member |

### 7.2 Change Advisory Board Composition

| Role | Member | Responsibility | Voting |
|------|--------|---------------|--------|
| CAB Chairperson | Head of Engineering | Chairs CAB meetings; final decision authority on tied votes | Yes |
| QA Representative | QA Director or delegate | Validates compliance and validation impact assessment | Yes |
| Clinical Validation Lead | Clinical Validation Manager | Assesses clinical accuracy impact | Yes |
| Security Representative | CISO or delegate | Evaluates security implications | Yes |
| DevOps Representative | DevOps Lead | Assesses infrastructure feasibility and risk | Yes |
| Regulatory Affairs | Regulatory Affairs Lead | Evaluates regulatory compliance impact | Yes |
| Product Owner | Product Management Lead | Assesses client impact and business priority | Yes |
| Change Coordinator | Quality Systems Specialist | Facilitates; presents CR details; non-voting | No |

### 7.3 Approval Process - Standard Changes

```
Step 1: Change Coordinator presents CR to CAB
        - Impact Assessment Report
        - Risk Assessment
        - Proposed implementation plan
        - Testing plan
        |
Step 2: CAB members review and discuss
        - Each member evaluates from their domain perspective
        - Questions directed to assessors and requestor
        |
Step 3: CAB votes
        - Approve: CR proceeds to implementation
        - Approve with Conditions: CR proceeds after conditions are met (documented)
        - Defer: CR returned for additional information or assessment
        - Reject: CR closed with documented rationale
        |
Step 4: Decision recorded
        - Vote outcome documented in CMS
        - Conditions (if any) documented with due dates
        - Implementation authorization (if approved) with authorized window
```

### 7.4 Approval Process - Minor Changes

```
Step 1: Technical Lead reviews CR and Impact Assessment
        |
Step 2: Technical Lead approves or requests additional information
        - If client impact is Medium, Product Owner also approves
        |
Step 3: Decision recorded in CMS
        |
Step 4: Implementation authorized
```

### 7.5 CAB Meeting Schedule

| Meeting Type | Frequency | Duration | Purpose |
|-------------|-----------|----------|---------|
| Standing CAB | Weekly (Tuesday, 10:00 CET) | 60 minutes | Review pending Standard CRs; status updates on in-progress changes |
| Ad-hoc CAB | As needed (24 hours notice) | 30 to 60 minutes | Urgent Standard CRs that cannot wait for standing meeting |
| Emergency CAB | Immediate (within 2 hours of request) | 30 minutes | Emergency CRs requiring immediate decision |

### 7.6 Escalation Procedure

If the CAB cannot reach consensus:

1. The CAB Chairperson may exercise a casting vote
2. If the QA Director objects on compliance grounds, the CR is escalated to the CEO
3. The CEO's decision is final and documented in the CR record
4. Compliance objections that are overridden must be documented with a justification and acknowledged by the CEO in writing

---

## 8. Implementation Planning

### 8.1 Implementation Plan Requirements

Every approved Standard and Emergency change shall have a documented Implementation Plan containing:

| Section | Content | Required For |
|---------|---------|-------------|
| **Objective** | Clear statement of what the implementation will achieve | All changes |
| **Prerequisites** | Conditions that must be met before implementation begins | All changes |
| **Implementation Steps** | Numbered, sequential steps with responsible individuals and estimated durations | All changes |
| **Back-Out Plan** | Step-by-step procedure for reversing the change if implementation fails | Standard and Emergency |
| **Back-Out Trigger Criteria** | Specific, measurable criteria that trigger back-out execution | Standard and Emergency |
| **Verification Steps** | Post-implementation checks to confirm successful deployment | All changes |
| **Maintenance Window** | Scheduled time for implementation (if downtime is required) | Changes requiring downtime |
| **Communication Plan** | Who needs to be informed, when, and through what channel | All changes |
| **Resource Requirements** | Personnel, infrastructure, and tools needed | All changes |
| **Dependencies** | Other changes, external parties, or conditions this implementation depends on | If applicable |
| **Go/No-Go Checklist** | Final checklist verified immediately before implementation begins | Standard and Emergency |

### 8.2 Go/No-Go Checklist

Before proceeding with implementation, the following checklist must be verified:

- [ ] CR is in "Approved" status in the CMS
- [ ] All approval conditions have been met and documented
- [ ] Implementation Plan has been reviewed by at least one person not involved in the change
- [ ] Back-out plan has been documented and verified as feasible
- [ ] All required testing environments are available and configured
- [ ] All required personnel are available for the implementation window
- [ ] Current system backup has been verified (completed within the last 24 hours)
- [ ] Client notifications have been sent (if required per Section 11)
- [ ] No active Change Freeze windows conflict with the implementation
- [ ] Monitoring and alerting systems are operational
- [ ] Communication channels are established (e.g., dedicated Slack channel for the implementation)

### 8.3 Implementation Windows

| Change Type | Permitted Windows | Restrictions |
|------------|------------------|-------------|
| Minor (no downtime) | Business hours (09:00 to 18:00 CET) | Not during Change Freeze windows |
| Standard (no downtime) | Business hours, with monitoring | Not during Change Freeze windows |
| Standard (with downtime) | Maintenance window: Saturday 02:00 to 06:00 CET | Minimum 5 business days advance client notification |
| Emergency | Any time | Retrospective CAB review within 5 business days |

### 8.4 Deployment Strategy

| Strategy | When to Use | Description |
|----------|------------|-------------|
| **Blue-Green** | Infrastructure changes, API updates | Two identical environments; traffic switched from blue (current) to green (new) after verification; instant rollback by switching back |
| **Canary** | SLM updates, processing logic changes | New version deployed to a small percentage of traffic; monitored; gradually expanded if metrics are healthy |
| **Rolling** | Non-critical updates, library upgrades | Instances updated sequentially; service maintained throughout |
| **Big Bang** | Schema migrations, ontology upgrades requiring atomic switch | All components updated simultaneously during maintenance window; higher risk, requires comprehensive back-out plan |

---

## 9. Testing Requirements per Change Type

### 9.1 Testing Matrix

| Test Type | Minor | Standard (Low/Medium Risk) | Standard (High/Critical Risk) | Emergency |
|-----------|-------|---------------------------|------------------------------|-----------|
| Unit Testing | Required | Required | Required | Required (may be deferred 48 hrs) |
| Integration Testing | If applicable | Required | Required | Required (may be deferred 48 hrs) |
| SLM Performance Testing | Not required | If SLM affected | Required for all affected SLMs | If SLM affected |
| Regression Testing | Targeted | Targeted | Full regression suite | Targeted |
| User Acceptance Testing (UAT) | Not required | If client-facing | Required | Not required (deferred) |
| Security Testing | Not required | If security-impacting | Required | If security-impacting |
| Performance/Load Testing | Not required | If infrastructure | Required | Not required (deferred) |
| Data Integrity Verification | Not required | Required | Required | Required |
| Audit Trail Verification | Not required | Required | Required | Required |
| Compliance Verification | Not required | If GxP-impacting | Required | Required (may be deferred 48 hrs) |
| Back-Out Testing | Not required | Recommended | Required (in pre-production) | Not required |

### 9.2 SLM Performance Testing Requirements

When a change affects any of the 24 SLMs, the following performance validation is required:

| SLM Function | Minimum F1 Threshold | Test Dataset | Pass Criteria |
|-------------|---------------------|-------------|--------------|
| Adverse Event Extraction | 0.92 (92%) | Clinician-validated gold standard (minimum 500 annotated examples) | F1 >= 0.92 on held-out test set |
| Biomarker Identification | 0.90 (90%) | Clinician-validated gold standard (minimum 300 annotated examples) | F1 >= 0.90 on held-out test set |
| Risk Signal Detection | 0.88 (88%) | Clinician-validated gold standard (minimum 400 annotated examples) | F1 >= 0.88 on held-out test set |
| Benefit Assessment | 0.92 (92%) | Clinician-validated gold standard (minimum 400 annotated examples) | F1 >= 0.92 on held-out test set |

Additional SLM-specific tests:

- [ ] Precision and recall breakdowns (not just F1) to detect trade-off shifts
- [ ] Confidence calibration analysis (predicted probabilities vs. observed frequencies)
- [ ] Edge case performance on known difficult examples
- [ ] Cross-therapeutic area performance consistency
- [ ] Output format conformance to schema specifications
- [ ] Latency benchmarks (P50, P95, P99 response times)

### 9.3 Re-Validation Triggers

The following changes trigger formal re-validation under GAMP 5 Category 5:

| Trigger | Scope of Re-Validation |
|---------|----------------------|
| SLM retraining with new data (more than 10% new training examples) | Full OQ and PQ for affected SLM(s) |
| SLM architecture change | Full IQ, OQ, and PQ for affected SLM(s) |
| Ontology major version upgrade (e.g., MedDRA v27.0 to v28.0) | OQ and PQ for all SLMs using the ontology |
| Infrastructure platform migration | Full IQ for affected infrastructure; OQ and PQ for dependent components |
| Cryptographic algorithm change | Full IQ, OQ, and PQ for audit trail subsystem |
| Database schema migration | OQ and PQ for affected data stores and dependent processing |
| API contract change (breaking) | OQ for API layer; integration testing with all clients |
| Security control architecture change | IQ and OQ for affected security controls |

### 9.4 Regression Testing

| Regression Scope | When Required | Coverage |
|-----------------|---------------|---------|
| **Targeted Regression** | Minor changes; Standard changes with isolated impact | Test cases directly related to the changed component and its immediate dependencies |
| **Extended Regression** | Standard changes with cross-component impact | Targeted regression plus test cases for components with data flow dependencies |
| **Full Regression** | High/Critical risk Standard changes; re-validation triggers | Complete regression suite covering all 24 SLMs, all data pipelines, all client-facing outputs, audit trail integrity, and compliance checks |

### 9.5 Test Environment Requirements

| Environment | Purpose | Data | Parity with Production |
|------------|---------|------|----------------------|
| Development | Developer testing, unit tests | Synthetic data only | Low (development configuration) |
| Staging | Integration testing, SLM performance testing | Anonymized production-equivalent data | High (production-equivalent configuration) |
| Pre-Production | UAT, full regression, back-out testing | Anonymized production-equivalent data | Full (mirrors production configuration) |
| Production | Live operations | Real client data | N/A (is production) |

### 9.6 Test Documentation

All testing shall be documented in a Test Summary Report containing:

- [ ] Test plan reference and version
- [ ] Test environment description and configuration evidence
- [ ] Test cases executed (total, passed, failed, blocked)
- [ ] Defects found (with severity and resolution status)
- [ ] SLM performance results vs. thresholds (if applicable)
- [ ] Regression test results
- [ ] Data integrity verification results
- [ ] Audit trail verification results
- [ ] Test execution evidence (screenshots, log excerpts, automated test reports)
- [ ] Tester sign-off
- [ ] QA review and sign-off
- [ ] Recommendation: Proceed to production / Do not proceed (with rationale)

---

## 10. Documentation Requirements

### 10.1 Change Request Documentation

Every change, regardless of classification, shall be documented in the Change Management System with the following records:

| Document | Minor | Standard | Emergency |
|----------|-------|----------|-----------|
| Change Request Form | Required | Required | Required (may be completed retrospectively within 24 hours) |
| Impact Assessment Report | Summary | Full | Summary (full within 5 business days) |
| Risk Assessment | Not required | Full | Summary (full within 5 business days) |
| Implementation Plan | Summary | Full | Summary (full retrospectively within 5 business days) |
| Test Plan | Not required | Full | Summary (full within 5 business days) |
| Test Summary Report | Not required | Full | Summary (full within 5 business days) |
| Back-Out Plan | Not required | Full | Summary |
| Client Notification | If applicable | If applicable | If applicable |
| Post-Implementation Review | Not required | Required | Required |
| Updated System Documentation | If applicable | Required | Required (within 10 business days) |
| Updated Validation Documentation | Not required | If re-validation triggered | If re-validation triggered |
| Updated Training Materials | Not required | If user-facing | If user-facing (within 10 business days) |
| Change Closure Report | Simple sign-off | Full | Full (within 10 business days) |

### 10.2 Document Retention

All change control documentation shall be retained in the document management system for:

| Document Type | Retention Period |
|--------------|----------------|
| Change Requests and associated records | Life of the platform + 5 years |
| Validation and re-validation evidence | Life of the platform + 15 years |
| Audit trail records | Life of the platform + 7 years (minimum) |
| Client notification records | Life of client engagement + 5 years |
| Test evidence | Life of the platform + 5 years |

### 10.3 Traceability

The Change Management System shall maintain bidirectional traceability between:

- Change Requests and affected Configuration Items
- Change Requests and associated test cases and test results
- Change Requests and updated documentation (SOPs, validation protocols, system descriptions)
- Change Requests and client notifications
- Change Requests and related Incident Reports (where the change addresses an incident)
- Change Requests and related CAPAs (Corrective and Preventive Actions)

---

## 11. Communication to Clients

### 11.1 Client Notification Requirements

| Change Type | Client Impact | Notification Timing | Notification Content |
|------------|--------------|--------------------|--------------------|
| Minor | None | No notification required | N/A |
| Minor | Low (cosmetic, no data impact) | Within 5 business days post-implementation | Brief description of change |
| Standard | Medium (format, interface changes) | Minimum **15 business days** before implementation | Full change summary, impact assessment, timeline |
| Standard | High (output, methodology, API changes) | Minimum **30 business days** before implementation | Full change summary, impact assessment, timeline, migration guide |
| Emergency | Any | Within **4 hours** of implementation | Nature of emergency, actions taken, impact assessment |
| Ontology Upgrade | Any | Minimum **30 business days** before implementation | Version details, term changes, impact on coded data, re-coding plan |
| SLM Retraining | Any | Minimum **15 business days** before implementation | Retraining scope, performance validation results, expected impact |

### 11.2 Notification Content Requirements

Client notifications for Standard changes with Medium or High impact shall include:

1. **Change Reference** - CR identifier and title
2. **Change Description** - Clear, non-technical summary of what is changing and why
3. **Impact Assessment** - How the change affects the client's data, outputs, integrations, or workflows
4. **Timeline** - Implementation date and any maintenance windows
5. **Action Required** - Any actions the client needs to take (e.g., API migration, output format update, re-validation of downstream processes)
6. **Testing Results** - Summary of testing performed and results (SLM performance metrics where relevant)
7. **Contact Information** - Designated contact for questions or concerns
8. **Opt-Out/Deferral Options** - Where applicable, options for the client to defer the change or opt out (with implications documented)

### 11.3 Notification Channels

| Channel | Use Case |
|---------|---------|
| Email to designated client contact | All notifications |
| Client portal (change log section) | All notifications (posted concurrently with email) |
| Scheduled call / meeting | High-impact Standard changes; Emergency change follow-up |
| API changelog | API changes (machine-readable changelog endpoint) |

### 11.4 Client Acknowledgement

For High-impact changes:

- [ ] Client acknowledgement of notification is required before implementation proceeds
- [ ] If no acknowledgement is received within 10 business days, a reminder is sent
- [ ] If no acknowledgement is received within 20 business days, the Client Success Manager escalates to the client's project sponsor
- [ ] Implementation shall not proceed without documented client acknowledgement (exception: Emergency changes)

---

## 12. Post-Implementation Review

### 12.1 Review Timeline

| Change Type | PIR Timing |
|------------|-----------|
| Minor | Not required (unless issues arise) |
| Standard | Within 10 business days of implementation |
| Emergency | Within 5 business days of implementation |

### 12.2 Post-Implementation Review Checklist

The following items shall be evaluated during the PIR:

**Implementation Outcome:**

- [ ] Was the change implemented as planned?
- [ ] Were there any deviations from the Implementation Plan? If so, were they documented?
- [ ] Was the back-out plan triggered? If so, why, and was it effective?
- [ ] Were there any unplanned outages or incidents during implementation?

**Verification Results:**

- [ ] Do all post-implementation verification checks pass?
- [ ] Are SLM performance metrics within validated thresholds? (AE F1 >= 92%, Biomarker F1 >= 90%, Risk F1 >= 88%, Benefit F1 >= 92%)
- [ ] Is the audit trail intact and hash chain verified?
- [ ] Are all ALCOA+ attributes maintained?
- [ ] Is data integrity confirmed across all affected data stores?

**Client Impact:**

- [ ] Have any client-reported issues been received?
- [ ] Are client deliverables (BRAT/CIOMS XII, eCTD Module 2.5, PBRER) generating correctly?
- [ ] Were client notifications sent as planned?
- [ ] Did clients acknowledge notifications (where required)?

**Compliance Verification:**

- [ ] Does the system remain in a validated state per GAMP 5?
- [ ] Is 21 CFR Part 11 compliance maintained?
- [ ] Is EU Annex 11 compliance maintained?
- [ ] Are security controls functioning as expected?
- [ ] Is EU data residency maintained?

**Documentation:**

- [ ] Is all change documentation complete and filed in the CMS?
- [ ] Have SOPs, system documentation, and training materials been updated?
- [ ] Has the validation documentation been updated (if re-validation was triggered)?
- [ ] Has the Change Log been updated?

**Lessons Learned:**

- [ ] What went well?
- [ ] What could be improved?
- [ ] Are there process improvements to recommend?
- [ ] Are there follow-up actions required?

### 12.3 PIR Outcomes

| Outcome | Action |
|---------|--------|
| **Successful** | CR status set to "Closed - Successful"; PIR report filed |
| **Successful with Issues** | CR status set to "Closed - Successful with Issues"; follow-up CRs or CAPAs raised as needed |
| **Failed** | CR status set to "Closed - Failed"; back-out executed; root cause analysis initiated; follow-up CR or Incident raised |
| **Partially Implemented** | CR status set to "Open - Partial"; remaining implementation planned; follow-up CR may be raised |

---

## 13. Emergency Change Procedure

### 13.1 Emergency Change Criteria

A change qualifies as an Emergency only when one or more of the following conditions exist:

1. **Data Integrity Threat** - Active or imminent compromise of ALCOA+ data integrity, including audit trail tampering or cryptographic hash chain breakage
2. **Patient Safety Risk** - A defect in SLM output that could lead to incorrect benefit-risk assessments affecting patient safety decisions
3. **Security Breach** - Active exploitation of a security vulnerability affecting Personal Data or system integrity
4. **Regulatory Mandate** - Immediate regulatory authority directive requiring system modification within a timeline incompatible with the Standard change process
5. **Complete Platform Outage** - Total loss of BRA Platform availability affecting active client engagements
6. **Data Loss** - Active or imminent loss of client data or processing outputs

### 13.2 Emergency Change Process

```
Step 1: DECLARE EMERGENCY
        - Requestor contacts the Emergency CAB Chair (or delegate) by phone
        - Verbal declaration of emergency with brief description
        - Emergency CAB Chair confirms emergency classification
        |
Step 2: EMERGENCY CAB CONVENES (within 2 hours)
        - Minimum: Emergency CAB Chair + one additional CAB member
        - Verbal briefing on the situation, proposed change, and risk
        - Verbal approval to proceed (documented retrospectively)
        |
Step 3: IMPLEMENT
        - Implementation proceeds immediately
        - All actions logged in real time (who, what, when)
        - Minimal viable change to address the immediate threat
        - Monitoring intensified during and after implementation
        |
Step 4: VERIFY
        - Post-implementation verification checks executed
        - Data integrity confirmed (ALCOA+ checks, hash chain verification)
        - SLM performance verified (if SLMs affected)
        - Security posture confirmed (if security-related)
        |
Step 5: NOTIFY
        - Affected clients notified within 4 hours of implementation
        - Internal stakeholders notified
        |
Step 6: RETROSPECTIVE DOCUMENTATION (within 24 hours)
        - Complete Change Request Form filed in CMS
        - Implementation actions documented
        - Verification results documented
        |
Step 7: RETROSPECTIVE REVIEW (within 5 business days)
        - Full CAB reviews the Emergency change
        - Complete Impact Assessment filed
        - Complete Risk Assessment filed
        - Determine if additional changes are needed
        - Root cause analysis completed
        - CAPA raised if process or system deficiency identified
        |
Step 8: FULL TESTING (within 5 business days, unless deferred)
        - Complete testing per Section 9 for the nature of the change
        - Re-validation if triggered per Section 9.3
        - Test Summary Report filed
```

### 13.3 Emergency Change Limitations

- Emergency changes shall implement the **minimum viable change** to address the immediate threat
- Feature enhancements or non-critical improvements shall not be bundled with Emergency changes
- If the root cause analysis identifies the need for a broader change, a separate Standard CR shall be raised
- No more than **3 consecutive Emergency changes** may be made to the same component without a comprehensive review by the full CAB

### 13.4 Emergency Change Authorities

| Role | Authority |
|------|----------|
| Emergency CAB Chair (Head of Engineering) | Approve any Emergency change |
| QA Director | Approve any Emergency change; can overrule on compliance grounds |
| CISO | Approve security-related Emergency changes |
| DevOps Lead | Approve infrastructure Emergency changes (in absence of CAB Chair) |
| On-Call Engineer | Execute approved Emergency changes; cannot self-approve |

---

## 14. Change Log Maintenance

### 14.1 Change Log Structure

The Change Log is maintained in the Change Management System and provides a comprehensive, searchable record of all changes. Each entry contains:

| Field | Description |
|-------|-----------|
| CR ID | Unique identifier (CR-YYYY-NNNN) |
| Title | Brief descriptive title |
| Category | Emergency / Standard / Minor |
| Priority | Critical / High / Medium / Low |
| Status | Open / In Assessment / Approved / In Implementation / In Testing / In PIR / Closed |
| Requestor | Name and department |
| Date Submitted | Date CR was created |
| Date Approved | Date of CAB or delegate approval |
| Date Implemented | Date change was deployed to production |
| Date Closed | Date PIR was completed and CR closed |
| Affected Components | List of Configuration Items affected |
| Risk Rating | Low / Medium / High / Critical |
| Client Impact | None / Low / Medium / High |
| Clients Notified | List of clients notified (if applicable) |
| Validation Impact | None / Partial Re-Validation / Full Re-Validation |
| Approver(s) | Names and roles of approvers |
| Outcome | Successful / Successful with Issues / Failed / Cancelled |

### 14.2 Change Log Accessibility

| Audience | Access Level |
|----------|-------------|
| ArcaScience internal staff | Full access (read) to all entries |
| Change Coordinator | Full access (read/write) |
| CAB Members | Full access (read); approval actions in their CRs |
| Client - designated contacts | Read access to CRs affecting their engagement (filtered view) |
| Auditors (internal and external) | Full access (read) during audit engagements |
| Regulatory authorities | Access upon formal request, subject to legal review |

### 14.3 Change Log Reporting

The Change Coordinator shall produce the following reports:

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| Weekly Change Summary | Weekly | CAB Members, Engineering Leads | Open CRs, CRs implemented this week, CRs pending approval |
| Monthly Change Metrics | Monthly | Senior Management, QA | KPIs per Section 15; trend analysis |
| Quarterly Change Review | Quarterly | Executive Team, QA Director | Strategic analysis; recurring change patterns; improvement recommendations |
| Annual Change Audit Report | Annually | Executive Team, External Auditors | Comprehensive annual summary; compliance assessment; audit readiness |
| Client Change Report | Per client SOW schedule | Client designated contacts | Changes affecting the specific client's engagement |

---

## 15. Metrics and KPIs for Change Management

### 15.1 Process Efficiency Metrics

| KPI | Definition | Target | Measurement |
|-----|-----------|--------|-------------|
| **Change Throughput** | Number of CRs completed per month | Tracked (no fixed target) | Count of CRs reaching "Closed" status per calendar month |
| **Triage SLA Compliance** | Percentage of CRs triaged within SLA | >= 95% | (CRs triaged within SLA / Total CRs) x 100 |
| **Assessment SLA Compliance** | Percentage of Impact Assessments completed within SLA | >= 90% | (Assessments within SLA / Total Assessments) x 100 |
| **Approval Cycle Time** | Average time from CR submission to approval | <= 5 business days (Standard); <= 4 hours (Emergency) | Mean calendar days from submission to approval |
| **Implementation Lead Time** | Average time from approval to production deployment | <= 10 business days (Standard); <= 24 hours (Emergency) | Mean calendar days from approval to implementation |
| **End-to-End Cycle Time** | Average time from CR submission to closure | <= 30 business days (Standard) | Mean calendar days from submission to closure |
| **Change Backlog** | Number of approved but unimplemented CRs | <= 15 at any time | Count of CRs in "Approved" or "In Implementation" status |

### 15.2 Quality Metrics

| KPI | Definition | Target | Measurement |
|-----|-----------|--------|-------------|
| **Change Success Rate** | Percentage of changes implemented without back-out | >= 95% | (Successful implementations / Total implementations) x 100 |
| **Change-Related Incidents** | Number of incidents caused by changes | <= 2 per quarter | Count of incidents with root cause traced to a CR |
| **Back-Out Rate** | Percentage of changes requiring back-out | <= 5% | (Back-outs / Total implementations) x 100 |
| **Re-Work Rate** | Percentage of CRs requiring re-work after PIR | <= 10% | (CRs with "Successful with Issues" / Total closed CRs) x 100 |
| **SLM Performance Preservation** | Percentage of SLM-affecting changes that maintain F1 thresholds post-implementation | 100% | (Changes maintaining thresholds / SLM-affecting changes) x 100 |
| **Data Integrity Preservation** | Percentage of changes with confirmed ALCOA+ compliance post-implementation | 100% | (Changes with ALCOA+ confirmation / Total changes) x 100 |
| **Validation State Preservation** | Percentage of changes maintaining validated state without unplanned re-validation | >= 98% | (Changes maintaining state / Total changes) x 100 |

### 15.3 Compliance Metrics

| KPI | Definition | Target | Measurement |
|-----|-----------|--------|-------------|
| **Documentation Completeness** | Percentage of closed CRs with all required documentation | 100% | (Fully documented CRs / Total closed CRs) x 100 |
| **Client Notification SLA** | Percentage of client notifications sent within required timelines | 100% | (On-time notifications / Required notifications) x 100 |
| **Emergency Change Ratio** | Percentage of all changes classified as Emergency | <= 5% | (Emergency CRs / Total CRs) x 100 |
| **Emergency Retrospective Compliance** | Percentage of Emergency changes with retrospective documentation within 5 business days | 100% | (Compliant Emergency CRs / Total Emergency CRs) x 100 |
| **Audit Finding Closure** | Percentage of audit findings related to change control closed within agreed timelines | 100% | (On-time closures / Total findings) x 100 |

### 15.4 KPI Review and Escalation

| Metric Status | Action |
|--------------|--------|
| All KPIs within target | Report in monthly metrics review; no action required |
| One or more KPIs amber (within 10% of target) | Investigate root cause; document in monthly report; corrective plan within 30 days |
| One or more KPIs red (outside target by more than 10%) | Escalate to QA Director; root cause analysis within 10 business days; CAPA raised if systemic issue identified |
| Sustained red status (2+ consecutive months) | Escalate to Executive Team; process improvement initiative launched |

---

## 16. Roles and Responsibilities Matrix

### 16.1 RACI Matrix

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

| Activity | Requestor | Change Coordinator | Technical Lead | CAB Chair | QA Director | Security Lead | DevOps Lead | Clinical Lead | Regulatory Lead | Product Owner | Client |
|----------|-----------|-------------------|---------------|-----------|-------------|---------------|-------------|---------------|----------------|--------------|--------|
| Initiate CR | R/A | I | C | I | I | I | I | I | I | C | C |
| Triage CR | I | R/A | C | I | - | - | - | - | - | - | - |
| Impact Assessment | C | R | A | I | C | C | C | C | C | C | - |
| Risk Assessment | C | R | A | C | C | C | C | C | C | - | - |
| Approve (Minor) | I | I | R/A | I | I | - | - | - | - | C | - |
| Approve (Standard) | I | R | C | A | C | C | C | C | C | C | I |
| Approve (Emergency) | I | I | C | R/A | C | C | C | - | - | - | I |
| Implementation Plan | C | R | A | I | C | C | C | - | - | - | - |
| Implementation | I | R | A | I | I | C | C | - | - | - | I |
| Testing | I | R | A | I | C | C | C | C | C | - | - |
| Client Notification | I | R | I | I | I | - | - | - | I | A | R |
| PIR | C | R | A | C | C | C | C | C | C | C | I |
| Close CR | I | R/A | C | I | C | - | - | - | - | - | - |
| Maintain Change Log | I | R/A | I | I | I | - | - | - | - | - | - |
| Report KPIs | I | R | I | I | A | - | - | - | - | - | - |

### 16.2 Role Descriptions

| Role | Responsibilities |
|------|-----------------|
| **Requestor** | Identifies need for change; completes CR form; provides technical details and justification; supports impact assessment; participates in implementation and testing as needed |
| **Change Coordinator** | Manages CR lifecycle; triages incoming CRs; coordinates assessments and approvals; facilitates CAB meetings; tracks implementation progress; maintains Change Log; produces metrics reports |
| **Technical Lead** | Leads impact and risk assessment for their domain; designs implementation approach; oversees implementation execution; ensures testing adequacy; approves Minor changes in their area |
| **CAB Chairperson** | Chairs CAB meetings; ensures all perspectives are heard; facilitates consensus; exercises casting vote if needed; approves Emergency changes; accountable for overall change control effectiveness |
| **QA Director** | Reviews compliance impact of all Standard and Emergency changes; approves changes affecting validated state or GxP compliance; can escalate or veto on compliance grounds; oversees change control KPIs |
| **Security Lead (CISO)** | Assesses security impact of all changes; approves security-related changes; ensures security controls remain effective post-change; approves security Emergency changes |
| **DevOps Lead** | Assesses infrastructure feasibility and risk; plans and executes infrastructure changes; maintains deployment tooling; manages maintenance windows; approves infrastructure Emergency changes (in absence of CAB Chair) |
| **Clinical Validation Lead** | Assesses impact on clinical accuracy and SLM performance; designs clinician validation protocols for model changes; verifies F1 performance thresholds post-change |
| **Regulatory Affairs Lead** | Assesses regulatory compliance impact; evaluates impact on BRAT/CIOMS XII, eCTD Module 2.5, and PBRER outputs; advises on regulatory notification requirements |
| **Product Owner** | Assesses client impact; prioritizes client-requested changes; approves client notifications; ensures client acknowledgement for High-impact changes; co-approves Minor changes with client impact |
| **Client (Designated Contact)** | Receives change notifications; provides feedback on proposed changes; acknowledges High-impact changes; reports post-change issues; requests changes through Client Success Manager |

### 16.3 Delegation and Absence

| Primary Role | Delegate | Delegation Conditions |
|-------------|----------|----------------------|
| CAB Chairperson | QA Director | Written delegation; valid for up to 10 business days |
| QA Director | Senior QA Manager | Written delegation; valid for up to 10 business days; cannot delegate compliance veto authority |
| Change Coordinator | Backup Change Coordinator | Automatic delegation during planned absence; handover notes required |
| Technical Lead | Senior Engineer in the same domain | Written delegation; valid for up to 10 business days |
| CISO | Senior Security Engineer | Written delegation; valid for up to 5 business days for Emergency approvals only |

### 16.4 Training Requirements

| Role | Required Training | Frequency |
|------|------------------|-----------|
| All roles | Change Control SOP (this document) | Upon assignment + annual refresher |
| Change Coordinator | Advanced Change Management (ITIL 4 or equivalent) | Upon assignment; certification maintained |
| CAB Members | GAMP 5 Change Control module | Upon assignment + annual refresher |
| Technical Leads | Risk Assessment methodology | Upon assignment + biennial refresher |
| QA Director | Regulatory compliance updates (21 CFR Part 11, EU Annex 11) | Annual |
| All implementers | Deployment procedures and back-out execution | Upon assignment + annual refresher |

---

## Appendix A: Change Request Form Template

```
===================================================================
CHANGE REQUEST FORM
===================================================================

CR ID:          [Auto-assigned: CR-YYYY-NNNN]
Date:           [Auto-populated]
Requestor:      ________________________
Department:     ________________________
Priority:       [ ] Critical  [ ] High  [ ] Medium  [ ] Low

-------------------------------------------------------------------
1. CHANGE DESCRIPTION
-------------------------------------------------------------------
Current State:

Proposed Change:

Justification:

-------------------------------------------------------------------
2. AFFECTED COMPONENTS
-------------------------------------------------------------------
[ ] SLM Module(s): _____________________________________________
[ ] Ontology: __________________________________________________
[ ] Infrastructure: ____________________________________________
[ ] API Layer: _________________________________________________
[ ] Security Controls: _________________________________________
[ ] Regulatory Alignment: ______________________________________
[ ] Documentation: _____________________________________________
[ ] Third-Party Components: ____________________________________

-------------------------------------------------------------------
3. PROPOSED CLASSIFICATION
-------------------------------------------------------------------
Category:       [ ] Emergency  [ ] Standard  [ ] Minor
Risk Level:     [ ] Critical   [ ] High  [ ] Medium  [ ] Low

-------------------------------------------------------------------
4. PROPOSED TIMELINE
-------------------------------------------------------------------
Requested Implementation Date: _______________
Change Freeze Conflicts:       [ ] None  [ ] Yes: _______________

-------------------------------------------------------------------
5. DEPENDENCIES
-------------------------------------------------------------------
Related CRs:           ________________________________________
External Dependencies: ________________________________________

-------------------------------------------------------------------
6. ATTACHMENTS
-------------------------------------------------------------------
[ ] Design Document
[ ] Test Plan
[ ] Impact Assessment (pre-filled)
[ ] Risk Assessment (pre-filled)
[ ] Other: _____________________________________________________

===================================================================
FOR CHANGE COORDINATOR USE ONLY
===================================================================
Classification Confirmed:  [ ] Emergency  [ ] Standard  [ ] Minor
Assigned Assessor(s):      ________________________________________
Approval Workflow:         ________________________________________
Target CAB Date:           ________________________________________
===================================================================
```

---

## Appendix B: Post-Implementation Review Form Template

```
===================================================================
POST-IMPLEMENTATION REVIEW
===================================================================

CR ID:              ________________________
CR Title:           ________________________
Implementation Date: ________________________
Review Date:        ________________________
Reviewer:           ________________________

-------------------------------------------------------------------
1. IMPLEMENTATION OUTCOME
-------------------------------------------------------------------
[ ] Implemented as planned
[ ] Implemented with deviations (describe below)
[ ] Back-out triggered (describe below)
[ ] Partially implemented (describe below)

Deviations / Issues:


-------------------------------------------------------------------
2. VERIFICATION RESULTS
-------------------------------------------------------------------
Post-implementation checks:     [ ] All Pass  [ ] Failures (detail below)
SLM performance thresholds:     [ ] Met       [ ] Not Met (detail below)
Audit trail integrity:          [ ] Verified  [ ] Issues (detail below)
ALCOA+ compliance:              [ ] Confirmed [ ] Issues (detail below)
Data integrity:                 [ ] Confirmed [ ] Issues (detail below)

Details:


-------------------------------------------------------------------
3. CLIENT IMPACT
-------------------------------------------------------------------
Client issues reported:         [ ] None  [ ] Yes (detail below)
Client deliverables verified:   [ ] Yes   [ ] N/A
Client notifications sent:      [ ] Yes   [ ] N/A
Client acknowledgements:        [ ] Yes   [ ] N/A  [ ] Pending

Details:


-------------------------------------------------------------------
4. COMPLIANCE
-------------------------------------------------------------------
GAMP 5 validated state:         [ ] Maintained  [ ] Re-validation required
21 CFR Part 11:                 [ ] Maintained  [ ] Issues (detail below)
EU Annex 11:                    [ ] Maintained  [ ] Issues (detail below)
EU data residency:              [ ] Maintained  [ ] Issues (detail below)

Details:


-------------------------------------------------------------------
5. DOCUMENTATION
-------------------------------------------------------------------
[ ] All CR documentation complete
[ ] SOPs updated
[ ] System documentation updated
[ ] Training materials updated
[ ] Validation documentation updated
[ ] Change Log updated

-------------------------------------------------------------------
6. LESSONS LEARNED
-------------------------------------------------------------------
What went well:

What could be improved:

Follow-up actions:

-------------------------------------------------------------------
7. SIGN-OFF
-------------------------------------------------------------------
Reviewer:               ________________  Date: ________________
Technical Lead:         ________________  Date: ________________
QA Representative:      ________________  Date: ________________

Outcome: [ ] Closed - Successful
         [ ] Closed - Successful with Issues
         [ ] Closed - Failed
         [ ] Open - Partial (follow-up CR: _______________)

===================================================================
```

---

### Amendment Log

| Version | Date | Author | Description of Change | Approved By |
|---------|------|--------|-----------------------|-------------|
| 1.0 | 2026-03-25 | ArcaScience Quality Assurance | Initial release | [Name, Title] |
| | | | | |
| | | | | |

---

*End of Document - ARC-SOP-CC-2026-001 v1.0*
