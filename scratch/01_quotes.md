# MHRA Meeting Transcript Analysis: Key Quotes and Concerns by Theme

**Meeting Date:** (From transcript)
**MHRA Participants:** Steph (Interlocuteur 1), Sharinto (Interlocuteur 2), Allison (Interlocuteur 7 -- Senior, most skeptical)
**ArcaScience Participants:** Romain/CEO (Interlocuteur 3), Carlo (Interlocuteur 4), Eric (Interlocuteur 5), Julien/CBO (Interlocuteur 6), Charbel/PM (Interlocuteur 8)

---

## Overall Assessment

Allison dominates the meeting as the senior decision-maker and most critical voice. Steph is the most receptive ("it offers utility" at 03:44) but still has fundamental questions about data quality and auditability. Sharinto focuses on data governance and confidentiality. The meeting ends with MHRA uncommitted and requesting time to deliberate internally.

**The single biggest takeaway:** MHRA is a POST-authorization safety body. Every pitch element that centers on pre-authorization / clinical trial data undermines credibility. The follow-up must be 100% anchored in post-authorization workflows.

---

## Theme 1: POST-AUTHORIZATION APPLICABILITY (The Central Blocker)

This is the dominant theme of the meeting and the single biggest obstacle to moving forward. Allison makes this point repeatedly and with increasing force.

### Quote 1 -- Steph signals post-auth orientation (04:18)
> "There's the type of thing that I have seen in industry. Where it's setting out the benefits and risk at the point of authorization. A lot of what we do is managing those risks. And they're not obviously as I said earlier, looking at safety post authorization. So that's kind of where we would be looking to use something like this."

**Analysis:** Steph is politely saying the platform looks like a pre-authorization tool, but their work is post-authorization. This is an early warning that ArcaScience's positioning is misaligned.

### Quote 2 -- Allison cannot see post-auth use (23:23)
> "So I am struggling to understand how we would use this in the post authorization space. I can sort of see how you might use it in that context because you've got structured data coming in from clinical trials, such as high quality... And you build bespoke models for every use case effectively."

**Analysis:** Allison acknowledges the pre-auth use case but explicitly states it does not apply to her team. The follow-up must demonstrate a post-auth scenario where the platform adds value with unstructured, messy, real-world data.

### Quote 3 -- The definitive statement (36:28)
> "I'm not interested... you know, you're talking to a load of post authorization people here... if you think this is messy, noisy data, you know, welcome to the world of post authorization, which is a million times worse. So how do you solve MY problem rather than THIS problem?"

**Analysis:** This is the most forceful and important statement in the entire meeting. Allison is saying: stop talking about pre-authorization. We are post-authorization. Our data is orders of magnitude messier. Solve OUR problem. Every element of the follow-up response must be framed around this demand.

### Quote 4 -- "That's what I want you to solve" (36:23)
> "That's what I want you to solve."

**Analysis:** In response to Steph suggesting that no tool can solve the antidepressant / long-marketed drug problem, Allison pushes back: that IS what she wants solved. She is not interested in easy problems.

### Quote 5 -- Concrete use case: antidepressants (24:15)
> "So say, I want to know about... I want to build, I don't know, benefit risk summary. On the risk of antidepressants and persistent sexual dysfunction. So nothing in the clinical trials, effectively because they were 12 week clinical trials. So everything is observational data, anecdotal, reports, yellow card reports, you know things in the media, discussion with patients, whole quality reports."

**Analysis:** This is Allison's test case. It is deliberately chosen to be hard: a well-known post-market safety issue where clinical trial evidence is inadequate, and the evidence base is heterogeneous and low-quality. The follow-up should consider addressing this exact example or one with comparable characteristics.

### Quote 6 -- Efficacy vs. effectiveness distinction (26:31)
> "But we don't do efficacy, of course, we do effectiveness... so no, can't necessarily take efficacy or effectiveness from clinical trial and assume that it translates into performance on the market."

**Analysis:** MHRA works with real-world effectiveness, not RCT efficacy. The platform must understand and operationalize this distinction. Any language about "efficacy" in follow-up materials should be replaced with or accompanied by "effectiveness."

### Quote 7 -- Long-marketed drugs are harder (34:43)
> "I mean, I think that those are much easier questions than for drugs that have been on the market for a long time. And safety events emerge."

**Analysis:** The Sanofi/rare disease example ArcaScience used is perceived as an "easy" problem. MHRA's hard problems involve drugs with decades of market exposure and emerging rare safety signals.

### Quote 8 -- Causality assessment is the real challenge (35:04)
> "You've got a lot of people using them and you may have a rare event. And you're trying to understand causality of that event across a lot of different data sources."

**Analysis:** The word "causality" is key. MHRA does not just aggregate data -- they assess whether a drug CAUSED an adverse event. The platform must support causal reasoning, not just information retrieval.

**What this means for the follow-up:** The proof of concept MUST center on a post-authorization scenario involving messy, heterogeneous data. It must demonstrate value beyond data extraction -- supporting the assessor's critical thinking about causality, data quality, and clinical significance.

---

## Theme 2: MODEL VALIDATION AND AUDITABILITY

### Quote 9 -- Black box concern (05:11)
> "I guess I'm asking about, you know, the black box of that AI tool and what's it based on, because that's fundamental for us to understand that."

**Analysis:** Steph explicitly uses the term "black box" -- the most feared term in regulatory AI. The follow-up must demonstrate complete transparency in how outputs are generated. Every output must be traceable to a specific source and processing step.

### Quote 10 -- Error propagation in serial models (13:07)
> "When you've got such complex models that they're happening in series, how do you validate them? ...how do you identify where that error might have happened?"

**Analysis:** With 24 models in series, errors can compound and become untraceable. Allison needs to know: (a) how each model is independently validated, (b) what the error rate is at each step, and (c) how errors are traced back through the chain. The follow-up should include a validation framework or model performance metrics.

### Quote 11 -- Uncertainty and gap flagging (18:42) -- Sharinto
> "So does it come up with levels of uncertainty, or does it flag where there are issues? For example, because of gaps in information source."

**Analysis:** The platform must produce uncertainty indicators and explicitly flag data gaps. Presenting incomplete information as complete would be a regulatory red flag.

### Quote 12 -- Study quality assessment gap (50:00)
> "Okay, that's extracting information into a structured form for you. To then... it doesn't tell you about the quality of that study. Still."

**Analysis:** This is Allison's most pointed technical critique. After a lengthy explanation from Charbel about the 24 models, Allison distills the gap: the platform extracts data but does NOT assess study quality. For MHRA assessors, study quality assessment is the core of their analytical work. Data extraction alone is table stakes.

### Quote 13 -- What assessors actually do (44:01)
> "What my assessors would do is they would say, okay, there's this observational study that seemed to show an association between the drug and the event. What that assessor then does is not just take the abstract and assume the abstract is right. They look at the methodology, they look at the confidence intervals. They look at the patient populations included. They look at the heterogeneity of the data sources, and they reach an opinion about whether that article is valid..."

**Analysis:** This is a specification document disguised as a question. Allison is telling ArcaScience exactly what the tool needs to do to be useful: methodology critique, CI analysis, population assessment, heterogeneity analysis, validity determination. The follow-up should map platform capabilities to each of these assessor tasks.

### Quote 14 -- "Under the hood" demand (38:54)
> "I need to see. I'd like to see under the hood, really because it's still a bit skeptical, and you haven't convinced me yet that this could... we could use this in our work."

**Analysis:** Allison wants technical transparency, not marketing. She is skeptical but open-minded ("really keen to look for ways to create efficiency"). The follow-up must provide deep technical detail: model architectures, validation metrics, processing pipelines, example outputs.

### Quote 15 -- Can it work today without building a model? (25:44)
> "If I asked your system that question, could it do it today without, or would you need to build a model for it?"

**Analysis:** A direct litmus test. If the answer is "we need to build/configure first," it confirms the scalability concern. The follow-up should demonstrate an ad-hoc query capability that works without bespoke setup.

**What this means for the follow-up:** Provide a transparent technical document showing: model architecture, validation methodology and metrics, error traceability, uncertainty quantification, and how study quality indicators are surfaced to the user.

---

## Theme 3: SCALABILITY (The Operational Dealbreaker)

### Quote 16 -- Scale of MHRA's operations (12:32)
> "We have 100 benefit risk assessors, looking across 600 drugs and millions of thousands and hundreds of thousands of devices. Our questions are not always the same."

**Analysis:** MHRA's scale is fundamentally different from a pharma client. 100 assessors, 600+ drugs, hundreds of thousands of devices, diverse questions. A bespoke-per-use-case approach is operationally impossible.

### Quote 17 -- Cannot build bespoke models for every use case (24:58)
> "What I can't see working is for every specific use case, I have to build a bespoke model."

**Analysis:** Repeated constraint. The models must be reusable across use cases.

### Quote 18 -- 80 concurrent safety issues (53:09)
> "There might be 80 safety issues ongoing at any one time across medicines and medical devices, and we can't develop an AI model for every use case. That's, you know, that's clearly not possible."

**Analysis:** Quantified: 80 concurrent safety issues. The platform must support all of them without per-issue model development.

### Quote 19 -- Must differentiate from ChatGPT (53:36)
> "How could you give out something generic? It's beyond the literature search because I can get ChatGPT to do that potentially or copilot or something. You know, beyond that, that would support the assessors, but doesn't require, you know, bespoke models to be generated every time."

**Analysis:** Two critical implications: (1) ChatGPT/Copilot is the competitive benchmark for literature search -- ArcaScience must demonstrate value ABOVE that baseline. (2) The value must be deliverable generically, without per-case customization.

**What this means for the follow-up:** Demonstrate a generic, reusable pipeline that works across therapeutic areas and safety issues with configuration (not retraining). Clearly articulate differentiation from general-purpose LLMs like ChatGPT.

---

## Theme 4: CONFIDENTIALITY (Hard Constraints on Data Sharing)

### Quote 20 -- CPRD cannot be shared (42:42)
> "We might use CPRD, which is our real world database, but that is billions and billions of data points. 30 million patient records over 30 years. And we might interrogate that. We can't give you that."

**Analysis:** CPRD is off-limits. This is one of the world's largest primary care databases and a cornerstone of MHRA's evidence base. The platform cannot rely on having access to it.

### Quote 21 -- Yellow Card data cannot be shared (43:13)
> "Can't give you our yellow card data because that's far too confidential. Because it's patient level data. We're not allowed to share that."

**Analysis:** Yellow Card (the UK's adverse event reporting system) is also off-limits. Patient-level pharmacovigilance data cannot leave MHRA.

### Quote 22 -- Ongoing safety issues are confidential (52:07)
> "Most of the things that we do are actually highly confidential and I don't think we could share to be honest an ongoing safety issue with you. I don't think we could do that because I just think it would be too confidential at this stage."

**Analysis:** Active safety investigations are commercially and regulatorily sensitive. Only completed, publicly reported cases can be used for a proof of concept.

### Quote 23 -- Multi-company confidentiality complexity (53:51)
> "Here we're working with multiple companies and multiple safety issues in different scenarios, and with very highly sensitive patient level data."

**Analysis:** Unlike pharma clients where ArcaScience works with one company's data, MHRA simultaneously handles data from many companies. This creates a much more complex confidentiality landscape -- data from Company A's product must never be visible in work on Company B's product.

### Quote 24 -- Sharinto raises confidentiality (40:48)
> "In terms of confidentiality... that's obviously where we'll be coming from in terms of protecting that information, because it would obviously be highly sensitive with regards to what we've got access to."

**Analysis:** Sharinto independently raises confidentiality, showing it is a shared concern across the MHRA team, not just Allison's issue.

**What this means for the follow-up:** The proof of concept MUST use only publicly available data. Long-term, the deployment model must address on-premises or secure enclave operation where MHRA data never leaves MHRA infrastructure. Multi-tenant confidentiality (data isolation between different drug/company investigations) must be addressed.

---

## Theme 5: DATA SOURCES AND QUALITY

### Quote 25 -- Data quality is fundamental (04:35)
> "When you're looking at data sources, how are you ensuring the quality of those data sources. Because it looks to me like the platform does make, you know, judgments on those benefits and risks dependent on what it's looking at."

**Analysis:** Steph identifies a circular risk: if the platform's outputs depend on input quality, and input quality is variable, then outputs could be misleading. Quality assurance of inputs is "fundamental."

### Quote 26 -- Incomplete data creates skewed views (18:42) -- Sharinto
> "What we wouldn't want is a skewed view because of perhaps incomplete or inconsistent data or data that's a variable quality."

**Analysis:** The risk is not just missing data but SKEWED conclusions from partial data. The platform must surface what is missing, not just what is found.

### Quote 27 -- Real-world data challenges (32:07)
> "We are dependent on... really real world database, electronic health records or observational studies, which are not easy to derive benefits from."

**Analysis:** MHRA's primary data sources for post-auth work are inherently difficult to work with. The platform must be designed for these data types, not just clean clinical trial data.

### Quote 28 -- Observational studies vs. case reports (47:22)
> "I'm not talking about case reports. I'm talking about big observational studies or meta-analyses. All that type of thing where you don't have patient level data."

**Analysis:** ArcaScience demonstrated case report processing, but MHRA needs aggregate-level study processing. The follow-up must show capability with observational studies and meta-analyses specifically.

### Quote 29 -- Effectiveness data availability challenged (31:45)
> "I don't believe that data is available easily or with any confidence for drugs on the market."

**Analysis:** Allison pushes back on Carlo's assertion that effectiveness data "is available." For marketed drugs, especially older ones, reliable effectiveness data is scarce. ArcaScience must not overstate data availability.

**What this means for the follow-up:** Demonstrate handling of low-quality, heterogeneous, real-world data. Show uncertainty quantification. Show gap detection. Show capability with observational studies and meta-analyses, not just case reports or clinical trials.

---

## Theme 6: UK-SPECIFIC CONTEXT

### Quote 30 -- Drug usage differs by country (26:59)
> "Usage of drugs is very different across the world, and safety events do not necessarily translate across the world, you know, we see different expressions or different safety events depending on how a drug is used first line, second line, third line in different scenarios."

**Analysis:** Global data is not sufficient. UK-specific prescribing patterns, treatment pathways, and population demographics create unique safety profiles. The platform must be able to filter and contextualize for UK-specific usage.

### Quote 31 -- Line of therapy changes benefit-risk (27:25)
> "If there's a drug... you use third line, and there's no other alternative for a patient, then a benefit risk is different to a first line therapy that they can then move on to something else."

**Analysis:** Benefit-risk is context-dependent: the same drug has a different benefit-risk profile depending on where it sits in the treatment pathway and what alternatives exist. The platform must support this contextual analysis.

**What this means for the follow-up:** Demonstrate awareness of UK-specific prescribing patterns. Show ability to contextualize benefit-risk by line of therapy and available alternatives. Consider integrating UK-specific data sources (NICE guidelines, BNF, etc.).

---

## Theme 7: MESSAGING AND CREDIBILITY

### Quote 32 -- "Antibodies going through the roof" (11:58)
> "My antibodies are going through the roof just because it says fill your benefit risk in seconds. Don't spend months looking at it."

**Analysis:** The marketing language actively alienates the senior decision-maker. "In seconds" sounds irresponsible to someone who spends months on careful assessment. All materials for MHRA must strip out speed claims and replace with accuracy/comprehensiveness messaging.

### Quote 33 -- "You make it sound so easy" (32:28)
> "Benefit is the most challenging thing we have to try and get a handle on across the different populations and different ages, comorbidities, ethnicities, whatever. And you make it sound so easy, and it's so so hard."

**Analysis:** ArcaScience's tone is perceived as dismissive of the genuine complexity of regulatory science. The follow-up must lead with humility and acknowledgment of difficulty, positioning the platform as a tool that ASSISTS with hard problems rather than solving them trivially.

**What this means for the follow-up:** Completely reframe messaging for a regulatory audience. Lead with humility. Acknowledge complexity. Position the tool as augmenting (not replacing) expert judgment. Remove any "in seconds" or speed-focused claims from MHRA-facing materials.

---

## Theme 8: COLLABORATION TERMS AND NEXT STEPS

### Quote 34 -- No funding available (54:47)
> "You don't have funding for this. So, you know, it's not something that we could offer funding for at the moment."

**Analysis:** Hard constraint: MHRA will not pay for a proof of concept. ArcaScience must absorb the cost as a strategic investment.

### Quote 35 -- Proof of concept format (55:08)
> "It really would be a proof... some sort of proof of concept where we were just, you know, testing or challenging your system."

**Analysis:** MHRA frames the next step as a TEST, not a partnership. They will challenge the system and evaluate the results. ArcaScience must deliver a compelling, standalone demonstration.

### Quote 36 -- MHRA will pick the use case (52:47)
> "The only thing I'm thinking about is whether we could look at a safety issue that's already in the public domain that we've already reported on."

**Analysis:** MHRA wants to select the test case themselves -- a previously concluded, publicly reported safety issue. This is the most credible test: can the platform reproduce what MHRA already found, and can it find anything additional?

### Quote 37 -- Internal deliberation required (57:51)
> "Let us take it away, and think about it again, and we'll have another look at the platform. And then we'll have an internal conversation. Come back to you."

**Analysis:** MHRA needs time to deliberate internally. ArcaScience should not push for an immediate next meeting but should prepare materials that support MHRA's internal discussion.

### Quote 38 -- Beta platform exploration (58:06)
> "We'll try and think through working through the beta version. We've still got access to that right and then to see if we can see an actual good use case."

**Analysis:** MHRA plans to independently explore the beta. The beta must be compelling, navigable, and self-explanatory enough for MHRA staff to discover value without ArcaScience guidance.

### Quote 39 -- Operational burden question (40:08) -- Sharinto
> "In terms of the data input, you're very much reliant on us to provide you with all of the sources that we would potentially need."

**Analysis:** Sharinto is probing whether the data sourcing burden falls on MHRA. If MHRA has to do all the data work AND then use the platform, the efficiency gain is diminished.

**What this means for the follow-up:** Prepare a self-funded proof of concept using a publicly reported MHRA safety issue. Let MHRA pick the case. Ensure the beta platform is independently navigable. Prepare materials that support MHRA's internal deliberation (concise, technically rigorous, addressing all concerns raised).

---

## Priority Matrix for Follow-Up

| Priority | Theme | Key Action Required |
|----------|-------|-------------------|
| CRITICAL | Post-auth applicability | Reframe entire value proposition around post-authorization safety work |
| CRITICAL | Scalability | Demonstrate generic, reusable pipeline (no bespoke models per case) |
| CRITICAL | Confidentiality | Design proof of concept using only public data; address on-prem deployment |
| CRITICAL | Model validation | Provide transparent technical detail, validation metrics, error traceability |
| CRITICAL | Messaging | Strip speed claims; lead with humility and accuracy positioning |
| HIGH | Data sources | Show capability with observational studies, meta-analyses, real-world data |
| HIGH | UK context | Demonstrate UK-specific contextualization (prescribing patterns, treatment lines) |
| HIGH | Study quality | Address the gap between data extraction and study quality assessment |
| HIGH | Collaboration terms | Prepare self-funded proof of concept; let MHRA select the test case |
| MEDIUM | Auditability | Ensure every output is traceable to source; human-in-the-loop framing |

---

## Speaker-by-Speaker Summary

### Allison (Interlocuteur 7) -- Senior Decision-Maker
- **Stance:** Skeptical but open-minded ("really keen to look for ways to create efficiency")
- **Key demand:** Solve the POST-authorization problem, not the pre-authorization one
- **Biggest concerns:** Scalability (80 concurrent safety issues), confidentiality (cannot share CPRD, Yellow Card, or ongoing investigations), study quality assessment, and differentiation from ChatGPT
- **What would convince her:** A deep technical dive ("under the hood"), a successful proof of concept on a publicly reported safety issue, and a deployment model that does not require bespoke setup per case
- **Red flags triggered:** "Benefit risk in seconds" messaging, case report examples (she wants observational studies), emphasis on pre-auth use cases, perceived oversimplification of benefit assessment

### Steph (Interlocuteur 1) -- Most Receptive
- **Stance:** Cautiously positive ("it offers utility")
- **Key concerns:** Data quality assurance, AI black box / auditability, post-auth applicability
- **What would convince her:** Clear demonstration that the platform augments (not replaces) assessor judgment, with transparent sourcing and quality indicators
- **Most helpful framing:** She already envisions the tool as an "intelligent repository" -- build on this framing

### Sharinto (Interlocuteur 2) -- Governance-Focused
- **Stance:** Neutral, probing
- **Key concerns:** Confidentiality, data governance, operational burden of data sourcing, incomplete data handling
- **What would convince her:** Clear data flow documentation, confidentiality safeguards, uncertainty quantification, and a practical understanding of what MHRA would need to provide vs. what the platform handles
