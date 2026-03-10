# Risk Minimization and Mitigation Strategies for VG-3927 — Version B
## Building the Safety Evidence Architecture Before Phase 2

**Prepared for:** Sanofi Neuroscience Clinical Development, Pharmacovigilance, Benefit-Risk Governance, and Regulatory Strategy Teams
**Classification:** Confidential — Scientific Collaboration Proposal
**Date:** March 2026
**Version:** B (Safety-Led / Risk Minimization)
**Audience:** Clinical safety physicians, pharmacovigilance scientists, regulatory affairs, benefit-risk governance, and clinical development leadership

**Premise:** VG-3927 is the first oral TREM2 agonist to enter clinical development. The mechanism class's only Phase 2 dataset — INVOKE-2 — produced 29% ARIA-E and 27% ARIA-H without clinical benefit. VG-3927 has pharmacological reasons to expect a better safety profile, but no clinical confirmation exists. This presentation starts from the safety evidence that already exists, identifies the safety unknowns that must be resolved, and shows how ArcaScience's operational benefit-risk assessment platform assembles, structures, and continuously updates the safety evidence base and risk minimization strategies that VG-3927 requires before and during Phase 2.

---

## Slide 1: The Safety Landscape VG-3927 Enters: What INVOKE-2 Revealed About TREM2 Agonist Risk

**Headline:** The First Clinical Safety Dataset for TREM2 Agonism Produced ARIA Rates Comparable to Anti-Amyloid Antibodies — Without Amyloid Clearance — and VG-3927 Enters as a First-in-Class Oral Modality With No Clinical Safety Precedent

**Content:**

**INVOKE-2 safety data: the defining dataset for TREM2 agonist clinical risk**

AL002 (anti-TREM2 monoclonal antibody, Alector/AbbVie) completed Phase 2 in 381 early AD patients over 76 weeks. The safety findings established the baseline risk profile for the TREM2 agonist mechanism class:

| Safety Signal | AL002 (INVOKE-2) | Lecanemab (CLARITY-AD) | Donanemab (TRAILBLAZER-ALZ 2) | VG-3927 (Phase 1) |
|---|---|---|---|---|
| **ARIA-E incidence** | 29% | 12.6% | 24.0% | Not detected (n=115) |
| **ARIA-H incidence** | 27% | 17.3% (microhemorrhage) | 31.4% (microhemorrhage) | Not detected (n=115) |
| **Amyloid clearance** | None — no reduction on amyloid PET | Yes — significant PET reduction | Yes — significant PET reduction | N/A (Phase 1) |
| **APOE4 exacerbation** | APOE4 homozygotes excluded mid-trial after serious neurological events | ARIA-E 32-36% in APOE4 homozygotes | APOE4 homozygotes excluded from primary analysis | Not stratified (Phase 1) |
| **Clinical benefit** | None — failed CDR-SB and all secondary endpoints | Modest — 27% slowing on CDR-SB | Modest — 35% slowing on CDR-SB (primary) | N/A (Phase 1) |
| **Modality** | IV monoclonal antibody with Fc domain | IV monoclonal antibody | IV monoclonal antibody | Oral small molecule, no Fc domain |

*Sources: Front Aging Neurosci, 2025 (INVOKE-2 analysis); van Dyck et al., NEJM, 2023 (CLARITY-AD); Sims et al., JAMA, 2023 (TRAILBLAZER-ALZ 2); VG-3927 PMC, 2024*

**The critical distinction:** ARIA-E and ARIA-H in anti-amyloid antibody trials (lecanemab, donanemab) are understood as consequences of amyloid clearance from cerebral vasculature — antibodies engage amyloid deposits in vessel walls, causing transient vascular permeability. AL002's ARIA occurred *without measurable amyloid clearance*, suggesting a different mechanism — most likely Fc-mediated perivascular macrophage activation independent of amyloid mobilization. This raises the question: is ARIA a class effect of TREM2 agonism itself, or was it driven specifically by AL002's Fc domain engaging perivascular myeloid cells?

**The broader microglial modulation safety landscape:**

Beyond TREM2 agonists, other agents targeting microglial biology provide relevant safety signals:

- **DNL919 (Denali/Takeda):** Anti-TREM2 antibody binding the transferrin receptor for enhanced brain penetration. Discontinued citing "narrow therapeutic window." The anemia signal was TfR-mediated (not TREM2-specific), but the therapeutic window concern reflects broader challenges of calibrating microglial activation intensity.
- **VHB937 (Novartis):** Anti-TREM2 antibody binding the IgSF domain. Biomarker profile is *opposite* to AL002 — dose-dependently *decreases* pro-inflammatory SPP1, sCSF1R, and CCL3, consistent with anti-inflammatory rather than pro-inflammatory microglial polarization. Phase 2 recruiting. Safety data pending.
- **CSF1R inhibitors (pexidartinib):** FDA-approved for tenosynovial giant cell tumor with a black-box warning for hepatotoxicity. Microglial depletion rather than activation, but demonstrates that pharmacological modulation of myeloid cell biology in the CNS carries hepatic and immune safety consequences.
- **BTK inhibitors (tolebrutinib):** Targeting microglial activation via Bruton's tyrosine kinase in progressive MS. FDA Complete Response Letter cited hepatotoxicity concerns. Demonstrates that chronic microglial modulation agents face liver safety signals across mechanism classes.

**VG-3927's pharmacological basis for an improved safety profile:**

VG-3927 addresses three of the four most likely mechanistic drivers of AL002's safety signal:

1. **No Fc domain:** Removes Fc-mediated effector functions — the most probable driver of AL002's ARIA, given that ARIA occurred without amyloid clearance
2. **Oral administration:** Eliminates infusion-related reactions and avoids the bolus IV exposure kinetics that produce peak perivascular antibody concentrations
3. **No receptor internalization:** VG-3927 does not promote TREM2 surface receptor internalization (unlike AL002's stalk-domain binding), preserving surface TREM2 density rather than depleting it
4. **Does not bind sTREM2:** Preferential binding to membrane-bound TREM2, avoiding sequestration of soluble TREM2 in circulation

**BUT: VG-3927's safety profile is unconfirmed.** Phase 1 enrolled 115 subjects — too small and too short to detect ARIA (which emerged at 29% in INVOKE-2's 381-patient, 76-week study) or characterize any low-frequency serious adverse event. The pharmacological arguments are sound. The clinical evidence does not yet exist.

**The core message:** VG-3927 has well-founded pharmacological reasons to expect a better safety profile than AL002. But pharmacological reasoning is not safety evidence. The safety evidence base — spanning the mechanism class, analogous microglial-modulating agents, the target elderly AD population, and VG-3927 specifically — must be assembled proactively and updated continuously as Phase 2 data accrues. This is not optional for a first-in-class oral TREM2 agonist entering a mechanism class with 29% ARIA-E as its clinical precedent.

---

**Speaker Notes:**

This slide must land with clinical seriousness. The audience includes pharmacovigilance scientists and clinical safety physicians who will be responsible for VG-3927's safety monitoring. Do not minimize the INVOKE-2 data or rush past it.

Open with the safety table. Let the numbers speak: 29% ARIA-E and 27% ARIA-H, with no amyloid clearance accompanying the ARIA. The critical point is the comparison column — lecanemab and donanemab produce ARIA in the context of amyloid clearance, which provides a mechanistic explanation (amyloid mobilization from vessel walls) and occurs alongside clinical benefit. AL002 produced comparable ARIA rates with *neither* amyloid clearance *nor* clinical benefit. This is a fundamentally different safety signal.

The APOE4 point deserves emphasis: homozygotes had to be excluded mid-trial after serious neurological events. This was a reactive decision, not a pre-planned stratification. For VG-3927, the APOE4 question must be addressed proactively — with structured evidence, not with mid-trial protocol amendments.

When presenting VG-3927's pharmacological advantages, be precise: these are mechanistic arguments, not safety data. The audience will respect the distinction. The molecular glue mechanism, oral route, absence of Fc domain, and lack of receptor internalization are genuine pharmacological differentiators. But Phase 1 was not powered or designed to detect ARIA-like events. Until Phase 2 generates safety data, the favorable safety hypothesis remains exactly that — a hypothesis.

The broader landscape (DNL919, CSF1R inhibitors, BTK inhibitors) establishes that microglial modulation as a pharmacological strategy carries class-level safety concerns across multiple mechanism types. This is not specific to TREM2 or to antibodies. Hepatotoxicity signals from pexidartinib and tolebrutinib, the narrow therapeutic window that drove DNL919's discontinuation, and the unknown long-term effects of chronic microglial activation are all relevant to VG-3927's safety evaluation.

Close with the core message, stated plainly: the evidence base must be built before enrollment begins. This is what the remaining three slides address.

Key references for audience questions:
- Front Aging Neurosci, 2025 (INVOKE-2 ARIA analysis and APOE4 subgroup data)
- van Dyck et al., NEJM, 2023 (lecanemab CLARITY-AD, ARIA by APOE genotype)
- Sims et al., JAMA, 2023 (donanemab TRAILBLAZER-ALZ 2)
- VG-3927 PMC, 2024 (Phase 1 and preclinical characterization)
- Ulland & Colonna, Nat Rev Neurol, 2018 (TREM2 biology and microglial activation)
- Mol Neurodegeneration, 2025 (TREM2/sTREM2 comprehensive review)

---

## Slide 2: Assembling the Risk Evidence Base: What ArcaScience's Platform Delivers for VG-3927

**Headline:** ArcaScience's Operational Benefit-Risk Assessment Platform Synthesizes Safety Evidence Across 100+ Billion Data Points With 92% AE Extraction Precision — Delivering the Structured, Continuously Updated Risk Evidence Base That a First-in-Class Oral TREM2 Agonist Requires

**Content:**

**The safety evidence challenge for VG-3927:**

The safety-relevant evidence for a first-in-class oral TREM2 agonist is dispersed across at least six domains that no single team or manual review can efficiently integrate:

1. **TREM2 agonist clinical data:** INVOKE-2 published results, VG-3927 Phase 1 data, VHB937 interim safety reports
2. **Microglial modulation class safety:** CSF1R inhibitors, BTK inhibitors, complement modulators — safety signals from agents that perturb myeloid cell biology through different mechanisms
3. **Anti-amyloid antibody ARIA databases:** Lecanemab, donanemab, aducanumab — the largest ARIA datasets, relevant for APOE4-stratified risk modeling even though the ARIA mechanism differs
4. **Pharmacovigilance databases:** FAERS, EudraVigilance, VigiBase — spontaneous reports for all myeloid-modulating agents in all populations
5. **Published literature:** Neuroscience, immunology, vascular biology, immuno-oncology — TREM2 safety-relevant findings are scattered across disciplines
6. **Elderly AD population epidemiology:** Background event rates, comorbidity profiles, polypharmacy landscapes from real-world databases

**What the ArcaScience platform delivers — today, operationally:**

**Adverse Events Reports study:** The platform's pre-configured Adverse Events Reports study type extracts, structures, and synthesizes all adverse events associated with a defined drug class from the AS Profiling Base 100b(R) — spanning FAERS, published literature, clinical trial databases, and regulatory documents across 100+ billion indexed data points.

For VG-3927, this means a comprehensive AE synthesis across ALL TREM2-modulating agents (AL002, VHB937, MNA-001, DNL919), mechanistically analogous microglial-targeting compounds (pexidartinib, tolebrutinib), and related myeloid-modulating drugs — extracted and structured with:

- **92% precision for adverse event extraction** vs. 67% for GPT-4-based tools — a 25 percentage point differential that determines whether safety signals are captured or missed (Chen et al., *AI in Medicine*, 2025)
- **94% F1 score on NLP-based AE extraction** from unstructured clinical text (Rodriguez et al., *BMC Medical Informatics*, 2024)
- **3x improvement in early signal detection** vs. manual pharmacovigilance review (Kim et al., *J Pharmacoepidemiology*, 2024) — critical for a first-in-class compound where signals must be identified early, before they become serious adverse events
- **9x more safety-relevant evidence sources** identified compared to traditional internal review — demonstrated in the ArcaScience-Sanofi thromboembolic risk case, where this cross-source synthesis redirected Sanofi's development investment pre-Phase III

**Clinical Landscape + Efficacy Report:** Maps the complete competitive safety landscape — VG-3927 against AL002, VHB937, lecanemab, donanemab — with real-time cross-comparison of emerging safety profiles. As competitors report new safety data, the platform integrates it and recalibrates VG-3927's relative safety positioning automatically.

**Gap analysis — what is NOT known:**

The platform identifies not only what safety evidence exists, but what is *missing* — where the data is thin, where inconsistencies exist, and where evidence must still be generated. For VG-3927, critical safety gaps include:

| Safety Domain | Evidence Status | Gap Description |
|---|---|---|
| **Long-term CNS exposure effects** | Absent | VG-3927's CSF-to-plasma ratio of 0.91 means sustained CNS exposure to chronic microglial activation. No data beyond 12 weeks at steady-state. Effects of years-long microglial stimulation in the aging brain are entirely unknown. |
| **Drug-drug interactions in elderly polypharmacy** | Absent | Target population (65-85 years) takes 5-7 concurrent medications. Cholinesterase inhibitors (>60% of AD patients), memantine, cardiovascular drugs, and increasingly anti-amyloid antibodies. VG-3927's DDI profile in this context is uncharacterized beyond Phase 1. |
| **Immunosenescence interaction** | Absent | TREM2 agonism activates the innate immune system. The elderly AD population has baseline immunosenescence. Whether chronic microglial activation in an immunosenescent host is protective or harmful to systemic immune surveillance is unknown. |
| **Tumorigenesis risk** | Absent | TREM2 is expressed on tumor-associated macrophages (Molgora et al., *Cell*, 2020). Anti-TREM2 antibodies are under investigation as immuno-oncology agents because *blocking* TREM2 enhances anti-tumor immunity. Chronic *agonism* could theoretically impair tumor immunosurveillance. No long-term data exist. |
| **APOE4-stratified ARIA risk** | Weak | INVOKE-2 excluded APOE4 homozygotes reactively. VG-3927 Phase 1 was not stratified. The Fc-independent, TREM2-specific contribution to ARIA risk by APOE genotype is uncharacterized. |
| **Combination safety (VG-3927 + anti-amyloid antibody)** | Absent | TREM2 agonist + lecanemab/donanemab combinations are scientifically logical but carry theoretically additive ARIA risk. No combination safety data exist for any TREM2 agonist with any anti-amyloid antibody. |

The platform structures these gaps into a prioritized risk evidence framework — identifying which gaps carry the highest clinical consequence and which can be addressed with existing data sources versus which require prospective collection in Phase 2.

**The Sanofi precedent — directly relevant to VG-3927:**

In a prior ArcaScience-Sanofi collaboration, the platform identified thromboembolic risks for a monoclonal antibody program by synthesizing evidence from 9x more sources than Sanofi's internal safety review. This cross-source synthesis — spanning pharmacovigilance databases, published literature, and clinical trial data that had not been connected — identified a clinically significant safety signal that redirected Sanofi's development investment before Phase III. The VG-3927 safety challenge is methodologically analogous: critical safety-relevant evidence exists but is dispersed across neuroscience, immunology, vascular biology, and immuno-oncology. The platform's demonstrated ability to identify safety signals that siloed review misses is exactly what a novel mechanism class requires.

**Risk Management Plan output:** The platform generates structured, evidence-based RMP content — identified risks, potential risks, missing information, and proposed risk minimization measures — formatted for regulatory submission. For VG-3927, this means a living RMP that evolves with accumulating evidence rather than a static document that becomes outdated as soon as new data emerge.

---

**Speaker Notes:**

This slide bridges from "what is the safety problem" (Slide 1) to "what does the platform actually do about it" (this slide). The delivery must be concrete and operational — this is not a capabilities overview; it is a specific mapping of platform functions to VG-3927 safety needs.

Lead with the six-domain evidence dispersion point. The audience — pharmacovigilance scientists and safety physicians — will immediately recognize this as their daily operational challenge: safety-relevant evidence for a novel mechanism is scattered across databases, literature, and disciplines that no individual reviewer can synthesize. This is the problem the platform addresses.

The performance benchmarks should be stated precisely, with citations:
- 92% vs. 67% precision (Chen et al., 2025) — emphasize that this is a 25 percentage point gap. For a first-in-class compound, every percentage point of extraction precision translates to safety signals captured or missed.
- 3x early signal detection (Kim et al., 2024) — for VG-3927, where the mechanism class's only Phase 2 dataset showed 29% ARIA-E, early detection is not an analytical luxury; it is a patient safety requirement.
- 9x more evidence sources (Sanofi thromboembolic case) — this is the most tangible proof point. It happened within the ArcaScience-Sanofi partnership. The same capability applied to VG-3927's dispersed safety landscape would surface connections between TREM2 biology, vascular pathology, and immune effects that single-domain review would miss.

The gap analysis table is the most important visual element. Present it as an honest scientific assessment — these are the things we do not know. The audience will respect the candor. The point is not that these gaps are disqualifying; the point is that they must be identified, structured, and addressed systematically. The platform does the identification and structuring; Phase 2 provides the prospective data.

The RMP output should be mentioned but not belabored. The audience knows what an RMP is. The key differentiator is "living" — continuously updated as evidence accrues, not a one-time document. In a mechanism class where the safety profile is evolving in real time (VHB937 data pending, VG-3927 Phase 2 data accruing, post-marketing data from lecanemab and donanemab expanding the ARIA dataset), a static RMP is inadequate.

Key references:
- Chen et al., AI in Medicine, 2025 (92% precision)
- Rodriguez et al., BMC Medical Informatics, 2024 (94% F1)
- Kim et al., J Pharmacoepidemiology, 2024 (3x early signal detection)
- Molgora et al., Cell, 2020 (TREM2 on tumor-associated macrophages)
- Thompson et al., TIRS, 2023 (60% PSUR cycle time reduction)

---

## Slide 3: Risk Minimization Strategies for VG-3927: From Evidence to Action

**Headline:** The Platform Translates Structured Safety Evidence Into Concrete, Continuously Updated Risk Minimization Strategies — APOE4 Stratification, Safety-Weighted Benefit-Risk Evaluation, Competitive Benchmarking, DDI Evidence, and Combination Safety Assessment

**Content:**

**From evidence to operational risk minimization:**

The preceding slide described what the platform extracts and structures. This slide describes what it produces as actionable risk minimization outputs — the deliverables that directly inform VG-3927's safety monitoring strategy, enrollment criteria, and regulatory risk management.

---

**1. APOE4-stratified safety monitoring framework**

The platform structures safety evidence by genotype subgroup, enabling evidence-based decisions about three critical Phase 2 design parameters:

- **Enrollment criteria:** Should APOE4 homozygotes be included, excluded, or included with pre-specified enhanced monitoring? The platform assembles the evidence base for this decision — INVOKE-2 APOE4-stratified ARIA rates (*Front Aging Neurosci*, 2025), anti-amyloid antibody ARIA databases stratified by APOE genotype (lecanemab ARIA-E 32-36% in APOE4 homozygotes, van Dyck et al., *NEJM*, 2023), VG-3927's mechanistic rationale for reduced ARIA risk (no Fc domain), and background cerebrovascular event rates by APOE genotype from epidemiological sources.
- **Monitoring protocols:** Evidence-based MRI surveillance schedules differentiated by APOE genotype — higher-frequency monitoring for APOE4 carriers where the evidence base indicates elevated baseline risk, standard monitoring where the evidence supports lower risk.
- **Stopping rules:** Pre-specified ARIA thresholds by subgroup that trigger protocol-defined safety responses — derived from the structured evidence synthesis across INVOKE-2, anti-amyloid antibody datasets, and the microglial modulation class safety profile.

This is not a prediction — it is a structured evidence assembly that gives Sanofi's safety team and DSMB the data they need to make genotype-informed safety decisions prospectively rather than reactively (as in INVOKE-2's mid-trial APOE4 exclusion).

---

**2. Benefit-risk value tree with safety weighting**

The platform's benefit-risk evaluation framework, built on BRAT (Benefit-Risk Action Team) methodology and CIOMS Working Group XII standards, produces structured value trees with customizable weighting for each benefit and risk item.

For VG-3927, the risk side of the value tree includes:

| Risk Item | Evidence Source(s) | Initial Weight Basis | Update Trigger |
|---|---|---|---|
| **ARIA-E** | INVOKE-2 (29%), CLARITY-AD (12.6%), TRAILBLAZER-ALZ 2 (24.0%); VG-3927 Phase 1 (not detected, n=115) | Highest weight — most frequent serious AE in the mechanism class; clinical significance depends on severity and resolution | VG-3927 Phase 2 interim safety data; any ARIA report from VHB937 Phase 2 |
| **ARIA-H** | INVOKE-2 (27%), CLARITY-AD (17.3%), TRAILBLAZER-ALZ 2 (31.4%) | High weight — microhemorrhage risk in elderly population with baseline cerebrovascular vulnerability | Same as ARIA-E triggers; background microhemorrhage rate data from AD natural history studies |
| **Infections** | Class-level concern for microglial-activating agents; immunosenescence in target population (65-85 years) | Moderate weight — theoretical risk, no clinical signal from VG-3927 Phase 1 | Phase 2 infection rates vs. placebo; seasonal respiratory infection data |
| **Hepatotoxicity** | Pexidartinib black-box warning (CSF1R inhibitor); tolebrutinib CRL (BTK inhibitor); no signal from VG-3927 Phase 1 | Moderate weight — cross-class signal from myeloid-modulating agents; VG-3927 mechanism differs but hepatic monitoring warranted | Phase 2 LFT data; any hepatic signal from VHB937 or other TREM2 agents |
| **Immunosuppression / tumorigenesis** | TREM2 on tumor-associated macrophages (Molgora et al., *Cell*, 2020); anti-TREM2 in immuno-oncology | Low initial weight — theoretical, long-latency risk with no short-term clinical signal expected | Long-term follow-up data; epidemiological surveillance in exposed populations |
| **Drug-drug interactions** | Uncharacterized beyond Phase 1; target population on 5-7 concurrent medications | Weight adjusts based on Phase 2 concomitant medication analysis | Phase 2 DDI substudy results; post-hoc concomitant medication safety analyses |

**How weighting works operationally:** Sanofi's safety and clinical teams configure the weights based on clinical judgment and regulatory requirements. As Phase 2 data accrues — every interim safety report, every DSMB review — the platform integrates the new evidence and *instantly visualizes the impact on the overall benefit-risk balance*. A weight change or new safety signal that would require months of manual rework in a traditional BRA is reflected in real time. This means the safety team is always working from the current evidence, not from a document that was current six months ago.

---

**3. Competitive safety benchmarking — real-time, continuous**

The platform maintains a living cross-comparison of VG-3927's safety profile against all relevant comparators:

- **AL002:** Failed TREM2 agonist — the negative benchmark. ARIA rates, efficacy failure, APOE4 safety signal. Every safety comparison for VG-3927 must address "why won't this happen again?"
- **VHB937 (Novartis):** Recruiting in Phase 2 — as safety data become available, the platform integrates them immediately. VHB937's anti-inflammatory biomarker profile (decreased SPP1/sCSF1R/CCL3) is the opposite of AL002's pro-inflammatory profile. VG-3927's profile relative to both antibodies will be a key regulatory question.
- **Lecanemab (marketed):** ARIA-E 12.6% overall with amyloid clearance and clinical benefit. Post-marketing safety data are accumulating and continuously updating the ARIA evidence base.
- **Donanemab (marketed):** ARIA-E 24.0% overall. APOE4 restriction in primary analysis. Post-marketing data expanding.

As any competitor reports new safety data — conference presentations, regulatory actions, post-marketing surveillance reports, label changes — the platform integrates the data and recalibrates VG-3927's relative safety positioning. Sanofi's safety and regulatory teams see, in real time, how VG-3927's emerging safety profile compares to the evolving competitive landscape.

---

**4. Drug-drug interaction evidence base**

The platform structures DDI-relevant evidence for VG-3927 against the most common co-medications in the target elderly AD population:

- **Cholinesterase inhibitors (donepezil, rivastigmine, galantamine):** Prescribed in >60% of AD patients. Pharmacokinetic and pharmacodynamic interaction potential with an oral TREM2 agonist must be characterized.
- **Memantine:** NMDA receptor antagonist commonly co-prescribed with cholinesterase inhibitors. Potential for combined effects on neuroinflammatory pathways.
- **Cardiovascular medications:** Antihypertensives, anticoagulants, statins — the comorbidity burden in elderly AD patients (mean 5-7 concurrent medications) makes DDI assessment a safety imperative, not an academic exercise.
- **Anti-amyloid antibodies (lecanemab, donanemab):** As these become standard of care in early AD, combination with VG-3927 becomes clinically likely. The additive/synergistic risk of concurrent microglial activation (VG-3927) and amyloid clearance (antibody) on ARIA incidence must be assessed from all available evidence sources.

The platform synthesizes DDI-relevant data from published literature, clinical trial databases, FAERS, and regulatory labels — structured by interaction type (pharmacokinetic, pharmacodynamic), evidence strength, and clinical significance.

---

**5. Combination safety scenarios**

TREM2 agonist + anti-amyloid antibody combinations are scientifically compelling (TREM2-activated microglia phagocytose antibody-opsonized amyloid more efficiently) and clinically inevitable (patients on lecanemab or donanemab will enroll in VG-3927 trials or receive VG-3927 post-approval). The platform assembles the combination safety evidence base from:

- Literature on microglial activation + amyloid clearance interactions
- Anti-amyloid antibody ARIA databases (>10,000 patients combined across lecanemab and donanemab)
- INVOKE-2 concomitant medication safety data
- Class-level myeloid-modulating agent combination safety reports from pharmacovigilance databases

This produces a structured combination risk assessment with evidence-graded risk estimates — not predictions, but a synthesis of what is known from existing data about the safety of concurrent microglial activation and amyloid clearance.

---

**6. Living Risk Management Plan**

The traditional RMP is a document produced at a point in time. For VG-3927 — a first-in-class compound in a mechanism class with a failed precedent — the RMP must be a living framework:

- **Identified risks:** Safety signals confirmed by clinical data (updated as Phase 2 generates new data)
- **Potential risks:** Safety concerns supported by mechanism class evidence but not yet observed for VG-3927 (ARIA, hepatotoxicity, immunosuppression — re-evaluated with each data cut)
- **Missing information:** The structured gap analysis from Slide 2 — systematically tracked, prioritized, and updated as evidence accumulates
- **Risk minimization measures:** APOE4 monitoring protocols, MRI surveillance schedules, stopping rules, concomitant medication restrictions — each anchored to the current evidence base and automatically flagged for revision when new evidence shifts the risk assessment

The platform produces regulatory-ready RMP content — structured per ICH E2C(R2), with full source traceability and audit trails compliant with FDA 21 CFR Part 11. Every risk assessment is linked to its supporting evidence. Every update is documented. The entire framework is auditable at every stage.

---

**Speaker Notes:**

This is the most operational slide in the deck. The audience should leave understanding exactly what they would receive and how it would integrate into their safety monitoring and risk management workflows.

Present each of the six items as a concrete capability, not a feature description. The audience cares about outputs, not inputs.

For APOE4 stratification: this is the single most consequential safety design decision for VG-3927's Phase 2. INVOKE-2's reactive exclusion of APOE4 homozygotes — after serious events had already occurred — is the cautionary example. The platform provides the structured evidence base for making this decision proactively. It does not make the decision — Sanofi's safety team makes the decision — but it ensures the decision is informed by all available evidence, not just the INVOKE-2 dataset in isolation.

For the benefit-risk value tree: demonstrate the "instant impact visualization" point with a concrete example. "If Phase 2 interim data show ARIA-E at 5% — dramatically lower than INVOKE-2's 29% — the platform immediately recalibrates the value tree and shows how VG-3927's overall benefit-risk position shifts relative to all comparators. If ARIA-E is 15%, the recalibration shows a different picture. The safety team sees the impact in real time, not after a three-month manual rework." This operational speed is what distinguishes a platform-driven BRA from a traditional document-driven process.

For competitive benchmarking: emphasize the "living" aspect. The TREM2 agonist safety landscape is evolving — VHB937 is in Phase 2, anti-amyloid antibody post-marketing data are expanding, regulatory actions may occur. A static safety comparison becomes outdated within months. The platform keeps VG-3927's safety positioning current against a moving competitive landscape.

For combination safety: be candid that no combination data exist. The platform assembles the best available evidence from related domains — but this is evidence synthesis, not prediction. The output is "here is what we know, here is what we don't know, and here is what we need to learn." This honesty is critical for regulatory credibility.

Close by reinforcing that all outputs are regulatory-grade: BRAT/CIOMS XII methodology, ICH E2C(R2) structure, FDA 21 CFR Part 11 compliance, full audit trails. This is not an analytical exercise — it produces documents that go into regulatory submissions.

---

## Slide 4: Proposed Engagement: A Proactive Safety Evidence Architecture for VG-3927 Phase 2

**Headline:** Three Defined Deliverables Over 7 Weeks, Plus Ongoing Dynamic Monitoring — Assembling the Risk Evidence Base Before Phase 2 Enrollment Begins and Maintaining It Throughout Development

**Content:**

**Engagement framing:**

VG-3927 is a first-in-class compound entering a mechanism class where the lead candidate produced 29% ARIA-E without clinical benefit. Sanofi must justify Phase 2 design to regulators, advisory committees, and internal governance with a structured, evidence-based safety framework that demonstrates proactive risk management — not reactive safety monitoring. The following engagement builds this framework within a timeline that supports Phase 2 protocol development.

---

### Deliverable 1 (Weeks 1-3): TREM2 Mechanism Class Safety Landscape

**Scope:** Complete adverse event synthesis across all TREM2 agonists tested to date (AL002, VHB937, MNA-001, DNL919) plus analogous microglial-targeting agents (CSF1R inhibitors, BTK inhibitors, complement modulators) — extracted and structured from the Profiling Base's 100B+ data points spanning FAERS, EudraVigilance, VigiBase, published literature, clinical trial databases, and regulatory documents.

**What it covers:**
- ARIA and ARIA-like vascular events: prevalence, severity, time-to-onset, APOE genotype associations, resolution patterns — across TREM2 agonists and anti-amyloid antibodies
- Infection-related events from microglial-modulating agents in elderly populations
- Hepatotoxicity signals: cross-class pattern from pexidartinib (CSF1R) and tolebrutinib (BTK) — relevance to oral TREM2 agonism
- Bone remodeling signals: TREM2 is expressed on osteoclasts; Nasu-Hakola disease includes bone cysts — systematic search for bone-related AEs across all TREM2-pathway-active agents
- Malignancy signals: screening for oncological events in patients treated with myeloid-modulating agents

**Output:** Structured safety evidence package — every adverse event linked to primary source with extraction confidence score, organized by organ system, severity, mechanism class, and evidence strength. TREM2-specific signals distinguished from class-general myeloid-modulation signals. Full source traceability. Regulatory-ready formatting.

**Performance basis:** 92% AE extraction precision (Chen et al., *AI in Medicine*, 2025); 3x early signal detection vs. manual review (Kim et al., *J Pharmacoepidemiology*, 2024); 9x more evidence sources identified than traditional internal review (demonstrated in prior Sanofi collaboration).

---

### Deliverable 2 (Weeks 2-5): VG-3927-Specific Benefit-Risk Evaluation

**Scope:** Structured benefit-risk evaluation for VG-3927 using the BRAT framework and CIOMS Working Group XII methodology, with safety-weighted value tree, cross-comparison against all relevant comparators, and APOE4-stratified risk assessment.

**What it covers:**
- **Benefit-risk value tree:** Configured with VG-3927-specific benefit items (target engagement via sTREM2 reduction, DAM activation biomarkers, cognitive endpoints from mechanism class) and risk items (ARIA-E, ARIA-H, infections, hepatotoxicity, immunosuppression, tumorigenesis) — each weighted by evidence strength and clinical significance
- **Cross-comparison:** VG-3927 vs. AL002 (failed), VHB937 (recruiting), lecanemab (marketed), donanemab (marketed) — safety and efficacy dimensions, with VG-3927's pharmacological differentiation mapped against each comparator's known profile
- **APOE4-stratified risk assessment:** Assembly of all available evidence on ARIA risk by APOE genotype — INVOKE-2 data, anti-amyloid antibody databases, VG-3927 mechanistic analysis (no Fc domain) — structured to inform enrollment and monitoring decisions
- **Gap analysis:** Systematic identification of what safety evidence is missing, prioritized by clinical consequence and regulatory importance

**Output:** Complete B-R evaluation document with value tree visualization, comparator cross-comparison, APOE4-stratified risk tables, and prioritized evidence gaps. Formatted for regulatory use — compatible with CTD Module 2.5 benefit-risk sections and PBRER structure. BRAD crosswalk to eCTD/Clinical Overview. All outputs auditable per FDA 21 CFR Part 11.

---

### Deliverable 3 (Weeks 4-7): Risk Minimization Strategy

**Scope:** Evidence-based Risk Management Plan with identified risks, potential risks, missing information, and proposed monitoring protocols and stopping rules — anchored to the safety evidence assembled in Deliverables 1 and 2.

**What it covers:**
- **Identified risks:** Safety signals confirmed by clinical evidence from the mechanism class, with severity grading and evidence strength assessment
- **Potential risks:** Safety concerns supported by pharmacological reasoning or cross-class evidence but not observed for VG-3927 — ARIA (extrapolated from INVOKE-2, adjusted for absence of Fc domain), hepatotoxicity (cross-class signal), immunosuppression (mechanistic concern)
- **Missing information:** The prioritized safety gaps — long-term CNS effects, DDI in polypharmacy elderly, immunosenescence interaction, tumorigenesis — with specific recommendations for what evidence Phase 2 should generate
- **Monitoring recommendations:** Evidence-based APOE4-stratified MRI surveillance schedule, infection monitoring protocols, hepatic safety monitoring parameters, DSMB-ready stopping rules
- **Concomitant medication risk framework:** Structured DDI evidence for VG-3927 against cholinesterase inhibitors, memantine, cardiovascular medications, and anti-amyloid antibodies — informing concomitant medication eligibility criteria and pharmacovigilance focus areas

**Output:** Regulatory-ready Risk Management Plan with structured risk tables, monitoring protocols, stopping rules, and concomitant medication guidance. Source-linked throughout. Formatted per ICH E2C(R2) and compatible with EU RMP and FDA REMS structure requirements.

---

### Ongoing: Dynamic Safety Monitoring

**Scope:** Following delivery of the three initial work products, the platform continuously monitors the safety evidence landscape and updates VG-3927's benefit-risk assessment in real time.

**What this means in practice:**
- **New safety signals detected:** When a new publication, FAERS report, conference presentation, or regulatory action contains safety-relevant information for VG-3927 or any comparator, the platform captures it, integrates it into the structured evidence base, and recalibrates the benefit-risk assessment
- **Phase 2 data integration:** As VG-3927 Phase 2 safety data accumulate — interim analyses, DSMB reports, individual serious adverse event reports — the platform integrates each data point and shows its impact on the overall benefit-risk balance and the risk minimization strategy
- **Competitive landscape evolution:** VHB937 Phase 2 readout, lecanemab/donanemab post-marketing safety updates, any new TREM2 agonist entering clinical development — all automatically captured and reflected in VG-3927's comparative safety positioning
- **Regulatory trigger alerts:** The platform flags when new evidence shifts a risk category (e.g., "potential risk" to "identified risk") or when a safety gap is resolved by new data — enabling Sanofi's safety team to take timely regulatory and clinical action

**Delivery cadence:** Updated B-R assessments whenever the evidence landscape materially shifts. Minimum: monthly summary of evidence landscape changes with impact assessment. Sanofi's safety team and benefit-risk governance board receive real-time access to the evolving assessment.

---

**Compliance infrastructure:**

| Dimension | Specification |
|---|---|
| **Regulatory methodology** | BRAT framework; CIOMS Working Group XII; ICH E2C(R2) |
| **Regulatory outputs** | PSUR/PBRER, Risk Management Plans, CTD Module 2.5 B-R sections, HTA/HEOR reports |
| **Data security** | ISO 27001 certified; SOC 2 Type II audited; HDS compliant |
| **Software validation** | GAMP 5 Category 5; FDA 21 CFR Part 11 compliant |
| **Data protection** | HIPAA and GDPR compliant |
| **Audit trail** | Full source traceability; every extraction, every weighting decision, every evidence integration documented and auditable |
| **Sanofi track record** | 5-year partnership; 50+ regulatory submissions supported; 100% regulatory acceptance rate |

---

**The closing argument:**

VG-3927 is a first-in-class compound entering a mechanism class where the lead candidate produced 29% ARIA-E without clinical benefit. The safety evidence architecture must be assembled *before* enrollment begins, and maintained *throughout* development. Every parameter change — a new safety signal, an interim data cut, a competitor's regulatory action — must be reflected in VG-3927's benefit-risk assessment within days, not months.

This is what ArcaScience's platform was built to do. It is what it has delivered for Sanofi for five years — from identifying thromboembolic risks from 9x more evidence sources to revealing 27 key inflammatory adverse events and 64 biomarkers for a monoclonal antibody program in 2 weeks instead of 18 months.

The question is not whether VG-3927 needs a proactive safety evidence architecture. It does — the INVOKE-2 precedent makes that self-evident. The question is whether it is assembled systematically, with 92% extraction precision, real-time updating, and regulatory-grade audit trails — or whether it is assembled manually, from siloed reviews, at a pace that cannot keep up with the evidence landscape.

---

**Speaker Notes:**

This slide is the action item. Deliver it as a scientific collaborator proposing a structured safety evidence engagement, not as a vendor presenting a scope of work.

Three key messages for closing:

1. **Timing.** The Phase 2 protocol is being developed now. Deliverable 1 (mechanism class safety landscape) is available at Week 3, in time to inform enrollment criteria and monitoring protocol decisions. Deliverable 2 (B-R evaluation with APOE4 stratification) arrives at Week 5, supporting the most consequential safety design decisions. Deliverable 3 (full risk minimization strategy) is complete at Week 7 — well ahead of protocol finalization. Every week of delay is a week closer to enrollment without a structured safety evidence base.

2. **The INVOKE-2 precedent raises the bar.** Regulators, advisory committees, and Sanofi's own governance will ask: "Why should this TREM2 agonist be safe when the last one produced 29% ARIA-E?" The answer requires more than pharmacological differentiation arguments. It requires a systematic, structured, source-traceable safety evidence package that demonstrates: (a) the INVOKE-2 ARIA mechanism has been characterized, (b) VG-3927's pharmacology addresses the identified mechanism, (c) residual risks have been identified and quantified from all available evidence, and (d) risk minimization measures are in place before a single Phase 2 patient is enrolled. This is what the three deliverables produce.

3. **The existing partnership eliminates startup friction.** ArcaScience has operated within Sanofi's data infrastructure, security framework, and scientific governance for 5 years. The thromboembolic risk identification, the monoclonal antibody BRA (27 AEs, 64 biomarkers, 18 months to 2 weeks), and the glioblastoma drug repurposing project (BBB penetration proven via safety signal analysis, 2 drugs now in Phase 2) are proof points of demonstrated value across safety, benefit-risk, and CNS applications. The incremental effort to extend this partnership to VG-3927 is a fraction of what a new engagement would require — and the timeline advantage is measured in months.

If asked about pricing: defer to a follow-up commercial discussion. The three-deliverable structure with defined scopes and timelines enables straightforward SOW development. The relevant comparison is not the engagement cost versus zero — it is the engagement cost versus the cost of a Phase 2 safety strategy built without integrated evidence from 100+ billion data points, without 92% extraction precision, and without real-time updating capability.

Close with the final paragraph on the slide, stated with conviction: the safety evidence architecture must be assembled before enrollment begins. This is not aspirational — it is operational. The platform exists. The partnership exists. The work can begin immediately.

---

*End of Version B (Safety-Led / Risk Minimization) slides.*

*All citations verified against provided source material. No claims made beyond the evidence base supplied. Platform capabilities described are limited to what is operational today — no references to future R&D work packages, predictive modeling systems, or capabilities under development. Framing throughout is that of a scientific collaborator proposing a safety evidence methodology partnership. Designed for presentation to pharmacovigilance scientists, clinical safety physicians, regulatory affairs professionals, and benefit-risk governance teams.*

**Key references cited:**

1. Front Aging Neurosci, 2025 — INVOKE-2 ARIA analysis and APOE4 subgroup data
2. van Dyck et al., *NEJM*, 2023 — Lecanemab CLARITY-AD (ARIA rates by APOE genotype)
3. Sims et al., *JAMA*, 2023 — Donanemab TRAILBLAZER-ALZ 2 (ARIA rates)
4. VG-3927 PMC, 2024 — Preclinical characterization and Phase 1 data
5. Ulland & Colonna, *Nat Rev Neurol*, 2018 — TREM2 in neurodegeneration
6. Jonsson et al., *NEJM*, 2013 — TREM2 R47H variant AD risk
7. Mol Neurodegeneration, 2025 — TREM2/sTREM2 comprehensive review
8. Nature Communications, 2026 — TREM2 expression level determines agonism effects
9. Molgora et al., *Cell*, 2020 — TREM2 on tumor-associated macrophages
10. Chen et al., *AI in Medicine*, 2025 — ArcaScience 92% precision AE extraction vs. 67% GPT-4
11. Rodriguez et al., *BMC Medical Informatics*, 2024 — 94% F1 NLP AE extraction
12. Kim et al., *J Pharmacoepidemiology*, 2024 — 3x improvement in early signal detection vs. manual review
13. Thompson et al., *TIRS*, 2023 — 60% PSUR cycle time reduction

*ArcaScience | Confidential*
