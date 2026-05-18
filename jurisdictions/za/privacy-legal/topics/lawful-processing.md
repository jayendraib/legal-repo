# Lawful Processing — South African Framework

This overlay covers the conditions for lawful processing of personal information under the Protection of Personal Information Act 4 of 2013 (POPIA), including the 8 conditions framework, lawful bases under s11, and direct marketing requirements. It is loaded by pia-generation, use-case-triage, dpa-review, reg-gap-analysis, and policy-monitor skills when jurisdiction = ZA.

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
| Article [N] | [do not reference GDPR articles — cite POPIA sections] |
| CCPA / CPRA / state privacy law | [do not reference US privacy laws] |

---

## 1. Statutory framework

POPIA establishes **8 conditions for the lawful processing** of personal information (s4 read with Chapter 3). These conditions apply to all processing by responsible parties and, through the operator agreement mechanism (s21), to operators.

### The 8 conditions — overview

| # | Condition | POPIA reference | Core requirement |
|---|---|---|---|
| 1 | Accountability | s8 | The responsible party must ensure compliance with all conditions and is responsible for demonstrating compliance |
| 2 | Processing limitation | s9–s12 | Processing must be lawful, minimised to what is necessary, and based on a valid lawful basis |
| 3 | Purpose specification | s13–s14 | PI must be collected for a specific, explicitly defined, and lawful purpose, and not retained beyond necessity |
| 4 | Further processing limitation | s15 | Secondary processing must be compatible with the original purpose, unless an exception applies |
| 5 | Information quality | s16 | PI must be complete, accurate, not misleading, and updated where necessary |
| 6 | Openness | s17–s18 | The responsible party must notify the IR and inform data subjects at collection |
| 7 | Security safeguards | s19–s22 | Appropriate, reasonable technical and organisational measures must be in place |
| 8 | Data subject participation | s23–s25 | Data subjects must be able to access, correct, and delete their PI |

---

## 2. Condition 1 — Accountability (s8)

### The s8 obligation

The responsible party must ensure that the conditions set out in Chapter 3, and all measures that give effect to those conditions, are complied with at the time of the determination of the purpose and means of the processing **and during the processing itself**.

### What accountability means in practice

| Requirement | Practical implementation |
|---|---|
| Demonstrate compliance | Maintain records showing how each condition is met |
| Information Officer | Designate and register an IO with the IR (s55–s56) |
| Compliance framework | Develop, implement, and maintain a POPIA compliance framework |
| Continuous improvement | April 2025 amended regulations require the compliance framework to be "continuously improved" |
| PI impact assessment | Conduct assessments for high-risk processing (recommended, not mandatory) |
| Training | Ensure all persons processing PI on behalf of the responsible party understand their obligations |

### April 2025 regulation amendments — continuous improvement

The amended regulations introduced the requirement that the responsible party's compliance framework must be **continuously improved**. This means:

- A framework created at POPIA commencement (2021) and never updated is insufficient
- Regular review cycles must be documented (annually at minimum)
- The framework must be updated to reflect new regulatory guidance, enforcement precedent, and operational changes
- The IO must report to the head of the responsible party on compliance status

---

## 3. Condition 2 — Processing limitation (s9–s12)

### s9 — Lawfulness of processing

Personal information must be processed:

1. **Lawfully** — in compliance with POPIA and any other applicable legislation
2. **In a reasonable manner** — that does not infringe the data subject's privacy

### s10 — Minimality

Personal information may only be processed if, given the purpose for which it is processed, it is **adequate, relevant, and not excessive**.

### s11 — Lawful bases for processing

POPIA s11 provides six lawful bases for processing personal information. At least one must apply:

| Basis | POPIA reference | Description |
|---|---|---|
| **Consent** | s11(1)(a) | The data subject (or a competent person where the data subject is a child) consents to the processing |
| **Contract** | s11(1)(b) | Processing is necessary to carry out actions for the conclusion or performance of a contract to which the data subject is a party |
| **Legal obligation** | s11(1)(c) | Processing is necessary for compliance with an obligation imposed by law on the responsible party |
| **Legitimate interest of data subject** | s11(1)(d) | Processing is necessary to protect a legitimate interest of the data subject |
| **Public law duty** | s11(1)(e) | Processing is necessary for the proper performance of a public law duty by a public body |
| **Legitimate interest of responsible party or third party** | s11(1)(f) | Processing is necessary for pursuing the legitimate interests of the responsible party or a third party to whom the information is supplied |

### Key differences from GDPR Art 6 bases

| GDPR Art 6 basis | POPIA s11 equivalent | Key difference |
|---|---|---|
| Consent (Art 6(1)(a)) | s11(1)(a) | Similar — but POPIA does not elevate consent above other bases |
| Performance of contract (Art 6(1)(b)) | s11(1)(b) | Similar |
| Legal obligation (Art 6(1)(c)) | s11(1)(c) | Similar |
| Vital interests (Art 6(1)(d)) | s11(1)(d) | POPIA uses "legitimate interest of data subject" — broader than "vital interests" |
| Public interest / official authority (Art 6(1)(e)) | s11(1)(e) | POPIA: "public law duty by a public body" — narrower (public bodies only) |
| Legitimate interests (Art 6(1)(f)) | s11(1)(f) | Similar — but POPIA does not require a formal balancing test. The responsible party must still consider the data subject's rights and interests |

### s11 — consent requirements

When relying on consent (s11(1)(a)):

1. **Voluntary** — consent must be freely given, without coercion or undue influence
2. **Specific** — consent must relate to a specific, defined purpose
3. **Informed** — the data subject must understand what they are consenting to
4. **Recorded** — the responsible party must be able to demonstrate that consent was obtained
5. **Withdrawable** — the data subject may withdraw consent at any time (s11(2)(a))
6. **Effect of withdrawal** — withdrawal does not affect the lawfulness of processing before withdrawal (s11(2)(b))

### s12 — Collection directly from data subject

Personal information must be collected directly from the data subject, unless:

1. The information is contained in or derived from a public record (s12(2)(a))
2. The data subject has deliberately made the information public (s12(2)(b))
3. The data subject has consented to collection from another source (s12(2)(c))
4. Collection from another source would not prejudice the data subject's legitimate interest (s12(2)(d))
5. Collection is necessary to maintain the legitimate interest of the responsible party or a third party (s12(2)(e))
6. Compliance with the direct collection requirement would prejudice a lawful purpose of the collection (s12(2)(f))
7. Compliance is not reasonably practicable in the circumstances (s12(2)(g))

---

## 4. Condition 3 — Purpose specification (s13–s14)

### s13 — Collection for specific purpose

Personal information must be collected for a **specific, explicitly defined, and lawful** purpose related to a function or activity of the responsible party.

The responsible party must take reasonably practicable steps to ensure the data subject is aware of the purpose of collection (linked to the s18 openness notification).

### s14 — Retention limitation

Records of personal information must **not be retained** any longer than is necessary for achieving the purpose for which the information was collected or subsequently processed, unless:

| Exception | POPIA reference | Application |
|---|---|---|
| Required or authorised by law | s14(1)(a) | Statutory retention periods (e.g., tax records, financial records, employee records) |
| Reasonably necessary for a lawful purpose | s14(1)(b) | Litigation hold, regulatory investigation |
| Contractual requirement | s14(1)(c) | Contract specifies retention period |
| Data subject has consented | s14(1)(d) | Written consent to extended retention |

When a responsible party is no longer authorised to retain PI, it must:

1. **Destroy or delete** the records as soon as reasonably practicable, or
2. **De-identify** the records so they can no longer be linked to a data subject

---

## 5. Condition 4 — Further processing limitation (s15)

### Compatible purpose test

Further processing of personal information must be compatible with the purpose for which it was collected. When assessing compatibility, consider:

1. The relationship between the original purpose and the further purpose
2. The nature of the information
3. The consequences of the further processing for the data subject
4. The manner in which the information was collected
5. Any contractual rights and obligations between the parties

### s15(3) exceptions — further processing is always compatible where:

| Exception | POPIA reference | Application |
|---|---|---|
| Data subject consent | s15(3)(a) | Consent to further processing obtained |
| Publicly available information | s15(3)(b) | Information from public records or deliberately made public |
| Crime prevention/prosecution | s15(3)(c) | Necessary for crime prevention, detection, apprehension, prosecution, or penalty enforcement |
| Required by law | s15(3)(d) | Legal obligation to process for secondary purpose |
| Legal proceedings | s15(3)(e) | Necessary for the conduct of legal proceedings |
| Historical/statistical/research | s15(3)(f) | With adequate safeguards against re-identification |

---

## 6. Conditions 5–6 — Information quality and openness

### Condition 5 — Information quality (s16)

The responsible party must take reasonably practicable steps to ensure that personal information is:

- **Complete** — no material omissions
- **Accurate** — factually correct
- **Not misleading** — does not create a false impression
- **Updated where necessary** — reflects current circumstances, having regard to the purpose for which the PI was collected or subsequently processed

### Condition 6 — Openness (s17–s18)

#### s17 — Notification to Information Regulator

Before commencing processing, the responsible party must notify the Information Regulator of:

- The categories of data subjects and PI processed
- The purpose of processing
- A description of the security measures in place
- Any planned cross-border or third-party transfers

**Practical note:** Notification is done through the IO registration process via the eServices portal. The IO's registration effectively serves as the s17 notification.

#### s18 — Notification to data subject at collection

When collecting personal information, the responsible party must take reasonably practicable steps to ensure the data subject is aware of:

| Item | s18 reference | What to disclose |
|---|---|---|
| Information collected | s18(1)(a) | What PI is being collected |
| Name and address | s18(1)(b) | Identity and contact details of the responsible party |
| Purpose | s18(1)(c) | Why the PI is being collected |
| Voluntary or mandatory | s18(1)(d) | Whether providing the PI is voluntary or mandatory |
| Consequences | s18(1)(e) | What happens if the data subject does not provide the PI |
| Applicable law | s18(1)(f) | Any law requiring or authorising the collection |
| Intended recipients | s18(1)(g) | Third parties or categories of third parties who may receive the PI |
| Cross-border transfer | s18(1)(h) | Whether PI will be transferred outside South Africa, and the level of protection |
| Right to access | s18(1)(i) | How the data subject can access their PI |
| Right to object | s18(1)(j) | The data subject's right to object to processing |
| Right to complain | s18(1)(k) | The right to lodge a complaint with the Information Regulator |

---

## 7. Conditions 7–8 — Security safeguards and data subject participation

### Condition 7 — Security safeguards (s19–s22)

#### s19 — Integrity and confidentiality

The responsible party must secure the integrity and confidentiality of PI by taking **appropriate, reasonable technical and organisational measures** to prevent:

- Loss of, damage to, or unauthorised destruction of PI
- Unlawful access to or processing of PI

The responsible party must:

1. Identify all reasonably foreseeable internal and external risks to PI
2. Establish and maintain appropriate safeguards against the identified risks
3. Regularly verify that the safeguards are effectively implemented
4. Ensure the safeguards are continually updated in response to new risks or deficiencies

#### s20 — Safeguards regarding information processed by operators

When PI is processed by an operator:

1. The responsible party must ensure the operator establishes and maintains security measures (s21(1))
2. The contract must require the operator to notify the responsible party of any security compromise (s22 read with s21)
3. The operator must treat the PI with the same level of security as if it were the responsible party

#### s22 — Breach notification

Where there are reasonable grounds to believe that PI has been accessed or acquired by an unauthorised person, the responsible party must notify:

| Recipient | Timeline | Method |
|---|---|---|
| Information Regulator | **As soon as reasonably possible** | eServices portal (mandatory since 1 April 2025) |
| Data subjects | **As soon as reasonably possible** after IR notification | Written notice — email, letter, or other appropriate means |

The notification must include:

- A description of the possible consequences of the breach
- The measures taken or to be taken by the responsible party to address the breach
- A recommendation of measures the data subject can take to mitigate adverse effects
- The identity of the unauthorised person (if known)

**Important:** The POPIA breach notification standard is "as soon as reasonably possible" — not a fixed deadline like GDPR's 72 hours. However, unreasonable delay will be treated as non-compliance.

### Condition 8 — Data subject participation (s23–s25)

See the data-subject-rights topic overlay for detailed coverage of:

- s23 right of access (reasonable fee permitted)
- s24 right to correction or deletion (30-day notification per April 2025 regulations)
- s25 remedies for refusal

---

## 8. Direct marketing (s69)

### Framework

POPIA s69 imposes specific requirements for processing personal information for **direct marketing by means of electronic communication** (email, SMS, automated calls, any form of electronic communication).

### April 2025 regulation amendments

The amended POPIA regulations (effective 17 April 2025) significantly strengthened the direct marketing framework:

| Amendment | Regulation | Effect |
|---|---|---|
| Opt-out does NOT constitute consent | Regs 2025 Reg 6 | The mere absence of an opt-out does not mean the data subject has consented to direct marketing |
| One-message consent rule | s69(3) | A responsible party may send **one** communication to request consent, provided the data subject has not previously objected |
| Recorded telemarketing | Regs 2025 Reg 6 | Telephonic or automated consent requests must be electronically recorded and made available to the data subject free of charge on request |
| Multi-channel consent | Regs 2025 Reg 6 | Consent forms must be available free of charge through multiple channels: email, telephone, SMS, WhatsApp, fax, or automated calling machine |
| Existing customer exception | s69(4) | A responsible party may market **similar** products or services to an existing customer who has not objected, provided the customer was given the opportunity to object at time of collection and at each subsequent communication |

### Direct marketing compliance checklist

| Step | Requirement | POPIA reference | Notes |
|---|---|---|---|
| 1 | Determine if the communication is "direct marketing" | s1 definition | Any approach to a data subject for the purpose of promoting or offering goods/services or requesting donations |
| 2 | Check if consent exists | s69(1)(a) | Explicit consent required — opt-out ≠ consent per April 2025 regulations |
| 3 | Check existing customer exception | s69(4) | Applies only to similar products/services, customer was informed of right to object, and has not objected |
| 4 | If no consent and no exception: one-message rule | s69(3) | May send one communication to request consent, if data subject has not previously objected |
| 5 | Provide opt-out mechanism | s69(1)(b) | Every direct marketing communication must include an opt-out mechanism |
| 6 | Process objections immediately | s11(3), Regs 2025 | Multi-channel objection must be honoured (email, WhatsApp, SMS, telephonic) |
| 7 | Record telephonic consent/marketing | Regs 2025 Reg 6 | Telephonic consent requests must be recorded, recording available free of charge |
| 8 | Maintain consent records | s8 accountability | Records of consent, opt-outs, and objections must be maintained as compliance evidence |

### FT Rams precedent

In 2024, FT Rams received the Information Regulator's first enforcement action specifically targeting direct marketing non-compliance:

- **Facts:** FT Rams continued marketing to individuals who had objected, failed to honour opt-out requests
- **Outcome:** Enforcement notice and R100K fine
- **Significance:** Established that the IR will enforce s69 violations as standalone contraventions, not merely as adjuncts to broader privacy complaints

---

## 9. Automated decision-making (s71)

### The s71 safeguard

A data subject may not be subject to a decision which results in **legal consequences** for them or which **affects them to a substantial degree**, which is based **solely** on the automated processing of personal information intended to provide a profile.

### When s71 applies

| Element | Requirement | Assessment |
|---|---|---|
| Decision | Must result in legal consequences or substantially affect the data subject | Credit refusal, insurance premium, employment screening = covered. Targeted advertising = likely not covered |
| Solely automated | No meaningful human involvement in the decision | A human rubber-stamp is insufficient — the review must be substantive |
| Profiling | Automated processing intended to provide a profile | Includes credit scoring, risk assessment, behavioural analytics |

### s71 exceptions

The s71 prohibition does not apply where:

1. The decision was taken in connection with the conclusion or performance of a contract, and the data subject's request was satisfied (s71(1)(a))
2. The decision is authorised or required by law and appropriate measures have been taken to protect the data subject's legitimate interests (s71(1)(b))

### s71 procedural safeguards

Where a data subject is affected by an automated decision:

1. The responsible party must notify the data subject that the decision was taken on the basis of automated processing (s71(2))
2. The data subject must be given an opportunity to make representations about the decision (s71(2))
3. The responsible party must provide sufficient information about the logic involved in the automated decision (s71(3))

---

## 10. Comparison table — POPIA s11 bases vs GDPR Art 6 bases

For practitioners who cross between SA and EU/UK jurisdictions, this table maps the lawful bases:

| # | GDPR Art 6 basis | POPIA s11 basis | Key differences |
|---|---|---|---|
| 1 | Consent (Art 6(1)(a)) | Consent (s11(1)(a)) | GDPR requires "clear affirmative action." POPIA requires voluntary, specific, informed consent. POPIA does not elevate consent above other bases. |
| 2 | Performance of contract (Art 6(1)(b)) | Contract (s11(1)(b)) | Substantially similar. POPIA: "necessary to carry out actions for the conclusion or performance of a contract." |
| 3 | Legal obligation (Art 6(1)(c)) | Legal obligation (s11(1)(c)) | Substantially similar. POPIA: "compliance with an obligation imposed by law." |
| 4 | Vital interests (Art 6(1)(d)) | Legitimate interest of data subject (s11(1)(d)) | POPIA is broader — "legitimate interest" is wider than GDPR "vital interests" (which relates to life-threatening situations). |
| 5 | Public interest / official authority (Art 6(1)(e)) | Public law duty (s11(1)(e)) | POPIA is narrower — limited to "public law duty by a public body." GDPR covers public interest more broadly. |
| 6 | Legitimate interests (Art 6(1)(f)) | Legitimate interests (s11(1)(f)) | Similar — but POPIA does not require a formal three-part balancing test (purpose, necessity, balancing). The responsible party must still consider the data subject's rights. POPIA applies to public bodies (GDPR excludes them from Art 6(1)(f)). |
| — | [No GDPR equivalent] | [POPIA covers juristic persons] | POPIA applies to natural and juristic persons. GDPR applies only to natural persons. This means a company's commercial information may be PI under POPIA. |

---

## 11. High-risk flags

| # | Flag | Statute | What to check | Enforcement precedent |
|---|---|---|---|---|
| 1 | Direct marketing without valid consent | POPIA s69, Regs 2025 | Is explicit consent recorded? Is existing-customer exception properly applied? Is telemarketing recorded? Is multi-channel objection honoured? Opt-out ≠ consent. | FT Rams (R100K fine — first direct marketing enforcement action) |
| 2 | Automated decision-making without s71 safeguards | POPIA s71 | Are solely automated decisions with legal effects or substantial impact being made? Is there meaningful human review? Are data subjects notified? | IR flagged AI as 2025/26 focus area |
| 3 | No lawful basis identified for processing | POPIA s11 | Has the responsible party identified which s11 basis applies to each processing activity? Is the basis documented? | Foundational compliance requirement — underpins all IR enforcement |
| 4 | Purpose not specified at collection | POPIA s13, s18 | Is the data subject informed of the specific purpose at the point of collection? Is the purpose explicitly defined and lawful? | s18 notification failures flagged in multiple IR assessments |
| 5 | Retention beyond necessity without legal basis | POPIA s14 | Is PI retained beyond the original purpose? Is there a legal basis for extended retention? Is a retention schedule in place? | Policy sweep finding in reg-gap-analysis |
| 6 | Further processing incompatible with original purpose | POPIA s15 | Is PI being used for a secondary purpose? Is the purpose compatible? Does a s15(3) exception apply? | Underpins "STOP" classification in use-case-triage |
| 7 | Compliance framework absent or stale | POPIA s8, Regs 2025 | Does a compliance framework exist? Has it been reviewed in the past 12 months? Does it cover all 8 conditions? Is it "continuously improved"? | DOJ&CD and Dis-Chem ordered to implement compliance frameworks |
