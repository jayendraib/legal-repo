# Data Subject Rights — South African Framework

This overlay covers the rights of data subjects under the Protection of Personal Information Act 4 of 2013 (POPIA), including the right of access, correction and deletion, objection, and the exemption framework. It is loaded by dsar-response, use-case-triage, and policy-monitor skills when jurisdiction = ZA.

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

POPIA establishes data subject rights primarily through Condition 8 (Data Subject Participation, s23–s25) and the objection right under s11(3). Unlike GDPR, POPIA does not provide a standalone right to data portability, and permits a reasonable fee for access requests.

### Key statutes and provisions

| Provision | Reference | Effect |
|---|---|---|
| Right of access | POPIA s23 | Data subject may request confirmation and access to personal information held |
| Right to correction or deletion | POPIA s24 | Data subject may request correction or deletion of inaccurate, irrelevant, excessive, out-of-date, incomplete, misleading, or unlawfully obtained PI |
| Right to object | POPIA s11(3)(a) | Data subject may object to processing on reasonable grounds relating to their particular situation |
| Destruction of records | POPIA s24(3) | Responsible party must destroy or delete PI that can no longer be retained under s14 |
| Remedies for refusal | POPIA s25 | Data subject may apply to court for appropriate relief if request refused |
| April 2025 regulations | POPIA Regs 2025 | Multi-channel requests, 30-day correction notification, recorded telephonic objections |

### Consequences of non-compliance

| Failure | Consequence | Enforcement precedent |
|---|---|---|
| Refusal to process valid access request | Complaint to Information Regulator, enforcement notice (s95), court application (s25) | IR processing complaints via eServices portal |
| Failure to respond to correction within 30 days | Breach of April 2025 regulations, enforcement notice | Active IR monitoring of compliance |
| Failure to honour objection to direct marketing | s69 contravention, administrative fine up to R10M | FT Rams (R100K fine — first direct marketing enforcement) |
| Systemic failure to facilitate rights | s8 accountability breach, compliance framework deficiency | Dis-Chem, DOJ&CD (compliance framework ordered) |

---

## 2. Right of access (s23)

### What the data subject may request

Under POPIA s23, a data subject may request a responsible party to:

1. **Confirm** whether the responsible party holds personal information about the data subject (s23(1)(a)).
2. **Provide a description** of the personal information held (s23(1)(b)(i)).
3. **Provide the identity or categories** of third parties who have or have had access to the information (s23(1)(b)(ii)).
4. **Provide access** to the personal information itself (s23(1)(b)(iii)).

### Reasonable fee

Unlike GDPR (where access is generally free), POPIA s23(2) permits the responsible party to charge a **reasonable fee** for access. The fee:

- Must be prescribed by the responsible party in advance
- Must not be excessive or designed to discourage requests
- Should reflect the actual cost of retrieving and providing the information
- Must be communicated to the data subject before processing the request

### No statutory deadline

POPIA does not prescribe a specific time limit for responding to access requests. The standard is "within a reasonable time" — assessed contextually based on:

- Volume and complexity of the information
- Format in which the information is held (live systems vs. backup tapes)
- Number of data sources to be searched
- Whether third parties hold relevant information

**Practical guidance:** Although no statutory deadline exists, unreasonable delay may constitute a refusal, entitling the data subject to seek relief under s25 or lodge a complaint with the Information Regulator. Most practitioners advise responding within 30 days as a benchmark of reasonableness.

### Format of response

The responsible party must provide the information in a form that is "reasonably understandable" to the data subject (s23(1)(b)). This means:

- Plain language, not raw database exports
- Personal information must be separated from other information if stored together
- If the responsible party holds PI in coded or abbreviated form, a translation or explanation must be provided

### Proportionality for backup and archived data

When access requests cover data held on backup tapes, archived systems, or disaster recovery storage:

1. Assess whether the backup data constitutes a "record" as defined in POPIA s1
2. Consider the cost and technical burden of retrieval against the data subject's interest
3. If retrieval from backup is disproportionate, explain this to the data subject and offer access to PI in active systems
4. Document the proportionality assessment — this may be scrutinised if the data subject complains

---

## 3. Right to correction and deletion (s24)

### Grounds for correction or deletion

A data subject may request correction or deletion of personal information that is:

- Inaccurate
- Irrelevant
- Excessive
- Out of date
- Incomplete
- Misleading
- Obtained unlawfully

### April 2025 regulation amendments

The amended POPIA regulations (effective 17 April 2025) introduced significant changes to the correction process:

#### 30-day response requirement

The responsible party must notify the data subject of the action taken on a correction request **within 30 days** of receiving the request. This notification must include:

- What correction was made (or why the request was refused)
- Whether third parties who received the incorrect information have been notified
- The data subject's right to lodge a complaint with the Information Regulator if dissatisfied

#### Multi-channel requests

Data subjects may now submit correction requests through any of the following channels:

| Channel | Requirements |
|---|---|
| Email | Standard written request |
| WhatsApp | Accepted as a valid channel — no written signature required |
| SMS | Accepted as a valid channel |
| Telephonic | Must be recorded and the recording made available to the data subject free of charge |
| In person | Standard written request or verbal request recorded by the responsible party |
| Fax | Still accepted |

**Key implication:** A responsible party cannot refuse a correction request solely because it was submitted via WhatsApp or SMS. The absence of a WhatsApp process does not excuse non-compliance — the responsible party must establish channels to receive and process multi-channel requests.

### Procedural checklist — correction request

1. **Receive and log** the request regardless of channel (email, WhatsApp, SMS, telephonic, in person)
2. **Verify identity** of the data subject — use reasonable steps, not excessive barriers
3. **Acknowledge receipt** — confirm the request has been received and provide a reference number
4. **Locate the PI** across all systems where it is held
5. **Assess the request** — does the PI fall within one of the s24 grounds?
6. **If correcting:** make the correction, notify the data subject within 30 days, notify third parties who received the incorrect PI
7. **If refusing:** provide written reasons within 30 days, inform the data subject of the right to complain to the Information Regulator
8. **Record the decision** and retain the record for compliance evidence
9. **If the PI was provided by a third party:** notify that third party of the correction request

### Destruction of PI no longer authorised (s24(3))

If a responsible party is no longer authorised to retain personal information (i.e., the purpose for collection has been achieved and no other legal basis for retention exists under s14), it must:

- Destroy or delete the PI as soon as reasonably practicable
- De-identify the PI so that it can no longer be linked to a data subject

The responsible party must restrict processing of the PI pending its destruction or deletion.

---

## 4. Right to object (s11(3))

### General objection right

Under POPIA s11(3)(a), a data subject may, at any time, **object to the processing** of personal information on reasonable grounds relating to their particular situation, unless legislation provides for such processing.

If a data subject objects and the objection is justified, the responsible party must **no longer process** the personal information concerned (s11(3)(b)).

### April 2025 regulation amendments — expanded channels

The amended regulations (effective 17 April 2025) significantly expand the objection framework:

#### Multi-channel objection

Data subjects may submit objections through any of the following channels:

- Email
- WhatsApp
- SMS
- Telephonic (must be recorded)
- In person
- Fax
- Automated calling machine response

#### Recording requirement

Telephonic objections must be:

1. Electronically recorded by the responsible party
2. Made available to the data subject free of charge upon request
3. Retained as evidence of the objection

#### Notification duty at collection

The responsible party must inform the data subject of the **right to object** at the time of collection (s18 read with April 2025 regulations). This notification must include:

- The existence of the right to object
- The channels through which objection can be submitted
- That telephonic objections will be recorded

### Objection to direct marketing (s69 read with s11(3))

The right to object has particular force in the direct marketing context:

1. A data subject may object to the processing of their PI for direct marketing at any time
2. Opt-out does **not** constitute consent (April 2025 regulations) — the mere fact that a data subject has not opted out does not mean consent exists
3. Once the data subject objects, all direct marketing to that data subject must cease
4. The one-message rule: a responsible party that does not have consent may send **one** communication to request consent, provided the data subject has not previously objected (s69(3))
5. Existing customer exception (s69(4)): a responsible party may market similar products/services to an existing customer who has not objected, provided they were given the opportunity to object at the time of collection

---

## 5. Data portability — no standalone right

POPIA does not establish a standalone right to data portability equivalent to GDPR Article 20.

### What POPIA provides

POPIA s12(1)(d) allows a data subject to request the responsible party to **transmit their personal information** in the possession or under the control of the responsible party to another responsible party, to the extent that this is technically practicable.

### Key differences from GDPR portability

| Aspect | GDPR Art 20 | POPIA s12(1)(d) |
|---|---|---|
| Standalone right | Yes — explicitly labelled "right to data portability" | No — embedded in general access provisions |
| Machine-readable format | Required ("structured, commonly used, machine-readable format") | Not required — no format specification |
| Scope | PI provided by data subject, processed by automated means, based on consent or contract | PI "in the possession or under the control" of the responsible party |
| Direct transmission | Required "where technically feasible" | "To the extent that this is technically practicable" |

**Practical guidance:** Do not reference "data portability" as a POPIA right in communications with data subjects or in privacy notices. Instead, reference the data subject's right to request access and transmission under s23 and s12(1)(d).

---

## 6. Exemption framework

POPIA provides several exemptions from the conditions for lawful processing. These are critical when assessing whether a data subject request must be honoured in full.

### s15 — further processing limitation exceptions

Processing for a secondary purpose (incompatible with the original purpose) is permitted where:

1. The data subject has consented (s15(3)(a))
2. The information is publicly available (s15(3)(b))
3. Necessary for the prevention or detection of crime, apprehension or prosecution of offenders, or the enforcement of a penalty (s15(3)(c))
4. Required by or under law (s15(3)(d))
5. Necessary for the conduct of legal proceedings (s15(3)(e))
6. Processing is for historical, statistical, or research purposes and the responsible party has adequate safeguards (s15(3)(f))

### s27 — special personal information exceptions

The general prohibition on processing special personal information (s26) does not apply where:

1. The data subject has consented (s27(1)(a))
2. Processing is necessary for establishing, exercising, or defending a right or obligation in law (s27(1)(b))
3. Processing is necessary to comply with an international public law obligation (s27(1)(c))
4. Processing is for historical, statistical, or research purposes (s27(1)(d))
5. The information has deliberately been made public by the data subject (s27(1)(e))
6. Processing is necessary for compliance with specific legislation (individual section-level exceptions in s28–s33)

### s37 — Information Regulator exemptions

The Information Regulator may grant an exemption from any condition for lawful processing if:

1. The public interest in the processing outweighs the interference with the data subject's privacy (s37(1)(a))
2. It would be impracticable for the responsible party to comply with the condition (s37(1)(b))
3. Exemption would not unduly prejudice the legitimate interests of the data subject (s37(1)(c))

Exemptions are published in the Government Gazette and may be subject to conditions.

---

## 7. Procedural checklists

### Checklist: handling an access request (s23)

| Step | Action | Timeline | Notes |
|---|---|---|---|
| 1 | Receive request | Day 0 | Log immediately regardless of channel |
| 2 | Verify identity | Days 1–3 | Reasonable verification — do not impose excessive barriers |
| 3 | Acknowledge receipt | Days 1–5 | Provide reference number, advise of fee if applicable |
| 4 | Assess scope | Days 3–10 | Identify all systems holding the data subject's PI |
| 5 | Check exemptions | Days 3–10 | Legal privilege, s15 exceptions, third-party PI in same records |
| 6 | Compile response | Days 10–25 | Reasonably understandable format, separate PI from other data |
| 7 | Deliver response | By day 30 (benchmark) | Include description of PI, categories of recipients, purposes |
| 8 | Record outcome | Same day as delivery | Retain record for compliance evidence |

### Checklist: handling a correction/deletion request (s24)

| Step | Action | Timeline | Notes |
|---|---|---|---|
| 1 | Receive request via any channel | Day 0 | WhatsApp, SMS, email, telephonic, in person all valid |
| 2 | If telephonic: confirm recording | Day 0 | Must record and make available free of charge |
| 3 | Verify identity | Days 1–3 | Reasonable steps |
| 4 | Acknowledge receipt | Days 1–5 | Reference number |
| 5 | Locate PI across systems | Days 3–10 | All databases, backups, third-party recipients |
| 6 | Assess against s24 grounds | Days 5–15 | Inaccurate, irrelevant, excessive, outdated, incomplete, misleading, unlawful |
| 7 | Make correction or prepare refusal reasons | Days 10–25 | Document rationale |
| 8 | Notify data subject of outcome | **Within 30 days** | Mandatory per April 2025 regulations |
| 9 | Notify third-party recipients | Within 30 days | If PI was shared with third parties |
| 10 | Inform of complaint right | Same day as notification | Right to complain to Information Regulator |

### Checklist: handling an objection (s11(3))

| Step | Action | Timeline | Notes |
|---|---|---|---|
| 1 | Receive objection via any channel | Day 0 | All channels valid per April 2025 regulations |
| 2 | If telephonic: confirm recording is active | Day 0 | Must record and make available free of charge |
| 3 | Verify identity | Days 1–3 | Reasonable steps |
| 4 | Acknowledge receipt | Days 1–5 | Reference number |
| 5 | Assess grounds | Days 3–15 | "Reasonable grounds relating to particular situation" |
| 6 | If direct marketing objection | Immediately | Cease all marketing — no assessment of grounds needed |
| 7 | Determine whether objection is justified | Days 5–20 | If non-marketing: assess proportionality |
| 8 | If justified: cease processing | Upon determination | No further processing of the PI for that purpose |
| 9 | If not justified: provide written reasons | Within 30 days (benchmark) | Inform of right to apply to court (s25) or complain to IR |
| 10 | Record outcome | Same day | Retain for compliance evidence |

---

## 8. High-risk flags

| # | Flag | Statute | What to check | Enforcement precedent |
|---|---|---|---|---|
| 1 | Breach notification failure or delay | POPIA s22(1) | Was the Information Regulator notified via eServices portal? Were data subjects notified? Was notification timely ("as soon as reasonably possible")? | Lancet Labs (R100K fine), DOJ&CD (R5M fine) |
| 2 | Direct marketing non-compliance | POPIA s69, Regs 2025 | Is explicit consent recorded? Is existing-customer exception properly applied? Is telemarketing recorded? Is multi-channel objection honoured? | FT Rams (R100K fine — first direct marketing enforcement action) |
| 3 | No process for multi-channel requests | POPIA s24, s11(3), Regs 2025 | Can the organisation receive and process requests via WhatsApp, SMS, telephonic? Are telephonic interactions recorded? | Active IR monitoring since April 2025 |
| 4 | Systemic refusal of access requests | POPIA s23, s25 | Are access requests being processed? Is the fee reasonable? Is the response timeline reasonable? | Court application under s25 available to data subjects |
| 5 | Failure to notify of right to object at collection | POPIA s18, s11(3), Regs 2025 | Is the right to object communicated at the point of PI collection? Are objection channels disclosed? | IR compliance assessment criteria |
