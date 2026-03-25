# Data Processing Agreement (DPA)

**Document ID:** ARC-DPA-2026-001
**Version:** 1.0
**Effective Date:** 2026-03-25
**Classification:** Confidential - Restricted
**Document Owner:** ArcaScience GmbH, Data Protection Office
**Review Cycle:** Annual or upon material change to processing activities
**Applicable Regulation:** EU GDPR (Regulation 2016/679), FDA 21 CFR Part 11, EU Annex 11

---

## Table of Contents

1. [Definitions](#1-definitions)
2. [Subject Matter and Duration of Processing](#2-subject-matter-and-duration-of-processing)
3. [Nature and Purpose of Processing](#3-nature-and-purpose-of-processing)
4. [Types of Personal Data Processed](#4-types-of-personal-data-processed)
5. [Categories of Data Subjects](#5-categories-of-data-subjects)
6. [Obligations of the Processor (ArcaScience)](#6-obligations-of-the-processor-arcascience)
7. [Obligations of the Controller (Pharma Client)](#7-obligations-of-the-controller-pharma-client)
8. [Sub-Processing Provisions](#8-sub-processing-provisions)
9. [International Data Transfers](#9-international-data-transfers)
10. [Data Security Measures](#10-data-security-measures)
11. [Data Breach Notification Procedures](#11-data-breach-notification-procedures)
12. [Data Subject Rights Support](#12-data-subject-rights-support)
13. [Data Protection Impact Assessment Support](#13-data-protection-impact-assessment-support)
14. [Audit Rights](#14-audit-rights)
15. [Data Return and Deletion Upon Termination](#15-data-return-and-deletion-upon-termination)
16. [Liability and Indemnification](#16-liability-and-indemnification)
17. [EU Data Residency Provisions](#17-eu-data-residency-provisions)
18. [Annex A: Technical and Organizational Measures (TOMs)](#annex-a-technical-and-organizational-measures-toms)
19. [Signature Block](#signature-block)

---

## 1. Definitions

For the purposes of this Data Processing Agreement ("DPA"), the following definitions shall apply in addition to those provided in Article 4 of the EU General Data Protection Regulation (GDPR):

| Term | Definition |
|------|-----------|
| **Personal Data** | Any information relating to an identified or identifiable natural person ("Data Subject"); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier, or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that natural person. |
| **Special Categories of Personal Data** | Personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data, data concerning health, or data concerning a natural person's sex life or sexual orientation (Article 9 GDPR). |
| **Processing** | Any operation or set of operations which is performed on Personal Data or on sets of Personal Data, whether or not by automated means, such as collection, recording, organization, structuring, storage, adaptation or alteration, retrieval, consultation, use, disclosure by transmission, dissemination or otherwise making available, alignment or combination, restriction, erasure, or destruction. |
| **Controller** | The Pharma Client identified in the signature block of this DPA, which alone or jointly with others determines the purposes and means of the Processing of Personal Data. |
| **Processor** | ArcaScience GmbH, which processes Personal Data on behalf of the Controller in connection with the BRA (Benefit-Risk Assessment) platform services. |
| **Sub-Processor** | Any third party engaged by the Processor to carry out specific Processing activities on behalf of the Controller. |
| **Data Subject** | The identified or identifiable natural person to whom the Personal Data relates. |
| **Supervisory Authority** | An independent public authority established by an EU Member State pursuant to Article 51 GDPR. |
| **BRA Platform** | ArcaScience's Benefit-Risk Assessment platform, comprising 24 clinician-trained Specialized Language Models (SLMs), validated under GAMP 5 Category 5, operating with ALCOA+ compliant cryptographic hash chaining audit trails. |
| **ALCOA+** | Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, and Available - the data integrity standard applied to all processing within the BRA Platform. |
| **Pseudonymized Data** | Personal data that can no longer be attributed to a specific Data Subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organizational measures to ensure non-attribution. |
| **Breach** | A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, Personal Data transmitted, stored, or otherwise processed. |
| **Standard Contractual Clauses (SCCs)** | The contractual clauses adopted by the European Commission pursuant to Article 46(2)(c) GDPR for the transfer of Personal Data to third countries. |
| **Master Services Agreement (MSA)** | The overarching agreement between the Controller and the Processor governing the provision of BRA Platform services, to which this DPA is annexed. |

---

## 2. Subject Matter and Duration of Processing

### 2.1 Subject Matter

This DPA governs the Processing of Personal Data by the Processor (ArcaScience) on behalf of the Controller (Pharma Client) in connection with the provision of Benefit-Risk Assessment platform services under the Master Services Agreement referenced in the signature block.

The Processing activities include, but are not limited to:

- Ingestion and normalization of clinical trial data using MedDRA v27.0, SNOMED CT, ChEBI, and Disease Ontology coding systems
- Extraction and classification of adverse events (AE) from clinical publications and regulatory submissions
- Biomarker identification and risk-benefit signal detection across structured and unstructured data sources
- Generation of benefit-risk assessment outputs aligned with BRAT/CIOMS XII framework
- Production of regulatory-grade documentation in eCTD Module 2.5 and PBRER format
- Maintenance of ALCOA+ compliant audit trails with cryptographic hash chaining

### 2.2 Duration

This DPA shall remain in force for the duration of the Master Services Agreement plus any retention period specified in Section 15 (Data Return and Deletion). Specific processing timelines for each engagement shall be documented in the applicable Statement of Work (SOW).

| Phase | Duration | Processing Activities |
|-------|----------|----------------------|
| Onboarding | Up to 60 calendar days from SOW execution | Data ingestion, schema mapping, validation environment setup |
| Active Processing | Per SOW term (typically 12 to 36 months) | Ongoing BRA platform operations, signal detection, report generation |
| Wind-Down | 90 calendar days from termination notice | Data extraction, return, and certified deletion |
| Post-Termination Retention | Maximum 30 calendar days after wind-down | Retention of audit trails and processing logs required for regulatory compliance |

### 2.3 Governing Law

This DPA shall be governed by the laws of the Federal Republic of Germany, without regard to its conflict of laws principles, unless the Controller's registered office is in another EU/EEA Member State, in which case the laws of that Member State shall apply.

---

## 3. Nature and Purpose of Processing

### 3.1 Nature of Processing

The Processor operates the BRA Platform to perform automated and semi-automated analysis of pharmaceutical data on behalf of the Controller. Processing is conducted through 24 Specialized Language Models (SLMs) that have been clinician-trained and validated under GAMP 5 Category 5 requirements.

The processing infrastructure comprises:

| Component | Function | Data Interaction |
|-----------|----------|-----------------|
| Apache Airflow | Orchestration of data processing pipelines | Scheduling and coordination of processing jobs; no persistent data storage |
| Amazon S3 (EU Region) | Object storage for ingested documents and outputs | Encrypted at rest (AES-256); versioned; lifecycle policies enforced |
| ElasticSearch | Full-text indexing and search across processed corpora | Indexed representations of processed documents; access-controlled |
| Amazon DocumentDB | Structured metadata storage | Patient-level metadata, coding mappings, processing state |
| QDrant | Vector database for semantic similarity operations | Embedding vectors derived from processed text; no raw personal data stored |
| FastAPI / NestJS | API layer for platform services | Transient processing; TLS 1.3 in transit; request/response logging |

### 3.2 Purpose of Processing

The Processor shall Process Personal Data solely for the following purposes:

1. **Clinical Data Normalization** - Mapping raw clinical data to standardized ontologies (MedDRA v27.0, SNOMED CT, ChEBI, Disease Ontology) for consistent analysis
2. **Adverse Event Extraction** - Identification, classification, and coding of adverse events from clinical trial publications, case safety reports, and real-world evidence sources (target F1 score: 92%)
3. **Biomarker Analysis** - Detection and characterization of biomarker signals from multi-source clinical data (target F1 score: 90%)
4. **Risk Signal Detection** - Quantitative and qualitative assessment of risk signals across patient populations (target F1 score: 88%)
5. **Benefit Assessment** - Structured evaluation of therapeutic benefits from clinical evidence (target F1 score: 92%)
6. **Regulatory Report Generation** - Production of benefit-risk assessment documentation in BRAT/CIOMS XII, eCTD Module 2.5, and PBRER formats
7. **Audit Trail Maintenance** - Recording of all processing operations in ALCOA+ compliant, cryptographically hash-chained audit logs
8. **Platform Administration** - Technical operations necessary to maintain, secure, and optimize the BRA Platform in service of the above purposes

The Processor shall not Process Personal Data for any purpose other than those listed above without prior written authorization from the Controller.

---

## 4. Types of Personal Data Processed

### 4.1 Categories of Personal Data

The following categories of Personal Data may be Processed under this DPA, depending on the scope defined in each Statement of Work:

| Category | Data Elements | Sensitivity Level | Typical Source |
|----------|--------------|-------------------|---------------|
| **Patient Demographics** | Age, sex, weight, height, ethnicity, country of residence (pseudonymized) | Special Category (Health) | Clinical trial databases, CRFs |
| **Clinical Trial Identifiers** | Randomization codes, site numbers, study arm assignments | Personal (indirect identifier) | EDC systems, IVRS logs |
| **Adverse Event Data** | AE descriptions, onset dates, severity grades, outcomes, causality assessments, MedDRA coded terms | Special Category (Health) | Safety databases (e.g., Argus, ARISg), CSRs |
| **Concomitant Medications** | Drug names, doses, routes, start/stop dates | Special Category (Health) | CRFs, EMR extracts |
| **Medical History** | Pre-existing conditions, surgical history, relevant family history | Special Category (Health) | CRFs, baseline assessments |
| **Laboratory Results** | Hematology, chemistry, urinalysis, biomarker assay values | Special Category (Health) | Central and local lab data feeds |
| **Vital Signs** | Blood pressure, heart rate, temperature, respiratory rate | Special Category (Health) | CRFs, monitoring device exports |
| **Efficacy Endpoints** | Primary and secondary endpoint measurements, response criteria | Special Category (Health) | CRFs, imaging reports, PRO instruments |
| **Patient-Reported Outcomes** | Quality of life scores, symptom diaries, treatment satisfaction | Special Category (Health) | ePRO systems, paper CRFs |
| **Real-World Data** | Claims data, EMR extracts, registry data (pseudonymized) | Special Category (Health) | Data vendors, hospital registries |
| **Investigator Data** | Names, professional qualifications, site affiliations | Personal | Trial master files, delegation logs |
| **Pharmacovigilance Reporters** | Reporter initials, professional role, contact institution | Personal | ICSRs, MedWatch forms |

### 4.2 Special Categories - Article 9 GDPR

The majority of Personal Data processed through the BRA Platform constitutes data concerning health as defined in Article 9(1) GDPR. The legal basis for processing such data shall be established by the Controller and documented in each Statement of Work. Typical legal bases include:

- Article 9(2)(i) - Processing necessary for reasons of public interest in the area of public health
- Article 9(2)(j) - Processing necessary for scientific research purposes
- Article 9(2)(a) - Explicit consent of the Data Subject (where applicable)

### 4.3 Pseudonymization Requirements

All patient-level data shall be pseudonymized by the Controller prior to transfer to the Processor, unless explicitly agreed otherwise in writing. The Processor shall not attempt to re-identify any pseudonymized Data Subjects. The pseudonymization key shall be retained solely by the Controller.

---

## 5. Categories of Data Subjects

The following categories of Data Subjects may be affected by the Processing activities under this DPA:

| Category | Description | Estimated Volume per Engagement |
|----------|-------------|-------------------------------|
| Clinical Trial Participants | Patients enrolled in Controller's interventional clinical trials (Phases I through IV) | 500 to 100,000 subjects per study |
| Healthy Volunteers | Participants in Phase I or bioequivalence studies | 20 to 500 subjects per study |
| Real-World Evidence Subjects | Patients whose data is captured in observational studies, registries, or claims databases | 10,000 to 10,000,000 records |
| Adverse Event Reporters | Healthcare professionals and consumers who report adverse events through spontaneous reporting systems | Variable |
| Clinical Investigators | Principal investigators, sub-investigators, and study coordinators at trial sites | 50 to 5,000 per program |
| Pharmacovigilance Personnel | Individuals involved in safety reporting for the Controller | 10 to 200 per engagement |

---

## 6. Obligations of the Processor (ArcaScience)

### 6.1 General Obligations

The Processor shall:

- [ ] Process Personal Data only on documented instructions from the Controller, including with regard to transfers of Personal Data to a third country, unless required to do so by EU or Member State law (Article 28(3)(a) GDPR)
- [ ] Ensure that persons authorized to Process the Personal Data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality (Article 28(3)(b) GDPR)
- [ ] Implement and maintain the technical and organizational measures specified in Annex A of this DPA (Article 28(3)(c) GDPR)
- [ ] Respect the conditions for engaging Sub-Processors as set out in Section 8 (Article 28(3)(d) GDPR)
- [ ] Assist the Controller in responding to Data Subject rights requests as set out in Section 12 (Article 28(3)(e) GDPR)
- [ ] Assist the Controller in ensuring compliance with obligations under Articles 32 to 36 GDPR (Article 28(3)(f) GDPR)
- [ ] At the choice of the Controller, delete or return all Personal Data upon termination as set out in Section 15 (Article 28(3)(g) GDPR)
- [ ] Make available to the Controller all information necessary to demonstrate compliance and allow for audits as set out in Section 14 (Article 28(3)(h) GDPR)

### 6.2 Platform-Specific Obligations

In addition to general GDPR obligations, the Processor shall:

- [ ] Maintain GAMP 5 Category 5 validation status for all 24 SLMs used in the processing of Personal Data
- [ ] Ensure ALCOA+ compliance of all audit trails, with cryptographic hash chaining providing tamper-evidence for all processing records
- [ ] Maintain FDA 21 CFR Part 11 and EU Annex 11 compliance for electronic records and electronic signatures
- [ ] Apply MedDRA v27.0, SNOMED CT, ChEBI, and Disease Ontology normalization consistently across all processed data
- [ ] Maintain documented performance benchmarks (AE extraction F1 >= 92%, Biomarker F1 >= 90%, Risk F1 >= 88%, Benefit F1 >= 92%) and notify the Controller of any degradation below these thresholds
- [ ] Provide the Controller with quarterly data processing reports including volumes processed, error rates, and system availability metrics
- [ ] Maintain a current register of all processing activities conducted on behalf of the Controller pursuant to Article 30(2) GDPR

### 6.3 Personnel Requirements

| Requirement | Standard | Evidence |
|------------|----------|----------|
| Background checks | Completed for all personnel with access to Controller data | Certificate on file |
| GDPR training | Annual, role-specific | Training records, completion certificates |
| GxP training | Annual, per ICH guidelines | Training records in LMS |
| Confidentiality agreements | Signed prior to access | Executed NDAs on file |
| Access provisioning | Role-based, least privilege, reviewed quarterly | Access review logs |
| Separation of duties | No single individual can both process and approve data modifications | RBAC configuration records |

### 6.4 Data Protection Officer

The Processor has appointed a Data Protection Officer who can be reached at:

- **Name:** [To be completed upon execution]
- **Email:** dpo@arcascience.com
- **Phone:** [To be completed upon execution]
- **Postal Address:** [To be completed upon execution]

---

## 7. Obligations of the Controller (Pharma Client)

### 7.1 General Obligations

The Controller shall:

- [ ] Ensure that it has a lawful basis for the Processing of Personal Data under this DPA, including for any Special Categories of Personal Data
- [ ] Provide documented processing instructions to the Processor in writing prior to commencement of each processing activity
- [ ] Ensure that all Personal Data transferred to the Processor has been collected in accordance with applicable data protection laws
- [ ] Pseudonymize patient-level data prior to transfer to the Processor, retaining the pseudonymization key exclusively within the Controller's systems
- [ ] Designate an authorized contact point for data protection matters related to this DPA
- [ ] Notify the Processor without undue delay of any changes to applicable data protection laws that may affect the Processing
- [ ] Respond to Data Subject requests within the legally required timeframes, utilizing the Processor's assistance as set out in Section 12
- [ ] Conduct or commission Data Protection Impact Assessments where required by Article 35 GDPR

### 7.2 Data Quality Obligations

The Controller shall:

- [ ] Ensure the accuracy and completeness of Personal Data provided to the Processor
- [ ] Provide data in formats compatible with the BRA Platform ingestion specifications
- [ ] Notify the Processor of any known data quality issues that may affect processing outcomes
- [ ] Validate pseudonymization prior to data transfer using the Controller's own quality assurance procedures

### 7.3 Instruction Requirements

All processing instructions from the Controller to the Processor shall be:

- Issued in writing (email to a designated operational mailbox is acceptable)
- Documented with a unique instruction reference number
- Signed or authorized by the Controller's designated data protection contact
- Retained by both parties for the duration of this DPA plus five (5) years

---

## 8. Sub-Processing Provisions

### 8.1 General Authorization

The Controller provides general written authorization for the Processor to engage Sub-Processors, subject to the conditions set out in this Section 8.

### 8.2 Current Sub-Processors

As of the effective date of this DPA, the following Sub-Processors are authorized:

| Sub-Processor | Service Provided | Data Processed | Location |
|--------------|-----------------|----------------|----------|
| Amazon Web Services EMEA SARL | Cloud infrastructure (S3, DocumentDB) | All data categories per Section 4 | EU (Frankfurt, eu-central-1) |
| Elastic N.V. | ElasticSearch managed service | Indexed document representations | EU (Frankfurt) |
| QDrant GmbH | Vector database hosting | Embedding vectors (no raw personal data) | EU (Frankfurt) |
| [Additional sub-processors to be listed as applicable] | | | |

### 8.3 Notification of Changes

The Processor shall:

1. Maintain a current list of Sub-Processors, accessible to the Controller upon request
2. Notify the Controller in writing at least **30 calendar days** before engaging any new Sub-Processor or replacing an existing one
3. Provide the Controller with the following information for each proposed Sub-Processor:
   - Legal name and registered address
   - Nature of processing to be sub-contracted
   - Categories of Personal Data involved
   - Location of processing
   - Security certifications held (ISO 27001, SOC 2, etc.)
4. Allow the Controller to object to the engagement of a new Sub-Processor within **15 calendar days** of notification

### 8.4 Objection Procedure

If the Controller objects to a proposed Sub-Processor:

1. The Processor shall not engage the Sub-Processor for the Controller's data until the objection is resolved
2. The parties shall negotiate in good faith to find an alternative arrangement within **30 calendar days**
3. If no resolution is reached, the Controller may terminate the affected Statement of Work without penalty, with a **90-day** wind-down period
4. The Controller's right to object shall not be exercised unreasonably

### 8.5 Sub-Processor Contractual Requirements

The Processor shall impose on each Sub-Processor, by way of a written contract, data protection obligations that are no less protective than those set out in this DPA. In particular, each Sub-Processor contract shall include:

- [ ] Processing only on the Processor's documented instructions
- [ ] Confidentiality obligations for all personnel
- [ ] Technical and organizational security measures equivalent to Annex A
- [ ] Audit rights for both the Processor and the Controller
- [ ] Breach notification obligations
- [ ] Data return and deletion obligations upon termination

### 8.6 Processor Liability for Sub-Processors

The Processor shall remain fully liable to the Controller for the performance of each Sub-Processor's obligations under this DPA.

---

## 9. International Data Transfers

### 9.1 General Principle

All Processing of Personal Data under this DPA shall take place within the European Economic Area (EEA) unless otherwise agreed in writing.

### 9.2 EU Data Residency Default

The BRA Platform is configured for EU data residency by default:

| Data Category | Storage Location | Processing Location | Transfer Outside EEA |
|--------------|-----------------|--------------------|--------------------|
| Patient-level data | EU (Frankfurt, eu-central-1) | EU (Frankfurt) | No |
| Adverse event data | EU (Frankfurt, eu-central-1) | EU (Frankfurt) | No |
| Audit trail logs | EU (Frankfurt, eu-central-1) | EU (Frankfurt) | No |
| Generated reports | EU (Frankfurt, eu-central-1) | EU (Frankfurt) | No |
| System telemetry | EU (Frankfurt, eu-central-1) | EU (Frankfurt) | No |
| Backup data | EU (Frankfurt, eu-central-1; Ireland, eu-west-1) | N/A (cold storage) | No |

### 9.3 Transfers to Third Countries

In the event that a transfer of Personal Data outside the EEA becomes necessary:

1. **Adequacy Decisions** - Transfers may be made to countries for which the European Commission has issued an adequacy decision under Article 45 GDPR without additional safeguards
2. **Standard Contractual Clauses** - For transfers to countries without an adequacy decision, the parties shall execute the EU Standard Contractual Clauses (Commission Implementing Decision (EU) 2021/914) prior to any transfer
3. **Transfer Impact Assessment** - The Processor shall conduct and document a Transfer Impact Assessment (TIA) for each destination country, assessing:
   - Local surveillance laws and government access to data
   - Rule of law and judicial independence
   - Effectiveness of SCCs in the local legal context
   - Supplementary measures required (encryption, pseudonymization, contractual commitments)
4. **Supplementary Measures** - Where a TIA identifies risks to Data Subject rights, the Processor shall implement supplementary technical measures, which may include:
   - Encryption in transit and at rest with keys held exclusively within the EEA
   - Additional pseudonymization layers
   - Contractual commitments to challenge government access requests
   - Transparent reporting on government access requests received

### 9.4 Controller Approval

No transfer of Personal Data outside the EEA shall occur without the Controller's prior written approval, which shall specify:

- The destination country
- The legal transfer mechanism relied upon
- The categories of Personal Data to be transferred
- The duration and purpose of the transfer

---

## 10. Data Security Measures

### 10.1 General Security Standard

The Processor shall implement and maintain technical and organizational measures that ensure a level of security appropriate to the risk of Processing, taking into account the state of the art, the costs of implementation, and the nature, scope, context, and purposes of Processing, as well as the risk of varying likelihood and severity for the rights and freedoms of Data Subjects.

### 10.2 Security Framework

The Processor maintains an information security management system based on ISO 27001:2022, with the following key controls:

| Control Domain | Measures | Verification |
|---------------|----------|-------------|
| **Access Control** | Role-based access control (RBAC); multi-factor authentication (MFA) for all platform access; quarterly access reviews; automated deprovisioning | Access review reports; MFA enforcement logs |
| **Encryption - At Rest** | AES-256 encryption for all data at rest in S3, DocumentDB, and ElasticSearch; encryption keys managed via AWS KMS (EU region) | KMS key rotation logs; encryption configuration audits |
| **Encryption - In Transit** | TLS 1.3 for all data in transit; certificate pinning for API communications; mutual TLS for inter-service communication | TLS configuration scans; certificate inventory |
| **Network Security** | VPC isolation; private subnets for data stores; WAF protection; DDoS mitigation; network segmentation between tenants | Network architecture diagrams; penetration test reports |
| **Audit Logging** | ALCOA+ compliant audit trails; cryptographic hash chaining for tamper evidence; immutable log storage; minimum 7-year retention | Hash chain verification reports; log integrity checks |
| **Vulnerability Management** | Automated vulnerability scanning (weekly); penetration testing (annual, third-party); patch management SLA of 72 hours for critical, 30 days for high | Scan reports; penetration test reports; patch compliance dashboards |
| **Backup and Recovery** | Daily encrypted backups; cross-region replication within EU; RPO of 1 hour; RTO of 4 hours; annual disaster recovery testing | DR test reports; backup verification logs |
| **Incident Response** | 24/7 security monitoring; documented incident response plan; tabletop exercises (semi-annual) | Incident reports; exercise after-action reports |
| **Physical Security** | AWS EU data centers (SOC 2 Type II, ISO 27001 certified); no on-premises processing of Controller data | AWS compliance reports; service attestations |
| **Data Segregation** | Logical tenant isolation at database, storage, and application layers; tenant-specific encryption keys | Architecture reviews; isolation test results |

### 10.3 GAMP 5 and GxP Compliance

The BRA Platform is validated under GAMP 5 Category 5 (Custom Applications). The Processor maintains:

- Validation master plan and individual validation protocols for each of the 24 SLMs
- Installation Qualification (IQ), Operational Qualification (OQ), and Performance Qualification (PQ) documentation
- Ongoing periodic review per GAMP 5 guidelines (at minimum annually)
- Change control procedures ensuring validated state is maintained (see ARC-SOP-CC-2026-001)
- Traceability matrix linking requirements to test cases to validation evidence

### 10.4 21 CFR Part 11 and EU Annex 11 Compliance

| Requirement | Implementation |
|------------|---------------|
| Electronic signatures | Unique user ID plus MFA; signing manifested with printed name, date/time, and meaning of signature |
| Audit trails | Cryptographic hash-chained, immutable, recording who, what, when, and why for all data modifications |
| System access controls | RBAC with least privilege; automatic session timeout; account lockout after 5 failed attempts |
| Authority checks | System enforces user privileges based on validated role definitions |
| Device checks | IP allowlisting; device registration; anomaly detection for unauthorized access attempts |
| Training | All users complete system-specific training and demonstrate competency prior to access |
| Record retention | All electronic records retained in original format for the duration specified by the Controller (minimum 15 years for clinical data) |
| System documentation | SOPs, system descriptions, and validation documentation maintained under document control |

### 10.5 Detailed Technical and Organizational Measures

See Annex A for the complete schedule of TOMs.

---

## 11. Data Breach Notification Procedures

### 11.1 Definition of Breach

A "Breach" for the purposes of this DPA means a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, Personal Data transmitted, stored, or otherwise processed by the Processor on behalf of the Controller.

### 11.2 Notification Timeline

| Event | Timeline | Responsible Party |
|-------|----------|------------------|
| Breach detection | Immediate (automated alerting) | Processor Security Operations |
| Internal escalation | Within 1 hour of detection | Processor Incident Response Team |
| Initial notification to Controller | Within **24 hours** of confirmed breach | Processor DPO |
| Detailed notification to Controller | Within **48 hours** of confirmed breach | Processor DPO |
| Controller notification to Supervisory Authority | Within **72 hours** of becoming aware (Article 33 GDPR) | Controller DPO |
| Notification to Data Subjects (if required) | Without undue delay (Article 34 GDPR) | Controller, with Processor support |

### 11.3 Initial Notification Content

The Processor's initial notification to the Controller shall include, to the extent known:

- [ ] Date and time of breach detection
- [ ] Date and time of breach occurrence (if different)
- [ ] Nature of the breach (confidentiality, integrity, availability)
- [ ] Categories and approximate number of Data Subjects affected
- [ ] Categories and approximate number of Personal Data records affected
- [ ] Name and contact details of the Processor's DPO or point of contact
- [ ] Description of likely consequences of the breach
- [ ] Measures taken or proposed to address the breach and mitigate its effects

### 11.4 Detailed Notification Content

The Processor's detailed notification shall supplement the initial notification with:

- [ ] Root cause analysis (preliminary)
- [ ] Technical details of the breach vector
- [ ] Chronological timeline of events
- [ ] Specific data elements affected
- [ ] Geographic scope of the breach
- [ ] Measures taken to contain the breach
- [ ] Measures taken to prevent recurrence
- [ ] Assessment of residual risk to Data Subjects

### 11.5 Ongoing Obligations

Following a Breach, the Processor shall:

1. Cooperate fully with the Controller's investigation
2. Preserve all evidence related to the breach, including log files and forensic images
3. Provide regular status updates (at minimum daily during active investigation)
4. Conduct a comprehensive root cause analysis and share findings with the Controller within **30 calendar days**
5. Implement agreed corrective and preventive actions within timelines agreed with the Controller
6. Provide the Controller with a final incident report within **60 calendar days** of breach closure
7. Participate in lessons-learned reviews and incorporate findings into security improvement plans

### 11.6 Breach Register

The Processor shall maintain a register of all Breaches (including near-misses) related to the Controller's Personal Data, including:

- Date and time of occurrence
- Nature and scope
- Data categories affected
- Response actions taken
- Notifications made
- Corrective actions implemented
- Closure date and sign-off

This register shall be made available to the Controller upon request and during audits.

---

## 12. Data Subject Rights Support

### 12.1 Scope of Support

The Processor shall assist the Controller in fulfilling its obligation to respond to Data Subject requests to exercise their rights under Chapter III of the GDPR, as follows:

| Right | GDPR Article | Processor Obligation | Response SLA |
|-------|-------------|---------------------|-------------|
| **Right of Access** | Art. 15 | Search and compile all Personal Data relating to the requesting Data Subject across all BRA Platform data stores | 5 business days |
| **Right to Rectification** | Art. 16 | Correct or complete Personal Data upon Controller instruction | 3 business days |
| **Right to Erasure** | Art. 17 | Delete Personal Data upon Controller instruction, subject to legal retention obligations | 10 business days |
| **Right to Restriction** | Art. 18 | Technically restrict Processing of specified Personal Data | 3 business days |
| **Right to Data Portability** | Art. 20 | Export Personal Data in structured, commonly used, machine-readable format (JSON, CSV, XML) | 10 business days |
| **Right to Object** | Art. 21 | Cease Processing of specified Personal Data upon Controller instruction | 3 business days |
| **Automated Decision-Making** | Art. 22 | Provide meaningful information about the logic involved in automated processing, including model explainability documentation for relevant SLMs | 10 business days |

### 12.2 Procedure

1. The Controller shall notify the Processor of a Data Subject request via the designated operational contact
2. The Processor shall acknowledge receipt within **1 business day**
3. The Processor shall provide the Controller with the requested information, correction confirmation, or deletion confirmation within the SLA specified above
4. All responses shall include an audit trail entry documenting the request, actions taken, and completion date
5. If the Processor receives a Data Subject request directly, it shall redirect the request to the Controller within **2 business days** and shall not respond to the Data Subject directly unless instructed by the Controller

### 12.3 Fees

The Processor shall provide Data Subject rights support at no additional charge for up to **20 requests per calendar quarter**. Requests exceeding this volume shall be charged at the Processor's then-current professional services rate, as agreed in the MSA.

---

## 13. Data Protection Impact Assessment Support

### 13.1 DPIA Obligation

Where the Controller is required to carry out a Data Protection Impact Assessment (DPIA) pursuant to Article 35 GDPR in connection with the Processing activities under this DPA, the Processor shall provide the following assistance:

### 13.2 Scope of Support

| DPIA Element | Processor Contribution |
|-------------|----------------------|
| **Systematic description of Processing** | Provide detailed data flow diagrams, system architecture documentation, and processing logic descriptions for BRA Platform operations |
| **Assessment of necessity and proportionality** | Document the technical basis for each processing operation and any less intrusive alternatives considered during platform design |
| **Risk assessment** | Provide threat modeling outputs, vulnerability assessment results, and risk register entries specific to the Controller's data |
| **Measures to address risks** | Document implemented technical and organizational measures (Annex A) and propose additional mitigations where risks are identified |
| **Stakeholder consultation** | Participate in DPIA consultation workshops with the Controller's DPO and relevant business stakeholders |
| **Prior consultation support** | If prior consultation with a Supervisory Authority is required (Article 36 GDPR), provide technical documentation and participate in authority discussions as requested |

### 13.3 DPIA Review Cycle

The Processor shall:

- Support an initial DPIA prior to commencement of processing under each Statement of Work
- Support DPIA reviews at least annually or upon material change to processing activities
- Proactively notify the Controller when platform changes may trigger a DPIA review requirement

---

## 14. Audit Rights

### 14.1 Controller Audit Rights

The Controller shall have the right to conduct audits of the Processor's compliance with this DPA, subject to the following conditions:

1. **Scope** - Audits may cover all aspects of the Processor's compliance with this DPA, including technical and organizational security measures, sub-processor management, breach response procedures, and personnel training
2. **Frequency** - The Controller may conduct up to **one (1) comprehensive audit per calendar year**, plus additional audits following a confirmed Breach or upon reasonable suspicion of non-compliance
3. **Notice** - The Controller shall provide at least **30 calendar days** written notice of an intended audit, specifying the scope and proposed dates
4. **Conduct** - Audits may be conducted by the Controller's internal audit function or by an independent third-party auditor appointed by the Controller, provided that the auditor is bound by appropriate confidentiality obligations and is not a competitor of the Processor
5. **Cooperation** - The Processor shall cooperate fully with the audit, providing access to relevant premises, personnel, systems, and documentation
6. **Business Hours** - On-site audit activities shall be conducted during normal business hours (09:00 to 18:00 CET) and shall not unreasonably disrupt the Processor's operations

### 14.2 Audit Alternatives

In lieu of an on-site audit, the Controller may accept:

- [ ] SOC 2 Type II report (issued within the preceding 12 months)
- [ ] ISO 27001:2022 certification (current)
- [ ] GAMP 5 validation summary report (current)
- [ ] Independent third-party audit report commissioned by the Processor
- [ ] Responses to the Controller's written audit questionnaire (e.g., SIG, CAIQ)

### 14.3 Audit Findings

1. The Processor shall respond to all audit findings within **30 calendar days**, providing a corrective action plan with timelines
2. Critical findings (those presenting an immediate risk to Personal Data) shall be addressed within **72 hours** with interim mitigations
3. The Processor shall implement agreed corrective actions within the timelines specified in the corrective action plan
4. The Controller may verify implementation of corrective actions through a targeted follow-up audit

### 14.4 Costs

Each party shall bear its own costs for the annual audit. Additional audits requested by the Controller (beyond the annual audit) shall be at the Controller's expense, unless the audit is triggered by a confirmed Breach attributable to the Processor.

---

## 15. Data Return and Deletion Upon Termination

### 15.1 Controller Election

Upon termination or expiry of the Master Services Agreement or any Statement of Work, the Controller shall instruct the Processor to either:

- **(a) Return** all Personal Data to the Controller in a structured, commonly used, and machine-readable format; or
- **(b) Delete** all Personal Data and certify such deletion in writing; or
- **(c) A combination** of return and deletion, as specified by the Controller

### 15.2 Timelines

| Activity | Timeline |
|----------|----------|
| Controller election notice | Within 30 calendar days of termination |
| Data return (if elected) | Within 60 calendar days of Controller election |
| Data deletion (if elected) | Within 90 calendar days of Controller election |
| Deletion certification | Within 10 business days of completed deletion |
| Backup purge | Within 120 calendar days of Controller election |

### 15.3 Return Format

If the Controller elects data return, the Processor shall provide:

- All Personal Data in the formats specified in the SOW (default: JSON, CSV, and/or XML)
- Associated metadata, including MedDRA, SNOMED CT, ChEBI, and Disease Ontology mappings
- Audit trail exports in a self-contained, verifiable format (including hash chain verification tools)
- Data dictionary and schema documentation sufficient for the Controller to interpret the returned data independently
- Transfer via encrypted channel (SFTP with AES-256 encryption or equivalent)

### 15.4 Deletion Standards

Deletion shall be performed in accordance with NIST SP 800-88 Rev. 1 guidelines:

| Storage Medium | Deletion Method |
|---------------|----------------|
| S3 objects | Secure delete with versioning purge; bucket lifecycle enforcement |
| DocumentDB records | Logical deletion followed by physical overwrite within 30 days |
| ElasticSearch indices | Index deletion with segment merge |
| QDrant vectors | Collection deletion with storage reclamation |
| Backup media | Cryptographic erasure (destruction of encryption keys) |
| Log files | Retained for regulatory compliance per Section 15.5; Personal Data redacted where feasible |

### 15.5 Regulatory Retention Exceptions

The Processor may retain Personal Data beyond the deletion timeline where:

1. Required by EU or Member State law (the Processor shall inform the Controller of such requirements unless prohibited by law)
2. Required for the Processor's legitimate compliance with audit trail obligations under 21 CFR Part 11 or EU Annex 11
3. Contained within system logs necessary for GxP compliance (in which case, the data shall be restricted from further Processing and retained only for the mandated period)

Any retained data shall be subject to the security measures specified in this DPA for the duration of retention.

---

## 16. Liability and Indemnification

### 16.1 Processor Liability

The Processor shall be liable for damages caused by Processing that does not comply with this DPA, the GDPR, or documented Controller instructions. The Processor shall be exempt from liability if it demonstrates that it is not in any way responsible for the event giving rise to the damage (Article 82(3) GDPR).

### 16.2 Liability Cap

Subject to Section 16.3, the Processor's aggregate liability under this DPA shall be limited to:

| Liability Category | Cap |
|-------------------|-----|
| Direct damages (excluding Breaches) | The greater of EUR 5,000,000 or the total fees paid under the MSA in the preceding 12-month period |
| Breach-related damages | The greater of EUR 10,000,000 or 200% of the total fees paid under the MSA in the preceding 12-month period |
| Regulatory fines and penalties | No cap (each party liable for its own fines) |

### 16.3 Uncapped Liability

The liability cap in Section 16.2 shall not apply to:

- Liability arising from the Processor's willful misconduct or gross negligence
- Liability arising from unauthorized Processing (Processing outside documented Controller instructions)
- Liability arising from the Processor's failure to comply with the Breach notification obligations in Section 11
- Indemnification obligations under Section 16.4

### 16.4 Indemnification

**Processor Indemnification:** The Processor shall indemnify, defend, and hold harmless the Controller from and against any third-party claims, losses, damages, fines, and expenses (including reasonable legal fees) arising from:

- The Processor's breach of this DPA
- The Processor's violation of applicable data protection laws
- The Processor's negligent or wrongful acts or omissions in the Processing of Personal Data

**Controller Indemnification:** The Controller shall indemnify, defend, and hold harmless the Processor from and against any third-party claims, losses, damages, fines, and expenses (including reasonable legal fees) arising from:

- The Controller's breach of this DPA
- The Controller's failure to establish a lawful basis for Processing
- The Controller's provision of inaccurate, incomplete, or improperly pseudonymized Personal Data

### 16.5 Mitigation

Each party shall take reasonable steps to mitigate any loss or damage for which the other party may be liable under this DPA.

---

## 17. EU Data Residency Provisions

### 17.1 Data Residency Commitment

The Processor commits that all Personal Data processed under this DPA shall be stored and processed exclusively within the European Economic Area (EEA), unless the Controller provides explicit prior written consent for processing in a specific non-EEA location.

### 17.2 Infrastructure Configuration

| Component | Region | Availability Zones | Data Residency Guarantee |
|-----------|--------|-------------------|------------------------|
| Primary compute (BRA Platform) | EU (Frankfurt, eu-central-1) | eu-central-1a, eu-central-1b, eu-central-1c | All processing within EEA |
| Primary storage (S3) | EU (Frankfurt, eu-central-1) | Multi-AZ within eu-central-1 | All data at rest within EEA |
| Metadata store (DocumentDB) | EU (Frankfurt, eu-central-1) | Multi-AZ within eu-central-1 | All structured data within EEA |
| Search index (ElasticSearch) | EU (Frankfurt, eu-central-1) | Multi-AZ within eu-central-1 | All indexed data within EEA |
| Vector store (QDrant) | EU (Frankfurt) | Single region | All vector data within EEA |
| Disaster recovery | EU (Ireland, eu-west-1) | Multi-AZ within eu-west-1 | DR site within EEA |
| Backup | EU (Frankfurt + Ireland) | Cross-region within EEA | All backups within EEA |

### 17.3 Technical Enforcement

The Processor enforces EU data residency through:

1. **AWS Service Control Policies (SCPs)** - Organizational policies preventing resource creation outside approved EU regions
2. **Network Controls** - VPC configurations ensuring data does not traverse non-EU network paths
3. **API Gateway Geo-Restrictions** - API endpoints configured to reject requests routing through non-EU infrastructure
4. **Encryption Key Residency** - All AWS KMS customer master keys (CMKs) created and stored in the EU (Frankfurt) region
5. **DNS Configuration** - All DNS records pointing to EU-based endpoints
6. **Monitoring and Alerting** - Automated alerts for any configuration changes that could affect data residency

### 17.4 Data Residency Verification

The Controller may request a data residency verification at any time. The Processor shall provide, within **10 business days**:

- Current infrastructure configuration evidence (sanitized to remove security-sensitive details)
- AWS resource inventory confirming region placement
- Network flow analysis demonstrating data paths remain within the EEA
- Certification from the Processor's CTO or CISO confirming continued EU data residency compliance

### 17.5 Schrems II Compliance

The Processor's EU data residency configuration is designed to address the concerns raised in the Court of Justice of the European Union's Schrems II decision (Case C-311/18) by ensuring that:

- No Personal Data is transferred to or accessible from jurisdictions subject to Section 702 of the U.S. Foreign Intelligence Surveillance Act or Executive Order 12333
- Encryption keys are held exclusively within the EEA
- The Processor will challenge any government access request that conflicts with EU data protection law and will notify the Controller to the extent legally permitted

---

## Annex A: Technical and Organizational Measures (TOMs)

The following measures are implemented by the Processor to protect Personal Data processed under this DPA. These measures satisfy the requirements of Article 32 GDPR and are aligned with the Processor's GAMP 5 Category 5 validation and ALCOA+ compliance framework.

### A.1 Measures for the Pseudonymization and Encryption of Personal Data

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.1.1 | Pseudonymization at ingestion | All patient identifiers stripped or replaced with pseudonymous tokens at the point of ingestion into the BRA Platform; mapping tables not stored by the Processor |
| A.1.2 | Encryption at rest | AES-256 encryption for all data stores (S3, DocumentDB, ElasticSearch); AWS KMS managed keys with automatic annual rotation |
| A.1.3 | Encryption in transit | TLS 1.3 enforced for all external and internal communications; HSTS enabled; certificate pinning for API clients |
| A.1.4 | Field-level encryption | Sensitive fields (e.g., date of birth ranges, genetic markers) encrypted at the application layer with tenant-specific keys |
| A.1.5 | Key management | AWS KMS with customer-managed CMKs; key access restricted to designated security personnel; key usage logged and monitored |
| A.1.6 | Cryptographic hash chaining | All audit trail entries linked via SHA-256 hash chains, providing tamper-evidence and supporting ALCOA+ integrity requirements |

### A.2 Measures for Ensuring Ongoing Confidentiality, Integrity, Availability, and Resilience

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.2.1 | Access control | Role-based access control (RBAC) with least privilege principle; quarterly access reviews; automated orphan account detection |
| A.2.2 | Multi-factor authentication | MFA required for all platform access (TOTP or hardware security key); no password-only access permitted |
| A.2.3 | Network segmentation | VPC isolation per tenant; private subnets for data stores; no direct internet access to databases; bastion host access with session recording |
| A.2.4 | Web application firewall | AWS WAF with OWASP Top 10 rule set; custom rules for API protection; rate limiting; bot detection |
| A.2.5 | DDoS protection | AWS Shield Advanced with 24/7 DDoS response team |
| A.2.6 | Intrusion detection | Network and host-based intrusion detection; anomaly-based alerting; integration with SIEM |
| A.2.7 | Anti-malware | Endpoint protection on all compute instances; real-time scanning of uploaded files |
| A.2.8 | High availability | Multi-AZ deployment for all critical components; automated failover; 99.9% uptime SLA |
| A.2.9 | Load balancing | Application load balancers with health checks; auto-scaling based on processing demand |
| A.2.10 | Data integrity checks | Checksums computed at ingestion and verified at each processing stage; ALCOA+ compliance verification on every write operation |

### A.3 Measures for Ensuring the Ability to Restore Availability and Access to Personal Data in a Timely Manner

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.3.1 | Backup strategy | Daily incremental backups; weekly full backups; encrypted and stored in a separate EU region (Ireland) |
| A.3.2 | Recovery point objective (RPO) | 1 hour for all data stores |
| A.3.3 | Recovery time objective (RTO) | 4 hours for full platform restoration |
| A.3.4 | Disaster recovery | Cross-region DR site in EU (Ireland); automated failover capability; annual DR testing with documented results |
| A.3.5 | Backup testing | Monthly restoration tests for random data subsets; annual full restoration test |
| A.3.6 | Incident response plan | Documented and tested incident response procedures; defined roles and escalation paths; semi-annual tabletop exercises |
| A.3.7 | Business continuity plan | Documented BCP covering loss of key personnel, data center failure, and supply chain disruption; annual review and update |

### A.4 Measures for Regularly Testing, Assessing, and Evaluating the Effectiveness of TOMs

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.4.1 | Vulnerability scanning | Automated weekly scans of all infrastructure and application components; results triaged within 24 hours |
| A.4.2 | Penetration testing | Annual third-party penetration test; scope includes application, network, and social engineering vectors; remediation tracked to closure |
| A.4.3 | Security audit | Annual internal security audit; ISO 27001 certification audit cycle |
| A.4.4 | GAMP 5 periodic review | Annual review of all validated systems to confirm continued validated state; documented per GAMP 5 guidelines |
| A.4.5 | SLM performance monitoring | Continuous monitoring of SLM performance metrics (AE extraction F1, Biomarker F1, Risk F1, Benefit F1) with alerts for degradation below validated thresholds |
| A.4.6 | Access reviews | Quarterly review of all user access rights; removal of unnecessary privileges within 5 business days |
| A.4.7 | Policy reviews | Annual review and update of all information security policies and procedures |
| A.4.8 | Training effectiveness | Annual assessment of security and data protection training effectiveness through testing and simulated phishing exercises |

### A.5 Measures for User Identification and Authorization

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.5.1 | Unique user identification | Every user assigned a unique, non-transferable user ID; shared accounts prohibited |
| A.5.2 | Authentication policy | Minimum 12-character passwords; complexity requirements enforced; password history (last 12); 90-day maximum age |
| A.5.3 | Session management | Automatic session timeout after 15 minutes of inactivity; concurrent session limits; secure session token handling |
| A.5.4 | Account lockout | Account locked after 5 consecutive failed login attempts; unlock requires administrator intervention or verified self-service |
| A.5.5 | Privileged access management | Separate administrative accounts; just-in-time (JIT) privilege elevation; all privileged actions logged |
| A.5.6 | Service account management | Service accounts with minimum required permissions; no interactive login; credentials rotated every 90 days; monitored for anomalous use |

### A.6 Measures for the Protection of Data During Transmission

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.6.1 | Transport encryption | TLS 1.3 for all external communications; TLS 1.2 minimum for legacy integrations (with documented exception and migration plan) |
| A.6.2 | API security | OAuth 2.0 with JWT tokens; API key rotation every 90 days; rate limiting per client; request/response validation |
| A.6.3 | File transfer | SFTP with AES-256 encryption for bulk data transfers; PGP encryption for email-based transfers (exceptional circumstances only) |
| A.6.4 | Certificate management | Automated certificate provisioning and renewal via AWS Certificate Manager; certificate transparency monitoring |
| A.6.5 | VPN access | IPsec VPN tunnels for site-to-site connectivity; WireGuard VPN for authorized remote access |

### A.7 Measures for the Protection of Data During Storage

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.7.1 | Storage encryption | All data stores encrypted at rest with AES-256; encryption enabled by default and cannot be disabled |
| A.7.2 | Data classification | All data classified according to sensitivity (Public, Internal, Confidential, Restricted); handling procedures enforced per classification |
| A.7.3 | Retention management | Automated lifecycle policies enforcing retention periods; automated deletion at expiry with audit logging |
| A.7.4 | Secure deletion | NIST SP 800-88 Rev. 1 compliant deletion procedures; cryptographic erasure for encrypted storage |
| A.7.5 | Immutable audit logs | Audit trail entries stored in append-only storage with hash chain verification; no delete or modify capability for any user role |

### A.8 Measures for Ensuring Physical Security of Processing Locations

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.8.1 | Data center security | AWS EU data centers with SOC 2 Type II and ISO 27001 certification; multi-layer physical security including biometric access, mantrap entry, 24/7 CCTV, and security personnel |
| A.8.2 | Office security | ArcaScience offices secured with access card entry; visitor logs; clean desk policy; secure disposal of physical media |
| A.8.3 | Endpoint security | Company-managed devices with full disk encryption; remote wipe capability; USB port restrictions; application allowlisting |

### A.9 Measures for Ensuring Event Logging

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.9.1 | Comprehensive logging | All system events, user actions, data access, and administrative operations logged with timestamp, user ID, action, and outcome |
| A.9.2 | ALCOA+ compliance | All audit trail entries verified for Attributability, Legibility, Contemporaneousness, Originality, and Accuracy, plus Completeness, Consistency, Endurance, and Availability |
| A.9.3 | Log integrity | Cryptographic hash chaining (SHA-256) ensuring tamper-evidence; hash chain verification run daily with automated alerting on any discrepancy |
| A.9.4 | Centralized logging | All logs forwarded to centralized SIEM (Security Information and Event Management) system; real-time correlation and alerting |
| A.9.5 | Log retention | Minimum 7 years for GxP-relevant logs; minimum 2 years for operational logs; configurable per Controller requirements |
| A.9.6 | Log access control | Read-only access for auditors and investigators; no user (including administrators) can modify or delete audit trail entries |

### A.10 Measures for Ensuring System Configuration and Default Settings

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.10.1 | Hardened baselines | All systems deployed from hardened images based on CIS Benchmarks; deviations documented and approved |
| A.10.2 | Configuration management | Infrastructure as Code (IaC) using Terraform; all changes version-controlled and peer-reviewed |
| A.10.3 | Change control | All changes to production systems subject to the formal change control procedure (ARC-SOP-CC-2026-001); no unauthorized changes permitted |
| A.10.4 | Default credentials | All default credentials changed prior to deployment; automated scanning for default credentials |
| A.10.5 | Least functionality | Unnecessary services, ports, and protocols disabled; software inventory maintained and reviewed quarterly |

### A.11 Measures for Internal IT and IT Security Governance

| # | Measure | Implementation Detail |
|---|---------|----------------------|
| A.11.1 | Security governance | Information Security Steering Committee meets quarterly; CISO reports to CEO; security budget allocated annually |
| A.11.2 | Risk management | Annual information security risk assessment; risk register maintained and reviewed quarterly; risk treatment plans tracked to closure |
| A.11.3 | Vendor management | Third-party risk assessments for all vendors with access to Personal Data; annual reassessment; contractual security requirements |
| A.11.4 | Security awareness | Mandatory annual security awareness training for all employees; role-specific training for developers, operators, and administrators |
| A.11.5 | Secure development | Secure Software Development Lifecycle (SSDLC) with threat modeling, code review, static analysis, and dynamic testing |

### A.12 Measures for Certification and Assurance

| # | Measure | Current Status |
|---|---------|---------------|
| A.12.1 | ISO 27001:2022 | Certified (scope: BRA Platform operations) |
| A.12.2 | SOC 2 Type II | Report issued annually (Trust Service Criteria: Security, Availability, Processing Integrity, Confidentiality) |
| A.12.3 | GAMP 5 Category 5 | Validated (24 SLMs, supporting infrastructure) |
| A.12.4 | FDA 21 CFR Part 11 | Compliant (assessed annually) |
| A.12.5 | EU Annex 11 | Compliant (assessed annually) |
| A.12.6 | ALCOA+ | Compliant (continuous monitoring) |

---

## Signature Block

This Data Processing Agreement is entered into as of the date last signed below.

### Controller (Pharma Client)

| Field | Details |
|-------|---------|
| Company Name | ______________________________ |
| Registered Address | ______________________________ |
| Authorized Signatory Name | ______________________________ |
| Title | ______________________________ |
| Signature | ______________________________ |
| Date | ______________________________ |
| Data Protection Contact | ______________________________ |
| Email | ______________________________ |

### Processor (ArcaScience GmbH)

| Field | Details |
|-------|---------|
| Company Name | ArcaScience GmbH |
| Registered Address | [To be completed] |
| Authorized Signatory Name | ______________________________ |
| Title | ______________________________ |
| Signature | ______________________________ |
| Date | ______________________________ |
| Data Protection Officer | ______________________________ |
| Email | dpo@arcascience.com |

---

### Amendment Log

| Version | Date | Author | Description of Change | Approved By |
|---------|------|--------|-----------------------|-------------|
| 1.0 | 2026-03-25 | ArcaScience Data Protection Office | Initial release | [Name, Title] |
| | | | | |
| | | | | |

---

*End of Document - ARC-DPA-2026-001 v1.0*
