# Standard Operating Procedure: Periodic Review and Continuous Improvement

| Field | Value |
|---|---|
| **Document ID** | ARCA-SOP-PRCI-2026-001 |
| **Version** | 1.0 |
| **Effective Date** | 2026-03-25 |
| **Review Date** | 2027-03-25 |
| **Classification** | Confidential |
| **Author** | ArcaScience Quality Assurance Team |
| **Approved By** | Head of Quality Assurance / VP Engineering |
| **Applicable Platform** | BRA (Benefit-Risk Assessment) Platform |
| **Regulatory Scope** | FDA 21 CFR Part 11, EU Annex 11, GAMP 5 Category 5, ICH Q10 |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Definitions](#2-definitions)
3. [Review Schedule](#3-review-schedule)
4. [Platform Performance Review](#4-platform-performance-review)
5. [Quality Metrics Review](#5-quality-metrics-review)
6. [Regulatory Compliance Review](#6-regulatory-compliance-review)
7. [Data Integrity Review](#7-data-integrity-review)
8. [Change Management Review](#8-change-management-review)
9. [Risk Register Review and Update](#9-risk-register-review-and-update)
10. [Training Effectiveness Review](#10-training-effectiveness-review)
11. [Improvement Action Tracking](#11-improvement-action-tracking)
12. [Management Review Meeting Procedure](#12-management-review-meeting-procedure)
13. [Review Report Template](#13-review-report-template)
14. [Approval Signatures](#14-approval-signatures)
15. [Revision History](#15-revision-history)

---

## 1. Purpose and Scope

### 1.1 Purpose

This SOP establishes the procedures for conducting periodic reviews of the ArcaScience BRA platform and its associated quality management system, and for driving continuous improvement across all operational, technical, and compliance domains.

The BRA platform - with its 24 clinician-trained SLMs, GAMP 5 Category 5 validated infrastructure, and ALCOA+ compliant data integrity framework - requires systematic, evidence-based review to ensure it continues to meet the evolving needs of big pharma clients, maintains regulatory compliance, and delivers measurable improvements in performance and quality over time.

This SOP aligns with ICH Q10 Pharmaceutical Quality System principles for management review and continual improvement.

### 1.2 Scope

This procedure applies to:

- All BRA platform components: Data Forge (Apache Airflow DAGs), S3 storage (raw + enriched), ElasticSearch, DocumentDB, QDrant vector DB, FastAPI (Python), NestJS (Node.js)
- All 24 SLM models and their performance characteristics
- All six output types: Disease Analysis, Clinical Landscape, Clinical Endpoint Study, AE Reports, BRA, BRA Summary
- Ontology services: MedDRA v27.0, SNOMED CT, ChEBI normalization
- Cryptographic hash chain audit trail infrastructure
- Quality management system processes (CAPA, deviations, change control, training)
- Client engagement delivery and satisfaction
- All personnel (14 FTEs current, scaling to 47+ under BR-PREDICT program)
- BRAT/CIOMS XII framework implementation

### 1.3 Responsibilities

| Role | Responsibility |
|---|---|
| **Head of Quality Assurance** | Overall ownership of this SOP; chairs management review meetings; ensures reviews are conducted on schedule |
| **VP Engineering** | Co-chairs management review; responsible for technical performance and infrastructure metrics |
| **ML Engineering Lead** | Provides SLM performance data, model trending analysis, and model improvement recommendations |
| **Data Engineering Lead** | Provides pipeline throughput, latency, and data quality metrics |
| **Infrastructure Lead** | Provides system availability, uptime, and infrastructure performance metrics |
| **Client Engagement Lead** | Provides client satisfaction data, engagement delivery metrics, and client feedback |
| **Security Lead** | Provides security incident data, vulnerability assessment results, and compliance status |
| **All Team Leads** | Contribute to review data collection, attend management reviews, and own assigned improvement actions |

---

## 2. Definitions

| Term | Definition |
|---|---|
| **Periodic Review** | A structured, scheduled evaluation of platform performance, quality metrics, regulatory compliance, and operational effectiveness conducted at defined intervals. |
| **KPI (Key Performance Indicator)** | A quantifiable measure used to evaluate the success of the BRA platform in meeting its objectives. KPIs are tracked over time to identify trends. |
| **Trend Analysis** | The practice of collecting data over time and analyzing it for patterns, anomalies, or directional changes that indicate improvement, degradation, or emerging risks. |
| **Management Review** | A formal meeting where senior leadership reviews the performance of the quality management system and BRA platform to ensure continuing suitability, adequacy, and effectiveness. Aligned with ICH Q10 requirements. |
| **CAPA (Corrective and Preventive Action)** | A systematic approach to investigating, understanding, and correcting discrepancies while attempting to prevent their recurrence. |
| **Deviation** | A departure from an approved procedure, specification, or expected result that requires documentation, investigation, and potential corrective action. |
| **Validated State** | The condition in which the BRA platform operates within its qualified and documented specifications, with evidence that it consistently produces results meeting predetermined criteria. |
| **BRAT Framework** | Benefit-Risk Action Team framework used by the BRA platform for structuring benefit-risk assessments. |
| **CIOMS XII** | Council for International Organizations of Medical Sciences Working Group XII framework for benefit-risk assessment of medicines. |
| **F1 Score** | The harmonic mean of precision and recall, used as a primary metric for evaluating SLM model performance. |
| **ALCOA+** | Data integrity framework: Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, Available. |

---

## 3. Review Schedule

### 3.1 Scheduled Reviews

| Review Type | Frequency | Timing | Duration | Attendees | Output |
|---|---|---|---|---|---|
| **Quarterly Operational Review** | Every 3 months | Weeks 1 - 2 of Jan, Apr, Jul, Oct | Half day (4 hours) | All team leads, Head of QA, VP Engineering | Quarterly Review Report |
| **Annual System Review** | Once per year | March (aligned with fiscal/regulatory calendar) | Full day (8 hours) | Senior leadership, all team leads, external QA auditor (optional) | Annual Review Report |
| **Management Review Meeting** | Semi-annual | June and December | 3 hours | VP Engineering, Head of QA, CEO, all team leads | Management Review Minutes |

### 3.2 Triggered Reviews

A triggered review must be initiated within 10 business days when any of the following events occur:

| Trigger Event | Review Scope | Initiated By |
|---|---|---|
| Critical incident or disaster recovery activation | Incident root cause, recovery effectiveness, process gaps | Head of QA |
| Regulatory finding (audit or inspection) | Affected processes, compliance gaps, corrective actions | Head of QA |
| SLM model F1 score drops below threshold (AE < 92%, NLP < 94%) for any module | Model performance, training data quality, root cause | ML Engineering Lead |
| Client complaint or dissatisfaction (formal) | Engagement delivery, output quality, communication | Client Engagement Lead |
| Major platform change (new module, infrastructure migration, ontology update) | Change impact, validated state, integration testing | VP Engineering |
| Cybersecurity incident | Security posture, vulnerability assessment, access controls | Security Lead |
| Significant personnel change (loss of key person, major team restructuring) | Knowledge continuity, cross-training gaps, process coverage | Head of QA |
| Regulatory guidance change (new ICH guideline, FDA/EMA guidance update) | Compliance gap analysis, required platform changes | Head of QA |

### 3.3 Review Calendar Template (Annual)

| Month | Scheduled Activity |
|---|---|
| **January** | Q4 Quarterly Operational Review; Annual planning for review activities |
| **February** | Data collection for Annual System Review |
| **March** | Annual System Review (full day) |
| **April** | Q1 Quarterly Operational Review |
| **May** | Improvement action progress review |
| **June** | Management Review Meeting (semi-annual) |
| **July** | Q2 Quarterly Operational Review |
| **August** | Mid-year improvement action progress review |
| **September** | Preparation for external audit readiness |
| **October** | Q3 Quarterly Operational Review |
| **November** | Data collection for Management Review |
| **December** | Management Review Meeting (semi-annual); Year-end metrics compilation |

---

## 4. Platform Performance Review

### 4.1 SLM Model Performance Trending

#### 4.1.1 Metrics to Track

| Metric | Baseline Target | Measurement Method | Frequency | Alert Threshold |
|---|---|---|---|---|
| **AE Extraction F1 Score** | >= 92% | Automated validation against gold-standard annotated dataset | Weekly per engagement; monthly aggregate | < 90% (warning); < 88% (critical) |
| **NLP F1 Score** | >= 94% | Automated validation against gold-standard annotated dataset | Weekly per engagement; monthly aggregate | < 92% (warning); < 90% (critical) |
| **Per-Module F1 Scores** (24 models) | Varies per module (see baseline table) | Module-specific test suites | Monthly | > 2% decline from baseline (warning); > 5% decline (critical) |
| **Precision per Module** | Varies per module | Automated validation | Monthly | > 3% decline from baseline |
| **Recall per Module** | Varies per module | Automated validation | Monthly | > 3% decline from baseline |
| **Confidence Score Distribution** | Per-module baseline distribution | Statistical analysis of output confidence scores | Monthly | Significant distribution shift (KS test p < 0.05) |
| **Clinician Agreement Rate** | >= 90% | Clinician review of random output samples | Quarterly | < 85% |

#### 4.1.2 Per-Module Trending Table Template

| SLM Module | Q1 F1 | Q2 F1 | Q3 F1 | Q4 F1 | Trend | Status | Action Required |
|---|---|---|---|---|---|---|---|
| Module 1: [Name] | ___% | ___% | ___% | ___% | [ ] Up [ ] Stable [ ] Down | [ ] Green [ ] Amber [ ] Red | |
| Module 2: [Name] | ___% | ___% | ___% | ___% | [ ] Up [ ] Stable [ ] Down | [ ] Green [ ] Amber [ ] Red | |
| ... (repeat for all 24 modules) | | | | | | | |

#### 4.1.3 Trending Analysis Procedure

1. Extract F1 scores for all 24 SLM models from the validation pipeline for the review period.
2. Plot trend lines for each module over the last 4 quarters (minimum).
3. Calculate moving averages and identify statistically significant trends.
4. For any module showing decline: initiate root cause analysis.
5. Compare cross-engagement performance to identify data-specific vs. model-specific issues.
6. Document findings in the Quarterly Review Report.
7. Propose retraining, fine-tuning, or architectural changes for declining models.

### 4.2 Extraction Accuracy Monitoring Across Engagements

| Metric | Measurement | Frequency |
|---|---|---|
| **Entity Extraction Accuracy** | Comparison of extracted entities to clinician-validated ground truth | Per engagement (sample basis) |
| **Relationship Extraction Accuracy** | Verification of extracted relationships between entities | Per engagement (sample basis) |
| **Ontology Mapping Accuracy** | Correct mapping to MedDRA v27.0, SNOMED CT, ChEBI codes | Per engagement |
| **Cross-Engagement Consistency** | Same entity/concept mapped identically across engagements | Quarterly |
| **False Positive Rate** | Incorrectly extracted entities per 1,000 records | Monthly |
| **False Negative Rate** | Missed entities per 1,000 records (estimated from spot-checks) | Monthly |

**Procedure:**
1. For each active engagement, select a random sample of processed records (minimum 5% or 50 records, whichever is greater).
2. Submit samples for clinician review (blinded to automated results).
3. Compare clinician annotations to automated extractions.
4. Calculate accuracy metrics and document in engagement quality log.
5. Aggregate across engagements for quarterly trending.
6. Investigate any engagement showing accuracy below the platform baseline.

### 4.3 Pipeline Throughput and Latency Metrics

| Metric | Target | Measurement Source | Frequency |
|---|---|---|---|
| **Data Forge Ingestion Rate** | Per-engagement SLA (documents/hour) | Airflow DAG metrics | Daily |
| **DAG Success Rate** | >= 99% | Airflow task success/failure counts | Daily |
| **Average DAG Execution Time** | Within SLA per DAG type | Airflow execution logs | Daily |
| **SLM Inference Latency (p50)** | < [X] seconds per document | FastAPI endpoint metrics | Daily |
| **SLM Inference Latency (p95)** | < [X] seconds per document | FastAPI endpoint metrics | Daily |
| **SLM Inference Latency (p99)** | < [X] seconds per document | FastAPI endpoint metrics | Daily |
| **End-to-End Processing Time** | Ingestion to output generation within engagement SLA | Pipeline orchestration metrics | Per engagement |
| **Queue Depth** | Trending toward zero (not growing) | Airflow queue metrics | Hourly |
| **Failed Task Retry Rate** | < 5% of total task executions | Airflow retry metrics | Weekly |

**Trending Procedure:**
1. Extract pipeline metrics from Airflow, CloudWatch, and application monitoring for the review period.
2. Plot throughput and latency trends over time.
3. Identify any degradation patterns correlated with data volume increases, infrastructure changes, or model updates.
4. Compare actual throughput to engagement SLAs.
5. Forecast capacity requirements for upcoming engagements and BR-PREDICT scaling.

### 4.4 System Availability and Uptime Metrics

| Metric | Target | Measurement Source | Frequency |
|---|---|---|---|
| **Overall Platform Availability** | >= 99.5% (excluding planned maintenance) | Synthetic monitoring + CloudWatch | Monthly |
| **S3 Availability** | >= 99.99% (AWS SLA) | AWS Health + S3 access monitoring | Monthly |
| **ElasticSearch Cluster Availability** | >= 99.5% | Cluster health monitoring | Monthly |
| **DocumentDB Availability** | >= 99.5% | DocumentDB CloudWatch metrics | Monthly |
| **QDrant Availability** | >= 99.5% | QDrant health endpoint monitoring | Monthly |
| **Airflow Scheduler Availability** | >= 99.5% | Airflow health monitoring | Monthly |
| **FastAPI Service Availability** | >= 99.5% | Health check endpoint monitoring | Monthly |
| **NestJS Service Availability** | >= 99.5% | Health check endpoint monitoring | Monthly |
| **Mean Time Between Failures (MTBF)** | Trending upward | Incident records | Quarterly |
| **Mean Time to Recovery (MTTR)** | Trending downward | Incident records | Quarterly |
| **Planned Downtime** | < 4 hours/month | Maintenance window records | Monthly |
| **Unplanned Downtime** | < 2 hours/month | Incident records | Monthly |

---

## 5. Quality Metrics Review

### 5.1 Incident and Deviation Trends

#### 5.1.1 Incident Metrics

| Metric | Tracking Method | Review Frequency |
|---|---|---|
| **Total Incidents (by severity)** | Incident management system | Monthly count; quarterly trend |
| **Incidents by Category** | Classification: Infrastructure, Pipeline, Model, Security, Data Integrity, Other | Quarterly distribution analysis |
| **Incidents by Root Cause** | Root cause categories: Human error, Software defect, Infrastructure failure, Configuration error, External dependency | Quarterly Pareto analysis |
| **Repeat Incidents** | Incidents with same root cause as previous incidents | Quarterly - indicates CAPA ineffectiveness |
| **Time to Detection** | Duration from incident occurrence to detection | Monthly average; quarterly trend |
| **Time to Resolution** | Duration from detection to resolution | Monthly average; quarterly trend |
| **Incidents Impacting Clients** | Count of incidents with client-visible impact | Monthly; zero target |

#### 5.1.2 Deviation Metrics

| Metric | Tracking Method | Review Frequency |
|---|---|---|
| **Total Deviations** | Deviation log | Monthly count; quarterly trend |
| **Deviations by Type** | Procedural, Data integrity, Validation, Output quality | Quarterly distribution |
| **Open Deviations (aging)** | Days open per deviation | Monthly - target: close within 30 days |
| **Deviations Leading to CAPA** | Percentage of deviations requiring CAPA | Quarterly |
| **Deviations by Process Area** | Ingestion, SLM pipeline, output generation, audit trail | Quarterly heat map |

#### 5.1.3 Trending Analysis Procedure

1. Extract incident and deviation data for the review period.
2. Create trend charts showing counts over time (minimum 4 quarters).
3. Perform Pareto analysis on root causes.
4. Identify any process areas with increasing incident/deviation rates.
5. Correlate spikes with platform changes, new engagements, or external events.
6. Document findings and proposed actions in review report.

### 5.2 CAPA Effectiveness

| Metric | Target | Measurement |
|---|---|---|
| **CAPA Initiated on Time** | 100% within 5 business days of root cause identification | Date comparison |
| **CAPA Completed on Time** | >= 90% within agreed timeframe | Completion date vs. target |
| **CAPA Effectiveness Rate** | >= 85% (no recurrence of root cause within 6 months) | Recurrence tracking |
| **Open CAPAs (aging)** | Zero CAPAs open > 90 days without documented justification | Aging report |
| **CAPA Verification Completed** | 100% of closed CAPAs have effectiveness verification | Verification records |

**Procedure:**
1. Review all CAPAs opened, completed, and verified during the review period.
2. For each closed CAPA, verify that the effectiveness check has been performed.
3. Identify any recurring issues that indicate CAPA ineffectiveness.
4. Review any overdue CAPAs and escalate if necessary.
5. Assess whether CAPA actions adequately address root causes.

### 5.3 Audit Finding Trends

| Metric | Tracking Method | Review Frequency |
|---|---|---|
| **Internal Audit Findings (by severity)** | Internal audit reports | Per audit; quarterly aggregate |
| **External Audit Findings** | Client audit reports, regulatory inspection reports | Per audit |
| **Finding Closure Rate** | Percentage of findings closed within agreed timeframe | Quarterly |
| **Repeat Findings** | Findings on same topic as previous audits | Per audit - indicates systemic issue |
| **Findings by Domain** | Data integrity, validation, documentation, security, process compliance | Annual distribution analysis |

### 5.4 Client Satisfaction Metrics

| Metric | Collection Method | Frequency | Target |
|---|---|---|---|
| **Deliverable Quality Score** | Client feedback survey (1-5 scale) | Per deliverable | >= 4.0 average |
| **On-Time Delivery Rate** | Delivery date vs. agreed timeline | Per deliverable | >= 95% |
| **Client Escalations** | Escalation log | Monthly count | Zero target |
| **Client NPS (Net Promoter Score)** | Annual client survey | Annual | >= 50 |
| **Repeat Engagement Rate** | Client renewal/expansion tracking | Annual | >= 80% |
| **Response Time to Client Queries** | Support ticket tracking | Monthly average | < 4 business hours |

**Procedure:**
1. Compile client satisfaction data from all active engagements.
2. Analyze trends across engagements and over time.
3. Identify any engagements with declining satisfaction.
4. Correlate satisfaction data with quality metrics (output accuracy, delivery timeliness).
5. Document specific client feedback themes and proposed responses.

---

## 6. Regulatory Compliance Review

### 6.1 Ontology Currency

| Ontology | Current Version | Latest Available Version | Status | Action Required |
|---|---|---|---|---|
| **MedDRA** | v27.0 | Check MSSO for latest | [ ] Current [ ] Update Available [ ] Update Required | |
| **SNOMED CT** | [Current version] | Check SNOMED International for latest | [ ] Current [ ] Update Available [ ] Update Required | |
| **ChEBI** | [Current version] | Check EBI for latest | [ ] Current [ ] Update Available [ ] Update Required | |

#### 6.1.1 Ontology Update Procedure

1. **Monitoring (Ongoing):** Designate a team member to monitor ontology provider release announcements.
2. **Impact Assessment (Within 5 business days of new release):**
   - Identify changes in the new ontology version (new terms, deprecated terms, hierarchy changes).
   - Assess impact on BRA platform mappings and existing engagement data.
   - Determine if update is required (regulatory mandate, client request, quality improvement) or optional.
3. **Update Planning (Within 10 business days if update required):**
   - Create change request per change management SOP.
   - Plan update deployment including regression testing.
   - Assess impact on validated state.
4. **Implementation:**
   - Deploy updated ontology to staging environment.
   - Execute regression test suite.
   - Verify mapping accuracy with new version.
   - Deploy to production per change management procedures.
5. **Post-Update Verification:**
   - Verify all active engagement data maps correctly with new ontology version.
   - Update platform documentation and version records.
   - Notify clients if mapping changes affect their engagement.

### 6.2 Regulatory Guidance Changes

#### 6.2.1 Monitoring Scope

| Regulatory Body | Guidance Areas to Monitor | Monitoring Frequency |
|---|---|---|
| **FDA** | 21 CFR Part 11 updates, computer system validation guidance, AI/ML guidance, benefit-risk assessment guidance | Monthly |
| **EMA** | Annex 11 updates, CHMP guidance, AI/ML regulatory framework, benefit-risk methodology guidance | Monthly |
| **ICH** | ICH Q8-Q12 updates, ICH E9(R1), ICH M4E(R2), new ICH guidelines relevant to BRA | Monthly |
| **ISPE** | GAMP 5 updates, data integrity guidance, cloud computing guidance | Quarterly |

#### 6.2.2 Regulatory Change Assessment Procedure

1. Identify new or revised regulatory guidance from monitoring activities.
2. Assess applicability to BRA platform operations.
3. If applicable, perform gap analysis between current practices and new requirements.
4. Classify impact: No action / Process update / Platform change / Revalidation required.
5. Create action items with timelines for any required changes.
6. Track implementation of regulatory changes to completion.
7. Document compliance assessment in regulatory compliance register.

### 6.3 Validation Status Review

| Component | Last Validation Date | Validation Type | Status | Next Review Date | Changes Since Validation |
|---|---|---|---|---|---|
| Data Forge Pipeline | _____________ | IQ/OQ/PQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| SLM Models (24) | _____________ | PQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| ElasticSearch | _____________ | IQ/OQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| DocumentDB | _____________ | IQ/OQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| QDrant Vector DB | _____________ | IQ/OQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| FastAPI Services | _____________ | OQ/PQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| NestJS Services | _____________ | OQ/PQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| Audit Trail System | _____________ | IQ/OQ/PQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| Ontology Services | _____________ | OQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |
| Output Generation | _____________ | PQ | [ ] Valid [ ] Review Needed [ ] Revalidation Required | _____________ | |

**Procedure:**
1. For each component, review all changes implemented since the last validation.
2. Assess whether changes are within the scope of existing validation or require revalidation.
3. Review any deviations or incidents that may affect validated state.
4. Confirm that validation documentation is current and accessible.
5. Schedule revalidation activities where required.

---

## 7. Data Integrity Review

### 7.1 Audit Trail Integrity Verification

#### 7.1.1 Automated Verification (Continuous)

| Check | Frequency | Method | Alert On |
|---|---|---|---|
| **Hash Chain Continuity** | Every new record insertion | Verify new record's hash links to previous record | Any chain break |
| **Hash Chain Full Verification** | Daily at 00:00 UTC | End-to-end chain verification from genesis to latest record | Any inconsistency |
| **Timestamp Monotonicity** | Every new record insertion | Verify timestamp is later than previous record | Out-of-order timestamp |
| **Record Completeness** | Every new record insertion | Verify all required fields are populated | Missing required field |
| **User Attribution** | Every new record insertion | Verify user identity is recorded and valid | Missing or invalid user |

#### 7.1.2 Manual Verification (Periodic)

| Check | Frequency | Procedure | Performed By |
|---|---|---|---|
| **Random Record Audit** | Monthly | Select 20 random audit trail records. Verify: attribution, timestamp accuracy, data completeness, hash integrity. | QA Analyst |
| **Cross-Reference Verification** | Quarterly | Select 10 platform actions. Trace from user action through all system logs to audit trail record. Verify consistency. | QA Lead |
| **Deletion/Modification Audit** | Monthly | Review all modification and deletion events in audit trail. Verify each has documented justification and appropriate authorization. | QA Lead |

### 7.2 ALCOA+ Compliance Spot-Checks

#### 7.2.1 Spot-Check Procedure

For each review period, select a random sample of records from active engagements (minimum 30 records across engagements) and evaluate against all ALCOA+ criteria:

| ALCOA+ Criterion | Verification Question | Check Method | Pass/Fail |
|---|---|---|---|
| **Attributable** | Can the record be traced to the person or system that created it? | Verify user ID, system identifier, and timestamp in audit trail | [ ] Pass [ ] Fail |
| **Legible** | Is the record readable and permanent? Can it be reproduced? | Visual inspection of stored records; verify rendering in output format | [ ] Pass [ ] Fail |
| **Contemporaneous** | Was the record created at the time the activity occurred? | Compare audit trail timestamp to expected processing window | [ ] Pass [ ] Fail |
| **Original** | Is this the original record or a certified true copy? | Verify record provenance; check for unauthorized copies or modifications | [ ] Pass [ ] Fail |
| **Accurate** | Does the record accurately reflect the observation or activity? | Compare extracted data to source document; verify against clinician review | [ ] Pass [ ] Fail |
| **Complete** | Is all required information present? No unexplained gaps? | Verify all mandatory fields populated; check for processing gaps | [ ] Pass [ ] Fail |
| **Consistent** | Is the record consistent across the data lifecycle? | Trace data from ingestion through processing to output; verify consistency | [ ] Pass [ ] Fail |
| **Enduring** | Is the record stored in a durable medium accessible throughout its retention period? | Verify storage durability (S3 durability, backup status, retention policy) | [ ] Pass [ ] Fail |
| **Available** | Can the record be retrieved when needed? | Attempt retrieval of historical records; verify access controls permit authorized access | [ ] Pass [ ] Fail |

#### 7.2.2 Spot-Check Results Tracking

| Review Period | Records Sampled | ALCOA+ Pass Rate | Findings | CAPA Required |
|---|---|---|---|---|
| Q1 20__ | _____ | ___% | | [ ] Yes [ ] No |
| Q2 20__ | _____ | ___% | | [ ] Yes [ ] No |
| Q3 20__ | _____ | ___% | | [ ] Yes [ ] No |
| Q4 20__ | _____ | ___% | | [ ] Yes [ ] No |

**Target:** 100% ALCOA+ compliance on spot-checked records.

### 7.3 Cryptographic Hash Chain Verification

#### 7.3.1 Verification Procedure

1. **Daily Automated Verification:**
   - The system automatically traverses the complete hash chain from genesis block to the latest record.
   - Each record's stored hash is recomputed from its contents and compared to the stored value.
   - Each record's "previous hash" pointer is verified against the actual hash of the preceding record.
   - Results are logged and any failure triggers an immediate alert to the QA team.

2. **Monthly Manual Verification:**
   - QA Analyst selects 50 random records distributed across the hash chain.
   - For each record: independently recompute the hash using the documented algorithm.
   - Verify the chain linkage for the selected records and their immediate neighbors.
   - Document verification results.

3. **Quarterly Full Chain Audit:**
   - Export the complete hash chain to an offline verification environment.
   - Run independent verification software (separate from production code) to validate the entire chain.
   - Compare chain length to expected record count.
   - Document results and file as controlled record.

#### 7.3.2 Hash Chain Incident Response

If a hash chain break or inconsistency is detected:

1. **Immediately** halt all platform write operations to preserve the chain state.
2. **Notify** Head of QA and VP Engineering within 15 minutes.
3. **Investigate** root cause: data corruption, software defect, unauthorized modification, or infrastructure issue.
4. **Document** the incident as a formal deviation.
5. **Assess** impact on data integrity and client deliverables.
6. **Remediate** based on root cause (restore from backup, correct software defect, etc.).
7. **Re-verify** the complete hash chain after remediation.
8. **Notify** affected clients if delivered data integrity is in question.
9. **Initiate** CAPA for the root cause.

---

## 8. Change Management Review

### 8.1 Changes Implemented Since Last Review

#### 8.1.1 Change Log Review Template

| Change ID | Date | Description | Category | Risk Level | Validated State Impact | Approval |
|---|---|---|---|---|---|---|
| CHG-____ | _________ | | [ ] Infrastructure [ ] Software [ ] Model [ ] Configuration [ ] Ontology [ ] Process | [ ] Low [ ] Medium [ ] High | [ ] No impact [ ] Within validation [ ] Revalidation required | [ ] Approved [ ] Pending |
| CHG-____ | _________ | | | | | |
| CHG-____ | _________ | | | | | |

#### 8.1.2 Change Summary Metrics

| Metric | Value | Trend |
|---|---|---|
| Total changes in review period | _____ | [ ] Increasing [ ] Stable [ ] Decreasing |
| Changes by category (breakdown) | Infrastructure: ___ Software: ___ Model: ___ Config: ___ Ontology: ___ Process: ___ | |
| Emergency changes | _____ | Target: < 10% of total |
| Changes requiring revalidation | _____ | |
| Failed changes (rolled back) | _____ | Target: < 5% |
| Change-related incidents | _____ | Target: zero |

### 8.2 Impact on Validated State

**Procedure:**
1. Review all changes implemented since the last periodic review.
2. For each change, verify that the change control process was followed correctly.
3. Confirm that validation impact assessments were performed where required.
4. Verify that any required revalidation activities have been completed.
5. Confirm that validation documentation has been updated to reflect changes.
6. Identify any changes that may have been implemented without proper change control.

**Assessment Checklist:**
- [ ] All changes have approved change requests
- [ ] Risk assessments completed for all changes
- [ ] Validation impact assessments completed where required
- [ ] Revalidation activities completed for impactful changes
- [ ] Regression testing performed and passed
- [ ] Validation documentation updated
- [ ] No unauthorized changes detected
- [ ] Rollback procedures documented for all changes

### 8.3 Effectiveness of Changes

| Change ID | Objective | Achieved | Evidence | Follow-Up |
|---|---|---|---|---|
| CHG-____ | | [ ] Yes [ ] Partial [ ] No | | |
| CHG-____ | | [ ] Yes [ ] Partial [ ] No | | |

**Procedure:**
1. For each significant change (medium/high risk), review whether the stated objective was achieved.
2. Collect evidence of effectiveness (metrics improvement, incident reduction, etc.).
3. For changes that did not achieve their objective, initiate investigation.
4. Document lessons learned for the change management process.

---

## 9. Risk Register Review and Update

### 9.1 Risk Register Review Procedure

1. **Retrieve** the current risk register for the BRA platform.
2. **Review each existing risk:**
   - Is the risk still relevant?
   - Has the likelihood changed?
   - Has the impact changed?
   - Are existing mitigations still effective?
   - Has the residual risk level changed?
3. **Identify new risks** arising from:
   - Incidents and deviations since the last review
   - Changes to the platform or infrastructure
   - New engagements or client requirements
   - Regulatory changes
   - Industry threat landscape changes
   - Personnel changes (especially with 14 to 47+ FTE scaling under BR-PREDICT)
4. **Retire risks** that are no longer applicable (with documented justification).
5. **Update risk scores** based on current assessment.
6. **Review risk mitigation actions** for completion and effectiveness.
7. **Prioritize** the updated risk register and identify top 10 risks.

### 9.2 Risk Register Template

| Risk ID | Description | Category | Likelihood (1-5) | Impact (1-5) | Risk Score | Existing Mitigations | Residual Risk | Mitigation Actions | Owner | Status | Last Review |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RSK-____ | | [ ] Technical [ ] Operational [ ] Regulatory [ ] Security [ ] Personnel | | | | | | | | [ ] Active [ ] Mitigated [ ] Retired | |

### 9.3 Risk Categories Specific to BRA Platform

| Category | Example Risks |
|---|---|
| **Model Risk** | SLM performance degradation, model drift, training data quality issues, adversarial inputs |
| **Data Risk** | Data corruption, ALCOA+ non-compliance, ontology mapping errors, hash chain breaks |
| **Infrastructure Risk** | Cloud service outages, capacity limitations, security vulnerabilities, DR readiness |
| **Regulatory Risk** | Guidance changes, audit findings, validation gaps, non-compliance exposure |
| **Engagement Risk** | Client dissatisfaction, deliverable quality issues, timeline overruns |
| **Personnel Risk** | Key person dependency, knowledge gaps, scaling challenges (14 to 47+ FTEs) |
| **Third-Party Risk** | Vendor service disruption, ontology provider changes, licensing issues |
| **Security Risk** | Cyber threats, data breach, unauthorized access, insider threat |

---

## 10. Training Effectiveness Review

### 10.1 Training Metrics

| Metric | Target | Measurement | Frequency |
|---|---|---|---|
| **Training Completion Rate** | 100% of required training completed on time | Training management system records | Monthly |
| **Training Assessment Pass Rate** | >= 90% first-attempt pass rate | Assessment scores | Per training event |
| **Time to Competency (New Hires)** | Within 90 days of start date | Manager assessment | Per new hire |
| **Recertification Compliance** | 100% recertified before expiration | Certification tracking | Monthly |
| **Training Hours per Employee** | >= 40 hours per year | Training records | Quarterly |

### 10.2 Training Effectiveness Assessment Procedure

1. **Review Training Records:**
   - Verify all team members have completed required training for their role.
   - Identify any overdue or expired certifications.
   - Review training assessment scores for trends.

2. **Competency Verification:**
   - Review on-the-job performance data linked to training topics.
   - Analyze incident and deviation data for training-related root causes.
   - Conduct manager interviews on team competency levels.

3. **Training Gap Analysis:**
   - Compare current role requirements to completed training.
   - Identify gaps created by platform changes, new features, or regulatory updates.
   - Identify gaps for the BR-PREDICT scaling (new roles, expanded responsibilities).

4. **Training Program Improvement:**
   - Review feedback from training participants.
   - Assess whether training content is current with platform version.
   - Propose updates to training curriculum based on findings.

### 10.3 Training Effectiveness Checklist

- [ ] All team members have completed required training
- [ ] No overdue certifications
- [ ] Assessment pass rates meet target
- [ ] No incidents attributed to training gaps in the review period
- [ ] Training content reviewed and current with platform version
- [ ] New hire onboarding program effectiveness assessed
- [ ] BR-PREDICT scaling training plan in place (47+ FTE target)
- [ ] Cross-training matrix reviewed and updated (minimum 2-person coverage per critical function)
- [ ] Training improvement actions documented and assigned

---

## 11. Improvement Action Tracking

### 11.1 Improvement Action Register

| Action ID | Source | Description | Priority | Owner | Target Date | Status | Completion Date | Effectiveness Verified |
|---|---|---|---|---|---|---|---|---|
| IMP-____ | [ ] Review [ ] CAPA [ ] Audit [ ] Client [ ] Other: ___ | | [ ] Critical [ ] High [ ] Medium [ ] Low | | | [ ] Open [ ] In Progress [ ] Completed [ ] Overdue [ ] Cancelled | | [ ] Yes [ ] No [ ] Pending |

### 11.2 Improvement Action Lifecycle

```
Identification --> Assessment --> Approval --> Implementation --> Verification --> Closure
      |                |              |              |                  |              |
   Source of       Impact and     Management    Execute per       Verify          Document
   improvement     resource       approval of   plan. Track       effectiveness   and close.
   (review,        assessment.    priority and  progress.         within defined  Update
   CAPA, audit,    Define         resources.                      timeframe.      metrics.
   client          success                      Update status
   feedback)       criteria.                    regularly.
```

### 11.3 Improvement Action Procedure

1. **Identification:** Log improvement action in register with source, description, and proposed benefit.
2. **Assessment:** Evaluate effort, resources required, and expected impact. Define success criteria.
3. **Prioritization:** Assign priority based on impact and urgency.
4. **Approval:** Obtain management approval for resource allocation.
5. **Implementation Planning:** Define steps, timeline, and responsible person.
6. **Execution:** Implement the improvement action per plan.
7. **Progress Tracking:** Report status at each quarterly review meeting.
8. **Verification:** After implementation, verify effectiveness against success criteria.
9. **Closure:** Document results and close action in register.

### 11.4 Improvement Action Metrics

| Metric | Target | Review Frequency |
|---|---|---|
| **Total Actions Open** | Trending downward (capacity-adjusted) | Quarterly |
| **Overdue Actions** | Zero overdue > 30 days beyond target date | Monthly |
| **Completion Rate** | >= 80% completed within target date | Quarterly |
| **Effectiveness Rate** | >= 85% of completed actions verified as effective | Quarterly |
| **Actions by Source** | Balanced distribution (not all reactive) | Annual |
| **Proactive vs. Reactive Ratio** | >= 40% proactive (from reviews, trend analysis) | Annual |

---

## 12. Management Review Meeting Procedure

### 12.1 Meeting Schedule and Logistics

| Attribute | Detail |
|---|---|
| **Frequency** | Semi-annual (June and December) with ad-hoc reviews as triggered |
| **Duration** | 3 hours |
| **Chair** | Head of Quality Assurance |
| **Co-Chair** | VP Engineering |
| **Required Attendees** | CEO, Head of QA, VP Engineering, all team leads |
| **Optional Attendees** | External QA consultant (for annual review) |
| **Minutes Recorded By** | QA Analyst (designated scribe) |
| **Minutes Distribution** | All attendees + controlled document repository within 5 business days |

### 12.2 Standing Agenda

| Agenda Item | Duration | Presenter | Input Required |
|---|---|---|---|
| 1. Review of previous meeting actions | 15 min | Head of QA | Previous meeting minutes and action tracker |
| 2. Platform performance summary (Section 4) | 30 min | VP Engineering + ML Engineering Lead | Performance dashboards and trending reports |
| 3. Quality metrics summary (Section 5) | 30 min | Head of QA | Incident, deviation, CAPA, and audit reports |
| 4. Regulatory compliance status (Section 6) | 20 min | Head of QA | Regulatory monitoring log, validation status register |
| 5. Data integrity review summary (Section 7) | 20 min | Head of QA | Audit trail verification reports, ALCOA+ spot-check results |
| 6. Change management summary (Section 8) | 15 min | VP Engineering | Change log, validation impact summary |
| 7. Risk register review (Section 9) | 15 min | Head of QA | Updated risk register |
| 8. Training effectiveness (Section 10) | 10 min | Head of QA | Training metrics report |
| 9. Improvement action status (Section 11) | 10 min | Head of QA | Improvement action register |
| 10. Client engagement update | 10 min | Client Engagement Lead | Client satisfaction data, engagement pipeline |
| 11. BR-PREDICT program update | 10 min | VP Engineering | Scaling progress, team growth, new capabilities |
| 12. New business and strategic items | 10 min | CEO | Strategic direction, market developments |
| 13. Actions and decisions summary | 5 min | Chair | Real-time capture during meeting |

### 12.3 Pre-Meeting Preparation

| Task | Responsible | Deadline |
|---|---|---|
| Compile performance metrics dashboard | VP Engineering + team leads | 10 business days before meeting |
| Compile quality metrics report | Head of QA | 10 business days before meeting |
| Update risk register | Head of QA | 7 business days before meeting |
| Update improvement action register | Head of QA | 7 business days before meeting |
| Distribute meeting package to all attendees | QA Analyst | 5 business days before meeting |
| Review meeting package | All attendees | Before meeting |

### 12.4 Meeting Output Requirements

Each management review meeting must produce:

1. **Meeting minutes** documenting all discussions, decisions, and actions.
2. **Updated action list** with owners, target dates, and priorities.
3. **Summary of decisions** on resource allocation, priority changes, or policy updates.
4. **Formal statement** on the continuing suitability, adequacy, and effectiveness of the quality management system.
5. **Identified improvement opportunities** for the next period.

### 12.5 Action Tracking from Management Review

| Action # | Description | Owner | Priority | Target Date | Status |
|---|---|---|---|---|---|
| MR-[YY]-[MM]-001 | | | [ ] Critical [ ] High [ ] Medium [ ] Low | | [ ] Open [ ] In Progress [ ] Completed |
| MR-[YY]-[MM]-002 | | | | | |

---

## 13. Review Report Template

### 13.1 Quarterly Operational Review Report

```
============================================================
QUARTERLY OPERATIONAL REVIEW REPORT
============================================================

Report Period: Q[X] 20[XX] ([Start Date] to [End Date])
Report Date: [Date]
Prepared By: [Name, Role]
Reviewed By: [Name, Role]

------------------------------------------------------------
1. EXECUTIVE SUMMARY
------------------------------------------------------------
[2-3 paragraph summary of key findings, trends, and
recommended actions for the quarter]

Overall Platform Health: [ ] GREEN  [ ] AMBER  [ ] RED

------------------------------------------------------------
2. PLATFORM PERFORMANCE
------------------------------------------------------------

2.1 SLM Model Performance
   - AE F1 Score (average): ___% (target: >= 92%)
   - NLP F1 Score (average): ___% (target: >= 94%)
   - Modules below threshold: [List or "None"]
   - Trend: [ ] Improving  [ ] Stable  [ ] Declining

2.2 Pipeline Performance
   - DAG Success Rate: ___% (target: >= 99%)
   - Average End-to-End Processing Time: ___
   - Queue Depth Trend: [ ] Stable  [ ] Growing

2.3 System Availability
   - Overall Availability: ___% (target: >= 99.5%)
   - Unplanned Downtime: ___ hours (target: < 2 hrs/month)
   - MTBF: ___
   - MTTR: ___

------------------------------------------------------------
3. QUALITY METRICS
------------------------------------------------------------

3.1 Incidents
   - Total incidents: ___
   - Severity 1: ___ | Severity 2: ___ | Severity 3: ___
   - Client-impacting: ___
   - Trend: [ ] Improving  [ ] Stable  [ ] Worsening

3.2 Deviations
   - Total deviations: ___
   - Open deviations: ___
   - Average age of open deviations: ___ days

3.3 CAPAs
   - Open CAPAs: ___
   - Completed CAPAs: ___
   - Effectiveness verified: ___
   - Overdue CAPAs: ___

3.4 Client Satisfaction
   - Average deliverable quality score: ___/5
   - On-time delivery rate: ___%
   - Client escalations: ___

------------------------------------------------------------
4. DATA INTEGRITY
------------------------------------------------------------
   - Hash chain verification status: [ ] PASS  [ ] FAIL
   - ALCOA+ spot-check pass rate: ___%
   - Audit trail anomalies detected: ___

------------------------------------------------------------
5. REGULATORY COMPLIANCE
------------------------------------------------------------
   - Ontology versions current: [ ] Yes  [ ] No
   - Regulatory changes identified: ___
   - Validation status: [ ] All valid  [ ] Reviews needed
   - Open regulatory actions: ___

------------------------------------------------------------
6. CHANGE MANAGEMENT
------------------------------------------------------------
   - Changes implemented: ___
   - Emergency changes: ___
   - Failed/rolled back changes: ___
   - Change-related incidents: ___

------------------------------------------------------------
7. RISK REGISTER
------------------------------------------------------------
   - Total active risks: ___
   - Top 3 risks:
     1. [Risk description] - Score: ___
     2. [Risk description] - Score: ___
     3. [Risk description] - Score: ___
   - New risks identified: ___
   - Risks retired: ___

------------------------------------------------------------
8. IMPROVEMENT ACTIONS
------------------------------------------------------------
   - Open actions: ___
   - Completed this quarter: ___
   - Overdue actions: ___
   - Proactive vs. reactive ratio: ___

------------------------------------------------------------
9. KEY DECISIONS AND ACTIONS
------------------------------------------------------------

| # | Decision/Action | Owner | Target Date | Priority |
|---|-----------------|-------|-------------|----------|
| 1 |                 |       |             |          |
| 2 |                 |       |             |          |

------------------------------------------------------------
10. NEXT REVIEW
------------------------------------------------------------
   - Scheduled date: [Date]
   - Focus areas for next quarter: [List]

============================================================
APPROVALS
============================================================

Prepared By: ___________________  Date: __________
             [Name / Role]

Reviewed By: ___________________  Date: __________
             [Head of QA]

Approved By: ___________________  Date: __________
             [VP Engineering]
============================================================
```

### 13.2 Annual System Review Report

The Annual System Review Report follows the same structure as the Quarterly Report but additionally includes:

- **Full-year trend analysis** across all metrics (4-quarter comparison).
- **Year-over-year comparison** (if prior year data available).
- **Regulatory compliance annual certification** statement.
- **Validation lifecycle summary** (all IQ/OQ/PQ activities for the year).
- **Training program annual summary** and curriculum review.
- **Risk register annual summary** with heatmap visualization.
- **Strategic improvement plan** for the coming year.
- **BR-PREDICT program progress** against scaling milestones.
- **Budget review** for quality and compliance activities.
- **External audit readiness assessment**.

---

## 14. Approval Signatures

### 14.1 SOP Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Author | _________________________ | _________________________ | _____________ |
| Head of Quality Assurance | _________________________ | _________________________ | _____________ |
| VP Engineering | _________________________ | _________________________ | _____________ |
| CEO | _________________________ | _________________________ | _____________ |

### 14.2 Review and Re-Approval Record

This SOP must be reviewed and re-approved annually or when triggered per Section 3.2.

| Review Date | Reviewed By | Outcome | Next Review Date |
|---|---|---|---|
| | | [ ] No changes [ ] Minor updates [ ] Major revision | |
| | | [ ] No changes [ ] Minor updates [ ] Major revision | |
| | | [ ] No changes [ ] Minor updates [ ] Major revision | |

---

## 15. Revision History

| Version | Date | Author | Description of Changes | Approved By |
|---|---|---|---|---|
| 1.0 | 2026-03-25 | ArcaScience Quality Assurance Team | Initial release | _____________ |
| | | | | |
| | | | | |

---

**CONTROLLED DOCUMENT** - This document is subject to change control procedures. Printed copies are uncontrolled. Always refer to the electronic version for the latest approved revision.
