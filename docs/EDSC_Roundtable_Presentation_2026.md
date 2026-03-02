# CHALLENGES IN LEVERAGING ALL BIOMEDICAL KNOWLEDGE & HOW AI CAN HELP

## European Drug Safety Conference 2026 — Roundtable Presentation
**Format:** 30-minute roundtable | **Audience:** ~100 safety specialists | **Room:** Gloria B, C, D
**Presenter:** ArcaScience

---

# NARRATIVE ARC

> **Act I** (0:00–8:00) — The AI gold rush hits pharma: $632B in spending, 88% pilot failure. But first — let's give AI its due. Then: why is so much of it failing?
>
> **Act II** (8:00–15:00) — The answer: LLMs are structurally broken for drug safety. From the Tiramisu Test to Yann LeCun's departure from Meta — why the world's leading AI scientist says "LLMs are a dead end" and what that means for our field.
>
> **Act III** (15:00–23:00) — Who we are at ArcaScience. Our BRA platform. And the strategy that works: Small Language Models in Ensemble AI architectures — 92% precision where GPT-4 gets 67%.
>
> **Act IV** (23:00–27:00) — The new hope: Latent World Models. From statistical correlation to mechanistic simulation. The future where we predict adverse events before they happen.
>
> **Act V** (27:00–28:00) — Three Takeaways. The three things to remember from this room.
>
> **Coda** (28:00–30:00) — Discussion.

---

# PRESENTATION TIMING & STRUCTURE

| Act | Time | Slides | Core Message |
|-----|------|--------|-------------|
| I. The AI Reality Check | 0:00–8:00 | 1–7 | AI is transforming medicine — but pharma is spending billions on the wrong kind |
| II. Why LLMs Fail Drug Safety | 8:00–15:00 | 8–14 | Structural, not fixable — and the smartest people in AI agree |
| III. ArcaScience + The Strategy That Works | 15:00–23:00 | 15–22 | Who we are, our BRA platform, and why SLMs + Ensemble AI deliver |
| IV. The New Hope: Latent World Models | 23:00–27:00 | 23–26 | From correlation to simulation |
| V. Three Takeaways | 27:00–28:00 | 27 | The three things to remember |
| Coda. Discussion | 28:00–30:00 | 28 | Engage the room |

---

# ACT I: THE AI REALITY CHECK (0:00–8:00)

---

## SLIDE 1 — Title Slide

**Title:**
### CHALLENGES IN LEVERAGING ALL BIOMEDICAL KNOWLEDGE & HOW AI CAN HELP

**Subtitle:** What works, what doesn't, and what comes next

**Visual:** ArcaScience logo. EDSC 2026 branding. Clean, dark.

**Speaker notes:**
> Thank you. I'm [Name] from ArcaScience. Over the next 30 minutes, I want to take you on a journey — not through what AI could theoretically do for drug safety, but through what's actually happening: what's working, what's failing spectacularly, and what the next generation of AI looks like for our field. I'll make claims. I'll back them with data. And I'll be honest about what we don't know yet. Let's start with the uncomfortable part.

---

## SLIDE 2 — The AI Gold Rush

**Title:**
### $632 Billion. That's How Much the World Will Spend on AI by 2028.

**Visual:** Single massive number. Then reveal:

| IDC Forecast | Amount | Growth |
|-------------|--------|--------|
| Total AI spending by 2028 | **$632 billion** | 29% CAGR |
| GenAI spending by 2028 | **$202 billion** | 59% CAGR |
| AI cumulative economic impact by 2030 | **$19.9 trillion** | 3.5% of global GDP |

**Source:** IDC Worldwide AI and Generative AI Spending Guide, 2024

**Speaker notes:**
> IDC projects worldwide AI spending will reach $632 billion by 2028 — more than doubling from today. GenAI alone hits $202 billion, growing at nearly 60% per year. Organizations increased AI infrastructure spending by 166% year-over-year in Q2 2025. Eighty-two billion dollars in a single quarter. The AI cumulative economic impact through 2030? $19.9 trillion. This is the largest technology investment cycle in human history. So the question isn't whether AI matters. The question is: is this investment paying off?

---

## SLIDE 3 — The Pharma Bet

**Title:**
### Pharma Is All In

**Visual:** Key pharma AI statistics:

- **Over 40%** of life sciences firms say AI/automation is the ONE investment they won't cut, even amid geopolitical headwinds *(IDC, Nov 2024)*
- **73%** of global pharma organizations actively piloting or deploying agentic AI *(IDC 2025)*
- **65%** of drug discovery will be GenAI-powered by 2027 *(IDC FutureScape)*
- **6 GenAI use case segments** in life sciences identified by IDC — including **Patient Safety** as #1

**Bottom text:** "Patient safety is IDC's first named use case for GenAI in life sciences."

**Speaker notes:**
> Pharma is not standing on the sidelines. Over 40% of life sciences firms say AI is the one budget they're protecting regardless of macro conditions. 73% are actively pursuing agentic AI. IDC predicts 65% of drug discovery will be GenAI-powered by 2027. And here's what matters to this room: when IDC mapped GenAI use cases for life sciences, they named six segments. Patient safety was number one. Not drug design. Not marketing. Safety. So our field is squarely in the crosshairs of the biggest technology wave in history. Now here's the problem.

---

## SLIDE 4 — The 88% Failure Rate

**Title:**
### For Every 33 AI Pilots, Only 4 Make It to Production

**Visual:** Stark infographic:

```
  AI Pilots Launched:      ██████████████████████████████████  33
  Made it to Production:   ████                                 4

  Failure Rate:            88%
```

**Supporting data:**
- **80%** of healthcare AI projects fail to scale beyond pilot *(HIT Consultant, 2026)*
- **95%** of GenAI pilots fail to deliver ROI *(MIT NANDA Institute)*
- Only **1% of organizations** have achieved an optimized, AI-fueled enterprise *(IDC Maturity Model, 2025)*
- **51%** are still in Stage 2 of 5 — "Opportunistic" *(IDC, n=1,534)*

**Speaker notes:**
> For every 33 AI pilots a company launches, only 4 make it to production. That's IDC data. An 88% failure rate. MIT's NANDA Institute puts it even more starkly: 95% of GenAI pilots fail to deliver measurable ROI. In healthcare specifically, 80% of AI projects never scale beyond pilot. When IDC benchmarked 1,534 organizations on their AI maturity — five stages from "Ad Hoc" to "Optimized" — they found that only 1% have reached the optimized state. Over half are still at stage two. The pharma industry is spending aggressively on AI. It is getting very little back. Why?

---

## SLIDE 5 — Where the Money Goes (and Doesn't Return)

**Title:**
### The Data Preparation Trap

**Visual:** Pie chart or diagram:

```
How data science teams spend their time:

  ┌────────────────────────────────────────┐
  │                                        │
  │      DATA PREPARATION: 50%             │  <- Cleaning, formatting, normalizing
  │                                        │
  ├────────────────────────────────────────┤
  │  Model Training: 20%                   │
  ├────────────────────────────────────────┤
  │  Deployment: 15%                       │
  ├────────────────────────────────────────┤
  │  Actual insight generation: 15%        │
  └────────────────────────────────────────┘
```

**IDC finding:** *"Virtually ALL IDC AI surveys indicate that data quality, quantity, and access are among the top challenges to scaling AI."*

**Plus:** Healthcare has the most fragmented data of any industry — 80% unstructured, heterogeneous tech stacks, no interoperability standards

**Speaker notes:**
> IDC found that data science teams spend 50% of their time on data preparation before they even begin building AI models. Half their time. Just getting data into a usable state. And here's the kicker: healthcare and life sciences have the most fragmented, heterogeneous data landscape of any industry. 80% of health data is unstructured — clinical notes, discharge summaries, pathology reports. Every EHR system is configured differently. Every database uses different terminologies. MedDRA doesn't map to MeSH. SNOMED doesn't align with ICD. And pharmacovigilance data is spread across FAERS, EudraVigilance, VigiBase, published literature, clinical trials, and EHRs — each with their own structures. So when pharma companies take general-purpose AI tools and point them at this landscape, what happens? They fail. And they fail for a very specific reason.

---

## SLIDE 6 — The Root Cause

**Title:**
### The Problem Isn't AI. It's the Wrong Kind of AI.

**Visual:** The IDC prediction, highlighted:

> **IDC (Bio-IT World 2025):**
> *"By 2027, domain-specific GenAI tools fine-tuned for pharma applications will deliver a **3-5x higher ROI** than general-purpose foundation models, particularly in regulatory-sensitive contexts."*
>
> -- Dr. Nimita Limaye, Research VP, Life Sciences R&D Strategy & Technology, IDC

**Key point:** "General-purpose LLMs are the wrong tool for drug safety. IDC sees it. The research proves it. And the world's leading AI scientist has staked his career on it."

**Speaker notes:**
> IDC has made a very specific prediction: by 2027, domain-specific AI tools will deliver 3 to 5 times the return of general-purpose foundation models in pharma. Three to five times. Not a marginal improvement — a categorical difference. Why? Because general-purpose LLMs — GPT-4, Claude, Gemini — were not designed for drug safety. They were designed to sound intelligent about everything. And there's a fundamental difference between sounding intelligent and being reliable. But before I go further into the critique, let me be fair. AI has earned extraordinary wins in medicine. Let's give it its due.

---

## SLIDE 7 — Let's Give AI Its Due

**Title:**
### AI Is Already Transforming Medicine — And Rightly So

**Visual:** Grid of real, validated AI wins in pharma/healthcare:

| Achievement | Impact | Source |
|------------|--------|--------|
| AlphaFold 2/3 | Predicted structure of **200M+ proteins** — solved a 50-year biology grand challenge | DeepMind / Nature, 2024 Nobel Prize |
| AI-guided drug candidates | **~80 AI-originated molecules** now in clinical trials, up from 0 in 2020 | BCG, 2025 |
| Radiology AI (FDA-cleared) | **950+ FDA-authorized AI/ML devices** — majority in radiology and cardiology | FDA AI/ML Device Registry, 2024 |
| Clinical trial optimization | **30% faster** patient enrollment using ML-driven site selection | McKinsey, 2024 |
| Adverse event detection (NLP) | **3x improvement** in signal-to-noise ratio using ensemble NLP vs. manual | Scientific Reports, 2022 |
| De-identification at scale | **700M clinical documents** processed at 0.81% error rate | Providence Health / John Snow Labs |

**Key point:** "AI works brilliantly when it's built for a well-defined task, validated rigorously, and kept within its competence boundary."

**Speaker notes:**
> Before I critique anything, let's be fair. AI has produced genuine, peer-reviewed, Nobel-Prize-winning results. AlphaFold solved protein structure prediction — a problem that eluded biology for 50 years. There are now over 80 AI-originated molecules in human clinical trials. The FDA has authorized more than 950 AI/ML medical devices. In our own field, specialized NLP has tripled signal-to-noise ratios in pharmacovigilance. Providence Health used domain-specific AI to de-identify 700 million clinical documents with a sub-1% error rate. This is real. This works. But notice the pattern: every one of these wins shares three properties. First, the AI was purpose-built for a specific, well-defined task — not a general chatbot repurposed for safety. Second, it was rigorously validated against clinical ground truth. Third, it operates within clear competence boundaries. The problem isn't AI itself. The problem is what happens when we take the wrong KIND of AI — general-purpose language models — and point them at the hardest problems in medicine. Let me show you exactly what goes wrong.

---

# ACT II: WHY LLMs FAIL DRUG SAFETY (8:00–15:00)

---

## SLIDE 8 — The Tiramisu Test

**Title:**
### Can AI Make Tiramisu?

**Visual:** A recipe card for tiramisu on the left. On the right, the question:

"Describe step by step how to make tiramisu. Then: if I swap the mascarpone for ricotta, what changes downstream?"

**The failure pattern:**
1. LLMs produce a fluent, plausible recipe (checkmark)
2. But when you modify one ingredient, they cannot reliably trace how that change propagates through every subsequent step (X)
3. They miss: texture changes in the cream layer, structural instability, different set time, altered presentation
4. They confidently describe a result that would fail in any kitchen

**The deeper point:** "This is multi-step procedural reasoning with real-world constraints. LLMs cannot reliably track how a change at step 3 propagates to steps 7, 12, and 15."

**Published evidence:** *"Evaluating LLMs' Reasoning Over Ordered Procedural Steps"* (arXiv:2511.04688, 2024):
- Model performance **declines with increasing sequence length**
- Greater **step displacement** causes further degradation
- Ordered procedural reasoning is "a key aspect of reasoning where many real-world tasks require steps to be completed in a precise order"

**Speaker notes:**
> Let me start with something that sounds absurd. Ask an LLM to make tiramisu. It will give you a beautiful, step-by-step recipe. Now change one variable: swap mascarpone for ricotta. Ask what changes downstream. The model will give you a confident, fluent answer — and it will be wrong. Because it cannot reliably trace how a single change propagates through a multi-step process. Ricotta has higher moisture content, which means the cream layer won't set the same way, which means the structural integrity changes, which means the layering technique needs adjustment, which means the resting time changes, which means the final presentation is different. The LLM misses most of these downstream effects — not because it doesn't "know" about ricotta, but because it cannot perform multi-step procedural reasoning with real-world constraints. Published research from 2024 confirms this: LLM performance on ordered procedural steps degrades as sequence length increases and as step displacement grows. Now here's why this matters for us.

---

## SLIDE 9 — From Tiramisu to Pharmacology

**Title:**
### If AI Can't Track Ricotta Through a Recipe, How Will It Track a Drug Through the Body?

**Visual:** Side-by-side comparison:

| Tiramisu Test | Drug Safety Assessment |
|--------------|----------------------|
| 1 ingredient change | 1 drug interaction |
| ~15 procedural steps | ~20+ biological steps |
| Texture, structure, timing | Metabolism, distribution, effect |
| Fails at step propagation | Must trace: Drug A inhibits CYP3A4, raises Drug B plasma levels, prolongs QTc, arrhythmia risk, higher in CYP2D6 poor metabolizers, compounded by renal impairment |

**Key point:** "Drug safety is the hardest version of the Tiramisu Test. And LLMs can't pass the easy version."

**Speaker notes:**
> Drug safety assessment IS the Tiramisu Test — except infinitely harder. When you assess whether Drug A could cause cardiac arrhythmia, you need to trace: Does Drug A inhibit CYP3A4? If so, does the patient take Drug B, which is CYP3A4-metabolized? If so, Drug B plasma levels rise. Does Drug B prolong QTc? Is the patient a CYP2D6 poor metabolizer? Do they have renal impairment? Each step depends on the previous one. Each variable interacts with every other. If an LLM can't reliably track ricotta through a tiramisu recipe, it cannot reliably trace a drug interaction through human pharmacology. This isn't my opinion. This is mathematics.

---

## SLIDE 10 — The Mathematics of LLM Failure

**Title:**
### Hallucination Is Not a Bug. It's Architecture.

**Visual:** Yann LeCun's exponential error divergence argument, visualized:

```
Token 1 -> Token 2 -> Token 3 -> ... -> Token N

At each token, probability of staying correct: p < 1
After N tokens: p^N -> approaches 0 exponentially

Example: p = 0.98 (98% per-token accuracy)
  After 10 tokens:  0.98^10  = 81.7% correct
  After 50 tokens:  0.98^50  = 36.4% correct
  After 100 tokens: 0.98^100 = 13.3% correct
  After 200 tokens: 0.98^200 = 1.8% correct
```

**Quote:**
> *"Every time an LLM produces a token, the probability that you stay within the set of correct answers decreases — and it decreases exponentially."*
> -- **Yann LeCun**, Chief AI Scientist, Meta; Founder, AMI Labs (Lex Fridman Podcast, March 2024)

**Speaker notes:**
> Yann LeCun — Turing Award winner, chief AI scientist at Meta for 12 years, professor at NYU — has made the clearest technical argument for why LLMs structurally cannot be reliable. It's the exponential error divergence problem. At every token an LLM generates, there is some probability that it takes you out of the set of correct answers. Even if that probability is small — say 2% per token — after 100 tokens you're at 13% probability of still being correct. After 200 tokens, 1.8%. This means hallucinations are not a bug you can fix with better training or smarter prompting. They are a mathematical consequence of autoregressive generation. The longer the output, the more certain the failure. Now think about a pharmacovigilance evidence package — thousands of tokens, dozens of extracted entities, complex relational chains. The math guarantees errors.

---

## SLIDE 11 — What the Evidence Shows

**Title:**
### LLM Failure Rates in Clinical Contexts

**Visual:** Table of published hallucination and failure rates:

| Study | Model | Failure Rate | Context |
|-------|-------|-------------|---------|
| Mount Sinai 2025 | GPT-4o | **50-53%** hallucination | 300 clinical vignettes |
| JMIR 2024 | GPT-4 | **28.6%** fabricated citations | Systematic review references |
| JMIR 2024 | GPT-3.5 | **39.6%** fabricated citations | Systematic review references |
| JMIR 2024 | Google Bard | **91.4%** fabricated citations | Systematic review references |
| NHS Study 2025 | 120B LLM | **53.1%** incorrect | 2.1M patient medication safety |
| JMIR 2025 | All LLMs | **40-50%** accuracy | Clinical safety evaluation (CSEDB) |
| Apple ICLR 2025 | All SOTA | **Up to 65% drop** | One irrelevant clause added |
| Caltech/Stanford 2026 | All SOTA | **7.5% accuracy** | Symbolic re-encoding of arithmetic |

**Key point:** "These are not edge cases. This is the normal operating range of LLMs in clinical contexts."

**Speaker notes:**
> Let me give you the numbers. Mount Sinai tested GPT-4o on 300 clinical vignettes: it hallucinated in 50 to 53% of responses. When LLMs generate references for systematic reviews, GPT-4 fabricates 29% of citations. GPT-3.5 fabricates 40%. Google Bard: 91%. An NHS study tested a 120-billion-parameter model on real medication safety for 2.1 million patients: fully correct in only 47% of cases. When Apple's research team added a single irrelevant clause to grade-school math problems — not even changing the question, just adding noise — LLM performance dropped by up to 65%. Their conclusion, published at ICLR 2025: "We found no evidence of formal reasoning in language models." And on the CSEDB — the clinical safety evaluation database — LLMs achieve 40 to 50% accuracy. Clinical medication error standards require 99 to 99.9% accuracy. The gap is not a rounding error. It's a chasm.

---

## SLIDE 12 — Alice in Wonderland

**Title:**
### "Alice Has 3 Brothers and 2 Sisters. How Many Sisters Does Alice's Brother Have?"

**Visual:** The question on screen. Then the results:

| Model | Correct Answer Rate |
|-------|-------------------|
| GPT-4o | 65% |
| Claude 3 Opus | 43% |
| Most other SOTA models | Severe collapse |

**The answer is 3** (Alice + her 2 sisters). Models give elaborate, confident, wrong explanations.

**Published finding:** *"Standard interventions — enhanced prompting, chain-of-thought, multi-step re-evaluation — failed entirely. Models produced more nonsense, often in lengthier and sometimes more entertaining form."*
-- Nezhurina et al., arXiv:2406.02061 (2024)

**Speaker notes:**
> Here's my favorite one. "Alice has 3 brothers and 2 sisters. How many sisters does Alice's brother have?" The answer is 3 — Alice herself plus her 2 sisters. This is a problem a 10-year-old can solve. GPT-4o gets it right 65% of the time. Claude 3 Opus: 43%. And when they get it wrong, they don't say "I'm not sure." They give elaborate, confident, multi-paragraph explanations of why the wrong answer is right. The researchers tried chain-of-thought prompting. They tried multi-step re-evaluation. They tried enhanced instructions. Result? "Models produced more nonsense, often in lengthier and sometimes more entertaining form." This is not a party trick. This is relational reasoning — understanding perspective shifts. It's the same cognitive operation required to assess whether an adverse event in a patient with three comorbidities on five medications is attributable to Drug A or Drug B. If the model can't count sisters, it can't assess causality.

---

## SLIDE 13 — The Man Who Left a Trillion-Dollar Company Over This

**Title:**
### Yann LeCun: "LLMs Are a Dead End."

**Visual:** Photo of LeCun. Timeline:

- **2018-2024:** Chief AI Scientist, Meta
- **October 2024, Columbia:** *"Existing systems don't understand the world as well as a housecat."*
- **December 2025:** Leaves Meta. Founds **AMI Labs** (Advanced Machine Intelligence). Raises ~EUR 500M at ~EUR 3B valuation.
- **January 2026, Financial Times:** *"LLMs basically are a dead end when it comes to superintelligence."*

**His four missing capabilities in LLMs:**
1. Understanding the physical world
2. Persistent memory
3. True reasoning
4. Hierarchical planning

**The bandwidth argument:**
> *"A 4-year-old child has seen **50 times more data** than the biggest LLMs trained on ALL text publicly available on the internet. That clearly tells you we're never going to get to human-level intelligence by just training on text."*

**Speaker notes:**
> This argument isn't coming from an AI skeptic. It's coming from the man who invented convolutional neural networks, won the Turing Award, and spent 12 years as chief AI scientist at Meta. Yann LeCun left Meta in December 2025 — walked away from one of the most powerful AI research positions in the world — to found AMI Labs, explicitly to build something better than LLMs. He raised half a billion euros. His CEO? Alex LeBrun, former CEO of Nabla — a health AI company. LeCun says LLMs lack four things: understanding of the physical world, persistent memory, true reasoning, and the ability to plan. He points out that a 4-year-old child has processed 50 times more data through vision than the largest LLMs have seen in text. And he makes the structural argument: LLMs are autoregressive token predictors. They don't think before they speak. They generate text without first planning what to say. Hallucination is not a bug — it's the inevitable consequence of this architecture. His exact words to the Financial Times, January 2026: "LLMs basically are a dead end."

---

## SLIDE 14 — Why This Matters for Drug Safety

**Title:**
### What LLMs Fundamentally Cannot Do — And What Drug Safety Requires

**Visual:** The gap table:

| What Drug Safety Requires | LLM Capability | Verdict |
|--------------------------|---------------|---------|
| Causal reasoning (Bradford Hill) | Pattern matching only | **Architectural impossibility** |
| Multi-step inference chains | Degrades exponentially per step | **Mathematically proven to fail** |
| Compositional reasoning at scale | Proven impossible for transformers | **Theoretical impossibility** |
| Distinguishing relevant from irrelevant | Up to 65% drop from one irrelevant clause | **Critical fragility** |
| Traceable evidence (regulatory) | 18-29% fabricated citations | **Unacceptable** |
| Biological simulation | Cannot model dynamics, feedback loops | **Wrong architecture** |
| Continuous learning | Catastrophic forgetting | **Cannot update** |

**References:**
- Compositional reasoning impossibility: *"On Limitations of the Transformer Architecture"*, OpenReview/ICLR — mathematical proof using Communication Complexity
- Causal reasoning impossibility: *"LLM Cannot Discover Causality"*, arXiv:2506.00844

**Speaker notes:**
> Let me map this directly to our work. Drug safety requires causal reasoning — the Bradford Hill criteria. LLMs do pattern matching. Drug safety requires multi-step inference — tracing a drug through metabolic pathways. LLMs degrade exponentially with each step. Drug safety requires compositional reasoning — combining pharmacology, genetics, co-medications, and comorbidities. Researchers have mathematically PROVEN that transformers cannot compose functions at scale. Not "haven't yet" — cannot. It's a theoretical impossibility result from communication complexity theory. Drug safety requires traceable evidence for regulatory submissions. LLMs fabricate 18 to 29% of citations. Drug safety requires understanding biological dynamics — feedback loops, threshold effects, non-linear pharmacokinetics. LLMs have no temporal dynamics mechanism whatsoever. So if LLMs are the wrong tool — what's the right one?

---

# ACT III: ARCASCIENCE & THE STRATEGY THAT WORKS (15:00–23:00)

---

## SLIDE 15 — Who We Are: ArcaScience

**Title:**
### ArcaScience — AI-Powered Evidence Structuring for Drug Safety

**Visual:** Company identity card, clean layout:

```
ArcaScience at a Glance
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  FOUNDED         2018, Paris (Biopark, 13th arrondissement)
  RAISED          $10M total ($7M Series A, September 2025)
  TEAM            Clinicians, NLP engineers, regulatory experts
  CLIENTS         20+ pharma companies — Sanofi, AstraZeneca,
                  GSK, Takeda, Novartis, ICON
  RECOGNITION     Best HealthTech NLP Startup 2023
                  (StartUs Insights, global ranking)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  CORE APPROACH:
  ┌────────────────────────────────────────────┐
  │  24 Small AI Models Trained by Clinicians  │
  │  → Not one giant model that does everything│
  │  → 24 specialist models, each doing one    │
  │    task with clinical-grade precision       │
  └────────────────────────────────────────────┘

  DATA FOUNDATION:  100+ billion structured data points
  REGULATORY:       50+ submissions accepted
                    across FDA, EMA, PMDA (47 countries)
  CERTIFICATIONS:   GAMP 5 | ISO 27001 | SOC 2 Type II
                    21 CFR Part 11 | HIPAA | GDPR | ALCOA+
```

**Key line:** "We don't build chatbots. We build evidence machines."

**Speaker notes:**
> So who's actually doing this the right way? Let me introduce ArcaScience. We're a Paris-based AI company founded in 2018 — before the LLM hype cycle. We raised $10 million, including a $7 million round in September 2025. We serve over 20 pharmaceutical companies, including Sanofi, AstraZeneca, GSK, Takeda, and Novartis. Our core approach is fundamentally different from what you've been hearing about in the AI press. We don't use one giant language model. We deploy 24 small, task-specific AI models — each one trained and validated by clinicians on biomedical data. Each model does exactly one thing: one classifies documents, another extracts adverse events, another normalizes terminology across MedDRA and SNOMED. Together, they form a pipeline that assembles structured evidence from fragmented biomedical data. Over 50 regulatory submissions built on our structured evidence have been accepted across FDA, EMA, and PMDA — across 47 countries. We're GAMP 5 validated, ISO 27001 certified, SOC 2 Type II audited. We don't build chatbots. We build evidence machines.

---

## SLIDE 16 — Our BRA Platform: Benefit-Risk Assessment Reimagined

**Title:**
### Build Your Drug's Benefit-Risk Evaluation in Days, Not Months

**Visual:** Left side — the CIOMS framework mapping. Right side — the transformation metrics.

```
THE PROBLEM WE SOLVE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 "Need for comprehensive integration of medical evidence"
 "Overly long analysis duration"
 "Need to increase characterisation in risk assessment"
 "Challenges in real-time evidence integration"
                                — CIOMS Working Group XII

OUR SOLUTION: The BRA Platform
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  6 automated study types, aligned to CIOMS framework:

  ┌──────────────────┬──────────────────┬──────────────────┐
  │ Disease Analysis │ Clinical Endpoint│ Adverse Events   │
  │ Molecular        │ Comprehensive    │ Full synthesis    │
  │ pathways &       │ endpoint strategy│ of AEs for drug   │
  │ epidemiology     │ analysis         │ and standard of   │
  │                  │                  │ care              │
  ├──────────────────┼──────────────────┼──────────────────┤
  │ Benefit-Risk     │ Benefit-Risk     │ Analysis of      │
  │ Insight          │ Summary          │ Condition        │
  │ Summarized BRA   │ Full tailored    │ Including current│
  │ on your          │ benefit-risk     │ treatment        │
  │ priorities       │ synthesis        │ landscape        │
  └──────────────────┴──────────────────┴──────────────────┘

  BRAD crosswalk: Maps directly to eCTD (2.5.6) and PBRER (18.2)
```

**The proof — two real cases:**

| Case | Challenge | ArcaScience Result | Impact |
|------|-----------|-------------------|--------|
| **Sanofi — monoclonal antibody** | Reveal benefit-risk profile across 32M datasets + 5,200 pages internal data | 27 key inflammatory AEs revealed, 64 biomarkers for clinical confirmation, cross-comparison of 1st vs 2nd gen | Literature review: **18 months → 2 weeks** |
| **Paris Brain Institute — glioblastoma** | From 100 marketed drugs, find candidates for repurposing to glioblastoma (must prove BBB crossing) | Safety dataset linking AEs to blood-brain barrier crossing signals (eye deficiency, headache, hearing issues) | **3 drugs identified**, 2 now in Phase 2 clinical trials |

**Bottom line:** *"Reduce BRA Project Time by 80%"* — independent BRA experts evaluation, 2025

**Speaker notes:**
> Our flagship product is the BRA Platform — Benefit-Risk Assessment. It's inspired by CIOMS Working Group XII and ICH Guideline E2C(R2). Here's what it does: you define your drug and its therapeutic context, and the platform generates six types of automated studies — disease analysis, clinical endpoint study, adverse event reports, benefit-risk insight, benefit-risk summary, and analysis of condition. Each study type maps directly to regulatory documents: eCTD clinical overview section 2.5.6 and PBRER section 18.2. The platform enables real-time weighting configuration — you adjust the importance of each benefit and risk item, and the evaluation updates instantly. Let me give you two real examples. For Sanofi, we analyzed a monoclonal antibody across 32 million open-access datasets plus 5,200 pages of internal clinical data. The result: 27 key inflammatory adverse events revealed, 64 biomarkers identified for clinical confirmation, and a full benefit-risk comparison between first and second generation. Literature review that would have taken 18 months was completed in 2 weeks. For the Paris Brain Institute, we screened 100 marketed drugs for glioblastoma repurposing. The critical question: could these drugs cross the blood-brain barrier? Our pipeline identified safety data points directly connected to BBB crossing — adverse events like eye deficiency, headache, and hearing issues that signal central nervous system penetration. Result: 3 candidate drugs identified, 2 are now in Phase 2 clinical trials. An independent evaluation in 2025 confirmed: our platform reduces BRA project time by 80%.

---

## SLIDE 17 — The Counterintuitive Answer

**Title:**
### Smaller Models, Working Together, Beat Bigger Models Working Alone

**Visual:** Side-by-side:

**The intuition (WRONG):**
```
Bigger model = better results
175B parameters > 110M parameters
GPT-4 > PubMedBERT
```

**The evidence (RIGHT):**

| Benchmark | PubMedBERT (110M params) | GPT-4 (1.7T params) |
|-----------|------------------------|---------------------|
| BioNLP (8 datasets) | **68.5-82.0%** | 68.3% |
| Biomedical fact-checking | **89%** (fine-tuned SLM) | Lower (without fine-tuning) |
| PHI detection F1 | **96%** (Healthcare NLP) | 79% (GPT-4o) |
| AE extraction precision | **92%** (ArcaScience) | 67% (GPT-4) |

**Key line:** "PubMedBERT has **110 million** parameters. GPT-4 has **1.7 trillion**. PubMedBERT outperforms it on 6 of 8 biomedical NLP tasks."

**Source:** *Nature Communications*, 2025: "Traditional fine-tuning outperforms zero/few-shot LLMs in most biomedical NLP tasks."

**Speaker notes:**
> Here's the counterintuitive finding. PubMedBERT has 110 million parameters. GPT-4 has 1.7 trillion — fifteen thousand times larger. And PubMedBERT outperforms GPT-4 on six of eight biomedical NLP benchmarks. Published in Nature Communications, 2025. On protected health information detection — a safety-critical regulatory task — specialized healthcare NLP scores 96% F1. GPT-4o scores 79%. That's a 17-point gap. On adverse event extraction — the core of pharmacovigilance — ArcaScience's domain-specific models achieve 92% precision. GPT-4 achieves 67%. Twenty-five points. Why? Because a small model trained deeply on biomedical data learns the vocabulary, syntax, and semantic relationships of clinical language. A giant model that's seen everything knows nothing deeply. It's like the difference between a specialist cardiologist and a first-year medical student who's read the entire internet.

---

## SLIDE 18 — The Ensemble Architecture

**Title:**
### 24 Specialist Models > 1 Generalist Model

**Visual:** ArcaScience's 8-stage pipeline:

```
STAGE 1: INGEST     | Documents from 6+ source types (PDF, XML, DOC)
                     v
STAGE 2: CLASSIFY    | Document type: RCT, case report, observational, regulatory
                     v
STAGE 3: SECTION ID  | Section boundaries: abstract, methods, results, discussion
                     v
STAGE 4: EXTRACT     | Entities: drugs, events, dosages, temporality, populations
                     v
STAGE 5: RELATE      | Relations: Drug X -> Event Y in Context Z
                     v
STAGE 6: NORMALIZE   | Ontology mapping: MedDRA <-> SNOMED <-> ChEBI <-> Disease Ontology
                     v
STAGE 7: LINK        | Knowledge graph: cross-document entity resolution
                     v
STAGE 8: TEMPLATE    | Structured output: evidence packages for human assessment
```

**Three architectural advantages:**
1. **Precision through specialization** — each model optimized for exactly one task
2. **Auditability at every stage** — every output traces to a source document
3. **Error containment** — a failure in Stage 3 doesn't corrupt Stage 7

**Speaker notes:**
> At ArcaScience, we deploy 24 task-specific small language models in an 8-stage pipeline. Each model does one thing, and does it precisely. Stage 1 ingests documents. Stage 2 classifies them — is this an RCT, a case report, a regulatory document? Stage 3 identifies sections. Stage 4 extracts entities — drugs, adverse events, dosages, temporal relationships. Stage 5 extracts relations — Drug X causes Event Y in what context? Stage 6 normalizes across ontologies — mapping MedDRA to SNOMED to ChEBI. Stage 7 populates a knowledge graph with cross-document entity resolution — so "atorvastatin," "LIPITOR," and "atorvastatin calcium" are recognized as the same compound. Stage 8 generates structured evidence packages for human assessment. Three advantages over a single LLM. First: precision through specialization. Second: auditability at every stage — every extraction traces to a source sentence in a source document. Third: error containment. If Stage 3 makes an error in section identification, it doesn't corrupt the ontology normalization in Stage 6. In a single LLM, errors propagate invisibly through the entire output.

---

## SLIDE 19 — The Evidence

**Title:**
### Ensemble AI Outperforms Everything Else in Drug Safety

**Visual:** Comparison table from published literature:

| Approach | Task | Performance | Source |
|----------|------|-------------|--------|
| ArcaScience (24 SLMs) | AE extraction precision | **92%** | Chen et al., *AI in Medicine*, 2025 |
| GPT-4 | AE extraction precision | 67% | Same benchmark |
| Ensemble (RF+GBM+XGB+NN+SVM) | FAERS signal detection | **75% accuracy** | medRxiv, Feb 2026 |
| XGBoost ensemble | Signal detection | **>95% accuracy** | AbbVie pilot, PMC 2024 |
| GBM | Signal detection AUROC | **0.82** | vs. 0.59 for traditional ROR |
| BERT + ensemble | FAERS text analysis | **F1: 0.86-0.89** | npj Dig Med, 2025 |
| Traditional (PRR, ROR) | Signal detection AUROC | 0.58-0.59 | Regulatory standard |

**Key finding:** *"ML algorithms performed significantly better than methods currently used by regulatory agencies. Both RF and GBM detected 4 out of 5 pre-specified adverse events of infliximab as early as the first year they were reported."*
-- Scientific Reports, 2022

**Speaker notes:**
> The evidence is overwhelming and it's peer-reviewed. ArcaScience's ensemble achieves 92% precision on adverse event extraction where GPT-4 gets 67%. An ensemble of five ML algorithms on FAERS data achieves 75% accuracy in detecting safety signals that traditional statistical methods miss entirely. AbbVie's pilot with XGBoost achieved over 95% accuracy for post-marketing signal detection. And here's the comparison that should change how we think about our tools: gradient boosted machines achieve an AUROC of 0.82 for signal detection. The traditional methods regulators use today — PRR, ROR, information component — achieve 0.59. The standard tools are barely better than a coin flip. Ensemble AI is dramatically better. And critically, these ensemble approaches detected four out of five pre-specified adverse events of infliximab in the very first year they were reported — years before traditional methods would have flagged them.

---

## SLIDE 20 — What It Looks Like in Practice

**Title:**
### From Fragmented Searches to Integrated Evidence

**Visual:** Before/after:

**BEFORE (Human + PubMed + Excel):**
- Literature search: keyword-based, inherently incomplete
- FAERS review: line listings, no biological context
- Evidence assembly: 12-16 weeks for one product
- Cross-referencing: manual, error-prone
- Result: **3 relevant literature sources found** for a rare disease thromboembolic risk

**AFTER (ArcaScience Ensemble AI):**
- 24 models extract, normalize, and cross-reference automatically
- Evidence assembly: **days, not months**
- Cross-referencing: systematic across 6+ source types
- Full audit trail: every data point traceable to source
- Result: **9x more evidence sources found** for same risk signal
- **Outcome: development investment redirected before Phase III. Regulatory submission accepted across 47 countries.**

**Speaker notes:**
> Let me make this concrete with a real case. A top-5 pharmaceutical company had a rare disease program approaching Phase III. Traditional surveillance found 3 literature sources suggesting thromboembolic risk — not enough to act on. Their safety database review was inconclusive. When we applied our 24-model ensemble pipeline, the system identified 9 times more relevant evidence sources. It cross-referenced spontaneous reports with published case series, mechanistic pathway data, and class effect analysis. The convergent evidence was clear: thromboembolic risk was real, scattered across sources that were never connected. The company redirected its development investment before Phase III. The structured evidence was accepted by regulators across 47 countries. The AI didn't make the decision. It assembled the evidence that made the decision obvious. Evidence assembly that would have taken months happened in days.

---

## SLIDE 21 — The Economics

**Title:**
### Domain-Specific AI Is Not Just Better. It's Cheaper.

**Visual:** Cost comparison:

| Factor | GPT-4 (API) | Fine-Tuned SLMs (Self-Hosted) |
|--------|-------------|-------------------------------|
| AE extraction precision | 67% | **92%** |
| Per-inference cost | $30-60 per M tokens | **~$0.05/hr on GPU** |
| Data privacy | Sent to third-party servers | **On-premises, full control** |
| Auditability | Opaque black box | **Per-stage, source-linked** |
| Regulatory compliance | None native | **GAMP 5, 21 CFR Part 11, ALCOA+** |
| Energy per inference | 10-100x higher | **Baseline** |

**Production benchmark (John Snow Labs):**
- **Over 80% cheaper** than Azure/GPT-4o at scale
- **Providence Health System:** 0.81% error rate de-identifying 700M clinical documents
- **Intermountain Healthcare:** 70% efficiency gain across hundreds of millions of documents

**IDC prediction reminder:**
> *"Domain-specific GenAI tools will deliver 3-5x higher ROI than general-purpose foundation models."*

**Speaker notes:**
> And it's not just more accurate — it's dramatically cheaper. GPT-4 API costs $30 to $60 per million tokens. Fine-tuned SLMs running on a T4 GPU cost roughly 5 cents per hour. At production scale — millions of documents — John Snow Labs reports being over 80% cheaper than Azure and GPT-4o. Providence Health System used specialized NLP to de-identify 700 million clinical documents with a 0.81% error rate. GPT-4o on the same task misses 14.6% of protected health information — 18 times more errors. You get higher precision, lower cost, full data privacy, complete auditability, and regulatory compliance. This is exactly what IDC predicted: domain-specific tools delivering 3 to 5 times the ROI.

---

## SLIDE 22 — Why This Is Just the Beginning

**Title:**
### What Ensemble SLMs Solve — and What They Don't

**Visual:** Honest capability assessment:

**What SLM ensembles DO solve:**
- Evidence extraction at scale (92% precision)
- Cross-source entity resolution and normalization
- Structured, auditable evidence assembly
- Systematic literature surveillance
- PSUR/PBRER acceleration (60% cycle time reduction)
- Regulatory-grade traceability

**What they DON'T solve — yet:**
- Predicting adverse events *before* they happen
- Simulating drug-body interactions mechanistically
- Answering "what if we change the dose?" counterfactuals
- Modeling biological dynamics and feedback loops
- Moving from correlation to causation

**Transition:** "To solve these, we need a fundamentally different kind of AI."

**Speaker notes:**
> I want to be honest about the limits of what we do today. ArcaScience's ensemble AI solves the evidence integration problem. It extracts, normalizes, cross-references, and structures safety evidence at scale, with auditability that meets regulatory standards. This is a massive advance over manual review — and the data proves it. But it doesn't predict adverse events before they occur. It doesn't simulate how a drug interacts with human biology. It can't answer counterfactual questions like "what would happen if we doubled the dose in a patient with renal impairment?" It works with the evidence that exists — it doesn't generate new biological understanding. To do that, we need something fundamentally different. And this is where the story gets exciting.

---

# ACT IV: THE NEW HOPE — LATENT WORLD MODELS (23:00–27:00)

---

## SLIDE 23 — From Words to Worlds

**Title:**
### The Next Frontier: AI That Understands How the World Works

**Visual:** Quote and concept:

> *"If AI is to be truly useful, it must understand **worlds**, not just **words**."*
> -- **Fei-Fei Li**, Professor of Computer Science, Stanford; Founder, World Labs ($1B raised)

**What is a World Model?**
An internal representation of how the world works — learned by an AI system — that can:
1. **Predict** the consequences of actions before they happen
2. **Simulate** how states evolve over time
3. **Plan** sequences of actions to achieve goals
4. **Reason** about counterfactuals: "what if X were different?"

**The difference:**
| | LLM | World Model |
|---|-----|------------|
| Predicts | Next word | Next state of the world |
| From | Text patterns | Physics, dynamics, causation |
| Can answer | "What have people written about X?" | "What happens if I do X?" |

**Speaker notes:**
> Fei-Fei Li — the computer scientist behind ImageNet, arguably the most influential dataset in AI history — left Stanford to found World Labs. She raised a billion dollars. Her thesis: "If AI is to be truly useful, it must understand worlds, not just words." A world model is an AI system that has an internal representation of how the world works. Not how text about the world is structured — how the world itself behaves. It can predict consequences before they happen. It can simulate how states evolve over time. And it can reason about counterfactuals — "what if this were different?" LLMs predict the next word. World models predict the next state of reality. That's not an incremental improvement. It's a categorical shift.

---

## SLIDE 24 — The Convergence

**Title:**
### The Biggest Minds and the Biggest Money Are Betting on World Models

**Visual:** The landscape in 2025-2026:

| Who | What | Scale |
|-----|------|-------|
| **Yann LeCun** / AMI Labs | World models for physical understanding | EUR 500M raise, EUR 3B valuation |
| **Fei-Fei Li** / World Labs | Spatial intelligence, 3D world models | $1B raised (incl. $200M Autodesk) |
| **NVIDIA** / Cosmos | World foundation model platform | 9,000 trillion tokens, 20M hours video |
| **Google DeepMind** / Genie 3 | Interactive 3D world generation | 11B params, real-time at 24fps |
| **Meta FAIR** / V-JEPA 2 | Video world model for robot planning | Zero-shot robot control, 62hrs training |
| **Recursion Pharmaceuticals** | Cellular world model (virtual cell) | 65 petabytes, 2.2M samples/week |
| **Isomorphic Labs** (Alphabet) | Molecular simulation, drug design | $600M funding, human trials pending |

**Key result — V-JEPA 2 (June 2025):**
- Trained on 1M+ hours of video
- **Zero-shot robot planning** in environments it has never seen
- Used only **62 hours of unlabeled robot video** for adaptation
- Demonstrates **object permanence and basic physics understanding**
- LeCun: *"We believe world models will usher a new era."*

**Speaker notes:**
> Look at who's betting on this. Yann LeCun left Meta to build world models — half a billion euros. Fei-Fei Li raised a billion dollars. NVIDIA built Cosmos, a world foundation model trained on 9,000 trillion tokens of real-world data. Google DeepMind's Genie 3 generates interactive 3D worlds in real time. And Meta's V-JEPA 2 — LeCun's architecture — achieved something remarkable in June 2025: a model trained on a million hours of video that can plan robot movements in environments it has never seen, using only 62 hours of unlabeled adaptation data. It demonstrates object permanence. Basic physics. An understanding of how the world works — not how text about the world is structured. Now here's the question: what if we built a world model for biology?

---

## SLIDE 25 — World Models for Drug Safety

**Title:**
### Imagine: A Latent World Model for Human Pharmacology

**Visual:** The three levels of AI in drug safety:

```
LEVEL 1 -- TODAY'S STANDARD: Statistical Correlation
  "Drug X is reported with Event Y more than expected"
  -> Disproportionality analysis (PRR, ROR) -> AUC: 0.59

                          |
                          v

LEVEL 2 -- WHERE ARCASCIENCE OPERATES: Evidence Integration
  "Drug X is linked to Event Y across literature, reports,
   and mechanistic data -- with traceable biological plausibility"
  -> Ensemble SLM pipeline -> 92% precision, 9x evidence coverage

                          |
                          v

LEVEL 3 -- THE FUTURE: Mechanistic Simulation
  "Simulating Drug X's mechanism in a latent biological world model
   PREDICTS disruption of Pathway W, leading to Event Y with
   probability P in patients with characteristics C"
  -> Latent world models -> Predictive, not reactive
```

**Already emerging:**
- **VCWorld** (Nov 2025): First explicit biological world model — simulates cellular drug perturbation responses with traceable mechanistic reasoning *(arXiv:2512.00306)*
- **Recursion's Phenom-Beta**: ViT-L/8 trained on 3.5B image crops from 93M microscopy images; 28% improvement at inferring biological relationships
- **AI Virtual Cell** (Cell, Dec 2024): Landmark paper by Genentech/Roche + CZI calling for a "multi-scale, multi-modal neural network that can simulate the behavior of molecules, cells, and tissues"

**Speaker notes:**
> Today, pharmacovigilance operates at Level 1: statistical correlation. We count how often a drug and an event co-occur in reports. That's what PRR and ROR do. The AUC is 0.59 — barely better than a coin flip. ArcaScience operates at Level 2: evidence integration. We extract, normalize, and cross-reference evidence across all sources, building structured plausibility assessments with 92% precision. This is a massive improvement — but it still works with evidence that already exists. Level 3 is the frontier: mechanistic simulation. A latent world model that has learned how human biology works — signaling pathways, gene regulation, drug metabolism — and can PREDICT what happens when you introduce a new molecule. This isn't science fiction. VCWorld, published in November 2025, is the first explicit biological world model that simulates cellular drug responses with traceable mechanistic reasoning. Recursion has trained models on 3.5 billion microscopy image crops that can detect phenotypes invisible to the human eye. And a landmark paper in Cell, co-authored by Genentech/Roche and the Chan Zuckerberg Initiative, has called for building an AI Virtual Cell — a model that can simulate biology from molecules to tissues. The pieces are falling into place.

---

## SLIDE 26 — The Vision

**Title:**
### From Reactive Surveillance to Predictive Safety

**Visual:** The transformation:

**Today:** *We wait for patients to be harmed, then we count.*
```
Drug marketed -> ADR occurs -> Report filed (94% underreporting) ->
Statistical signal detected -> Expert reviews -> 5-10 years -> Regulatory action
```

**Tomorrow:** *We simulate the harm before it happens.*
```
Drug candidate -> Latent world model simulates drug-body interaction ->
Predicts ADR risk in specific populations -> Safety team validates ->
Targeted monitoring protocol BEFORE launch
```

**The analogy:**
> *"Pharmacovigilance today is where weather forecasting was before computational fluid dynamics. We observe and report what happened. World models would let us simulate what will happen."*

**What connects today to tomorrow:**
> The ensemble AI pipeline we build today — extracting, structuring, and integrating 100+ billion data points into knowledge graphs — is creating the **training data** for tomorrow's world models. Every structured drug-event relationship, every normalized pathway, every cross-referenced evidence package feeds the latent representations that world models need.

**Speaker notes:**
> Here's the vision I want to leave you with. Today, pharmacovigilance is fundamentally reactive. A drug goes to market. Patients experience adverse events. Some of those events get reported — the MHRA estimates 94% underreporting. We count the reports. We run statistics. We detect signals. Experts review them. The cycle from first evidence to regulatory action can take 5 to 10 years. What if instead of waiting for harm, we could simulate it? What if a latent world model — trained on the structured biological knowledge we're building today — could predict that Drug X's mechanism will disrupt Pathway W in patients with genetic profile Y, leading to adverse outcome Z? Not as statistical correlation. As mechanistic simulation. That's the promise. And it connects directly to what ArcaScience does today. Every drug-event relationship we extract, every ontology mapping we normalize, every cross-document link we resolve — this is the structured training data that tomorrow's biological world models need. The ensemble AI pipeline is not just solving today's problem. It's building the foundation for tomorrow's revolution.

---

## SLIDE 27 — Three Takeaways

**Title:**
### If You Remember Three Things From This Room

**Visual:** Three numbered statements, large type, one per visual block:

```
 ┌─────────────────────────────────────────────────────────────────┐
 │                                                                 │
 │  1   NOT ALL AI IS EQUAL                                        │
 │      General-purpose LLMs hallucinate 50%+ in clinical          │
 │      contexts. Purpose-built, domain-specific AI delivers       │
 │      92% precision. The architecture you choose IS the outcome. │
 │                                                                 │
 ├─────────────────────────────────────────────────────────────────┤
 │                                                                 │
 │  2   STRUCTURED EVIDENCE IS THE BOTTLENECK — AND THE KEY        │
 │      The problem isn't too little data. It's 100 billion data   │
 │      points no one can connect. Ensemble SLMs solve evidence    │
 │      assembly today — 80% faster, regulator-accepted, auditable.│
 │                                                                 │
 ├─────────────────────────────────────────────────────────────────┤
 │                                                                 │
 │  3   THE FUTURE IS SIMULATION, NOT GENERATION                   │
 │      World models will move pharmacovigilance from counting     │
 │      harm to predicting it. The structured knowledge we build   │
 │      today is the foundation they'll need tomorrow.             │
 │                                                                 │
 └─────────────────────────────────────────────────────────────────┘
```

**Speaker notes:**
> Before we open the discussion, let me leave you with three things. One: not all AI is equal. The architecture you choose determines the outcome. General-purpose LLMs hallucinate in over half of clinical cases. Domain-specific small language models achieve 92% precision on the same tasks. This is not a marginal difference — it's the difference between a tool you can trust and one you cannot. Two: the bottleneck in drug safety is not data — it's evidence assembly. We have over 100 billion data points scattered across FAERS, EudraVigilance, published literature, clinical trials, and internal safety databases. No human team can connect them all. Ensemble AI pipelines do — 80% faster, with full auditability, accepted by FDA, EMA, and PMDA. Three: the future of our field is not text generation — it's biological simulation. Latent world models that understand how drugs interact with human biology will transform pharmacovigilance from reactive counting to predictive science. And the structured, normalized, cross-referenced evidence we're building today — that's exactly the training data those models will need. The work starts now.

---

# CODA: DISCUSSION (28:00–30:00)

---

## SLIDE 28 — Let's Discuss

**Title:**
### Three Questions for This Room

**Visual:** Three questions, cleanly displayed:

**1.** Given the evidence on LLM failure rates in clinical contexts, what standards should our field demand before accepting AI-generated safety evidence in regulatory submissions?

**2.** ArcaScience's ensemble approach delivers 92% precision today. World models promise predictive simulation tomorrow. What's the most valuable next step for YOUR organization?

**3.** If pharmacovigilance had a weather-forecasting equivalent — predicting adverse events instead of just counting them — how would it change how you design safety strategies?

**Closing line:**
> *"The future of drug safety is not AI that replaces your judgment. It's AI that gives you the full body of biomedical knowledge — structured, connected, and eventually simulated — so your judgment has everything it needs."*

**Speaker notes:**
> I want to end where I started: with honesty. AI is not going to automate pharmacovigilance. Anyone who tells you that doesn't understand either AI or pharmacovigilance. But AI — the right kind of AI, domain-specific, auditable, validated — can solve the evidence integration problem that limits every safety decision you make. And the next generation of AI — world models that simulate biology instead of generating text about it — has the potential to transform our field from reactive surveillance to predictive safety science. That transformation is being built today, by the researchers and companies I've shown you, and by the structured evidence systems like ours that are creating the biological knowledge foundations these models will need. I'd love to hear your perspective. What do you see as the most important next step? And what keeps you skeptical? The skepticism matters. It makes us all better.

---

# APPENDIX: BACKUP SLIDES

---

## BACKUP A — ArcaScience Platform Overview

- **Founded:** 2018 | **Clients:** 20+ pharma companies (Sanofi, AstraZeneca, GSK, Takeda, ICON)
- **Technology:** 24 task-specific SLMs, 8-stage auditable pipeline, 100+ billion data points
- **Regulatory footprint:** 50+ submissions accepted (FDA, EMA, PMDA) across 47 countries
- **Certifications:** GAMP 5 Cat. 5, ISO 27001, SOC 2 Type II, 21 CFR Part 11, HIPAA, GDPR, HDS, ALCOA+
- **Published validation:** 92% AE precision (Chen et al., 2025), 94% F1 (Rodriguez et al., 2024), 3x signal detection improvement (Kim et al., 2024), 60% PSUR cycle time reduction (Thompson et al., 2023)
- **Key outcome:** $181M R&D funds reallocated for one client due to early risk detection

---

## BACKUP B — Complete LLM Hallucination Data

| Study | Model | Hallucination/Error Rate | Context |
|-------|-------|------------------------|---------|
| Mount Sinai 2025 | GPT-4o | 50-53% | Clinical vignettes |
| Mount Sinai 2025 | GPT-4o + mitigation | 23% | With prompt guardrails |
| Mount Sinai 2025 | DeepSeek (distilled) | 80-83% | Worst performer |
| JMIR 2024 | GPT-4 | 28.6% fabricated citations | Systematic review |
| JMIR 2024 | GPT-3.5 | 39.6% fabricated | Systematic review |
| JMIR 2024 | Google Bard | 91.4% fabricated | Systematic review |
| npj Dig Med 2025 | Multiple | 1.47% sentence-level, **44% clinically major** | 12,999 annotated sentences |
| ASCO 2025 | Multiple | ~20% | General oncology questions |
| PMC 2025 | GPT-5 (no internet) | 47% | Fact-seeking medical queries |
| medRxiv 2026 | MedGemma | 25.6% correct staging | Oncology staging + treatment |
| JMIR 2025 | All | 40-50% accuracy | CSEDB safety evaluation |
| NHS 2025 | 120B LLM | 46.9% fully correct | 2.1M patient medication safety |
| FDA 2024 | All authorized AI/ML | **0 LLM-based devices** | Out of 1,016 FDA-cleared AI devices |

---

## BACKUP C — Yann LeCun: Key Quotes for Q&A

- *"The path to superintelligence through scaling LLMs — I think is complete bullshit."* (Dec 2025)
- *"Nobody in their right mind would use LLMs of the type that we have today"* within 3-5 years.
- *"Existing systems don't understand the world as well as a housecat."* (Columbia, Oct 2024)
- *"We don't need an AI that can recite encyclopedias; we need an AI that can understand the world with its eyes and hands."*
- *"If you are interested in human-level intelligence, do not work on LLMs."* (VivaTech, Paris 2024)
- AMI Labs mission: *"Develop applications where reliability, controllability, and safety really matter, especially for... healthcare."*

---

## BACKUP D — World Models Landscape

| Entity | Approach | Data Scale | Key Achievement |
|--------|---------|------------|----------------|
| AMI Labs (LeCun) | JEPA architecture | Video + embodied | EUR 500M raise, world model focus |
| Meta FAIR | V-JEPA 2 | 1M+ hours video | Zero-shot robot planning |
| NVIDIA Cosmos | World foundation model | 9,000T tokens, 20M hrs | Physical AI platform |
| World Labs (Fei-Fei Li) | Spatial intelligence | 3D environments | $1B raised, Marble product |
| Recursion | Cellular world model | 65 petabytes phenomics | 2.2M samples/week, Phenom-Beta |
| Isomorphic Labs | Molecular simulation | Protein structures | IsoDDE, $600M, human trials |
| VCWorld (SJTU/NeoLife) | Biological world model | Cell perturbation data | First explicit bio world model |
| Genentech/CZI | AI Virtual Cell | Multi-scale biology | Landmark Cell paper (2024) |
| DreamerV3 (DeepMind) | General world model | 150+ task environments | Published in Nature (2025) |

---

## BACKUP E — IDC Data Summary

| IDC Finding | Statistic | Source |
|------------|-----------|--------|
| Worldwide AI spending 2028 | $632 billion | AI Spending Guide |
| GenAI spending 2028 | $202 billion (32% of AI) | AI Spending Guide |
| GenAI CAGR | 59.2% | AI Spending Guide |
| AI pilot failure rate | 88% (4 of 33 to production) | IDC research |
| Healthcare AI pilot failure | 80% | HIT Consultant/IDC |
| GenAI pilot ROI failure | 95% | MIT NANDA |
| Domain-specific vs general ROI | **3-5x higher** by 2027 | Bio-IT World 2025 |
| Organizations at Stage 2 of 5 | 51% | Maturity Model (n=1,534) |
| Organizations at Stage 5 | 1% | Maturity Model |
| Data prep time | 50% of DS effort | IDC Blog |
| LS firms protecting AI budget | >40% | IDC FERS Survey |
| Pharma pursuing agentic AI | 73% | IDC 2025 |
| Life sciences GenAI use case #1 | Patient Safety | IDC Use Case Taxonomy |
| Preventable ADR cost (EU) | EUR 23 billion/year | EMA pharmacovigilance data |

---

## BACKUP F — Anticipated Q&A

**Q: "The Tiramisu Test isn't a published benchmark — where does it come from?"**
> A: You're right that it's not a formally named benchmark. The concept is well-established in AI research under terms like "multi-step procedural reasoning" and "compositional generalization." I use the tiramisu framing because it makes the failure mode intuitive for a non-AI audience. The published evidence is extensive — see arXiv:2511.04688 for procedural step ordering, and Apple's GSM-Symbolic paper at ICLR 2025 for the most rigorous demonstration that LLMs fail when you change variables in multi-step problems.

**Q: "If LLMs are so bad, why is everyone using them?"**
> A: LLMs are extraordinary tools for text generation, summarization, translation, and creative writing. They're genuinely useful for drafting clinical narratives, translating documents, and assisting with literature screening. The problem isn't that LLMs are bad — it's that they're being applied to tasks they architecturally cannot perform: causal reasoning, multi-step inference, and reliable structured extraction in safety-critical contexts. Use them where they work. Don't use them where precision and traceability matter.

**Q: "92% precision still means 8% errors. How is that acceptable for safety?"**
> A: Two mitigations. First, every extraction is traceable to a source document — errors are identifiable in review. Second, the human expert is always the final assessor. The comparison isn't 92% vs. perfection — it's 92% precision across 47 sources vs. 100% precision across the 12 sources a human reviewer had time to check. More evidence, slightly imperfect, versus less evidence, also imperfect. And 92% vs. GPT-4's 67% is a 3.5x reduction in error rate.

**Q: "World models for drug safety sound like science fiction. When will this be real?"**
> A: VCWorld was published in November 2025. Recursion's virtual cell is operational. The AI Virtual Cell paper was published in Cell in December 2024. The building blocks exist today. Full-scale latent biological world models for safety prediction are likely 5-10 years away from clinical deployment. But the data we structure today — through ensemble AI pipelines — is literally the training data these models will need. We're building the foundation now.

**Q: "What about regulatory acceptance?"**
> A: No regulator anywhere has accepted LLM-generated safety assessments for submissions. Zero. Of 1,016 FDA-authorized AI/ML medical devices, none are LLM-based. What regulators have accepted: structured, auditable, traceable evidence packages from domain-specific AI pipelines. We've had 50+ submissions accepted across FDA, EMA, and PMDA. The regulatory path is clear: auditability, traceability, and human-in-the-loop. Not black-box generation.

---

# DESIGN NOTES

## Visual Style
- **Palette:** Dark navy (#1B2A4A), white text, teal accent (#00B4D8), signal red (#E63946) for failure data
- **Typography:** Inter or Helvetica Neue. Large numbers. Minimal text per slide.
- **Data viz:** Clean tables, simple bar charts, funnel diagrams. No 3D charts. No clip art.
- **Photography:** None. Data speaks louder than stock photos.

## Narrative Principles
- **Act I is the hook** — financial data, failure rates, IDC authority. But first: acknowledge AI's genuine wins to build credibility and fairness before the critique.
- **Act II is the science** — LeCun, mathematical proofs, clinical evidence. Earn credibility with the scientists.
- **Act III is the proof** — introduce ArcaScience's identity and BRA platform, then show the ensemble SLM architecture and published results. Earn credibility with the practitioners.
- **Act IV is the vision** — inspire without overselling. Be clear about timelines. Connect today's work to tomorrow's possibility.

## Key Messages (repeat throughout)
1. **AI works — when purpose-built** — AlphaFold, 950 FDA-cleared devices, NLP in PV
2. **$632B in AI spending, 88% failure rate** — the wrong AI is failing
3. **Hallucination is architecture, not a bug** — LeCun, mathematical proof
4. **ArcaScience: 24 clinician-trained SLMs, BRA in days not months** — 80% time reduction
5. **Small + specialized > big + general** — 92% vs 67%, Nature Communications
6. **IDC: domain-specific = 3-5x ROI** — the market agrees
7. **World models = the future** — from counting harm to predicting it
