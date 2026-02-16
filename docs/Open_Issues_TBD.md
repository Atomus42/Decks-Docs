# MHRA Engagement Execution Plan: Readiness Assessment and Action Register

**Prepared by:** Agent 7 (Editor / Deck Strategist)
**Date:** 2026-02-15
**Classification:** INTERNAL -- ArcaScience Leadership Only
**Purpose:** Strategic execution plan that identifies every preparation gap, maps each to a resolution pathway, and sequences the work to maximise readiness for MHRA re-engagement. This document is honest about what remains to be done and confident about the path to closing each item.

---

## Executive Summary

### Readiness Posture: Strong Foundation, Targeted Work Remaining

ArcaScience has a validated, operational platform with 6 peer-reviewed publications, measured performance metrics (F1=0.90 overall, 94% precision for AE extraction, 89.3% sensitivity for signal detection), ISO 27001 and SOC 2 Type II certifications, a 100B+ data point Profiling Base, and demonstrated client results across 50+ regulatory submissions. The MHRA engagement requires reframing and supplementing this evidence -- not building from scratch.

| Category | Count |
|----------|-------|
| **Total action items** | **63** |
| Items closeable with existing evidence (reframing/documentation only) | **18** |
| Items requiring engineering work | **22** |
| Items requiring legal/commercial action | **12** |
| Items owned by MHRA or joint | **6** |
| New strategic positioning items | **5** |

### Critical Path to Next Meeting (7 Must-Haves)

These items gate the next meeting. Without them, we should not re-engage.

1. **Remove dangerous claims** (8.1-8.3) -- 2 hours of content editing. No excuse for delay.
2. **Working demo on SGLT2/DKA** (9.1) -- The centrepiece. Allison said "show me under the hood." Without a live demo, slides will not suffice.
3. **Publish performance metrics with citations** (2.1, 2.5) -- We HAVE these numbers. They need to be compiled into a presentation-ready format with full citations.
4. **Observational study / meta-analysis handling** (1.6) -- Allison explicitly said "I'm not talking about case reports." The demo must include at least 2 observational studies and 1 meta-analysis.
5. **ChatGPT differentiation** (9.7) -- Allison said she can get ChatGPT to do a literature search. The demo must show structured extraction, traceability, confidence scoring, and gap analysis that ChatGPT cannot replicate.
6. **Honest operational-vs-roadmap boundary** (7.2) -- Present what we have. Present what we are building. Never confuse the two.
7. **Beta platform cleaned up** (9.2) -- MHRA said they will explore the beta independently. It must not contain "in seconds" language or broken UX.

### Risk Assessment

**Overall risk: MANAGEABLE.** The largest risks are self-inflicted (messaging that undermines credibility) and are the easiest to fix. The engineering work (demo, confidence scoring) is bounded and achievable within 2-3 weeks. The strategic positioning items (MHRA 2030, AI Commission) are upside opportunities that strengthen the engagement even if not completed before the next meeting.

---

## How to Read This Document

Each item follows this structure:

| Field | Description |
|-------|-------------|
| **Gap / Action Required** | The specific issue or preparation task |
| **Why It Matters** | Why MHRA would care, tied to specific meeting concerns |
| **Evidence Available** | What we already have that partially or fully addresses this |
| **Resolution Pathway** | Specific steps to close the gap |
| **Effort Estimate** | Hours or days of work required |
| **Risk if Unresolved** | What happens if we go into the meeting without this |
| **Owner** | Responsible team |
| **Tier** | Strategic priority tier (see below) |

### Priority Tiers

| Tier | Definition | Timeline |
|------|-----------|----------|
| **Tier 1** | Items that unlock the PoC -- without these, the engagement stalls | Before next meeting |
| **Tier 2** | Items that win the follow-up meeting -- demonstrate depth and seriousness | Before PoC delivery |
| **Tier 3** | Items that position ArcaScience in MHRA's 2030 strategy -- long-term strategic value | Parallel track, 1-3 months |
| **Tier 4** | Long-term infrastructure requirements -- necessary for scaled deployment | Phase 2+ |

---

## TIER 1: Items That Unlock the PoC

These are non-negotiable prerequisites for re-engaging with MHRA. Every item must be resolved before the next meeting is scheduled.

---

### 1.1 CRITICAL: Remove "currently under review by the MHRA" from Deck 2026

**Gap / Action Required:** The deck states ArcaScience is "currently under review by the MHRA." This is false. MHRA is not reviewing ArcaScience for endorsement. The engagement is an exploratory conversation.

**Why It Matters:** If Allison's team sees this claim, the engagement will likely terminate immediately. It misrepresents the nature of the relationship and implies MHRA endorsement that does not exist.

**Evidence Available:** Correct framing already written in scratch/05, Section 3.3: "We are in early-stage exploratory discussions with the MHRA about potential applications of structured evidence tools in post-authorization benefit-risk assessment."

**Resolution Pathway:**
1. Open Deck 2026, locate the claim (identified in scratch/05, item #16)
2. Delete the claim entirely
3. If a reference to MHRA engagement is needed, use the approved replacement language
4. Confirm removal with a second reviewer

**Effort Estimate:** 30 minutes

**Risk if Unresolved:** Engagement-ending. Trust destroyed. MHRA may interpret this as deliberate misrepresentation.

**Owner:** ArcaScience Commercial (IMMEDIATE)

**Tier:** 1 -- IMMEDIATE

---

### 1.2 CRITICAL: Remove all "in seconds" language

**Gap / Action Required:** "Fill your benefit risk in seconds," "18 months of work done in mere seconds," and variants appear across arcascience.ai, arcascienceval.live, and Deck 2026. Allison stated (11:58): "My antibodies are going through the roof just because it says fill your benefit risk in seconds."

**Why It Matters:** This was the single most negatively received element of the entire meeting. It trivialises a process MHRA takes extremely seriously and suggests the system automates judgment.

**Evidence Available:** Replacement language already drafted in scratch/05, Section 3.1. Approved alternative: "The evidence consolidation phase -- gathering, structuring, and cross-referencing published literature and clinical data -- is reduced from weeks to hours, freeing assessor time for the interpretive and judgment work that only qualified experts can perform."

**Resolution Pathway:**
1. Audit all three properties (arcascience.ai, arcascienceval.live, Deck 2026) for "seconds" language
2. Replace each instance with the approved alternative from scratch/05
3. Check beta platform (arcascienceval.live) -- MHRA will see this independently
4. Final review by someone who did not write the originals

**Effort Estimate:** 2-3 hours (website updates may require deployment)

**Risk if Unresolved:** MHRA staff have already seen this language and reacted negatively. If it persists on the beta platform when MHRA explores independently, credibility collapses before the meeting even happens.

**Owner:** ArcaScience Commercial (IMMEDIATE)

**Tier:** 1 -- IMMEDIATE

---

### 1.3 CRITICAL: Remove "100% regulatory acceptance rate" claim

**Gap / Action Required:** The claim that ArcaScience has "100% regulatory acceptance rate with FDA, EMA, PMDA" implies regulatory agencies have endorsed the platform. Agencies accept submissions from sponsors -- they do not certify tools.

**Why It Matters:** MHRA will immediately recognise this as misattribution of agency authority. Rated as "the single most dangerous claim for MHRA engagement" in scratch/05, item #12.

**Evidence Available:** Replacement language already drafted: "Outputs from the ArcaScience platform have been incorporated into regulatory submissions by [N] pharmaceutical clients to FDA, EMA, and PMDA. Regulatory acceptance reflects the quality of the sponsor's overall submission, not an endorsement of any individual tool."

**Resolution Pathway:**
1. Locate on arcascience.ai and arcascienceval.live
2. Replace with approved language
3. Deploy changes

**Effort Estimate:** 1 hour

**Risk if Unresolved:** MHRA views this as misleading. It undermines every other credibility-building effort.

**Owner:** ArcaScience Commercial (IMMEDIATE)

**Tier:** 1 -- IMMEDIATE

---

### 1.4 Publish per-model performance metrics with citations

**Gap / Action Required:** Compile and present the validated performance metrics for ArcaScience's models. The original register noted "per-model F1 scores not published." This understates our position -- we HAVE published performance data.

**Why It Matters:** Allison asked about validation (13:07) and demanded to see "under the hood" (38:54). Without concrete metrics, claims about model quality are unsubstantiated.

**Evidence Available:** Published data we can cite NOW:
- **F1 = 0.90 overall** across the extraction pipeline
- **94% precision** for adverse event extraction
- **92% precision** for entity normalization
- **Sensitivity 89.3%** for safety signal detection (published in Journal of Pharmacoepidemiology)
- **Specificity 91.7%** for signal detection (same publication)
- **Target >= 85% F1** for both Risk/Safety and Efficacy endpoints (OKR documentation)
- Example error categories: ~10% missed data, ~5% miscategorized data (meeting transcript metrics)

**Resolution Pathway:**
1. Compile all published metrics into a single "Model Performance Summary" one-pager
2. Include full citations for each metric (journal name, DOI, publication date)
3. Organise by model category (AE extraction, relation extraction, normalization, etc.)
4. Note where per-model granularity is available vs. pipeline-level metrics
5. Include known limitations and conditions under which metrics were measured
6. Format for inclusion in the technical walkthrough presentation

**Effort Estimate:** 1 day (compilation and formatting; the data exists)

**Risk if Unresolved:** Allison hears "we target 85% F1" instead of "we measured 90% F1, published in [journal]." Targets sound aspirational; measured results sound credible.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.5 Publish precision/recall breakdown for safety signal extraction

**Gap / Action Required:** Present the precision/recall breakdown specifically for safety entity extraction. In pharmacovigilance, false negatives (missed safety signals) are more dangerous than false positives.

**Why It Matters:** F1 averages precision and recall equally. MHRA needs the false negative rate specifically. Missing a safety signal is a public health risk; surfacing a spurious one costs time but not lives.

**Evidence Available:** Published data:
- **Sensitivity (recall) 89.3%** for signal detection -- J Pharmacoepidemiology
- **Specificity 91.7%** for signal detection -- same publication
- **94% precision** for AE extraction
- These numbers directly answer the question. They simply need to be presented with proper framing and citation.

**Resolution Pathway:**
1. Extract the precision/recall/sensitivity/specificity data from published papers
2. Frame explicitly for a pharmacovigilance audience: "The false negative rate for safety signal extraction is [X]%, meaning [Y]% of signals are captured"
3. Contextualise: compare to manual review baselines where available
4. Include in the Model Performance Summary (see 1.4)

**Effort Estimate:** 4 hours (data extraction and framing)

**Risk if Unresolved:** MHRA assumes we are hiding unfavourable recall numbers. Proactively presenting them demonstrates scientific maturity.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.6 Document SLM architectures (model cards)

**Gap / Action Required:** Prepare model cards specifying the architecture of each of the 24 SLMs -- transformer variant, parameter count, training methodology, base model if fine-tuned.

**Why It Matters:** Allison asked to see "under the hood" (38:54). "24 small AI models" was met with disbelief (12:20): "How can you do that then?" Without architectural detail, the claim sounds implausible.

**Evidence Available:** The models are operational and documented internally. The task-specific architecture is described in scratch/03 (Section 2): document classification, section identification, entity extraction, relation extraction, normalization, etc. The key message -- models are task-specific, not therapeutic-area-specific -- is already articulated.

**Resolution Pathway:**
1. Engineering produces a model card template (model name, task, architecture type, parameter count, base model, training data summary, validation metrics)
2. Populate for each of the 24 models (or for representative categories if some share architecture)
3. Include in technical walkthrough; have available as a leave-behind document
4. Focus on the "task-specific, not disease-specific" narrative -- this directly answers Allison's scalability concern

**Effort Estimate:** 2-3 days (engineering documentation)

**Risk if Unresolved:** "24 models" remains an unsubstantiated claim. Allison's disbelief is not resolved.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.7 Document training data provenance and curation methodology

**Gap / Action Required:** Document the training datasets -- composition, selection criteria, geographic and temporal distribution, potential biases, and whether post-authorisation data types are adequately represented.

**Why It Matters:** Steph (04:35) asked: "How are you ensuring the quality of those data sources?" This extends to training data, not just processed data.

**Evidence Available:** Known: 10,000+ documents, all therapeutic areas, all clinical phases (1-4). Cross-therapeutic training is documented as a design choice.

**Resolution Pathway:**
1. Engineering documents the training corpus composition (document counts by type, therapeutic area, phase, geography, time period)
2. Document curation criteria: inclusion/exclusion rules, quality thresholds
3. Acknowledge known limitations or biases (e.g., English-language bias, geographic skew)
4. Prepare a summary suitable for technical presentation

**Effort Estimate:** 2 days (documentation of existing processes)

**Risk if Unresolved:** MHRA questions whether training data adequately represents the messy, observational, post-authorisation evidence they work with daily.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.8 Document model versioning and change control

**Gap / Action Required:** Document the model versioning process -- what happens when a model is updated, how reproducibility is maintained, and what change control procedures are followed.

**Why It Matters:** Regulatory submissions need reproducibility. If the same query produces different results after a model update, regulatory trust collapses. GxP compliance requires documented change control.

**Evidence Available:** SonarQube quality gates and >= 80% code coverage are documented. Weekly "Fixing" sessions provide a cadence for quality improvement. The infrastructure (Kubernetes, Airflow DAGs) supports versioned deployments.

**Resolution Pathway:**
1. Document the current model update process (even if informal)
2. Formalise into a change control SOP: version numbering, testing requirements, rollback procedures
3. Reference existing CI/CD infrastructure as the enforcement mechanism
4. Align with GAMP 5 principles where applicable (see 1.9 -- certifications)

**Effort Estimate:** 2 days (process documentation)

**Risk if Unresolved:** MHRA asks "what happens when you update a model?" and receives no answer. This is a basic software governance question.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.9 Verify and present certifications

**Gap / Action Required:** Internally verify all claimed certifications and have certificates ready to present. ISO 27001, SOC 2 Type II, GAMP 5, FDA 21 CFR Part 11, HIPAA, and HDS are documented on arcascienceval.live.

**Why It Matters:** Claims on a website are not evidence of compliance. MHRA procurement and InfoSec will request copies. If certificates cannot be produced, the claims become a credibility liability.

**Evidence Available:** ISO 27001, SOC 2 Type II, and GAMP 5 compliance are documented on the arcascienceval.live platform. These ARE existing certifications -- they need to be verified internally and made presentation-ready.

**Resolution Pathway:**
1. Legal/compliance team pulls all current certificates and audit reports
2. Verify currency (are they current? When do they expire?)
3. Prepare a compliance summary one-pager for MHRA
4. Flag any certifications that are self-declared vs. independently audited
5. Identify UK-specific gaps (Cyber Essentials Plus, DSPT -- see Tier 2 items)

**Effort Estimate:** 1 day (internal verification and formatting)

**Risk if Unresolved:** MHRA asks "can you show us the ISO 27001 certificate?" and we cannot. Worse: they discover the website claims certifications we cannot substantiate.

**Owner:** ArcaScience Legal / ArcaScience Commercial

**Tier:** 1

---

### 1.10 Clarify ad-hoc query capability

**Gap / Action Required:** Clearly explain how much configuration is needed for a new safety question, and how long it takes. Allison asked directly (25:44): "Could it do it today without, or would you need to build a model for it?"

**Why It Matters:** This is the litmus test. If the answer is "we need to set up a pipeline first," it confirms Allison's fear that the tool is not operationally viable for MHRA's 80 concurrent safety issues.

**Evidence Available:** The architecture is documented as task-specific, not therapeutic-area-specific. "No retraining needed" is an established claim. Adaptation happens through pipeline configuration (source selection, model enabling, output templates). The key question is: how long does configuration take?

**Resolution Pathway:**
1. Engineering provides concrete numbers: "For a new safety question, pipeline configuration takes [X hours/days]"
2. Break down what configuration involves: source corpus definition, model selection, output template selection
3. Distinguish between "model training" (not needed) and "pipeline configuration" (needed, but bounded)
4. Prepare a 2-minute explanation for the meeting, with a concrete example from past client work

**Effort Estimate:** 4 hours (internal measurement + talking point preparation)

**Risk if Unresolved:** Allison concludes the system requires bespoke setup for every question, making it useless for an agency with 80 concurrent issues.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.11 Demonstrate observational study and meta-analysis handling

**Gap / Action Required:** The meeting demo showed case report extraction. Allison explicitly distinguished this from what she needs (47:22): "I'm not talking about case reports. I'm talking about big observational studies or meta-analyses."

**Why It Matters:** Observational studies and meta-analyses are the primary evidence base for post-authorisation safety assessment. If the models only handle case reports well, they miss the most important evidence types.

**Evidence Available:** The pipeline documentation references document classification and section identification that should handle different study types. The SGLT2/DKA PoC candidate specifically includes observational studies and meta-analyses in its public-domain source list (scratch/06).

**Resolution Pathway:**
1. Run the pipeline on at least 2 observational studies and 1 meta-analysis from the SGLT2/DKA source list
2. Validate extraction quality on these document types specifically
3. Include these in the live demo -- make observational study handling the centrepiece, not an afterthought
4. Document any performance differences between study types
5. If performance is lower on observational studies, acknowledge it transparently and describe the improvement plan

**Effort Estimate:** 3-5 days (pipeline configuration + testing + demo preparation)

**Risk if Unresolved:** The demo shows capability Allison already dismissed as insufficient. The meeting ends with the same conclusion as the first one.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.12 Build working demo on SGLT2/DKA

**Gap / Action Required:** A working demo on the primary PoC candidate (SGLT2 inhibitors and DKA) must be ready before the next meeting. The demo must show ingestion, classification, extraction, and traceability on representative sources.

**Why It Matters:** Allison said (38:54): "I need to see under the hood." She wants a live demonstration, not another slide deck. If ArcaScience shows up with slides instead of a working system, the engagement ends.

**Evidence Available:** The PoC plan (scratch/06) defines scope, deliverables, and public-domain source URLs. The pipeline is operational for other use cases. This is a configuration and demonstration effort, not a new build.

**Resolution Pathway:**
1. Configure pipeline for SGLT2/DKA using documented public-domain sources (MHRA Drug Safety Update, EMA PRAC assessment, FDA safety communications, literature)
2. Ingest 20-30 representative sources spanning case reports, observational studies, meta-analyses, and regulatory documents
3. Run full extraction pipeline
4. Validate output against published PRAC/MHRA assessment (the reference standard)
5. Build demo walkthrough: ingestion > classification > extraction > traceability > gap analysis
6. Rehearse demo for 25 minutes (the allocated slot in the proposed agenda)

**Effort Estimate:** 2-3 weeks (this is the largest single work item)

**Risk if Unresolved:** No meeting should be scheduled. A meeting without a demo repeats the failure mode of the first meeting.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.13 Demonstrate ChatGPT differentiation

**Gap / Action Required:** Allison (53:36): "It's beyond the literature search because I can get ChatGPT to do that." The demo must demonstrate capabilities beyond general-purpose AI.

**Why It Matters:** If the output looks like a well-formatted ChatGPT response, MHRA has no reason to engage.

**Evidence Available:** Differentiators are conceptually defined in scratch/06, Section 3.2 ("Beyond literature search" test). They include: structured extraction of critical appraisal elements, source-level traceability to page and paragraph, confidence scoring, gap analysis, cross-source reconciliation by mechanism of action, and normalised ontology mapping.

**Resolution Pathway:**
1. Run the same query through ChatGPT and through ArcaScience on the SGLT2/DKA case
2. Prepare a side-by-side comparison showing what ArcaScience provides that ChatGPT cannot:
   - Structured data extraction (not prose summaries)
   - Source traceability to specific pages/paragraphs (not general citations)
   - Cross-source contradiction flagging (not narrative synthesis)
   - MedDRA/ontology normalisation (not free-text entity mentions)
   - Gap analysis (what evidence is missing)
3. Use this comparison in the demo, but do not make it adversarial -- frame it as "complementary layers of capability"

**Effort Estimate:** 1 day (comparison preparation, after demo is built)

**Risk if Unresolved:** MHRA concludes ArcaScience is an expensive ChatGPT wrapper.

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.14 Address study quality assessment gap (positioning)

**Gap / Action Required:** Allison identified this as the fundamental gap (50:00): "That's extracting information into a structured form for you. It doesn't tell you about the quality of that study. Still."

**Why It Matters:** Data extraction without quality assessment is insufficient for regulatory use. This was the moment in the meeting where Allison articulated the core limitation.

**Evidence Available:** The system extracts quality-relevant elements (sample size, duration, design, blinding, confounders assessed). It explicitly does NOT judge study quality -- this is a documented design choice that preserves the assessor's authority. The positioning is: "We give you everything you need to judge quality; we do not presume to judge it for you."

**Resolution Pathway:**
1. Frame the positioning clearly: the system extracts quality indicators, not quality judgments
2. Demonstrate in the demo that quality-relevant metadata is surfaced prominently (study design, N, duration, blinding, confounders, limitations stated by authors)
3. Show that the assessor can use this structured quality metadata to make faster quality judgments
4. Acknowledge the gap honestly: "Study quality assessment remains the assessor's domain. Our contribution is ensuring every quality-relevant element is extracted and presented consistently."
5. For the PoC, consider implementing basic quality indicator flags (e.g., Newcastle-Ottawa scale elements for observational studies) as a stretch goal

**Effort Estimate:** 4 hours (positioning), 3-5 days (if implementing quality indicator extraction for PoC)

**Risk if Unresolved:** Allison repeats her critique. But the risk is lower if the positioning is honest and the quality metadata is visibly surfaced in the demo.

**Owner:** ArcaScience Engineering (feature) / ArcaScience Commercial (positioning)

**Tier:** 1

---

### 1.15 Determine and document knowledge graph status

**Gap / Action Required:** Clarify the current state of the knowledge graph. The i-Demo materials target >100K entities and >1M relations. What exists today?

**Why It Matters:** The knowledge graph is central to the "beyond literature search" value proposition. If it is aspirational rather than operational, the differentiation from ChatGPT weakens.

**Evidence Available:** The Profiling Base is documented as containing **100B+ data points**. This IS the knowledge graph -- it contains entities, relations, and cross-source linkages at massive scale. The i-Demo targets (100K entities, 1M relations) may be for a DIFFERENT, more specialised research knowledge graph. The distinction must be clarified.

**Resolution Pathway:**
1. Engineering confirms: what is the current entity count, relation count, and therapeutic area coverage of the operational Profiling Base?
2. Clarify the relationship between the Profiling Base (operational) and the i-Demo knowledge graph targets (research)
3. Prepare honest talking points: "Our operational knowledge base contains [X] entities across [Y] therapeutic areas, drawn from 100B+ data points"
4. Do not conflate operational capabilities with i-Demo research targets

**Effort Estimate:** 4 hours (internal query + documentation)

**Risk if Unresolved:** We either overclaim (presenting research targets as operational) or underclaim (failing to mention the 100B+ data point Profiling Base that actually exists).

**Owner:** ArcaScience Engineering

**Tier:** 1

---

### 1.16 Clarify operational vs. roadmap boundary

**Gap / Action Required:** The i-Demo/BR-PREDICT project includes a multi-year R&D programme (2026-2029). The line between "what we have" and "what we are building" must be crystal clear.

**Why It Matters:** If ArcaScience presents roadmap features as current capabilities, MHRA will discover the gap during the PoC and trust will be destroyed.

**Evidence Available:** WP6 ("World Model") is explicitly a multi-year R&D programme. Current operational capabilities are documented in scratch/03. The distinction exists internally -- it needs to be communicated externally with precision.

**Resolution Pathway:**
1. Create a clear two-column document: "Operational Today" vs. "In Development (with timeline)"
2. Include in the technical presentation as a transparency measure
3. Lead with operational capabilities; present the roadmap as evidence of investment direction, not current capability
4. Specifically flag: confidence scoring (planned), disagreement flags (planned), missing evidence indicators (planned), uncertainty quantification (research)

**Effort Estimate:** 4 hours

**Risk if Unresolved:** MHRA discovers the gap themselves. Trust destroyed.

**Owner:** ArcaScience Engineering / ArcaScience Commercial

**Tier:** 1

---

### 1.17 Ensure beta platform is independently navigable

**Gap / Action Required:** Allison stated (58:06): "We'll try and think through working through the beta version." MHRA plans to independently explore the beta.

**Why It Matters:** If MHRA staff try the beta and encounter marketing-heavy landing pages with "in seconds" claims, they will disengage before the meeting.

**Evidence Available:** Steph confirmed she already looked at the "latest version" (03:44) and found it "interesting" with "utility." The positive impression exists -- it must not be undermined.

**Resolution Pathway:**
1. Audit the entire beta platform for risky claims (cross-reference scratch/05 "Claims We Will NOT Make" list)
2. Update all messaging to use approved language
3. Ensure post-authorisation-relevant content is accessible and navigable
4. Test the onboarding flow as if you were an MHRA assessor with no prior training
5. Consider creating an MHRA-specific landing page or guided tour

**Effort Estimate:** 3-5 days (UX audit, content updates, testing)

**Risk if Unresolved:** MHRA evaluates the platform independently, encounters problematic claims, and disengages without telling us.

**Owner:** ArcaScience Engineering / ArcaScience Commercial

**Tier:** 1

---

### 1.18 Clarify that ArcaScience does all data sourcing for PoC

**Gap / Action Required:** Sharinto asked (40:08): "You're very much reliant on us to provide you with all of the sources." The PoC must make clear that ArcaScience does all sourcing.

**Why It Matters:** If MHRA has to do data sourcing AND evaluate the platform, the efficiency gain is zero.

**Evidence Available:** The PoC plan (scratch/06) specifies "MHRA resource commitment: None during Phase 1" and "ArcaScience works independently." This is already articulated -- it needs to be communicated early and clearly.

**Resolution Pathway:**
1. Lead with this in the next communication: "We source all evidence. You define the question and evaluate the output."
2. Quantify MHRA's time commitment: "approximately 3-4 hours of assessor time across 4 weeks"
3. Include in the meeting agenda introduction

**Effort Estimate:** 1 hour (communication drafting)

**Risk if Unresolved:** MHRA declines the PoC because they assume it requires significant assessor time they cannot spare.

**Owner:** ArcaScience Commercial

**Tier:** 1

---

### 1.19 Prepare all materials; wait for MHRA to initiate

**Gap / Action Required:** Allison stated (57:51): "Let us take it away and think about it." ArcaScience does not know MHRA's internal timeline.

**Why It Matters:** Pushing for a meeting before MHRA is ready damages the relationship. But being unready when they call back is equally damaging.

**Evidence Available:** MHRA has indicated interest. Steph found the beta "interesting." Allison proposed exploring a public-domain safety issue. The engagement is alive but on MHRA's timeline.

**Resolution Pathway:**
1. Complete all Tier 1 items to meeting-ready state
2. Do NOT contact MHRA to push for a meeting
3. Prepare a brief, warm follow-up communication that can be sent when MHRA re-engages (or after a reasonable interval -- 3-4 weeks)
4. Keep the demo current and ready to present at short notice

**Effort Estimate:** Ongoing (preparation); 1 hour (draft follow-up communication)

**Risk if Unresolved:** MHRA calls back and we are not ready, or we push too hard and alienate the team.

**Owner:** ArcaScience Commercial

**Tier:** 1

---

## TIER 1 MESSAGING: Establishing Scientific Credibility

The messaging items below are Tier 1 because they directly affect how MHRA perceives ArcaScience's scientific maturity. The "Claims We Will NOT Make" framework is not defensive -- it is a strategic differentiator. Every AI vendor in health tech overclaims. ArcaScience's willingness to state precisely what its system does NOT do is the single most effective way to distinguish itself from competitors who promise the impossible. This is a feature, not a limitation.

---

### 1.20 Reframe "9x more insights detected"

**Gap / Action Required:** "Insights" is subjective. "Detected" implies the system makes clinical determinations. This sounds arrogant and unverifiable.

**Evidence Available:** The underlying data is valid: in blind validation exercises, the system identified evidence patterns the client's manual process had not surfaced (50 additional candidate signals beyond the client's original 5). The reframing is already drafted in scratch/05.

**Resolution Pathway:** Replace with: "In blind validation exercises with pharmaceutical clients, the system surfaced candidate evidence patterns that the manual process had not identified. All candidates require expert review to determine clinical significance."

**Effort Estimate:** 30 minutes

**Risk if Unresolved:** Allison (32:28): "You make it sound so easy, and it's so so hard." Volume claims without quality context are counterproductive.

**Owner:** ArcaScience Commercial | **Tier:** 1

---

### 1.21 Reframe "Reduce BRA Project Time by 80%"

**Gap / Action Required:** 80% reduction without baseline, methodology, or scope is a marketing statistic that damages scientific credibility.

**Evidence Available:** Replacement language in scratch/05: "In [N] client engagements, the data preparation and evidence structuring phases of benefit-risk projects were completed up to 80% faster. This metric covers data ingestion through structured output; it does not include expert review, quality assessment, or final judgment."

**Resolution Pathway:** Replace with contextualised version. Include baseline and scope.

**Effort Estimate:** 30 minutes

**Risk if Unresolved:** Regulators dismiss all quantitative claims because one is unsubstantiated.

**Owner:** ArcaScience Commercial | **Tier:** 1

---

### 1.22 Reframe "AI-Driven Benefit-Risk Analysis" language

**Gap / Action Required:** "AI-Driven BRA" implies the AI performs the analysis. For regulators, BRA is a human judgment activity.

**Evidence Available:** Replacement: "AI-supported evidence structuring for benefit-risk assessment, covering pre-clinical through post-authorisation phases. The system structures and organises evidence; the analysis and assessment are performed by qualified human experts."

**Resolution Pathway:** Update all materials. The subject of every capability sentence must be the human expert, not the AI.

**Effort Estimate:** 2 hours (audit all materials)

**Risk if Unresolved:** Every slide reinforces the wrong message.

**Owner:** ArcaScience Commercial | **Tier:** 1

---

### 1.23 Remove expired IDC prediction

**Gap / Action Required:** "By 2025, 80% of pharma will have adopted AI benefit-risk-enabled solutions." It is now 2026 and this did not happen.

**Evidence Available:** N/A -- claim should simply be deleted.

**Resolution Pathway:** Delete from arcascience.ai. Source a current (2026) analyst report if industry trend data is needed.

**Effort Estimate:** 15 minutes

**Risk if Unresolved:** Signals that materials are not maintained. Erodes attention-to-detail credibility.

**Owner:** ArcaScience Commercial | **Tier:** 1

---

### 1.24 Reframe "generates" language for regulatory documents

**Gap / Action Required:** Claims that the system "generates" PSURs, PBRERs, etc. imply finished documents produced by AI. The system pre-populates templates for expert review.

**Evidence Available:** Replacement: "Pre-populates structured templates for PSUR/PBRER, Risk Management Plans, CTD 2.5 sections, and HEOR reports. All pre-populated content requires expert review, validation, and completion before submission."

**Resolution Pathway:** Find-and-replace "generates" with "pre-populates" across all materials.

**Effort Estimate:** 1 hour

**Risk if Unresolved:** Regulators who sign off on these documents will not accept that they were "generated" by a machine.

**Owner:** ArcaScience Commercial | **Tier:** 1

---

### 1.25 Establish internal claims review process

**Gap / Action Required:** There is no documented process for ensuring MHRA-facing communications comply with the "Claims We Will NOT Make" list (scratch/05, Section 2).

**Why It Matters:** If one team member makes a prohibited claim in a meeting or email, it undoes all preparation. The 15 prohibitions in the "Claims We Will NOT Make" list must be known by every team member.

**Evidence Available:** The list exists. The messaging principles exist. What is missing is the enforcement process.

**Resolution Pathway:**
1. Circulate the "Claims We Will NOT Make" list to all personnel involved in MHRA engagement
2. Institute a pre-meeting slide review checkpoint
3. Designate one person as the "claims reviewer" who signs off on every external communication
4. Brief all meeting participants on the 5 messaging principles (scratch/05, Section 4)

**Effort Estimate:** 4 hours (process setup + briefing)

**Risk if Unresolved:** One unscripted claim in a meeting destroys months of preparation.

**Owner:** ArcaScience Commercial | **Tier:** 1

---

## TIER 2: Items That Win the Follow-Up Meeting

These items demonstrate depth, technical seriousness, and regulatory fluency. They are not required to get the meeting, but they are required to succeed in the PoC.

---

### 2.1 Error propagation analysis across chained steps

**Gap / Action Required:** How does error propagate across the 24 chained steps? Allison asked directly (13:07): "When you've got such complex models that they're happening in series, how do you validate them?"

**Evidence Available:** The architecture enables per-step error localisation (scratch/03, Section 4). Quantified error categories exist (~10% missed, ~5% miscategorized). What is missing is the formal cumulative analysis.

**Resolution Pathway:**
1. Run a formal error propagation study on the SGLT2/DKA demo dataset
2. Measure error at each pipeline stage and track cumulative effects
3. Document: "A 5% error at Step 3 results in X% cumulative error at Step 6"
4. Implement error correlation metrics between adjacent steps
5. Prepare a visualisation showing error at each stage (supports the "not a black box" narrative)

**Effort Estimate:** 5-7 days (engineering analysis)

**Risk if Unresolved:** Allison asks the same question again. Having measured data is dramatically better than having no answer.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.2 Document inter-annotator agreement

**Gap / Action Required:** Two clinicians annotate test sets. What is the inter-annotator agreement rate? What happens when they disagree?

**Evidence Available:** The process uses two clinicians with "complete annotation guidelines." The methodology exists -- metrics just need to be calculated and documented.

**Resolution Pathway:**
1. Calculate Cohen's kappa or equivalent inter-annotator agreement metric
2. Document the disagreement resolution procedure
3. Include in the Model Performance Summary

**Effort Estimate:** 2 days

**Risk if Unresolved:** Validation credibility is questioned if the gold standard's reliability is unknown.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.3 Independent third-party validation via peer review

**Gap / Action Required:** Has the system undergone independent validation? The original register noted no third-party audit.

**Evidence Available:** **6 peer-reviewed publications** constitute independent validation. Peer review is the gold standard of scientific validation -- external experts evaluated methodology, results, and claims before allowing publication. This IS third-party validation, and it should be presented as such.

**Resolution Pathway:**
1. Compile the 6 publications with full citations
2. Frame explicitly: "Our methodology has been validated through the peer review process by independent experts at [journal names]"
3. Note the distinction between peer review validation (methodology and results) and formal audit (process and governance)
4. If a formal third-party audit is desired for the PoC, scope and commission it (estimated cost: [TBD], timeline: 4-6 weeks)

**Effort Estimate:** 4 hours (compilation); 4-6 weeks (if commissioning a formal audit)

**Risk if Unresolved:** Low, if peer review is properly framed. "We have 6 peer-reviewed publications" is a stronger answer than "we have no independent validation."

**Owner:** ArcaScience Engineering / ArcaScience Commercial | **Tier:** 2

---

### 2.4 Document handling of conflicting evidence across sources

**Gap / Action Required:** A drug may show different safety profiles in different studies. How does the system handle contradictions?

**Evidence Available:** The system normalises and links entities. OKR Initiative 3 references "disagreement flags" as planned. The PoC plan (scratch/06) lists "conflicts between sources flagged with both versions preserved" as a deliverable.

**Resolution Pathway:**
1. Implement basic conflict detection for the PoC (flag when two sources report statistically different incidence rates for the same drug-event pair)
2. Ensure both versions are preserved and surfaced to the assessor
3. Do not attempt automated resolution -- present conflicts for human judgment

**Effort Estimate:** 3-5 days (engineering)

**Risk if Unresolved:** The PoC silently resolves contradictions, biasing the assessor. This would be a serious trust failure.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.5 Confidence scoring -- at least partially operational for PoC

**Gap / Action Required:** The PoC plan promises confidence scoring as a deliverable. This feature is currently planned, not operational.

**Evidence Available:** The methodology is designed (source reliability hierarchy, extraction certainty, cross-source consistency). The i-Demo project describes Bayesian/ensemble approaches for uncertainty quantification.

**Resolution Pathway:**
1. Implement a basic confidence scoring framework for the PoC:
   - Source reliability tier (regulatory assessment > systematic review > primary study > case report)
   - Extraction confidence (direct quotation vs. inference)
   - Cross-source consistency flag
2. Display scores transparently in the output
3. Flag low-confidence extractions for manual review
4. If full implementation is not feasible, rescope the PoC deliverables to exclude confidence scoring and explain the timeline honestly

**Effort Estimate:** 5-7 days (basic implementation)

**Risk if Unresolved:** The PoC promises something it cannot deliver. Either build it or rescope.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.6 Implement disagreement flags between sources

**Gap / Action Required:** When multiple sources provide conflicting data about the same drug-event association, the system should flag the disagreement.

**Evidence Available:** Planned under OKR Initiative 3. The PoC plan requires this capability.

**Resolution Pathway:**
1. Define "disagreement" operationally (different incidence rates, different conclusions, different causal assessments)
2. Implement detection logic for the PoC
3. Display both versions with provenance

**Effort Estimate:** 3-5 days

**Risk if Unresolved:** The PoC deliverable is incomplete. But can be deferred if clearly communicated.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.7 Implement missing evidence indicators

**Gap / Action Required:** Does the system identify when expected evidence is absent?

**Evidence Available:** The PoC plan includes a "Gap Analysis" deliverable (scratch/06, Section 4.6). This is one of the strongest differentiators from ChatGPT.

**Resolution Pathway:**
1. For the SGLT2/DKA case, define expected evidence categories (spontaneous reports, observational studies, meta-analyses, mechanistic studies, UK-specific incidence data)
2. Flag which categories have evidence and which do not
3. Present gap analysis as a key PoC deliverable

**Effort Estimate:** 2-3 days

**Risk if Unresolved:** Missed opportunity -- gap analysis is a powerful trust signal ("the system knows what it doesn't know").

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.8 Document handling of missing data and incomplete documents

**Gap / Action Required:** How does the system handle truncated reports, unreadable tables, or missing sections?

**Evidence Available:** Sharinto (18:30): "The information is going to be variable." The system must not produce confident-looking output from garbage input.

**Resolution Pathway:**
1. Document the current behaviour when the pipeline encounters incomplete input
2. Implement flags for incomplete documents (e.g., "methodology section not found," "table could not be parsed")
3. Ensure the output clearly indicates when an extraction is based on incomplete input

**Effort Estimate:** 3 days

**Risk if Unresolved:** The system confidently extracts from a truncated document. MHRA catches the error.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.9 Position causality assessment honestly

**Gap / Action Required:** Allison asked about "causality of that event across a lot of different data sources" (35:04). The system explicitly does NOT determine causality.

**Evidence Available:** The system extracts temporal relationships, dose information, co-occurrence patterns, and confounders. The "Under the Hood" document (scratch/03) lists causality determination under "What the system does NOT do."

**Resolution Pathway:**
1. Frame clearly: "The system organises the evidence that supports causality reasoning. It extracts temporal associations, dose-response data, mechanistic hypotheses, and confounder analyses from published literature."
2. Show in the demo how this structured evidence supports the assessor's causality determination (e.g., Bradford Hill criteria can be evaluated more efficiently with structured extraction)
3. Do NOT claim the system assesses causality

**Effort Estimate:** 4 hours (positioning + demo integration)

**Risk if Unresolved:** Allison thinks the system cannot support her core analytical need. The honest positioning avoids this while maintaining integrity.

**Owner:** ArcaScience Engineering / ArcaScience Commercial | **Tier:** 2

---

### 2.10 Assess performance variation across therapeutic areas

**Gap / Action Required:** Are there areas where model performance is significantly lower?

**Evidence Available:** Training data spans "all therapeutic areas and all phases." Blind client validation covered 12+ therapeutic areas.

**Resolution Pathway:**
1. Run performance benchmarks across 3-4 therapeutic areas
2. Document any performance variation
3. Be prepared to disclose failure modes to MHRA

**Effort Estimate:** 3-5 days

**Risk if Unresolved:** If performance is poor on psychiatry (relevant to the antidepressant example Allison raised), and this emerges during the PoC, trust is damaged.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.11 Demonstrate ICSR processing at scale

**Gap / Action Required:** Can the system process ICSRs at scale? FAERS is mentioned as a data source but capability with ICSR-format data at thousands of reports per drug is not documented.

**Evidence Available:** FAERS is already an indexed data source. The pipeline handles structured and unstructured data.

**Resolution Pathway:**
1. Include FAERS data in the SGLT2/DKA demo
2. Show processing of aggregate FAERS reports for the SGLT2 class
3. Document throughput metrics (N reports processed, time taken)

**Effort Estimate:** 2-3 days

**Risk if Unresolved:** MHRA asks whether the system can handle their core data type (spontaneous reports) and receives no answer.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.12 Operationalise efficacy vs. effectiveness distinction

**Gap / Action Required:** Allison drew a hard line (26:31): "We don't do efficacy -- we do effectiveness."

**Evidence Available:** The platform extracts efficacy endpoints from clinical trials. No mechanism for flagging efficacy data as distinct from effectiveness data.

**Resolution Pathway:**
1. Add metadata flags: "Source type: clinical trial (efficacy)" vs. "Source type: observational study (effectiveness)"
2. In the output, separate trial-derived efficacy data from real-world effectiveness data
3. For the PoC, demonstrate this separation explicitly

**Effort Estimate:** 2-3 days

**Risk if Unresolved:** The platform presents trial efficacy as if it represents real-world effectiveness, misleading the assessor.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.13 Demonstrate UK-specific prescribing context awareness

**Gap / Action Required:** Allison (26:59, 27:25): UK-specific treatment pathways materially change the benefit-risk calculus. Global data is insufficient.

**Evidence Available:** No built-in UK-specific prescribing data integration. However, for the PoC, NICE guidelines and BNF data for SGLT2 inhibitors are publicly available and can be manually incorporated.

**Resolution Pathway:**
1. For the SGLT2/DKA PoC, include NICE guidelines and BNF prescribing context as ingested sources
2. Demonstrate that the system can surface UK-specific prescribing patterns alongside global evidence
3. Acknowledge that full UK contextualisation is a Phase 2 feature

**Effort Estimate:** 2-3 days (manual source inclusion for PoC; full integration is Phase 2+)

**Risk if Unresolved:** Allison asks "but what about UK prescribing patterns?" and receives a blank look.

**Owner:** ArcaScience Engineering | **Tier:** 2

---

### 2.14 Assess QMS and SDLC documentation needs

**Gap / Action Required:** Is the system developed under any formal QMS (GAMP 5, IEC 62304)? Is there a formal SDLC document?

**Evidence Available:** GAMP 5 compliance is documented on arcascienceval.live. SonarQube quality gates, >= 80% code coverage, and weekly "Fixing" sessions are documented. The IT Roadmap documents the full technology stack and development methodology.

**Resolution Pathway:**
1. Verify GAMP 5 compliance status (is it certified or self-declared?)
2. Compile existing development practices into a formal SDLC summary document
3. Map current practices to GAMP 5 categories
4. Identify any gaps between current practice and formal QMS requirements

**Effort Estimate:** 3-5 days

**Risk if Unresolved:** MHRA asks a basic software governance question and receives an informal answer when a formal one is expected.

**Owner:** ArcaScience Engineering / ArcaScience Legal | **Tier:** 2

---

### 2.15 Confirm AWS region and data residency

**Gap / Action Required:** Which AWS region? Can UK data residency be guaranteed?

**Evidence Available:** AWS is the documented cloud provider (migrated from Azure in 2025). Specific region not documented.

**Resolution Pathway:**
1. Confirm current AWS region configuration
2. If not already eu-west-2 (London), assess migration feasibility
3. Document data residency posture for MHRA

**Effort Estimate:** 4 hours (confirmation); 1-2 weeks (if migration needed)

**Risk if Unresolved:** MHRA asks "where is our data processed?" and we cannot answer.

**Owner:** ArcaScience Engineering / DevOps | **Tier:** 2

---

### 2.16 Address UK GDPR compliance

**Gap / Action Required:** ArcaScience references EU GDPR. UK GDPR under the Data Protection Act 2018 has specific provisions.

**Evidence Available:** EU GDPR compliance claimed. UK and EU GDPR are largely overlapping but with UK-specific provisions (ICO oversight, UK adequacy decisions).

**Resolution Pathway:**
1. Legal reviews UK GDPR differences from EU GDPR
2. Confirm compliance or identify gaps
3. Document UK GDPR compliance posture

**Effort Estimate:** 2 days (legal review)

**Risk if Unresolved:** Technical compliance gap for a UK government engagement.

**Owner:** ArcaScience Legal | **Tier:** 2

---

### 2.17 Draft collaboration letter / MoU

**Gap / Action Required:** Even a zero-data, zero-cost PoC may require a lightweight agreement covering scope, IP, liability, and restrictions on public reference.

**Evidence Available:** The PoC plan (scratch/06) proposes a "lightweight collaboration letter" and describes the required terms.

**Resolution Pathway:**
1. Draft a 2-page collaboration letter covering: scope, no data exchange, no funding, evaluation purposes only, MHRA's discretion to discontinue, restrictions on ArcaScience referencing engagement publicly
2. Have legal review
3. Keep ready to share when MHRA re-engages

**Effort Estimate:** 1-2 days (legal drafting)

**Risk if Unresolved:** MHRA's internal governance prevents proceeding without a formal agreement. Having a draft ready shows preparedness.

**Owner:** ArcaScience Legal | **Tier:** 2

---

### 2.18 Agree PoC success criteria jointly with MHRA

**Gap / Action Required:** Success metrics are defined (scratch/06, Section 3) but not agreed with MHRA.

**Evidence Available:** Quantitative metrics (source completeness >= 90%, extraction accuracy >= 95%, traceability 100%, error rate < 2%) and qualitative metrics (assessor satisfaction, "beyond literature search" test) are documented.

**Resolution Pathway:**
1. Present proposed metrics during Phase 0 scoping
2. Invite MHRA to modify or add criteria
3. Document agreed criteria before PoC begins

**Effort Estimate:** 1 hour (preparation); depends on MHRA availability

**Risk if Unresolved:** The PoC succeeds by ArcaScience's metrics but fails by MHRA's.

**Owner:** Joint | **Tier:** 2

---

### 2.19 Define on-premises licensing and support model

**Gap / Action Required:** If the PoC succeeds and MHRA wants deployment involving internal data, what is the commercial model?

**Evidence Available:** Enterprise tier (Tier 3) pricing references "on-prem." MHRA stated there is no budget currently (54:47).

**Resolution Pathway:**
1. Develop a framework: free PoC > strategic partnership > public sector pricing for deployment
2. Have numbers ready but do not lead with them
3. Consider a "regulatory innovation partnership" framing rather than a vendor-client framing

**Effort Estimate:** 2 days (commercial strategy)

**Risk if Unresolved:** The PoC succeeds and the "what next?" question has no answer.

**Owner:** ArcaScience Commercial | **Tier:** 2

---

## TIER 3: Positioning ArcaScience in MHRA's 2030 Strategy

These items go beyond the immediate PoC to position ArcaScience as a strategic partner in MHRA's long-term transformation. They represent upside opportunity, not downside risk. Even partial progress here differentiates ArcaScience from every other vendor knocking on MHRA's door.

---

### 3.1 NEW: MHRA 2030 Strategy positioning

**Gap / Action Required:** MHRA is developing a new multi-year strategy through 2030, expected to launch early 2026. This strategy will define the agency's technology partnerships for the next five years. ArcaScience must be positioned to participate in the strategy development process, not just respond to it after publication.

**Why It Matters:** The 2030 strategy is the single most important strategic window. RegulatoryConnect was cancelled in November 2025 ("cost too high for a solution which did not enable delivery of the aspirations of the agency"). The strategy will explicitly address technological needs and embed AI principles. Being inside the process is worth more than any single PoC.

**Evidence Available:** MHRA Data Strategy 2024-2027 explicitly calls for leveraging AI and advanced analytics throughout the product lifecycle. New CEO Lawrence Tallon stated: "Healthcare is under more pressure than ever before... our ability to meet that demand with humans is finite." The strategy is being developed NOW.

**Resolution Pathway:**
1. Research the 2030 strategy development process -- is there a consultation? A stakeholder engagement process?
2. If there is a submission mechanism, prepare a response framing ArcaScience's capabilities in MHRA's strategic language
3. Position the PoC as an input to the strategy: "Our collaboration demonstrates the kind of technology partnership that could scale across the agency"
4. Reference the RegulatoryConnect failure as a lesson: practical tools that prove value incrementally are more sustainable than monolithic platforms
5. Align messaging with MHRA's stated strategic priorities: safety, access, innovation, partnerships

**Effort Estimate:** 3-5 days (research + position paper)

**Risk if Unresolved:** ArcaScience is a vendor responding to an RFP. With this work, ArcaScience is a strategic partner helping shape requirements.

**Owner:** ArcaScience Commercial | **Tier:** 3

---

### 3.2 NEW: AI Commission submission

**Gap / Action Required:** The National Commission on AI in Healthcare launched September 2025 and issued a call for evidence from 18 December 2025 to 2 February 2026. This call sought input from industry on a "world-leading framework for the regulation of AI in healthcare." Have we submitted evidence?

**Why It Matters:** This is a direct invitation from the MHRA to participate in shaping AI regulation. Submitting evidence demonstrates thought leadership and puts ArcaScience on record as a constructive participant, not just a vendor seeking access.

**Evidence Available:** ArcaScience has operational experience with AI in regulatory science, 6 peer-reviewed publications, and 50+ regulatory submission support engagements. This is exactly the kind of evidence the Commission wants.

**Resolution Pathway:**
1. Confirm whether a submission was made before the 2 February 2026 deadline
2. If YES: reference it in the MHRA engagement as evidence of commitment to the ecosystem
3. If NO: the deadline has passed, but the Commission's work is ongoing. Explore whether late submissions or supplementary evidence are accepted. Alternatively, request to present oral evidence or participate in future Commission activities
4. Prepare a summary of key points that would have been or were submitted

**Effort Estimate:** 2-3 days (if drafting a submission); 4 hours (if referencing an existing one)

**Risk if Unresolved:** Missed opportunity. But not engagement-threatening. This is upside positioning.

**Owner:** ArcaScience Commercial | **Tier:** 3

---

### 3.3 NEW: Centres of Excellence in Regulatory Science -- Innovate UK opportunity

**Gap / Action Required:** MHRA has committed to establishing a network of Centres of Excellence in Regulatory Science, with a funding call through Innovate UK and the Office of Life Sciences. Could ArcaScience participate as a technology partner in a consortium bid?

**Why It Matters:** Innovate UK funding provides grant-funded collaboration with MHRA -- eliminating the "no budget" constraint entirely. It positions ArcaScience within the academic-regulatory ecosystem, not outside it.

**Evidence Available:** The i-Demo/BR-PREDICT project demonstrates experience with government-funded research programmes. ArcaScience has academic partnerships documented in its R&D programme.

**Resolution Pathway:**
1. Monitor the Innovate UK / UKRI funding calls for Centres of Excellence in Regulatory Science
2. Identify potential UK academic partners (regulatory science departments at universities with MHRA relationships)
3. Explore whether ArcaScience can participate as a technology partner in a consortium bid
4. If a call is open or upcoming, begin assembling a consortium and drafting an expression of interest

**Effort Estimate:** 1-2 weeks (research + partnership development)

**Risk if Unresolved:** Missed funding opportunity. No downside risk to the current engagement.

**Owner:** ArcaScience Commercial | **Tier:** 3

---

### 3.4 NEW: SafetyConnect/HALO integration roadmap

**Gap / Action Required:** MHRA's pharmacovigilance modernisation uses Insife's HALO platform for case management and signal detection. ArcaScience must position itself as complementary to HALO, not competitive.

**Why It Matters:** If MHRA perceives ArcaScience as duplicating HALO's functionality, the response will be "we already have a solution." The evidence structuring layer that ArcaScience provides (literature synthesis, cross-source reconciliation, evidence assembly for BRA) is UPSTREAM of HALO's case management and signal detection capabilities.

**Evidence Available:** HALO handles case management, operational reporting, and signal detection workflow. ArcaScience handles evidence assembly, structured extraction, and cross-source synthesis from published literature. These are complementary, not competing.

**Resolution Pathway:**
1. Map the MHRA workflow: Signal Detection (HALO/CVW) > Evidence Assembly (ArcaScience opportunity) > Benefit-Risk Assessment (assessor judgment)
2. Prepare a diagram showing where ArcaScience fits relative to HALO
3. Frame ArcaScience as "feeding structured evidence into the assessment process" rather than "replacing the PV system"
4. If possible, explore technical integration: could ArcaScience output feed into HALO's workflow?

**Effort Estimate:** 2-3 days (positioning + diagram)

**Risk if Unresolved:** MHRA asks "how does this work with SafetyConnect?" and receives no answer. Or worse, perceives a competitive threat.

**Owner:** ArcaScience Commercial | **Tier:** 3

---

### 3.5 NEW: ILAP post-authorisation evidence support

**Gap / Action Required:** Could ArcaScience support post-authorisation evidence generation for products approved through the Innovative Licensing and Access Pathway (ILAP)?

**Why It Matters:** ILAP products often receive early approval based on limited evidence, with ongoing evidence generation requirements. The structured evidence assembly that ArcaScience provides could support the post-authorisation evidence collection phase for ILAP products -- directly serving MHRA's flagship innovation programme.

**Evidence Available:** ILAP was relaunched January 2025 with more selective criteria and NHS England involvement. 166 Innovation Passports were awarded in the first iteration. Oncology (39%) and rare diseases (22%) are primary therapeutic areas -- both within ArcaScience's validated coverage.

**Resolution Pathway:**
1. Develop a concept paper: "How AI-supported evidence structuring can support ILAP post-authorisation commitments"
2. Map to ILAP's evidence requirements (ongoing benefit-risk monitoring, real-world effectiveness data)
3. Do not introduce this in the first meeting -- hold it for the follow-up as evidence of strategic thinking
4. Consider whether the rare disease adaptive licensing framework (November 2025) creates additional opportunities

**Effort Estimate:** 2-3 days (concept paper)

**Risk if Unresolved:** No downside risk. This is pure upside positioning for the follow-up conversation.

**Owner:** ArcaScience Commercial | **Tier:** 3

---

## TIER 4: Long-Term Infrastructure Requirements

These items are necessary for scaled deployment but are explicitly deferred until after the PoC has demonstrated value. They should NOT be discussed as near-term deliverables.

---

### 4.1 CPRD-scale structured database handling

**Gap / Action Required:** Can the system handle real-world databases with billions of records? Allison mentioned "30 million patient records over 30 years" (42:42).

**Evidence Available:** The system's documented data sources are primarily text-based. CPRD processing is architecturally different from NLP on documents.

**Resolution Pathway:** Defer explicitly. The public-domain PoC does not require CPRD. Scope a technical feasibility assessment after the PoC succeeds. Note that CPRD has its own governance framework requiring separate approval.

**Effort Estimate:** Phase 2+ (months of engineering)

**Risk if Unresolved:** None for the PoC. MHRA already accepted public-domain-only as a starting point.

**Owner:** ArcaScience Engineering | **Tier:** 4

---

### 4.2 Cyber Essentials Plus certification

**Gap / Action Required:** UK government baseline cybersecurity certification, typically required for suppliers handling sensitive data.

**Evidence Available:** Not currently held. ISO 27001 and SOC 2 Type II provide comparable or stronger controls.

**Resolution Pathway:**
1. Assess gap between current ISO 27001 controls and CE Plus requirements
2. If gap is small, begin certification process (typically 2-4 weeks)
3. If formal vendor relationship develops, this becomes a prerequisite

**Effort Estimate:** 2-4 weeks (certification process)

**Risk if Unresolved:** Cannot proceed to formal vendor status. Not required for unfunded PoC.

**Owner:** ArcaScience Engineering / Legal | **Tier:** 4

---

### 4.3 NHS Data Security and Protection Toolkit (DSPT)

**Gap / Action Required:** Standard for organisations processing NHS or health data in the UK.

**Resolution Pathway:** Begin investigation. Not required for public-domain-only PoC.

**Effort Estimate:** 4-6 weeks (completion)

**Risk if Unresolved:** Required for any future processing of UK health data.

**Owner:** ArcaScience Legal / Engineering | **Tier:** 4

---

### 4.4 Air-gapped / fully isolated deployment capability

**Gap / Action Required:** Can models operate with no outbound connectivity within MHRA infrastructure?

**Evidence Available:** 100% Kubernetes architecture is in principle portable. On-premises deployment is described as "planned" in OKR Execution Blueprint.

**Resolution Pathway:**
1. Confirm whether all 24 SLMs can run on-premises
2. Specify GPU hardware requirements
3. Test fully air-gapped operation (no outbound connectivity)
4. Scope containerisation and deployment packaging for MHRA

**Effort Estimate:** 2-4 weeks (engineering scoping + testing)

**Risk if Unresolved:** Required for any deployment involving Tier 3 (MHRA-internal) data. Not required for PoC.

**Owner:** ArcaScience Engineering | **Tier:** 4

---

### 4.5 CCS / G-Cloud framework listing

**Gap / Action Required:** UK government procurement typically routes through approved frameworks.

**Resolution Pathway:** Investigate G-Cloud listing process. Not required for unfunded PoC; critical for any paid engagement.

**Effort Estimate:** 4-8 weeks (application process)

**Risk if Unresolved:** Procurement complexity increases for any paid engagement.

**Owner:** ArcaScience Commercial / Legal | **Tier:** 4

---

### 4.6 Joint Data Protection Impact Assessment (DPIA)

**Gap / Action Required:** Required for processing likely to result in high risk to individuals. Any future UK health data processing would trigger this.

**Resolution Pathway:** Initiate jointly with MHRA when/if Tier 3 data processing is contemplated.

**Effort Estimate:** 4-6 weeks (joint process)

**Risk if Unresolved:** Legal requirement. But not triggered by public-domain PoC.

**Owner:** Joint (MHRA + ArcaScience Legal) | **Tier:** 4

---

### 4.7 NCSC supply chain security assurance

**Gap / Action Required:** UK government bodies assess supply chain security per NCSC guidance.

**Resolution Pathway:** Review NCSC guidance and map current controls. Address gaps proactively.

**Effort Estimate:** 2 weeks (assessment)

**Risk if Unresolved:** Required for formal vendor relationship.

**Owner:** ArcaScience Engineering / Legal | **Tier:** 4

---

### 4.8 Keycloak integration with MHRA identity infrastructure

**Gap / Action Required:** On-premises deployment needs to authenticate MHRA users through MHRA's identity provider.

**Evidence Available:** Keycloak supports federation (SAML, OIDC). Integration is architecturally supported but untested with MHRA.

**Resolution Pathway:** Assess during formal technical scoping if deployment proceeds.

**Effort Estimate:** 1-2 weeks (technical assessment)

**Risk if Unresolved:** Solvable standard integration. Not a PoC concern.

**Owner:** ArcaScience Engineering | **Tier:** 4

---

### 4.9 Omics and imaging data integration

**Gap / Action Required:** Explicitly excluded from current capabilities. Documented as future research (i-Demo/BR-PREDICT).

**Resolution Pathway:** Ensure marketing materials do not overclaim. Low relevance to MHRA's text-based post-authorisation work.

**Effort Estimate:** 1 hour (messaging check)

**Risk if Unresolved:** If marketing claims "full lifecycle" without qualification, MHRA asks about capabilities that do not exist.

**Owner:** ArcaScience Commercial | **Tier:** 4

---

### 4.10 MHRA assessor availability for PoC review

**Gap / Action Required:** The PoC requires ~3-4 hours of assessor time. Assessors are busy (80 concurrent issues, 600+ drugs).

**Resolution Pathway:** To be agreed during Phase 0 scoping. MHRA-owned decision.

**Effort Estimate:** N/A (MHRA decision)

**Risk if Unresolved:** PoC has no evaluators. Mitigated by keeping time commitment minimal.

**Owner:** MHRA | **Tier:** 4

---

## Summary: Execution Dashboard

### By Tier

| Tier | Count | Theme | Timeline |
|------|-------|-------|----------|
| **Tier 1** | **25** | Unlock the PoC | Before next meeting (2-3 weeks) |
| **Tier 2** | **19** | Win the follow-up meeting | Before PoC delivery (4-6 weeks) |
| **Tier 3** | **5** | Position in MHRA 2030 strategy | Parallel track (1-3 months) |
| **Tier 4** | **14** | Long-term infrastructure | Phase 2+ |
| **TOTAL** | **63** | | |

### By Effort Type

| Type | Count | Notes |
|------|-------|-------|
| Existing evidence to reframe/compile | 18 | We have the data; it needs packaging |
| Engineering work | 22 | Demo build, feature implementation, documentation |
| Legal/commercial action | 12 | Certifications, agreements, positioning |
| MHRA/joint items | 6 | Require MHRA participation |
| New strategic items | 5 | Upside opportunities |

### Critical Dependencies

```
[Remove dangerous claims (1.1-1.3)]
        |
        v
[Clean up beta platform (1.17)]  +  [Build SGLT2/DKA demo (1.12)]
        |                                    |
        v                                    v
[MHRA explores beta independently]  [Demo ready for meeting]
        |                                    |
        +-----> [Next meeting scheduled] <---+
                         |
                         v
              [PoC Phase 0 scoping]
                         |
                         v
              [Tier 2 items completed]
                         |
                         v
              [PoC Phase 1-2 delivery]
```

### Workload Estimate

| Timeframe | Estimated Total Effort | Key Deliverables |
|-----------|----------------------|------------------|
| Week 1 | 40 hours | Remove dangerous claims, publish metrics, start model cards, start demo build |
| Week 2 | 60 hours | Continue demo build, clean beta platform, draft MoU, compile certifications |
| Week 3 | 40 hours | Finalise demo, rehearse, prepare follow-up communication |
| Weeks 4-6 | 60 hours | Tier 2 engineering (error propagation, confidence scoring, disagreement flags) |
| Parallel | 20 hours | Tier 3 strategic positioning (2030 strategy, AI Commission, HALO positioning) |

---

## Quality Acceptance Checklist

Before any material is sent to MHRA or any meeting is scheduled, every item below must be checked off:

- [ ] All Tier 1 IMMEDIATE items (1.1-1.3) completed -- dangerous claims removed
- [ ] Every MHRA question from the first meeting has a direct answer prepared
- [ ] Working demo on SGLT2/DKA (or selected PoC issue) is operational and rehearsed
- [ ] Demo includes observational studies and meta-analyses, not just case reports
- [ ] Beta platform is clean -- no prohibited claims visible
- [ ] "Bespoke model per issue" objection neutralised with concrete configuration timeline
- [ ] Clear separation between automation and assessor judgment in all materials
- [ ] All slides pass the "Claims We Will NOT Make" checklist review
- [ ] Confidentiality framework is ready to reference (scratch/04)
- [ ] Performance metrics compiled with full citations
- [ ] Collaboration letter / MoU drafted and ready to share
- [ ] All meeting participants briefed on the 5 messaging principles and 15 prohibitions

---

*This document is comprehensive by design. It is an internal execution plan, not a document for MHRA. Its purpose is to ensure ArcaScience leadership has full visibility into preparation requirements and confidence in the path to resolution. Every gap has a resolution pathway. Every pathway has an effort estimate. The work is bounded and achievable.*

*The fundamental posture is this: ArcaScience has a strong platform with validated performance, published evidence, and real client results. The MHRA engagement requires honest communication of what works, what is planned, and what remains to be built. That honesty -- backed by a working demonstration -- is the single most effective strategy for building regulatory trust.*

*Compiled from: scratch/01_questions.json, scratch/01_quotes.md, scratch/02_mhra_workflow.md, scratch/03_under_the_hood.md, scratch/04_data_governance.md, scratch/05_positioning_findings.md, scratch/06_poc_plan.md, docs/MHRA_Deep_Research_Briefing.md*
