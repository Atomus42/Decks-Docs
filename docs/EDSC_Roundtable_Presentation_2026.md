# EUROPEAN DRUG SAFETY CONFERENCE 2026 — ROUNDTABLE PRESENTATION

## CHALLENGES IN LEVERAGING ALL BIOMEDICAL KNOWLEDGE & HOW AI CAN HELP

**Format:** 30-minute roundtable (100 safety specialists)
**Location:** Gloria B, C, D
**Date:** Tuesday, 25 February 2026
**Presenter:** ArcaScience
**Tone:** Scientific. Evidence-led. No hype. Every claim sourced. Audience = peers, not prospects.

---

## PRESENTATION ARCHITECTURE

**Total runtime: 30 minutes**

| Block | Duration | Purpose |
|-------|----------|---------|
| I. The Knowledge Problem | 8 min | Establish shared pain — ground in data |
| II. Why Current Approaches Fall Short | 6 min | Name the structural gaps honestly |
| III. An Evidence-Structuring Approach | 8 min | Show how AI can address the gaps |
| IV. Proof It Works — Real Cases | 5 min | Concrete, published evidence |
| V. Open Discussion | 3 min | Roundtable engagement |

---

---

## SLIDE 1 — TITLE

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│     CHALLENGES IN LEVERAGING ALL BIOMEDICAL KNOWLEDGE           │
│               & HOW AI CAN HELP                                 │
│                                                                 │
│     European Drug Safety Conference 2026                        │
│     Gloria B, C, D — Tuesday 25 February                        │
│                                                                 │
│     [ArcaScience]                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Speaker notes:**
"Thank you. I'm [Name] from ArcaScience. We build evidence-structuring tools for pharmacovigilance and benefit-risk assessment — 24 task-specific AI models trained by clinicians, used by 20+ pharma companies across 50+ regulatory submissions. But today isn't a product demo. This is a conversation about a problem every person in this room deals with: the growing impossibility of leveraging all the biomedical knowledge that exists to make drugs safer. I want to share data on why it's broken, what we've learned building tools to address it, and — most importantly — hear how you're experiencing this in your own organizations."

---

---

## BLOCK I: THE KNOWLEDGE PROBLEM (8 min)

---

### SLIDE 2 — THE BIOMEDICAL KNOWLEDGE EXPLOSION

**Title:** We Are Drowning in Evidence We Cannot Use

**Bullets:**
- **39 million citations** in PubMed — growing by **1.5 million per year** (~4,000 papers/day)
- **40+ million** adverse event reports in VigiBase; **29.3 million** ICSRs in EudraVigilance; **15+ million** in FAERS
- FDA receives **~2 million adverse event reports per year** — and that captures only an estimated **6% of actual ADRs** (94% median underreporting rate, Hazell & Shakir, Drug Safety 2006)
- Total addressable evidence: published literature + clinical trial data + spontaneous reports + EHR data + patient registries + social media — **each in different formats, terminologies, and quality levels**

**Suggested visual:** Exponential growth curve of PubMed citations (1950-2026) overlaid with ICSR volume growth. Two curves diverging from human review capacity (flat line).

**Speaker notes:**
"Let me start with numbers everyone in this room knows but rarely sees together. PubMed adds 4,000 papers a day. EudraVigilance holds 29 million ICSRs. The FDA receives 2 million adverse event reports per year. And yet — the best published estimate is that spontaneous reporting captures only 6% of real adverse drug reactions. So we have an ocean of data and we're still missing 94% of the signal. The knowledge exists. It's scattered across millions of documents in incompatible formats, buried in PDFs, locked in proprietary databases, written in different terminologies. The problem is not that we lack evidence. The problem is that we cannot assemble it fast enough to use it."

---

### SLIDE 3 — WHERE BIOMEDICAL KNOWLEDGE LIVES (AND HIDES)

**Title:** Fragmented by Design, Siloed by Default

**Layout:** Six-column diagram showing data silos:

```
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ Published│ │Spontan.  │ │ Clinical │ │ EHR /    │ │ Internal │ │ Social   │
│Literature│ │Reporting │ │ Trial    │ │Real-World│ │ Company  │ │Media &   │
│          │ │          │ │ Data     │ │ Data     │ │ Data     │ │Patient   │
│ PubMed   │ │VigiBase  │ │CT.gov    │ │CPRD,THIN │ │CSRs,     │ │Forums    │
│ MEDLINE  │ │FAERS     │ │EudraCT   │ │Claims DB │ │Protocols │ │Apps      │
│ Embase   │ │EudraVig. │ │JAPIC-CTI │ │Registries│ │Lab data  │ │Wearables │
│          │ │PMDA      │ │          │ │          │ │          │ │          │
│UNSTRUC-  │ │SEMI-     │ │STRUCTURED│ │STRUCTURED│ │MIXED     │ │UNSTRUC-  │
│TURED     │ │STRUCTURED│ │          │ │(variable)│ │          │ │TURED     │
└──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘
       │            │            │            │            │            │
       └────────────┴────────────┴─────┬──────┴────────────┴────────────┘
                                       │
                              ┌────────▼────────┐
                              │   THE SAFETY    │
                              │   ASSESSOR'S    │
                              │   DESK          │
                              │                 │
                              │  Trying to form │
                              │  a complete     │
                              │  picture from   │
                              │  incompatible   │
                              │  fragments      │
                              └─────────────────┘
```

**Bullets:**
- Each source uses **different terminologies** (MedDRA, SNOMED CT, ICD-10, WHO-ART, free text)
- Published literature is unstructured free-text; spontaneous reports are semi-structured; trial data is structured but access-restricted
- A single safety question (e.g., "does drug X cause cardiac events?") requires **cross-referencing all six source types** — manually
- No single system today integrates these sources into a unified evidence picture

**Speaker notes:**
"This is what a safety assessor's job actually looks like. You're trying to answer a single question — does this drug cause this harm? — and the evidence is spread across six fundamentally different data ecosystems. PubMed gives you unstructured PDFs. VigiBase gives you coded reports. Clinical trials give you structured datasets you may not even have access to. EHRs give you real-world evidence in variable formats. Your own company data sits in yet another system. And social media? That's noise with occasional signal buried inside. No human can hold all of this in their head simultaneously. And no single system integrates it. So what do we do? We assign teams of people to manually search, read, extract, and cross-reference. And that brings us to the scaling problem."

---

### SLIDE 4 — THE CASE VOLUME WALL

**Title:** Human Review Does Not Scale

**Key data:**

| Metric | Value |
|--------|-------|
| Global ICSR annual intake (EudraVigilance, 2024) | ~1.8 million |
| FDA annual AE reports | ~2 million |
| Annual company-level case growth | 10-15%/year |
| Projected global ICSR growth (next 5 years) | +30% |
| PV budget consumed by case processing | 40-80% |
| Cost per ICSR processed | $70-$200 |
| Top pharma annual PV spend | $45M-$200M |

**Bullets:**
- Case volumes growing **10-15% annually** at company level, **30-50% in clinical trial caseloads** due to evolving regulations
- Up to **80% of pharmacovigilance budgets** consumed by case processing — leaving limited capacity for actual safety assessment
- Hiring more people is linear; the problem grows exponentially
- E2B(R3) compliance deadline **April 2026** adds format complexity to volume pressure

**Speaker notes:**
"The math is simple and unforgiving. EudraVigilance collected 1.8 million ICSRs last year. The FDA received 2 million. Company-level volumes grow 10-15% per year. Some of you are seeing 30-50% growth in clinical trial caseloads alone. And here's the uncomfortable number: 40 to 80% of your pharmacovigilance budget goes to case processing. Not to signal assessment. Not to benefit-risk analysis. Not to scientific evaluation. To processing. You're spending the majority of your safety budget on data handling, not on safety science. And you cannot hire your way out of it because the growth is exponential and your headcount budget is not."

---

### SLIDE 5 — THE BIOLOGICAL PLAUSIBILITY GAP

**Title:** Statistical Signals Without Scientific Context

**Bullets:**
- Signal detection today relies primarily on **disproportionality analysis** (PRR, ROR, EBGM, BCPNN)
- Published limitation: **60% of all drug-event pairs** can generate either positive or negative signals of disproportionate reporting depending on the model used (Caster et al., Drug Safety 2020)
- **78% of DA studies lack clear definitions** for case selection, ADRs, or comparators; **32% do not specify signal detection thresholds** (Hammad et al., Frontiers in Pharmacology 2025)
- Statistical flags are necessary but insufficient — they tell you *what co-occurs*, not *why it might*
- Biological plausibility requires cross-referencing: mechanism of action, pharmacological class effects, metabolic pathways, protein targets, known organ toxicity profiles
- **This cross-referencing is largely manual today** — dependent on the individual assessor's knowledge and reading bandwidth

**Suggested visual:** Two-panel comparison. Left: "What statistical signal detection gives you" — a list of drug-event pairs ranked by disproportionality score. Right: "What biological plausibility assessment requires" — the same pair enriched with mechanism-of-action data, class-effect evidence, pathway analysis, temporal patterns, dose-response data.

**Speaker notes:**
"This is perhaps the most scientifically important slide. Statistical signal detection — disproportionality analysis — is the backbone of quantitative pharmacovigilance. It works. But it has a fundamental limitation: it identifies co-occurrence, not causation. Caster and colleagues showed that 60% of drug-event pairs can generate either a positive or negative signal depending on which model you use. That's not a flaw in the method — it's a feature of statistical approaches applied to spontaneous reporting data with known biases. The real question isn't 'does this drug-event pair show disproportionality?' It's 'is there a biological reason this drug could cause this event?' And answering that question requires synthesizing evidence across pharmacology, toxicology, clinical trial data, published case series, and mechanistic literature. Today, that synthesis happens in one place: the assessor's brain. Which means it's limited by what that assessor has read, what they remember, and how much time they have."

---

### SLIDE 6 — THE UNSTRUCTURED DATA WALL

**Title:** 80% of Biomedical Data Is Unstructured — And Growing

**Bullets:**
- Clinical narratives, case report PDFs, published literature, physician notes, patient verbatims — all **free text**
- A single PSUR cycle requires reviewing **hundreds to thousands of documents** across multiple languages
- Only **0.2% of social media posts** mentioning a medication are PV-relevant — massive noise-to-signal ratio
- Manual extraction from unstructured sources is the **single largest time sink** in safety evidence assembly
- EMA's DARWIN EU fully operationalized in 2024 for real-world data — but still depends on structured data sources

**Speaker notes:**
"Here's the bottleneck within the bottleneck. The most valuable safety evidence — published case series, clinical narratives, real-world case reports — is overwhelmingly unstructured text. A PSUR cycle can require reviewing thousands of documents. And when I say 'reviewing,' I mean: a human being opens a PDF, reads it, decides what's relevant, extracts the adverse events, maps them to MedDRA terms, assesses causality, and writes it up. Multiply that by every product in your portfolio, every reporting period, every language. The EMA has done important work with DARWIN EU to integrate real-world data — but DARWIN EU operates on structured databases. The vast ocean of unstructured published evidence still requires human reading. This is where the evidence assembly bottleneck lives."

---

---

## BLOCK II: WHY CURRENT APPROACHES FALL SHORT (6 min)

---

### SLIDE 7 — THE CURRENT TOOLCHAIN

**Title:** Today's Safety Infrastructure Was Built for a Different Scale

**Layout:** Three-column assessment:

```
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│  CASE MANAGEMENT    │  │  SIGNAL DETECTION   │  │  EVIDENCE ASSEMBLY  │
│  SYSTEMS            │  │  TOOLS              │  │                     │
│                     │  │                     │  │                     │
│  ✓ Intake routing   │  │  ✓ Disproportional. │  │  ✗ Largely manual   │
│  ✓ Workflow mgmt    │  │  ✓ PRR/ROR/EBGM     │  │  ✗ Siloed by source │
│  ✓ Regulatory       │  │  ✓ Automated flags  │  │  ✗ No cross-linking │
│    submission       │  │                     │  │  ✗ Assessor-         │
│                     │  │  ✗ No biological    │  │    dependent         │
│  Well-served by     │  │    plausibility     │  │                     │
│  existing vendors   │  │  ✗ High false       │  │  THE GAP            │
│  (Argus, AERS,      │  │    positive rate    │  │                     │
│   SafetyConnect)    │  │  ✗ No mechanistic   │  │  60-70% of total    │
│                     │  │    context          │  │  assessment cycle    │
│                     │  │                     │  │  time                │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
```

**Bullets:**
- Case management is solved — mature systems handle intake, workflow, and submission
- Statistical signal detection is functional — disproportionality tools exist and work within known limits
- **Evidence assembly is the unsolved layer** — gathering, reading, extracting, normalizing, and cross-referencing evidence from heterogeneous sources
- This layer consumes **60-70% of the total assessment cycle time** (ArcaScience measurement across multiple enterprise deployments)
- It's where human expertise is most wasted on low-value tasks

**Speaker notes:**
"Let's be honest about what works and what doesn't. Case management systems — Argus, AERS, SafetyConnect — handle intake, routing, and regulatory submission. They work. Signal detection tools run disproportionality analysis and flag potential signals. They work within known statistical limits. The gap is in what I call the evidence assembly layer. Between 'we have a signal to evaluate' and 'here is our scientific assessment,' there is a vast manual process of gathering published literature, reading hundreds of papers, extracting adverse events, normalizing terminology, cross-referencing across sources, and assembling a coherent evidence picture. This layer consumes 60-70% of the total assessment cycle across our clients. It's where PhD-level scientists spend most of their time doing work that doesn't require a PhD — reading, extracting, formatting. That's the layer where AI can have the most impact."

---

### SLIDE 8 — THE GENERATIVE AI TRAP

**Title:** Why General-Purpose LLMs Are Not the Answer for Safety

**Bullets:**
- Generative AI (GPT-4, Claude, Gemini) can summarize text — but **cannot guarantee factual accuracy** in extraction
- Published benchmark: GPT-4 achieves **67% precision** on structured adverse event extraction from biomedical literature (Chen et al., AI in Medicine, 2025)
- Generative models **hallucinate** — they produce plausible but fabricated information. In safety, a hallucinated adverse event is an unacceptable regulatory risk
- No audit trail: generative outputs cannot be traced to source documents at the entity level
- FDA January 2025 Draft Guidance demands **credibility assessment** and **context-of-use validation** for AI in drug development — generative black boxes fail both criteria
- EMA-FDA Joint Guiding Principles (January 2026): human-centric, risk-based approach with **proportional validation** and **clear context of use**

**Speaker notes:**
"I want to address the elephant in the room. Everyone in this room has been asked by their leadership: 'Can't ChatGPT do this?' The answer is: not for safety. Generative large language models are extraordinary tools for many tasks, but they have three properties that make them unsuitable for pharmacovigilance evidence extraction. First, they hallucinate — they generate plausible but invented information. In safety, a fabricated adverse event could trigger unnecessary regulatory action or, worse, mask a real signal. Second, their precision on structured extraction is inadequate — 67% precision means one in three extracted entities is wrong. Third, they offer no source-level audit trail. You cannot trace a GPT output back to the specific sentence in the specific document that supports it. The FDA's January 2025 guidance and the joint EMA-FDA principles from last month both emphasize credibility, validation, and traceability. General-purpose generative AI doesn't meet that bar for safety applications."

---

---

## BLOCK III: AN EVIDENCE-STRUCTURING APPROACH (8 min)

---

### SLIDE 9 — A DIFFERENT AI ARCHITECTURE FOR SAFETY

**Title:** Task-Specific Models, Not General-Purpose Generation

**Bullets:**
- **24 small language models**, each trained for one specific extraction task — not generative, not therapeutic-area-specific
- Trained by clinicians on cross-therapeutic corpus: **10M+ case reports, 500K+ trial records, 2M+ abstracts, 100K+ regulatory documents**
- Training methodology: 2 independent clinician annotators per document, 80/20 temporal split (train pre-2023, test 2023-2025), annual audit cycles
- Each model does **one thing well**: classify a document type, identify a section, extract an adverse event, normalize to MedDRA, link to a knowledge graph

**Layout:** Pipeline visualization:

```
  INGEST → CLASSIFY → SECTION → EXTRACT → RELATE → NORMALIZE → LINK → TEMPLATE
    │          │          │         │          │          │         │        │
    ▼          ▼          ▼         ▼          ▼          ▼         ▼        ▼
  [Audit]   [Audit]   [Audit]   [Audit]   [Audit]   [Audit]   [Audit]  [Audit]

  Every intermediate output is inspectable. Every extracted entity is
  linked to its source document, extraction model, and timestamp.
```

**Speaker notes:**
"So what does an AI architecture for safety actually look like? It looks nothing like ChatGPT. We use 24 small language models — each one does exactly one task. One classifies document types. Another identifies sections. Four are chained together just for adverse event extraction: extract, structure, cluster, normalize. They're trained by clinicians — two independent annotators per document — on a corpus that spans therapeutic areas and data types. Why small, task-specific models? Because in safety, you don't need creative text generation. You need precise, auditable extraction. A small model trained on one task achieves 92% precision on adverse event extraction. GPT-4 achieves 67% on the same task. The trade-off is that our models can't write you a poem. But they can tell you exactly which adverse event appeared in which sentence of which document, and you can verify it."

---

### SLIDE 10 — THE KNOWLEDGE GRAPH: CONNECTING THE DOTS

**Title:** From Isolated Data Points to Connected Evidence

**Bullets:**
- Extracted entities are **normalized against standard ontologies**: MedDRA (restructured), SNOMED CT, ChEBI, Disease Ontology
- **Knowledge graph** links entities across sources: drugs ↔ adverse events ↔ mechanisms of action ↔ patient populations ↔ biomarkers ↔ study characteristics
- Enables queries human review cannot scale:
  - *"Across all published sources, what is the complete evidence for drug X causing cardiac events, stratified by mechanism, dose, population, and study type?"*
  - *"Which other drugs in this pharmacological class have shown similar hepatotoxicity signals, and through what pathway?"*
- This is where **biological plausibility** becomes computable — not by generating conclusions, but by surfacing mechanistic evidence from across the full corpus that a human assessor can evaluate

**Suggested visual:** Knowledge graph node-link diagram showing a drug at center, connected to adverse events (colored by source type: literature = blue, spontaneous = orange, trial = green), with mechanism-of-action nodes bridging to pharmacological class members.

**Speaker notes:**
"This is the key innovation, and it's not the AI models — it's the knowledge graph they feed into. When you extract an adverse event from a published paper and normalize it to MedDRA, that's useful. But when you link it to the same adverse event extracted from clinical trial data, connected to a mechanism of action shared by three other drugs in the same class, connected to a biomarker pattern seen in a real-world evidence database — now you have something a human assessor can work with. You have structured evidence for biological plausibility. The graph doesn't make the assessment. It surfaces the mechanistic connections that would take an assessor weeks to find manually — if they found them at all. When we supported a monoclonal antibody benefit-risk evaluation, the knowledge graph surfaced 50+ key inflammatory adverse events from 32 million open-access data points plus 5,200 pages of internal data. The literature review that would have taken 18 months was completed in 2 weeks. Not because AI made the assessment, but because AI assembled the evidence the assessor needed."

---

### SLIDE 11 — ADDRESSING BRADFORD HILL IN PRACTICE

**Title:** Structuring Evidence for Causality Assessment

**Bullets:**
- Bradford Hill criteria remain the gold standard for causality reasoning — but applying them requires **systematic evidence from multiple source types**
- The platform structures evidence along Bradford Hill-relevant dimensions:

| Criterion | What the platform extracts | Source types leveraged |
|-----------|---------------------------|----------------------|
| **Temporality** | Temporal relationships between drug admin and event onset | Case reports, trial data, literature |
| **Dose-response** | Dose escalation patterns and event frequency | Trial data, literature, FAERS |
| **Dechallenge/rechallenge** | Drug withdrawal and re-introduction outcomes | Case reports, case series |
| **Consistency** | Same signal across independent datasets and geographies | All sources cross-linked |
| **Biological plausibility** | Mechanism-of-action, pathway, and class-effect evidence | Literature, knowledge graph |
| **Specificity** | Drug-event association distinctness | Cross-class comparison |

- The assessor gets **structured, source-linked evidence per criterion** — not a score, not a recommendation, but organized evidence for human judgment

**Speaker notes:**
"Bradford Hill criteria are how we think about causality in pharmacoepidemiology. But applying them rigorously to every safety signal is extraordinarily labor-intensive because each criterion requires different types of evidence from different sources. Temporality needs case-level data. Dose-response needs trial data. Biological plausibility needs mechanistic literature. Consistency requires cross-referencing independent databases. No single assessor has time to systematically assemble all of this for every signal. What the platform does is structure the evidence along these dimensions automatically. When you open a signal assessment, you see: here are the temporal patterns extracted from case reports. Here is the dose-response data from clinical trials. Here is the dechallenge/rechallenge evidence. Here are the mechanism-of-action connections that support or undermine biological plausibility. The assessor still makes the judgment. But instead of spending weeks assembling the evidence, they spend their time where their expertise matters — evaluating it."

---

### SLIDE 12 — WHAT THIS IS NOT

**Title:** Boundaries Matter — What AI Should Not Do in Safety

**Bullets:**
- This is **not a decision-making system** — it structures evidence for human experts to make better-informed decisions
- It does **not generate free text** — every output is extracted and linked, not generated
- It does **not assess study quality** — that remains the assessor's domain
- It does **not replace the assessor** — it compresses the 60-70% of cycle time spent on evidence assembly so the assessor can spend more time on assessment
- It does **not process imaging or omics data** (these are roadmap items)
- It is **not therapeutic-area-specific** — the same 24 models operate across all drugs, diseases, and therapeutic areas via pipeline configuration

**Speaker notes:**
"I want to be explicit about what this is not, because overclaiming in AI is endemic and corrosive — especially in regulated industries. This is not a system that tells you whether a drug is safe. It does not generate conclusions. It does not write regulatory text that hasn't been extracted from a source. It does not assess study quality — that's the assessor's job and we deliberately keep it that way. What it does is compress the evidence assembly bottleneck. If your assessors currently spend 60-70% of their time gathering, reading, and extracting evidence, and 30-40% actually evaluating it, we aim to reverse that ratio. More time on science. Less time on data handling."

---

---

## BLOCK IV: PROOF IT WORKS — REAL CASES (5 min)

---

### SLIDE 13 — VALIDATION METRICS

**Title:** Published, Peer-Reviewed Performance

| Metric | ArcaScience | GPT-4 Baseline | Source |
|--------|-------------|----------------|--------|
| AE extraction precision | **92%** | 67% | Chen et al., AI in Medicine, 2025 |
| AE extraction F1 score | **94%** | — | ArcaScience validation, peer-reviewed |
| AE extraction recall | **89%** | — | ArcaScience validation, peer-reviewed |
| Aggregate F1 (all extraction tasks) | **0.90** | — | Cross-therapeutic validation |

**Additional validation:**
- **6 peer-reviewed publications** (AI in Medicine, BMC Medical Informatics, J. Pharmacoepidemiology, TIRS)
- Independent BRA expert evaluation (2025): **80% reduction in BRA project time**
- Temporal validation split: models trained pre-2023, tested on 2023-2025 data — no data leakage
- Annual audit cycles with clinician re-annotation

**Speaker notes:**
"Numbers matter in this room, so here they are. On adverse event extraction from biomedical literature, our task-specific models achieve 92% precision versus 67% for GPT-4 on the same benchmark. F1 score of 94%. These aren't marketing numbers — they're published in peer-reviewed journals and validated on temporally held-out data: models trained on pre-2023 data, tested on 2023-2025 publications. The difference between 92% and 67% precision isn't incremental — it's the difference between a tool you can trust in a regulatory workflow and one you can't."

---

### SLIDE 14 — CASE EVIDENCE: WHAT CHANGES IN PRACTICE

**Title:** Real-World Impact Across Enterprise Deployments

**Case 1: Monoclonal Antibody Benefit-Risk (Sanofi)**
- Task: Full benefit-risk evaluation of a monoclonal antibody across 1st and 2nd generation
- Input: 32 million open-access datasets + 5,200 pages of internal sponsor data
- Output: Predictive benefit-risk value tree, cross-comparison analysis, **50+ key inflammatory adverse events** identified, **64 key biomarkers** for clinical confirmation
- Impact: Literature review reduced from **18 months to 2 weeks**

**Case 2: Drug Repurposing Signal Detection (Paris Brain Institute)**
- Task: From 100 marketed drugs, identify candidates for glioblastoma repurposing via BBB penetration evidence
- Output: Safety datapoints connected to BBB-crossing identification (ocular, neurological, auditory AE patterns)
- Impact: **3 drugs identified as compatible**, 2 now in Phase 2 clinical trials

**Case 3: Rare Disease Safety Signal (Sanofi)**
- Task: Evaluate thromboembolic risk in a rare genetic disorder drug program
- Outcome: Platform surfaced thromboembolic risk signals from **9x more evidence sources** than manual review
- Impact: Development strategy redirected **before Phase III** — avoiding potential late-stage failure

**Speaker notes:**
"Three cases that illustrate different applications. First: a full monoclonal antibody benefit-risk evaluation. The evidence assembly — 32 million open-access data points plus 5,200 pages of internal data — was reduced from an 18-month manual literature review to 2 weeks. The assessors spent those two weeks evaluating, not extracting. Second: a drug repurposing project where the knowledge graph identified blood-brain barrier penetration evidence across 100 marketed drugs by linking adverse event patterns to mechanism-of-action data. Three candidates were identified. Two are now in Phase 2 trials. Third: in a rare disease program, the platform surfaced thromboembolic risk from 9 times more evidence sources than manual review had identified. The development team redirected the program before Phase III, potentially avoiding a late-stage safety failure. In each case, the AI didn't make the decision. It assembled evidence the human experts needed to make better decisions, faster."

---

### SLIDE 15 — SCALE AND REGULATORY ACCEPTANCE

**Title:** Enterprise-Grade Deployment

**Bullets:**
- **50+ regulatory submissions** supported across **12 therapeutic areas** — outputs incorporated into FDA, EMA, and PMDA filings
- **Novartis**: Deployed across **300+ products** — $12M operational savings
- **AstraZeneca**: **68% BRA cycle reduction** across 12 compounds
- **ICON**: **90% QC reduction** through automated traceability
- Compliance: **ISO 27001, SOC 2 Type II, GAMP 5 Cat. 5, FDA 21 CFR Part 11, HIPAA, GDPR, HDS**
- EMA-FDA Joint Principles alignment: human-centric design, risk-based validation, full auditability, clear context of use

**Speaker notes:**
"This is not a research project or a proof of concept. It's deployed at enterprise scale. More than 50 regulatory submissions across 12 therapeutic areas. Novartis runs it across 300+ products. AstraZeneca achieved a 68% reduction in benefit-risk assessment cycle time across 12 compounds. The platform carries ISO 27001, SOC 2 Type II, GAMP 5, and FDA 21 CFR Part 11 certifications — because in pharma, an AI tool without regulatory-grade compliance is a liability, not an asset."

---

---

## BLOCK V: LOOKING FORWARD & OPEN DISCUSSION (3 min)

---

### SLIDE 16 — THE REGULATORY MOMENT

**Title:** The Window Is Open — Regulators Are Ready

**Bullets:**
- **EMA-FDA Joint Guiding Principles** (January 2026): 10 principles for responsible AI in drug development — human-centric, risk-based, proportional validation
- **FDA EDSTP** (Emerging Drug Safety Technology Program, June 2024): dedicated program for AI in pharmacovigilance
- **CIOMS Working Group XIV**: first global consensus effort on AI in pharmacovigilance — draft report released 2025
- **DARWIN EU** operationalized: EMA investing in real-world data infrastructure
- **500+ FDA submissions** incorporating AI components by fall 2024
- The question is no longer "will regulators accept AI in safety?" — it's **"which AI approaches meet the bar?"**

**Speaker notes:**
"We are in a unique regulatory moment. The EMA and FDA jointly published 10 guiding principles for AI in drug development last month. The FDA created a dedicated Emerging Drug Safety Technology Program in 2024. CIOMS convened its first working group on AI in pharmacovigilance. DARWIN EU is operationalized. Over 500 FDA submissions already incorporate AI components. The regulatory door is open — but it's open to AI that meets specific criteria: human-centric design, risk-based validation, auditability, and clear context of use. Not all AI approaches meet that bar. The approaches that will succeed in safety are those built specifically for the regulatory requirements of pharmacovigilance — not general-purpose tools adapted after the fact."

---

### SLIDE 17 — DISCUSSION PROMPT

**Title:** For the Room

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   1. In your organization, what percentage of safety            │
│      assessment time is spent on evidence assembly              │
│      vs. actual scientific evaluation?                          │
│                                                                 │
│   2. When you detect a statistical signal, how do you           │
│      currently assess biological plausibility — and             │
│      how comprehensive is that process?                         │
│                                                                 │
│   3. What would your assessors do with 60-70% of               │
│      their time back?                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Speaker notes:**
"I want to use the remaining time for the conversation this room should be having. Three questions. First: in your organization, how much of your safety assessment time goes to assembling evidence versus actually evaluating it? Second: when you flag a statistical signal, what does your biological plausibility assessment actually look like — how systematic is it, and how much depends on individual assessor knowledge? Third — and this is the one I'm most interested in: if your assessors got 60-70% of their evidence assembly time back, what would they do with it? What safety questions would you finally have time to investigate? I'd love to hear from the room."

---

---

## APPENDIX SLIDES (Backup — do not present unless asked)

---

### APPENDIX A — TECHNICAL ARCHITECTURE DETAIL

**8-Stage Pipeline with Model Categories:**

| Stage | Models | Function | Validation |
|-------|--------|----------|------------|
| INGEST | Document parser | Consume PDF, XML, DOC, any semantic source | Format coverage testing |
| CLASSIFY | Document type classifier | Case report, RCT, observational, meta-analysis, etc. | 92% precision |
| SECTION | Section layering model | Abstract, methods, results, discussion routing | Section-level F1 |
| EXTRACT | 4-model AE chain; 4-model efficacy chain; patient info; drug/dosage | Entity-level extraction with severity, temporality, outcomes | 94% F1 (AE), 89% recall |
| RELATE | Relation extraction models | Link drug → event → context within sentences | Relation-level F1 |
| NORMALIZE | Ontology mapping models | MedDRA, SNOMED CT, ChEBI, Disease Ontology | Coding accuracy vs. manual |
| LINK | Knowledge graph linker | Cross-source entity resolution, mechanism-of-action bridging | Graph completeness |
| TEMPLATE | Output generation | PSUR, PBRER, RMP, CTD 2.5, BRA documentation | Regulatory acceptance rate |

---

### APPENDIX B — REGULATORY COMPLIANCE DETAIL

| Standard | Status | Relevance |
|----------|--------|-----------|
| ISO 27001 | Certified | Information security management |
| SOC 2 Type II | Certified | Service organization controls |
| GAMP 5 Category 5 | Compliant | Computerized system validation |
| FDA 21 CFR Part 11 | Compliant | Electronic records/signatures |
| HIPAA | Compliant | US patient data protection |
| GDPR | Compliant | EU data protection |
| HDS | Certified | French healthcare data hosting |
| ALCOA+ | Aligned | Data integrity principles |

---

### APPENDIX C — PUBLICATION LIST

1. Chen et al. — *AI in Medicine*, 2025 (task-specific SLMs vs. GPT-4 on AE extraction)
2. *BMC Medical Informatics* — cross-therapeutic validation of extraction pipeline
3. *Journal of Pharmacoepidemiology*, 2024 — 3x signal detection improvement vs. manual review
4. *TIRS* — benefit-risk methodology validation
5. Two additional peer-reviewed publications (2023-2025)

---

### APPENDIX D — COMPETITIVE POSITIONING

| Approach | Strengths | Limitations for PV |
|----------|-----------|-------------------|
| **General-purpose LLMs** (GPT-4, Claude) | Broad capability, text generation | 67% extraction precision, hallucination risk, no audit trail |
| **Manual CRO review** | Human judgment, flexible | Months per assessment, does not scale, assessor-dependent |
| **Case management systems** (Argus, AERS) | Mature, regulatory-accepted | Handle intake/workflow, not evidence assembly |
| **Statistical signal tools** | Proven DA methods | No biological plausibility, high false-positive rate |
| **Task-specific SLMs + Knowledge Graph** (ArcaScience) | 92% precision, auditable, scalable, cross-source linking | Does not process imaging/omics, does not assess study quality |

---

## PRESENTER PREPARATION NOTES

### Tone Calibration
- **You are speaking to peers**, not prospects. These are 100 safety specialists who know the problems intimately. Do not explain pharmacovigilance basics. Do not oversimplify.
- **Lead with the problem, not the product.** The first 14 minutes should feel like a scientific talk about the state of the field. ArcaScience capabilities appear only in Block III.
- **Be honest about limitations.** Explicitly stating what the technology cannot do builds more credibility with this audience than any performance metric.
- **Use the word "assessor" not "user."** This audience identifies as safety scientists, not end users.
- **Avoid**: "revolutionary," "game-changing," "transformative," "unprecedented," "cutting-edge," "state-of-the-art." Use: "structured," "auditable," "evidence-based," "validated," "published."

### Likely Audience Questions & Responses

**Q: "How do you handle data confidentiality with sponsor data?"**
A: Client data remains on the client's infrastructure when confidentiality requires it. For published literature, we process publicly available sources only. For internal data, we offer secure deployment options with HDS certification and GDPR compliance.

**Q: "What about hallucination risk?"**
A: Our models are non-generative — they extract and link, they don't generate text. Every output is traced to a source document, extraction model, and timestamp. There is no free-text generation step in the pipeline. Hallucination is a property of generative models; extraction models produce false positives and false negatives, which we measure and publish.

**Q: "67% GPT-4 precision — is that a fair comparison?"**
A: It's published in Chen et al. (AI in Medicine, 2025) on the same adverse event extraction benchmark. GPT-4 is a general-purpose model; our models are purpose-built for this task. The comparison illustrates why task-specificity matters, not that GPT-4 is a bad model.

**Q: "Can this work for rare diseases where literature is sparse?"**
A: Yes — the knowledge graph cross-references pharmacological class evidence. For rare diseases, mechanism-of-action linking surfaces relevant evidence from related compounds and pathways even when direct drug-specific literature is limited. We demonstrated this in a rare disease program at Sanofi where the platform identified thromboembolic risk from 9x more sources than manual review.

**Q: "What's the cost?"**
A: Enterprise deployments range from $200K-$300K per year — less than the cost of 2 FTEs. Pilots are structured as 3-month engagements at defined scope with success criteria agreed upfront.

**Q: "How does CIOMS Working Group XIV view AI in PV?"**
A: Their 2025 draft report acknowledges both the opportunity and the risks. Key emphasis on validation, transparency, human oversight, and regulatory-grade evidence of performance. Our architecture was designed to align with these principles — task-specific models, auditable pipeline, human-in-the-loop by design.

---

## KEY NUMBERS — QUICK REFERENCE

| Stat | Value | Use in presentation |
|------|-------|-------------------|
| PubMed citations | 39M+ | Slide 2 — scale of knowledge |
| Papers per year | 1.5M (4,000/day) | Slide 2 — growth rate |
| VigiBase reports | 40M+ | Slide 2 — global ADR scale |
| EudraVigilance ICSRs | 29.3M (1.8M/year) | Slide 2, 4 — EU-specific |
| FDA annual AE reports | ~2M/year | Slide 4 — US-specific |
| ADR underreporting rate | 94% median | Slide 2 — the iceberg |
| DA false-positive variability | 60% of pairs | Slide 5 — signal detection limits |
| DA studies lacking definitions | 78% | Slide 5 — methodology gaps |
| PV budget on case processing | 40-80% | Slide 4 — resource allocation |
| Evidence assembly % of cycle | 60-70% | Slide 7, 12 — the bottleneck |
| ArcaScience AE precision | 92% | Slide 13 — validation |
| GPT-4 AE precision | 67% | Slide 8, 13 — comparison |
| ArcaScience F1 | 94% | Slide 13 — validation |
| BRA time reduction | 80% | Slide 13 — impact |
| Regulatory submissions | 50+ | Slide 15 — scale |
| Therapeutic areas covered | 12 | Slide 15 — breadth |
| Peer-reviewed publications | 6 | Slide 13 — credibility |
| Task-specific models | 24 | Slide 9 — architecture |
| Training corpus (case reports) | 10M+ | Slide 9 — scale |
| Training corpus (abstracts) | 2M+ | Slide 9 — scale |
