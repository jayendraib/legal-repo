# ZA Commercial-Legal Overlay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Adapt the commercial-legal plugin for South African law using additive overlays in `jurisdictions/za/commercial-legal/`, following the same architecture as the employment-legal overlay.

**Architecture:** Overlay system per ADR-001 and `jurisdictions/za/ARCHITECTURE.md`. 8 new statute YAML files in the shared `statutes/` directory. 6 topic overlay markdown files, a skill router, and a practice profile template in `jurisdictions/za/commercial-legal/`. Cold-start interview fork extends the existing ZA fork pattern. Validation scripts extended to cover commercial-legal. 16 eval cases.

**Spec:** `docs/superpowers/specs/2026-05-18-za-commercial-legal-expansion.md`

**Reference implementation:** `jurisdictions/za/employment-legal/` — match all file formats exactly.

**Tech Stack:** YAML (statutes, evals), Markdown (topics, router, template), Python 3 (validators)

---

## File Map

### New files to create

```
jurisdictions/za/statutes/
  cpa.yaml                          # Consumer Protection Act 68 of 2008
  ecta.yaml                         # Electronic Communications and Transactions Act 25 of 2002
  popia.yaml                        # Protection of Personal Information Act 4 of 2013
  conventional-penalties.yaml       # Conventional Penalties Act 15 of 1962
  competition.yaml                  # Competition Act 89 of 1998
  bbbee.yaml                        # B-BBEE Act 53 of 2003 (as amended)
  prescription.yaml                 # Prescription Act 68 of 1969
  copyright.yaml                    # Copyright Act 98 of 1978

jurisdictions/za/commercial-legal/
  router.md                         # Skill → topic + statute mapping
  practice-profile-template.md      # ZA variant of commercial-legal/CLAUDE.md
  topics/
    contract-fundamentals.md        # SA contract law, ECTA, CPA, exchange control, VAT
    liability-and-penalties.md      # Conventional Penalties Act, damages, prescription
    data-protection.md              # POPIA operator agreements, cross-border, enforcement
    competition-and-bbbee.md        # Competition Act, B-BBEE procurement, fronting
    confidentiality-and-restraint.md # NDA enforceability, restraint of trade, interdicts
    dispute-resolution.md           # Governing law, AFSA, arbitration, prescription

jurisdictions/za/evals/commercial-legal/
  vendor-agreement-review/
    case-01-happy-path.yaml
    case-02-foreign-vendor-multiple-flags.yaml
    case-03-cpa-covered-counterparty.yaml
    case-04-bbbee-procurement.yaml
  saas-msa-review/
    case-01-happy-path.yaml
    case-02-foreign-vendor-cross-border-vat.yaml
    case-03-cpa-threshold-boundary.yaml
    case-04-penalty-clause-in-sla.yaml
  nda-review/
    case-01-green-happy-path.yaml
    case-02-embedded-restraint.yaml
    case-03-personal-data-in-scope.yaml
  cold-start-interview/
    case-01-in-house-domestic.yaml
    case-02-mixed-foreign-small-business.yaml
    case-03-private-practice-multi-client.yaml
  customize/
    case-01-update-bbbee-level.yaml
    case-02-change-governing-law.yaml
```

### Files to modify

```
scripts/validate-za-router.py       # Add commercial-legal router validation
scripts/validate-za-templates.py    # Add commercial-legal template + required terms
jurisdictions/za/commercial-legal/.gitkeep  # DELETE (replaced by real files)
```

---

## Task 1: Statute YAML Files (8 files)

**Files:**
- Create: `jurisdictions/za/statutes/cpa.yaml`
- Create: `jurisdictions/za/statutes/ecta.yaml`
- Create: `jurisdictions/za/statutes/popia.yaml`
- Create: `jurisdictions/za/statutes/conventional-penalties.yaml`
- Create: `jurisdictions/za/statutes/competition.yaml`
- Create: `jurisdictions/za/statutes/bbbee.yaml`
- Create: `jurisdictions/za/statutes/prescription.yaml`
- Create: `jurisdictions/za/statutes/copyright.yaml`

Follow the exact schema from `jurisdictions/za/statutes/bcea.yaml`. Every section entry must have: `ref`, `value`, `effective_from`, `effective_until`, `effect`. Monetary entries also need `currency` and `unit`.

- [ ] **Step 1: Create `cpa.yaml`**

```yaml
statute: "Consumer Protection Act 68 of 2008"
authority: "Department of Trade, Industry and Competition"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/consumer-protection-act"

sections:
  juristic_person_threshold:
    ref: "CPA s5(2)(b), GN R294 GG 34399"
    value: 2000000
    currency: ZAR
    unit: "annual turnover or asset value"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "The CPA does not apply to transactions between juristic persons whose annual turnover or asset value equals or exceeds the threshold. Below-threshold juristic persons are treated as consumers."
    note: "Threshold set by Ministerial determination. Natural persons are always covered regardless of value."

  fixed_term_max_duration:
    ref: "CPA s14(1), Regulation 5(1)"
    value: 24
    unit: "months"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "Fixed-term consumer agreements must not exceed 24 months from the date of signature, unless a longer period is expressly agreed and the supplier can demonstrate a financial benefit to the consumer."
    note: "s14 does NOT apply between juristic persons regardless of turnover — only natural persons and sole proprietors."

  cancellation_notice_period:
    ref: "CPA s14(2)(b)"
    value: 20
    unit: "business days"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "A consumer may cancel a fixed-term agreement at any time by giving the supplier 20 business days' written notice. The consumer remains liable for amounts owed up to the date of cancellation, and the supplier may impose a reasonable cancellation penalty."

  supplier_expiry_notice_min:
    ref: "CPA s14(2)(a)"
    value: 40
    unit: "business days before expiry"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "The supplier must give the consumer written notice of the pending expiry of a fixed-term agreement not less than 40 and not more than 80 business days before the expiry date."

  supplier_expiry_notice_max:
    ref: "CPA s14(2)(a)"
    value: 80
    unit: "business days before expiry"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "Upper bound of the supplier notification window for pending expiry of fixed-term agreements."

  cooling_off_period:
    ref: "CPA s16(3)(a)"
    value: 5
    unit: "business days"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "A consumer who entered into a transaction as a result of direct marketing may cancel it within 5 business days after the later of the date on which the agreement was concluded or the goods were delivered."

  cpa_fine_max:
    ref: "CPA s112(1)"
    value: 1000000
    currency: ZAR
    unit: "per contravention or 10% of annual turnover"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "The National Consumer Tribunal may impose an administrative fine not exceeding the greater of R1,000,000 or 10% of the respondent's annual turnover."
```

- [ ] **Step 2: Create `ecta.yaml`**

```yaml
statute: "Electronic Communications and Transactions Act 25 of 2002"
authority: "Department of Communications and Digital Technologies"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/electronic-communications-and-transactions-act"

sections:
  data_message_legal_recognition:
    ref: "ECTA s11(1)"
    value: true
    effective_from: "2002-08-30"
    effective_until: null
    effect: "Information is not without legal force and effect merely because it is wholly or partly in the form of a data message."

  writing_requirement:
    ref: "ECTA s12"
    value: true
    effective_from: "2002-08-30"
    effective_until: null
    effect: "A requirement in law that a document or information must be in writing is met if the document is in the form of a data message and accessible for subsequent reference."

  electronic_signature_validity:
    ref: "ECTA s13(2)"
    value: true
    effective_from: "2002-08-30"
    effective_until: null
    effect: "An electronic signature is not without legal force and effect merely on the grounds that it is in electronic form."

  advanced_signature_required_when:
    ref: "ECTA s13(1)"
    value: "required by law without specifying type"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "Where the signature of a person is required by law and such law does not specify the type of signature, that requirement is met only if an advanced electronic signature is used."
    note: "Advanced e-signatures must be accredited by the SAAA. Required for: suretyships, copyright assignments, notarised documents, sealed documents."

  electronic_contract_formation:
    ref: "ECTA s22(1)"
    value: true
    effective_from: "2002-08-30"
    effective_until: null
    effect: "An agreement is not without legal force and effect merely because it was concluded partly or in whole by means of data messages."

  electronic_contract_conclusion:
    ref: "ECTA s22(2)"
    value: "at time and place acceptance received by offeror"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "An agreement concluded between parties by means of data messages is concluded at the time when and place where the acceptance of the offer was received by the offeror."

  schedule_1_exclusions:
    ref: "ECTA Schedule 1"
    value: "alienation of land, long leases >20 years, wills, bills of exchange"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "The provisions of ECTA relating to data messages, electronic signatures, and electronic transactions do not apply to these categories of agreements."
```

- [ ] **Step 3: Create `popia.yaml`**

```yaml
statute: "Protection of Personal Information Act 4 of 2013"
authority: "Information Regulator"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/protection-personal-information-act"

sections:
  operator_agreement_required:
    ref: "POPIA s21(1)"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A responsible party must, in terms of a written contract between it and the operator, ensure that the operator establishes and maintains security measures referred to in s19."
    note: "POPIA uses 'responsible party' (not 'controller') and 'operator' (not 'processor'). The contract must specify that the operator processes only on the responsible party's instructions."

  security_safeguards:
    ref: "POPIA s19(1)"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A responsible party must secure the integrity and confidentiality of personal information by taking appropriate, reasonable technical and organisational measures."

  breach_notification:
    ref: "POPIA s22(1)"
    value: "as soon as reasonably possible"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Where there are reasonable grounds to believe that personal information has been accessed or acquired by an unauthorised person, the responsible party must notify the Information Regulator and the data subject as soon as reasonably possible."

  cross_border_transfer:
    ref: "POPIA s72(1)"
    value: "prohibited unless safeguards met"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "A responsible party may not transfer personal information to a third party in a foreign country unless the recipient is subject to a law, binding corporate rules, or binding agreement providing an adequate level of protection substantially similar to POPIA."
    note: "No adequacy list published by the Information Regulator as of 2025. Practical approach is data transfer agreements adapted from GDPR SCCs."

  administrative_fine_max:
    ref: "POPIA s107(1)"
    value: 10000000
    currency: ZAR
    unit: "per contravention"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Any person convicted of an offence under POPIA is liable to a fine not exceeding R10 million or imprisonment for up to 10 years, or both."

  direct_marketing_restrictions:
    ref: "POPIA s69(1)"
    value: true
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Processing of personal information for direct marketing by electronic communication is prohibited unless the data subject has given consent or is an existing customer (and the marketing relates to similar products/services)."
    note: "Amended POPIA regulations (April 2025) introduce stricter requirements for direct marketing, telemarketing call recordings, and managing objections."
```

- [ ] **Step 4: Create `conventional-penalties.yaml`**

```yaml
statute: "Conventional Penalties Act 15 of 1962"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.justice.gov.za/legislation/acts/1962-015.pdf"

sections:
  enforceability:
    ref: "Conventional Penalties Act s1(1)"
    value: true
    effective_from: null
    effective_until: null
    effect: "A penalty stipulation providing that a person shall be liable to pay a sum of money or deliver anything for breach of contract, whether by way of penalty or as liquidated damages, is enforceable in any competent court."
    note: "SA enforces penalty clauses — opposite of the US approach where penalty clauses are generally void. SA treats 'liquidated damages' and 'penalty' identically under this Act."

  no_cumulation:
    ref: "Conventional Penalties Act s2(1)"
    value: true
    effective_from: null
    effective_until: null
    effect: "A creditor shall not recover both the penalty and damages for the same act or omission, unless the contract expressly provides otherwise. A creditor may not recover damages in lieu of the penalty unless the contract expressly so provides."
    note: "This is the most common trap in US-drafted agreements used in SA. A contract must expressly permit claiming both penalty and damages, or claiming damages instead of the penalty."

  no_penalty_for_defective_performance_accepted:
    ref: "Conventional Penalties Act s2(2)"
    value: true
    effective_from: null
    effective_until: null
    effect: "A person who accepts or is obliged to accept defective or non-timeous performance shall not recover a penalty unless the penalty was expressly stipulated for that defect or delay."

  judicial_reduction:
    ref: "Conventional Penalties Act s3"
    value: true
    effective_from: null
    effective_until: null
    effect: "If a penalty is out of proportion to the prejudice suffered, the court may reduce it to an equitable extent, considering not only the creditor's proprietary interest but every other rightful interest affected."

  forfeiture_as_penalty:
    ref: "Conventional Penalties Act s4"
    value: true
    effective_from: null
    effective_until: null
    effect: "A forfeiture clause (upon withdrawal from an agreement, a party forfeits the right to restitution or remains liable for performance) is treated as a penalty stipulation subject to sections 1-3."
```

- [ ] **Step 5: Create `competition.yaml`**

```yaml
statute: "Competition Act 89 of 1998"
authority: "Competition Commission"
last_confirmed: "2025-05-01"
source_url: "https://www.compcom.co.za/wp-content/uploads/2021/03/Competition-Act-A6.pdf"

sections:
  horizontal_practices_prohibited:
    ref: "Competition Act s4(1)(b)"
    value: "per se prohibited"
    effective_from: "1999-09-01"
    effective_until: null
    effect: "The following restrictive horizontal practices are per se prohibited: directly or indirectly fixing a purchase or selling price or any other trading condition; dividing markets by allocating customers, suppliers, territories, or types of goods/services; collusive tendering."

  vertical_practices_test:
    ref: "Competition Act s5(1)"
    value: "substantial lessening of competition test"
    effective_from: "1999-09-01"
    effective_until: null
    effect: "An agreement between parties in a vertical relationship is prohibited if it has the effect of substantially preventing or lessening competition, unless pro-competitive gains outweigh the effect."

  minimum_resale_price_maintenance:
    ref: "Competition Act s5(2)"
    value: "prohibited"
    effective_from: "1999-09-01"
    effective_until: null
    effect: "The practice of minimum resale price maintenance is prohibited. A supplier may recommend a minimum resale price provided it is clear the recommendation is not binding."

  administrative_penalty_max:
    ref: "Competition Act s59(2)"
    value: 10
    unit: "percent of annual turnover in SA"
    effective_from: "1999-09-01"
    effective_until: null
    effect: "The Competition Tribunal may impose an administrative penalty not exceeding 10% of the firm's annual turnover in South Africa during its preceding financial year."
```

- [ ] **Step 6: Create `bbbee.yaml`**

```yaml
statute: "Broad-Based Black Economic Empowerment Act 53 of 2003 (as amended by Act 46 of 2013)"
authority: "Department of Trade, Industry and Competition"
last_confirmed: "2025-05-01"
source_url: "https://www.thedtic.gov.za/financial-and-non-financial-support/b-bbee/"

sections:
  organs_of_state_must_apply:
    ref: "B-BBEE Act s10(1)(b)"
    value: true
    effective_from: "2014-10-24"
    effective_until: null
    effect: "Every organ of state and public entity must apply relevant codes of good practice when developing and implementing a preferential procurement policy."

  fronting_prohibition:
    ref: "B-BBEE Act s13F"
    value: true
    effective_from: "2014-10-24"
    effective_until: null
    effect: "Fronting practices are prohibited. A B-BBEE initiative in which black persons are discouraged from substantially participating, economic benefits do not flow to black people in the specified ratios, or terms were not negotiated at arm's length, constitutes fronting."
    note: "Fronting is a criminal offence. Contracts awarded on false B-BBEE information may be cancelled."

  eme_threshold:
    ref: "B-BBEE Codes of Good Practice, Statement 000"
    value: 10000000
    currency: ZAR
    unit: "annual turnover"
    effective_from: "2019-05-01"
    effective_until: null
    effect: "An Exempted Micro Enterprise (EME) is a business with an annual total revenue of R10 million or less. EMEs are deemed Level 4 contributors (Level 1 if 100% black-owned, Level 2 if 51%+ black-owned)."
    gazette_date: "2019-05-01"

  qse_threshold:
    ref: "B-BBEE Codes of Good Practice, Statement 000"
    value: 50000000
    currency: ZAR
    unit: "annual turnover"
    effective_from: "2019-05-01"
    effective_until: null
    effect: "A Qualifying Small Enterprise (QSE) is a business with annual total revenue between R10 million and R50 million. QSEs use the QSE scorecard with all 5 elements of B-BBEE."
    gazette_date: "2019-05-01"

  preferential_procurement_80_20:
    ref: "Preferential Procurement Regulations 2017, reg 6(1)"
    value: 80
    unit: "points for price, 20 for B-BBEE"
    effective_from: "2017-04-01"
    effective_until: null
    effect: "For procurement of goods and services with a rand value up to R50 million, 80 points are allocated for price and 20 points for the bidder's B-BBEE status level."

  preferential_procurement_90_10:
    ref: "Preferential Procurement Regulations 2017, reg 7(1)"
    value: 90
    unit: "points for price, 10 for B-BBEE"
    effective_from: "2017-04-01"
    effective_until: null
    effect: "For procurement of goods and services with a rand value above R50 million, 90 points are allocated for price and 10 points for the bidder's B-BBEE status level."
```

- [ ] **Step 7: Create `prescription.yaml`**

```yaml
statute: "Prescription Act 68 of 1969"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.justice.gov.za/legislation/acts/1969-068.pdf"

sections:
  debt_prescription_period:
    ref: "Prescription Act s11(d)"
    value: 3
    unit: "years"
    effective_from: null
    effective_until: null
    effect: "A debt prescribes (becomes unenforceable) after 3 years, unless a longer period applies under another provision of s11."

  other_debt_prescription:
    ref: "Prescription Act s11(a)"
    value: 6
    unit: "years"
    effective_from: null
    effective_until: null
    effect: "Any debt not falling under another provision of s11 prescribes after 6 years."
    note: "The 6-year period applies to claims arising from breach of contract where the claim is not for a 'debt' in the narrow sense (e.g. claims for damages for breach)."

  prescription_begins:
    ref: "Prescription Act s12(1)"
    value: "when the debt is due"
    effective_from: null
    effective_until: null
    effect: "Prescription begins to run as soon as the debt is due. A debt is due when the creditor has knowledge of the identity of the debtor and the facts from which the debt arises."

  delay_of_prescription:
    ref: "Prescription Act s13(1)"
    value: true
    effective_from: null
    effective_until: null
    effect: "If the creditor is prevented by superior force (including ignorance of facts) from interrupting prescription, the period is extended."
```

- [ ] **Step 8: Create `copyright.yaml`**

```yaml
statute: "Copyright Act 98 of 1978"
authority: "Companies and Intellectual Property Commission (CIPC)"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/copyright-act"

sections:
  employer_ownership:
    ref: "Copyright Act s21(1)(d)"
    value: true
    effective_from: null
    effective_until: null
    effect: "Where a work is made in the course of employment under a contract of service, the employer is the owner of any copyright subsisting in the work, subject to any agreement to the contrary."

  assignment_must_be_in_writing:
    ref: "Copyright Act s22(3)"
    value: true
    effective_from: null
    effective_until: null
    effect: "No assignment of copyright and no exclusive licence to do an act which is subject to copyright shall have effect unless it is in writing signed by or on behalf of the assignor or licensor."

  computer_generated_works:
    ref: "Copyright Act s1, s21(1)(c)"
    value: "person who arranged creation is author"
    effective_from: null
    effective_until: null
    effect: "In the case of a computer-generated literary, dramatic, musical or artistic work, the person by whom the arrangements necessary for the creation of the work were undertaken is deemed the author."
```

- [ ] **Step 9: Run statute validator**

Run: `python3 scripts/validate-za-statutes.py`
Expected: All 12 statute files pass (4 existing + 8 new). Zero errors.

- [ ] **Step 10: Commit**

```bash
git add jurisdictions/za/statutes/cpa.yaml jurisdictions/za/statutes/ecta.yaml jurisdictions/za/statutes/popia.yaml jurisdictions/za/statutes/conventional-penalties.yaml jurisdictions/za/statutes/competition.yaml jurisdictions/za/statutes/bbbee.yaml jurisdictions/za/statutes/prescription.yaml jurisdictions/za/statutes/copyright.yaml
git commit -m "feat(za): add 8 commercial-legal statute YAML files

CPA, ECTA, POPIA, Conventional Penalties Act, Competition Act,
B-BBEE Act, Prescription Act, Copyright Act. All pass
validate-za-statutes.py."
```

---

## Task 2: Topic Overlay Markdown Files (6 files)

**Files:**
- Create: `jurisdictions/za/commercial-legal/topics/contract-fundamentals.md`
- Create: `jurisdictions/za/commercial-legal/topics/liability-and-penalties.md`
- Create: `jurisdictions/za/commercial-legal/topics/data-protection.md`
- Create: `jurisdictions/za/commercial-legal/topics/competition-and-bbbee.md`
- Create: `jurisdictions/za/commercial-legal/topics/confidentiality-and-restraint.md`
- Create: `jurisdictions/za/commercial-legal/topics/dispute-resolution.md`
- Delete: `jurisdictions/za/commercial-legal/.gitkeep`

Follow the format of `jurisdictions/za/employment-legal/topics/dismissal.md`: H1 title, H2 sections for major areas, statute references in the format `CPA s14`, `POPIA s21(1)`, flag tables, no US-specific concepts.

Each topic file should include:
1. A header paragraph stating which skills load it and what statutes it references
2. The statutory framework (SA-specific)
3. Procedural checklists or assessment frameworks where applicable
4. Flag tables matching the 12 high-risk flags from the spec (flags distributed across the topics they relate to)
5. A "must not contain" reminder for US terms specific to that topic

The spec (Section 3, Topic Overlay Map) contains the complete content outline for each file. The spec (Section 6, High-Risk Flag Table) contains the 12 flags — distribute them to the topic files that own their subject matter:

| Flag | Topic file |
|---|---|
| #1 No POPIA operator agreement | data-protection.md |
| #2 Cross-border data without safeguards | data-protection.md |
| #3 Penalty-damages cumulation trap | liability-and-penalties.md |
| #4 Foreign governing law + exchange control | contract-fundamentals.md |
| #5 CPA-covered non-compliant terms | contract-fundamentals.md |
| #6 Overbroad restraint of trade | confidentiality-and-restraint.md |
| #7 B-BBEE fronting indicators | competition-and-bbbee.md |
| #8 Missing non-variation clause | contract-fundamentals.md |
| #9 Uncapped liability + specific performance | liability-and-penalties.md |
| #10 Auto-renewal without proper notice | contract-fundamentals.md |
| #11 VAT on imported services misconfigured | contract-fundamentals.md |
| #12 Prescription period mismatch | dispute-resolution.md |

- [ ] **Step 1: Create `topics/` directory and all 6 topic files**

Create each file following the content outline in spec Section 3. Each file should be 150-300 lines. Use the dismissal.md reference for format but with commercial-legal content.

The H1 for each file:
- `# Contract Fundamentals — South African Framework`
- `# Liability and Penalties — South African Framework`
- `# Data Protection — South African Framework (POPIA)`
- `# Competition and B-BBEE — South African Framework`
- `# Confidentiality and Restraint of Trade — South African Framework`
- `# Dispute Resolution — South African Framework`

- [ ] **Step 2: Delete `.gitkeep`**

```bash
rm jurisdictions/za/commercial-legal/.gitkeep
```

- [ ] **Step 3: Verify all 6 topic files exist and have content**

```bash
for f in contract-fundamentals liability-and-penalties data-protection competition-and-bbbee confidentiality-and-restraint dispute-resolution; do
  wc -l "jurisdictions/za/commercial-legal/topics/${f}.md"
done
```

Expected: All 6 files exist, each 150+ lines.

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/commercial-legal/topics/ jurisdictions/za/commercial-legal/.gitkeep
git commit -m "feat(za): add 6 commercial-legal topic overlay files

contract-fundamentals, liability-and-penalties, data-protection,
competition-and-bbbee, confidentiality-and-restraint, dispute-resolution.
Includes all 12 high-risk flags distributed across topics."
```

---

## Task 3: Skill Router

**Files:**
- Create: `jurisdictions/za/commercial-legal/router.md`

Follow the exact format of `jurisdictions/za/employment-legal/router.md`: markdown with an embedded `yaml` code fence.

- [ ] **Step 1: Create the router file**

```markdown
# Skill Router — South African Commercial Contracts Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/commercial-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
vendor-agreement-review:
  topics: [contract-fundamentals, liability-and-penalties, data-protection, competition-and-bbbee, confidentiality-and-restraint, dispute-resolution]
  statutes: [cpa, ecta, popia, conventional-penalties, competition, bbbee, prescription, copyright]

saas-msa-review:
  topics: [contract-fundamentals, liability-and-penalties, data-protection, competition-and-bbbee, dispute-resolution]
  statutes: [cpa, ecta, popia, conventional-penalties, competition, bbbee, prescription]

nda-review:
  topics: [contract-fundamentals, data-protection, confidentiality-and-restraint, dispute-resolution]
  statutes: [ecta, popia, prescription]

cold-start-interview:
  topics: []
  statutes: [cpa, ecta, popia, conventional-penalties, competition, bbbee, prescription, copyright]

customize:
  topics: []
  statutes: []
```
```

Note: The triple-backtick fence closing needs to appear after the YAML block. The router validator parses this exact format.

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/commercial-legal/router.md
git commit -m "feat(za): add commercial-legal skill router

Maps 5 in-scope skills to topic overlays and statute files."
```

---

## Task 4: Practice Profile Template

**Files:**
- Create: `jurisdictions/za/commercial-legal/practice-profile-template.md`

Follow the format of `jurisdictions/za/employment-legal/practice-profile-template.md`. Start with the HTML comment header (CONFIGURATION LOCATION + JURISDICTION OVERLAY instruction), then the SA-native sections.

- [ ] **Step 1: Create the practice profile template**

The template must include:
1. HTML comment header with `CONFIGURATION LOCATION` and `JURISDICTION OVERLAY` instruction pointing to `jurisdictions/za/commercial-legal/router.md`
2. All sections from spec Section 4 (Section replacement table + New sections)
3. SA work-product header (spec Section 4, "Work-product header")
4. SA-required terms that the template validator will check: `CPA`, `POPIA`, `B-BBEE`, `ECTA`, `Conventional Penalties Act`, `admitted attorney`, `operator agreement`, `responsible party`
5. No US-forbidden terms outside the privilege caveat section

Use the employment-legal template as the structural model but replace all employment-specific content with commercial contract content from the spec.

Key sections in order:
- `# Commercial Contracts Practice Profile — South Africa`
- `## Who we are` (extended with CIPC, B-BBEE level, provinces)
- `## Who's using this` (extended with SA Legal Practice Act roles)
- `## SA statutory baseline` (NEW — router instruction)
- `## B-BBEE compliance posture` (NEW)
- `## CPA applicability` (NEW)
- `## SA contract fundamentals` (NEW)
- `## Available integrations`
- `## Playbook` (with SA-specific governing law, data protection, liability, term sections)
- `## Escalation` (extended with B-BBEE trigger)
- `## House style`
- `## Outputs` (SA privilege header)
- `## NDA triage preferences`
- `## Matter workspaces`

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/commercial-legal/practice-profile-template.md
git commit -m "feat(za): add commercial-legal practice profile template

SA-native template with B-BBEE posture, CPA applicability, POPIA
operator agreement framing, SA privilege header. Replaces US
governing law, data protection, and work-product header sections."
```

---

## Task 5: Cold-Start Interview Fork

**Files:**
- Modify: `commercial-legal/skills/cold-start-interview/SKILL.md`

The cold-start interview SKILL.md does not currently have a ZA fork. Add one following the same pattern as employment-legal (ADR-001 D8): a jurisdiction branch after Part 0 that asks SA-specific configuration questions and writes to the ZA practice profile template.

- [ ] **Step 1: Read the current cold-start interview SKILL.md fully**

Read `commercial-legal/skills/cold-start-interview/SKILL.md` to find the Part 0 completion point where the fork should be inserted.

- [ ] **Step 2: Add the ZA fork**

After Part 0 completes (company profile written), insert a jurisdiction check:

```markdown
### Part 0.5 — South African commercial contracts (ZA fork)

**Trigger:** If the company profile's `jurisdiction` field is `ZA`, or the user indicates South African jurisdiction during Part 0, run Part 0.5 before proceeding to Part 1.

**Purpose:** Capture SA-specific configuration that the commercial-legal overlay needs. The overlay lives in `jurisdictions/za/commercial-legal/` and the practice profile template at `jurisdictions/za/commercial-legal/practice-profile-template.md` requires these fields populated.

**Questions (must-have — ask all 7):**

1. "What is your company's current B-BBEE status level? (Level 1-8 / EME / QSE / not verified / exempt)"
   → Writes to: `## B-BBEE compliance posture`

2. "Are your typical counterparties natural persons, below-threshold juristic persons (under R2m turnover/assets), or above-threshold juristic persons?"
   → Writes to: `## CPA applicability`

3. "What is your standard governing law and dispute resolution position? (SA law + High Court / SA law + AFSA arbitration / other)"
   → Writes to: `## Playbook → Governing law`

4. "Do you have a POPIA operator agreement template, or do you typically sign the vendor's data processing terms? When vendors host data outside SA, what's your position on cross-border transfers?"
   → Writes to: `## Playbook → Data protection`

5. "Do you contract with government or public sector entities? If yes, are B-BBEE scorecard requirements part of your tender responses?"
   → Writes to: `## B-BBEE compliance posture` + `## Escalation`

6. "Do you regularly contract with foreign (non-SA) vendors or pay fees/royalties/license fees to non-resident parties?"
   → Writes to: `## SA contract fundamentals` (exchange control awareness)

7. "Is your company VAT-registered? Do your foreign SaaS/service providers charge SA VAT, or do you account for imported services VAT under reverse charge?"
   → Writes to: `## SA contract fundamentals` (VAT posture)

**After Part 0.5:** Use `jurisdictions/za/commercial-legal/practice-profile-template.md` instead of the US template for writing `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Proceed to Part 1 (practice setting, role, integrations) as normal.

**Nice-to-have questions** are folded into Part 2 (playbook interview):
- Q8 (penalty clause posture) during liability discussion
- Q9 (contract term preference) during term & termination
- Q10 (dispute history) during governing law
- Q11 (sector restrictions) during escalation
```

- [ ] **Step 3: Commit**

```bash
git add commercial-legal/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to commercial-legal cold-start interview

7 must-have questions after Part 0 when jurisdiction = ZA. Covers
B-BBEE level, CPA counterparty threshold, governing law, POPIA
operator posture, public sector contracting, exchange control,
and VAT registration."
```

---

## Task 6: Validation Scripts

**Files:**
- Modify: `scripts/validate-za-router.py`
- Modify: `scripts/validate-za-templates.py`

The existing validators are hardcoded to employment-legal. Extend them to also validate commercial-legal.

- [ ] **Step 1: Extend `validate-za-router.py` to handle commercial-legal**

The current script has hardcoded paths:
```python
ROUTER_PATH = REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "router.md"
SKILLS_DIR = REPO_ROOT / "employment-legal" / "skills"
TOPICS_DIR = REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "topics"
```

Refactor to iterate over all practice areas that have a router. Change the approach to:

```python
PRACTICE_AREAS = [
    {
        "name": "employment-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "router.md",
        "skills_dir": REPO_ROOT / "employment-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "topics",
    },
    {
        "name": "commercial-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "commercial-legal" / "router.md",
        "skills_dir": REPO_ROOT / "commercial-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "commercial-legal" / "topics",
    },
]
```

Then loop over each practice area and validate. The `main()` function returns 1 if any area fails.

- [ ] **Step 2: Extend `validate-za-templates.py` to handle commercial-legal**

Add the commercial-legal template to `ZA_TEMPLATES`:
```python
ZA_TEMPLATES = [
    ROOT / "jurisdictions" / "za" / "employment-legal" / "practice-profile-template.md",
    ROOT / "jurisdictions" / "za" / "commercial-legal" / "practice-profile-template.md",
]
```

Add commercial-legal required sections and terms. The validator needs practice-area-specific config. Refactor to a dict:

```python
TEMPLATE_CONFIG = {
    "employment-legal": {
        "path": ROOT / "jurisdictions" / "za" / "employment-legal" / "practice-profile-template.md",
        "required_sections": [
            "Jurisdictional footprint", "Statutory baseline", "Employment equity",
            "Dispute resolution", "Leave and conditions", "Termination review",
            "Hiring review", "Escalation", "Seed documents", "Outputs",
        ],
        "sa_required_terms": ["CCMA", "BCEA", "LRA", "bargaining council", "Schedule 8", "admitted attorney"],
        "us_forbidden": [
            (r"\bFMLA\b", "FMLA"), (r"\bFLSA\b", "FLSA"), (r"\bEEOC\b", "EEOC"),
            (r"\bNLRB\b", "NLRB"), (r"\bWARN Act\b", "WARN Act"),
            (r"\bCal-WARN\b", "Cal-WARN"), (r"\bstate supplements?\b", "state supplement(s)"),
        ],
    },
    "commercial-legal": {
        "path": ROOT / "jurisdictions" / "za" / "commercial-legal" / "practice-profile-template.md",
        "required_sections": [
            "Who we are", "Who's using this", "SA statutory baseline",
            "B-BBEE compliance posture", "CPA applicability", "SA contract fundamentals",
            "Playbook", "Escalation", "Outputs", "NDA triage preferences",
        ],
        "sa_required_terms": [
            "CPA", "POPIA", "B-BBEE", "ECTA", "Conventional Penalties Act",
            "admitted attorney", "operator agreement", "responsible party",
        ],
        "us_forbidden": [
            (r"\bUCC\b", "UCC"), (r"\bFRCP\b", "FRCP"),
            (r"\bHadley v Baxendale\b", "Hadley v Baxendale"),
            (r"\bdata controller\b", "data controller"),
            (r"\bdata processor\b", "data processor"),
            (r"\bpreliminary injunction\b", "preliminary injunction"),
        ],
    },
}
```

- [ ] **Step 3: Run both validators**

```bash
python3 scripts/validate-za-router.py
python3 scripts/validate-za-templates.py
python3 scripts/validate-za-statutes.py
```

Expected: All pass with 0 errors.

- [ ] **Step 4: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for commercial-legal overlay

Router validator now checks both employment-legal and commercial-legal.
Template validator has practice-area-specific required sections and terms."
```

---

## Task 7: Scenario Eval Cases (16 files)

**Files:**
- Create: 16 YAML files in `jurisdictions/za/evals/commercial-legal/`

Follow the exact format of `jurisdictions/za/evals/employment-legal/termination-review/case-01-misconduct-no-hearing.yaml`: YAML with `name`, `skill`, `input`, `expected_flags`, `expected_statutes`, `must_not_contain`, `notes`.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/evals/commercial-legal/{vendor-agreement-review,saas-msa-review,nda-review,cold-start-interview,customize}
```

- [ ] **Step 2: Create all 16 eval case files**

Write each case from the spec (Section 7, Eval Case Outlines). Each file should be ~20-40 lines of YAML. The `input` field should contain a realistic 3-5 sentence fact pattern. The `expected_flags` should list the flag names from the high-risk flag table. The `must_not_contain` should include the US terms from the terminology table.

Files to create:
- `vendor-agreement-review/case-01-happy-path.yaml`
- `vendor-agreement-review/case-02-foreign-vendor-multiple-flags.yaml`
- `vendor-agreement-review/case-03-cpa-covered-counterparty.yaml`
- `vendor-agreement-review/case-04-bbbee-procurement.yaml`
- `saas-msa-review/case-01-happy-path.yaml`
- `saas-msa-review/case-02-foreign-vendor-cross-border-vat.yaml`
- `saas-msa-review/case-03-cpa-threshold-boundary.yaml`
- `saas-msa-review/case-04-penalty-clause-in-sla.yaml`
- `nda-review/case-01-green-happy-path.yaml`
- `nda-review/case-02-embedded-restraint.yaml`
- `nda-review/case-03-personal-data-in-scope.yaml`
- `cold-start-interview/case-01-in-house-domestic.yaml`
- `cold-start-interview/case-02-mixed-foreign-small-business.yaml`
- `cold-start-interview/case-03-private-practice-multi-client.yaml`
- `customize/case-01-update-bbbee-level.yaml`
- `customize/case-02-change-governing-law.yaml`

- [ ] **Step 3: Validate YAML syntax**

```bash
python3 -c "import yaml; [yaml.safe_load(open(f)) for f in __import__('glob').glob('jurisdictions/za/evals/commercial-legal/**/*.yaml', recursive=True)]"
```

Expected: No errors.

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/evals/commercial-legal/
git commit -m "feat(za): add 16 commercial-legal scenario eval cases

4 vendor-agreement-review, 4 saas-msa-review, 3 nda-review,
3 cold-start-interview, 2 customize. Each specifies input scenario,
expected flags, expected statutes, and US must-not-contain terms."
```

---

## Task 8: Final Validation Run

**Files:** None created — this is a verification task.

- [ ] **Step 1: Run all three validators**

```bash
python3 scripts/validate-za-statutes.py
python3 scripts/validate-za-router.py
python3 scripts/validate-za-templates.py
```

Expected output:
```
OK: 12 statute files validated, no errors
OK: employment-legal — 7 skills, all references resolve
OK: commercial-legal — 5 skills, all references resolve
  OK: practice-profile-template.md (employment-legal)
  OK: practice-profile-template.md (commercial-legal)
2 templates checked, no errors
```

- [ ] **Step 2: Run JSON/YAML sanity check (repo-wide)**

```bash
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('jurisdictions/**/*.yaml', recursive=True)]"
```

Expected: No errors.

- [ ] **Step 3: Verify US concept leak check**

```bash
grep -rn "FMLA\|FLSA\|at-will\|EEOC\|NLRB\|UCC\|FRCP 26" jurisdictions/za/commercial-legal/ || echo "No US leaks found"
grep -rn "data controller\|data processor" jurisdictions/za/commercial-legal/ || echo "No GDPR terminology leaks"
```

Expected: "No US leaks found" and "No GDPR terminology leaks" (or matches only in explicit must-not-contain sections).

- [ ] **Step 4: Verify file count and structure**

```bash
echo "--- Statute files ---"
ls jurisdictions/za/statutes/*.yaml | wc -l  # Expected: 12

echo "--- Commercial-legal topic files ---"
ls jurisdictions/za/commercial-legal/topics/*.md | wc -l  # Expected: 6

echo "--- Router ---"
ls jurisdictions/za/commercial-legal/router.md  # Expected: exists

echo "--- Practice profile template ---"
ls jurisdictions/za/commercial-legal/practice-profile-template.md  # Expected: exists

echo "--- Eval cases ---"
find jurisdictions/za/evals/commercial-legal -name "*.yaml" | wc -l  # Expected: 16
```

- [ ] **Step 5: Document expert review gate**

The final step is not automated. Add a note to the spec or a `REVIEW.md` file documenting:
- All validators pass
- Expert review pending: an SA commercial law practitioner should review statute YAML values, topic overlay content, high-risk flags, and practice profile template before the overlay is used in production.

- [ ] **Step 6: Final commit**

```bash
git add -A
git commit -m "chore(za): final validation pass for commercial-legal overlay

All validators pass. Expert review gate documented.
12 statute files, 6 topic overlays, 1 router, 1 practice profile
template, 1 cold-start fork, 16 eval cases."
```
