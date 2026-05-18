# ZA Privacy-Legal Overlay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the South African overlay for the privacy-legal plugin following the same additive pattern as the employment-legal and commercial-legal overlays.

**Architecture:** Additive overlays in `jurisdictions/za/privacy-legal/` — statute YAML files (shared), topic overlay markdown files, skill router, ZA practice profile template, cold-start interview fork, validation, and eval cases. No upstream skill modifications except cold-start-interview. See ADR-001 (`project/decisions/001-sa-overlay-architecture.md`).

**Spec:** `docs/superpowers/specs/2026-05-18-za-privacy-legal-expansion.md` — read this before starting any task. It contains the full legal content for each file.

**Reference implementation:** `jurisdictions/za/employment-legal/` (phase 1) and `jurisdictions/za/commercial-legal/` (phase 2).

---

## File Map

### New files

| File | Responsibility |
|---|---|
| `jurisdictions/za/statutes/cybercrimes.yaml` | Cybercrimes Act 19 of 2020 statute entries |
| `jurisdictions/za/statutes/paia.yaml` | Promotion of Access to Information Act 2 of 2000 statute entries |
| `jurisdictions/za/privacy-legal/router.md` | Maps 7 in-scope skills to topic + statute files |
| `jurisdictions/za/privacy-legal/practice-profile-template.md` | ZA practice profile template for SA privacy practitioners |
| `jurisdictions/za/privacy-legal/topics/data-subject-rights.md` | POPIA s23/s24/s11(3), April 2025 regs, exemptions |
| `jurisdictions/za/privacy-legal/topics/operator-agreements.md` | POPIA s21, responsible party/operator, s72 cross-border |
| `jurisdictions/za/privacy-legal/topics/impact-assessment.md` | POPIA s57 prior authorization, 8 conditions, special PI, children's PI |
| `jurisdictions/za/privacy-legal/topics/lawful-processing.md` | 8 conditions framework, s11 bases, s69 direct marketing |
| `jurisdictions/za/privacy-legal/topics/enforcement-and-compliance.md` | IR powers, fines, eServices portal, IO registration, PAIA manual |
| `jurisdictions/za/privacy-legal/topics/cross-border-and-special-categories.md` | s72 transfers, s26-33 special PI, s34-35 children's PI, s57(1)(d) |
| `jurisdictions/za/evals/privacy-legal/dpa-review/case-01-gdpr-modeled-dpa.yaml` | Eval: GDPR-styled DPA reviewed under POPIA |
| `jurisdictions/za/evals/privacy-legal/dpa-review/case-02-we-are-operator.yaml` | Eval: BPO reviews client operator agreement |
| `jurisdictions/za/evals/privacy-legal/dpa-review/case-03-cross-border-inadequate.yaml` | Eval: Transfer to US without binding agreement |
| `jurisdictions/za/evals/privacy-legal/dpa-review/case-04-subprocessor-chain.yaml` | Eval: Multi-jurisdiction subprocessor chain |
| `jurisdictions/za/evals/privacy-legal/dsar-response/case-01-standard-access.yaml` | Eval: Standard access request under s23 |
| `jurisdictions/za/evals/privacy-legal/dsar-response/case-02-correction-whatsapp.yaml` | Eval: Correction via WhatsApp under April 2025 regs |
| `jurisdictions/za/evals/privacy-legal/dsar-response/case-03-telephonic-objection.yaml` | Eval: Telephonic objection to direct marketing |
| `jurisdictions/za/evals/privacy-legal/dsar-response/case-04-access-with-privilege.yaml` | Eval: Access request with privilege exemption analysis |
| `jurisdictions/za/evals/privacy-legal/pia-generation/case-01-biometric-facial.yaml` | Eval: Facial recognition for office access |
| `jurisdictions/za/evals/privacy-legal/pia-generation/case-02-childrens-edtech.yaml` | Eval: EdTech platform collecting children's PI |
| `jurisdictions/za/evals/privacy-legal/pia-generation/case-03-alternative-credit.yaml` | Eval: Alternative credit scoring with automated decisions |
| `jurisdictions/za/evals/privacy-legal/use-case-triage/case-01-deidentified-analytics.yaml` | Eval: De-identified analytics (PROCEED) |
| `jurisdictions/za/evals/privacy-legal/use-case-triage/case-02-loyalty-crosslinking.yaml` | Eval: Loyalty card cross-linking (PRIOR AUTH) |
| `jurisdictions/za/evals/privacy-legal/use-case-triage/case-03-policy-conflict.yaml` | Eval: Processing conflicts with privacy notice (STOP) |
| `jurisdictions/za/evals/privacy-legal/use-case-triage/case-04-wellness-health.yaml` | Eval: Employee wellness with health data (PIA REQUIRED) |
| `jurisdictions/za/evals/privacy-legal/policy-monitor/case-01-undisclosed-subprocessor.yaml` | Eval: Sweep finds undisclosed Mixpanel |
| `jurisdictions/za/evals/privacy-legal/policy-monitor/case-02-whatsapp-business.yaml` | Eval: New WhatsApp Business channel |
| `jurisdictions/za/evals/privacy-legal/policy-monitor/case-03-retention-gap.yaml` | Eval: Retention period gap in privacy notice |
| `jurisdictions/za/evals/privacy-legal/reg-gap-analysis/case-01-april-2025-regs.yaml` | Eval: April 2025 POPIA regulation amendments |
| `jurisdictions/za/evals/privacy-legal/reg-gap-analysis/case-02-cybercrimes-s54.yaml` | Eval: Cybercrimes Act ESP reporting |
| `jurisdictions/za/evals/privacy-legal/reg-gap-analysis/case-03-crossborder-guidance.yaml` | Eval: IR cross-border transfer guidance note |

### Modified files

| File | Change |
|---|---|
| `jurisdictions/za/statutes/popia.yaml` | Add 17 new sections (conditions, rights, special PI, children's PI, IO, etc.) |
| `scripts/validate-za-router.py` | Add privacy-legal to `PRACTICE_AREAS` list |
| `scripts/validate-za-templates.py` | Add privacy-legal to `TEMPLATE_CONFIG` dict |
| `privacy-legal/skills/cold-start-interview/SKILL.md` | Add ZA fork after Part 0 |

---

## Task 1: Extend `popia.yaml` with 17 new sections

**Files:**
- Modify: `jurisdictions/za/statutes/popia.yaml`

**Context:** The existing file has 6 sections from the commercial-legal expansion. Privacy-legal needs the full POPIA machinery. Read spec Section 1 for the complete list.

- [ ] **Step 1: Read the existing file**

Read `jurisdictions/za/statutes/popia.yaml` to confirm the 6 existing sections and the file's header format.

- [ ] **Step 2: Add 17 new sections**

Append the following sections after the existing `direct_marketing_restrictions` entry. Follow the exact YAML schema from the existing file — every section needs `ref`, `value`, `effective_from`, `effective_until`, `effect`, and optional `note`.

Sections to add (see spec Section 1 for full details):

```yaml
  conditions_lawful_processing:
    ref: "POPIA s8-s12"
    value: 8
    unit: "conditions"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Personal information must be processed in accordance with 8 conditions: accountability, processing limitation, purpose specification, further processing limitation, information quality, openness, security safeguards, data subject participation."

  consent:
    ref: "POPIA s11(1)(a)"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Personal information may only be processed if the data subject consents to the processing."
    note: "Consent is one of several lawful bases under s11. Unlike GDPR, POPIA does not elevate consent above other bases — legitimate interest (s11(1)(f)) is equally valid."

  purpose_specification:
    ref: "POPIA s13"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Personal information must be collected for a specific, explicitly defined and lawful purpose related to a function or activity of the responsible party."

  data_retention:
    ref: "POPIA s14"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Records of personal information must not be retained any longer than is necessary for achieving the purpose for which the information was collected or subsequently processed, unless retention is required or authorised by law, reasonably necessary for a lawful purpose, or the responsible party requires it for contractual purposes."

  openness_notification:
    ref: "POPIA s18"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A responsible party must, when collecting personal information, take reasonably practicable steps to ensure the data subject is aware of: the information being collected, the name and address of the responsible party, the purpose of collection, whether the supply is voluntary or mandatory, and the consequences of failure to provide the information."

  data_subject_access:
    ref: "POPIA s23"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A data subject may request a responsible party to confirm whether it holds personal information about them and request access to that information. The responsible party may charge a reasonable fee."
    note: "Unlike GDPR Article 15 where access is generally free, POPIA permits a reasonable fee for access requests."

  data_subject_correction_deletion:
    ref: "POPIA s24"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A data subject may request correction or deletion of personal information that is inaccurate, irrelevant, excessive, out of date, incomplete, misleading, or obtained unlawfully."
    note: "April 2025 amended regulations require the responsible party to notify the data subject of action taken within 30 days and allow multi-channel requests (WhatsApp, SMS, email, telephonic with recording)."

  data_subject_objection:
    ref: "POPIA s11(3)(a)"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A data subject may object to the processing of personal information on reasonable grounds relating to his, her or its particular situation, unless legislation provides for such processing."
    note: "April 2025 amended regulations expand objection channels to include WhatsApp, SMS, email, and telephonic (must be recorded). Responsible party must inform data subject of right to object at collection."

  special_personal_information:
    ref: "POPIA s26-s33"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Processing of special personal information is prohibited unless a s27 exception applies. Special PI includes: religious or philosophical beliefs, race or ethnic origin, trade union membership, political persuasion, health, sex life, biometric information, and criminal behaviour."

  children_personal_information:
    ref: "POPIA s34-s35"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Processing of personal information of a child (under 18) is prohibited unless a competent person (parent or guardian) has consented on behalf of the child, or unless a s35 exception applies."
    note: "Child is defined as a natural person under the age of 18 who is not legally competent without the assistance of a competent person."

  prior_authorization:
    ref: "POPIA s57"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A responsible party must obtain prior authorisation from the Information Regulator before processing if it plans to: (a) process unique identifiers for a purpose other than collection and with aim of cross-linking across responsible parties; (b) process criminal behaviour data on behalf of third parties; (c) process information for credit reporting; (d) transfer special PI or children's PI to a foreign country without adequate protection."
    note: "Prior authorisation is required only once per processing type (s57(4)). Not required if a code of conduct has been issued for the sector (s57(3)). Failure to notify is an offence — fine up to R10M or 12 months imprisonment (s59)."

  information_officer_registration:
    ref: "POPIA s55-s56"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Every responsible party must register an Information Officer with the Information Regulator. The IO may only take up duties after registration (s55(2)). The IO has duties under both POPIA and PAIA including: encouraging compliance, dealing with requests, working with the IR on investigations, ensuring a compliance framework is developed and maintained."
    note: "CEO is the default IO for private bodies. Deputy IOs may be designated under s56 and must also be registered. IO must be based in South Africa per IR guidance. Not registering is not a criminal offence but the head of the organisation is personally liable."

  automated_decision_making:
    ref: "POPIA s71"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A data subject may not be subject to a decision which results in legal consequences for him, her or it, or which affects him, her or it to a substantial degree, which is based solely on the basis of the automated processing of personal information intended to provide a profile of such person."
    note: "Information Regulator flagged AI and automated decision-making as a focus area for 2025/26."

  unique_identifiers:
    ref: "POPIA s57(1)(a)"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A unique identifier is any identifier assigned to a data subject and used by a responsible party for purposes of its operations that uniquely identifies the data subject. Processing unique identifiers for a purpose other than intended at collection, with aim of linking across responsible parties, requires prior authorisation."

  direct_marketing_2025_regs:
    ref: "POPIA Regs 2025 Reg 6"
    value: true
    effective_from: "2025-04-17"
    effective_until: null
    effect: "Consent for direct marketing through unsolicited electronic communication must be obtained on a form substantially similar to Form 4, free of charge and reasonably accessible including by email, telephone, SMS, WhatsApp, fax, or automated calling machine. Opt-out does not constitute consent. Telephonic or automated consent requests must be electronically recorded and made available to the data subject on request."
    note: "These regulations came into immediate effect on 17 April 2025. The IR is actively pursuing test cases on whether live telemarketing constitutes 'electronic communication' under s69."

  complaint_procedures_2025_regs:
    ref: "POPIA Regs 2025 Reg 7"
    value: true
    effective_from: "2025-04-17"
    effective_until: null
    effect: "Complaints may be lodged by: the data subject, a person acting on behalf of the data subject, any person with sufficient personal interest, a responsible party or data subject aggrieved by an adjudicator determination, or any person acting in the public interest. The Regulator must provide a reference number within 14 days of receipt."
    note: "Assistance must be provided to complainants in languages other than English. Confidentiality protections aligned with the Protected Disclosures Act."

  eservices_portal_breach_reporting:
    ref: "IR operational directive"
    value: true
    effective_from: "2025-04-01"
    effective_until: null
    effect: "All security compromise notifications must be submitted via the Information Regulator's eServices portal. Email submissions are no longer accepted for breach reporting."
    note: "Mandatory since 1 April 2025. Portal URL: https://eservices.inforegulator.org.za"
```

- [ ] **Step 3: Update `last_confirmed` date**

Change the top-level `last_confirmed` field to `"2026-05-18"`.

- [ ] **Step 4: Validate**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: `OK: jurisdictions/za/statutes/popia.yaml (23 sections)` — 6 existing + 17 new.

- [ ] **Step 5: Commit**

```bash
git add jurisdictions/za/statutes/popia.yaml
git commit -m "feat(za): extend popia.yaml with 17 privacy-legal sections"
```

---

## Task 2: Create `cybercrimes.yaml`

**Files:**
- Create: `jurisdictions/za/statutes/cybercrimes.yaml`

- [ ] **Step 1: Write the statute file**

```yaml
statute: "Cybercrimes Act 19 of 2020"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-18"
source_url: "https://www.gov.za/documents/acts/cybercrimes-act-19-2020"

sections:
  unlawful_access:
    ref: "Cybercrimes Act s2"
    value: true
    effective_from: "2021-12-01"
    effective_until: null
    effect: "Any person who unlawfully and intentionally accesses or intercepts data, a computer program, a computer data storage medium, or a computer system is guilty of an offence."

  unlawful_interception:
    ref: "Cybercrimes Act s3"
    value: true
    effective_from: "2021-12-01"
    effective_until: null
    effect: "Any person who unlawfully and intentionally intercepts data, including within a computer system, is guilty of an offence."

  unlawful_interference:
    ref: "Cybercrimes Act s5"
    value: true
    effective_from: "2021-12-01"
    effective_until: null
    effect: "Any person who unlawfully and intentionally interferes with data or a computer program is guilty of an offence."

  esp_fi_breach_reporting:
    ref: "Cybercrimes Act s54"
    value: "72 hours"
    unit: "reporting deadline"
    effective_from: null
    effective_until: null
    effect: "Electronic communications service providers and financial institutions must report to the South African Police Service within 72 hours of becoming aware that their systems have been involved in the commission of an offence under this Act."
    note: "NOT YET IN FORCE — will commence on a date to be proclaimed by the President. When in force, creates a parallel reporting obligation alongside POPIA s22 notification to the Information Regulator."

  penalties_serious:
    ref: "Cybercrimes Act s18"
    value: 15
    unit: "years maximum imprisonment"
    effective_from: "2021-12-01"
    effective_until: null
    effect: "Persons found guilty of cybercrime offences under this Act face fines and prison sentences of up to 15 years."

  evidence_preservation:
    ref: "Cybercrimes Act s41"
    value: true
    effective_from: "2021-12-01"
    effective_until: null
    effect: "A magistrate or judge may direct any person to preserve data that may be relevant to an investigation for a specified period."
```

- [ ] **Step 2: Validate**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: `OK: jurisdictions/za/statutes/cybercrimes.yaml (6 sections)`

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/statutes/cybercrimes.yaml
git commit -m "feat(za): add Cybercrimes Act statute file for privacy-legal"
```

---

## Task 3: Create `paia.yaml`

**Files:**
- Create: `jurisdictions/za/statutes/paia.yaml`

- [ ] **Step 1: Write the statute file**

```yaml
statute: "Promotion of Access to Information Act 2 of 2000"
authority: "Information Regulator"
last_confirmed: "2026-05-18"
source_url: "https://www.gov.za/documents/promotion-access-information-act"

sections:
  paia_manual_private_body:
    ref: "PAIA s51"
    value: true
    effective_from: "2001-03-09"
    effective_until: null
    effect: "The head of a private body must compile a manual containing: a description of its structure, contact details of the information officer, a description of the subjects on which records are available, and the categories of records held."
    note: "PAIA manual compliance rates are extremely low — only 2% of private bodies submitted annual reports in 2023/24. The Information Regulator is actively assessing compliance."

  paia_manual_public_body:
    ref: "PAIA s14"
    value: true
    effective_from: "2001-03-09"
    effective_until: null
    effect: "The information officer of a public body must compile a manual containing: a description of its structure, functions, contact details, guidance on requesting information, and a description of categories of records held."

  information_officer_duties_paia:
    ref: "PAIA s17"
    value: true
    effective_from: "2001-03-09"
    effective_until: null
    effect: "The information officer of a public body may designate deputy information officers to whom powers and duties are delegated. This extends to private bodies via POPIA s56."
    note: "The IO registered under POPIA has dual duties under both POPIA and PAIA. April 2025 POPIA regulation amendments removed the POPIA Reg 4 duty to maintain a PAIA manual, but the obligation remains under PAIA itself."

  annual_reporting:
    ref: "PAIA s32, s83(4)"
    value: true
    effective_from: "2001-03-09"
    effective_until: null
    effect: "Both public and private bodies must submit annual PAIA reports to the Information Regulator showing how they handle requests for information."
    note: "Compliance is extremely low: 33% of public bodies and less than 2% of private bodies submitted reports in 2023/24. The IR is increasing monitoring and enforcement."
```

- [ ] **Step 2: Validate**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: `OK: jurisdictions/za/statutes/paia.yaml (4 sections)`

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/statutes/paia.yaml
git commit -m "feat(za): add PAIA statute file for privacy-legal"
```

---

## Task 4: Create 6 topic overlay files

**Files:**
- Create: `jurisdictions/za/privacy-legal/topics/data-subject-rights.md`
- Create: `jurisdictions/za/privacy-legal/topics/operator-agreements.md`
- Create: `jurisdictions/za/privacy-legal/topics/impact-assessment.md`
- Create: `jurisdictions/za/privacy-legal/topics/lawful-processing.md`
- Create: `jurisdictions/za/privacy-legal/topics/enforcement-and-compliance.md`
- Create: `jurisdictions/za/privacy-legal/topics/cross-border-and-special-categories.md`

**Context:** Read the spec Section 3 (Topic Overlay Map) and Section 6 (High-Risk Flag Table) for content areas. Read `jurisdictions/za/employment-legal/topics/dismissal.md` for the exact format pattern: heading structure, terminology table, statutory framework section, procedural checklists, high-risk flag callouts, and table formats.

Each topic overlay must follow this structure:

```markdown
# [Topic Title] — South African Framework

This overlay covers [scope]. It is loaded by [skill list] when jurisdiction = ZA.

**Terminology requirement:** When jurisdiction = ZA, use POPIA terminology exclusively.

| Do NOT use (GDPR/US) | Use instead (POPIA) |
|---|---|
| data controller | responsible party |
| data processor | operator |
| [etc.] | [etc.] |

---

## 1. Statutory framework
[Key acts, sections, consequences]

## 2. [Substantive content sections]
[Checklists, tables, procedures]

## 3. High-risk flags
[Flag table with: flag name, why high-risk, what to check, statute ref]
```

Each file should be approximately 10-18KB following this structure. The legal content for each topic is specified in the decision spec:
- **data-subject-rights.md** — Spec Section 3 row 1 + Spec Section 6 flags 1-4 (DSAR-related)
- **operator-agreements.md** — Spec Section 3 row 2 + Spec Section 6 flag 3
- **impact-assessment.md** — Spec Section 3 row 3 + Spec Section 6 flags 6, 9, 10
- **lawful-processing.md** — Spec Section 3 row 4 + Spec Section 6 flags 4, 11
- **enforcement-and-compliance.md** — Spec Section 3 row 5 + Spec Section 6 flags 1, 2, 7, 8, 12
- **cross-border-and-special-categories.md** — Spec Section 3 row 6 + Spec Section 6 flags 5, 6, 9, 10

The POPIA-to-GDPR terminology table must appear in every topic overlay:

| Do NOT use (GDPR/US) | Use instead (POPIA) |
|---|---|
| data controller | responsible party |
| data processor | operator |
| Data Protection Officer (DPO) | Information Officer (IO) |
| supervisory authority / Data Protection Authority | Information Regulator |
| Data Protection Impact Assessment (DPIA) | prior authorisation (s57) / personal information impact assessment |
| Standard Contractual Clauses (SCCs) | binding agreement (s72) or adapted data transfer agreement |
| data subject access request (DSAR) | request for access (s23) |
| right to portability | [no POPIA equivalent — do not reference] |
| Article [N] | [do not reference GDPR articles — cite POPIA sections] |
| CCPA / CPRA / state privacy law | [do not reference US privacy laws] |

- [ ] **Step 1: Remove `.gitkeep` and create topics directory**

```bash
rm jurisdictions/za/privacy-legal/.gitkeep
mkdir -p jurisdictions/za/privacy-legal/topics
```

- [ ] **Step 2: Write `data-subject-rights.md`**

Content areas (from spec): POPIA s23 access (reasonable fee permitted, unlike GDPR), s24 correction/deletion (30-day response per April 2025 regs, multi-channel including WhatsApp/SMS), s11(3) objection (expanded channels, recorded telephonic), exemption framework (s15, s27, s37), no explicit portability right, procedural checklist for handling requests. Include the April 2025 regulation amendments as a dedicated subsection. Include a procedural checklist with steps, timelines, and channel requirements.

- [ ] **Step 3: Write `operator-agreements.md`**

Content areas: POPIA s21 operator agreements (not "DPA"), responsible party vs operator terminology, s19 security safeguards obligation flow-down to operator, s72 cross-border transfer (no adequacy list, adapted SCCs), direct marketing restrictions on operators, standard clause positions for SA, term-by-term review framework mapped to POPIA. Include a comparison table showing GDPR Art 28 DPA terms vs POPIA s21 operator agreement requirements.

- [ ] **Step 4: Write `impact-assessment.md`**

Content areas: POPIA s57 prior authorization (replaces GDPR DPIA), triggers (unique identifier cross-linking, special PI/children's PI transfer to inadequate countries, credit reporting, criminal behavior on behalf of third parties), 8 conditions as PIA framework, s26-33 special PI categories, s34-35 children's PI, IR submission process for prior authorization (4-week response, 13-week investigation), PIA vs prior authorization — when each applies. Include the prior authorization trigger checklist and IR submission process.

- [ ] **Step 5: Write `lawful-processing.md`**

Content areas: POPIA's 8 conditions (accountability, purpose specification, processing limitation, further processing limitation, information quality, openness, security safeguards, data subject participation), s11 lawful bases (consent, legitimate interest, contract, legal obligation, public interest, proper performance of public law duty), comparison with GDPR Art 6 for practitioners crossing over, s69 direct marketing (opt-out ≠ consent per April 2025 regs, one-message rule for consent requests, existing customer exception s69(4), recorded telemarketing).

- [ ] **Step 6: Write `enforcement-and-compliance.md`**

Content areas: IR powers and structure, enforcement notices (process: complaint → investigation → enforcement notice → infringement notice → fine/prosecution), s107 fines (R10M max), instalment payments (April 2025 regs), eServices portal for breach reporting (mandatory since 1 April 2025), complaint procedures (expanded standing per April 2025 regs, 14-day acknowledgment, public interest complaints), IO registration and duties (s55-56, eServices portal, dual POPIA/PAIA mandate), compliance framework obligation (s8 accountability, continuously improved per amended Reg 4), Cybercrimes Act s54 parallel SAPS reporting, PAIA manual requirements. Include IR enforcement action table (DOJ&CD R5M, Dis-Chem, Lancet R100K, FT Rams R100K, Blouberg R500K, DBE R5M) as precedent reference.

- [ ] **Step 7: Write `cross-border-and-special-categories.md`**

Content areas: s72 cross-border transfer restrictions (5 permitted grounds: adequate law/BCRs/binding agreement, consent, contractual necessity, interest of data subject, benefit of data subject), no adequacy list published by IR, practical mechanisms (adapted GDPR SCCs as binding agreements, BCRs within corporate groups, consent), National Data and Cloud Policy (2024) data sovereignty provisions, s26-33 special PI (race, health, religion, biometrics, trade union, political, sex life, criminal behaviour — each with its own authorisation section s28-33), s34-35 children's PI (under 18, competent person consent), s57 prior authorization for special PI/children's PI transfers to inadequate countries. Note unique SA consideration: POPIA applies to juristic persons — most foreign laws don't, creating an adequacy gap.

- [ ] **Step 8: Verify all topic files exist**

```bash
ls -la jurisdictions/za/privacy-legal/topics/
```

Expected: 6 `.md` files.

- [ ] **Step 9: Commit**

```bash
git add jurisdictions/za/privacy-legal/
git commit -m "feat(za): add 6 privacy-legal topic overlay files"
```

---

## Task 5: Create the skill router

**Files:**
- Create: `jurisdictions/za/privacy-legal/router.md`

- [ ] **Step 1: Write the router**

```markdown
# Skill Router — South African Privacy Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/privacy-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
dpa-review:
  topics: [operator-agreements, cross-border-and-special-categories, lawful-processing]
  statutes: [popia, cybercrimes]

dsar-response:
  topics: [data-subject-rights, enforcement-and-compliance]
  statutes: [popia, paia]

pia-generation:
  topics: [impact-assessment, lawful-processing, cross-border-and-special-categories]
  statutes: [popia, cybercrimes]

use-case-triage:
  topics: [impact-assessment, lawful-processing, cross-border-and-special-categories]
  statutes: [popia]

policy-monitor:
  topics: [data-subject-rights, operator-agreements, lawful-processing, enforcement-and-compliance]
  statutes: [popia]

reg-gap-analysis:
  topics: [impact-assessment, lawful-processing, enforcement-and-compliance]
  statutes: [popia, cybercrimes, paia]

cold-start-interview:
  topics: []
  statutes: [popia, cybercrimes, paia]
```
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/privacy-legal/router.md
git commit -m "feat(za): add privacy-legal skill router"
```

---

## Task 6: Create the practice profile template

**Files:**
- Create: `jurisdictions/za/privacy-legal/practice-profile-template.md`

**Context:** Read spec Section 4 for the full template design. Read `jurisdictions/za/employment-legal/practice-profile-template.md` for the exact format (462 lines). The privacy-legal ZA template should follow the same structure.

The template must include, in order:

1. **Config location comment** — same as employment-legal ZA but referencing privacy-legal paths. Include the `JURISDICTION OVERLAY` instruction pointing to `jurisdictions/za/privacy-legal/router.md`.
2. **Title and setup prompt** — `# Privacy Practice Profile — South Africa`
3. **`## Who we are`** — responsible party/operator orientation, privacy team, DPO equivalent (IO), data categories. References `company-profile.md` for shared fields.
4. **`## Who's using this`** — Role picker with SA options (Admitted attorney or advocate under Legal Practice Act 28 of 2014 | Non-lawyer with attorney access | Non-lawyer without attorney access).
5. **Quiet mode** — carried from US template unchanged.
6. **`## Available integrations`** — Document storage, Slack, Scheduled tasks, Information Regulator eServices portal.
7. **`## Information Officer`** — IO name, registration status (eServices portal), deputy IO, dual duties (POPIA + PAIA). NEW section.
8. **`## POPIA compliance framework`** — Framework status, last review date, continuous improvement (April 2025 regs), PI impact assessment status. NEW section.
9. **`## Operator agreement playbook`** — "When we are the operator" / "When we are the responsible party" tables with POPIA s21 terms. Replaces US "DPA playbook."
10. **`## Privacy notice commitments`** — Data categories, purposes, retention, third parties, data subject rights. Mapped to POPIA s18.
11. **`## PIA house style`** — Trigger (s57 prior authorization + internal policy), format, depth, sign-off (includes IR submission for prior authorization cases).
12. **`## Data subject request process`** — s23 access (reasonable fee), s24 correction (30-day), s11(3) objection (multi-channel). April 2025 regs. Replaces US "DSAR process."
13. **`## Cross-border transfers`** — s72 framework, mechanisms, data location register. NEW section.
14. **`## Breach response`** — s22 notification, eServices portal, Cybercrimes Act s54 SAPS reporting. NEW section.
15. **`## Direct marketing compliance`** — s69, April 2025 regs, existing customer exception, one-message rule. NEW section.
16. **`## Escalation`** — IR, SAPS, High Court, industry bodies. SA-specific.
17. **`## Seed documents`** — Privacy notice, operator agreement template, reference PIA, IO registration, breach plan, compliance framework.
18. **`## Outputs`** — SA privilege header formulation (not US "ATTORNEY WORK PRODUCT"). Include privacy-specific POPIA s99 note about IR investigation powers. Non-lawyer output mode.
19. **Reviewer note format, decision tree, dashboard** — carried from US template unchanged.
20. **Decision posture, shared guardrails, citation hygiene, verification log** — carried from US template, adapt examples to POPIA cites.
21. **Scaffolding not blinders, ad-hoc questions, proportionality** — carried unchanged.
22. **Jurisdiction recognition** — carried unchanged (this IS the ZA template, but the section handles edge cases).
23. **Retrieved-content trust, large input/output** — carried unchanged.
24. **`## Matter workspaces`** — carried with privacy-legal-specific context.

- [ ] **Step 1: Write the complete practice profile template**

Write the full file following the structure above. Use `[PLACEHOLDER]` markers for all user-configurable fields. The file should be approximately 40-50KB.

- [ ] **Step 2: Verify SA-specific terms are present**

```bash
grep -c "responsible party\|operator\|Information Regulator\|POPIA\|admitted attorney\|Information Officer" jurisdictions/za/privacy-legal/practice-profile-template.md
```

Expected: 20+ matches.

- [ ] **Step 3: Verify no US-specific terms leak**

```bash
grep -n "data controller\|data processor\|CCPA\|HIPAA\|FERPA\|COPPA\|FMLA\|FLSA\|EEOC\|UCC\|FRCP" jurisdictions/za/privacy-legal/practice-profile-template.md || echo "PASS: no US terms found"
```

Expected: Only hits inside the privilege caveat section (which explains why US work-product doctrine doesn't apply). Zero hits outside that section.

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/privacy-legal/practice-profile-template.md
git commit -m "feat(za): add privacy-legal ZA practice profile template"
```

---

## Task 7: Add cold-start interview ZA fork

**Files:**
- Modify: `privacy-legal/skills/cold-start-interview/SKILL.md`

**Context:** Read the existing ZA fork in `employment-legal/skills/cold-start-interview/SKILL.md` lines 182-280 for the exact pattern. The fork goes after Part 0, checks company profile jurisdiction, and branches to SA-specific questions.

- [ ] **Step 1: Read the current cold-start SKILL.md**

Read `privacy-legal/skills/cold-start-interview/SKILL.md` to find where Part 0 ends and Parts 1+ begin. The fork goes between Part 0 and Part 1.

- [ ] **Step 2: Add the ZA fork section**

Insert after the Part 0 section (after the integration check and before the US-specific interview parts). The fork section should follow this exact structure:

```markdown
### Jurisdiction check — South African overlay

After writing the Part 0 sections, check the company profile for jurisdiction:

- Read `~/.claude/plugins/config/claude-for-legal/company-profile.md` → `Primary jurisdiction`
- If the primary jurisdiction is **South Africa** (or ZA, or the user's company is SA-based based on the company profile answers):

**Fork to the SA interview path.** The rest of this interview (Parts 1-3) uses SA-specific questions. The output writes to the ZA practice profile template at `${CLAUDE_PLUGIN_ROOT}/../../../jurisdictions/za/privacy-legal/practice-profile-template.md` instead of the US template at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`.

If the primary jurisdiction is NOT South Africa, continue with the US interview path below (Parts 1-3 as written).

---

#### SA Part 1: Privacy practice configuration (3-5 min)

> POPIA is national — unlike US state privacy laws, there are no per-state variations. But there are several dimensions that shape how POPIA applies to your organisation: your responsible party/operator orientation, your Information Officer registration status, your cross-border transfer posture, and your direct marketing approach.

**Responsible party / operator orientation:**

> 1. **Are you primarily a responsible party, an operator, or both?**
>    - Primarily responsible party (you determine the purpose and means of processing PI — typical for most businesses)
>    - Primarily operator (you process PI on a responsible party's instructions — typical for outsourced service providers, cloud platforms, BPOs)
>    - Both — we're a responsible party for our own data and operator for client data

**Information Officer:**

> 2. **Has your Information Officer been registered with the Information Regulator?**
>    - Yes — IO name: _____, Deputy IO: _____
>    - Registration in progress
>    - Not yet — we need to do this
>
> *(POPIA s55-56 requires IO registration before they can take up duties. The CEO is the default IO for private bodies.)*

**POPIA compliance framework:**

> 3. **Do you have a documented POPIA compliance framework?**
>    - Yes — last reviewed: _____
>    - In development
>    - No
>
> *(POPIA s8 accountability condition. The April 2025 amended regulations require the framework to be "continuously improved.")*

**Cross-border transfers:**

> 4. **Does your organisation transfer personal information outside South Africa?**
>    - Yes — to which countries, and what mechanism? (binding agreement / BCRs / consent / adequate protection law / not sure)
>    - No — all processing stays in SA
>    - Not sure
>
> *(POPIA s72 restricts cross-border transfers. No adequacy list has been published by the Information Regulator.)*

**Breach response:**

> 5. **Two questions on breach preparedness:**
>    1. Do you have a documented breach response plan?
>    2. Are you registered on the Information Regulator's eServices portal? (Mandatory for breach reporting since 1 April 2025.)

**Direct marketing:**

> 6. **Does your organisation do direct marketing by electronic communication (email, SMS, automated calls, WhatsApp)?**
>    - Yes — we have explicit consent mechanisms in place
>    - Yes — we rely on the existing customer exception (s69(4))
>    - Yes — but our consent process may need updating
>    - No — we don't do electronic direct marketing
>
> *(April 2025 POPIA regulations: opt-out ≠ consent, telemarketing must be recorded, multi-channel objection must be offered.)*

**Prior authorization:**

> 7. **Does your organisation do any of the following (each requires prior authorization from the Information Regulator under POPIA s57)?**
>    - Process unique identifiers to cross-link data across responsible parties (for a purpose other than originally intended at collection)
>    - Process information on criminal behaviour on behalf of third parties
>    - Process personal information for credit reporting purposes
>    - Transfer special personal information or children's PI to a foreign country without adequate protection
>    - None of the above

#### SA Part 2: Seed documents

> The documents that make the biggest difference for SA privacy practice:
>
> **Must-have:**
> 1. **Privacy notice/policy** (URL or file) — I'll extract your published commitments for the policy-monitor skill. Paste the URL, share a file path, or say 'skip for now.'
>
> 2. **Operator agreement template** (file) — I'll extract your standard positions for the operator agreement playbook. If you don't have one, I'll set defaults.
>
> 3. **Reference PIA** (file) — I'll learn your house format, section structure, and risk scoring approach.

> **Nice-to-have (skip if you don't have them handy):**
> 4. **IO registration certificate** — confirms registration status and IO details
> 5. **Breach response plan** — I'll extract your response team, procedures, and timelines
> 6. **POPIA compliance framework document** — I'll extract your current framework status

If they skip seed documents: flag every section built without seed documents with `[NO SEED — defaults used; accuracy improves with your privacy notice, operator agreement template, and reference PIA]`.

#### SA Part 3: Build the configuration

Use the ZA practice profile template. Populate all sections from the interview answers and seed documents. Write to `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`, creating parent directories as needed.

After writing, show the tailored capability list:

> **Here's what I can help with in SA privacy law:**
>
> - **Operator agreement review with POPIA s21 framework** — term-by-term review, responsible party/operator analysis, cross-border transfer check. Try: `/privacy-legal:dpa-review`
> - **Data subject request handling** — s23 access, s24 correction/deletion, s11(3) objection, April 2025 multi-channel requirements. Try: `/privacy-legal:dsar-response`
> - **Privacy impact assessment** — POPIA 8-conditions framework, s57 prior authorization analysis, special PI and children's PI checks. Try: `/privacy-legal:pia-generation`
> - **Processing activity triage** — PROCEED/PIA REQUIRED/PRIOR AUTHORIZATION REQUIRED/STOP classification. Try: `/privacy-legal:use-case-triage`
> - **Privacy policy drift monitoring** — sweep outputs against POPIA notice commitments, flag gaps. Try: `/privacy-legal:policy-monitor`
> - **Regulatory gap analysis** — diff new regulations against current POPIA compliance posture. Try: `/privacy-legal:reg-gap-analysis`
```

- [ ] **Step 3: Verify the fork integrates cleanly**

Read the modified file and confirm:
- The fork section appears between Part 0 and the existing US Parts 1-3
- The `${CLAUDE_PLUGIN_ROOT}` path reference is correct
- The fork condition matches the employment-legal pattern

- [ ] **Step 4: Commit**

```bash
git add privacy-legal/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to privacy-legal cold-start interview"
```

---

## Task 8: Extend validation scripts

**Files:**
- Modify: `scripts/validate-za-router.py`
- Modify: `scripts/validate-za-templates.py`

- [ ] **Step 1: Add privacy-legal to the router validator**

In `scripts/validate-za-router.py`, add a new entry to the `PRACTICE_AREAS` list after the `commercial-legal` entry:

```python
    {
        "name": "privacy-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "privacy-legal" / "router.md",
        "skills_dir": REPO_ROOT / "privacy-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "privacy-legal" / "topics",
    },
```

- [ ] **Step 2: Add privacy-legal to the template validator**

In `scripts/validate-za-templates.py`, add a new entry to the `TEMPLATE_CONFIG` dict after the `commercial-legal` entry:

```python
    "privacy-legal": {
        "path": ROOT / "jurisdictions" / "za" / "privacy-legal" / "practice-profile-template.md",
        "required_sections": [
            "Who we are", "Who's using this", "Information Officer",
            "POPIA compliance framework", "Operator agreement playbook",
            "Privacy notice commitments", "PIA house style",
            "Data subject request process", "Cross-border transfers",
            "Breach response", "Direct marketing compliance",
            "Escalation", "Outputs", "Seed documents",
        ],
        "sa_required_terms": [
            "POPIA", "Information Regulator", "responsible party", "operator",
            "Information Officer", "admitted attorney", "s21", "s72", "s57",
        ],
        "us_forbidden": [
            (r"\bdata controller\b", "data controller"),
            (r"\bdata processor\b", "data processor"),
            (r"\bGDPR\b", "GDPR"),
            (r"\bCCPA\b", "CCPA"),
            (r"\bCPRA\b", "CPRA"),
            (r"\bHIPAA\b", "HIPAA"),
            (r"\bFERPA\b", "FERPA"),
            (r"\bCOPPA\b", "COPPA"),
            (r"\bDPIA\b", "DPIA"),
        ],
    },
```

- [ ] **Step 3: Run both validators**

```bash
python3 scripts/validate-za-router.py
python3 scripts/validate-za-templates.py
```

Expected:
- Router: `OK: [privacy-legal] 7 skills, all references resolve`
- Template: `OK: [privacy-legal] practice-profile-template.md`

- [ ] **Step 4: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for privacy-legal overlay"
```

---

## Task 9: Create 21 scenario eval cases

**Files:**
- Create: 21 `.yaml` files across 6 skill directories under `jurisdictions/za/evals/privacy-legal/`

**Context:** Read spec Section 7 for the complete eval case outlines. Each case follows the exact YAML schema from the employment-legal evals. Read `jurisdictions/za/evals/employment-legal/termination-review/case-01-misconduct-no-hearing.yaml` for the reference format.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/evals/privacy-legal/{dpa-review,dsar-response,pia-generation,use-case-triage,policy-monitor,reg-gap-analysis}
```

- [ ] **Step 2: Write the 4 `dpa-review` cases**

Write each case as a YAML file following the schema: `name`, `skill`, `input`, `expected_flags`, `expected_statutes`, `must_not_contain`, `notes`. See spec Section 7 for the exact input scenarios, expected flags, expected statutes, and must-not-contain lists.

Files:
- `case-01-gdpr-modeled-dpa.yaml` — SaaS company receives GDPR-styled DPA
- `case-02-we-are-operator.yaml` — BPO reviews client operator agreement
- `case-03-cross-border-inadequate.yaml` — SA fintech transferring to AWS US
- `case-04-subprocessor-chain.yaml` — Multi-jurisdiction subprocessor chain

- [ ] **Step 3: Write the 4 `dsar-response` cases**

Files:
- `case-01-standard-access.yaml` — Standard access request under s23
- `case-02-correction-whatsapp.yaml` — Correction via WhatsApp under April 2025 regs
- `case-03-telephonic-objection.yaml` — Telephonic objection to direct marketing
- `case-04-access-with-privilege.yaml` — Former employee access with privilege exemption

- [ ] **Step 4: Write the 3 `pia-generation` cases**

Files:
- `case-01-biometric-facial.yaml` — Facial recognition for office access
- `case-02-childrens-edtech.yaml` — EdTech platform for SA schools
- `case-03-alternative-credit.yaml` — Alternative credit scoring with automated decisions

- [ ] **Step 5: Write the 4 `use-case-triage` cases**

Files:
- `case-01-deidentified-analytics.yaml` — De-identified analytics (PROCEED)
- `case-02-loyalty-crosslinking.yaml` — Loyalty card cross-linking (PRIOR AUTH REQUIRED)
- `case-03-policy-conflict.yaml` — Processing conflicts with notice (STOP)
- `case-04-wellness-health.yaml` — Employee wellness with health data (PIA REQUIRED)

- [ ] **Step 6: Write the 3 `policy-monitor` cases**

Files:
- `case-01-undisclosed-subprocessor.yaml` — Sweep finds undisclosed Mixpanel
- `case-02-whatsapp-business.yaml` — New WhatsApp Business channel
- `case-03-retention-gap.yaml` — Retention period gap in privacy notice

- [ ] **Step 7: Write the 3 `reg-gap-analysis` cases**

Files:
- `case-01-april-2025-regs.yaml` — April 2025 POPIA regulation amendments
- `case-02-cybercrimes-s54.yaml` — Cybercrimes Act ESP reporting obligation
- `case-03-crossborder-guidance.yaml` — IR cross-border transfer guidance note

- [ ] **Step 8: Verify file count**

```bash
find jurisdictions/za/evals/privacy-legal -name "*.yaml" | wc -l
```

Expected: `21`

- [ ] **Step 9: Validate YAML syntax**

```bash
python3 -c "import yaml; import glob; [yaml.safe_load(open(f)) for f in glob.glob('jurisdictions/za/evals/privacy-legal/**/*.yaml', recursive=True)]"
```

Expected: no errors.

- [ ] **Step 10: Commit**

```bash
git add jurisdictions/za/evals/privacy-legal/
git commit -m "feat(za): add 21 privacy-legal scenario eval cases"
```

---

## Task 10: Final validation run

**Files:** None (read-only verification)

- [ ] **Step 1: Run statute validation**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: All statute files pass, including the extended `popia.yaml` (23 sections), new `cybercrimes.yaml` (6 sections), and new `paia.yaml` (4 sections).

- [ ] **Step 2: Run router validation**

```bash
python3 scripts/validate-za-router.py
```

Expected: `OK: [privacy-legal] 7 skills, all references resolve` — all topic files and statute files exist.

- [ ] **Step 3: Run template validation**

```bash
python3 scripts/validate-za-templates.py
```

Expected: `OK: [privacy-legal] practice-profile-template.md` — all required sections present, SA terms found, no US terms outside privilege caveat.

- [ ] **Step 4: Run JSON/YAML sanity check**

```bash
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('jurisdictions/za/**/*.yaml', recursive=True)]"
```

Expected: no errors.

- [ ] **Step 5: Verify no orphaned topic files**

The router validator already checks this. Confirm output has no `WARN: [privacy-legal] orphaned topic file` lines.

- [ ] **Step 6: Verify directory structure matches architecture**

```bash
find jurisdictions/za/privacy-legal -type f | sort
```

Expected output:
```
jurisdictions/za/privacy-legal/practice-profile-template.md
jurisdictions/za/privacy-legal/router.md
jurisdictions/za/privacy-legal/topics/cross-border-and-special-categories.md
jurisdictions/za/privacy-legal/topics/data-subject-rights.md
jurisdictions/za/privacy-legal/topics/enforcement-and-compliance.md
jurisdictions/za/privacy-legal/topics/impact-assessment.md
jurisdictions/za/privacy-legal/topics/lawful-processing.md
jurisdictions/za/privacy-legal/topics/operator-agreements.md
```

- [ ] **Step 7: Spot-check — no GDPR terminology leaks**

```bash
grep -rn "data controller\|data processor\|DPIA\|supervisory authority\|Article 28\|Article 35\|Article 15\|Article 22" jurisdictions/za/privacy-legal/topics/ || echo "PASS: no GDPR terminology in topic overlays"
```

Expected: PASS (no matches), OR matches only inside terminology comparison tables (which explain what NOT to use).

- [ ] **Step 8: Commit final validation results (if any fixes needed)**

If any validation step failed, fix the issue and commit the fix before proceeding.
