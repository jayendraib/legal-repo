# Cross-Border Transfers and Special Categories — South African Framework

This overlay covers the cross-border transfer regime under POPIA s72 and the special categories of personal information under s26–s35. It is loaded by dpa-review, pia-generation, and use-case-triage skills when jurisdiction = ZA.

**Terminology requirement:** When jurisdiction = ZA, use POPIA terminology exclusively.

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
| adequacy decision | [no POPIA equivalent — IR has not published an adequacy list] |
| Article [N] | [do not reference GDPR articles — cite POPIA sections] |
| CCPA / CPRA / state privacy law | [do not reference US privacy laws] |

---

## 1. Statutory framework

### Cross-border transfer regime

POPIA s72 restricts the transfer of personal information to third parties in foreign countries. Unlike GDPR, which relies on an adequacy decision framework administered by the European Commission, POPIA's cross-border provisions operate without a published adequacy list, placing the compliance burden squarely on the responsible party.

### Special categories regime

POPIA s26–s35 prohibits the processing of special personal information (s26–s33) and children's personal information (s34–s35) unless specific exceptions apply. When special PI or children's PI is transferred cross-border, the two regimes interact — triggering both s72 transfer safeguards and s57(1)(d) prior authorisation.

### Key provisions

| Provision | Reference | Effect |
|---|---|---|
| Cross-border transfer restriction | POPIA s72(1) | A responsible party may not transfer PI to a foreign country unless the recipient is subject to adequate protection |
| 5 permitted grounds | POPIA s72(1)(a)–(e) | Specific grounds permitting transfer |
| Prior authorisation for special PI/children's PI transfer | POPIA s57(1)(d) | Transfer of special PI or children's PI to inadequate country requires prior authorisation from the IR |
| Special PI prohibition | POPIA s26 | Processing of special PI prohibited unless s27 exception applies |
| Children's PI prohibition | POPIA s34 | Processing of children's PI prohibited unless s35 exception applies |

---

## 2. Cross-border transfer — s72 framework

### The 5 permitted grounds

A responsible party may transfer personal information to a third party in a foreign country **only if** one of the following grounds is met:

#### s72(1)(a) — Adequate law, binding corporate rules, or binding agreement

The third party who is the recipient of the information is subject to:

| Mechanism | Description | Practical application |
|---|---|---|
| **Adequate law** | A law, binding corporate rules, or binding agreement that provides an adequate level of protection substantially similar to POPIA | No adequacy list published by the IR — cannot assume any country has "adequate" law |
| **Binding corporate rules** | Intra-group rules binding all members of a corporate group to equivalent standards | Suitable for multinational groups; must demonstrate binding nature and enforceability |
| **Binding agreement** | A contractual agreement between the responsible party and the recipient providing adequate protection | Most common mechanism — adapted from GDPR SCCs but referencing POPIA provisions |

#### s72(1)(b) — Data subject consent

The data subject **consents** to the transfer.

- Consent must be voluntary, specific, and informed
- The data subject must be told specifically that PI will be transferred to a foreign country and that the level of protection may differ
- Not practical for large-scale commercial transfers

#### s72(1)(c) — Contractual necessity with data subject

The transfer is **necessary for the performance of a contract** between the data subject and the responsible party.

- E.g., booking a hotel in a foreign country requires transferring the data subject's PI to the hotel
- Must be genuinely necessary — convenience does not satisfy this test

#### s72(1)(d) — Contract in interest of data subject

The transfer is **necessary for the conclusion or performance of a contract** concluded in the interest of the data subject between the responsible party and a third party.

- E.g., insurance claim processing through an international reinsurer
- The contract must be in the data subject's interest, not merely the responsible party's

#### s72(1)(e) — Benefit of data subject where consent impracticable

The transfer is for the **benefit of the data subject** and it is not reasonably practicable to obtain the consent of the data subject, and if it were reasonably practicable, the data subject would be likely to give consent.

- Emergency situations — e.g., transferring medical records to a foreign hospital for emergency treatment
- High threshold — must demonstrate impracticability of obtaining consent

### No adequacy list

As of 2025/26, the Information Regulator has **not published an adequacy list** of countries deemed to provide an adequate level of protection. This has significant practical consequences:

| Consequence | Impact |
|---|---|
| No safe harbour | No country can be assumed to provide adequate protection for purposes of s72(1)(a) |
| Binding agreement required for every transfer | Unless another s72 ground applies, each transfer must be covered by a binding agreement |
| Higher compliance burden | SA responsible parties face a more onerous regime than GDPR (which has ~15 adequacy decisions) |
| Uncertainty | Responsible parties must make their own adequacy assessments — with no IR guidance on methodology |

### IR Guidance Note — expected 2025/26

The Information Regulator has indicated it will issue a Guidance Note on cross-border transfers, potentially triggered by the AfCFTA (African Continental Free Trade Area) Digital Trade Protocol. The guidance is expected to address:

- Adequacy assessment methodology
- Binding agreement minimum terms
- Specific cross-border scenarios (cloud hosting, remote access, third-party data sharing)
- Interaction between s72 and s57(1)(d) for special PI transfers

Until this guidance is issued, responsible parties should apply the precautionary approach and ensure binding agreements are in place for all cross-border transfers.

---

## 3. Practical mechanisms for cross-border compliance

### Mechanism 1 — Binding agreement (adapted from GDPR SCCs)

The most common approach in SA practice is to adapt GDPR Standard Contractual Clauses into a POPIA-compliant binding agreement:

| SCC element | POPIA adaptation |
|---|---|
| References to GDPR articles | Replace with POPIA section references |
| "Controller/processor" terminology | Replace with "responsible party/operator" |
| "Supervisory authority" | Replace with "Information Regulator" |
| "DPO" | Replace with "Information Officer" |
| Art 28 processor obligations | Map to s21 operator obligations |
| Art 32 security measures | Map to s19 security safeguards |
| Art 33 breach notification (72 hours) | Map to s22 ("as soon as reasonably possible") |
| Data subject rights (Arts 15–22) | Map to s23 (access), s24 (correction), s11(3) (objection) — omit portability |
| Adequacy assessment reference | Note absence of IR adequacy list; responsible party's own assessment |
| Governing law | South African law governs the POPIA obligations |
| Jurisdiction | South African courts or IR for POPIA disputes |

**Important:** Do not simply append a POPIA reference to an unmodified GDPR SCC. The binding agreement must substantively reflect POPIA's framework, not merely cross-reference it.

### Mechanism 2 — Binding corporate rules (BCRs)

For multinational groups with SA subsidiaries or branches:

| Element | Requirement |
|---|---|
| Scope | Must cover all group entities processing SA PI |
| Binding nature | Must be legally binding on all group entities — not advisory guidelines |
| Enforceability | Must be enforceable by data subjects as third-party beneficiaries |
| Content | Must address all 8 POPIA conditions, s72 obligations, s22 breach notification |
| IO integration | SA IO must have oversight of group compliance as it affects SA PI |
| Review | Regular review and update to reflect POPIA regulatory developments |

### Mechanism 3 — Consent

For specific, limited transfers where consent is appropriate:

| Requirement | Detail |
|---|---|
| Voluntary | Not coerced or bundled with unrelated consent |
| Specific | Identifies the recipient country, recipient entity, and purpose of transfer |
| Informed | Data subject is told that the foreign country may not provide equivalent protection |
| Recorded | Evidence of consent retained |
| Withdrawable | Data subject can withdraw consent, and further transfers must cease |

### Mechanism 4 — Contract schedule

An efficient approach is to include the s72 binding agreement as a schedule to the s21 operator agreement:

- Schedule 1: s21 operator obligations
- Schedule 2: s72 binding agreement for cross-border transfer
- Schedule 3: Technical and organisational measures (s19)

This consolidates all data protection obligations in one document.

---

## 4. Cloud storage and cross-border transfer

### When cloud storage constitutes a cross-border transfer

| Scenario | Cross-border transfer? | Action required |
|---|---|---|
| Cloud provider with SA data centre, data stored exclusively in SA | **No** (provided no replication or access from outside SA) | Verify data residency in operator agreement |
| Cloud provider with SA data centre, data replicated to other regions | **Yes** — each replication location constitutes a transfer | s72 binding agreement for each region |
| Cloud provider without SA data centre | **Yes** | s72 binding agreement required |
| Cloud provider's support staff access data from outside SA | **Potentially yes** — access from a foreign country may constitute a transfer | Assess access model, restrict if possible, include in binding agreement |
| Backup and disaster recovery in foreign data centre | **Yes** | Include in s72 assessment and binding agreement |
| SaaS provider processes data on foreign servers | **Yes** | s72 binding agreement required |

### National Data and Cloud Policy (May 2024)

The South African National Data and Cloud Policy (Cabinet approved, May 2024) introduces additional requirements for government data:

| Requirement | Detail |
|---|---|
| Data sovereignty | Government data with national security content must be stored in South Africa |
| Data residency | Government departments must assess whether cloud services store data in SA |
| Procurement | Cloud procurement must include data residency requirements |
| Scope | Applies to government departments and public entities — not directly to the private sector, but influences tender requirements |

**Practical implication for private sector:** Private companies contracting with government departments should expect data residency requirements in government tenders. Non-compliance may disqualify a tender bid.

---

## 5. Unique SA consideration — juristic person coverage

POPIA's definition of "data subject" includes **juristic persons** (companies, close corporations, trusts, partnerships). This creates a unique cross-border challenge:

| Issue | Impact |
|---|---|
| Most foreign laws do not protect juristic persons | GDPR, UK GDPR, LGPD, PIPA — all protect natural persons only |
| Adequacy gap | Even if a foreign country's law provides adequate protection for natural persons, it may not protect juristic persons |
| Binding agreement must cover juristic persons | When adapting SCCs or creating binding agreements, the protections must extend to juristic person PI |
| B2B data transfers | Commercial data (company financials, business contact details, corporate communications) may constitute PI of a juristic person under POPIA |
| Per-entity assessment | Each foreign recipient must be assessed for whether its data protection law covers juristic persons |

### Practical guidance

When assessing cross-border transfers involving juristic person PI:

1. Identify whether the foreign recipient's law protects juristic persons — if not, "adequate law" under s72(1)(a) may not be established for that PI
2. Ensure the binding agreement explicitly extends protections to juristic person PI
3. Document the adequacy gap and the contractual mitigation

---

## 6. Special personal information (s26–s33)

### General prohibition

POPIA s26 provides a general prohibition: **no person may process special personal information** except as provided by s27 (general exceptions) and s28–s33 (category-specific exceptions).

### Categories with specific authorisation provisions

| Category | POPIA section | Category-specific exceptions |
|---|---|---|
| **Religious or philosophical beliefs** | s28 | Processing by religious/philosophical bodies for their members or persons regularly in contact with the body; by institutions based on those beliefs for employees/students/members; for social welfare, spiritual care, or pastoral activities; where necessary for a right or obligation in law |
| **Race or ethnic origin** | s29 | Processing to identify a data subject, to comply with legislation, or to counter discrimination (e.g., employment equity reporting) |
| **Trade union membership** | s30 | Processing by trade unions for their members; by employers for trade union contribution deductions or for trade union activities |
| **Political persuasion** | s31 | Processing by political parties for their members; for opinion surveys where PI is subsequently anonymised |
| **Health or sex life** | s32 | Processing by medical/healthcare professionals for treatment; by insurance companies for assessment of risk; for compliance with occupational health obligations; for public health emergencies; for research with adequate safeguards |
| **Criminal behaviour** | s33(1) | Processing by the body responsible for the alleged criminal behaviour; under control of bodies charged with enforcing law; for credit bureau purposes (s57(1)(c) prior authorisation required for credit reporting) |
| **Biometric information** | s33(2) | Processing for identification or security purposes, provided the biometric information is processed in a way that uniquely identifies the data subject |

### General exceptions (s27(1))

The general prohibition on special PI processing does not apply where:

| # | Exception | s27(1) reference | Application |
|---|---|---|---|
| 1 | Consent | s27(1)(a) | The data subject (or competent person for a child) has given consent |
| 2 | Legal obligation/right | s27(1)(b) | Processing is necessary for establishing, exercising, or defending a right or obligation in law |
| 3 | International public law | s27(1)(c) | Necessary for compliance with an international public law obligation |
| 4 | Historical/statistical/research | s27(1)(d) | With adequate safeguards against re-identification |
| 5 | Deliberately made public | s27(1)(e) | The data subject has deliberately made the information public |
| 6 | Specific section compliance | s27(1)(f) | Necessary for compliance with the specific exceptions in s28–s33 |

### Assessment framework for special PI processing

When evaluating whether special PI processing is permitted:

1. **Identify the category** — which s26 category does the PI fall into?
2. **Check general exceptions (s27)** — does any s27(1) exception apply?
3. **Check category-specific exceptions (s28–s33)** — does the specific section provide an exception?
4. **Check cross-border implications** — if the special PI will be transferred to a foreign country without adequate protection, s57(1)(d) prior authorisation is required
5. **Check third-party processing** — if the special PI will be processed by an operator, the s21 agreement must specifically address special PI
6. **Document the basis** — record which exception applies and the supporting evidence

---

## 7. Children's personal information (s34–s35)

### Definition

A **child** under POPIA is a natural person under the age of 18 years who is not legally competent without the assistance of a competent person (parent or guardian) as defined in the Children's Act 38 of 2005.

### Processing restrictions

| Rule | POPIA reference | Detail |
|---|---|---|
| General prohibition | s34(1) | Processing children's PI is prohibited |
| Competent person consent | s35(1)(a) | A competent person must consent on behalf of the child |
| Best interests | s35(1) read with Children's Act | Processing must be in the best interests of the child |
| Capacity to consent | s35(2) | A child who has capacity and is sufficiently mature may consent independently — assessed case by case |

### s35 exceptions to the prohibition

| Exception | s35 reference | Application |
|---|---|---|
| Competent person consent | s35(1)(a) | Parent or guardian consents |
| Necessary to establish/exercise/defend right or obligation in law | s35(1)(b) | Legal proceedings, statutory obligations |
| Necessary for compliance with international public law | s35(1)(c) | International obligations |
| Historical/statistical/research with adequate safeguards | s35(1)(d) | Research use with de-identification |
| Deliberately made public by child | s35(1)(e) | Child has made PI public — rare |
| Processing relates to PI of parent/guardian and necessary for function | s35(2) | Administrative processing of family data |

### Cross-border transfer of children's PI

When children's PI is transferred to a foreign country without adequate protection:

1. **s72 applies** — all general cross-border transfer requirements must be met
2. **s57(1)(d) applies** — prior authorisation from the IR is **mandatory**
3. **Double protection** — children's PI requires both the cross-border safeguard and the prior authorisation

### DBE precedent

The Department of Basic Education (DBE) case is the leading enforcement precedent on children's PI:

| Aspect | Detail |
|---|---|
| **Facts** | DBE published matric examination results in newspapers |
| **PI involved** | Names, ID numbers, examination results of children (matriculants under 18) |
| **IR finding** | Processing children's PI without adequate safeguards, wide publication amplified privacy impact |
| **Outcome** | R5M fine — among the largest IR fines issued |
| **Status** | Supreme Court appeal pending as of 2025/26 — fine has not been set aside |
| **Significance** | Established that even routine government functions must comply with children's PI protections |

---

## 8. Interaction between cross-border and special categories

### When both regimes apply

The s72 cross-border regime and the s26–s35 special categories regime interact in the following scenarios:

| Scenario | s72 requirement | Special category/children requirement | Prior authorisation |
|---|---|---|---|
| Special PI transferred to adequate country | s72(1)(a) — binding agreement, BCRs, or adequate law | s27 exception must apply | **Not required** — s57(1)(d) only applies to inadequate countries |
| Special PI transferred to inadequate country | s72(1)(a)–(e) — one ground must be met | s27 exception must apply | **Required** — s57(1)(d) mandatory |
| Children's PI transferred to adequate country | s72(1)(a) — binding agreement, BCRs, or adequate law | s35 exception must apply (competent person consent) | **Not required** |
| Children's PI transferred to inadequate country | s72(1)(a)–(e) — one ground must be met | s35 exception must apply (competent person consent) | **Required** — s57(1)(d) mandatory |
| General PI transferred to any country | s72(1)(a)–(e) — one ground must be met | N/A | Not required (unless s57(1)(a)–(c) trigger applies) |

### Assessment checklist — cross-border transfer involving special PI or children's PI

| Step | Action | Reference |
|---|---|---|
| 1 | Identify the special PI category or confirm children's PI | s26–s33 (special), s34 (children) |
| 2 | Confirm a s27 exception (special PI) or s35 exception (children's PI) exists | s27, s35 |
| 3 | Identify the recipient country | — |
| 4 | Assess whether the recipient country provides adequate protection | s72(1)(a) — no adequacy list exists, so own assessment required |
| 5 | If inadequate country: determine s72 ground for transfer | s72(1)(a)–(e) |
| 6 | If inadequate country: prepare and submit s57(1)(d) prior authorisation application | s57, s58, s59 |
| 7 | Do not commence transfer until prior authorisation received | s59 — failure is a criminal offence |
| 8 | Include cross-border provisions in operator agreement (if operator involved) | s21, s72 |
| 9 | Document assessment and retain for compliance evidence | s8 accountability |

---

## 9. Transfer register

Responsible parties should maintain a **cross-border transfer register** documenting all transfers of PI outside South Africa:

| Field | Detail |
|---|---|
| Recipient entity | Name and country of the recipient |
| Recipient status | Responsible party, operator, or other third party |
| PI categories | General PI, special PI (which category), children's PI |
| Data subjects | Categories (employees, customers, suppliers) and approximate volumes |
| Purpose | Why the transfer occurs |
| s72 ground | Which s72(1) ground applies |
| Safeguard mechanism | Binding agreement, BCRs, consent, contractual necessity, benefit |
| Prior authorisation | Required (s57(1)(d))? Applied for? Received? |
| Date of last review | When the transfer was last assessed for compliance |

---

## 10. High-risk flags

| # | Flag | Statute | What to check | Enforcement precedent |
|---|---|---|---|---|
| 1 | Cross-border transfer without safeguards | POPIA s72 | Is PI being transferred to a foreign country? Which s72 ground applies? Is a binding agreement in place? | No enforcement yet — IR guidance note expected 2025/26 |
| 2 | Special PI transfer to inadequate country without prior authorisation | POPIA s57(1)(d), s59 | Is special PI (s26–s33) or children's PI (s34–s35) being transferred to a country without adequate protection? Has prior authorisation been obtained from the IR? | s59 makes failure a criminal offence — fine up to R10M or 12 months imprisonment |
| 3 | Children's PI without competent person consent | POPIA s34–s35 | Is the data subject under 18? Has a competent person consented? Is the processing in the child's best interests? | DBE matric results (R5M fine) |
| 4 | Special PI without authorisation | POPIA s26–s33, s27 | Which special PI category? Which s27 exception applies? Is third-party processing or cross-border triggering s57? | IR Guidance Note on special PI issued |
| 5 | Cloud storage in foreign jurisdiction without s72 assessment | POPIA s72 | Where is PI hosted? Is replication occurring across regions? Do support staff access from outside SA? | Common compliance gap — especially with global SaaS providers |
| 6 | Binding agreement uses unmodified GDPR SCCs | POPIA s72(1)(a) | Does the agreement reference POPIA provisions? Does it cover juristic persons? Does it use POPIA terminology? | Unmodified SCCs may not satisfy s72(1)(a) "adequate" standard |
| 7 | Juristic person PI not covered in cross-border safeguards | POPIA s1 (data subject definition), s72 | Does the binding agreement extend protections to juristic person PI? Does the foreign law protect juristic persons? | Unique SA gap — no enforcement yet, but potential exposure |
| 8 | Government data stored outside SA without authority | National Data and Cloud Policy (2024) | Is government data with national security content hosted outside South Africa? | Policy compliance — affects government tender eligibility |
