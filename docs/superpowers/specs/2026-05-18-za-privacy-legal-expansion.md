# ZA Privacy-Legal Expansion — Decision Spec

**Date:** 2026-05-18
**Plugin:** privacy-legal v1.0.2
**Decider:** Rakheen Dama
**Architecture:** ADR-001 (additive overlays in `jurisdictions/za/`)
**Reference implementation:** `jurisdictions/za/employment-legal/`

---

## Decision Summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | privacy-legal — 9 skills, 7 in scope | user confirmed |
| 2 | Statutes | Extend `popia.yaml` (+17 sections). New: `cybercrimes.yaml`, `paia.yaml` | Perplexity + user confirmed |
| 3 | Skill divergence | 5 HIGH, 2 MEDIUM, 2 LOW — 7 in scope | user confirmed |
| 4 | Topic overlays | 6 topic files serving 7 skills | user confirmed |
| 5 | Practice profile | 8 sections replaced, 5 new SA-specific sections | user confirmed |
| 6 | Cold-start questions | 7 must-have, 3 nice-to-have, 6 seed documents | Perplexity verified + user confirmed |
| 7 | High-risk flags | 12 flags mapped to IR enforcement precedent | Perplexity + user confirmed |
| 8 | Validation | 21 eval cases across 6 skills, expert review gate | user confirmed |

---

## 1. Statute Inventory

### Existing statutes — extend

#### `popia.yaml` — 17 new sections

Existing sections (6): operator_agreement_required, security_safeguards, breach_notification, cross_border_transfer, administrative_fine_max, direct_marketing_restrictions.

New sections to add:

| Section key | Ref | Temporal? | Notes |
|---|---|---|---|
| `conditions_lawful_processing` | s8–s12 | No | 8 conditions framework |
| `consent` | s11(1)(a) | No | Consent as lawful basis |
| `purpose_specification` | s13 | No | Purpose limitation |
| `data_retention` | s14 | No | Retention limits |
| `openness_notification` | s18 | No | Notice obligations at collection |
| `data_subject_access` | s23 | No | Right of access, reasonable fee permitted |
| `data_subject_correction_deletion` | s24 | Yes — April 2025 regs | 30-day response, multi-channel |
| `data_subject_objection` | s11(3)(a) | Yes — April 2025 regs | Multi-channel (WhatsApp/SMS/email), recorded telephonic |
| `special_personal_information` | s26–s33 | No | Race, health, biometrics, trade union, criminal, religion, political, sex life |
| `children_personal_information` | s34–s35 | No | Under 18, competent person consent |
| `prior_authorization` | s57 | No | Unique identifiers, criminal data, credit reporting, special PI transfers |
| `information_officer_registration` | s55–s56 | No | IO + deputy IO, eServices portal |
| `automated_decision_making` | s71 | No | Right not to be subject to solely automated decisions |
| `unique_identifiers` | s57(1)(a) | No | Cross-linking triggers prior authorization |
| `direct_marketing_2025_regs` | Regs 2025 Reg 6 | Yes — effective 17 April 2025 | Opt-out ≠ consent, recorded telemarketing, multi-channel consent |
| `complaint_procedures_2025_regs` | Regs 2025 Reg 7 | Yes — effective 17 April 2025 | Expanded standing, 14-day acknowledgment, public interest complaints |
| `eservices_portal_breach_reporting` | IR operational directive | Yes — effective 1 April 2025 | Mandatory breach reporting via eServices portal |

#### `ecta.yaml` — no changes needed

ECTA Chapter VIII data protection provisions repealed when POPIA commenced. Existing 7 sections sufficient.

#### `cpa.yaml` — no changes needed

Existing 7 sections sufficient. Direct marketing under CPA s11 is secondary to POPIA s69 for privacy-legal purposes.

### New statute files

#### `cybercrimes.yaml`

| Section key | Ref | Notes |
|---|---|---|
| `data_offences` | s2–s5 | Unlawful access, interception, interference with data |
| `esp_fi_breach_reporting` | s54 | 72-hour reporting to SAPS — NOT YET IN FORCE |
| `penalties` | s18 | Up to 15 years imprisonment |
| `evidence_preservation` | s41 | Expedited preservation of data direction |

Statute: Cybercrimes Act 19 of 2020
Authority: Department of Justice and Constitutional Development
Source URL: https://www.gov.za/documents/acts/cybercrimes-act-19-2020

#### `paia.yaml`

| Section key | Ref | Notes |
|---|---|---|
| `paia_manual_requirement` | s14 (public), s51 (private) | Manual required for all bodies |
| `information_officer_duties_paia` | s17 | Deputy IO designation under PAIA |
| `refusal_grounds` | s36–s45 (public), s62–s69 (private) | Grounds for refusing access |
| `annual_reporting` | s32, s83(4) | Annual PAIA reports — 2% private body compliance |

Statute: Promotion of Access to Information Act 2 of 2000
Authority: Information Regulator
Source URL: https://www.gov.za/documents/promotion-access-information-act

---

## 2. Skill Divergence Matrix

| Skill | Divergence | In scope | Reasoning |
|---|---|---|---|
| `dpa-review` | HIGH | Y | POPIA "responsible party"/"operator" (not controller/processor). s21 operator agreements ≠ GDPR Art 28. s72 cross-border with no adequacy list. |
| `dsar-response` | HIGH | Y | POPIA s23 access (reasonable fee), s24 correction (30-day response). No portability right. April 2025 regs: multi-channel, recorded telephonic. Exemption framework differs. |
| `pia-generation` | HIGH | Y | No mandatory DPIA — s57 prior authorization instead. 8 conditions framework (not Art 6 bases). Special PI (s26–33), children's PI (s34–35). IR submission for prior authorization. |
| `use-case-triage` | HIGH | Y | "DPIA MANDATORY" → "PRIOR AUTHORIZATION REQUIRED" (s57). Different triggers: unique identifier cross-linking, special PI transfers, credit reporting. s11 lawful bases (not Art 6). |
| `cold-start-interview` | HIGH | Y | ZA fork after Part 0. SA-specific questions, writes to ZA practice profile template. |
| `policy-monitor` | MEDIUM | Y | Drift-detection process portable but regulatory framework changes: POPIA commitments replace GDPR/CCPA. IR direct marketing guidance, eServices portal. |
| `reg-gap-analysis` | MEDIUM | Y | Methodology portable but scoping/framing US-centric. SA: POPIA applicability (s3), IR guidance notes, sector codes. |
| `customize` | LOW | N | Reads/writes practice profile — no embedded legal content. |
| `matter-workspace` | LOW | N | Pure infrastructure — jurisdiction-neutral file management. |

---

## 3. Topic Overlay Map

| Topic file | Skills served | Key content areas |
|---|---|---|
| `data-subject-rights.md` | dsar-response, use-case-triage, policy-monitor | POPIA s23 access (reasonable fee), s24 correction/deletion (30-day per April 2025 regs), s11(3) objection (multi-channel, recorded telephonic), exemption framework (s15, s27, s37), no explicit portability, procedural checklist |
| `operator-agreements.md` | dpa-review, policy-monitor | POPIA s21 framing (not "DPA"), responsible party vs operator terminology, s19 security flow-down, s72 cross-border (no adequacy list, adapted SCCs), direct marketing on operators, term-by-term review mapped to POPIA |
| `impact-assessment.md` | pia-generation, use-case-triage, reg-gap-analysis | s57 prior authorization (replaces GDPR DPIA), triggers: unique identifier cross-linking, special PI/children's PI transfer, credit reporting. 8 conditions as PIA framework. s26–33 special PI, s34–35 children's PI. IR submission for prior authorization |
| `lawful-processing.md` | pia-generation, use-case-triage, dpa-review, reg-gap-analysis, policy-monitor | 8 conditions: accountability, purpose specification, processing limitation, further processing limitation, information quality, openness, security safeguards, data subject participation. s11 lawful bases. s69 direct marketing (opt-out ≠ consent per April 2025 regs) |
| `enforcement-and-compliance.md` | reg-gap-analysis, policy-monitor, dsar-response | IR powers, enforcement notices, s107 fines (R10M max), instalment payments (April 2025 regs), eServices portal (mandatory April 2025), complaint procedures (expanded standing, 14-day ack), IO registration (s55–56), compliance framework (continuously improved), Cybercrimes Act s54 SAPS reporting |
| `cross-border-and-special-categories.md` | dpa-review, pia-generation, use-case-triage | s72 cross-border restrictions (no adequacy list, BCRs, binding agreement, consent), National Data and Cloud Policy (2024), s26–33 special PI categories, s34–35 children's PI, s57 prior authorization for transfers |

---

## 4. Practice Profile Template Design

### Sections replaced (US → ZA)

| US section | ZA replacement | Key changes |
|---|---|---|
| Config header | Add `JURISDICTION OVERLAY` instruction | Router wiring |
| `## Who we are` | "controller/processor" → "responsible party/operator". Regulatory footprint → POPIA, Cybercrimes Act, PAIA | Terminology |
| `## Who's using this` | Role → "Admitted attorney or advocate under Legal Practice Act 28 of 2014 / Non-lawyer with attorney access / Non-lawyer without attorney access" | Same as employment-legal ZA |
| `## DPA playbook` | `## Operator agreement playbook` — "When we are the operator" / "When we are the responsible party". Terms mapped to POPIA s21. | POPIA terminology and framework |
| `## Privacy policy commitments` | `## Privacy notice commitments` — mapped to POPIA s18 openness requirements | POPIA categories |
| `## PIA house style` | Trigger: s57 prior authorization + internal policy. Framework: 8 conditions. Sign-off includes IR submission for prior authorization cases. | POPIA prior authorization replaces GDPR DPIA |
| `## DSAR process` | `## Data subject request process` — s23 access (reasonable fee), s24 correction (30-day, multi-channel), s11(3) objection. No portability right. Telephonic requests recorded per April 2025 regs. | POPIA rights structure |
| `## Escalation` | IR (enforcement, complaints, prior authorization), SAPS (Cybercrimes Act), High Court (appeal), industry bodies | SA regulatory bodies |
| `## Outputs` → header | SA privilege: `PRIVILEGED & CONFIDENTIAL — PREPARED BY/AT THE DIRECTION OF LEGAL COUNSEL FOR THE PURPOSE OF PROVIDING LEGAL ADVICE`. In-house commercial-vs-legal capacity caveat. POPIA s99 IR investigation powers note. | SA privilege formulation |
| `## Seed documents` | Privacy notice/policy, operator agreement template, reference PIA, IO registration certificate, breach response plan, POPIA compliance framework | SA-specific documents |
| Sectoral notices line | Removed entirely | GLBA/HIPAA/FERPA/COPPA are US-specific |

### New SA-specific sections

| Section | Content |
|---|---|
| `## Information Officer` | IO name, registration status (eServices portal), deputy IO, dual duties (POPIA + PAIA), IO must be in SA for multinationals |
| `## POPIA compliance framework` | Framework status, last review date, continuous improvement (April 2025 regs), PI impact assessment status |
| `## Cross-border transfers` | s72 framework, no adequacy list, practical mechanisms (adapted SCCs, BCRs, consent, binding agreement), data location register, IR guidance note expected 2025/26 |
| `## Breach response` | s22 notification (IR + data subjects, "as soon as reasonably possible"), eServices portal (mandatory April 2025), Cybercrimes Act s54 SAPS reporting (when in force), response team, assessment criteria |
| `## Direct marketing compliance` | s69 framework, April 2025 regs (opt-out ≠ consent, recorded telemarketing, multi-channel objection, existing customer exception), IR December 2024 Guidance Note, one-message consent rule |

### Header formulation

Attorney header: `PRIVILEGED & CONFIDENTIAL — PREPARED BY/AT THE DIRECTION OF LEGAL COUNSEL FOR THE PURPOSE OF PROVIDING LEGAL ADVICE`

Non-lawyer header: `CONFIDENTIAL — NOT LEGAL ADVICE — CONSULT AN ADMITTED ATTORNEY OR ADVOCATE BEFORE ACTING`

Privacy-specific note:
> POPIA s99 empowers the Information Regulator to require any person to produce documents or information relevant to an investigation. Legal professional privilege may be asserted but is not an absolute bar to regulatory investigation — the IR may challenge the privilege claim. Mark documents accurately; do not assert privilege over documents that are compliance records rather than legal advice.

### Sections carried unchanged

Config location header structure, quiet mode, proportionality, scaffolding-not-blinders, ad-hoc questions, retrieved-content trust, large input/output, matter workspaces, reviewer note format, decision tree, dashboard, decision posture, shared guardrails, citation hygiene, verification log.

---

## 5. Cold-Start Interview Questions

### Fork mechanism

After Part 0, check company profile → if jurisdiction = ZA, fork to SA interview path. Output writes to ZA practice profile template. Same pattern as employment-legal ZA fork.

### Must-have questions (7)

**Q1: Responsible party or operator orientation?**
> Are you primarily a responsible party, operator, or both?
- Primarily responsible party
- Primarily operator
- Both

**Q2: Information Officer registration?**
> Has your IO been registered with the Information Regulator?
- Yes — IO name, Deputy IO
- Registration in progress
- Not yet

**Q3: POPIA compliance framework?**
> Do you have a documented POPIA compliance framework?
- Yes — last reviewed: _____
- In development
- No

**Q4: Cross-border transfers?**
> Does your organisation transfer PI outside South Africa?
- Yes — countries + mechanism (binding agreement / BCRs / consent / adequate law)
- No
- Not sure

**Q5: Breach response readiness?**
> 1. Do you have a documented breach response plan?
> 2. Are you registered on the IR eServices portal?

**Q6: Direct marketing?**
> Does your organisation do direct marketing by electronic communication?
- Yes — explicit consent in place
- Yes — existing customer exception (s69(4))
- Yes — consent process may need updating
- No

**Q7: Prior authorization processing?**
> Does your organisation do any of: unique identifier cross-linking across responsible parties, criminal behavior data on behalf of third parties, credit reporting, special PI/children's PI transfer to inadequate foreign country?
- Yes (specify which)
- None

### Nice-to-have questions (3)

**Q8:** Sector-specific obligations (financial services, healthcare, telecoms, education)
**Q9:** Data subject request volume and handling
**Q10:** Operator agreement negotiation posture (better extracted from seed doc)

### Seed documents

| Priority | Document |
|---|---|
| Must-have | Privacy notice/policy (URL or file) |
| Must-have | Operator agreement template |
| Must-have | Reference PIA |
| Nice-to-have | IO registration certificate |
| Nice-to-have | Breach response plan |
| Nice-to-have | POPIA compliance framework document |

---

## 6. High-Risk Flag Table

| # | Flag | Statute | What to check | Enforcement precedent |
|---|---|---|---|---|
| 1 | Breach notification failure or delay | s22(1) | IR notified via eServices portal? Data subjects notified? Timely? | Lancet (R100K), DOJ&CD (R5M) |
| 2 | Inadequate security safeguards | s19(1) | Technical measures current? Organizational measures documented? PI impact assessment done? | DOJ&CD (expired licenses), Dis-Chem (3.6M records), TransUnion |
| 3 | No written operator agreement | s21(1) | Written contract with every operator? s19 safeguards covered? | Dis-Chem (no contract with Grapevine) |
| 4 | Direct marketing without valid consent | s69, Regs 2025 | Explicit consent recorded? Existing-customer exception proper? Telemarketing recorded? Multi-channel objection? | FT Rams (R100K — first DM enforcement) |
| 5 | Cross-border transfer without safeguards | s72, s57(1)(d) | What s72 mechanism? Special PI/children's PI triggering s57? Cloud storage = transfer? | No enforcement yet — IR guidance note expected |
| 6 | Prior authorization not obtained | s57, s58, s59 | Unique ID cross-linking? Criminal data for third parties? Credit reporting? Special PI transfer? | s59 makes failure an offence (R10M / 12 months) |
| 7 | IO not registered | s55(2), s56 | IO on eServices portal? Deputy IO designated in writing? IO in SA? | 2% private body compliance rate |
| 8 | Compliance framework absent or stale | s8, Regs 2025 | Framework exists? Last reviewed? Covers all 8 conditions? PI impact assessment done? | DOJ&CD + Dis-Chem ordered to implement |
| 9 | Special PI without authorization | s26–s33, s27 | Which category? Which s27 exception? Third-party processing or cross-border = s57? | IR Guidance Note issued |
| 10 | Children's PI without competent person consent | s34–s35 | Age verified? Competent person consent? Best interests? | DBE matric results (R5M) |
| 11 | Automated decision-making without safeguards | s71 | Solely automated decisions with legal effects? Human review mechanism? Data subject notified? | IR flagged AI as 2025/26 focus |
| 12 | PAIA manual missing | PAIA s14/s51 | Manual exists? Publicly available? IO details included? Annual report submitted? | OUTA, SSA, 17 law firms assessed |

### Flag-to-topic mapping

| Flag # | Topic overlay |
|---|---|
| 1, 2, 7, 8, 12 | enforcement-and-compliance.md |
| 3 | operator-agreements.md |
| 4 | lawful-processing.md |
| 5, 6, 9, 10 | cross-border-and-special-categories.md, impact-assessment.md |
| 11 | lawful-processing.md |

---

## 7. Eval Case Outlines

### `dpa-review` — 4 cases

**Case 1: Operator agreement missing s21 essentials**
- Input: SaaS company receives vendor's GDPR-modeled DPA using controller/processor terminology, referencing SCCs.
- Expected flags: Terminology mismatch, no s21 compliance, s72 assessment needed, s19 safeguards reference missing.
- Expected statutes: POPIA s21, s19, s72
- Must NOT contain: "data controller", "data processor", "GDPR Article 28", "Standard Contractual Clauses" (without adaptation note), "supervisory authority"

**Case 2: We are the operator**
- Input: BPO receives client's operator agreement with 24-hour breach notification, unlimited audit, 7-day deletion, no subprocessors without consent.
- Expected flags: Term-by-term playbook assessment, cross-border check for offshore operations.
- Expected statutes: POPIA s21, s22, s19

**Case 3: Cross-border to inadequate country**
- Input: SA fintech transferring customer data (including ID numbers) to AWS US. No binding agreement. Relying on AWS standard terms.
- Expected flags: s72 no adequacy, need binding agreement, possible s57(1)(d) prior authorization, AWS terms ≠ binding agreement.
- Expected statutes: POPIA s72, s57(1)(d), s19

**Case 4: Subprocessor chain across jurisdictions**
- Input: SA company engages operator with subprocessors in Nigeria, India, UK. 30-day notice for subprocessor changes.
- Expected flags: Per-jurisdiction s72 assessment, juristic person coverage gap for UK GDPR, layered s21 obligations.
- Expected statutes: POPIA s72, s21, s19
- Must NOT contain: "adequacy decision", "Article 46 safeguards"

### `dsar-response` — 4 cases

**Case 1: Standard access request**
- Input: Individual emails requesting all PI held. Identity verified. Data in CRM, email, HR, backup tapes.
- Expected flags: s23 access, reasonable fee, description of PI/categories/recipients/purpose, backup tape proportionality.
- Expected statutes: POPIA s23, s18
- Must NOT contain: "right to portability", "Article 15 GDPR", "45-day deadline", "free of charge"

**Case 2: Correction via WhatsApp (April 2025 regs)**
- Input: Data subject submits correction request via WhatsApp. Company has no WhatsApp process.
- Expected flags: Multi-channel required per April 2025 regs, 30-day response, written notification of action, no process ≠ excuse.
- Expected statutes: POPIA s24, Regs 2025 Reg 3

**Case 3: Telephonic objection to direct marketing**
- Input: Data subject phones to object to marketing SMS. No recording mechanism.
- Expected flags: Telephonic objection valid per April 2025 regs, must record and make available free, inform of right to object at collection.
- Expected statutes: POPIA s11(3), s69, Regs 2025 Reg 2
- Must NOT contain: "right to erasure", "Article 21 GDPR", opt-out framed as sufficient

**Case 4: Access request with privilege exemption**
- Input: Former employee requests all PI including investigation notes, disciplinary records, performance reviews marked "legal advice."
- Expected flags: s23 applies, privilege analysis (legal vs commercial capacity for investigation notes), performance reviews generally not privileged.
- Expected statutes: POPIA s23, s15, s18
- Must NOT contain: "FOIA", "subject access request", "DSAR" as legal term

### `pia-generation` — 3 cases

**Case 1: Biometric data — facial recognition**
- Input: Facial recognition for office access. 200 employees, Gauteng.
- Expected flags: Special PI (biometrics s26), s57 prior authorization if cross-linking, s27 employment exception analysis, s19 biometric security.
- Expected statutes: POPIA s26, s27, s33, s57, s19
- Must NOT contain: "DPIA", "legitimate interest balancing test", "Data Protection Officer"

**Case 2: Children's data — educational platform**
- Input: EdTech for SA schools. Names, grades, learning progress, behavioral analytics, ages 10-17. Azure SA hosting.
- Expected flags: Children's PI (s34-35), competent person consent, s72 + s57(1)(d) if Azure regions outside SA, behavioral analytics = possible s57(1)(a) cross-linking, DBE precedent.
- Expected statutes: POPIA s34, s35, s57, s72, s19

**Case 3: Alternative credit scoring**
- Input: Fintech using mobile/social/purchase data for credit scores shared with lenders.
- Expected flags: s57(1)(c) credit reporting, s57(1)(a) cross-linking, s71 automated decisions, special PI risk from social media, s69 if scores trigger offers.
- Expected statutes: POPIA s57(1)(a)(c), s71, s26, s69
- Must NOT contain: "FCRA", "Article 22 GDPR"

### `use-case-triage` — 4 cases

**Case 1: PROCEED — de-identified analytics**
- Input: Internal dashboard with aggregated, de-identified sales data by region.
- Expected classification: PROCEED — s6(1)(b) de-identified data excluded if cannot be re-identified.
- Expected statutes: POPIA s6(1)(b)

**Case 2: PRIOR AUTHORIZATION REQUIRED — loyalty cross-linking**
- Input: Retail group linking loyalty cards across 5 subsidiaries for unified profiles + personalized marketing.
- Expected classification: PRIOR AUTHORIZATION REQUIRED — s57(1)(a) unique identifiers, s69 direct marketing.
- Expected statutes: POPIA s57(1)(a), s69
- Must NOT contain: "DPIA mandatory", "Article 35 high-risk list"

**Case 3: STOP — conflicts with privacy notice**
- Input: Privacy notice says "we do not share PI with third parties for marketing." Marketing wants to share email list with co-marketing partner.
- Expected classification: STOP — direct conflict with published commitments. s69 + s18.
- Expected statutes: POPIA s69, s18, s11

**Case 4: PIA REQUIRED — employee wellness with health data**
- Input: Voluntary wellness program tracking health metrics via wearable. Third-party US platform.
- Expected classification: PIA REQUIRED — special PI (health s26), s72 US transfer, voluntary ≠ consent in employment, s57(1)(d) prior authorization possible.
- Expected statutes: POPIA s26, s27, s72, s57(1)(d), s19

### `policy-monitor` — 3 cases

**Case 1: Undisclosed subprocessor (sweep)**
- Input: Sweep finds approved DPA for Mixpanel not in privacy notice third-party section.
- Expected gap: REQUIRED — misrepresents current practice. Add to disclosures. Check s72 for hosting location.
- Expected statutes: POPIA s18, s21, s72

**Case 2: WhatsApp Business channel (direct query)**
- Input: "We want to use WhatsApp Business API for order updates and promotional messages."
- Expected gap: REQUIRED for promotional (s69 consent needed). ADVISABLE for order updates (disclose WhatsApp as channel). April 2025 regs apply.
- Expected statutes: POPIA s69, s18, Regs 2025 Reg 6

**Case 3: Retention gap (sweep)**
- Input: PIA approved 3-year retention for support tickets. Privacy notice says "only as long as necessary" with no period.
- Expected gap: ADVISABLE — not technically wrong but lacks specificity. Recommend retention schedule reference.
- Expected statutes: POPIA s14, s18

### `reg-gap-analysis` — 3 cases

**Case 1: April 2025 POPIA regulation amendments**
- Input: "POPIA regulations just amended — gap analysis."
- Expected gaps: Multi-channel objection, recorded telemarketing, 30-day correction response, expanded complaint standing, IO duty updates, instalment fines.
- Expected statutes: POPIA Regs 2025

**Case 2: Cybercrimes Act s54 commencement**
- Input: "We're an ESP. What do we need when Cybercrimes Act reporting kicks in?"
- Expected gaps: Parallel 72-hour SAPS reporting, incident response plan update, evidence preservation procedures.
- Expected statutes: Cybercrimes Act s54, POPIA s22

**Case 3: IR cross-border transfer guidance note**
- Input: "IR published cross-border guidance — assess impact."
- Expected gaps: Adequacy assessment methodology, binding agreement requirements, s72 documentation, transfer register.
- Expected statutes: POPIA s72, s57(1)(d)

### Validation rules (all cases)

- No GDPR terminology as legal terms: "data controller", "data processor", "supervisory authority", "DPO", "DPIA", "SCCs", "Article X"
- POPIA terminology used consistently: "responsible party", "operator", "Information Regulator", "Information Officer", "prior authorization", "conditions for lawful processing"
- No US privacy law references: "CCPA", "CPRA", "HIPAA", "FERPA", "COPPA", "FTC"
- April 2025 regulation amendments reflected where applicable
- "As soon as reasonably possible" for breach notification (not "72 hours" — that's GDPR/Cybercrimes Act, not POPIA)

### Expert review gate

Before release, an SA privacy practitioner must review:
- Statute YAML values against current POPIA text and April 2025 amended regulations
- Topic overlay procedures against current POPIA conditions and IR guidance notes
- High-risk flag table against current IR enforcement patterns and priorities
- Practice profile template for completeness and correct SA privilege formulation
- Eval case expected outputs for legal accuracy

---

## 8. Source Provenance Log

| Item | Source | Tag |
|---|---|---|
| POPIA statute text and structure | Perplexity search (popia.co.za, gov.za, DLA Piper, CMS Law) | [Perplexity — verify] |
| April 2025 POPIA regulation amendments | Perplexity search (Baker McKenzie, Bowmans, ITLawCo, Power Law Africa) | [Perplexity — verify] |
| IR enforcement actions and fines | Perplexity search (SEESA Nov 2025 briefing, ITWeb, Bowmans, Juta, Baker McKenzie) | [Perplexity — verify] |
| IO registration requirements | Perplexity search (inforegulator.org.za, Bowmans, Michalsons) | [Perplexity — verify] |
| s57 prior authorization requirements | Perplexity search (popia.co.za, inforegulator.org.za, Bowmans, SEESA) | [Perplexity — verify] |
| s72 cross-border transfer framework | Perplexity search (popia.co.za, CMS Law, Scielo) | [Perplexity — verify] |
| IR 2025/26 strategic plan | Perplexity search (inforegulator.org.za strategic plan PDF) | [Perplexity — verify] |
| Cybercrimes Act 19 of 2020 | Perplexity search (gov.za, Scielo, Baker McKenzie, LSSA) | [Perplexity — verify] |
| Skill divergence assessments | Model analysis of skill SKILL.md files + Perplexity research on SA equivalents | [model knowledge — verify] |
| Employment-legal reference implementation | Direct read of `jurisdictions/za/employment-legal/` files | [codebase — verified] |
| All decisions | User confirmed during interview | [user confirmed] |

---

## Implementation Sequence

Following the same task structure as the employment-legal build:

1. Statute YAML files (extend `popia.yaml` + new `cybercrimes.yaml` + new `paia.yaml`)
2. Topic overlay markdown files (6 files in `jurisdictions/za/privacy-legal/topics/`)
3. Skill router (`jurisdictions/za/privacy-legal/router.md`)
4. Practice profile template (`jurisdictions/za/privacy-legal/practice-profile-template.md`)
5. Cold-start interview ZA fork (add to `privacy-legal/skills/cold-start-interview/SKILL.md`)
6. Validation scripts (extend existing validators for privacy-legal)
7. Scenario eval cases (21 cases in `jurisdictions/za/evals/privacy-legal/`)
8. Final validation run
