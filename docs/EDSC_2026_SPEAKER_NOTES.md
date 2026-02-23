# EDSC 2026 — SPEAKER NOTES
## What to say at each slide | Read & rehearse this document

**Format:** 30-minute roundtable | **Room:** Gloria B, C, D | **Audience:** ~100 safety specialists

---

## NARRATIVE ARC — Memorize this

| Act | Time | Emotional beat |
|-----|------|---------------|
| I. The AI Reality Check | 0:00–7:00 | "We have a problem" — concern, shared recognition |
| II. Why LLMs Fail Drug Safety | 7:00–15:00 | "Here's why" — scientific authority, intellectual clarity |
| III. SLMs + Ensemble AI | 15:00–22:00 | "Here's what works" — confidence, proof, relief |
| IV. Latent World Models | 22:00–28:00 | "Here's what's coming" — hope, inspiration, vision |
| Coda | 28:00–30:00 | "Over to you" — respect, engagement |

---

## ACT I: THE AI REALITY CHECK (0:00–7:00)

---

### SLIDE 1 — Title (30 seconds)

Thank you. I'm [Name] from ArcaScience. Over the next 30 minutes, I want to take you on a journey — not through what AI could theoretically do for drug safety, but through what's actually happening: what's working, what's failing spectacularly, and what the next generation of AI looks like for our field. I'll make claims. I'll back them with data. And I'll be honest about what we don't know yet. Let's start with the uncomfortable part.

---

### SLIDE 2 — The AI Gold Rush (90 seconds)

IDC projects worldwide AI spending will reach $632 billion by 2028 — more than doubling from today. GenAI alone hits $202 billion, growing at nearly 60% per year. Organizations increased AI infrastructure spending by 166% year-over-year in Q2 2025. Eighty-two billion dollars in a single quarter.

The AI cumulative economic impact through 2030? $19.9 trillion.

This is the largest technology investment cycle in human history.

So the question isn't whether AI matters. The question is: **is this investment paying off?**

---

### SLIDE 3 — Pharma Is All In (60 seconds)

Pharma is not standing on the sidelines. Over 40% of life sciences firms say AI is the one budget they're protecting regardless of macro conditions. 73% are actively pursuing agentic AI. IDC predicts 65% of drug discovery will be GenAI-powered by 2027.

And here's what matters to this room: when IDC mapped GenAI use cases for life sciences, they named six segments. Patient safety was number one. Not drug design. Not marketing. **Safety.**

So our field is squarely in the crosshairs of the biggest technology wave in history. Now here's the problem.

---

### SLIDE 4 — The 88% Failure Rate (90 seconds)

For every 33 AI pilots a company launches, only 4 make it to production. That's IDC data. An 88% failure rate.

MIT's NANDA Institute puts it even more starkly: 95% of GenAI pilots fail to deliver measurable ROI.

In healthcare specifically, 80% of AI projects never scale beyond pilot.

When IDC benchmarked 1,534 organizations on their AI maturity — five stages from "Ad Hoc" to "Optimized" — they found that only 1% have reached the optimized state. Over half are still at stage two.

**The pharma industry is spending aggressively on AI. It is getting very little back. Why?**

---

### SLIDE 5 — The Data Preparation Trap (90 seconds)

IDC found that data science teams spend 50% of their time on data preparation before they even begin building AI models. Half their time. Just getting data into a usable state.

And here's the kicker: healthcare and life sciences have the most fragmented, heterogeneous data landscape of any industry. 80% of health data is unstructured — clinical notes, discharge summaries, pathology reports. Every EHR system is configured differently. Every database uses different terminologies.

MedDRA doesn't map to MeSH. SNOMED doesn't align with ICD. And pharmacovigilance data is spread across FAERS, EudraVigilance, VigiBase, published literature, clinical trials, and EHRs — each with their own structures.

So when pharma companies take general-purpose AI tools and point them at this landscape, what happens? **They fail.** And they fail for a very specific reason.

---

### SLIDE 6 — The Root Cause (60 seconds)

IDC has made a very specific prediction: by 2027, domain-specific AI tools will deliver 3 to 5 times the return of general-purpose foundation models in pharma. Three to five times. Not a marginal improvement — a categorical difference.

Why? Because general-purpose LLMs — GPT-4, Claude, Gemini — were not designed for drug safety. They were designed to sound intelligent about everything. And there's a fundamental difference between sounding intelligent and being reliable.

Let me show you exactly why these models fail, and I'm going to start with a test that sounds trivial but reveals something profound.

---

## ACT II: WHY LLMs FAIL DRUG SAFETY (7:00–15:00)

---

### SLIDE 7 — The Tiramisu Test (90 seconds)

Let me start with something that sounds absurd. Ask an LLM to make tiramisu. It will give you a beautiful, step-by-step recipe.

Now change one variable: swap mascarpone for ricotta. Ask what changes downstream.

The model will give you a confident, fluent answer — and it will be wrong. Because it cannot reliably trace how a single change propagates through a multi-step process.

Ricotta has higher moisture content, which means the cream layer won't set the same way, which means the structural integrity changes, which means the layering technique needs adjustment, which means the resting time changes, which means the final presentation is different. The LLM misses most of these downstream effects — not because it doesn't "know" about ricotta, but because it cannot perform multi-step procedural reasoning with real-world constraints.

Published research from 2024 confirms this: LLM performance on ordered procedural steps degrades as sequence length increases and as step displacement grows.

Now here's why this matters for us.

---

### SLIDE 8 — From Tiramisu to Pharmacology (60 seconds)

Drug safety assessment IS the Tiramisu Test — except infinitely harder.

When you assess whether Drug A could cause cardiac arrhythmia, you need to trace: Does Drug A inhibit CYP3A4? If so, does the patient take Drug B, which is CYP3A4-metabolized? If so, Drug B plasma levels rise. Does Drug B prolong QTc? Is the patient a CYP2D6 poor metabolizer? Do they have renal impairment?

Each step depends on the previous one. Each variable interacts with every other.

**If an LLM can't reliably track ricotta through a tiramisu recipe, it cannot reliably trace a drug interaction through human pharmacology.** This isn't my opinion. This is mathematics.

---

### SLIDE 9 — The Mathematics of LLM Failure (90 seconds)

Yann LeCun — Turing Award winner, chief AI scientist at Meta for 12 years, professor at NYU — has made the clearest technical argument for why LLMs structurally cannot be reliable.

It's the exponential error divergence problem. At every token an LLM generates, there is some probability that it takes you out of the set of correct answers. Even if that probability is small — say 2% per token — after 100 tokens you're at 13% probability of still being correct. After 200 tokens, 1.8%.

This means hallucinations are not a bug you can fix with better training or smarter prompting. They are a mathematical consequence of autoregressive generation. The longer the output, the more certain the failure.

Now think about a pharmacovigilance evidence package — thousands of tokens, dozens of extracted entities, complex relational chains. **The math guarantees errors.**

---

### SLIDE 10 — LLM Failure Rates in Clinical Contexts (90 seconds)

Let me give you the numbers.

Mount Sinai tested GPT-4o on 300 clinical vignettes: it hallucinated in 50 to 53% of responses.

When LLMs generate references for systematic reviews, GPT-4 fabricates 29% of citations. GPT-3.5 fabricates 40%. Google Bard: 91%.

An NHS study tested a 120-billion-parameter model on real medication safety for 2.1 million patients: fully correct in only 47% of cases.

When Apple's research team added a single irrelevant clause to grade-school math problems — not even changing the question, just adding noise — LLM performance dropped by up to 65%. Their conclusion, published at ICLR 2025: *"We found no evidence of formal reasoning in language models."*

Clinical medication error standards require 99 to 99.9% accuracy. **The gap is not a rounding error. It's a chasm.**

---

### SLIDE 11 — Alice in Wonderland (60 seconds)

Here's my favorite one. "Alice has 3 brothers and 2 sisters. How many sisters does Alice's brother have?"

The answer is 3 — Alice herself plus her 2 sisters. This is a problem a 10-year-old can solve.

GPT-4o gets it right 65% of the time. Claude 3 Opus: 43%. And when they get it wrong, they don't say "I'm not sure." They give elaborate, confident, multi-paragraph explanations of why the wrong answer is right.

The researchers tried chain-of-thought prompting. They tried multi-step re-evaluation. Result? *"Models produced more nonsense, often in lengthier and sometimes more entertaining form."*

This is relational reasoning — understanding perspective shifts. It's the same cognitive operation required to assess whether an adverse event in a patient with three comorbidities on five medications is attributable to Drug A or Drug B. **If the model can't count sisters, it can't assess causality.**

---

### SLIDE 12 — Yann LeCun (90 seconds)

This argument isn't coming from an AI skeptic. It's coming from the man who invented convolutional neural networks, won the Turing Award, and spent 12 years as chief AI scientist at Meta.

Yann LeCun left Meta in December 2025 — walked away from one of the most powerful AI research positions in the world — to found AMI Labs, explicitly to build something better than LLMs. He raised half a billion euros. His CEO? Alex LeBrun, former CEO of Nabla — a health AI company.

LeCun says LLMs lack four things: understanding of the physical world, persistent memory, true reasoning, and the ability to plan.

He points out that a 4-year-old child has processed 50 times more data through vision than the largest LLMs have seen in text.

And he makes the structural argument: LLMs are autoregressive token predictors. They don't think before they speak. They generate text without first planning what to say. Hallucination is not a bug — it's the inevitable consequence of this architecture.

His exact words to the Financial Times, January 2026: **"LLMs basically are a dead end."**

---

### SLIDE 13 — The Gap (60 seconds)

Let me map this directly to our work.

Drug safety requires causal reasoning — the Bradford Hill criteria. LLMs do pattern matching. Drug safety requires multi-step inference — tracing a drug through metabolic pathways. LLMs degrade exponentially with each step.

Drug safety requires compositional reasoning — combining pharmacology, genetics, co-medications, and comorbidities. Researchers have mathematically PROVEN that transformers cannot compose functions at scale. Not "haven't yet" — **cannot**. It's a theoretical impossibility result.

Drug safety requires traceable evidence for regulatory submissions. LLMs fabricate 18 to 29% of citations.

So if LLMs are the wrong tool — **what's the right one?**

---

## ACT III: THE STRATEGY THAT WORKS — SLMs + ENSEMBLE AI (15:00–22:00)

---

### SLIDE 14 — Smaller > Bigger (90 seconds)

Here's the counterintuitive finding.

PubMedBERT has 110 million parameters. GPT-4 has 1.7 trillion — fifteen thousand times larger. And PubMedBERT outperforms GPT-4 on six of eight biomedical NLP benchmarks. Published in Nature Communications, 2025.

On protected health information detection — a safety-critical regulatory task — specialized healthcare NLP scores 96% F1. GPT-4o scores 79%. That's a 17-point gap.

On adverse event extraction — the core of pharmacovigilance — ArcaScience's domain-specific models achieve 92% precision. GPT-4 achieves 67%. Twenty-five points.

Why? Because a small model trained deeply on biomedical data learns the vocabulary, syntax, and semantic relationships of clinical language. A giant model that's seen everything knows nothing deeply.

**It's like the difference between a specialist cardiologist and a first-year medical student who's read the entire internet.**

---

### SLIDE 15 — The Ensemble Architecture (90 seconds)

At ArcaScience, we deploy 24 task-specific small language models in an 8-stage pipeline. Each model does one thing, and does it precisely.

Stage 1 ingests documents. Stage 2 classifies them. Stage 3 identifies sections. Stage 4 extracts entities — drugs, adverse events, dosages, temporal relationships. Stage 5 extracts relations. Stage 6 normalizes across ontologies — mapping MedDRA to SNOMED to ChEBI. Stage 7 populates a knowledge graph with cross-document entity resolution — so "atorvastatin," "LIPITOR," and "atorvastatin calcium" are recognized as the same compound. Stage 8 generates structured evidence packages for human assessment.

Three advantages over a single LLM.

First: **precision through specialization**. Second: **auditability at every stage** — every extraction traces to a source sentence in a source document. Third: **error containment**. If Stage 3 makes an error, it doesn't corrupt Stage 6. In a single LLM, errors propagate invisibly through the entire output.

---

### SLIDE 16 — Ensemble AI Outperforms Everything (60 seconds)

The evidence is overwhelming and it's peer-reviewed.

ArcaScience's ensemble achieves 92% precision on adverse event extraction where GPT-4 gets 67%. AbbVie's pilot with XGBoost achieved over 95% accuracy for post-marketing signal detection.

And here's the comparison that should change how we think about our tools: gradient boosted machines achieve an AUROC of 0.82 for signal detection. The traditional methods regulators use today — PRR, ROR — achieve 0.59. The standard tools are barely better than a coin flip.

And critically, these ensemble approaches detected four out of five pre-specified adverse events of infliximab **in the very first year they were reported** — years before traditional methods would have flagged them.

---

### SLIDE 17 — Before / After (60 seconds)

Let me make this concrete with a real case.

A top-5 pharmaceutical company had a rare disease program approaching Phase III. Traditional surveillance found 3 literature sources suggesting thromboembolic risk — not enough to act on.

When we applied our 24-model ensemble pipeline, the system identified 9 times more relevant evidence sources. It cross-referenced spontaneous reports with published case series, mechanistic pathway data, and class effect analysis.

The convergent evidence was clear: thromboembolic risk was real, scattered across sources that were never connected. The company redirected its development investment before Phase III. The structured evidence was accepted by regulators across 47 countries.

**The AI didn't make the decision. It assembled the evidence that made the decision obvious.**

---

### SLIDE 18 — The Economics (60 seconds)

And it's not just more accurate — it's dramatically cheaper.

GPT-4 API costs $30 to $60 per million tokens. Fine-tuned SLMs running on a T4 GPU cost roughly 5 cents per hour. At production scale, John Snow Labs reports being over 80% cheaper than Azure and GPT-4o.

Providence Health System used specialized NLP to de-identify 700 million clinical documents with a 0.81% error rate. GPT-4o on the same task misses 14.6% of protected health information — 18 times more errors.

Higher precision, lower cost, full data privacy, complete auditability, and regulatory compliance. **This is exactly what IDC predicted: domain-specific tools delivering 3 to 5 times the ROI.**

---

### SLIDE 19 — Honest Limits (60 seconds)

I want to be honest about the limits of what we do today.

ArcaScience's ensemble AI solves the evidence integration problem. It extracts, normalizes, cross-references, and structures safety evidence at scale, with auditability that meets regulatory standards. This is a massive advance over manual review — and the data proves it.

But it doesn't predict adverse events before they occur. It doesn't simulate how a drug interacts with human biology. It can't answer counterfactual questions like "what would happen if we doubled the dose in a patient with renal impairment?"

It works with the evidence that exists — it doesn't generate new biological understanding. To do that, we need something fundamentally different.

**And this is where the story gets exciting.**

---

## ACT IV: THE NEW HOPE — LATENT WORLD MODELS (22:00–28:00)

---

### SLIDE 20 — From Words to Worlds (90 seconds)

Fei-Fei Li — the computer scientist behind ImageNet, arguably the most influential dataset in AI history — left Stanford to found World Labs. She raised a billion dollars.

Her thesis: *"If AI is to be truly useful, it must understand worlds, not just words."*

A world model is an AI system that has an internal representation of how the world works. Not how text about the world is structured — how the world itself behaves.

It can predict consequences before they happen. It can simulate how states evolve over time. And it can reason about counterfactuals — "what if this were different?"

LLMs predict the next word. World models predict the next state of reality. **That's not an incremental improvement. It's a categorical shift.**

---

### SLIDE 21 — The Convergence (90 seconds)

Look at who's betting on this.

Yann LeCun left Meta to build world models — half a billion euros. Fei-Fei Li raised a billion dollars. NVIDIA built Cosmos, a world foundation model trained on 9,000 trillion tokens of real-world data. Google DeepMind's Genie 3 generates interactive 3D worlds in real time.

And Meta's V-JEPA 2 — LeCun's architecture — achieved something remarkable in June 2025: a model trained on a million hours of video that can plan robot movements in environments it has never seen, using only 62 hours of unlabeled adaptation data. It demonstrates object permanence. Basic physics. An understanding of how the world works.

**Now here's the question: what if we built a world model for biology?**

---

### SLIDE 22 — Three Levels of AI in Drug Safety (90 seconds)

Today, pharmacovigilance operates at Level 1: statistical correlation. We count how often a drug and an event co-occur in reports. That's what PRR and ROR do. The AUC is 0.59 — barely better than a coin flip.

ArcaScience operates at Level 2: evidence integration. We extract, normalize, and cross-reference evidence across all sources, building structured plausibility assessments with 92% precision. This is a massive improvement — but it still works with evidence that already exists.

Level 3 is the frontier: mechanistic simulation. A latent world model that has learned how human biology works — signaling pathways, gene regulation, drug metabolism — and can PREDICT what happens when you introduce a new molecule.

This isn't science fiction. VCWorld, published in November 2025, is the first explicit biological world model. Recursion has trained models on 3.5 billion microscopy image crops. And a landmark paper in Cell has called for building an AI Virtual Cell.

**The pieces are falling into place.**

---

### SLIDE 23 — The Vision (90 seconds)

Here's the vision I want to leave you with.

Today, pharmacovigilance is fundamentally reactive. A drug goes to market. Patients experience adverse events. Some of those events get reported — the MHRA estimates 94% underreporting. We count the reports. We run statistics. We detect signals. Experts review them. The cycle from first evidence to regulatory action can take 5 to 10 years.

What if instead of waiting for harm, we could simulate it? What if a latent world model could predict that Drug X's mechanism will disrupt Pathway W in patients with genetic profile Y, leading to adverse outcome Z? Not as statistical correlation. **As mechanistic simulation.**

And it connects directly to what ArcaScience does today. Every drug-event relationship we extract, every ontology mapping we normalize, every cross-document link we resolve — this is the structured training data that tomorrow's biological world models need.

**The ensemble AI pipeline is not just solving today's problem. It's building the foundation for tomorrow's revolution.**

---

### SLIDE 24 — Discussion (60 seconds)

I want to end where I started: with honesty.

AI is not going to automate pharmacovigilance. Anyone who tells you that doesn't understand either AI or pharmacovigilance.

But AI — the right kind of AI, domain-specific, auditable, validated — can solve the evidence integration problem that limits every safety decision you make. And the next generation of AI — world models that simulate biology instead of generating text about it — has the potential to transform our field from reactive surveillance to predictive safety science.

I'd love to hear your perspective. What do you see as the most important next step? And what keeps you skeptical?

**The skepticism matters. It makes us all better.**
