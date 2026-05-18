# ZA Commercial-Legal Expansion — Decision Spec

**Date:** 2026-05-18
**Plugin:** commercial-legal v1.0.2
**Produced by:** `/jurisdiction-expansion commercial-legal`
**Architecture:** `jurisdictions/za/ARCHITECTURE.md` + ADR-001

---

## Decision Summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | commercial-legal — 12 skills, 5 in scope | user confirmed |
| 2 | Statutes | 8 new statute YAML files + exchange control and VAT coverage in topic overlays | Perplexity + user confirmed |
| 3 | Skill divergence | 3 HIGH, 2 MEDIUM in scope; 7 LOW out of scope | user confirmed |
| 4 | Topic overlays | 6 topic files serving 3 review skills | Perplexity + user confirmed |
| 5 | Practice profile | SA-native template with 4 new sections + SA privilege header | user confirmed |
| 6 | Cold-start | 7 must-have + 4 nice-to-have questions; fork after Part 0 | Perplexity + user confirmed |
| 7 | High-risk flags | 12 SA-specific flags cross-referenced to all Step 2 statutes | Perplexity + user confirmed |
| 8 | Validation | 16 eval cases across 5 skills + terminology must-not-contain list + expert review gate | user confirmed |

---

## 1. Statute Inventory

All statutes are **new** — none of the existing employment-legal statute files (bcea.yaml, lra.yaml, eea.yaml, sectoral-determinations.yaml) are relevant to commercial-legal.

| # | Statute | File | Key sections | Temporal / Gazette values |
|---|---|---|---|---|
| 1 | Consumer Protection Act 68 of 2008 | `cpa.yaml` | s5(2) exemption threshold; s14 fixed-term (24 months max, 20 business days' notice); s16 cooling-off (5 days); s22 plain language; s48 unfair terms; s49 notice for risk/liability; s51 prohibited terms; s54/s56 quality/implied warranty; s61 product liability | CPA juristic person threshold (R2m — Ministerial determination) |
| 2 | Electronic Communications and Transactions Act 25 of 2002 | `ecta.yaml` | s11 legal recognition of data messages; s12 writing requirement; s13 electronic signatures (standard vs advanced); s20 automated transactions; s22 electronic contract formation; s43 e-commerce disclosure; Schedule 1/2 exclusions | None |
| 3 | Protection of Personal Information Act 4 of 2013 | `popia.yaml` | s19 security safeguards; s21 operator agreements; s22 breach notification; s69 direct marketing; s72 cross-border transfers; s107 penalties (up to R10m) | Penalty ceiling R10m (statute, not Gazette) |
| 4 | Conventional Penalties Act 15 of 1962 | `conventional-penalties.yaml` | s1 enforceability; s2 no cumulation (penalty OR damages unless expressly permitted); s3 judicial reduction (proportionality); s4 forfeiture = penalty | None |
| 5 | Competition Act 89 of 1998 | `competition.yaml` | s4 restrictive horizontal (price-fixing, market division, collusive tendering per se prohibited); s5 restrictive vertical (substantial lessening test); s5(2) minimum resale price maintenance; s9 price discrimination by dominant firms | Penalty cap 10% SA turnover (statute) |
| 6 | Broad-Based Black Economic Empowerment Act 53 of 2003 (as amended by Act 46 of 2013) | `bbbee.yaml` | s10 organs of state must apply codes; s13F fronting prohibition; preferential procurement (80/20 for bids up to R50m, 90/10 above R50m); EME threshold (R10m); QSE threshold (R10m-R50m) | EME/QSE turnover thresholds; B-BBEE scorecard weightings (Gazette/Codes of Good Practice) |
| 7 | Prescription Act 68 of 1969 | `prescription.yaml` | s11 prescriptive periods (3 years debt, 6 years other); s12 when prescription begins; s13 delay of prescription | None |
| 8 | Copyright Act 98 of 1978 | `copyright.yaml` | s21(1)(c) works in course of employment; s22 assignment must be in writing; s11B computer-generated works | None |

**Additional coverage in topic overlays (not separate statute files):**
- Exchange Control Regulations (Currency and Exchanges Act 9 of 1933) — SARB Financial Surveillance, Authorised Dealer requirements, arm's length pricing, Circular 13/2024 liberalization
- VAT Act 89 of 1991 + Electronic Services Regulations (2025) — 15.5% rate (May 2025), 16% (April 2026), B2B exclusion rules, reverse charge, R1m registration threshold

---

## 2. Skill Divergence Matrix

| # | Skill | Divergence | In scope v1 | Reasoning |
|---|---|---|---|---|
| 1 | `vendor-agreement-review` | **HIGH** | Yes | Provisional mode defaults to US. SA divergences: specific performance primary remedy, Conventional Penalties Act (enforceable), CPA s48 unfair terms for below-threshold B2B, B-BBEE supplier compliance, POPIA operator agreements. |
| 2 | `saas-msa-review` | **HIGH** | Yes | Explicitly references US auto-renewal statutes. SA has CPA s14, POPIA s21 operator agreements, s72 cross-border, ECTA electronic formation. VAT on imported electronic services (April 2025 reforms). |
| 3 | `cold-start-interview` | **HIGH** | Yes | Entry point configuring everything downstream. Needs SA fork for B-BBEE, CPA applicability, POPIA operator template, SA governing law, exchange control, VAT posture. Single upstream file modification per ADR-001 D8. |
| 4 | `nda-review` | **MEDIUM** | Yes | Triage framework is playbook-driven (portable), but SA restraint of trade doctrine differs (presumed valid, Basson v Chilwan 5-part test), POPIA interaction for NDAs covering personal info, SA interdict vs US preliminary injunction. |
| 5 | `customize` | **MEDIUM** | Yes | Process-neutral but needs awareness of SA-specific configuration fields (B-BBEE, CPA threshold, POPIA operator template, exchange control, VAT). |
| 6 | `review` | LOW | No | Infrastructure router — no substantive legal content. |
| 7 | `review-proposals` | LOW | No | Process-neutral playbook update review. |
| 8 | `renewal-tracker` | LOW | No | Register format jurisdiction-neutral. CPA s14 notice captured at review time. |
| 9 | `escalation-flagger` | LOW | No | Reads from user-configured matrix. B-BBEE escalation configured in matrix. |
| 10 | `stakeholder-summary` | LOW | No | Output format skill. SA privilege handled by practice profile template. |
| 11 | `amendment-history` | LOW | No | Document analysis, fully jurisdiction-neutral. |
| 12 | `matter-workspace` | LOW | No | Infrastructure, process-neutral. |

---

## 3. Topic Overlay Map

6 topic files in `jurisdictions/za/commercial-legal/topics/`:

| # | Topic file | Skills served | Key content areas |
|---|---|---|---|
| 1 | `contract-fundamentals.md` | vendor-agreement-review, saas-msa-review, nda-review | SA common law of contract (no consideration, causa, consensus ad idem); ECTA formation and e-signatures (standard vs advanced, Schedule 1/2 exclusions); CPA applicability threshold (R2m juristic person; s14 does NOT apply between juristic persons); CPA s48 unfair terms, s22 plain language, s14 fixed-term limits; specific performance as primary remedy; Shifren principle (non-variation clauses strictly enforced); exceptio non adimpleti contractus; CPA Regulation 44(3) unfair terms list; commercial bribery as grounds for rescission; **exchange control** (SARB Financial Surveillance, Authorised Dealer routing, arm's length for related parties, Circular 13/2024); **VAT on electronic services** (15.5% rate, April 2026 16%, B2B exclusion, reverse charge, R1m threshold) |
| 2 | `liability-and-penalties.md` | vendor-agreement-review, saas-msa-review | Conventional Penalties Act (enforceable — opposite of US; s2 no cumulation; s3 judicial reduction); SA indemnity conventions; SA damages taxonomy (general vs special — Lavery v Jungheinrich test stricter than Hadley v Baxendale); CPA s51 gross negligence prohibition; specific performance as primary remedy; Prescription Act periods (3 years debt, 6 years other); Drax Energy case on per-claim vs aggregate cap interpretation; Barkhuizen v Napier on unconscionable limitation periods |
| 3 | `data-protection.md` | vendor-agreement-review, saas-msa-review, nda-review | POPIA operator agreements (s21 — "operator" not "processor"); responsible party/operator terminology; security safeguards (s19); breach notification (s22 — 2,374 breaches reported 2024/25, 40% increase); cross-border transfers (s72 — no adequacy list from Information Regulator yet, practical approach is data transfer agreements); sub-operator agreements required (same terms must flow down); BCRs don't need registration; R10m penalty ceiling; Information Regulator enforcement actions (R5m DBE, R5m DOJ, R500k Blouberg, R100k Lancet); amended POPIA regulations (April 2025 — stricter direct marketing, telemarketing, compliance frameworks); must-not-contain: "data controller", "data processor", "GDPR", "DPA" |
| 4 | `competition-and-bbbee.md` | vendor-agreement-review, saas-msa-review | Competition Act s4/s5 restrictive practices; s5(2) minimum resale price maintenance ban; B-BBEE Act s10 preferential procurement; scorecard levels and EME/QSE thresholds; fronting prohibition (s13F — criminal offence); trickle-down effect on private sector; exclusivity clause analysis through competition lens; public sector contracting (performance security, penalty at prime rate, B-BBEE scoring 80/20 and 90/10) |
| 5 | `confidentiality-and-restraint.md` | nda-review, vendor-agreement-review | NDA enforceability under SA common law; restraint of trade doctrine (Magna Alloys v Ellis — presumed valid, onus on party seeking escape); Basson v Chilwan 5-part reasonableness test (protectable interest, prejudice, proportionality, public policy, necessity — 5th limb from Kwik Kopy v van Haarlem); SA interdict procedures (interim vs final, Webster v Mitchell urgency); Beadica — Constitutional Court on pacta sunt servanda subject to public policy; typical court-upheld durations (3-4 months); non-compete/non-solicit in commercial context; POPIA interaction when NDA covers personal info |
| 6 | `dispute-resolution.md` | vendor-agreement-review, saas-msa-review, nda-review | SA governing law conventions; AFSA arbitration (domestic — typical 12-18 weeks); International Arbitration Act 15 of 2017 (cross-border); Arbitration Act 42 of 1965 (domestic); High Court jurisdiction and divisions (Johannesburg trial dates extending to 2027 — arbitration increasingly preferred); SCA reaffirmed binding nature of arbitration clauses (2025); Prescription Act 68 of 1969; SA attitude to foreign governing law (mandatory SA law — CPA, POPIA, Competition Act — applies regardless of contractual choice for SA-connected transactions); enforcement of foreign judgments |

**Topic-to-skill matrix:**

| Topic | vendor-agreement-review | saas-msa-review | nda-review |
|---|---|---|---|
| contract-fundamentals | Yes | Yes | Yes |
| liability-and-penalties | Yes | Yes | — |
| data-protection | Yes | Yes | Yes |
| competition-and-bbbee | Yes | Yes | — |
| confidentiality-and-restraint | Yes | — | Yes |
| dispute-resolution | Yes | Yes | Yes |

---

## 4. Practice Profile Template Design

### Section replacement table

| US template section | ZA treatment | What changes |
|---|---|---|
| Who we are | Keep + extend | Add: CIPC registration number, B-BBEE status level, provinces of operation |
| Who's using this | Keep + extend | Add: admitted attorney / candidate attorney / non-lawyer (SA Legal Practice Act) |
| Available integrations | Keep as-is | Jurisdiction-neutral |
| Playbook → Governing law | Replace | SA law + AFSA arbitration + High Court division (not Delaware/NY/CA) |
| Playbook → Data protection | Replace | POPIA operator agreement s21 / responsible party / operator / cross-border s72 (not GDPR DPA / controller / processor) |
| Playbook → Liability | Extend | Add: Conventional Penalties Act, CPA s51, specific performance awareness |
| Playbook → Term & termination | Extend | Add: CPA s14 applicability, 20 business days' notice, month-to-month continuation |
| Escalation | Keep + extend | Add: B-BBEE compliance as automatic escalation trigger |
| House style | Keep as-is | Jurisdiction-neutral |
| Outputs → Work-product header | Replace | SA privilege header (see below) |
| NDA triage preferences | Keep as-is | Playbook-driven structure |
| Decision posture | Keep as-is | Jurisdiction-neutral |
| Shared guardrails | Keep as-is | Already has jurisdiction-recognition section |
| Matter workspaces | Keep as-is | Jurisdiction-neutral |

### New sections (no US equivalent)

| # | Section | Purpose |
|---|---|---|
| 1 | SA statutory baseline | Router instruction: "After loading context, read `jurisdictions/za/commercial-legal/router.md` and load the listed overlays for this skill." |
| 2 | B-BBEE compliance posture | B-BBEE level (1-8/EME/QSE), procurement requirements, fronting awareness, vendor B-BBEE certificate review |
| 3 | CPA applicability | Counterparty threshold assessment framework. Below R2m = CPA overlay activates. |
| 4 | SA contract fundamentals | Key divergences: specific performance, Conventional Penalties Act, Shifren principle, exceptio non adimpleti contractus, prescription periods. Pointers to topic overlays. |

### Work-product header (SA formulation)

**If Role is Lawyer / legal professional:**

```
PRIVILEGED & CONFIDENTIAL — LEGAL PROFESSIONAL PRIVILEGE

[Note: SA legal professional privilege is narrower than US attorney-client privilege
+ work product combined. In-house counsel: this protection applies only when acting
in a legal advisory capacity, not when acting in a commercial/management capacity.
Confirm the applicable privilege regime before relying on this marking to shield the
document from disclosure.]
```

**If Role is Non-lawyer:**

```
RESEARCH NOTES — NOT LEGAL ADVICE — REVIEW WITH AN ADMITTED ATTORNEY OR
ADVOCATE BEFORE ACTING
```

### Seed documents for cold-start

| # | Document | Why |
|---|---|---|
| 1 | 3-5 recent signed vendor/supplier agreements (SA-governed) | Extract actual playbook positions |
| 2 | 1-2 NDA templates (company's standard form) | Establish NDA triage baseline |
| 3 | Current B-BBEE verification certificate | B-BBEE compliance posture section |
| 4 | POPIA operator agreement template (if exists) | Data protection posture |
| 5 | Escalation matrix / approval authority document | Configure escalation section |
| 6 | Standard terms of business / general conditions | Understand the company's own paper |

---

## 5. Cold-Start Interview Questions

### Must-have (7)

| # | Question | Configures |
|---|---|---|
| 1 | What is your company's current B-BBEE status level? (Level 1-8 / EME / QSE / not verified / exempt) | B-BBEE compliance posture |
| 2 | Are your typical counterparties natural persons, below-threshold juristic persons (under R2m turnover/assets), or above-threshold juristic persons? | CPA applicability |
| 3 | What is your standard governing law and dispute resolution position? (SA law + High Court / SA law + AFSA arbitration / other) | Playbook → Governing law |
| 4 | Do you have a POPIA operator agreement template, or do you typically sign the vendor's data processing terms? When vendors host data outside SA, what's your position on cross-border transfers? | Playbook → Data protection |
| 5 | Do you contract with government or public sector entities? If yes, are B-BBEE scorecard requirements part of your tender responses? | B-BBEE + escalation |
| 6 | Do you regularly contract with foreign (non-SA) vendors or pay fees/royalties/license fees to non-resident parties? | Exchange control awareness |
| 7 | Is your company VAT-registered? Do your foreign SaaS/service providers charge SA VAT, or do you account for imported services VAT under reverse charge? | VAT posture |

### Nice-to-have (4)

| # | Question | Configures |
|---|---|---|
| 8 | Does your team use penalty clauses (liquidated damages) in your standard contracts? Are you comfortable with counterparties including them? | Conventional Penalties Act posture |
| 9 | What is your typical contract term for vendor/SaaS agreements? Do you accept multi-year lock-ins? | Playbook → Term & termination |
| 10 | Have you had disputes go to arbitration or litigation in the past 2 years? If so, AFSA, High Court, or other? | Dispute resolution |
| 11 | Do you have specific sectors or industries where you won't do business, or where you require enhanced due diligence? | Escalation triggers |

### Fork structure

ZA fork inserts after Part 0 (company profile) when jurisdiction = ZA. 7 must-have questions are asked in Part 0.5. Nice-to-haves fold into Part 2 (playbook) naturally: Q8 during liability, Q9 during term & termination, Q10 during governing law, Q11 during escalation.

---

## 6. High-Risk Flag Table

| # | Flag | Why it's high-risk | What to check | Statutes |
|---|---|---|---|---|
| 1 | **No POPIA operator agreement** | Vendor processes personal data without written operator agreement per s21. Information Regulator actively enforcing (R100k-R5m fines). Absence is itself a contravention. | Does vendor process personal data? Written operator agreement? Security measures (s19), processing-only-on-instruction, breach notification (s22), sub-operator flow-down? | POPIA s19, s21, s22 |
| 2 | **Cross-border data transfer without safeguards** | Personal data leaving SA without s72 protection. No adequacy list from Information Regulator — contractual protection is the practical default. | Where is data hosted? Data transfer agreement? GDPR SCCs adapted for POPIA? | POPIA s72 |
| 3 | **Penalty-damages cumulation trap** | Contract has penalty clause + damages claim for same breach without express cumulation permission. Conventional Penalties Act s2 bars both. Most US-drafted agreements don't account for this. | Penalty clause present? Damages clause for same breach? Express permission for both? | Conventional Penalties Act s1, s2 |
| 4 | **Foreign governing law + exchange control blind spot** | Non-SA vendor, foreign governing law, foreign currency payment. Cross-border payments require Authorised Dealer routing. Related-party fees must be arm's length. | Counterparty non-SA? Foreign currency? Exchange control acknowledged? Arm's length? | Exchange Control Regulations |
| 5 | **CPA-covered agreement with non-compliant terms** | Counterparty is natural person or below-threshold juristic person (<R2m). Contract violates CPA requirements. | CPA-covered? Fixed term >24 months? Plain language? Unfair terms? Gross negligence exclusion (void under s51)? | CPA s14, s22, s48, s51 |
| 6 | **Overbroad restraint of trade** | Non-compete/non-solicit/exclusivity may fail Basson v Chilwan 5-part test. Presumed valid but courts routinely strike down overbroad restraints. | Duration, geographic scope, restricted activity scope, protectable interest identified, proportionality. Courts typically uphold 3-4 months. | Common law (Basson v Chilwan, Magna Alloys v Ellis) |
| 7 | **B-BBEE fronting indicators** | Contract relies on B-BBEE status that may constitute fronting (s13F — criminal offence since 2013 amendment). Contracts awarded on false B-BBEE info can be cancelled. | B-BBEE certificate verified? Black persons substantially participating? Economic benefits flowing correctly? Terms arm's length? | B-BBEE Act s13F |
| 8 | **Missing or defective non-variation clause** | No Shifren clause means oral agreements can modify the contract. A clause that doesn't entrench itself is ineffective. | Non-variation clause present? Self-entrenching? History of oral variations? | Common law (Shifren principle) |
| 9 | **Uncapped liability + specific performance exposure** | US-style uncapped liability is more dangerous in SA: specific performance is primary remedy (court compels performance AND payment). CPA s51 prohibits excluding supplier gross negligence. | Liability capped? Carve-outs defined? Specific performance excluded? CPA applicable? | Common law + CPA s51 |
| 10 | **Auto-renewal without proper notice mechanics** | CPA-covered: supplier must notify 40-80 business days before expiry (s14). Non-CPA: SA courts increasingly hostile to silent auto-renewals. Johannesburg High Court delays (trial dates to 2027) make prevention critical. | CPA-covered? s14 notice windows? Calendar-based cancel-by deadline? Renewal term reasonable? | CPA s14 |
| 11 | **VAT on imported services misconfigured** | Foreign SaaS vendor VAT treatment incorrect. B2B exclusion only applies if vendor supplies solely to SA VAT-registered vendors (one non-registered customer kills it). Rate 15.5% (May 2025), 16% (April 2026). | Foreign vendor? SA VAT-registered? B2B exclusion valid? Correct rate? | VAT Act, Electronic Services Regs (2025) |
| 12 | **Prescription period mismatch** | Claims limitation period shorter than Prescription Act periods. Unconscionably short limitations may be unenforceable (Barkhuizen v Napier — Constitutional Court). | Limitation period specified? Comparison to Prescription Act? Reasonable in context? Runs from discovery or breach? | Prescription Act s11, s12 |

---

## 7. Eval Case Outlines

### vendor-agreement-review (4 cases)

**Case 1 — Happy path:** SA vendor agreement, two above-threshold juristic persons, SA governing law, AFSA arbitration, liability capped at 12 months' fees, penalty clause with express cumulation, POPIA operator agreement attached, Shifren clause.
- Expected flags: none critical
- Expected statutes: Conventional Penalties Act, POPIA s21
- Must NOT contain: FMLA, FLSA, at-will, EEOC, UCC, FRCP 26(b)(3), "data controller", "data processor", "attorney work product"

**Case 2 — Foreign vendor, multiple flags:** US SaaS vendor, Delaware governing law, USD payment, no POPIA operator agreement, uncapped liability, penalty + damages without express cumulation, data hosted in US.
- Expected flags: #1, #2, #3, #4, #9, #11
- Expected statutes: POPIA s21/s72, Conventional Penalties Act s2, Exchange Control Regs, VAT Act
- Must NOT contain: "data processor", "attorney work product", "Hadley v Baxendale"

**Case 3 — CPA-covered counterparty:** Vendor agreement with sole proprietor, 36-month auto-renewing term, complex language, gross negligence excluded, no s49 notice.
- Expected flags: #5, #10
- Expected statutes: CPA s14, s22, s48, s49, s51
- Must NOT contain: UCC, "consideration" as formation requirement, US state consumer protection

**Case 4 — B-BBEE procurement:** Supply to organ of state, B-BBEE Level 4 minimum required, vendor provides Level 3 certificate, exclusivity clause restricting supplier.
- Expected flags: #7, Competition Act s5
- Expected statutes: B-BBEE Act s10/s13F, Competition Act s5
- Must NOT contain: FAR, DFARS, US government contracting terminology

### saas-msa-review (4 cases)

**Case 1 — Happy path:** SA SaaS vendor, annual term, 60-day cancel notice, POPIA operator agreement, data in SA, SA governing law, AFSA, CPI-capped escalation.
- Expected flags: minimal
- Expected statutes: POPIA s21, ECTA s22
- Must NOT contain: "California auto-renewal statute", GDPR terminology, "data controller"

**Case 2 — Foreign vendor, cross-border + VAT:** US SaaS vendor, data in AWS eu-west-1, no POPIA operator agreement, 30-day auto-renewal notice, USD payment, vendor claims B2B VAT exclusion but SA company has non-registered subsidiary using platform.
- Expected flags: #1, #2, #4, #10, #11
- Expected statutes: POPIA s21/s72, Exchange Control Regs, VAT Act Electronic Services Regs
- Must NOT contain: "GDPR Article 46", "Standard Contractual Clauses" without POPIA adaptation, "data processor"

**Case 3 — CPA threshold boundary:** SaaS to startup (R1.8m turnover), 30-month term, uncapped price escalation, unilateral amendment clause.
- Expected flags: #5, #10
- Expected statutes: CPA s14, s22, s48, s51
- Must NOT contain: US state auto-renewal statutes, "unconscionability" in US sense

**Case 4 — Penalty clause in SLA:** SLA with service credits as penalty for downtime + separate damages clause for data loss from same event, no express cumulation.
- Expected flags: #3
- Expected statutes: Conventional Penalties Act s1/s2/s3
- Must NOT contain: "liquidated damages" in US sense

### nda-review (3 cases)

**Case 1 — GREEN happy path:** Mutual NDA, two SA companies, 2-year term, 2-year survival, standard carve-outs, SA governing law, no embedded restrictive covenants, electronically signed.
- Expected: GREEN
- Expected statutes: Common law, ECTA s13
- Must NOT contain: "preliminary injunction" (use "interdict"), "consideration", "attorney work product"

**Case 2 — Embedded restraint, auto-YELLOW:** One-way NDA with 2-year worldwide non-compete and non-solicit, receiving party is 15-person technology firm, no protectable interest identified.
- Expected: auto-YELLOW, flag #6
- Expected statutes: Common law (Basson v Chilwan, Magna Alloys, Kwik Kopy)
- Must NOT contain: "non-compete per se invalid", "blue pencil doctrine"

**Case 3 — Personal data in scope:** NDA for due diligence covering employee records, no POPIA compliance clause, no operator agreement.
- Expected: YELLOW, flag #1
- Expected statutes: POPIA s21, s19, s22
- Must NOT contain: "HIPAA", "PII", "PHI"

### cold-start-interview (3 cases)

**Case 1 — In-house, domestic-only:** SA in-house team, above-threshold counterparties, SA governing law, B-BBEE Level 4, VAT-registered, no foreign vendors.
- Expected: ZA fork activates, 7 must-have questions, CPA mostly-inapplicable, exchange control N/A, SA privilege header
- Must NOT contain: US state jurisdiction questions, "ATTORNEY WORK PRODUCT"

**Case 2 — Mixed foreign + small business:** SA company contracting with foreign SaaS vendors (USD), below-threshold small business customers.
- Expected: ZA fork activates, exchange control applicable, CPA applicable for small business customers, VAT on imported services flagged
- Must NOT contain: US state-by-state questions, "data processor"

**Case 3 — Private practice, multi-client:** SA law firm, multiple clients, matter workspaces needed.
- Expected: ZA fork activates, matter workspaces enabled, 7 must-have questions, SA privilege header for external counsel
- Must NOT contain: "ATTORNEY WORK PRODUCT", single-client assumptions

### customize (2 cases)

**Case 1 — Update B-BBEE level:** Change Level 4 to Level 2.
- Expected: Shows SA-specific B-BBEE section, allows edit, notes procurement scoring impact
- Must NOT contain: US-only sections as full map

**Case 2 — Change governing law:** Change default from SA to English law for international deals.
- Expected: Updates governing law, flags exchange control still applies, notes SA mandatory law applies regardless
- Must NOT contain: Delaware/NY/CA as defaults

### Terminology must-not-contain (all skills)

| US term | SA replacement |
|---|---|
| "consideration" (as formation requirement) | causa / no equivalent requirement |
| "UCC" | SA common law of contract + CPA |
| "liquidated damages" | "penalty stipulation" (Conventional Penalties Act) |
| "data controller" / "data processor" | "responsible party" / "operator" (POPIA) |
| "attorney work product" | "legal professional privilege" |
| "preliminary injunction" | "interdict" |
| "PII" / "personal data" | "personal information" (POPIA definition) |
| "HIPAA" / "PHI" | Not applicable — use POPIA |
| "FMLA" / "FLSA" / "at-will" / "EEOC" | Not applicable — employment-legal domain |
| "Hadley v Baxendale" | SA damages taxonomy (Lavery v Jungheinrich) |
| "blue pencil doctrine" | SA severability |

### Expert review gate

Before release, an SA commercial law practitioner reviews:
- Statute YAML values against current legislation and Government Gazette
- Topic overlay procedures against current statutes and practice
- High-risk flag table against current Information Regulator enforcement patterns and court decisions
- Practice profile template for completeness and correctness
- Eval cases for realistic fact patterns and correct expected outcomes

---

## 8. Source Provenance Log

| Item | Source | Tag |
|---|---|---|
| CPA s14 fixed-term rules, s48 unfair terms | Perplexity (gov.za, SAFLII, MacRobert attorneys) | [Perplexity — verify] |
| CPA s14 does not apply between juristic persons | Perplexity (MacRobert attorneys newsletter) | [Perplexity — verify] |
| ECTA s13 e-signatures, s22 formation | Perplexity (gov.za, Adobe, Michalsons, DML Law, Brian Kahn) | [Perplexity — verify] |
| POPIA s21 operator agreements, s72 cross-border | Perplexity (IRBA, C-BRTA, CMS Law, popia.co.za) | [Perplexity — verify] |
| POPIA enforcement actions (R5m DBE, R5m DOJ, etc.) | Perplexity (SEESA, Information Regulator media statements, Baker McKenzie) | [Perplexity — verify] |
| Conventional Penalties Act s1-s4 | Perplexity (justice.gov.za, Trans-Lex) | [Perplexity — verify] |
| Competition Act s4/s5 | Perplexity (compcom.co.za, DML Law, Webber Wentzel) | [Perplexity — verify] |
| B-BBEE Act s10, s13F, procurement scoring | Perplexity (DTIC, bbbeecommission.co.za) | [Perplexity — verify] |
| Restraint of trade (Basson v Chilwan, Magna Alloys) | Perplexity (RSM, SAFLII, CEO SA, High Court 2024 judgment) | [Perplexity — verify] |
| Exchange control regulations, Circular 13/2024 | Perplexity (SARB, Webber Wentzel, Deloitte) | [Perplexity — verify] |
| VAT on electronic services (April 2025 reforms) | Perplexity (SARS, vatcalc.com, EY, globalvatcompliance.com) | [Perplexity — verify] |
| VAT rate 15.5% (May 2025), 16% (April 2026) | Perplexity (globalvatcompliance.com, SARS) | [Perplexity — verify] |
| Shifren principle | Model knowledge | [model knowledge — verify] |
| Lavery v Jungheinrich (special damages test) | Perplexity (Cliffe Dekker Hofmeyr May 2025 alert) | [Perplexity — verify] |
| Drax Energy liability cap interpretation | Perplexity (Cliffe Dekker Hofmeyr March 2024 alert) | [Perplexity — verify] |
| Barkhuizen v Napier (limitation period fairness) | Model knowledge | [model knowledge — verify] |
| Specific performance as primary remedy | Model knowledge + Perplexity (Wikipedia, Studocu) | [model knowledge — verify] |
| No consideration doctrine in SA | Model knowledge + Perplexity (Wikipedia SA contract law) | [Perplexity — verify] |
| SA arbitration landscape (trial dates to 2027) | Perplexity (Pinsent Masons March 2026) | [Perplexity — verify] |
| SCA reaffirmed binding arbitration clauses (2025) | Perplexity (Pinsent Masons) | [Perplexity — verify] |
| Prescription Act periods (3yr/6yr) | Model knowledge | [model knowledge — verify] |
| Copyright Act s21/s22 | Model knowledge | [model knowledge — verify] |
| Kwik Kopy v van Haarlem 5th limb | Perplexity (CEO SA, High Court 2024) | [Perplexity — verify] |
| Sub-operator agreement requirement under POPIA | Perplexity (IRBA, C-BRTA agreements) | [Perplexity — verify] |
| No Information Regulator adequacy list | Perplexity (CMS Law) | [Perplexity — verify] |
| Johannesburg High Court delays (trial dates to 2027) | Perplexity (Pinsent Masons, Bowmans) | [Perplexity — verify] |

---

## Implementation Task Sequence

Following the same structure as the employment-legal build:

1. **Statute YAML files** — 8 new files in `jurisdictions/za/statutes/`
2. **Topic overlay markdown files** — 6 files in `jurisdictions/za/commercial-legal/topics/`
3. **Skill router** — `jurisdictions/za/commercial-legal/router.md`
4. **Practice profile template** — `jurisdictions/za/commercial-legal/practice-profile-template.md`
5. **Cold-start interview fork** — Extend existing ZA fork in cold-start-interview SKILL.md
6. **Validation scripts** — Extend existing validators for new statute files, router, template
7. **Scenario eval cases** — 16 cases in `jurisdictions/za/evals/commercial-legal/`
8. **Final validation run** — All validators pass, expert review gate documented
