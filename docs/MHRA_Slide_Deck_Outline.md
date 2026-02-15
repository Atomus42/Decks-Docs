# MHRA Follow-Up Meeting: Slide Deck Outline

**Document classification:** Internal preparation -- deck structure for ArcaScience leadership review
**Version:** 1.0
**Date:** 2026-02-15
**Prepared by:** Agent 7 (Editor / Deck Strategist)
**Tone directive:** Regulator-grade. Precise. Audit-friendly. No hype.

---

## Guiding Principles for Every Slide

1. The **human assessor** is the central figure in every diagram and narrative. The AI is the instrument; the assessor is the agent.
2. **Lead with limitations and boundaries** before capabilities. This mirrors how regulators evaluate: identify risks first, then weigh benefits.
3. **3-6 bullets maximum** per slide. Boardroom-clean. No clutter.
4. **Zero speed claims.** No "in seconds," no "18 months to seconds," no absolute percentages without methodology.
5. All language tested against the "Claims We Will NOT Make" list (Appendix 10B of Base Document).
6. Every quantitative claim includes: sample size, baseline, and known limitations.

---

## Slide 1: Title Slide

**Title:** ArcaScience: Structured Evidence Tools for Post-Authorisation Safety Assessment

**Objective:** Set a precise, measured tone from the first frame. Signal that this meeting is a response to MHRA's stated concerns, not a repeat of the initial pitch.

**Bullets:**
- Follow-up to [date] exploratory discussion with MHRA Benefit-Risk Evaluation Group
- Prepared in response to the questions and concerns raised by MHRA participants
- Agenda: what we heard, what we are, what we are not, and a proposed next step

**Suggested figure/diagram:** Clean title card. ArcaScience logo (small). MHRA crest NOT included unless MHRA grants explicit permission. No stock imagery. No marketing taglines.

**Speaker notes:** Open by thanking MHRA for their time and candour in the first meeting. State explicitly: "We heard your concerns, and this presentation is structured around addressing them directly. We will lead with our limitations before discussing capabilities."

---

## Slide 2: What We Heard -- MHRA's Five Core Questions

**Title:** What You Told Us: Five Questions We Must Answer

**Objective:** Demonstrate active listening. Frame the entire deck as a response to MHRA's own stated needs, not as a sales narrative.

**Bullets:**
1. "How does this apply to post-authorisation safety work -- not pre-authorisation?" (Allison)
2. "We cannot develop a bespoke model for every use case. How does this scale?" (Allison)
3. "I need to see under the hood." (Allison)
4. "We cannot share Yellow Card data, CPRD, or ongoing investigations." (Allison, Sharinto)
5. "You make it sound so easy, and it is so hard." (Allison)

**Suggested figure/diagram:** None. Clean text only. Each question attributed with speaker name. No diagrams competing with the words -- let MHRA see that their words were heard verbatim.

**Speaker notes:** Read each quote slowly. Do not paraphrase. Acknowledge that the initial meeting's messaging fell short of what MHRA rightly expects. State: "The rest of this presentation is organised around answering these five questions."

---

## Slide 3: What ArcaScience Is -- and What It Is NOT

**Title:** Boundaries First: What ArcaScience Does Not Do

**Objective:** Lead with what the system cannot and should not do. Establish credibility through self-imposed boundaries before any capability claim.

**Bullets:**
- Does NOT render benefit-risk verdicts or automate regulatory judgment
- Does NOT assess study quality or determine whether a study is valid
- Does NOT generate free-text conclusions (not a ChatGPT-style generative tool)
- Does NOT handle imaging, omics, or proprietary real-world databases (e.g., CPRD) without on-premises deployment
- Does NOT replace assessor expertise in causal reasoning, contextual judgment, or UK-specific effectiveness assessment
- **What it IS:** An evidence-structuring engine that extracts, classifies, normalises, and links published evidence -- delivering a structured starting point for the expert work only assessors can perform

**Suggested figure/diagram:** Diagram 5.6 from 05_positioning_findings.md -- "What Changes vs. What Stays the Same." Two-column layout. Left column (muted colour): "What changes -- faster, more structured" (literature search, data extraction, normalisation, cross-referencing, template pre-population). Right column (prominent colour, wider): "What stays the same -- assessor-owned" (study quality assessment, clinical interpretation, causality determination, benefit-risk weighing, regulatory action). The right column is visually larger to signal that the assessor's role is dominant.

**Speaker notes:** Spend more time on the left side of this slide (limitations) than the right (capabilities). If an MHRA participant interrupts with a question about any limitation, welcome it -- it means they are engaged. The goal is to earn the right to present capabilities by first demonstrating you understand the boundaries.

---

## Slide 4: Post-Authorisation Workflow Fit

**Title:** Where We Help in MHRA's Post-Authorisation Workflow -- and Where We Do Not

**Objective:** Map ArcaScience's contribution to the specific workflow MHRA described. Demonstrate understanding of the post-authorisation context. Show that the platform addresses evidence assembly, not assessment.

**Bullets:**
- MHRA's workflow: Signal detection --> Evidence assembly --> Critical appraisal --> Benefit-risk judgment --> Regulatory action
- ArcaScience supports the **evidence assembly** step: literature retrieval, structured extraction, cross-referencing, gap identification
- The system does NOT participate in signal detection (assessor + Yellow Card + epidemiology team), critical appraisal (assessor judgment), or regulatory action (assessor + committee)
- Handles observational studies, meta-analyses, systematic reviews, and case series -- not only clinical trial data

**Suggested figure/diagram:** Diagram 5.1 from 05_positioning_findings.md -- "Assessor-Led Workflow: Where Automation Ends and Judgment Begins." Horizontal process flow with two swim lanes. Upper lane (muted grey/blue): "System -- automated" covering ingestion, structuring, cross-referencing. Lower lane (prominent MHRA teal): "Assessor -- expert judgment" covering quality assessment, contextual judgment, benefit-risk determination, regulatory action. A clearly marked **HANDOFF POINT** divides the two. The assessor lane is visually dominant.

**Speaker notes:** Point to the handoff boundary explicitly. Say: "Everything to the left of this line is what we automate. Everything to the right is what only your assessors can do. We are not proposing to cross that line." If asked about the antidepressant/PSSD use case Allison raised, acknowledge it directly: "That is exactly the type of hard, messy, post-authorisation problem this tool is designed to support -- not by solving it, but by accelerating the evidence-gathering that precedes your assessors' expert analysis."

---

## Slide 5: Under the Hood -- Pipeline Architecture

**Title:** 24 Task-Specific Models, Not One Black Box

**Objective:** Address Allison's direct request to "see under the hood." Show that the pipeline is decomposed, auditable, and transparent at every step.

**Bullets:**
- Pipeline processes documents through discrete, chained steps: Ingest --> Classify --> Identify Sections --> Extract Entities --> Extract Relations --> Normalise --> Link --> Template
- Each step produces **inspectable intermediate output** before feeding the next
- Models are task-specific (e.g., "adverse event extractor," "study design classifier"), NOT therapeutic-area-specific
- No new model is trained per drug or per safety question -- the same 24 models work across all therapeutic areas
- Adaptation happens through **pipeline configuration** (query scope, source selection, output template), not model retraining

**Suggested figure/diagram:** Diagram 5.5 from 05_positioning_findings.md -- "24 Task-Specific Models: What Each One Does and Does Not Do." A simplified pipeline schematic showing 4-5 representative model categories in sequence (Document Classification --> Section ID --> Entity Extraction --> Normalisation --> Knowledge Graph Linking). At each step, show: model function, example input/output, and a "does NOT do" annotation (e.g., Study Design Classifier "does NOT assess study quality or risk of bias"). Keep to 4-5 steps on-slide; full 24-model detail in appendix.

**Speaker notes:** Emphasise: "Each arrow in this pipeline is an auditable boundary. There is no single opaque model producing end-to-end results. If Step 3 makes an error, the reviewer can inspect Step 3's output, identify the error, and trace it without needing to understand the entire chain." Reference the training data: "These models were trained on 10,000+ documents spanning all therapeutic areas and all clinical phases, making them deliberately cross-therapeutic."

---

## Slide 6: Traceability -- From Source Document to Extracted Element

**Title:** Full Audit Trail: Every Data Point Traceable to Source

**Objective:** Demonstrate that every output element can be traced back through the chain to the original source document, section, and sentence. Address the "black box" concern directly.

**Bullets:**
- Every extracted element links to: source document (DOI/PMID), source section and sentence, extraction model that produced it
- Assessor can click through from any data point in the output to the original text
- Confidence scoring (in development): per-element indicator based on extraction certainty and source reliability
- Disagreement flags (in development): where models or sources produce conflicting extractions, both are preserved
- Honest status: source-to-statement linkage is operational; confidence scoring and disagreement flags are planned features, not yet in production

**Suggested figure/diagram:** Diagram 5.2 from 05_positioning_findings.md -- "From Source Document to Extracted Element: Full Traceability." Vertical drill-down showing a single data point's journey from published article (DOI shown) --> Document Classification ("observational study, retrospective cohort") --> Section ID (methodology, results, safety) --> Entity Extraction ("myocardial infarction," "adalimumab," "2 weeks post-administration") --> Normalisation (MedDRA PT code) --> Assessor Review Point. Every arrow is bidirectional. Final element labelled "Candidate -- Pending Expert Review."

**Speaker notes:** Walk through one concrete example end to end. Use a real published article if possible (e.g., from the SGLT2/DKA literature). Show the assessor review point at the bottom: "This is where the system's work ends and the assessor's judgment begins. The assessor sees not only the extracted element but the full chain of how it was derived."

---

## Slide 7: Data Sources and Confidentiality -- MHRA-Safe by Design

**Title:** Three-Tier Data Model: Your Data Never Leaves Your Control

**Objective:** Address MHRA's confidentiality constraints directly. Show that the PoC requires zero MHRA data and that the long-term architecture respects the hard boundaries stated in the meeting.

**Bullets:**
- **Tier 1 (Public domain):** PubMed, ClinicalTrials.gov, FAERS, regulatory public assessment reports, MHRA Drug Safety Updates -- processed on ArcaScience infrastructure, no MHRA data involved
- **Tier 2 (Licensed):** Subscription databases (e.g., Pharmapendium) -- accessible via standard licensing, not MHRA-specific
- **Tier 3 (MHRA internal):** Yellow Card, CPRD, ongoing investigations -- **never leaves MHRA**; any future integration requires on-premises deployment within MHRA's secure environment
- For the proof of concept: **Tier 1 only.** Zero MHRA data enters ArcaScience systems at any stage
- Long-term architecture: "bring the algorithm to the data" -- containerised models deployed inside MHRA infrastructure, processing in-situ, no data egress

**Suggested figure/diagram:** Two-panel layout. **Left panel (PoC phase):** Simple flow showing ArcaScience infrastructure processing only public data, with structured output delivered to MHRA for evaluation. No data flows from MHRA to ArcaScience. **Right panel (future phase, if warranted):** ArcaScience models deployed within MHRA's secure boundary; all processing occurs inside MHRA; no data egress. MHRA infrastructure boundary drawn as a prominent security perimeter. Label clearly: "PoC = left panel. Right panel is a future possibility, not a current commitment."

**Speaker notes:** Be explicit: "We heard you say that Yellow Card data is patient-level and cannot leave MHRA, that CPRD cannot be shared, and that ongoing safety investigations are confidential. Our proof of concept requires none of that data. We work exclusively with public-domain sources. If the PoC demonstrates value and MHRA wishes to explore integration with internal data in the future, we have an architecture for that -- but we are not proposing it now, and we acknowledge that several engineering and governance steps remain before that is viable."

---

## Slide 8: Quality Control and Uncertainty -- What We Measure and What We Cannot

**Title:** What the System Knows, What It Flags, and What Only the Assessor Knows

**Objective:** Address Sharinto's question about uncertainty and gaps. Demonstrate that the system is designed to surface its own limitations, not to present incomplete information as complete.

**Bullets:**
- System extracts study design elements (sample size, duration, CIs, confounders, limitations) but does **not** judge whether those elements are adequate
- Missing data fields are explicitly flagged (e.g., "no sample size reported," "no follow-up duration stated")
- When sources conflict, both versions are preserved and presented side by side -- the system does not silently resolve contradictions
- Confidence scoring: each extraction receives an indicator based on source reliability and extraction certainty (in development)
- The system reports what it does not know: gap analysis identifies evidence types expected but absent

**Suggested figure/diagram:** Diagram 5.3 from 05_positioning_findings.md -- "What the System Knows, What It Does Not Know, and What Only You Know." Three-column panel. Column 1 (narrow): "What the system does" -- extracts, normalises, cross-references. Column 2 (medium): "What the system flags but cannot judge" -- sample size, design type, missing fields, conflicting evidence. Column 3 (widest, most prominent): "What only the assessor knows" -- whether methodology is adequate, whether a gap is clinically meaningful, how to weigh conflicting evidence, whether an association is causal. The third column is widest to communicate that the assessor's contribution is the most substantial.

**Speaker notes:** Directly reference Sharinto's concern from the first meeting: "You asked whether the system flags where there are issues. The answer is yes -- it flags missing fields, conflicting evidence, and data gaps. But it does not resolve those flags. That resolution -- determining clinical significance, methodological adequacy, and evidentiary weight -- is the assessor's responsibility and expertise."

---

## Slide 9: Addressing the Key Objections

**Title:** Direct Responses to the Concerns Raised in Our First Meeting

**Objective:** Consolidate and directly address the most critical objections from the initial meeting. No evasion.

**Bullets:**
- **"Fill BR in seconds":** We acknowledge this messaging was inappropriate. We are removing all speed claims from regulator-facing materials. Evidence consolidation is accelerated; the assessment itself is and must remain a human-led process.
- **"Can't build bespoke models per case":** No bespoke model is built. The same 24 task-specific models work across all therapeutic areas. Only the query scope and source selection change per use case.
- **"Beyond what ChatGPT could do":** Differentiators are structured extraction of critical appraisal elements, source-level traceability, cross-study reconciliation, confidence scoring, and gap analysis -- not keyword retrieval or text generation.
- **"100% regulatory acceptance rate":** We will not repeat this claim. Regulatory acceptance reflects the sponsor's overall submission, not an endorsement of any tool used in preparation.

**Suggested figure/diagram:** None. Clean text. Let the directness of the responses carry the slide. A visual here would dilute the message.

**Speaker notes:** This slide is where credibility is won or lost. Deliver each response calmly and without defensiveness. If Allison pushes back on any point, welcome it. The goal is to demonstrate that ArcaScience has listened, internalised the feedback, and acted on it. Do not rush past the first bullet -- the speed claims were the single biggest credibility issue in the first meeting.

---

## Slide 10: Proof-of-Concept Proposal

**Title:** A No-Funding, Public-Domain Proof of Concept -- On Your Terms

**Objective:** Present a concrete, low-risk next step. Demonstrate that ArcaScience is prepared to invest its own resources and let MHRA control the test conditions.

**Bullets:**
- ArcaScience proposes to run its existing pipeline against a **publicly reported, completed safety issue selected by MHRA**
- Three candidate options prepared (SGLT2/DKA, fluoroquinolones, valproate) -- MHRA may select any of these or propose an alternative
- **Zero funding required** from MHRA; ArcaScience absorbs all cost
- **Zero confidential data** involved; all inputs are public-domain
- MHRA assessors compare ArcaScience output against their own historical assessment of the same issue
- Total MHRA time commitment: approximately 3-4 hours over 4 weeks

**Suggested figure/diagram:** Simple three-phase timeline. Phase 0: Joint scoping (1 meeting, MHRA selects use case). Phase 1: ArcaScience builds evidence map independently (2 weeks, no MHRA effort). Phase 2: Joint review session (90 minutes, MHRA evaluates output). Below the timeline, a single row of success metrics: source completeness >= 90%, extraction accuracy >= 95%, traceability = 100%, error rate < 2%.

**Speaker notes:** Emphasise three things: (1) MHRA picks the test case, (2) MHRA shares no data, (3) the total time ask is under 4 hours. If asked about the recommended candidate (SGLT2/DKA), be prepared to explain why: medium-high complexity, genuine causality challenges, multi-regulator documentation, low political sensitivity. But defer to MHRA's preference -- the goal is to let them control the evaluation.

---

## Slide 11: PoC Deliverables -- What MHRA Would Receive

**Title:** What You Would Receive: Six Deliverables for Evaluation

**Objective:** Make the PoC output concrete and tangible. Show that the deliverable package is structured, auditable, and designed for assessor review.

**Bullets:**
1. **Evidence map:** All relevant public sources identified, classified by type, design, population, date, with temporal mapping
2. **Structured extraction output:** Per-source extraction of study characteristics, findings, and critical appraisal elements, linked to source text
3. **Templated draft sections:** PSUR-like structure pre-populated from extracted evidence (for illustration, not regulatory use)
4. **Traceability report:** Complete audit trail from source document to structured output
5. **Confidence scoring:** Per-element scoring based on source reliability, extraction certainty, cross-source consistency
6. **Gap analysis:** Explicit identification of what evidence is missing from public sources

**Suggested figure/diagram:** A simple numbered list with small icons per deliverable (document icon, chain-link icon for traceability, magnifying glass for gap analysis). Keep it clean -- the deliverable names and descriptions carry this slide.

**Speaker notes:** For each deliverable, briefly connect it to an MHRA concern from the first meeting. Evidence map = "comprehensive evidence base." Traceability report = "see under the hood." Gap analysis = "the system knows what it does not know." Confidence scoring = "levels of uncertainty, flagging where there are issues."

---

## Slide 12: Next Meeting Agenda

**Title:** Proposed Agenda: 60-Minute Follow-Up Meeting

**Objective:** Show that ArcaScience has a structured, respectful plan for the next interaction. Signal preparedness without presumption.

**Bullets:**
- 0:00-0:10 -- Confirm use case and data boundaries (MHRA selects; ArcaScience presents options)
- 0:10-0:25 -- Under-the-hood technical walkthrough (pipeline, models, validation, traceability)
- 0:25-0:45 -- Live demonstration on agreed public safety issue (3-5 representative sources, extraction from observational study, confidence scoring, source traceability)
- 0:45-0:55 -- Review sample outputs and traceability (MHRA assessors select elements and trace to source)
- 0:55-1:00 -- Agree next steps (PoC go/no-go, timeline, assessor availability)

**Suggested figure/diagram:** Clean agenda table. No diagram needed. Optionally, a single visual showing the split: "ArcaScience presents" (first half) vs. "MHRA challenges" (second half), reinforcing that the meeting is designed for MHRA to test, not for ArcaScience to sell.

**Speaker notes:** Note that the live demo segment (20 minutes) is the longest single block. This is intentional -- Allison asked to "see under the hood," and a live demo is more convincing than slides. Prepare fallback: if technical issues prevent live demo, have pre-recorded output and static screenshots ready. Under no circumstances should marketing slides appear during this meeting.

---

## Slide 13: Appendix A -- Validation Approach

**Title:** Model Validation: Four Complementary Methods

**Objective:** Provide technical depth for MHRA participants who want to understand validation methodology. This slide is for reference, not for presentation unless MHRA requests it.

**Bullets:**
- **Method 1: Clinician-annotated test sets** -- Dual-annotated by two independent clinicians; model outputs compared against gold standard; measured precision, recall, F1 (target >= 85%)
- **Method 2: Statistical comparison against noisy data** -- Performance measured on real-world, imperfect data, not only clean test sets
- **Method 3: Blind comparison against client assessments** -- Client's independently produced assessment serves as ground truth; ArcaScience output compared blind
- **Method 4: Client-specific sampling** -- After pipeline configuration, targeted samples drawn from the specific therapeutic context and evaluated for the same error metrics
- **Open item (TBD):** Formal error propagation analysis across the full chain is under development; current per-model metrics do not yet quantify cumulative error across chained steps

**Suggested figure/diagram:** Simple 2x2 matrix showing the four methods, with one axis as "internal vs. external validation" and the other as "clean data vs. noisy data." This positions the validation as multi-dimensional, not reliant on a single method.

**Speaker notes:** If Allison asks about specific F1 scores per model, be prepared to share what is available and be transparent about what is not yet measured. If asked about inter-annotator agreement between the two clinicians, acknowledge this as a TBD. Honesty about gaps in validation is more credible than overclaiming.

---

## Slide 14: Appendix B -- Post-Authorisation Use Case Flow (Detailed)

**Title:** Supporting Post-Authorisation Safety Assessment: A Practical Workflow

**Objective:** Provide a detailed, MHRA-specific workflow diagram for assessors who want to see exactly how the tool fits their daily work. Directly addresses Allison's statement that she could not see how the tool applies to post-authorisation.

**Bullets:**
1. Safety signal emerges (entirely outside the system -- MHRA assessor + Yellow Card + epidemiology team)
2. Evidence scoping: assessor defines drug class, adverse event of interest, relevant data sources (assessor directs; system executes)
3. Literature sweep: system retrieves and structures all published literature matching the assessor-defined query
4. Comparator assembly: system pulls structured data on the drug class for comparative profiling
5. Evidence dashboard delivered to assessor: number of studies, study types, key findings, data gaps, conflicting results -- all hyperlinked to source
6. Critical appraisal and benefit-risk judgment: assessor evaluates, accepts/rejects, and writes conclusions (entirely human)

**Suggested figure/diagram:** Diagram 5.4 from 05_positioning_findings.md -- "Supporting Post-Authorization Safety Assessment: A Practical Workflow." Steps 1 and 6 are shown entirely in the "Assessor" swim lane. Steps 3-4 are in the "System" swim lane. Step 2 (evidence scoping) is shown as a joint activity with the assessor directing. Step 5 (dashboard delivery) is the handoff point. The assessor swim lane is visually dominant.

**Speaker notes:** This slide is held in reserve for when Allison or Steph asks: "But how would we actually use this in our day-to-day work?" Walk through a concrete example -- e.g., "Suppose you receive a signal about antidepressants and persistent sexual dysfunction. You define the drug class and the adverse event. The system retrieves and structures all published literature, identifies observational studies and their methodologies, flags gaps. You then evaluate each source, applying your expertise in UK prescribing context and causality assessment. The system did not make a judgment -- it assembled and organised the evidence for your judgment."

---

## Production Notes for Deck Designer

### Visual language
- Colour palette: muted blues, greys, and one accent colour (teal or dark green). No bright reds, oranges, or marketing gradients.
- Typography: clean, sans-serif. No italic emphasis except for direct quotes.
- Every diagram must place the **human assessor** as the central or largest element.
- All "system" elements are shown in muted/supporting colours; all "assessor" elements are shown in prominent/foreground colours.
- No stock photos, no abstract AI imagery, no neural network visualisations. These signal marketing, not substance.

### Slide density
- Maximum 6 bullets per slide. No exceptions.
- No bullet should exceed two lines of text at presentation font size.
- If a bullet requires more explanation, move the detail to speaker notes or an appendix slide.

### Language rules
- Subject of capability sentences should be the human assessor, not the AI.
  - Correct: "Assessors receive a structured evidence package enabling them to..."
  - Incorrect: "Our AI identifies 9x more signals than..."
- No absolute claims: no "100%," no "always," no "every" without qualification.
- No speed claims: no "in seconds," no "in minutes," no time comparisons.
- No superlatives: no "world's largest," no "most comprehensive," no "best-in-class."
- Use "evidence-structuring platform" or "evidence-structuring tool" as the standard descriptor. Not "AI-driven benefit-risk analysis platform."

### Handling Q&A
- Prepare a separate Q&A reference document (not in the deck) with detailed answers to all 20 TBD questions from scratch file 03 (Section 8).
- If a question is asked that cannot be answered, say so: "That is a question we cannot answer today. We will provide a written response within [timeframe]."
- Never deflect a question by pivoting to a capability claim. Answer the question, acknowledge the gap, then offer the next step.

---

*Document prepared by Agent 7 -- Editor / Deck Strategist*
*For internal use in MHRA meeting response preparation*
*All content derived from scratch files 01-06 and MHRA_Collaboration_Base.md*
