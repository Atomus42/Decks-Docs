# EDSC 2026 — SLIDE DECK
## What to put on screen | 24 slides + 6 backup

> **Design:** Dark navy (#1B2A4A), white text, teal accent (#00B4D8), signal red (#E63946) for failure data.
> Inter or Helvetica Neue. Large numbers. Minimal text. No stock photos. No clip art.

---

## SLIDE 1 — Title

**CHALLENGES IN LEVERAGING ALL BIOMEDICAL KNOWLEDGE & HOW AI CAN HELP**

*What works, what doesn't, and what comes next*

ArcaScience logo | EDSC 2026 | Gloria B, C, D

---

## SLIDE 2 — The AI Gold Rush

### $632 Billion.
**That's how much the world will spend on AI by 2028.**

| IDC Forecast | Amount | Growth |
|-------------|--------|--------|
| Total AI spending by 2028 | **$632B** | 29% CAGR |
| GenAI spending by 2028 | **$202B** | 59% CAGR |
| AI economic impact by 2030 | **$19.9T** | 3.5% of global GDP |

*Source: IDC Worldwide AI and Generative AI Spending Guide, 2024*

---

## SLIDE 3 — Pharma Is All In

- **>40%** of LS firms: AI is the ONE budget they won't cut *(IDC, Nov 2024)*
- **73%** actively piloting agentic AI *(IDC 2025)*
- **65%** of drug discovery GenAI-powered by 2027 *(IDC FutureScape)*
- **Patient Safety** = IDC's #1 GenAI use case in life sciences

---

## SLIDE 4 — The 88% Failure Rate

### For every 33 AI pilots, only 4 make it to production.

```
AI Pilots Launched:      ██████████████████████████████████  33
Made it to Production:   ████                                 4

Failure Rate:            88%
```

- **80%** of healthcare AI projects fail to scale *(HIT Consultant, 2026)*
- **95%** of GenAI pilots fail to deliver ROI *(MIT NANDA Institute)*
- Only **1%** of orgs at optimized AI maturity *(IDC, n=1,534)*

---

## SLIDE 5 — The Data Preparation Trap

```
How data science teams spend their time:

  ┌─────────────────────────────────────────┐
  │      DATA PREPARATION: 50%              │
  ├─────────────────────────────────────────┤
  │  Model Training: 20%                    │
  ├─────────────────────────────────────────┤
  │  Deployment: 15%                        │
  ├─────────────────────────────────────────┤
  │  Actual insight generation: 15%         │
  └─────────────────────────────────────────┘
```

**80%** of health data is unstructured | MedDRA ≠ MeSH ≠ SNOMED ≠ ICD

*"Data quality, quantity, and access are among the top challenges to scaling AI."* — IDC

---

## SLIDE 6 — The Root Cause

### The problem isn't AI. It's the wrong kind of AI.

> *"By 2027, domain-specific GenAI tools fine-tuned for pharma will deliver a **3-5x higher ROI** than general-purpose foundation models."*
>
> — Dr. Nimita Limaye, Research VP, Life Sciences R&D, IDC

---

## SLIDE 7 — The Tiramisu Test

### Can AI make tiramisu?

*"Describe step by step how to make tiramisu. Then: if I swap mascarpone for ricotta, what changes downstream?"*

1. LLMs produce a fluent recipe ✓
2. Cannot trace how one change propagates through all steps ✗
3. Miss: texture, structure, set time, presentation
4. Confidently describe a result that would fail in any kitchen

*Published: arXiv:2511.04688 — performance declines with sequence length and step displacement*

---

## SLIDE 8 — From Tiramisu to Pharmacology

### If AI can't track ricotta through a recipe, how will it track a drug through the body?

| Tiramisu Test | Drug Safety Assessment |
|--------------|----------------------|
| 1 ingredient change | 1 drug interaction |
| ~15 steps | ~20+ biological steps |
| Texture, structure, timing | Metabolism, distribution, effect |
| Fails at propagation | Must trace: CYP3A4 → plasma levels → QTc → arrhythmia → CYP2D6 → renal impairment |

**Drug safety is the hardest version of the Tiramisu Test.**

---

## SLIDE 9 — The Mathematics of LLM Failure

### Hallucination is not a bug. It's architecture.

```
Per-token accuracy: p = 0.98

  After 10 tokens:   81.7% correct
  After 50 tokens:   36.4% correct
  After 100 tokens:  13.3% correct
  After 200 tokens:   1.8% correct
```

> *"Every time an LLM produces a token, the probability that you stay correct decreases — exponentially."*
> — **Yann LeCun**, Turing Award, Founder AMI Labs

---

## SLIDE 10 — LLM Failure Rates in Clinical Contexts

| Study | Model | Failure Rate | Context |
|-------|-------|-------------|---------|
| Mount Sinai 2025 | GPT-4o | **50-53%** hallucination | 300 clinical vignettes |
| JMIR 2024 | GPT-4 | **28.6%** fabricated citations | Systematic reviews |
| JMIR 2024 | Google Bard | **91.4%** fabricated citations | Systematic reviews |
| NHS 2025 | 120B LLM | **53.1%** incorrect | 2.1M patient medication safety |
| Apple ICLR 2025 | All SOTA | **Up to 65% drop** | One irrelevant clause added |
| Caltech 2026 | All SOTA | **7.5% accuracy** | Symbolic re-encoding |

**These are not edge cases. This is the normal operating range.**

---

## SLIDE 11 — Alice in Wonderland

### "Alice has 3 brothers and 2 sisters. How many sisters does Alice's brother have?"

| Model | Correct Answer Rate |
|-------|-------------------|
| GPT-4o | 65% |
| Claude 3 Opus | 43% |

**The answer is 3.** Models give elaborate, confident, wrong explanations.

*"Models produced more nonsense, often in lengthier and sometimes more entertaining form."*
— Nezhurina et al., 2024

---

## SLIDE 12 — Yann LeCun: "LLMs Are a Dead End."

**Timeline:**
- 2018-2024: Chief AI Scientist, Meta
- Oct 2024: *"Existing systems don't understand the world as well as a housecat."*
- Dec 2025: Leaves Meta → founds **AMI Labs** (EUR 500M raise, EUR 3B valuation)
- Jan 2026, FT: *"LLMs basically are a dead end."*

**Four missing capabilities:** Physical understanding | Persistent memory | True reasoning | Hierarchical planning

> *"A 4-year-old child has seen **50x more data** than the biggest LLMs trained on ALL text on the internet."*

---

## SLIDE 13 — The Gap

### What drug safety requires vs. what LLMs can do

| Requirement | LLM Capability | Verdict |
|------------|---------------|---------|
| Causal reasoning (Bradford Hill) | Pattern matching | **Impossible** |
| Multi-step inference | Degrades exponentially | **Proven to fail** |
| Compositional reasoning | Proven impossible for transformers | **Theoretical limit** |
| Filter irrelevant info | 65% drop from 1 clause | **Fragile** |
| Traceable evidence | 18-29% fabricated | **Unacceptable** |
| Biological simulation | No dynamics mechanism | **Wrong architecture** |

---

## SLIDE 14 — Smaller > Bigger

### Smaller models, working together, beat bigger models alone.

| Benchmark | PubMedBERT (110M) | GPT-4 (1.7T) |
|-----------|-------------------|---------------|
| BioNLP (8 datasets) | **68.5-82.0%** | 68.3% |
| PHI detection F1 | **96%** | 79% |
| AE extraction precision | **92%** (ArcaScience) | 67% |

*PubMedBERT: 110M parameters. GPT-4: 1.7 trillion. 15,000x smaller. Better.*

*Source: Nature Communications, 2025*

---

## SLIDE 15 — The Ensemble Architecture

### 24 specialist models > 1 generalist model

```
INGEST → CLASSIFY → SECTION ID → EXTRACT → RELATE → NORMALIZE → LINK → TEMPLATE
  6+ formats   RCT/case/obs   boundaries   entities   drug→event   MedDRA↔SNOMED   knowledge graph   evidence packages
```

**Three advantages:**
1. **Precision** — each model optimized for one task
2. **Auditability** — every output traces to source
3. **Error containment** — stage failures don't propagate

---

## SLIDE 16 — Ensemble AI Outperforms Everything

| Approach | Task | Performance |
|----------|------|-------------|
| ArcaScience (24 SLMs) | AE extraction | **92%** precision |
| GPT-4 | AE extraction | 67% precision |
| XGBoost ensemble | Signal detection | **>95%** accuracy |
| GBM | Signal detection AUROC | **0.82** |
| Traditional (PRR, ROR) | Signal detection AUROC | 0.59 |

*"ML detected 4/5 pre-specified AEs of infliximab in the first year reported."*
— Scientific Reports, 2022

---

## SLIDE 17 — Before / After

### From fragmented searches to integrated evidence

| | BEFORE | AFTER (ArcaScience) |
|--|--------|-------------------|
| Evidence sources found | 3 | **27 (9x)** |
| Assembly time | 12-16 weeks | **Days** |
| Audit trail | None | Full, source-linked |
| Outcome | Inconclusive | **Phase III redirected, accepted in 47 countries** |

---

## SLIDE 18 — The Economics

| Factor | GPT-4 (API) | Fine-Tuned SLMs |
|--------|-------------|-----------------|
| AE precision | 67% | **92%** |
| Cost at scale | $30-60/M tokens | **>80% cheaper** |
| Data privacy | Third-party servers | **On-premises** |
| Auditability | Black box | **Per-stage, source-linked** |
| Regulatory | None native | **GAMP 5, 21 CFR Part 11, ALCOA+** |

*IDC: "Domain-specific = 3-5x higher ROI."*

---

## SLIDE 19 — Honest Limits

### What SLM ensembles solve — and what they don't

**Solved today:**
- 92% precision evidence extraction
- Cross-source normalization
- Regulatory-grade traceability
- PSUR/PBRER 60% faster

**Not yet:**
- Predicting AEs before they happen
- Simulating drug-body interactions
- Counterfactual reasoning
- Biological dynamics modeling

*"To solve these, we need a fundamentally different kind of AI."*

---

## SLIDE 20 — From Words to Worlds

> *"If AI is to be truly useful, it must understand **worlds**, not just **words**."*
> — **Fei-Fei Li**, Stanford, Founder World Labs ($1B raised)

| | LLM | World Model |
|--|-----|------------|
| Predicts | Next word | Next state of the world |
| From | Text patterns | Physics, dynamics, causation |
| Answers | "What have people written about X?" | "What happens if I do X?" |

---

## SLIDE 21 — The Convergence

| Who | What | Scale |
|-----|------|-------|
| **LeCun** / AMI Labs | World models | EUR 500M, EUR 3B valuation |
| **Fei-Fei Li** / World Labs | Spatial intelligence | $1B raised |
| **NVIDIA** / Cosmos | World foundation model | 9,000T tokens |
| **Recursion** | Cellular world model | 65 petabytes |
| **Isomorphic Labs** | Molecular simulation | $600M funding |

**V-JEPA 2 (June 2025):** Zero-shot robot planning, object permanence, 62hrs of data.

---

## SLIDE 22 — Three Levels of AI in Drug Safety

```
LEVEL 1: Statistical Correlation        → PRR, ROR → AUROC 0.59
              ↓
LEVEL 2: Evidence Integration            → ArcaScience → 92% precision, 9x coverage
              ↓
LEVEL 3: Mechanistic Simulation          → Latent World Models → Predictive, not reactive
```

**Already emerging:**
- VCWorld (Nov 2025) — first biological world model
- Recursion Phenom-Beta — 3.5B image crops, 93M microscopy images
- AI Virtual Cell (Cell, Dec 2024) — Genentech/Roche + CZI

---

## SLIDE 23 — The Vision

### From reactive surveillance to predictive safety

**Today:** Drug marketed → ADR → Report (94% underreporting) → Signal → 5-10 years → Action

**Tomorrow:** Drug candidate → World model simulates → Predicts ADR risk → Targeted monitoring BEFORE launch

> *"Pharmacovigilance today is where weather forecasting was before computational fluid dynamics."*

**The bridge:** ArcaScience's structured knowledge graphs = training data for tomorrow's world models.

---

## SLIDE 24 — Discussion

### Three questions for this room:

**1.** What standards should we demand before accepting AI-generated safety evidence in regulatory submissions?

**2.** What's the most valuable next step for YOUR organization?

**3.** If we could predict adverse events instead of counting them — how would you redesign safety strategies?

> *"The future of drug safety is not AI that replaces your judgment. It's AI that gives you the full body of biomedical knowledge — structured, connected, and eventually simulated — so your judgment has everything it needs."*

---

# BACKUP SLIDES

---

## BACKUP A — ArcaScience Platform

- Founded 2018 | 20+ pharma clients (Sanofi, AstraZeneca, GSK, Takeda, ICON)
- 24 SLMs, 8-stage pipeline, 100+ billion data points
- 50+ regulatory submissions accepted (FDA, EMA, PMDA), 47 countries
- GAMP 5, ISO 27001, SOC 2, 21 CFR Part 11, HIPAA, GDPR, HDS, ALCOA+
- $181M R&D reallocated for one client

---

## BACKUP B — Full Hallucination Data Table

| Study | Model | Rate | Context |
|-------|-------|------|---------|
| Mount Sinai 2025 | GPT-4o | 50-53% | Clinical vignettes |
| Mount Sinai 2025 | GPT-4o + mitigation | 23% | With guardrails |
| Mount Sinai 2025 | DeepSeek | 80-83% | Worst performer |
| JMIR 2024 | GPT-3.5 | 39.6% fabricated | Systematic review |
| JMIR 2024 | Google Bard | 91.4% fabricated | Systematic review |
| npj Dig Med 2025 | Multiple | 44% clinically major | 12,999 sentences |
| PMC 2025 | GPT-5 | 47% incorrect | Medical queries |
| NHS 2025 | 120B LLM | 53.1% incorrect | 2.1M patients |
| FDA 2024 | All AI/ML | 0 LLM-based | 1,016 cleared devices |

---

## BACKUP C — LeCun Quotes

- *"The path to superintelligence through scaling LLMs — I think is complete bullshit."*
- *"Nobody in their right mind would use LLMs of the type we have today"* within 3-5 years
- *"Existing systems don't understand the world as well as a housecat."*
- *"If you are interested in human-level intelligence, do not work on LLMs."*

---

## BACKUP D — World Models Landscape

| Entity | Approach | Key Achievement |
|--------|---------|----------------|
| AMI Labs | JEPA architecture | EUR 500M, world model focus |
| Meta FAIR | V-JEPA 2 | Zero-shot robot planning |
| NVIDIA Cosmos | World foundation model | 9,000T tokens |
| Recursion | Cellular world model | 65PB phenomics |
| VCWorld | Biological world model | First explicit bio world model |
| Genentech/CZI | AI Virtual Cell | Landmark Cell paper |

---

## BACKUP E — IDC Data Summary

| Finding | Statistic |
|---------|-----------|
| AI spending 2028 | $632B |
| GenAI spending 2028 | $202B (59% CAGR) |
| Pilot failure rate | 88% |
| GenAI ROI failure | 95% |
| Domain-specific ROI advantage | 3-5x by 2027 |
| Pharma pursuing agentic AI | 73% |
| LS GenAI use case #1 | Patient Safety |
| Preventable ADR cost (EU) | EUR 23B/year |

---

## BACKUP F — Q&A Answers

See: `EDSC_2026_STUDY_GUIDE.md` — Section "Anticipated Q&A"
