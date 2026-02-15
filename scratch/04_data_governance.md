# Section 4: Data Governance & Confidentiality Framework

## Purpose

This section directly addresses the confidentiality and data protection concerns raised by MHRA during the January 2026 meeting. MHRA participants made clear that patient-level data, ongoing safety investigations, and internal assessments cannot be shared externally. Any proposed collaboration must operate within these constraints from day one, with no exceptions and no ambiguity.

---

## 1. Understanding MHRA's Confidentiality Requirements

The meeting transcript reveals four non-negotiable boundaries stated by MHRA:

| Constraint | Direct Quote (Allison / MHRA) | Implication |
|---|---|---|
| **Yellow Card data cannot leave MHRA** | "We can't give you our yellow card data... it's patient level data, we're not allowed to share that" | No patient-level pharmacovigilance data may be transmitted to, accessed by, or processed on ArcaScience infrastructure |
| **Ongoing safety issues are confidential** | "Most of our things are highly confidential"; "I don't think we could share an ongoing safety issue with you" | Any proof-of-concept must use historical, already-public safety evaluations only |
| **CPRD access is restricted** | "We couldn't use that data source" (regarding CPRD's 30M patient records over 30 years) | CPRD integration would require in-situ deployment within MHRA's secure environment; data extraction is not an option |
| **Regulatory independence must be preserved** | Implied throughout: MHRA cannot appear reliant on a commercial vendor's AI outputs for active regulatory decisions | The collaboration framework must position ArcaScience as a tool provider, not a decision-maker; MHRA assessors remain the sole arbiters of benefit-risk conclusions |

**Design principle**: The collaboration model must be constructed so that MHRA shares zero confidential data during the initial phase, and any future phases involving internal data are architecturally designed so that data never leaves MHRA's control.

---

## 2. ArcaScience Data Classification Model

To map directly onto MHRA's constraints, we propose a three-tier data classification:

### Tier 1: Public Domain Sources (No MHRA Data Required)

These sources are openly available and can be processed by ArcaScience directly on its own infrastructure. No MHRA data or access is involved.

| Source | Access Method | Notes |
|---|---|---|
| PubMed / MEDLINE | ArcaScience Profiling Base (already indexed) | Literature articles, systematic reviews, meta-analyses |
| ClinicalTrials.gov | ArcaScience Profiling Base (already indexed) | Trial registries, protocols, results |
| Product labels / SmPCs | Public regulatory databases | UK-specific labeling from MHRA public site |
| MHRA Public Assessment Reports (PARs) | Publicly available on MHRA website | Historical assessments already in the public domain |
| MHRA safety communications (Drug Safety Updates, alerts) | Publicly available | Only those already published by MHRA |
| WHO / Uppsala Monitoring Centre public signals | Publicly available | Published signal assessments |

**Status**: ArcaScience already processes Tier 1 sources within its existing Profiling Base (documented as containing 100B+ data points from public sources). This tier requires no data exchange with MHRA whatsoever.

### Tier 2: Subscription / Licensed Databases

These sources require licensing agreements but do not contain MHRA-internal or patient-level data.

| Source | Access Method | Notes |
|---|---|---|
| FDA Adverse Event Reporting System (FAERS) | Public download / API | US pharmacovigilance data; publicly available |
| EudraVigilance public data (line listings) | EMA access portal | European ADR data; public aggregate level |
| Pharmapendium, Cortellis, or similar | Commercial subscription | ArcaScience or MHRA holds license |
| MedDRA ontology | Licensed | ArcaScience already uses a restructured version for adverse event normalization |

**Status**: ArcaScience has documented experience integrating subscription databases (referenced in the i-Demo presentation as including sources like "Pharmapendium or FX"). Access requires standard data licensing, not MHRA data sharing.

### Tier 3: MHRA Internal / Confidential Data (NEVER Leaves MHRA)

This tier encompasses all data that MHRA has identified as non-shareable.

| Source | Classification | Handling Rule |
|---|---|---|
| Yellow Card reports (patient-level) | Strictly confidential | Must remain within MHRA infrastructure at all times; no extraction, no transmission, no external processing |
| CPRD (Clinical Practice Research Datalink) | Restricted access | 30M patients, 30 years of records; any processing must occur in-situ within MHRA's secure environment |
| Internal benefit-risk assessments (ongoing) | Highly confidential | Cannot be shared with external parties while under active review |
| Internal signal detection work products | Highly confidential | Same as above |
| Completed internal assessments (unpublished) | Confidential | May only become available if MHRA chooses to declassify or publish |

**Governing rule for Tier 3**: ArcaScience never receives, stores, processes, or has access to Tier 3 data on its own infrastructure. Any future interaction with Tier 3 data would require deployment of ArcaScience tools within MHRA's own secure environment (see Section 3 below).

---

## 3. Proposed Operating Models for Each Tier

### Model A: Public-Domain Proof of Concept (Tier 1 Only) -- Recommended Starting Point

```
+-------------------------------------------------+
|           ArcaScience Infrastructure             |
|           (AWS / Kubernetes)                     |
|                                                  |
|   +-------------------------------------------+ |
|   |  Profiling Base (Public Data Only)         | |
|   |  - PubMed, ClinicalTrials.gov, labels     | |
|   |  - MHRA Public Assessment Reports         | |
|   |  - Published safety communications        | |
|   +-------------------------------------------+ |
|                                                  |
|   +-------------------------------------------+ |
|   |  24 SLM Models                            | |
|   |  (extraction, normalization, clustering)   | |
|   +-------------------------------------------+ |
|                                                  |
|   Output: Structured BRA on a publicly known     |
|   safety issue selected by MHRA                  |
+-------------------------------------------------+
              |
              | Deliverable only: structured output
              | (no MHRA data involved at any stage)
              v
+-------------------------------------------------+
|           MHRA Review                            |
|   Assessors compare output against their own     |
|   previously completed, published assessment     |
+-------------------------------------------------+
```

**Key properties**:
- Zero MHRA data enters ArcaScience systems
- MHRA selects the topic (a historical, already-public safety issue)
- ArcaScience runs its models against publicly available sources only
- MHRA evaluates the output against their own known results
- No confidentiality risk whatsoever

### Model B: On-Premises / Private Deployment (Future Phase -- For Tier 2 and Tier 3)

For any future phase involving MHRA's internal data sources, ArcaScience has stated that it supports client-side deployment where "the data never leaves the client side" (Romain, meeting transcript). The i-Demo documentation confirms a pattern where "the client connects their data systems to the structuring engine" and "data is indexed on the client's end."

A private deployment model would look as follows:

```
+-------------------------------------------------+
|        MHRA Secure Environment                   |
|        (MHRA-controlled infrastructure)          |
|                                                  |
|   +-------------------------------------------+ |
|   |  ArcaScience Models (deployed on-prem)    | |
|   |  - SLMs for extraction & normalization     | |
|   |  - Configured pipelines for MHRA use case  | |
|   +-------------------------------------------+ |
|                                                  |
|   +-------------------------------------------+ |
|   |  MHRA Data Sources                        | |
|   |  - Yellow Card (Tier 3)                   | |
|   |  - Internal assessments (Tier 3)          | |
|   |  - Licensed databases (Tier 2)            | |
|   +-------------------------------------------+ |
|                                                  |
|   All processing occurs within MHRA boundary.    |
|   No data egress. MHRA retains full control.     |
+-------------------------------------------------+
```

**Key properties**:
- ArcaScience models are deployed into MHRA's environment
- All data remains within MHRA's infrastructure boundary
- No data transmitted to ArcaScience servers
- MHRA IT controls access, networking, and audit logging
- ArcaScience provides model artifacts and configuration support only

**Important caveat (TBD)**: While ArcaScience has described this client-side deployment model in general terms and demonstrated it with pharmaceutical clients (e.g., Sanofi preclinical data), the specific requirements for an air-gapped or fully isolated UK government deployment have not been documented. The following remain open items:

- Whether ArcaScience models can operate fully air-gapped (no outbound connectivity)
- Containerization and deployment packaging for MHRA's specific infrastructure
- Licensing model for on-premises deployment
- Ongoing model update and maintenance procedures in an isolated environment

These items would need to be scoped during a formal technical assessment phase, after the PoC has demonstrated value.

---

## 4. Handling Large Real-World Data Sources (The CPRD Pattern)

CPRD (Clinical Practice Research Datalink) represents the most data-intensive scenario raised in the meeting: 30 million patient records spanning 30 years. Allison stated plainly: "We couldn't use that data source" in the context of sharing it externally.

### Proposed Approach: In-Place Query Model

Rather than extracting or transmitting CPRD data, the approach would follow a "bring the algorithm to the data" pattern:

```
+-------------------------------------------------+
|        MHRA Secure Environment                   |
|                                                  |
|   +-------------------------------------------+ |
|   |  CPRD Data Store                          | |
|   |  (30M patients, 30 years)                 | |
|   +-------------------------------------------+ |
|              |                                   |
|              v                                   |
|   +-------------------------------------------+ |
|   |  ArcaScience Extraction Models            | |
|   |  (deployed within MHRA boundary)          | |
|   |  - Process data in-situ                   | |
|   |  - Extract aggregated, de-identified       | |
|   |    statistical summaries only              | |
|   +-------------------------------------------+ |
|              |                                   |
|              v                                   |
|   +-------------------------------------------+ |
|   |  Derived Aggregates Only                  | |
|   |  - No patient-level data extracted         | |
|   |  - Statistical summaries, counts, rates   | |
|   |  - Usable within BRA workflow              | |
|   +-------------------------------------------+ |
+-------------------------------------------------+
```

**Design principles for CPRD integration**:

1. **In-situ processing**: ArcaScience models are deployed inside the secure environment that hosts CPRD. Models query the data; data does not move.
2. **Aggregate outputs only**: The models produce de-identified, statistical-level summaries (incidence rates, relative risks, confidence intervals). No patient-level records are extracted or surfaced.
3. **Connector pattern**: ArcaScience has documented connector patterns for integrating private data sources (i-Demo: "client connects their data systems to the structuring engine"). A CPRD-specific connector would follow this pattern.
4. **MHRA controls the query scope**: MHRA assessors define the query parameters (drug, event, population). ArcaScience models execute the extraction. MHRA reviews the aggregate output.

**Critical TBDs for CPRD integration**:

- [ ] CPRD-specific connector has NOT been built; this is a future engineering effort
- [ ] Data schema mapping between CPRD's structure and ArcaScience's ingestion pipeline is undefined
- [ ] Performance characteristics of running SLMs against a dataset of this scale (30M patients) are untested
- [ ] CPRD has its own governance framework; any integration would require CPRD's independent approval
- [ ] Whether MHRA's CPRD access terms permit running third-party algorithms against the data is unknown

**Recommendation**: CPRD integration should be treated as a Phase 2+ objective, investigated only after the public-domain PoC has established trust and demonstrated model utility. It should not be discussed as a near-term deliverable.

---

## 5. Security Controls & Compliance

### 5.1 Documented ArcaScience Security Capabilities

The following security measures are documented in ArcaScience's IT Roadmap (January 2026) and public materials:

| Control | Implementation | Source |
|---|---|---|
| **Authentication** | Keycloak with OAuth 2.0 and OpenID Connect | IT Roadmap: BRA Platform Global Architecture |
| **Authorization** | JWT-based authentication with Role-Based Access Control (RBAC) | IT Roadmap: BRA Platform Global Architecture |
| **API security** | API rate limiting and request throttling | IT Roadmap: BRA Platform Global Architecture |
| **Data storage** | S3 storage for client data, PostgreSQL for primary database | IT Roadmap: Software Architecture |
| **Caching and queuing** | Redis for session management, job queues, query caching, rate limiting | IT Roadmap: BRA Platform Global Architecture |
| **Monitoring** | Comprehensive logging and monitoring with structured logs | IT Roadmap: BRA Platform Global Architecture |
| **Infrastructure** | 100% Kubernetes on AWS (migrated from Azure in 2025) | IT Roadmap: 2025 Retrospective |
| **Real-time updates** | WebSocket-based notifications for project updates | IT Roadmap: BRA Platform Global Architecture |

### 5.2 Claimed Certifications and Standards

The following certifications are referenced in ArcaScience's public-facing materials (website, deck):

| Certification / Standard | Status | Notes |
|---|---|---|
| **ISO 27001** | Claimed on website | Information security management; independent verification status not confirmed in reviewed materials |
| **GDPR** | Claimed on website | European data protection compliance |
| **FDA 21 CFR Part 11** | Claimed on website and deck ("FDA-Compliant Documentation") | Electronic records and signatures; relevant for regulatory document generation |
| **HIPAA** | Claimed on website | US healthcare data protection |
| **HDS (Hebergeur de Donnees de Sante)** | Claimed on website | French health data hosting certification |

**Important note**: The claims above are sourced from ArcaScience's own materials. Independent audit reports or certification documents have not been reviewed as part of this assessment. MHRA should request copies of relevant certificates and audit reports during any formal evaluation.

### 5.3 Additional Controls MHRA May Require (TBD)

MHRA, as a UK government body handling sensitive health data, is likely to require compliance with standards beyond those currently documented by ArcaScience:

| Requirement | Description | ArcaScience Status |
|---|---|---|
| **Cyber Essentials Plus** | UK government baseline cybersecurity certification, typically required for suppliers handling sensitive data | **TBD** -- not documented in reviewed materials |
| **NHS Data Security and Protection Toolkit (DSPT)** | Standard for organizations processing NHS or health data in the UK | **TBD** -- not documented |
| **UK GDPR (post-Brexit specific provisions)** | Compliance with the UK's own implementation of GDPR under the Data Protection Act 2018 | **TBD** -- ArcaScience references EU GDPR; UK-specific provisions not addressed |
| **Crown Commercial Service (CCS) framework** | Procurement framework for UK government technology suppliers | **TBD** -- not documented |
| **UK Government Cloud (G-Cloud) listing** | Marketplace for cloud services approved for UK government use | **TBD** -- not documented |
| **Data Protection Impact Assessment (DPIA)** | Required for processing that is likely to result in high risk to individuals | **TBD** -- would need to be conducted jointly |
| **Supply chain security assurance** | NCSC supply chain security guidance | **TBD** -- not documented |
| **Data residency** | Whether data must remain in UK-based data centers | **TBD** -- ArcaScience uses AWS; specific region configuration not documented |

**Recommendation**: ArcaScience should proactively engage with MHRA's IT security and information governance teams to obtain the full list of required certifications and controls before any deployment involving MHRA data or infrastructure access.

---

## 6. PoC-First Approach: Why Public Domain Data First

The public-domain proof of concept is not a compromise -- it is the strategically correct starting point. It eliminates all confidentiality risk while simultaneously proving (or failing to prove) the platform's utility for MHRA's core work.

### 6.1 Confidentiality Benefits

| Risk | Status with Public-Domain PoC |
|---|---|
| Patient data exposure | **Eliminated** -- no patient data involved |
| Ongoing safety issue leaked | **Eliminated** -- only historical, published issues used |
| MHRA internal assessments shared | **Eliminated** -- MHRA compares outputs internally without sharing their assessment |
| CPRD data accessed by external party | **Eliminated** -- CPRD not involved |
| Regulatory independence compromised | **Eliminated** -- MHRA evaluates the tool; the tool does not make decisions |

### 6.2 Alignment with MHRA's Own Proposal

Allison stated in the meeting: "The only thing I'm thinking about is whether we could look at a safety issue that's already in the public domain that we've already reported on." The public-domain PoC directly implements this suggestion.

### 6.3 What the PoC Proves

Even without any MHRA data, the PoC can demonstrate:

1. **Comprehensiveness**: Does ArcaScience surface safety signals and evidence that MHRA's own assessors identified, using only public data?
2. **Incremental value**: Does ArcaScience surface additional relevant evidence that the original assessment did not include?
3. **Data quality handling**: How does the platform handle observational studies, meta-analyses, and literature of variable quality -- the exact challenge Allison raised?
4. **Structured output**: Does the output format (templated documents, stratified data) align with MHRA's workflow?
5. **Auditability**: Can MHRA trace every output back to its source document and understand the extraction logic?

### 6.4 Decision Gate

After the PoC, MHRA faces a simple decision tree:

```
PoC Result
    |
    +-- Output matches or exceeds MHRA's own assessment
    |       |
    |       +-- Proceed to Phase 2 discussion
    |           (private deployment scoping, security assessment)
    |
    +-- Output is incomplete or inaccurate
            |
            +-- No further investment of MHRA time or resources
                (no data was shared, no harm done)
```

This structure ensures that MHRA invests minimal resources and takes zero confidentiality risk before deciding whether deeper engagement is warranted.

---

## 7. Open Items and TBDs

The following items are explicitly unresolved and must be addressed before any engagement beyond the public-domain PoC:

| Item | Category | Required For | Owner |
|---|---|---|---|
| MHRA-specific IT security requirements | Security | Any deployment touching MHRA infrastructure | MHRA IT / InfoSec |
| UK government cloud certifications (Cyber Essentials Plus, G-Cloud, DSPT) | Compliance | Any formal vendor relationship with MHRA | ArcaScience |
| UK GDPR / Data Protection Act 2018 compliance specifics | Legal | Any processing of UK-origin data | ArcaScience Legal |
| Air-gapped deployment capabilities | Engineering | Tier 3 data integration | ArcaScience Engineering |
| CPRD connector development and testing | Engineering | CPRD integration (Phase 2+) | ArcaScience Engineering |
| CPRD governance approval for third-party algorithm execution | Governance | CPRD integration (Phase 2+) | MHRA / CPRD |
| Data residency (UK-based hosting) | Infrastructure | Any deployment processing UK health data | ArcaScience DevOps |
| Independent verification of ISO 27001, GDPR, and other certifications | Compliance | Formal vendor assessment | ArcaScience / MHRA Procurement |
| On-premises licensing and support model | Commercial | Private deployment | ArcaScience Commercial |
| Model update and maintenance procedures for isolated environments | Operations | Private deployment | ArcaScience Engineering |
| Data Protection Impact Assessment (DPIA) | Legal/Regulatory | Any processing involving personal data | Joint (MHRA + ArcaScience) |
| Memorandum of Understanding (MoU) or collaboration agreement | Legal | Formalizing the PoC engagement | Joint (MHRA Legal + ArcaScience Legal) |

---

## Summary

The confidentiality framework for MHRA engagement rests on three principles:

1. **Start with zero data sharing.** The public-domain PoC uses only openly available information. MHRA shares nothing. ArcaScience proves its value -- or does not -- without any confidentiality exposure.

2. **Classify data rigorously.** The three-tier model (Public / Licensed / MHRA-Internal) creates clear rules for what data can be processed, where, and under what conditions. Tier 3 data never leaves MHRA.

3. **Defer what is not yet built.** ArcaScience has described client-side deployment capabilities and has demonstrated them with pharmaceutical clients. However, specific MHRA requirements (air-gapped deployment, UK government certifications, CPRD integration) have not been engineered or certified. These items are honestly marked as TBD and should be addressed only after the PoC has established whether deeper collaboration is worth pursuing.

This approach respects MHRA's stated constraints, avoids overclaiming ArcaScience's current capabilities, and provides a clear, low-risk path to evaluating whether the platform has genuine utility for post-authorization safety work.
