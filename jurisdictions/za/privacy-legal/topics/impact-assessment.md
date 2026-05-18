# Impact Assessment — South African Framework

This overlay covers personal information impact assessments (PIAs) and the mandatory prior authorisation regime under the Protection of Personal Information Act 4 of 2013 (POPIA). It is loaded by pia-generation, use-case-triage, and reg-gap-analysis skills when jurisdiction = ZA.

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

South African law does not have a mandatory "DPIA" in the GDPR sense. Instead, POPIA establishes two distinct mechanisms:

1. **Prior authorisation (s57)** — a **mandatory, statutory** requirement for specific types of processing. The responsible party must obtain authorisation from the Information Regulator before commencing the processing.

2. **Personal information impact assessment (PIA)** — a **voluntary, best-practice** assessment that responsible parties may conduct to evaluate compliance with POPIA's 8 conditions for lawful processing. No statutory requirement to conduct a PIA, but recommended by the Information Regulator and increasingly expected in enforcement proceedings.

### Key distinction

| Aspect | Prior authorisation (s57) | Personal information impact assessment (PIA) |
|---|---|---|
| Legal status | Mandatory statutory requirement | Voluntary best practice |
| Trigger | Specific processing types listed in s57(1) | Any processing activity (risk-based) |
| Who decides | Information Regulator — must approve before processing begins | Responsible party — self-assessment |
| Consequence of omission | Criminal offence — fine up to R10M or 12 months imprisonment (s59) | No direct penalty — but weakens defence in enforcement proceedings |
| Output | IR authorisation decision | Internal assessment report |
| Frequency | Once per processing type (s57(4)) | Periodic review recommended |

---

## 2. Prior authorisation (s57)

### The four s57 triggers

A responsible party **must** obtain prior authorisation from the Information Regulator before processing personal information if the processing involves any of the following:

#### s57(1)(a) — Unique identifier cross-linking

**Trigger:** Processing a unique identifier of a data subject for a purpose other than the purpose for which the identifier was specifically intended at collection, with the aim of linking the information processed by different responsible parties.

**Examples:**
- Retail group linking loyalty card numbers across subsidiaries to build unified customer profiles
- Financial services group linking customer ID numbers across banking, insurance, and investment entities
- Health insurer linking medical scheme numbers with pharmacy dispensing records across different service providers

**Key elements to assess:**
1. Is a unique identifier being processed?
2. Is it being used for a purpose other than originally intended?
3. Is the aim to link information across different responsible parties (not just different systems within the same responsible party)?

#### s57(1)(b) — Criminal behaviour data for third parties

**Trigger:** Processing information on criminal behaviour or on unlawful or objectionable conduct on behalf of a third party.

**Examples:**
- Background screening company processing criminal records on behalf of employers
- Fraud prevention bureau sharing fraud data across member institutions
- Private investigation firm compiling criminal behaviour profiles for clients

#### s57(1)(c) — Credit reporting

**Trigger:** Processing information for the purposes of credit reporting.

**Examples:**
- Credit bureau processing consumer credit data
- Alternative credit scoring using non-traditional data sources (mobile data, social media, purchase history)
- Fintech providing credit assessments to lenders

#### s57(1)(d) — Special PI or children's PI transfer to inadequate country

**Trigger:** Transferring special personal information (s26–s33) or children's personal information (s34–s35) to a third party in a foreign country that does not provide an adequate level of protection for the processing of personal information.

**Examples:**
- SA healthcare provider transferring patient health data (special PI — s32) to a US cloud platform
- EdTech company transferring children's learning data to servers in a country without adequate protection
- SA trade union transferring membership data (special PI — s30) to an international federation

### IR submission process

| Step | Action | Timeline | Notes |
|---|---|---|---|
| 1 | Prepare application | Pre-submission | Identify the s57 trigger, describe the processing, outline safeguards |
| 2 | Submit to Information Regulator | Day 0 | Email: POPIACompliance@inforegulator.org.za (subject to eServices portal migration) |
| 3 | IR acknowledgment | Within 14 days | Reference number assigned |
| 4 | IR initial response | **Within 4 weeks** | IR may request additional information |
| 5 | IR investigation | Up to **13 weeks** from submission | IR may consult with the responsible party, conduct inspections |
| 6 | IR decision | At conclusion of investigation | Authorise, authorise with conditions, or refuse |
| 7 | Commencement of processing | After authorisation received | Processing before authorisation = offence (s59) |

### Important s57 qualifications

1. **Once per processing type (s57(4)):** Prior authorisation is required only once for each type of processing. If a responsible party obtains authorisation for loyalty card cross-linking, it does not need to re-apply each time it links a new batch of data — the authorisation covers the processing type.

2. **Code of conduct exemption (s57(3)):** Prior authorisation is not required if a code of conduct has been issued for the sector under s60 and the responsible party complies with it. As of 2025/26, no sector codes of conduct have been issued under POPIA.

3. **Criminal offence for failure (s59):** Any person who processes personal information in contravention of s57 (without obtaining prior authorisation) is guilty of an offence and liable to a fine of up to R10M or imprisonment for up to 12 months, or both.

---

## 3. The 8 conditions as PIA assessment framework

When conducting a voluntary PIA, use POPIA's 8 conditions for lawful processing as the assessment framework. This ensures the PIA is legally grounded in the SA statutory regime rather than imported from GDPR.

### Condition-by-condition assessment checklist

| # | Condition | POPIA ref | Key questions |
|---|---|---|---|
| 1 | **Accountability** | s8 | Has the responsible party designated an IO? Is a compliance framework in place? Is it continuously improved (per April 2025 regulations)? |
| 2 | **Processing limitation** | s9–s12 | Is there a lawful basis under s11? Is PI collected directly from the data subject (s12)? Is collection minimised to what is necessary? |
| 3 | **Purpose specification** | s13–s14 | Is the purpose specific, explicitly defined, and lawful? Is PI retained only as long as necessary? |
| 4 | **Further processing limitation** | s15 | Is any secondary processing compatible with the original purpose? Does a s15(3) exception apply? |
| 5 | **Information quality** | s16 | Is the PI complete, accurate, not misleading, and updated where necessary? |
| 6 | **Openness** | s17–s18 | Has the responsible party notified the IR (s17)? Is the data subject informed at collection (s18)? |
| 7 | **Security safeguards** | s19–s22 | Are appropriate, reasonable technical and organisational measures in place? Are operator agreements in writing (s21)? Is there a breach response plan (s22)? |
| 8 | **Data subject participation** | s23–s25 | Can data subjects access their PI (s23)? Can they request correction (s24)? Are request channels established? |

### PIA report structure

A SA-compliant PIA report should include:

1. **Executive summary** — processing activity description, overall risk rating
2. **Processing description** — PI categories, data subjects, purposes, recipients, retention periods
3. **Lawful basis analysis** — which s11 basis applies, consent records if applicable
4. **8-conditions assessment** — condition-by-condition analysis with findings
5. **Special PI and children's PI assessment** — s26–s33 and s34–s35 applicability
6. **Cross-border transfer assessment** — s72 applicability, mechanisms in place
7. **Prior authorisation assessment** — does any s57 trigger apply?
8. **Risk register** — identified risks, likelihood, impact, mitigation measures
9. **Recommendations** — actions required before processing may commence
10. **Sign-off** — IO approval, legal review if applicable, IR submission for s57 if triggered

---

## 4. Special personal information (s26–s33)

### Categories and their specific provisions

POPIA prohibits the processing of special personal information unless a general exception under s27 or a category-specific exception applies.

| Category | POPIA section | Specific provisions |
|---|---|---|
| Religious or philosophical beliefs | s28 | Permitted by religious or philosophical bodies for their members, or by institutions based on those beliefs for employees/members |
| Race or ethnic origin | s29 | Permitted for identifying data subjects, compliance with legislation, countering discrimination |
| Trade union membership | s30 | Permitted by trade unions for their members, or by employers for trade union contribution deductions |
| Political persuasion | s31 | Permitted by political parties for their members |
| Health or sex life | s32 | Permitted for medical treatment by health professionals, insurance assessments, occupational health obligations, public health emergencies |
| Criminal behaviour | s33(1) | Prohibited except by the responsible party (the body responsible for the alleged criminal behaviour), under the control of bodies charged with enforcing law, or for credit bureau purposes |
| Biometric information | s33(2) | Permitted for identification or security, provided the biometric information is processed in a way that uniquely identifies the data subject |

### General exceptions (s27(1))

The prohibition on processing special PI does not apply where:

1. **Consent:** The data subject has consented (s27(1)(a))
2. **Legal obligation/right:** Processing is necessary for establishing, exercising, or defending a right or obligation in law (s27(1)(b))
3. **International public law:** Processing is necessary to comply with an international public law obligation (s27(1)(c))
4. **Historical/statistical/research:** Processing is for historical, statistical, or research purposes with adequate safeguards (s27(1)(d))
5. **Deliberately made public:** The data subject has deliberately made the information public (s27(1)(e))
6. **Specific section compliance:** Processing is necessary for compliance with specific provisions in s28–s33 (s27(1)(f))

---

## 5. Children's personal information (s34–s35)

### Definition

A **child** under POPIA is a natural person under the age of 18 years who is not legally competent without the assistance of a competent person (parent or guardian) as defined in the Children's Act 38 of 2005.

### Processing restrictions

| Rule | POPIA reference | Detail |
|---|---|---|
| General prohibition | s34(1) | Processing children's PI is prohibited unless a s35 exception applies |
| Competent person consent | s35(1)(a) | A competent person (parent/guardian) must consent on behalf of the child |
| Best interests | s35(1) read with Children's Act | Processing must be in the best interests of the child |
| Capacity to consent | s35(2) | A child who has the capacity to consent and is sufficiently mature may consent independently — rare in practice |

### Children's PI in PIAs

When a PIA involves children's personal information:

1. **Age verification:** Describe the mechanism for verifying age at the point of PI collection
2. **Consent mechanism:** Describe how competent person consent is obtained and recorded
3. **Best interests assessment:** Document how the best interests of the child are served by the processing
4. **s57(1)(d) trigger:** If children's PI is transferred to a foreign country without adequate protection, prior authorisation is required
5. **Proportionality:** Apply heightened scrutiny — children's PI requires the most restrictive interpretation of all conditions

### DBE precedent

The Department of Basic Education (DBE) received a R5M fine from the Information Regulator for publishing matric results in newspapers. This case established that:

- Publishing children's examination results constitutes processing of children's PI
- Widespread publication amplifies the privacy impact
- The DBE's appeal (Supreme Court) is pending as of 2025/26 — the fine has not been set aside

---

## 6. PIA vs prior authorisation — decision tree

Use this decision tree to determine whether a processing activity requires a voluntary PIA, mandatory prior authorisation, or both.

### Step 1: Does any s57 trigger apply?

| Question | If yes | If no |
|---|---|---|
| Are unique identifiers being cross-linked across responsible parties? (s57(1)(a)) | Prior authorisation required | Continue |
| Is criminal behaviour data being processed for third parties? (s57(1)(b)) | Prior authorisation required | Continue |
| Is the processing for credit reporting purposes? (s57(1)(c)) | Prior authorisation required | Continue |
| Is special PI or children's PI being transferred to a foreign country without adequate protection? (s57(1)(d)) | Prior authorisation required | Continue |

### Step 2: Does the processing involve heightened risk?

Even if no s57 trigger applies, a voluntary PIA is recommended when:

- Special PI (s26–s33) is processed (even domestically)
- Children's PI (s34–s35) is processed
- Large-scale processing of PI (volume, scope, or sensitivity)
- New technology is deployed (biometrics, AI, automated profiling)
- Cross-border transfer is involved (even without special PI)
- The processing is novel or the responsible party has not previously conducted this type of processing

### Step 3: Determine the action

| Scenario | Action required |
|---|---|
| s57 trigger applies | **Mandatory:** Submit prior authorisation application to IR before commencing processing. **Recommended:** Also conduct a PIA to support the application. |
| No s57 trigger, but heightened risk | **Recommended:** Conduct a voluntary PIA. Document the assessment and retain for compliance evidence. |
| No s57 trigger, low risk | **Optional:** PIA is good practice but not required. Document the risk assessment decision. |
| s57 trigger applies AND heightened risk factors present | **Mandatory:** Prior authorisation. **Strongly recommended:** Comprehensive PIA to demonstrate s8 accountability. |

---

## 7. Prior authorisation application content

When submitting a prior authorisation application to the Information Regulator, include:

### Application structure

| Section | Content | Notes |
|---|---|---|
| 1. Responsible party details | Name, registration number, IO name and registration number, contact details | IO must be registered before submission |
| 2. s57 trigger identification | Which s57(1) paragraph applies and why | Cite the specific trigger |
| 3. Processing description | PI categories, data subjects, purposes, recipients, retention periods | Be specific — generic descriptions delay processing |
| 4. Lawful basis | Which s11 basis applies | Include supporting evidence (consent records, contract, legislation) |
| 5. Safeguards | Technical and organisational measures (s19) | Demonstrate that s19 measures are appropriate |
| 6. Data subject rights | How s23 access, s24 correction, s11(3) objection are facilitated | Demonstrate Condition 8 compliance |
| 7. Cross-border considerations | If s57(1)(d): destination country, recipient, transfer mechanism | Include binding agreement if relying on s72(1)(a) |
| 8. Risk assessment | Identified risks to data subjects, mitigation measures | PIA report may be attached as supporting evidence |
| 9. Special PI / children's PI details | If applicable: categories of special PI, age of children, consent mechanisms | Demonstrate compliance with s26–s35 |

### Submission

- **Email:** POPIACompliance@inforegulator.org.za (subject to migration to eServices portal)
- **Expected timeline:** 4-week initial response, up to 13-week investigation
- **Important:** Do not commence the processing until authorisation is received. Processing before authorisation is a criminal offence (s59).

---

## 8. Automated decision-making (s71)

### Relevance to impact assessments

POPIA s71 provides that a data subject may not be subject to a decision which results in legal consequences or substantially affects them, where the decision is based **solely** on automated processing intended to provide a profile.

### When s71 applies

| Element | Requirement |
|---|---|
| Decision type | Must result in legal consequences or substantially affect the data subject |
| Automation | Decision must be based solely on automated processing |
| Profiling | Automated processing must be intended to provide a profile |
| Human review | A decision with meaningful human review is not "solely" automated |

### PIA considerations for automated processing

When a PIA involves automated decision-making:

1. **Identify** all decisions based on automated processing
2. **Assess** whether any decision results in legal consequences or substantially affects data subjects
3. **Document** the human review mechanism — is it meaningful or a rubber stamp?
4. **Notify** data subjects that automated processing is occurring (s18 openness)
5. **Provide** the data subject with an opportunity to make representations (s71(2))
6. **Record** the logic involved in the automated decision for transparency

### Information Regulator focus area

The IR has flagged AI and automated decision-making as a focus area for 2025/26. PIAs involving automated processing should anticipate heightened regulatory scrutiny and include comprehensive risk assessment and mitigation measures.

---

## 9. High-risk flags

| # | Flag | Statute | What to check | Enforcement precedent |
|---|---|---|---|---|
| 1 | Prior authorisation not obtained | POPIA s57, s59 | Is any s57 trigger present? Has the IR been approached? Processing commenced without authorisation = criminal offence (fine up to R10M or 12 months imprisonment) | s59 makes failure an offence — no enforcement case yet, but IR has flagged proactive enforcement |
| 2 | Special PI processed without authorisation | POPIA s26–s33, s27 | Which special PI category? Which s27 exception applies? If third-party processing or cross-border, s57 may be triggered | IR Guidance Note on special PI issued |
| 3 | Children's PI without competent person consent | POPIA s34–s35 | Is the data subject under 18? Has a competent person consented? Is the processing in the child's best interests? | DBE matric results (R5M fine) |
| 4 | Unique identifier cross-linking without prior authorisation | POPIA s57(1)(a) | Are identifiers being used for a purpose other than collection? Is cross-linking across responsible parties occurring? | No enforcement yet — loyalty and financial sector at highest risk |
| 5 | Credit reporting without prior authorisation | POPIA s57(1)(c) | Is the processing for credit reporting? Does it include alternative credit scoring? | Fintech and alternative lending sector exposure |
| 6 | Automated decision-making without s71 safeguards | POPIA s71 | Are solely automated decisions affecting data subjects? Is there meaningful human review? Are data subjects notified? | IR flagged AI as 2025/26 focus area |
| 7 | PIA not conducted for high-risk processing | POPIA s8 (accountability) | Is high-risk processing occurring without any documented risk assessment? Weakens s8 accountability defence | DOJ&CD and Dis-Chem ordered to implement compliance frameworks |
