# Confidentiality and Restraint of Trade — South African Framework

This overlay covers NDA enforceability, the SA restraint of trade doctrine, interdict procedures, and POPIA interaction with confidentiality obligations. It is loaded by nda-review and vendor-agreement-review skills when jurisdiction = ZA.

---

## 1. NDA enforceability under SA common law

Non-disclosure agreements are fully enforceable under SA common law. The key principles:

### Formation

An NDA is a standard contract governed by SA common law principles:

- No consideration required (see contract-fundamentals.md) — a unilateral NDA (one party disclosing, one party receiving) is enforceable without the receiving party providing anything in return.
- Consensus ad idem — the parties must agree on the scope of confidential information, the obligations, and the duration.
- ECTA governs electronic execution (see contract-fundamentals.md) — standard electronic signatures are sufficient.

### Scope of confidential information

SA courts will enforce confidentiality obligations that are clearly defined and reasonable. The definition of confidential information should:

1. **Be specific enough to be identifiable** — "all information" is too broad and may be unenforceable. Identify categories: technical data, financial information, customer lists, business strategies.
2. **Include standard exclusions** — information in the public domain, independently developed, received from third parties without restriction, required to be disclosed by law or court order.
3. **Address residual knowledge** — SA law does not have a well-developed "residuals" doctrine. If parties intend that knowledge retained in unaided memory is excluded, this must be expressly stated.

### Duration

There is no statutory maximum duration for confidentiality obligations. SA courts will enforce reasonable durations. Typical ranges:

| Context | Typical duration |
|---|---|
| Pre-transaction due diligence | 2-3 years |
| Technology partnership | 3-5 years |
| Employment-related | Duration of employment + 1-3 years |
| Trade secrets | Indefinite (until information enters public domain) |

An indefinite confidentiality obligation for trade secrets is enforceable in SA, provided the definition of trade secrets is clear and the information genuinely qualifies.

### Remedies for breach

The primary remedies for breach of an NDA are:

1. **Interdict** — a court order compelling the receiving party to stop using or disclosing the information (see section 4 below).
2. **Damages** — compensation for loss suffered as a result of the breach.
3. **Specific performance** — a court order compelling the receiving party to return or destroy confidential information.

---

## 2. Restraint of trade doctrine

SA law diverges fundamentally from many US jurisdictions on restraint of trade. The foundational principle, established in **Magna Alloys and Research (SA) (Pty) Ltd v Ellis** (1984), is:

**A restraint of trade is presumed valid and enforceable. The onus is on the party seeking to escape the restraint to prove that it is unreasonable.**

This is the opposite of many US states where non-competes are presumed invalid, disfavoured, or prohibited outright (e.g., California).

### Basson v Chilwan 5-part reasonableness test

The Supreme Court of Appeal in **Basson v Chilwan** (1993) established the test for reasonableness of a restraint. The party seeking to escape the restraint must prove:

1. **Protectable interest** — does the party enforcing the restraint have a protectable interest that the restraint legitimately serves? Recognised protectable interests include:
   - Trade secrets and confidential information
   - Trade connections and customer relationships
   - The stability of the workforce (in employment context)
   - Goodwill associated with a business

2. **Prejudice** — is the party subject to the restraint prejudiced by its enforcement? The court considers the extent to which the restraint restricts the party's ability to earn a livelihood or conduct business.

3. **Proportionality** — is there a proportional balance between the interests of the parties? The restraint must not go further than necessary to protect the legitimate interest.

4. **Public policy** — does the restraint offend public policy? A restraint that creates a monopoly, unreasonably restricts competition, or is contrary to constitutional values may be struck down.

5. **Necessity** (5th limb from **Kwik Kopy (SA) (Pty) Ltd v van Haarlem**) — is the restraint necessary to protect the interest identified? Could a less restrictive alternative achieve the same protection?

### Beadica and pacta sunt servanda

The Constitutional Court in **Beadica 231 CC v Trustees for the time being of Oregon Trust** (2020) reaffirmed that contractual terms freely agreed between the parties are enforceable (pacta sunt servanda), subject to public policy. This strengthens the enforceability of reasonably drafted restraints.

However, the court also confirmed that public policy includes the values of the Constitution — equality, dignity, and freedom. A restraint that is grossly disproportionate or oppressive may be struck down on public policy grounds.

### Typical court-upheld parameters

SA courts have provided guidance on what they consider reasonable:

| Parameter | Typically upheld | Likely challenged |
|---|---|---|
| Duration | 3-4 months | 24+ months |
| Geographic scope | Province or major metropolitan area | Entire SA or worldwide (unless business is genuinely national/global) |
| Restricted activity | Specific competing activity | All commercial activity in any industry |
| Customer non-solicit | Named customers or customers dealt with | All customers of a national enterprise |

**Important:** These are guidelines, not bright-line rules. Each case turns on its facts, including the nature of the business, the seniority of the restrained party, and the specific protectable interest.

### Severability

SA law allows courts to sever an unreasonable restraint provision if the reasonable and unreasonable parts are severable. However, SA law does **not** have a "blue pencil doctrine" equivalent in the US sense — courts will not rewrite the restraint to make it reasonable. The court severs the offending provision and enforces the remainder, or strikes down the entire clause if the parts are not severable.

---

## 3. Non-compete and non-solicit in commercial context

Restraint of trade clauses appear in commercial contracts (not just employment agreements) in several contexts:

### Sale of business

Restraints in sale-of-business agreements are viewed more favourably by courts than employment restraints. The seller has received consideration (the purchase price) for the restraint, and the buyer has a clear protectable interest in the goodwill purchased. Courts typically uphold:

- Longer durations (12-24 months common)
- Broader geographic scope (matching the sold business's footprint)
- Broader activity restrictions (the specific business sold)

### Joint venture and partnership

Restraints between joint venture partners or partners are assessed similarly to sale-of-business restraints. The protectable interest is the joint venture's competitive position and the parties' investment in it.

### Franchise and distribution

Franchisor-franchisee restraints are common and generally enforceable where they protect the franchisor's intellectual property, trade secrets, and system goodwill. Competition Act s5 (see competition-and-bbbee.md) may apply if the restraint has the effect of substantially lessening competition.

### Exclusivity as restraint

An exclusivity clause in a commercial contract (exclusive supply, exclusive distribution) may function as a restraint of trade. The same Basson v Chilwan analysis applies, with additional Competition Act considerations (see competition-and-bbbee.md section on exclusivity).

---

## 4. SA interdict procedures

The interdict is the SA equivalent of an injunction. It is the primary enforcement mechanism for restraint of trade and confidentiality breaches.

### Types of interdict

| Type | Purpose | Standard |
|---|---|---|
| Interim interdict | Temporary order pending final determination | See requirements below |
| Final interdict | Permanent order after trial | Proved right, proved breach, no alternative remedy |
| Rule nisi | Interim order calling on respondent to show cause | Used in urgent applications |

### Requirements for interim interdict

The applicant must establish:

1. **Prima facie right** — a right that, though open to some doubt, is not frivolous. In restraint/NDA cases, the contract itself is usually sufficient.
2. **Well-grounded apprehension of irreparable harm** — the applicant will suffer harm that cannot be adequately compensated by an award of damages if the interdict is not granted.
3. **Balance of convenience** — the balance of prejudice favours granting the interdict.
4. **No alternative remedy** — there is no other satisfactory remedy available to the applicant.

### Urgency (Webster v Mitchell)

The Supreme Court of Appeal in **Webster v Mitchell** established that an applicant seeking an urgent interdict must demonstrate:

- The matter cannot wait for the normal court process
- The applicant has not been dilatory — delay in bringing the application undermines the claim of urgency
- The consequences of not granting urgent relief are serious and irreversible

**Practical timeline:** An urgent interdict application in the High Court can be heard within 1-5 days of filing. A contested interim interdict on the normal roll takes 4-8 weeks. A final interdict at trial takes 12-24 months (longer in the Johannesburg division — see dispute-resolution.md).

---

## 5. POPIA interaction with NDAs

Where an NDA covers personal information, POPIA creates additional obligations beyond the contractual confidentiality framework. This interaction is relevant in several scenarios:

### Due diligence

Where parties exchange personal information (employee records, customer databases, supplier details) under an NDA for due diligence purposes:

1. The disclosing party is the **responsible party** for the personal information.
2. The receiving party is an **operator** to the extent it processes the information.
3. An **operator agreement** (POPIA s21) is required — the NDA alone does not satisfy POPIA. The operator agreement must address processing-on-instruction, security safeguards, breach notification, and return/deletion (see data-protection.md).
4. **Purpose limitation** — POPIA s13 requires that personal information be processed only for the purpose collected. The NDA should specify the due diligence purpose, and the receiving party must not use the personal information for any other purpose.

### Post-termination obligations

Upon termination of the NDA:

- The NDA typically requires return or destruction of confidential information.
- POPIA s14 independently requires that personal information be destroyed or de-identified once the purpose for processing has been achieved.
- The obligations are complementary: the NDA addresses confidential information broadly, and POPIA addresses personal information specifically.
- The more onerous obligation applies — if the NDA requires return within 30 days but POPIA s14 requires immediate destruction, the earlier obligation controls.

### Breach notification

If personal information covered by the NDA is compromised:

- The **NDA** typically requires notification to the disclosing party.
- **POPIA s22** independently requires notification to the Information Regulator and data subjects.
- Both obligations run concurrently. The receiving party must notify both the disclosing party (under the NDA) and the responsible party/Information Regulator (under POPIA).

### High-risk flag: Overbroad restraint of trade

| Check | What to look for |
|---|---|
| Duration proportionate | Is the restraint duration proportionate to the protectable interest? Courts typically uphold 3-4 months in commercial context |
| Geographic scope defined | Is the geographic scope limited to the area where the protectable interest exists, or is it unreasonably broad? |
| Restricted activity specific | Is the restricted activity specific to the protectable interest, or does it sweep in unrelated activities? |
| Protectable interest identified | Has the contract identified a specific protectable interest (trade secrets, customer connections, goodwill)? |
| Proportionality | Does the restraint go further than necessary to protect the identified interest? |
| Commercial vs employment | Is this a sale-of-business restraint (more likely upheld) or an employment-type restraint dressed up in commercial terms? |

**Why this matters:** While SA law presumes restraints valid, courts routinely strike down overbroad restraints under the Basson v Chilwan test. An unenforceable restraint provides no protection — it is worse than a well-drafted, narrower restraint that a court would uphold. The 5th limb (necessity, from Kwik Kopy v van Haarlem) means that if a less restrictive alternative exists, the broader restraint may fail.

---

## 6. Must-not-contain reference

When jurisdiction = ZA, confidentiality and restraint review skills must not use the following US terms:

| US term | SA replacement |
|---|---|
| "preliminary injunction" / "TRO" | interdict (interim or final) |
| "non-compete per se invalid" | SA presumes restraints valid (Magna Alloys v Ellis) |
| "blue pencil doctrine" | SA severability (courts sever, not rewrite) |
| "consideration" (as formation requirement) | Not required — unilateral NDA enforceable |
| "inevitable disclosure doctrine" | Not recognised in SA — must prove actual misuse |
| "Defend Trade Secrets Act" / "UTSA" | SA common law trade secret protection |
| "attorney work product" | legal professional privilege |
