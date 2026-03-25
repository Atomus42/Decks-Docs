# Standard Operating Procedure - Incident and Deviation Management

**Document ID:** SOP-INC-DEV-2026-001
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
5. [Incident Classification Matrix](#5-incident-classification-matrix)
6. [Incident Detection and Reporting](#6-incident-detection-and-reporting)
7. [Initial Assessment and Triage](#7-initial-assessment-and-triage)
8. [Investigation Procedure](#8-investigation-procedure)
9. [Containment Actions](#9-containment-actions)
10. [CAPA Procedure](#10-capa-procedure)
11. [Impact Assessment on Validated State](#11-impact-assessment-on-validated-state)
12. [Client Notification Requirements](#12-client-notification-requirements)
13. [Regulatory Notification Requirements](#13-regulatory-notification-requirements)
14. [Incident Resolution and Closure](#14-incident-resolution-and-closure)
15. [Post-Incident Review](#15-post-incident-review)
16. [Deviation Trending and Metrics](#16-deviation-trending-and-metrics)
17. [Escalation Matrix](#17-escalation-matrix)
18. [Roles and Responsibilities](#18-roles-and-responsibilities)
19. [Appendix A - Incident Report Template](#appendix-a---incident-report-template)
20. [Appendix B - CAPA Form Template](#appendix-b---capa-form-template)
21. [Appendix C - Quick Reference Flowchart](#appendix-c---quick-reference-flowchart)
22. [Revision History](#revision-history)

---

## 1. Purpose

This SOP establishes the procedures for detecting, reporting, classifying, investigating, resolving, and preventing recurrence of incidents and deviations affecting the ArcaScience Benefit-Risk Assessment (BRA) platform. It ensures that:

- Every incident or deviation is captured, classified, and resolved in a documented, traceable manner
- Data integrity (ALCOA+) is maintained or restored following any incident
- The validated state of the GAMP 5 Category 5 platform is assessed and preserved
- Root cause analysis is conducted with appropriate rigor based on incident severity
- Corrective and Preventive Actions (CAPAs) are implemented and verified for effectiveness
- Client notification obligations are met within contractually defined timelines
- Regulatory notification obligations are assessed and fulfilled where applicable
- Trends are monitored to identify systemic issues before they escalate
- Compliance with FDA 21 CFR Part 11, EU Annex 11, and GAMP 5 requirements is maintained throughout the incident lifecycle

**Regulatory Basis:** ICH Q10 (Pharmaceutical Quality System), FDA 21 CFR Part 11, EU GMP Annex 11, GAMP 5 Category 5 validation lifecycle, ICH Q9 (Quality Risk Management).

---

## 2. Scope

### 2.1 In Scope

- All incidents and deviations affecting the BRA platform, its 24 SLMs, 6 output types, and supporting infrastructure
- Infrastructure components: Apache Airflow, S3, ElasticSearch, DocumentDB, QDrant, FastAPI, NestJS
- Data integrity events affecting ALCOA+ compliance
- Extraction accuracy events (F1 score deviations)
- Ontology-related events (MedDRA, SNOMED CT, ChEBI, Disease Ontology)
- Regulatory output quality events (eCTD Module 2.5, PBRER, BRAT/CIOMS XII)
- Access control and electronic signature events (21 CFR Part 11)
- Audit trail events
- Performance and availability events
- Client-facing delivery events
- Near-miss events (conditions that could have resulted in an incident but did not)

### 2.2 Out of Scope

- General IT helpdesk requests (password resets, software installation) - covered under IT support procedures
- Planned changes to the platform - covered under Change Control SOP
- Non-platform business incidents (HR, finance) - covered under corporate policies
- Client-side incidents in client-owned systems (e.g., Sanofi ARTEMIS issues not caused by BRA platform)

---

## 3. Definitions

| Term | Definition |
|------|-----------|
| **Incident** | Any unplanned event that disrupts or has the potential to disrupt the normal operation of the BRA platform, its outputs, or its compliance state |
| **Deviation** | A departure from an approved procedure, specification, standard, or expected result. In this SOP, deviations are treated as a subset of incidents requiring investigation |
| **Near-Miss** | An event or condition that did not result in an incident but, under slightly different circumstances, could have. Near-misses are reported and tracked to enable preventive action |
| **CAPA** | Corrective and Preventive Action - a systematic approach to identifying, investigating, and resolving issues (corrective) and preventing their recurrence or occurrence of similar issues (preventive) |
| **Root Cause** | The fundamental underlying reason for an incident or deviation, as opposed to symptoms or contributing factors |
| **Critical Incident** | An incident that directly affects data integrity, regulatory output accuracy, or system availability during client delivery. Requires immediate containment and escalation to Head of Quality within 1 hour |
| **Major Incident** | An incident that affects platform performance, audit compliance, or quality metrics without immediate impact on client deliverables. Requires escalation to QA Lead within 4 hours |
| **Minor Incident** | An incident with limited operational impact that does not affect data integrity, regulatory outputs, or client deliverables. Requires documentation within 24 hours |
| **Containment Action** | An immediate action taken to limit the impact of an incident before the root cause is identified and permanent correction is implemented |
| **Corrective Action** | An action taken to eliminate the root cause of an existing incident or deviation |
| **Preventive Action** | An action taken to eliminate the cause of a potential incident or deviation that has not yet occurred |
| **Validated State** | The documented condition in which the BRA platform operates within its qualified parameters as established during GAMP 5 Category 5 IQ/OQ/PQ |
| **Impact Assessment** | A documented evaluation of how an incident affects the validated state, data integrity, regulatory compliance, and client deliverables |
| **5-Why Analysis** | A root cause analysis technique that iteratively asks "Why?" to drill down from symptoms to root cause |
| **Ishikawa Diagram** | A cause-and-effect diagram (also called fishbone diagram) used to systematically identify potential root causes across categories (People, Process, Technology, Data, Environment, Measurement) |
| **Fault Tree Analysis** | A top-down, deductive analysis technique that maps the logical combinations of events leading to an undesired outcome |
| **ALCOA+** | Attributable, Legible, Contemporaneous, Original, Accurate, Complete, Consistent, Enduring, Available |
| **SLA** | Service Level Agreement - contractually defined performance and availability commitments |

---

## 4. References

| Reference | Description |
|-----------|-------------|
| ICH Q10 | Pharmaceutical Quality System |
| ICH Q9 | Quality Risk Management |
| FDA 21 CFR Part 11 | Electronic Records; Electronic Signatures |
| EU Annex 11 | Computerised Systems |
| GAMP 5 (2nd Edition) | A Risk-Based Approach to Compliant GxP Computerized Systems |
| SOP-TRAIN-COMP-2026-001 | Training and Competency Management |
| SOP-SANOFI-DEMO-2026-001 | Sanofi Demo Instance Setup & Configuration |
| SOP-CHG-CTRL-2026 | Change Control |
| SOP-VAL-2026 | Platform Validation Master Plan |
| SOP-ITSEC-2026 | IT Security and Access Control |

---

## 5. Incident Classification Matrix

### 5.1 Classification Levels

Every incident must be classified into one of three severity levels based on its actual or potential impact. Classification determines response timelines, investigation rigor, escalation requirements, and notification obligations.

### 5.2 Critical Incidents

**Definition:** Incidents that directly compromise data integrity, regulatory output accuracy, or system availability during active client delivery.

| Category | Examples | Impact Characteristics |
|----------|---------|----------------------|
| Data Integrity Breach | Unauthorized modification of platform data; audit trail tampering or gap; loss of data traceability; ALCOA+ violation affecting released output | Regulatory output may contain incorrect or unverifiable data; client and regulatory trust compromised |
| Extraction Error Affecting Regulatory Output | SLM produces incorrect extraction that propagates to released BRA, AE Report, or other regulatory output; ontology miscoding affecting regulatory submission data | Released output contains factual errors that could affect regulatory decisions |
| System Outage During Client Delivery | Platform unavailable during scheduled client demo or deliverable handoff; data loss during client engagement; client-facing environment corrupted | Direct client relationship impact; SLA breach; potential contractual consequences |
| Access Control Failure - Unauthorized Access | Unauthorized user gains access to platform or client data; privilege escalation; compromised credentials used to access regulated data | 21 CFR Part 11 non-compliance; potential data breach; client confidentiality compromised |
| Electronic Signature Failure | Electronic signature mechanism compromised; signatures applied without proper authentication; signature records corrupted | 21 CFR Part 11 non-compliance; regulatory validity of signed records in question |

**Response Requirements:**
- Detection to initial report: Immediate (within 15 minutes)
- Escalation to Head of Quality: Within 1 hour
- Containment action initiated: Within 2 hours
- Client notification (if applicable): Within 4 hours
- Root cause investigation initiated: Within 24 hours
- Investigation completion target: 5 business days
- CAPA plan due: 10 business days from incident report

### 5.3 Major Incidents

**Definition:** Incidents that affect platform performance, quality metrics, or audit compliance without immediate direct impact on released client deliverables.

| Category | Examples | Impact Characteristics |
|----------|---------|----------------------|
| F1 Score Below Threshold | SLM extraction F1 score drops below defined threshold (< 0.85 for critical modules, < 0.80 for non-critical); systematic extraction quality degradation | Output quality degraded but not yet released to client; risk of undetected errors in future outputs |
| Audit Trail Gap | Missing audit log entries for non-critical operations; audit trail timestamp inconsistency; log storage failure for historical data | ALCOA+ partial non-compliance; audit readiness compromised; may not affect currently released data |
| Access Control Failure - Configuration | RBAC misconfiguration granting excessive privileges; delayed user deprovisioning; access review overdue | 21 CFR Part 11 compliance risk; potential for unauthorized actions (none confirmed) |
| Validation Protocol Deviation | IQ/OQ/PQ test step fails; validation documentation incomplete; traceability matrix gap discovered | GAMP 5 Category 5 validated state uncertain; requires reassessment |
| Pipeline Failure - Non-Client-Facing | Airflow DAG failure in non-production environment; data ingestion error in staging; scheduled job missed | Operational disruption; may delay deliverables if not resolved promptly |
| Ontology Mapping Error (Pre-Release) | MedDRA, SNOMED CT, ChEBI, or Disease Ontology mapping error discovered during review before output release | Error caught before client impact; indicates process gap in verification |
| Backup/Recovery Failure | Backup job failure; recovery test reveals data gap; DR drill fails to meet RTO/RPO | Business continuity risk; data durability concern |

**Response Requirements:**
- Detection to initial report: Within 4 hours
- Escalation to QA Lead: Within 4 hours
- Containment action initiated: Within 8 hours
- Client notification: Only if deliverable timeline affected
- Root cause investigation initiated: Within 48 hours
- Investigation completion target: 10 business days
- CAPA plan due: 20 business days from incident report

### 5.4 Minor Incidents

**Definition:** Incidents with limited operational impact that do not affect data integrity, regulatory outputs, or client deliverables.

| Category | Examples | Impact Characteristics |
|----------|---------|----------------------|
| UI Rendering Issue | Display formatting error; chart rendering glitch; CSS/layout issue in non-critical view | Visual only; no data impact; user workaround available |
| Non-Critical Performance Degradation | Slower-than-expected query response; temporary resource spike; non-SLA-affecting latency | User experience impacted; no data or accuracy impact |
| Documentation Gap | SOP section outdated; training material references superseded version; non-critical procedure undocumented | Administrative gap; no direct operational impact |
| Non-Critical Job Delay | Scheduled non-critical report delayed; monitoring dashboard temporarily unavailable | Operational inconvenience; no quality or compliance impact |
| Minor Configuration Drift | Non-critical setting differs from documented standard; cosmetic environment difference | Low risk; should be corrected during next maintenance window |

**Response Requirements:**
- Detection to initial report: Within 24 hours
- Escalation: QA Lead informed at next daily standup
- Containment: If needed, within next maintenance window
- Client notification: Not required
- Root cause analysis: Simplified (5-Why sufficient)
- Investigation completion target: 20 business days
- CAPA: Only if pattern of similar minor incidents identified (3+ in 90 days)

### 5.5 Classification Decision Matrix

Use the following decision tree when the appropriate classification is not immediately clear:

| Question | If Yes | If No |
|----------|--------|-------|
| Does the incident affect data in a released or client-facing output? | Critical | Continue |
| Is the platform unavailable during a scheduled client engagement? | Critical | Continue |
| Has unauthorized access to regulated data occurred or is confirmed? | Critical | Continue |
| Does the incident affect F1 scores, audit trails, or validation status? | Major | Continue |
| Could the incident affect a future client deliverable if not resolved? | Major | Continue |
| Does the incident require a change to a validated component? | Major | Continue |
| Is the impact limited to visual, performance, or administrative areas? | Minor | Re-evaluate with QA Lead |

**Important:** When in doubt, classify at the higher severity level. Reclassification downward is permitted after initial assessment with QA Lead approval and documented rationale.

---

## 6. Incident Detection and Reporting

### 6.1 Detection Methods

Incidents may be detected through any of the following channels:

| Detection Channel | Examples | Primary Detector |
|------------------|---------|-----------------|
| Automated Monitoring | Airflow DAG failure alert; ElasticSearch health check; S3 access anomaly; system performance threshold breach | DevOps monitoring system |
| F1 Score Monitoring | Automated F1 score calculation falls below threshold; extraction quality dashboard alert | ML Engineer monitoring dashboard |
| Audit Trail Monitoring | Audit log gap detection; timestamp anomaly alert; access pattern anomaly | QA automated checks |
| Manual Review | QA review identifies output error; Regulatory SME identifies mapping issue; Medical/Clinical review identifies extraction inaccuracy | Any team member during quality review |
| Client Report | Client identifies error in delivered output; client reports platform issue; client raises concern during demo | Demo Lead or Regulatory SME (client contact) |
| Security Monitoring | Access control alert; authentication failure pattern; data exfiltration detection | DevOps / IT Security |
| Self-Report | Team member identifies own error; team member notices anomaly during routine work | Any team member |

### 6.2 Reporting Procedure - Step by Step

**Step 1: Immediate Verbal Notification (Critical incidents only)**

- For Critical incidents: Immediately notify QA Lead and Head of Quality by phone/Teams/Slack
- Do not wait for written report completion before verbal notification
- State: What happened, when, what is the current impact, what immediate containment you have taken (if any)

**Step 2: Complete Incident Report Form**

- Open Incident Report Form (Appendix A) or equivalent electronic form in the quality system
- Complete all fields in Section 1 (Reporter Information) and Section 2 (Incident Description)
- Assign initial classification (Critical / Major / Minor) based on Section 5 of this SOP
- Assign a unique Incident ID using the format: INC-[YYYY]-[Sequential 4-digit number] (e.g., INC-2026-0001)

**Step 3: Submit to QA Lead**

- Submit the completed initial report to QA Lead via the quality management system
- For Critical incidents: Submit within 15 minutes of detection (form may be partially complete; update within 4 hours)
- For Major incidents: Submit within 4 hours of detection
- For Minor incidents: Submit within 24 hours of detection

**Step 4: Acknowledge Receipt**

- QA Lead (or designee) acknowledges receipt and confirms or adjusts classification within:
  - Critical: 30 minutes of submission
  - Major: 4 hours of submission
  - Minor: Next business day

**Step 5: Assign Investigation Owner**

- QA Lead assigns an Investigation Owner based on the incident category and affected system
- Investigation Owner is documented on the Incident Report Form
- Investigation Owner acknowledges assignment and confirms understanding of timeline requirements

### 6.3 Reporting Obligations

- **All personnel** are required to report incidents and near-misses. Failure to report a known or suspected incident is itself a deviation
- **No punitive action** will be taken against personnel who report incidents or near-misses in good faith. ArcaScience maintains a just culture that encourages reporting
- **Near-misses** are reported using the same form but classified as "Near-Miss" rather than Critical/Major/Minor. Near-misses are tracked for trending but do not require CAPA unless a pattern is identified
- **Anonymous reporting** is available via the quality system for situations where the reporter is uncomfortable with identified reporting. Anonymous reports receive the same investigation rigor

---

## 7. Initial Assessment and Triage

### 7.1 Triage Process

Upon receiving an incident report, the QA Lead (or designated triage officer) performs the following assessment within the timelines specified in Section 6.2, Step 4:

**Step 1: Verify and Confirm Classification**

- Review the reporter's initial classification against Section 5 classification criteria
- Confirm classification or reclassify with documented rationale
- If reclassified upward: immediately apply the higher-severity timeline requirements
- If reclassified downward: document rationale and notify reporter

**Step 2: Assess Immediate Risk**

| Risk Factor | Assessment Question | If Yes |
|------------|--------------------| ------|
| Data Integrity | Is any data currently compromised or at risk of compromise? | Initiate immediate containment |
| Client Impact | Is a client currently affected or will be affected within 24 hours? | Initiate client notification process |
| Regulatory Impact | Does this affect data used in or intended for regulatory submissions? | Notify Regulatory SME immediately |
| Ongoing Harm | Is the incident ongoing and causing continuing damage? | Initiate immediate containment |
| Scope Unknown | Is the full extent of the incident unclear? | Assign additional resources for rapid scoping |

**Step 3: Assign Resources**

| Classification | Investigation Owner | Supporting Resources | Executive Sponsor |
|---------------|--------------------|--------------------|-------------------|
| Critical | QA Lead (personally) or senior QA designee | Cross-functional team (minimum: affected role lead + DevOps + relevant SME) | Head of Quality |
| Major | QA Lead assigns from quality team | Affected role lead + one additional SME | QA Lead |
| Minor | QA Lead assigns (may be the reporter's manager) | As needed | None required |

**Step 4: Establish Investigation Timeline**

- Document investigation start date, target completion date, and interim milestone dates on the Incident Report Form
- For Critical incidents: Daily progress updates to Head of Quality
- For Major incidents: Progress updates every 3 business days to QA Lead
- For Minor incidents: Update at investigation completion

**Step 5: Open Incident Tracking Record**

- Create tracking record in quality management system
- Link to Incident Report Form
- Set status to "Under Investigation"
- Set up automated reminders for timeline milestones

---

## 8. Investigation Procedure

### 8.1 Investigation Approach by Classification

| Classification | Required Analysis Method | Minimum Investigation Depth | Documentation |
|---------------|------------------------|---------------------------|---------------|
| Critical | Ishikawa Diagram AND 5-Why Analysis; Fault Tree Analysis if systemic | Identify root cause, all contributing factors, and systemic implications | Full investigation report with evidence package |
| Major | 5-Why Analysis (minimum); Ishikawa if multiple factors suspected | Identify root cause and primary contributing factors | Investigation report with key evidence |
| Minor | 5-Why Analysis (simplified) | Identify root cause | Brief investigation summary on Incident Report Form |

### 8.2 Investigation Steps - Detailed Procedure

**Step 1: Secure Evidence (Within 2 hours of assignment for Critical; 24 hours for Major)**

- [ ] Capture system logs relevant to the incident timeframe
- [ ] Preserve audit trail records for the affected period
- [ ] Screenshot or export relevant dashboards, monitoring data, and alerts
- [ ] Identify and interview witnesses / personnel involved
- [ ] Document the system state at time of detection (configuration, version, environment)
- [ ] Preserve any affected data in its current state (do not modify until evidence is secured)
- [ ] Record the exact sequence of events leading to detection

**Step 2: Define the Problem Statement**

Document a precise problem statement answering:
- What happened? (Specific observation, not interpretation)
- When did it happen? (Exact date/time or range)
- Where did it happen? (System, module, environment, component)
- Who detected it? (Person, system, process)
- What is the actual impact? (Quantified where possible)
- What is the potential impact if not resolved?

**Step 3: 5-Why Analysis**

Perform iterative "Why?" questioning to drill from symptom to root cause:

| Level | Question | Answer | Evidence |
|-------|----------|--------|----------|
| Why 1 | Why did [problem statement] occur? | _________________ | _________________ |
| Why 2 | Why did [Answer 1] occur? | _________________ | _________________ |
| Why 3 | Why did [Answer 2] occur? | _________________ | _________________ |
| Why 4 | Why did [Answer 3] occur? | _________________ | _________________ |
| Why 5 | Why did [Answer 4] occur? | _________________ | _________________ |

**Rules for 5-Why Analysis:**
- Each "Why" must be answered with a factual, evidence-based statement
- Do not accept "human error" as a root cause - ask why the human error was possible
- Do not stop at fewer than 3 levels unless the root cause is clearly a one-time external event
- Continue beyond 5 levels if the root cause has not been reached
- Document the evidence supporting each answer

**Step 4: Ishikawa (Fishbone) Diagram (Critical and Major incidents)**

Analyze potential root causes across six categories:

| Category | Guiding Questions | Potential Causes Identified |
|----------|------------------|---------------------------|
| **People** | Was training adequate? Was the correct person assigned? Was workload manageable? Was there a communication failure? | _________________ |
| **Process** | Was the SOP followed? Is the SOP adequate? Was the review process effective? Were handoffs clear? | _________________ |
| **Technology** | Did the system perform as expected? Was there a software bug? Was there a configuration error? Were monitoring/alerts adequate? | _________________ |
| **Data** | Was the input data correct and complete? Was the ontology mapping accurate? Were source documents reliable? | _________________ |
| **Environment** | Was the correct environment used? Were there resource constraints? Were there external dependencies that failed? | _________________ |
| **Measurement** | Were metrics and thresholds appropriate? Were the monitoring tools functioning? Was the detection method adequate? | _________________ |

**Step 5: Fault Tree Analysis (Critical incidents with systemic implications)**

For Critical incidents where the Ishikawa analysis reveals multiple contributing factors or potential systemic issues:

1. Define the top-level undesired event (the incident)
2. Identify the immediate causal events (AND/OR gates)
3. Decompose each causal event into sub-causes
4. Continue decomposition until basic events (root causes) are identified
5. Document the fault tree diagram
6. Identify single points of failure and common cause failures

**Step 6: Determine Root Cause**

- Based on the analysis, state the root cause clearly and specifically
- Distinguish between root cause (what to fix permanently), contributing factors (what made it worse), and triggering event (what set it off)
- Verify the root cause: "If this cause is eliminated, would the incident be prevented?" If no, continue analysis
- Document the root cause determination with supporting evidence

**Step 7: Assess Scope and Recurrence Risk**

- Could this root cause affect other outputs, modules, or processes?
- Has this type of incident occurred before? (Check incident trending data)
- What is the likelihood of recurrence if no action is taken?
- Are there other systems or processes with similar vulnerability?

**Step 8: Document Investigation Findings**

- Complete the investigation section of the Incident Report Form (Appendix A)
- Attach all evidence (logs, screenshots, interview notes, analysis diagrams)
- Submit to QA Lead for review

### 8.3 Investigation Quality Review

- QA Lead reviews all investigation reports for adequacy
- For Critical incidents: Head of Quality must also approve the investigation
- Review criteria:
  - Is the problem statement clear and specific?
  - Is the root cause analysis thorough and evidence-based?
  - Is the root cause a genuine root cause (not a symptom)?
  - Have contributing factors been identified?
  - Has scope of impact been fully assessed?
  - Are the findings actionable (can specific CAPAs be designed)?
- If the investigation is inadequate, QA Lead returns it to the Investigation Owner with specific feedback and a revised deadline

---

## 9. Containment Actions

### 9.1 Purpose of Containment

Containment actions are immediate, temporary measures taken to prevent an incident from causing further harm while the root cause is investigated and permanent corrections are developed. Containment is not the final solution - it is a bridge to CAPA.

### 9.2 Containment Action Decision Matrix

| Incident Type | Potential Containment Actions | Decision Authority |
|--------------|------------------------------|-------------------|
| Data Integrity Breach | Quarantine affected data; restrict access to affected system; suspend affected output generation; enable enhanced audit logging | QA Lead (Critical: Head of Quality) |
| Extraction Error in Released Output | Issue hold notice on affected output; notify client of potential issue; prepare corrected output; review other outputs from same SLM | QA Lead + Regulatory SME |
| System Outage During Client Delivery | Activate backup environment; switch to pre-staged demo instance; communicate delay to client; engage DevOps for emergency restoration | Demo Lead + DevOps (escalate to Head of Operations) |
| F1 Score Below Threshold | Suspend deployment of affected SLM module; revert to last known good model version; flag outputs generated since last passing score for review | ML Engineer + QA Lead |
| Audit Trail Gap | Enable redundant logging; manually document affected period activities; restrict operations in affected area until logging restored | QA Lead + DevOps |
| Access Control Failure | Immediately revoke compromised access; force password reset for affected accounts; review access logs for unauthorized actions; enable enhanced monitoring | DevOps + QA Lead (Critical: Head of Quality) |
| Ontology Mapping Error | Suspend affected ontology mappings; revert to previous verified version; flag outputs using affected mappings for review | Medical/Clinical + QA Lead |
| Pipeline Failure | Restart failed pipeline with monitoring; switch to manual processing if urgent; implement additional checkpoints | Data Engineer + DevOps |

### 9.3 Containment Action Procedure

**Step 1:** Investigation Owner proposes containment action(s) within the timeline specified for the incident classification

**Step 2:** Decision authority reviews and approves the proposed containment

**Step 3:** Containment action is implemented and documented:
- What action was taken
- Who implemented it
- When it was implemented
- What is the expected effect
- What monitoring is in place to verify effectiveness
- When will containment be reviewed for continued need

**Step 4:** Verify containment effectiveness within:
- Critical: 4 hours of implementation
- Major: 24 hours of implementation
- Minor: Next business day

**Step 5:** If containment is ineffective, escalate immediately and implement alternative containment

**Step 6:** Containment remains in place until permanent CAPA is implemented and verified

### 9.4 Containment Documentation

All containment actions must be documented on the Incident Report Form, including:
- Containment action description
- Approval authority and date
- Implementation date and time
- Implementer name
- Effectiveness verification method and result
- Planned removal date (linked to CAPA implementation)

---

## 10. CAPA Procedure

### 10.1 CAPA Initiation

CAPAs are initiated for:
- All Critical incidents (mandatory)
- All Major incidents (mandatory)
- Minor incidents where a pattern is identified (3+ similar incidents in 90 days)
- Near-misses where the potential impact was Critical or Major
- Any incident where the QA Lead determines CAPA is warranted

### 10.2 CAPA Development - Step by Step

**Step 1: Define Corrective Action(s)**

Based on the investigation root cause:
- What specific change will eliminate the root cause?
- Who will implement the change?
- What is the implementation timeline?
- What resources are required?
- What is the success criterion?

| Corrective Action Element | Description |
|--------------------------|-------------|
| Action Description | Specific, measurable action to eliminate root cause |
| Responsible Person | Named individual accountable for implementation |
| Target Completion Date | Realistic date considering resource availability and change control |
| Resources Required | Personnel, tools, budget, time |
| Success Criteria | Measurable outcome that confirms the action is effective |
| Verification Method | How success will be measured (test, audit, review, monitoring) |

**Step 2: Define Preventive Action(s)**

Based on the scope assessment:
- What changes will prevent similar incidents in other areas?
- Are there systemic improvements needed (process, training, technology, monitoring)?
- Do other SOPs, training materials, or configurations need updating?

| Preventive Action Element | Description |
|--------------------------|-------------|
| Action Description | Specific action to prevent similar incidents elsewhere |
| Scope | Which systems, processes, or roles are affected |
| Responsible Person | Named individual accountable |
| Target Completion Date | Date |
| Success Criteria | How prevention will be verified |

**Step 3: Risk Assessment of CAPA**

Before implementing CAPA, assess the risk of the proposed changes:
- Could the corrective action introduce new risks?
- Does the change affect the validated state (see Section 11)?
- Does the change require change control approval?
- What is the rollback plan if the CAPA causes unintended effects?

**Step 4: CAPA Approval**

| Classification | Approval Authority |
|---------------|-------------------|
| Critical incident CAPA | Head of Quality + Head of Operations |
| Major incident CAPA | QA Lead |
| Minor incident CAPA | QA Lead |

**Step 5: CAPA Implementation**

- Implement corrective actions per the approved plan
- Document each implementation step with date, implementer, and evidence
- If implementation requires change control, follow SOP-CHG-CTRL-2026
- If implementation affects training requirements, update training matrix per SOP-TRAIN-COMP-2026-001

**Step 6: CAPA Effectiveness Verification**

- Verify effectiveness after a defined observation period:
  - Critical CAPA: 30-day effectiveness check + 90-day confirmation
  - Major CAPA: 60-day effectiveness check
  - Minor CAPA: 90-day effectiveness check
- Effectiveness is verified by the QA Lead (not the CAPA implementer)
- Verification methods include: repeat testing, monitoring data review, audit, process observation
- If CAPA is not effective, reopen the investigation and develop revised CAPA

### 10.3 CAPA Tracking

- All open CAPAs are tracked in the quality management system
- CAPA status is reviewed weekly by QA Lead
- Overdue CAPAs are escalated:
  - 1-7 days overdue: Reminder to responsible person
  - 8-14 days overdue: Escalation to responsible person's manager
  - 15+ days overdue: Escalation to Head of Quality
- CAPA metrics are reported monthly (see Section 16)

---

## 11. Impact Assessment on Validated State

### 11.1 When Required

A validated state impact assessment is mandatory for:
- All Critical incidents
- All Major incidents involving platform functionality, data processing, or infrastructure
- Any incident where a validated component (per the Validation Master Plan) is affected
- Any incident requiring a change to validated configuration, code, or infrastructure

### 11.2 Assessment Procedure

**Step 1: Identify Affected Validated Components**

Cross-reference the incident with the Validation Traceability Matrix to identify which IQ/OQ/PQ test cases cover the affected functionality.

| Component Category | Examples in BRA Platform |
|-------------------|------------------------|
| Data Ingestion | Airflow DAGs, S3 ingestion, source connectors |
| Data Storage | ElasticSearch indices, DocumentDB collections, QDrant vector stores |
| Processing | 24 SLM modules, extraction pipelines, ontology normalization |
| Output Generation | Disease Analysis, Clinical Landscape, Clinical Endpoint Study, AE Reports, BRA, BRA Summary |
| Audit Trail | Logging infrastructure, audit record storage, tamper-evidence mechanisms |
| Access Control | RBAC configuration, authentication, electronic signatures |
| User Interface | FastAPI endpoints, NestJS frontend, reporting views |

**Step 2: Determine Impact Level**

| Impact Level | Definition | Required Action |
|-------------|-----------|----------------|
| **No Impact** | Incident does not affect any validated component or its operation | Document assessment; no revalidation needed |
| **Potential Impact** | Incident may have affected a validated component but no evidence of actual impact | Targeted re-execution of relevant OQ/PQ test cases |
| **Confirmed Impact** | Incident has demonstrably affected a validated component's operation or output | Revalidation of affected component(s) per Validation Master Plan; may require full OQ/PQ re-execution |
| **Systemic Impact** | Incident reveals a fundamental issue with the validation approach or infrastructure | Full revalidation assessment; Validation Master Plan review; potential re-execution of complete IQ/OQ/PQ |

**Step 3: Execute Revalidation (if required)**

- Follow the Validation Master Plan (SOP-VAL-2026) for revalidation procedures
- Document the rationale for revalidation scope (why specific test cases were selected)
- Execute test cases and document results
- If revalidation fails, escalate immediately and expand scope

**Step 4: Document Assessment**

- Complete the Impact Assessment section of the Incident Report Form
- Attach revalidation results (if applicable)
- QA Lead signs off on the impact assessment
- For Critical incidents: Head of Quality also signs off

---

## 12. Client Notification Requirements

### 12.1 Notification Decision Matrix

| Criteria | Notification Required | Timeline | Method |
|----------|---------------------|----------|--------|
| Incident affects data in a delivered output | Yes - Mandatory | Within 4 hours of confirmation | Phone/video call + written follow-up |
| Incident affects scheduled deliverable timeline | Yes - Mandatory | Within 8 hours of determination | Email to client project manager |
| Incident affects demo instance availability | Yes - Mandatory | Within 4 hours of detection | Phone/video call to client contact |
| Incident affects data integrity of client data | Yes - Mandatory | Within 2 hours of confirmation | Phone/video call + written follow-up |
| F1 score below threshold for client deliverable | Yes - After assessment | Within 24 hours of assessment completion | Written report to client quality contact |
| Major incident with no client impact | No - Unless client requests | N/A | N/A |
| Minor incident | No | N/A | N/A |
| Near-miss | No - Unless client contract requires | Per contract | Per contract |

### 12.2 Notification Procedure

**Step 1: Prepare Notification Content**

The notification must include:
- Incident summary (what happened, when)
- Current status (contained, under investigation, resolved)
- Impact assessment (what client data/outputs are affected)
- Actions taken (containment, investigation in progress)
- Expected resolution timeline
- Next communication commitment (when the client will receive the next update)

The notification must NOT include:
- Speculation about root cause (before investigation is complete)
- Blame attribution
- Internal personnel names (unless client relationship requires it)
- Technical details beyond what is relevant to the client's understanding

**Step 2: Review and Approve Notification**

| Client | Notification Reviewer | Notification Approver |
|--------|----------------------|----------------------|
| Sanofi | Regulatory SME | Head of Operations |
| Other big pharma clients | Regulatory SME | Head of Operations |

**Step 3: Deliver Notification**

- Primary notification via phone/video call (for Critical incidents)
- Written confirmation via email within 2 hours of verbal notification
- All notifications documented in the incident record (date, time, recipient, content, delivery method)

**Step 4: Ongoing Communication**

- Provide updates at the committed frequency until incident is closed
- Final notification includes: root cause summary, CAPA summary, verification of data integrity, confirmation that validated state is restored

### 12.3 Sanofi-Specific Notification Requirements

For Sanofi engagements, the following additional requirements apply:

| Requirement | Detail |
|------------|--------|
| RAISE Framework Alignment | Notification must address which RAISE pillar(s) are affected and how compliance is being restored |
| Notification Recipients | Primary: Sanofi project manager; CC: Sanofi quality contact and Sanofi AI governance (if AI/SLM-related) |
| Language | Notifications in English; French translation provided within 24 hours if requested |
| Follow-Up Report | Formal written incident summary within 10 business days of closure, aligned to RAISE pillars |

---

## 13. Regulatory Notification Requirements

### 13.1 Assessment of Regulatory Notification Need

Most BRA platform incidents will NOT require direct regulatory notification, as ArcaScience is a platform/tool provider rather than a marketing authorization holder. However, the following situations require assessment:

| Situation | Assessment Required | Potential Notification |
|-----------|--------------------|-----------------------|
| Data integrity breach affecting data intended for regulatory submission | Yes - by Regulatory SME + QA Lead | Client (MAH) must assess their notification obligations; ArcaScience supports with evidence |
| Extraction error in output used in a filed regulatory document | Yes - by Regulatory SME + QA Lead | Client (MAH) must assess; may require amendment to submission |
| 21 CFR Part 11 non-compliance affecting signed electronic records | Yes - by QA Lead | May require notification to FDA if records are part of regulated submissions |
| EU Annex 11 non-compliance | Yes - by QA Lead | May require notification to relevant EU competent authority |
| Safety signal missed due to platform error | Yes - by Medical/Clinical + Regulatory SME + QA Lead | Client (MAH) has pharmacovigilance notification obligations; ArcaScience provides full support |

### 13.2 Regulatory Notification Procedure

1. Regulatory SME and QA Lead jointly assess whether the incident triggers regulatory notification obligations (for ArcaScience directly or for the client as MAH)
2. If client notification obligations are identified, notify client immediately per Section 12 with specific regulatory context
3. If ArcaScience direct notification obligations are identified, Head of Quality prepares the notification in consultation with legal counsel
4. All regulatory notifications require Head of Quality and legal counsel approval before submission
5. Document the regulatory assessment outcome regardless of whether notification is required

---

## 14. Incident Resolution and Closure

### 14.1 Resolution Criteria

An incident may be closed when ALL of the following criteria are met:

| Closure Criterion | Verification Method | Sign-Off |
|-------------------|--------------------| --------|
| Root cause identified and documented | Investigation report reviewed and approved | QA Lead |
| Containment action effective (or no longer needed) | Effectiveness verification documented | Investigation Owner |
| Corrective action implemented | Implementation evidence documented | CAPA Owner |
| Preventive action implemented (or scheduled with plan) | Implementation evidence or approved plan | CAPA Owner |
| Impact on validated state assessed and resolved | Impact assessment documented; revalidation completed if required | QA Lead |
| Client notified and satisfied (if applicable) | Client acknowledgment documented | Head of Operations |
| All affected data verified for integrity | ALCOA+ verification of affected data/outputs | QA Lead |
| Training updated (if CAPA requires) | Training material updated; affected personnel retrained | Training Coordinator |
| All documentation complete | Incident Report Form fully completed, all attachments present | QA Lead |

### 14.2 Closure Procedure

**Step 1:** Investigation Owner completes all sections of the Incident Report Form and attaches all evidence

**Step 2:** Investigation Owner requests closure by submitting the complete package to QA Lead

**Step 3:** QA Lead reviews the package against closure criteria (Section 14.1)

**Step 4:** If criteria not met, QA Lead returns to Investigation Owner with specific deficiencies

**Step 5:** If criteria met:
- For Critical incidents: Head of Quality reviews and approves closure
- For Major incidents: QA Lead approves closure
- For Minor incidents: QA Lead approves closure

**Step 6:** Quality management system status updated to "Closed"

**Step 7:** Closure notification sent to all stakeholders (internal; client if applicable)

### 14.3 Closure Timelines

| Classification | Target Closure | Maximum Allowable |
|---------------|---------------|-------------------|
| Critical | 15 business days | 30 business days (extension requires Head of Quality approval) |
| Major | 30 business days | 60 business days (extension requires QA Lead approval) |
| Minor | 45 business days | 90 business days (extension requires QA Lead approval) |

Note: These timelines include CAPA implementation but NOT effectiveness verification (which occurs post-closure per the CAPA plan).

---

## 15. Post-Incident Review

### 15.1 When Required

| Incident Type | Post-Incident Review Required |
|--------------|------------------------------|
| All Critical incidents | Mandatory - formal review meeting |
| Major incidents with systemic findings | Mandatory - formal review meeting |
| Major incidents without systemic findings | QA Lead determination |
| Minor incidents | Not required (trending analysis instead) |
| Recurring incidents (same root cause, 2+ occurrences) | Mandatory - formal review meeting |

### 15.2 Post-Incident Review Process

**Step 1: Schedule Review Meeting**

- Within 5 business days of incident closure
- Attendees: Investigation Owner, affected role leads, QA Lead, Head of Quality (Critical), relevant SMEs
- Duration: 60-90 minutes

**Step 2: Review Agenda**

| Agenda Item | Duration | Lead |
|-------------|----------|------|
| Incident summary and timeline | 10 minutes | Investigation Owner |
| Root cause analysis review | 15 minutes | Investigation Owner |
| Containment and CAPA effectiveness | 15 minutes | CAPA Owner |
| Impact assessment and revalidation results | 10 minutes | QA Lead |
| Lessons learned discussion | 20 minutes | All participants |
| Action items and systemic improvements | 15 minutes | QA Lead |

**Step 3: Document Lessons Learned**

For each lesson learned, document:
- What went well during the incident response
- What could have been done better
- What systemic changes would prevent similar incidents
- Are there other processes, systems, or roles that should be reviewed based on this incident
- Should any SOP, training material, or monitoring configuration be updated

**Step 4: Assign Follow-Up Actions**

- Each lesson learned with an actionable improvement is assigned an owner and deadline
- Follow-up actions are tracked in the quality management system
- QA Lead reviews follow-up action completion

**Step 5: Distribute Review Summary**

- Post-incident review summary is distributed to all team members (with appropriate detail level)
- Lessons learned are added to the organizational knowledge base
- Training materials are updated if applicable (per SOP-TRAIN-COMP-2026-001)

---

## 16. Deviation Trending and Metrics

### 16.1 Key Metrics

| Metric | Definition | Target | Review Frequency |
|--------|-----------|--------|-----------------|
| Total incidents per month | Count of all incidents reported, by classification | Trending downward or stable | Monthly |
| Mean time to detect (MTTD) | Average time from incident occurrence to detection | Critical < 1 hour; Major < 4 hours; Minor < 24 hours | Monthly |
| Mean time to contain (MTTC) | Average time from detection to effective containment | Critical < 2 hours; Major < 8 hours | Monthly |
| Mean time to resolve (MTTR) | Average time from report to closure | Critical < 15 days; Major < 30 days; Minor < 45 days | Monthly |
| CAPA on-time completion rate | Percentage of CAPAs completed by target date | >= 90% | Monthly |
| CAPA effectiveness rate | Percentage of CAPAs verified as effective at first check | >= 85% | Quarterly |
| Repeat incident rate | Percentage of incidents with same root cause as a prior incident | <= 5% | Quarterly |
| Near-miss reporting rate | Number of near-misses reported per month | Trending upward (indicates healthy reporting culture) | Monthly |
| Incidents by category | Distribution across Critical/Major/Minor | Major + Critical < 20% of total | Monthly |
| Incidents by root cause category | Distribution across People/Process/Technology/Data/Environment/Measurement | No single category > 40% | Quarterly |
| Client-reported incidents | Incidents first detected by client | <= 5% of total incidents | Quarterly |
| Overdue investigations | Number of investigations past target completion date | 0 | Weekly |
| Overdue CAPAs | Number of CAPAs past target completion date | 0 | Weekly |

### 16.2 Trending Analysis Process

1. **Monthly:** Training Coordinator compiles incident metrics and distributes to QA Lead and Head of Quality
2. **Monthly:** QA Lead reviews metrics for trends, spikes, and anomalies
3. **Quarterly:** QA Lead prepares trending analysis report including:
   - Trend charts for all key metrics
   - Root cause category analysis
   - Comparison to previous quarters
   - Identification of emerging patterns
   - Recommendations for systemic improvements
4. **Quarterly:** Management review meeting includes incident trending as a standing agenda item
5. **Annually:** Comprehensive incident trending review as part of management review, including:
   - Year-over-year comparison
   - Training effectiveness correlation (cross-reference SOP-TRAIN-COMP-2026-001 KPIs)
   - Client satisfaction correlation
   - Regulatory inspection readiness assessment

### 16.3 Trend-Triggered Actions

| Trend Identified | Trigger Threshold | Required Action |
|-----------------|-------------------|----------------|
| Increase in total incidents | > 20% increase month-over-month for 2 consecutive months | QA Lead initiates root cause review of the trend |
| Cluster of similar incidents | 3+ incidents with same root cause category in 90 days | Mandatory systemic investigation and preventive CAPA |
| CAPA effectiveness declining | Effectiveness rate drops below 80% for a quarter | CAPA process review and improvement initiative |
| Increase in client-reported incidents | Any increase over previous quarter | Detection and monitoring capability review |
| Repeat incident | Any incident with same root cause as closed incident | Reopen prior CAPA; escalate to Head of Quality |
| MTTD increasing | Average exceeds target for 2 consecutive months | Monitoring and alerting infrastructure review |

---

## 17. Escalation Matrix

### 17.1 Escalation Levels

| Level | Trigger | Escalated To | Timeline | Expected Action |
|-------|---------|-------------|----------|-----------------|
| **Level 1** | Incident reported | QA Lead | Per classification timeline | Triage, assign, track |
| **Level 2** | Critical incident reported OR investigation stalled OR containment ineffective | Head of Quality | Within 1 hour (Critical) or when triggered | Executive oversight, resource allocation, decision authority |
| **Level 3** | Client impact confirmed OR regulatory notification needed OR systemic issue identified | Head of Quality + Head of Operations | Within 2 hours of trigger | Cross-functional response, client communication, strategic decisions |
| **Level 4** | Data breach with legal implications OR regulatory enforcement action OR material contract breach | CEO / Legal Counsel | Immediately | Legal strategy, external communication, crisis management |

### 17.2 Escalation Contact Matrix

| Role | Primary Contact | Backup Contact | Contact Method |
|------|----------------|---------------|----------------|
| QA Lead | [Named individual] | [Named backup] | Phone, Teams, Email |
| Head of Quality | [Named individual] | QA Lead (for initial triage) | Phone, Teams, Email |
| Head of Operations | [Named individual] | [Named backup] | Phone, Teams, Email |
| DevOps On-Call | Rotating schedule (posted in Teams) | DevOps Lead | Phone, PagerDuty |
| Regulatory SME | [Named individual] | [Named backup] | Phone, Teams, Email |
| Medical/Clinical Lead | [Named individual] | [Named backup] | Phone, Teams, Email |
| Demo Lead | [Named individual] | [Named backup] | Phone, Teams, Email |
| Sanofi Client Contact | As defined in engagement agreement | [Backup contact] | Per engagement agreement |

### 17.3 After-Hours Escalation

- Critical incidents detected outside business hours are escalated immediately via phone
- DevOps on-call is available 24/7 for infrastructure-related Critical incidents
- QA Lead is available on-call for Critical incident triage
- Head of Quality is available for Critical incident escalation requiring executive decision
- After-hours response for Major and Minor incidents begins at the start of the next business day

---

## 18. Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Head of Quality** | Approve Critical incident closures; executive sponsor for Critical CAPAs; approve regulatory notifications; chair post-incident reviews for Critical incidents; approve investigation extensions; final authority on classification disputes; approve client notifications for Critical incidents |
| **Head of Operations** | Resource allocation for incident response; approve client notifications; escalation point for operational impact; authorize emergency changes; manage client relationship during incidents |
| **QA Lead** | Triage all incidents; assign Investigation Owners; review and approve all investigations; approve Major/Minor closures; track CAPA progress; compile trending metrics; conduct quarterly trending analysis; approve reclassifications; lead post-incident reviews for Major incidents; audit incident process annually |
| **Investigation Owner (assigned per incident)** | Lead the investigation; secure evidence; conduct root cause analysis; propose containment and CAPA; document all findings; present at post-incident review; track CAPA implementation to completion |
| **CAPA Owner (may be same as Investigation Owner)** | Implement approved corrective and preventive actions; document implementation evidence; support effectiveness verification; report progress to QA Lead |
| **DevOps** | Monitor infrastructure; detect and report infrastructure incidents; implement infrastructure containment actions; provide system logs and evidence; support investigation with technical data; implement infrastructure CAPAs; maintain on-call availability |
| **ML Engineer** | Monitor SLM performance; detect and report extraction quality incidents; investigate SLM-related root causes; implement model-related CAPAs; provide F1 score data and analysis |
| **Data Engineer** | Monitor data pipelines; detect and report data quality incidents; investigate data-related root causes; implement pipeline CAPAs; provide data quality evidence |
| **Regulatory SME** | Assess regulatory impact of incidents; evaluate regulatory notification needs; review client notifications for regulatory accuracy; support CAPA development for regulatory outputs; validate output corrections |
| **Medical/Clinical** | Assess clinical impact of extraction errors; evaluate ontology-related incidents; validate clinical accuracy of corrected outputs; support CAPA development for clinical content |
| **Demo Lead** | Report client-detected incidents; manage client communication during incidents affecting demos; implement containment for demo environment issues; coordinate with QA on client notification content |
| **All Personnel** | Report incidents and near-misses promptly; preserve evidence; cooperate with investigations; implement assigned CAPAs; participate in post-incident reviews when requested; complete incident-related training |

---

## Appendix A - Incident Report Template

### INCIDENT REPORT FORM

**Form ID:** IRF-2026-[Sequential Number]
**Controlled Document - Do Not Reproduce Without Authorization**

---

**Section 1: Reporter Information**

| Field | Entry |
|-------|-------|
| Incident ID | INC-________-________ |
| Reporter Name | _________________________ |
| Reporter Role | _________________________ |
| Report Date | _________________________ |
| Report Time | _________________________ |
| Detection Method | [ ] Automated Monitor [ ] Manual Review [ ] Client Report [ ] Self-Report [ ] Security Alert [ ] Other: ________ |

---

**Section 2: Incident Description**

| Field | Entry |
|-------|-------|
| Incident Date | _________________________ |
| Incident Time (or estimated range) | _________________________ |
| Incident Location (system/module/environment) | _________________________ |
| Initial Classification | [ ] Critical [ ] Major [ ] Minor [ ] Near-Miss |
| Incident Category | [ ] Data Integrity [ ] Extraction Error [ ] System Outage [ ] Access Control [ ] F1 Score [ ] Audit Trail [ ] Performance [ ] Ontology [ ] Pipeline [ ] UI [ ] Documentation [ ] Other: ________ |

**Incident Description (What happened? Be specific and factual):**

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

**Immediate Impact (What is affected right now?):**

___________________________________________________________________________

___________________________________________________________________________

**Potential Impact (What could be affected if not resolved?):**

___________________________________________________________________________

___________________________________________________________________________

**Affected BRA Platform Outputs (check all that apply):**

| Output | Affected? | Details |
|--------|-----------|---------|
| Disease Analysis | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| Clinical Landscape | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| Clinical Endpoint Study | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| AE Reports | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| BRA | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| BRA Summary | [ ] Yes [ ] No [ ] Unknown | _________________________ |

**Affected Infrastructure Components (check all that apply):**

| Component | Affected? | Details |
|-----------|-----------|---------|
| Apache Airflow | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| S3 | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| ElasticSearch | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| DocumentDB | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| QDrant | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| FastAPI | [ ] Yes [ ] No [ ] Unknown | _________________________ |
| NestJS | [ ] Yes [ ] No [ ] Unknown | _________________________ |

**Client Impact:**

| Field | Entry |
|-------|-------|
| Is a client currently affected? | [ ] Yes [ ] No [ ] Unknown |
| If yes, which client? | _________________________ |
| Is a deliverable at risk? | [ ] Yes [ ] No [ ] Unknown |
| Is a demo affected? | [ ] Yes [ ] No [ ] Unknown |

---

**Section 3: Classification Confirmation (QA Lead)**

| Field | Entry |
|-------|-------|
| QA Lead Name | _________________________ |
| Classification Confirmed | [ ] Critical [ ] Major [ ] Minor [ ] Near-Miss |
| Reclassified from Initial? | [ ] Yes (original: ________) [ ] No |
| Reclassification Rationale | _________________________ |
| Date/Time Confirmed | _________________________ |
| Investigation Owner Assigned | _________________________ |
| Investigation Target Completion | _________________________ |

---

**Section 4: Containment Actions**

| Action # | Containment Action Description | Approved By | Implemented By | Implementation Date/Time | Effectiveness Verified? | Verification Date |
|---------|-------------------------------|------------|---------------|------------------------|------------------------|-------------------|
| 1 | _________________________ | _________ | _________ | _________ | [ ] Yes [ ] No | _________ |
| 2 | _________________________ | _________ | _________ | _________ | [ ] Yes [ ] No | _________ |
| 3 | _________________________ | _________ | _________ | _________ | [ ] Yes [ ] No | _________ |

---

**Section 5: Investigation**

**Problem Statement:**

___________________________________________________________________________

___________________________________________________________________________

**5-Why Analysis:**

| Level | Question | Answer | Evidence Reference |
|-------|----------|--------|-------------------|
| Why 1 | _________________________ | _________________________ | _________________________ |
| Why 2 | _________________________ | _________________________ | _________________________ |
| Why 3 | _________________________ | _________________________ | _________________________ |
| Why 4 | _________________________ | _________________________ | _________________________ |
| Why 5 | _________________________ | _________________________ | _________________________ |

**Ishikawa Analysis (Critical/Major incidents):**

| Category | Potential Causes Identified | Confirmed/Eliminated |
|----------|---------------------------|---------------------|
| People | _________________________ | _________________________ |
| Process | _________________________ | _________________________ |
| Technology | _________________________ | _________________________ |
| Data | _________________________ | _________________________ |
| Environment | _________________________ | _________________________ |
| Measurement | _________________________ | _________________________ |

**Root Cause Determination:**

| Field | Entry |
|-------|-------|
| Root Cause | _________________________ |
| Contributing Factor(s) | _________________________ |
| Triggering Event | _________________________ |
| Root Cause Verification ("If eliminated, would incident be prevented?") | [ ] Yes [ ] No (if No, continue analysis) |

**Scope Assessment:**

| Field | Entry |
|-------|-------|
| Could this affect other outputs/modules? | [ ] Yes [ ] No - Detail: _________________________ |
| Has this occurred before? | [ ] Yes (Incident ID: ________) [ ] No |
| Recurrence likelihood (without action) | [ ] High [ ] Medium [ ] Low |
| Similar vulnerabilities elsewhere? | [ ] Yes [ ] No - Detail: _________________________ |

---

**Section 6: Impact Assessment on Validated State**

| Field | Entry |
|-------|-------|
| Validated components affected | _________________________ |
| Impact level | [ ] No Impact [ ] Potential Impact [ ] Confirmed Impact [ ] Systemic Impact |
| Revalidation required? | [ ] Yes [ ] No |
| Revalidation scope | _________________________ |
| Revalidation completed? | [ ] Yes (Date: ________) [ ] No [ ] N/A |
| Revalidation result | [ ] Pass [ ] Fail [ ] N/A |

---

**Section 7: Client Notification**

| Field | Entry |
|-------|-------|
| Client notification required? | [ ] Yes [ ] No |
| Client name | _________________________ |
| Notification method | [ ] Phone [ ] Video Call [ ] Email [ ] Written Report |
| Notification date/time | _________________________ |
| Notified by | _________________________ |
| Client recipient | _________________________ |
| Client acknowledgment received? | [ ] Yes (Date: ________) [ ] No [ ] Pending |
| Follow-up communications (dates) | _________________________ |

---

**Section 8: Regulatory Notification**

| Field | Entry |
|-------|-------|
| Regulatory notification assessment completed? | [ ] Yes [ ] No [ ] N/A |
| Assessed by | _________________________ |
| Regulatory notification required? | [ ] Yes [ ] No |
| If yes - authority | _________________________ |
| If yes - notification date | _________________________ |
| If yes - reference number | _________________________ |

---

**Section 9: CAPA Reference**

| Field | Entry |
|-------|-------|
| CAPA required? | [ ] Yes [ ] No |
| CAPA Form ID | CAP-________-________ |
| CAPA Owner | _________________________ |
| CAPA Target Completion | _________________________ |

---

**Section 10: Closure**

| Closure Criterion | Met? | Evidence |
|-------------------|------|----------|
| Root cause identified and documented | [ ] Yes [ ] No | _________________________ |
| Containment effective or removed | [ ] Yes [ ] No [ ] N/A | _________________________ |
| Corrective action implemented | [ ] Yes [ ] No [ ] N/A | _________________________ |
| Preventive action implemented or planned | [ ] Yes [ ] No [ ] N/A | _________________________ |
| Validated state assessed and resolved | [ ] Yes [ ] No | _________________________ |
| Client notified and satisfied | [ ] Yes [ ] No [ ] N/A | _________________________ |
| Data integrity verified (ALCOA+) | [ ] Yes [ ] No | _________________________ |
| Training updated (if required) | [ ] Yes [ ] No [ ] N/A | _________________________ |
| Documentation complete | [ ] Yes [ ] No | _________________________ |

---

**Section 11: Signatures**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Investigation Owner | _____________ | _____________ | _____________ |
| QA Lead | _____________ | _____________ | _____________ |
| Head of Quality (Critical only) | _____________ | _____________ | _____________ |
| Head of Operations (if client affected) | _____________ | _____________ | _____________ |

---

**Section 12: Attachments Checklist**

| Attachment | Included? |
|------------|----------|
| System logs | [ ] Yes [ ] No [ ] N/A |
| Audit trail records | [ ] Yes [ ] No [ ] N/A |
| Screenshots / exports | [ ] Yes [ ] No [ ] N/A |
| Witness / interview notes | [ ] Yes [ ] No [ ] N/A |
| Ishikawa diagram | [ ] Yes [ ] No [ ] N/A |
| Fault tree diagram | [ ] Yes [ ] No [ ] N/A |
| Revalidation results | [ ] Yes [ ] No [ ] N/A |
| Client notification copies | [ ] Yes [ ] No [ ] N/A |
| CAPA form | [ ] Yes [ ] No [ ] N/A |
| Other: _________________________ | [ ] Yes |

---

## Appendix B - CAPA Form Template

### CORRECTIVE AND PREVENTIVE ACTION (CAPA) FORM

**Form ID:** CAP-2026-[Sequential Number]
**Controlled Document - Do Not Reproduce Without Authorization**

---

**Section 1: CAPA Identification**

| Field | Entry |
|-------|-------|
| CAPA ID | CAP-________-________ |
| Related Incident ID | INC-________-________ |
| Incident Classification | [ ] Critical [ ] Major [ ] Minor |
| CAPA Initiation Date | _________________________ |
| CAPA Owner | _________________________ |
| CAPA Due Date | _________________________ |

---

**Section 2: Problem Summary**

| Field | Entry |
|-------|-------|
| Root Cause (from investigation) | _________________________ |
| Contributing Factors | _________________________ |
| Scope of Impact | _________________________ |

---

**Section 3: Corrective Actions**

| CA # | Action Description | Responsible Person | Target Date | Resources Required | Success Criteria | Status |
|------|-------------------|-------------------|-------------|-------------------|-----------------|--------|
| CA-1 | _________________________ | _________ | _________ | _________ | _________________________ | [ ] Planned [ ] In Progress [ ] Completed [ ] Verified |
| CA-2 | _________________________ | _________ | _________ | _________ | _________________________ | [ ] Planned [ ] In Progress [ ] Completed [ ] Verified |
| CA-3 | _________________________ | _________ | _________ | _________ | _________________________ | [ ] Planned [ ] In Progress [ ] Completed [ ] Verified |

**Corrective Action Implementation Evidence:**

| CA # | Implementation Date | Implemented By | Evidence Description | Evidence Attached? |
|------|--------------------| --------------|---------------------|-------------------|
| CA-1 | _________ | _________ | _________________________ | [ ] Yes |
| CA-2 | _________ | _________ | _________________________ | [ ] Yes |
| CA-3 | _________ | _________ | _________________________ | [ ] Yes |

---

**Section 4: Preventive Actions**

| PA # | Action Description | Scope (systems/processes affected) | Responsible Person | Target Date | Success Criteria | Status |
|------|-------------------|-----------------------------------|-------------------|-------------|-----------------|--------|
| PA-1 | _________________________ | _________________________ | _________ | _________ | _________________________ | [ ] Planned [ ] In Progress [ ] Completed [ ] Verified |
| PA-2 | _________________________ | _________________________ | _________ | _________ | _________________________ | [ ] Planned [ ] In Progress [ ] Completed [ ] Verified |
| PA-3 | _________________________ | _________________________ | _________ | _________ | _________________________ | [ ] Planned [ ] In Progress [ ] Completed [ ] Verified |

**Preventive Action Implementation Evidence:**

| PA # | Implementation Date | Implemented By | Evidence Description | Evidence Attached? |
|------|--------------------| --------------|---------------------|-------------------|
| PA-1 | _________ | _________ | _________________________ | [ ] Yes |
| PA-2 | _________ | _________ | _________________________ | [ ] Yes |
| PA-3 | _________ | _________ | _________________________ | [ ] Yes |

---

**Section 5: Risk Assessment of CAPA**

| Question | Response |
|----------|----------|
| Could the corrective/preventive actions introduce new risks? | [ ] Yes [ ] No - If yes: _________________________ |
| Does any action affect the validated state? | [ ] Yes [ ] No - If yes: _________________________ |
| Is change control required? | [ ] Yes (Change ID: ________) [ ] No |
| Are training updates required? | [ ] Yes [ ] No - If yes: _________________________ |
| What is the rollback plan if actions cause unintended effects? | _________________________ |

---

**Section 6: CAPA Approval**

| Role | Name | Approved? | Signature | Date |
|------|------|-----------|-----------|------|
| CAPA Owner | _________ | [ ] Yes [ ] No | _________ | _________ |
| QA Lead | _________ | [ ] Yes [ ] No | _________ | _________ |
| Head of Quality (Critical CAPAs) | _________ | [ ] Yes [ ] No | _________ | _________ |
| Head of Operations (Critical CAPAs) | _________ | [ ] Yes [ ] No | _________ | _________ |

---

**Section 7: Effectiveness Verification**

| Verification Check | Scheduled Date | Actual Date | Verification Method | Result | Verified By |
|-------------------|----------------|-------------|--------------------| -------|------------|
| First effectiveness check | _________ | _________ | _________________________ | [ ] Effective [ ] Not Effective | _________ |
| Confirmation check (Critical only) | _________ | _________ | _________________________ | [ ] Effective [ ] Not Effective | _________ |

**Effectiveness Verification Details:**

| Field | Entry |
|-------|-------|
| Has the root cause been eliminated? | [ ] Yes [ ] No |
| Have similar incidents occurred since CAPA implementation? | [ ] Yes (Incident ID: ________) [ ] No |
| Are metrics within acceptable range? | [ ] Yes [ ] No - Detail: _________________________ |
| Is the CAPA sustainable long-term? | [ ] Yes [ ] No - Detail: _________________________ |

**If CAPA Not Effective:**

| Field | Entry |
|-------|-------|
| Reason for ineffectiveness | _________________________ |
| Revised CAPA plan | _________________________ |
| Revised CAPA ID (if new CAPA opened) | CAP-________-________ |

---

**Section 8: CAPA Closure**

| Field | Entry |
|-------|-------|
| All corrective actions implemented and verified? | [ ] Yes [ ] No |
| All preventive actions implemented and verified? | [ ] Yes [ ] No |
| Effectiveness verified? | [ ] Yes [ ] No |
| Training completed (if required)? | [ ] Yes [ ] No [ ] N/A |
| Change control completed (if required)? | [ ] Yes [ ] No [ ] N/A |
| Documentation complete? | [ ] Yes [ ] No |
| CAPA Status | [ ] CLOSED - EFFECTIVE [ ] CLOSED - REPLACED BY CAP-________ [ ] OPEN |

---

**Section 9: Closure Signatures**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CAPA Owner | _____________ | _____________ | _____________ |
| QA Lead | _____________ | _____________ | _____________ |
| Head of Quality (Critical CAPAs) | _____________ | _____________ | _____________ |

---

## Appendix C - Quick Reference Flowchart

### Incident Management Process Flow

```
DETECTION
    |
    v
Is this an incident or near-miss?
    |                    |
    v                    v
  Incident            Near-Miss
    |                    |
    v                    v
Complete IRF         Complete IRF
Sections 1-2         (mark Near-Miss)
    |                    |
    v                    v
Submit to            Submit to
QA Lead              QA Lead
    |                    |
    v                    v
TRIAGE               Track for
(QA Lead)            trending
    |
    v
Classify: Critical / Major / Minor
    |
    +---> Critical: Verbal notify Head of Quality within 1 hour
    |     Contain within 2 hours
    |     Investigate within 24 hours
    |     Client notify within 4 hours (if applicable)
    |
    +---> Major: Notify QA Lead within 4 hours
    |     Contain within 8 hours
    |     Investigate within 48 hours
    |
    +---> Minor: Document within 24 hours
          Investigate within 20 business days
    |
    v
INVESTIGATION
    |
    v
Secure evidence
    |
    v
Define problem statement
    |
    v
5-Why Analysis (all) + Ishikawa (Critical/Major) + Fault Tree (Critical systemic)
    |
    v
Determine root cause
    |
    v
Assess scope and recurrence risk
    |
    v
QA Lead reviews investigation
    |
    v
IMPACT ASSESSMENT
    |
    v
Assess validated state impact
    |
    v
Revalidate if required
    |
    v
CAPA
    |
    v
Develop corrective actions
    |
    v
Develop preventive actions
    |
    v
Risk assess CAPA
    |
    v
Approve CAPA
    |
    v
Implement CAPA
    |
    v
CLOSURE
    |
    v
Verify all closure criteria met
    |
    v
QA Lead / Head of Quality approves closure
    |
    v
POST-INCIDENT REVIEW (Critical + systemic Major)
    |
    v
Document lessons learned
    |
    v
Update training / SOPs / monitoring as needed
    |
    v
EFFECTIVENESS VERIFICATION
    |
    v
30/60/90 day check per classification
    |
    v
Confirm CAPA effective - COMPLETE
    or
Reopen and revise CAPA - return to CAPA step
```

---

## Revision History

| Version | Date | Author | Change Description | Approved By |
|---------|------|--------|-------------------|-------------|
| 1.0 | 2026-03-25 | ArcaScience Quality Assurance | Initial release | Head of Quality / Head of Operations |

---

**END OF DOCUMENT**

*This document is the property of ArcaScience. Unauthorized reproduction or distribution is prohibited. This is a controlled document - verify current version before use.*
