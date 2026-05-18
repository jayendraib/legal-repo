# Operator Agreements — South African Framework

This overlay covers the framework for agreements between responsible parties and operators under the Protection of Personal Information Act 4 of 2013 (POPIA), including the s21 written contract requirement, security safeguard flow-down, cross-border transfer obligations, and term-by-term review guidance. It is loaded by dpa-review and policy-monitor skills when jurisdiction = ZA.

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
| data processing agreement (DPA) | written contract (s21) or operator agreement |
| Article [N] | [do not reference GDPR articles — cite POPIA sections] |
| CCPA / CPRA / state privacy law | [do not reference US privacy laws] |

---

## 1. Statutory framework

POPIA s21 establishes the framework for the relationship between a responsible party and an operator. The agreement between them is a **written contract** under s21(1) — POPIA does not use the term "data processing agreement" (DPA), and SA practitioners should use "operator agreement" or "written contract" in all documentation and correspondence.

### Key provisions

| Provision | Reference | Effect |
|---|---|---|
| Written contract required | POPIA s21(1) | A responsible party must, in terms of a written contract, ensure the operator establishes and maintains security measures under s19 |
| Processing on instruction only | POPIA s21(2) | The operator may process PI only with the knowledge or authorisation of the responsible party |
| Operator treated as responsible party for security | POPIA s21(1) read with s19 | The operator must secure the integrity and confidentiality of PI as if it were a responsible party for purposes of s19 |
| Breach notification | POPIA s22 | The operator must notify the responsible party immediately upon becoming aware of a security compromise |
| Cross-border transfer | POPIA s72 | If the operator is in a foreign country, s72 safeguards must be in place |
| Direct marketing restrictions | POPIA s69 | Operator processing PI for direct marketing must comply with s69 |

### What POPIA does NOT require (compared to GDPR Art 28)

Understanding what POPIA omits is critical when reviewing operator agreements modelled on GDPR templates:

| GDPR Art 28 requirement | POPIA position |
|---|---|
| Detailed specification of processing activities | Not required by s21 — but good practice |
| Prior written authorisation for sub-processors | Not explicitly required — s21 addresses the responsible party/operator relationship only |
| Obligation to assist with DPIAs | No DPIA concept — s57 prior authorisation is the responsible party's obligation |
| Obligation to assist with data subject requests | Not explicitly required by s21 — but implied by the responsible party's s23–s25 obligations |
| Right to audit | Not explicitly required by s21 — contractual matter |
| Return or deletion of data on termination | Not explicitly required by s21 — contractual matter |
| Records of processing activities | Not explicitly required by POPIA |

**Practical implication:** When reviewing an operator agreement modelled on GDPR Art 28, many of the Art 28 terms are good practice but not POPIA requirements. The s21 obligations are narrower — the core obligation is to ensure the operator maintains s19 security measures. However, prudent practice is to include terms addressing the GDPR Art 28 areas as contractual protections, even where POPIA does not mandate them.

---

## 2. Responsible party vs operator — obligations matrix

### Determining status

| Factor | Responsible party | Operator |
|---|---|---|
| Determines purpose of processing | Yes | No — processes on instruction |
| Determines means of processing | Yes (or jointly) | May determine some technical means |
| Directly accountable to data subjects | Yes — s23 access, s24 correction, s11(3) objection | No direct data subject relationship |
| Must register IO | Yes — s55 | No IO registration for operator activities |
| Must notify IR of security compromise | Yes — s22(1) | Must notify the responsible party |
| Subject to s57 prior authorisation | Yes | No — this is the responsible party's obligation |
| Cross-border transfer obligations | Yes — must ensure s72 compliance | Must comply with contractual terms set by responsible party |

### Dual-status entities

Many SA organisations act as both responsible party and operator:

- **As responsible party:** for their own employee data, customer data, business contact data
- **As operator:** when processing PI on behalf of clients (e.g., BPO, payroll provider, cloud hosting)

The operator agreement must clearly delineate which PI is processed in which capacity. Misclassification of status is a common compliance gap.

### POPIA applies to juristic persons

A critical SA-specific consideration: POPIA protects the personal information of **juristic persons** (companies, trusts, close corporations) in addition to natural persons (s1 definition of "data subject"). This means:

- Operator agreements must cover PI of both natural and juristic person clients
- Cross-border adequacy assessments must account for the fact that most foreign data protection laws do not protect juristic persons, creating a potential adequacy gap under s72

---

## 3. Security safeguards flow-down (s19 via s21)

### The s19 obligation

POPIA s19(1) requires a responsible party to secure the integrity and confidentiality of PI by taking **appropriate, reasonable technical and organisational measures** to prevent:

- Loss of, damage to, or unauthorised destruction of PI
- Unlawful access to or processing of PI

### Flow-down mechanism

The s21(1) written contract is the mechanism by which the responsible party ensures the operator meets the s19 standard. The contract must:

1. **Establish** that the operator will implement security measures as if it were a responsible party
2. **Maintain** those measures throughout the duration of the processing relationship
3. **Ensure** the operator notifies the responsible party of any security compromise

### Minimum security safeguards for operator agreements

Based on s19 requirements and IR enforcement precedent, the operator agreement should address:

| Security area | s19 requirement | Contract clause guidance |
|---|---|---|
| Access controls | Appropriate measures to prevent unauthorised access | Specify access controls: role-based access, multi-factor authentication, password policies |
| Encryption | Appropriate measures to protect integrity | Specify encryption standards for data at rest and in transit |
| Personnel security | Organisational measures | Confidentiality agreements for operator staff, background checks where appropriate |
| Incident response | Breach notification via s22 | Notification timeline (contractual — POPIA says "as soon as reasonably possible"), escalation procedures |
| Regular testing | "Appropriate, reasonable" standard | Vulnerability assessments, penetration testing frequency |
| Disposal | Prevent unauthorised access post-termination | Secure destruction/return of PI on termination |

### Dis-Chem precedent — the consequences of inadequate operator controls

In 2023, Dis-Chem Pharmacies received an enforcement notice after a security compromise affecting 3.6 million customer records. Key findings relevant to operator agreements:

- Dis-Chem had engaged a third-party operator (Grapevine) for a promotional SMS campaign
- **No written operator agreement** existed between Dis-Chem and Grapevine as required by s21(1)
- Grapevine's security was inadequate — weak password policies, insufficient access controls
- The Information Regulator held **Dis-Chem** (the responsible party) accountable for the operator's security failures
- Dis-Chem was ordered to implement a POPIA compliance framework and ensure all operator agreements comply with s21

**Lesson:** The responsible party cannot outsource accountability. Even if the operator caused the breach, the responsible party bears regulatory responsibility for ensuring the operator's security measures comply with s19 via s21.

---

## 4. Cross-border transfer obligations (s72)

### When an operator agreement involves cross-border transfer

An operator agreement triggers s72 assessment when:

1. The operator is located in a foreign country
2. The operator uses sub-operators in foreign countries
3. The operator stores PI on servers located outside South Africa (including cloud hosting)
4. The operator's staff access PI from outside South Africa (even if data is hosted in SA)

### s72 permitted grounds for cross-border transfer

| Ground | POPIA reference | Practical application in operator agreements |
|---|---|---|
| Adequate law, binding corporate rules, or binding agreement | s72(1)(a) | Primary mechanism — include a binding agreement as schedule to operator agreement |
| Data subject consent | s72(1)(b) | Requires explicit, informed consent — not practical for most operator arrangements |
| Contractual necessity with data subject | s72(1)(c) | Applicable where the processing is necessary to perform a contract with the data subject |
| Contract in interest of data subject | s72(1)(d) | Limited application |
| Benefit of data subject where consent impracticable | s72(1)(e) | Emergency or impracticable circumstances |

### No adequacy list

As of 2025/26, the Information Regulator has **not published an adequacy list** of countries deemed to provide adequate protection. This means:

- No country can be assumed to have "adequate" protection for purposes of s72(1)(a)
- Every cross-border transfer requires either a **binding agreement**, binding corporate rules, or one of the other s72 grounds
- The absence of an adequacy list increases the importance of contractual safeguards

### Practical mechanisms for cross-border operator arrangements

| Mechanism | How it works | Notes |
|---|---|---|
| Binding agreement (adapted from GDPR SCCs) | Include POPIA-specific provisions in the transfer agreement, adapting GDPR SCC structure | Most common approach. Must reference POPIA obligations, not GDPR articles |
| Binding corporate rules | Intra-group transfers governed by group-wide privacy rules | Suitable for multinational groups with SA subsidiaries |
| Consent | Data subject provides explicit, informed consent to the specific transfer | Impractical for large-scale operator arrangements |
| Contract schedule | s72 binding agreement included as a schedule to the s21 operator agreement | Efficient — combines operator and transfer obligations in one document |

### Cloud storage as cross-border transfer

Cloud hosting arrangements require particular attention:

- If PI is stored on servers outside South Africa, this constitutes a cross-border transfer even if the cloud provider has a SA data centre option
- If data is replicated across multiple regions (including regions outside SA), each replication location constitutes a transfer
- If the cloud provider's support staff access PI from outside SA, this may constitute a transfer
- The operator agreement must specify permitted data locations and restrict replication to approved regions

---

## 5. Direct marketing restrictions on operators (s69)

### When operators process PI for direct marketing

If an operator processes PI on behalf of a responsible party for direct marketing purposes, the following restrictions apply:

1. **Consent responsibility:** The responsible party must ensure valid consent exists before instructing the operator to conduct direct marketing (s69(1))
2. **Opt-out ≠ consent:** Per April 2025 regulations, the mere absence of an opt-out does not constitute consent — explicit consent is required
3. **One-message rule:** A responsible party may instruct an operator to send one communication to request consent, provided the data subject has not previously objected (s69(3))
4. **Existing customer exception:** Marketing of similar products/services to existing customers who have not objected is permitted under s69(4)
5. **Recording of telemarketing:** If the operator conducts telemarketing, calls must be recorded and recordings made available to data subjects free of charge (April 2025 regulations)

### Operator agreement clauses for direct marketing

The operator agreement should include:

- Prohibition on the operator conducting direct marketing except on the responsible party's written instruction
- Requirement to maintain records of consent for each data subject
- Obligation to process objections immediately and cease marketing
- Telemarketing recording and retention obligations
- Compliance with the responsible party's channel-specific consent processes

---

## 6. Term-by-term review framework

When reviewing an operator agreement (whether received from an operator or drafted internally), assess each term against POPIA requirements. The table below maps common GDPR-modelled DPA terms to their POPIA equivalents.

### Comparison table: GDPR Art 28 DPA terms vs POPIA s21 requirements

| DPA term (GDPR model) | POPIA equivalent | Required by POPIA? | Recommended position |
|---|---|---|---|
| **Subject matter and duration** | Define PI processed, purposes, duration | Not explicitly required by s21 | Include — necessary for clarity and s13 purpose specification |
| **Nature and purpose of processing** | Link to responsible party's processing purpose | Not explicitly required by s21 | Include — aligns with s13 |
| **Type of personal data** | Categories of PI (general, special, children's) | Not explicitly required | Include — determines s26–s35 and s57 obligations |
| **Categories of data subjects** | Natural and juristic persons | Not explicitly required | Include — POPIA covers juristic persons |
| **Obligations of the processor** | Operator processes only on instruction (s21(2)) | **Yes — s21(2)** | Mandatory |
| **Security measures** | s19 safeguards established and maintained (s21(1)) | **Yes — s21(1)** | Mandatory — specify technical and organisational measures |
| **Sub-processor engagement** | Prior authorisation of sub-operators | Not required by s21 | Include — responsible party cannot monitor what it does not know about |
| **Assistance with data subject requests** | Operator assists with s23 access, s24 correction | Not explicitly required | Include — responsible party needs operator cooperation to fulfil s23–s25 |
| **Assistance with DPIAs** | No DPIA in POPIA — s57 prior authorisation is responsible party's duty | N/A | Omit DPIA references. Include obligation to provide information for s57 applications if applicable |
| **Breach notification** | Operator notifies responsible party of security compromise (s22 read with s21) | **Yes — s22** | Mandatory — specify timeline and content of notification |
| **Data return/deletion on termination** | Secure disposal of PI | Not explicitly required by s21 | Include — critical for s14 retention limits and s19 security |
| **Audit rights** | Responsible party's right to inspect operator's compliance | Not required by s21 | Include — necessary to fulfil s8 accountability |
| **International transfers** | s72 cross-border safeguards | **Yes — if applicable** | Mandatory if operator is in or uses resources in a foreign country |
| **Confidentiality obligations for personnel** | s19 organisational measures | Implied by s19 via s21 | Include — specify confidentiality agreements for operator staff |

### Standard clause positions

When negotiating an operator agreement, the following positions reflect SA market practice:

| Clause | Responsible party position | Operator position | Resolution guidance |
|---|---|---|---|
| Breach notification timeline | "Immediately" or "within 24 hours" | "As soon as reasonably possible" (POPIA wording) | POPIA uses "as soon as reasonably possible" — contractual timelines beyond this are negotiable. Avoid "72 hours" (GDPR language) |
| Sub-operator engagement | Prior written consent for all sub-operators | Notification with right to object | Prior consent is not a POPIA requirement but is prudent — the responsible party bears regulatory risk |
| Audit rights | Unlimited audit right | Annual third-party audit report | Proportionate approach — annual SOC 2 or ISO 27001 report with right to specific audit on reasonable notice |
| Data deletion timeline | "Within 7 days of termination" | "Within 90 days" | Negotiate based on technical feasibility. Specify secure deletion method and certification |
| Liability cap | Uncapped for data protection breaches | Capped at contract value | POPIA does not prescribe — contractual matter. Consider insurance requirements |
| Indemnification | Operator indemnifies for breaches caused by its acts or omissions | Limited to direct damages | Align with s19 accountability — the operator's failure is the responsible party's regulatory risk |

---

## 7. Review framework — when we are the operator

When acting as operator (processing PI on behalf of a client/responsible party), assess the operator agreement from the operator's perspective:

### Operator-side checklist

| # | Check | POPIA basis | Risk if missing |
|---|---|---|---|
| 1 | Does the agreement clearly identify us as operator? | s21 | Status confusion — may be treated as responsible party with full s8 accountability |
| 2 | Are instructions from the responsible party documented in writing? | s21(2) | Processing without authorisation may constitute unlawful processing |
| 3 | Are security measure obligations reasonable and achievable? | s19 via s21 | Over-commitment creates contractual liability |
| 4 | Is breach notification timeline realistic? | s22 | "Immediately" may not be technically possible — negotiate "as soon as reasonably possible" |
| 5 | Are sub-operator arrangements addressed? | Good practice | If we use sub-operators, ensure mechanism for responsible party approval |
| 6 | Does the agreement address cross-border considerations? | s72 | If we host or access data from outside SA, s72 binding agreement needed |
| 7 | Are direct marketing restrictions clear? | s69 | If we conduct marketing on behalf of the responsible party, consent obligations must be specified |
| 8 | Is PI return/deletion feasible within the stated timeline? | s14, s19 | Technical limitations on deletion from backups must be disclosed |
| 9 | Is the liability allocation proportionate to the fee? | Contractual | Unlimited liability for a low-value contract creates existential risk |
| 10 | Are audit rights proportionate? | Contractual | On-demand audits may be disproportionate — negotiate scheduled audits with reasonable notice |

---

## 8. High-risk flags

| # | Flag | Statute | What to check | Enforcement precedent |
|---|---|---|---|---|
| 1 | No written operator agreement | POPIA s21(1) | Is there a written contract between the responsible party and every operator? Does it address s19 security measures? | Dis-Chem (enforcement notice — 3.6M records breached via uncontracted third party Grapevine) |
| 2 | Operator agreement uses GDPR terminology without adaptation | POPIA s21, s72 | Does the agreement reference "controller/processor", "SCCs", "DPO", "DPIA", "Article 28"? These terms have no legal effect under POPIA | Common finding in multinational operator arrangements |
| 3 | No cross-border safeguards for foreign operator | POPIA s72 | Is the operator located outside SA? Are sub-operators in foreign countries? Is cloud hosting outside SA? Is there a binding agreement? | No enforcement yet — IR guidance note expected 2025/26 |
| 4 | Operator conducting direct marketing without consent confirmation | POPIA s69, Regs 2025 | Has the responsible party confirmed valid consent before instructing operator to market? Is telemarketing recorded? | FT Rams (R100K fine — responsible party liable for marketing non-compliance) |
| 5 | Security measures not specified in agreement | POPIA s19 via s21(1) | Does the agreement specify technical and organisational measures? Or does it merely reference "appropriate measures" without detail? | Dis-Chem (weak passwords, insufficient access controls at operator level) |
| 6 | Sub-operators engaged without responsible party knowledge | Good practice (s8 accountability) | Does the operator use sub-operators? Is the responsible party aware? Can the responsible party object to or approve sub-operators? | Responsible party bears regulatory risk for entire processing chain |
