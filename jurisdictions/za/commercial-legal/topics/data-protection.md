# Data Protection — South African Framework

This overlay covers the Protection of Personal Information Act 4 of 2013 (POPIA) as it applies to commercial contracts, operator agreements, cross-border data transfers, and breach notification. It is loaded by vendor-agreement-review, saas-msa-review, and nda-review skills when jurisdiction = ZA.

**Terminology requirement:** SA data protection law uses its own terminology. Do not use GDPR/EU terms in ZA outputs.

| Do NOT use | Use instead |
|---|---|
| data controller | responsible party |
| data processor | operator |
| data subject | data subject (same term, retained in POPIA) |
| GDPR | POPIA |
| DPA (Data Processing Agreement) | operator agreement (POPIA s21) |
| personal data | personal information |
| PII / PHI | personal information (POPIA definition) |

---

## 1. POPIA overview for commercial contracts

POPIA regulates the processing of personal information by responsible parties. In commercial contracts, POPIA is relevant whenever one party processes personal information on behalf of another.

### Key definitions

- **Personal information** (s1) — information relating to an identifiable, living natural person or an identifiable, existing juristic person. Includes name, contact details, ID number, financial information, biometric data, and opinions about the person.
- **Responsible party** (s1) — the party that determines the purpose of and means for processing personal information. In a commercial context, typically the party that owns the customer/employee data.
- **Operator** (s1) — the party that processes personal information on behalf of the responsible party under a contract or mandate. In a commercial context, typically the vendor/service provider.
- **Processing** (s1) — any operation performed on personal information, including collection, storage, modification, retrieval, consultation, use, disclosure, archiving, and destruction.

### When POPIA applies to a commercial contract

POPIA applies whenever:

1. The vendor/service provider will **process personal information** as part of delivering the services.
2. The information relates to **identifiable persons** (natural or juristic).
3. The processing is performed by **automated or non-automated means**.

Common triggers in commercial contracts: cloud hosting, SaaS platforms, payroll processing, customer relationship management, data analytics, marketing services, IT support with access to systems containing personal information.

---

## 2. Operator agreements (POPIA s21)

Section 21 requires that where a responsible party engages an operator to process personal information, the processing must be governed by a **written contract** that establishes the conditions for processing.

### Mandatory s21 requirements

The operator agreement must, at minimum, address:

1. **Processing only on instruction** — the operator may process personal information only with the knowledge or authorisation of the responsible party (s21(1)(a)).
2. **Security safeguards** — the operator must treat the personal information as confidential and implement appropriate security measures as required by s19 (s21(1)(b)).
3. **Notification of security compromises** — the operator must notify the responsible party immediately where there are reasonable grounds to believe that personal information has been accessed or acquired by any unauthorised person (s21(2)).

### Practical requirements beyond the statutory minimum

Best practice in SA operator agreements includes the following provisions, which flow from POPIA's general conditions for lawful processing and the Information Regulator's enforcement approach:

| Provision | Source | Why required |
|---|---|---|
| Purpose limitation | s13 | Operator must process only for the specified purpose |
| Data minimisation | s10 | Operator must not process more information than necessary |
| Retention limitation | s14 | Operator must delete or return personal information when purpose is fulfilled |
| Access and correction | s23-s25 | Operator must assist responsible party in responding to data subject requests |
| Breach notification procedure | s22 | Detailed procedure for notifying responsible party, who must notify Information Regulator and data subjects |
| Audit rights | Enforcement practice | Responsible party must be able to verify operator compliance |
| Return/deletion on termination | s14 | Personal information returned or securely destroyed at end of contract |

### Sub-operator agreements

Where the operator engages a sub-operator (sub-contractor), the **same contractual terms must flow down** to the sub-operator. The responsible party must approve the appointment of sub-operators, either specifically or by category. The operator remains liable to the responsible party for the sub-operator's compliance.

This is a critical requirement that many vendor agreements fail to address: a cloud hosting provider that uses sub-processors for backup, monitoring, or analytics must ensure each sub-processor is bound by equivalent obligations.

### High-risk flag: No POPIA operator agreement

| Check | What to look for |
|---|---|
| Personal information processed | Does the vendor/service provider process personal information as part of the services? |
| Written operator agreement | Is there a written agreement (or schedule/annexure) that specifically addresses POPIA s21 requirements? |
| Security measures specified | Does the agreement specify the technical and organisational security measures the operator must implement (s19)? |
| Processing-only-on-instruction | Does the agreement restrict the operator to processing only on the responsible party's instructions? |
| Breach notification included | Does the agreement require the operator to notify the responsible party immediately of any security compromise (s22)? |
| Sub-operator flow-down | Does the agreement require equivalent terms to flow down to sub-operators? |
| Return/deletion clause | Does the agreement address what happens to personal information on termination? |

**Why this matters:** The Information Regulator is actively enforcing POPIA operator agreement requirements. The absence of an operator agreement is itself a contravention of s21, irrespective of whether a breach has occurred. Enforcement actions in 2024/25 include fines of R5m (Department of Basic Education), R5m (Department of Justice and Constitutional Development), R500k (Blouberg Municipality), and R100k (Lancet Laboratories). The Information Regulator reported 2,374 breach notifications in 2024/25, a 40% increase over the prior year.

---

## 3. Security safeguards (POPIA s19)

Section 19 requires a responsible party to secure the integrity and confidentiality of personal information by taking appropriate, reasonable technical and organisational measures to prevent:

- Loss of, damage to, or unauthorised destruction of personal information
- Unlawful access to or processing of personal information

### What "appropriate, reasonable" means in practice

The standard is proportionate to the nature and quantity of personal information processed and the harm that could result from a breach. Relevant measures include:

- Encryption of personal information in transit and at rest
- Access controls limiting who can view or modify personal information
- Regular security assessments and penetration testing
- Employee training on data protection
- Incident response plans and procedures
- Physical security of data centres and offices

The Information Regulator's amended POPIA regulations (April 2025) introduced stricter requirements for compliance frameworks, including the obligation to maintain documented security measures and to conduct regular reviews.

---

## 4. Breach notification (POPIA s22)

Where there are reasonable grounds to believe that personal information has been accessed or acquired by an unauthorised person, the responsible party must notify:

1. **The Information Regulator** — as soon as reasonably possible after the discovery of the compromise.
2. **The data subject** — as soon as reasonably possible after the discovery, unless the identity of the data subject cannot be established.

### Notification content

The notification must include:

- A description of the possible consequences of the security compromise
- A description of the measures the responsible party intends to take to address the compromise
- A recommendation regarding the measures the data subject should take to mitigate the adverse effects
- The identity of the unauthorised person who may have accessed the information (if known)

### Operator's obligation

The operator must notify the **responsible party** immediately upon becoming aware of a security compromise (s21(2)). The responsible party then bears the notification obligation to the Information Regulator and data subjects.

### Enforcement context

The Information Regulator received **2,374 breach notifications** in the 2024/25 financial year, representing a **40% increase** over the previous year. The Regulator has stated that failure to notify is itself a contravention, compounding the original breach.

---

## 5. Cross-border data transfers (POPIA s72)

Section 72 restricts the transfer of personal information outside the Republic of South Africa.

### Transfer conditions

Personal information may only be transferred to a recipient in another country if:

1. **Adequate protection** — the recipient is subject to a law, binding corporate rules, or binding agreement that provides an adequate level of protection substantially similar to the conditions for lawful processing under POPIA (s72(1)(a)).
2. **Data subject consent** — the data subject consents to the transfer (s72(1)(b)).
3. **Contractual necessity** — the transfer is necessary for the performance of a contract between the data subject and the responsible party, or for the implementation of pre-contractual measures taken in response to the data subject's request (s72(1)(c)).
4. **Responsible party's benefit** — the transfer is for the benefit of the data subject and it is not reasonably practicable to obtain consent (s72(1)(d)).

### No adequacy list

The Information Regulator has **not published an adequacy list** of countries deemed to provide adequate protection. This is a significant practical gap. The consequence is that the most common basis for cross-border transfers is **contractual protection** — a data transfer agreement between the parties that imposes POPIA-equivalent obligations on the recipient.

### Practical approach

1. **Data transfer agreements** — the preferred mechanism. The agreement must impose obligations substantially similar to POPIA's conditions for lawful processing on the foreign recipient.
2. **Adapting GDPR SCCs** — some SA practitioners adapt GDPR Standard Contractual Clauses for POPIA. However, the SCCs must be modified to reference POPIA terminology and requirements, not GDPR.
3. **Binding Corporate Rules (BCRs)** — BCRs do not need to be registered with the Information Regulator. They must provide an adequate level of protection and be binding on all group entities.
4. **Consent** — data subject consent is a valid basis, but must be voluntary, specific, and informed. It is impractical for large-scale B2B data transfers.

### High-risk flag: Cross-border data transfer without safeguards

| Check | What to look for |
|---|---|
| Data leaving SA | Will personal information be transferred to, stored in, or accessed from a country outside SA? |
| Hosting location identified | Where is the data physically hosted? Cloud providers may replicate across regions |
| Transfer mechanism in place | Is there a data transfer agreement, BCR, or data subject consent in place? |
| POPIA-equivalent obligations | Does the transfer mechanism impose obligations substantially similar to POPIA on the foreign recipient? |
| Adapted for POPIA (not GDPR) | If using adapted SCCs, do they reference POPIA terminology (responsible party, operator, personal information) rather than GDPR terminology? |
| Sub-operator location disclosed | If the operator uses sub-operators, are the sub-operators' locations and applicable data protection regimes disclosed? |

**Why this matters:** Transferring personal information outside SA without adequate protection is a contravention of s72. The Information Regulator can issue enforcement notices, impose administrative fines up to R10 million, and refer matters for criminal prosecution. Given the absence of an adequacy list, the burden falls on the responsible party to demonstrate adequate protection through contractual or other mechanisms.

---

## 6. Penalty ceiling and enforcement

### Administrative fines

The Information Regulator may impose administrative fines of up to **R10 million** for contravention of POPIA provisions.

### Criminal penalties

Certain POPIA contraventions constitute criminal offences, punishable by a fine or imprisonment of up to 10 years:

- Obstruction of the Information Regulator (s100)
- Failure to comply with an enforcement notice (s101)
- Offences by responsible parties or operators relating to account numbers (s104-s106)

### Enforcement track record

| Entity | Fine | Date | Basis |
|---|---|---|---|
| Department of Basic Education | R5 million | 2024 | Breach of learner personal information |
| Department of Justice and Constitutional Development | R5 million | 2024 | Failure to implement adequate security measures |
| Blouberg Municipality | R500,000 | 2024 | Non-compliance with POPIA conditions |
| Lancet Laboratories | R100,000 | 2024 | Breach notification handling |

The trajectory indicates increasing enforcement activity and escalating fines. The Information Regulator has publicly stated its intention to pursue more enforcement actions against private sector entities.

---

## 7. Amended POPIA regulations (April 2025)

The amended regulations, effective April 2025, introduced several changes relevant to commercial contracts:

1. **Stricter direct marketing rules** — responsible parties must obtain express opt-in consent for direct marketing by electronic means (s69). Existing customer exception narrowed.
2. **Telemarketing requirements** — new requirements for telemarketing scripts and consent recording.
3. **Compliance frameworks** — responsible parties must maintain documented compliance frameworks, including regular risk assessments, staff training records, and incident response procedures.
4. **Information officer registration** — all responsible parties must register their information officer with the Information Regulator.

### Impact on commercial contracts

- Vendor agreements involving marketing services must address the stricter s69 requirements
- SaaS agreements providing marketing automation must include compliance with the amended direct marketing rules
- Operator agreements must address the operator's role in supporting the responsible party's compliance framework

---

## 8. POPIA interaction with NDAs

Where an NDA covers personal information (e.g., due diligence involving employee records, customer databases, or patient information):

1. The disclosing party is the **responsible party** for the personal information.
2. The receiving party becomes an **operator** to the extent it processes the personal information under the NDA.
3. A **POPIA operator agreement** (or operator annexure to the NDA) is required.
4. The NDA's confidentiality obligations do not substitute for POPIA compliance — the operator agreement must address POPIA-specific requirements (security safeguards, breach notification, purpose limitation, retention, deletion).
5. Upon termination of the NDA, personal information must be returned or securely destroyed in accordance with s14 and the operator agreement.

---

## 9. Must-not-contain reference

When jurisdiction = ZA, data protection review skills must not use the following terms:

| Do NOT use | Use instead |
|---|---|
| data controller | responsible party |
| data processor | operator |
| GDPR | POPIA |
| DPA (Data Processing Agreement) | operator agreement (POPIA s21) |
| personal data | personal information |
| PII / PHI | personal information |
| HIPAA | Not applicable — use POPIA |
| Standard Contractual Clauses (without POPIA adaptation) | POPIA-adapted data transfer agreement |
| "Article 46" or other GDPR article references | POPIA section references (s72, s21, etc.) |
