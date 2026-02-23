# EDSC 2026 — STUDY GUIDE
## What to learn and internalize before Tuesday

---

# 1. YOUR NARRATIVE IN ONE PARAGRAPH

The world is spending $632B on AI by 2028. Pharma is all in — patient safety is IDC's #1 GenAI use case. But 88% of AI pilots fail. The reason: general-purpose LLMs are architecturally incapable of the causal reasoning, multi-step inference, and traceable evidence drug safety demands. The Tiramisu Test proves they can't track one variable change through 15 steps — drug safety requires 20+. Yann LeCun (Turing Award, ex-Meta) left to build something better, calling LLMs "a dead end." The answer today: Small Language Models in ensemble architectures — ArcaScience's 24-model pipeline achieves 92% precision where GPT-4 gets 67%, at 80% lower cost. The answer tomorrow: Latent World Models that simulate biology mechanistically, predicting adverse events before they happen. ArcaScience's structured knowledge graphs are building the training data for that future.

---

# 2. KEY STATISTICS — Know these cold

## IDC Data
| Stat | Number | Source |
|------|--------|--------|
| Worldwide AI spending 2028 | $632 billion, 29% CAGR | IDC AI Spending Guide |
| GenAI spending 2028 | $202 billion, 59% CAGR | IDC AI Spending Guide |
| AI economic impact by 2030 | $19.9 trillion (3.5% global GDP) | IDC |
| AI infra spending growth Q2 2025 | 166% YoY, $82B in one quarter | IDC |
| AI pilot failure rate | 88% (4 of 33 reach production) | IDC |
| GenAI pilot ROI failure | 95% | MIT NANDA Institute |
| Healthcare AI pilot failure | 80% | HIT Consultant |
| Organizations at AI maturity Stage 5 | 1% of 1,534 orgs | IDC Maturity Model |
| Organizations still at Stage 2 | 51% | IDC Maturity Model |
| Data prep time for DS teams | 50% of effort | IDC Blog |
| LS firms protecting AI budget | >40% | IDC FERS Survey |
| Pharma pursuing agentic AI | 73% | IDC 2025 |
| Domain-specific vs general ROI | 3-5x higher by 2027 | IDC Bio-IT World 2025 |
| Life sciences GenAI use case #1 | Patient Safety | IDC Use Case Taxonomy |

## LLM Failure Data
| Stat | Number | Source |
|------|--------|--------|
| GPT-4o hallucination on clinical vignettes | 50-53% | Mount Sinai 2025 |
| GPT-4 fabricated citations | 28.6% | JMIR 2024 |
| Google Bard fabricated citations | 91.4% | JMIR 2024 |
| 120B LLM on 2.1M patient med safety | 53.1% incorrect | NHS Study 2025 |
| LLM performance drop from 1 irrelevant clause | Up to 65% | Apple, ICLR 2025 |
| LLM accuracy on symbolic arithmetic | 7.5% | Caltech/Stanford 2026 |
| CSEDB clinical safety accuracy | 40-50% | JMIR 2025 |
| Alice in Wonderland — GPT-4o | 65% correct | Nezhurina et al., 2024 |
| Alice in Wonderland — Claude 3 Opus | 43% correct | Nezhurina et al., 2024 |
| FDA-cleared AI/ML devices that are LLM-based | 0 of 1,016 | FDA 2024 |

## ArcaScience Performance
| Stat | Number | Comparison |
|------|--------|-----------|
| AE extraction precision | 92% | vs GPT-4 at 67% |
| Evidence coverage | 9x more sources | vs traditional review |
| PSUR cycle time | 60% reduction | vs manual process |
| Regulatory submissions accepted | 50+ | FDA, EMA, PMDA across 47 countries |
| Client R&D reallocation | $181M | from one early risk detection |
| Production cost vs GPT-4 | >80% cheaper | John Snow Labs benchmark |

## World Models
| Stat | Detail |
|------|--------|
| LeCun/AMI Labs | EUR 500M raise, EUR 3B valuation, Dec 2025 |
| Fei-Fei Li/World Labs | $1B raised |
| NVIDIA Cosmos | 9,000 trillion tokens, 20M hours video |
| V-JEPA 2 | 1M+ hours video, zero-shot robot planning, 62hrs adaptation |
| Recursion Phenom-Beta | 3.5B image crops, 93M microscopy images, 65PB data |
| VCWorld | First biological world model, Nov 2025, arXiv:2512.00306 |
| AI Virtual Cell | Cell journal, Dec 2024, Genentech/Roche + CZI |

---

# 3. KEY CONCEPTS — Understand deeply

## The Tiramisu Test
- **What it proves:** LLMs cannot track how changing one variable propagates through a multi-step procedure.
- **Why it matters for PV:** Drug safety assessment is multi-step procedural reasoning with biological constraints. If an LLM can't track ricotta through a recipe (~15 steps), it can't trace a drug interaction through human pharmacology (~20+ steps).
- **Published backing:** arXiv:2511.04688 — "Evaluating LLMs' Reasoning Over Ordered Procedural Steps." Performance declines with sequence length and step displacement.
- **If challenged:** "The Tiramisu Test is not a formal benchmark name — it's an intuitive framing of the published finding that LLMs fail at multi-step procedural reasoning. Apple's GSM-Symbolic paper at ICLR 2025 is the most rigorous demonstration."

## Exponential Error Divergence (LeCun)
- **The math:** If per-token accuracy is p < 1, after N tokens the probability of staying correct is p^N, which approaches 0 exponentially.
- **At p = 0.98:** 10 tokens → 81.7%, 50 → 36.4%, 100 → 13.3%, 200 → 1.8%
- **Implication:** Hallucination is not a training problem or a prompting problem. It's a mathematical inevitability of autoregressive token generation. You cannot fix it. You can only reduce the per-token error rate — but the exponential decay remains.
- **Source:** LeCun, Lex Fridman Podcast (March 2024); later reinforced in multiple talks (NYU, Columbia, VivaTech).

## Compositional Reasoning Impossibility
- **The proof:** "On Limitations of the Transformer Architecture" (OpenReview/ICLR) — uses Communication Complexity theory to prove transformers cannot compose functions at scale.
- **What it means:** Drug safety requires composing multiple types of knowledge (pharmacology + genetics + comorbidities + co-medications). Transformers are mathematically proven unable to do this reliably at scale.
- **Also:** "LLM Cannot Discover Causality" (arXiv:2506.00844) — formal proof that LLMs cannot perform causal discovery from data.

## Why Small > Big in Biomedical NLP
- **The evidence:** Nature Communications 2025 — "Traditional fine-tuning outperforms zero/few-shot LLMs in most biomedical NLP tasks."
- **PubMedBERT (110M params) beats GPT-4 (1.7T params)** on 6/8 BioNLP benchmarks.
- **Why:** Fine-tuning on domain data creates dense, precise representations of clinical language. General pre-training creates broad but shallow coverage. Depth beats breadth for specialized tasks.
- **The analogy:** "A specialist cardiologist vs. a first-year medical student who's read the entire internet."

## Ensemble Architecture Advantages
1. **Precision through specialization** — each of 24 models is optimized for exactly one task
2. **Auditability** — every extraction traces to a specific sentence in a specific source document
3. **Error containment** — failures in one stage don't corrupt other stages (unlike LLMs where errors propagate invisibly)
- **Pipeline:** Ingest → Classify → Section ID → Extract → Relate → Normalize → Link → Template

## World Models (The Future)
- **Definition:** An internal representation of how the world works, learned by an AI system, that can predict consequences, simulate state evolution, plan actions, and reason about counterfactuals.
- **LLM vs World Model:** LLMs predict the next word from text patterns. World models predict the next state of reality from physics/dynamics/causation.
- **Yann LeCun's bet:** Left Meta (Dec 2025), founded AMI Labs (EUR 500M), dedicated to world models. CEO = Alex LeBrun (ex-Nabla, health AI).
- **JEPA architecture:** Joint Embedding Predictive Architecture — learns representations in latent space, not token space. Can be trained on video/sensor data, not just text.
- **Biological world models already emerging:**
  - VCWorld (Nov 2025): first explicit biological world model, simulates cellular drug perturbation responses
  - Recursion Phenom-Beta: trained on 3.5B microscopy image crops, detects invisible phenotypes
  - AI Virtual Cell (Cell, Dec 2024): landmark paper calling for multi-scale biological simulation
- **The ArcaScience bridge:** Structured knowledge graphs from ensemble AI pipelines = training data for future biological world models. Every normalized drug-event relationship feeds the latent representations these models need.
- **The analogy:** "Pharmacovigilance today is where weather forecasting was before computational fluid dynamics. We observe and report. World models would let us simulate."

---

# 4. YANN LECUN — Know his story

- **Who:** Turing Award winner (2018, with Bengio and Hinton). Inventor of convolutional neural networks. Professor at NYU (Courant Institute). Chief AI Scientist at Meta from 2018 to 2024.
- **The departure:** Left Meta December 2025. Founded AMI Labs (Advanced Machine Intelligence). Raised ~EUR 500M at ~EUR 3B valuation. CEO: Alex LeBrun (former CEO of Nabla, a health AI company).
- **His core argument:** LLMs are autoregressive token predictors — they generate text without planning or understanding. They lack: (1) understanding of the physical world, (2) persistent memory, (3) true reasoning, (4) hierarchical planning.
- **The bandwidth argument:** "A 4-year-old child has seen 50 times more data [through vision] than the biggest LLMs trained on ALL text publicly available on the internet."
- **Key quotes:**
  - "LLMs basically are a dead end when it comes to superintelligence." (FT, Jan 2026)
  - "The path to superintelligence through scaling LLMs — I think is complete bullshit." (Dec 2025)
  - "Existing systems don't understand the world as well as a housecat." (Columbia, Oct 2024)
  - "If you are interested in human-level intelligence, do not work on LLMs." (VivaTech, Paris 2024)
  - AMI Labs mission: "Develop applications where reliability, controllability, and safety really matter, especially for... healthcare."

---

# 5. ANTICIPATED Q&A — Prepare your answers

### Q: "The Tiramisu Test isn't a published benchmark — where does it come from?"
**A:** You're right that it's not a formally named benchmark. The concept is well-established in AI research under "multi-step procedural reasoning" and "compositional generalization." I use tiramisu because it makes the failure mode intuitive. The published evidence: arXiv:2511.04688 for procedural step ordering, Apple's GSM-Symbolic (ICLR 2025) for the most rigorous demonstration.

### Q: "If LLMs are so bad, why is everyone using them?"
**A:** LLMs are extraordinary for text generation, summarization, translation, creative writing. They're useful for drafting clinical narratives, translating documents, literature screening. The problem isn't that LLMs are bad — it's that they're applied to tasks they architecturally cannot perform: causal reasoning, multi-step inference, reliable structured extraction in safety-critical contexts. Use them where they work. Don't use them where precision and traceability matter.

### Q: "92% precision still means 8% errors. How is that acceptable?"
**A:** Two mitigations. First, every extraction is traceable to a source document — errors are identifiable in review. Second, the human expert is always the final assessor. The comparison isn't 92% vs. perfection — it's 92% across 47 sources vs. 100% across the 12 sources a human had time to check. More evidence, slightly imperfect, versus less evidence, also imperfect. And 92% vs. 67% = 3.5x error reduction.

### Q: "World models sound like science fiction. When?"
**A:** VCWorld was published November 2025. Recursion's virtual cell is operational. The AI Virtual Cell paper was in Cell December 2024. Building blocks exist today. Full-scale latent biological world models for safety prediction: likely 5-10 years from clinical deployment. But the data we structure today — through ensemble AI — is literally the training data these models need. We're building the foundation now.

### Q: "What about regulatory acceptance?"
**A:** No regulator anywhere has accepted LLM-generated safety assessments. Zero. Of 1,016 FDA-authorized AI/ML devices, none are LLM-based. What regulators accept: structured, auditable, traceable evidence from domain-specific AI. We've had 50+ submissions accepted across FDA, EMA, PMDA. The path is clear: auditability, traceability, human-in-the-loop.

### Q: "How does this compare to what [Competitor X] does?"
**A:** Most competitors use general-purpose LLMs or workflow automation. We use 24 task-specific SLMs in an auditable pipeline. The difference: our outputs trace to source documents, meet regulatory standards (GAMP 5, 21 CFR Part 11, ALCOA+), and achieve 92% precision vs. 67% for LLM-based approaches. We're not a chatbot. We're an evidence assembly engine.

### Q: "What about RAG? Doesn't retrieval-augmented generation solve hallucination?"
**A:** RAG reduces hallucination for factual questions, but it doesn't solve multi-step reasoning, causal inference, or compositional reasoning — the core requirements for drug safety. RAG helps you find the right passage. It doesn't help you trace a drug through 20 biological steps. And RAG outputs are still generated by an LLM, so the exponential error divergence still applies to the synthesis step.

### Q: "Isn't ArcaScience also AI? Why trust yours?"
**A:** Our models are task-specific, domain-trained, and validated against published benchmarks. Every output is traceable to a source document and a specific extraction step. We're not asking you to trust AI blindly — we're giving you an auditable evidence pipeline where every claim can be verified. The human expert makes the decision. The AI does the evidence assembly that used to take months.

---

# 6. ARCASCIENCE FACTS — Quick reference

- **Founded:** 2018
- **What:** 24 task-specific SLMs in an 8-stage auditable pipeline for pharmacovigilance evidence assembly
- **Data:** 100+ billion data points
- **Clients:** 20+ pharma (Sanofi, AstraZeneca, GSK, Takeda, ICON, Novartis)
- **Regulatory:** 50+ submissions accepted (FDA, EMA, PMDA) across 47 countries
- **Certifications:** GAMP 5 Cat. 5, ISO 27001, SOC 2 Type II, 21 CFR Part 11, HIPAA, GDPR, HDS, ALCOA+
- **Key metrics:** 92% AE precision, 9x evidence coverage, 60% PSUR cycle reduction, $181M R&D reallocation
- **Use cases:** PSUR/PBRER acceleration, signal detection, literature surveillance, aggregate analysis, drug repurposing evidence, rare disease evidence assembly, regulatory submission support

---

# 7. TONE & DELIVERY NOTES

- **You are a peer, not a vendor.** You're a safety scientist talking to safety scientists about a shared problem.
- **Lead with the problem, not the product.** Acts I and II are about the industry's problem. Act III introduces ArcaScience as proof that a better approach works.
- **Be honest about limits.** Slide 19 (honest limits) and Act IV (world models as future, not present) build credibility.
- **Use numbers, not adjectives.** "92% vs 67%" beats "much better." "$632 billion" beats "massive spending."
- **The Tiramisu Test is your storytelling anchor.** It makes an abstract concept (multi-step procedural reasoning) tangible. Return to it.
- **LeCun is your authority anchor.** A Turing Award winner who bet half a billion euros validates the claim that LLMs are broken.
- **The weather forecasting analogy is your vision anchor.** "We observe and report. World models would let us simulate."
- **Energy management:** Start strong (alarm), go deep (science), deliver relief (proof), end with inspiration (vision). Don't let the energy dip in Act II — the failure data should feel shocking, not tedious.
- **Pace:** You have ~75 seconds per slide on average. Slides 7 (Tiramisu) and 12 (LeCun) are your two "moment" slides — take your time.
- **Room engagement:** At Slide 19 transition ("this is where it gets exciting"), make eye contact. At Slide 24 questions, genuinely pause. Let silence work.
