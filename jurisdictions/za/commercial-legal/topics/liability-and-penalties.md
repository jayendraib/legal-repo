# Liability and Penalties — South African Framework

This overlay covers the SA law of contractual penalties, liability limitation, damages, and prescription. It is loaded by vendor-agreement-review and saas-msa-review skills when jurisdiction = ZA.

---

## 1. Conventional Penalties Act 15 of 1962

SA law treats contractual penalty clauses as **enforceable**. This is the opposite of many US jurisdictions where penalty clauses are void and only "liquidated damages" (a reasonable pre-estimate of loss) are permitted. In SA, the correct terminology is "penalty stipulation" — avoid using "liquidated damages" in the US sense.

### s1 — enforceability

A penalty stipulation is any contractual provision that fixes in advance the consequences of a breach — whether as a monetary amount, a forfeiture, or an obligation to deliver or perform. All are valid and enforceable.

### s2 — no cumulation rule

**This is the most commonly triggered trap in cross-border contracts.**

Section 2 provides that a creditor who claims a penalty stipulation **cannot also claim damages** for the same breach, unless the contract **expressly** permits cumulation.

The rule operates as follows:

| Contract provides | Creditor may claim |
|---|---|
| Penalty clause only | Penalty OR damages (not both) — creditor must elect |
| Penalty clause + express cumulation permission | Penalty AND damages for the same breach |
| No penalty clause | Damages only (common law) |

**US-drafted contracts typically do not include express cumulation permissions** because the concept does not exist in US law. When reviewing a US-origin contract for SA use, the absence of a cumulation clause means the SA party must elect between the penalty and a damages claim — it cannot pursue both.

### s3 — judicial reduction

A court may reduce a penalty if it is **out of proportion** to the prejudice suffered. The court considers:

1. The actual prejudice suffered by the creditor
2. The circumstances in which the penalty was agreed
3. The relationship between the penalty amount and the loss
4. The financial position of the parties

This is a discretionary power, not an automatic right. The debtor bears the onus of proving that the penalty is disproportionate.

### s4 — forfeiture as penalty

Any provision for forfeiture (e.g., forfeiture of a deposit on breach) is treated as a penalty stipulation. The same no-cumulation rule and judicial reduction power apply.

### High-risk flag: Penalty-damages cumulation trap

| Check | What to look for |
|---|---|
| Penalty clause present | Contract contains a clause fixing a monetary amount or other consequence for breach |
| Damages clause for same breach | Separate clause entitling the innocent party to claim damages for the same breach event |
| Express cumulation permission | Specific language permitting the creditor to claim BOTH the penalty and damages for the same breach |
| Forfeiture provisions | Any forfeiture clause (deposit, prepayment) — treated as a penalty under s4 |
| SLA service credits | SLA service credits that function as penalties — separate damages claim for same outage? |

**Why this matters:** Without express cumulation permission, a party that claims the penalty is barred from claiming damages for the same breach (and vice versa). Most US-drafted agreements do not account for the Conventional Penalties Act, leaving the SA party with a forced election it did not intend.

---

## 2. SA damages taxonomy

SA contract law distinguishes between general and special damages, but the test for remoteness differs from the English law position (Hadley v Baxendale):

### General damages

Damages that arise **naturally and generally** from the breach — the normal, foreseeable consequences. These are recoverable without specific proof that the defendant contemplated them.

### Special damages

Damages arising from **special circumstances** known to both parties at the time of contracting. The SA test, established in **Lavery v Jungheinrich AG** and subsequent cases, is stricter than the English Hadley v Baxendale test:

1. The special circumstances must have been **within the contemplation of both parties** at the time of contract.
2. The defaulting party must have **tacitly agreed to bear liability** for the special damages — mere knowledge of the special circumstances is not enough.
3. The claimant must prove that the special damages were a **probable consequence** of the breach in the special circumstances.

### Practical impact on limitation clauses

When drafting or reviewing limitation of liability clauses for SA:

- Excluding "consequential damages" without defining the term is ambiguous in SA law — the general/special distinction does not map neatly to direct/consequential
- Specify which heads of loss are excluded (e.g., loss of profit, loss of data, business interruption) rather than using the undefined "consequential damages" label
- Exclusion of general damages is uncommon and may face a reasonableness challenge

### Drax Energy — per-claim vs aggregate cap

In the **Drax Energy** matter (Cliffe Dekker Hofmeyr, March 2024), the court addressed the interpretation of liability caps in commercial contracts. The key takeaway:

- A cap expressed as "aggregate liability" applies to all claims combined
- A cap expressed as "liability per claim" or "per event" applies separately to each breach
- Ambiguous drafting (cap without specifying per-claim or aggregate) is construed against the party seeking to rely on the cap (contra proferentem)

Draft liability caps with explicit per-claim and aggregate mechanics to avoid this ambiguity.

---

## 3. Specific performance and liability caps

Because specific performance is the primary remedy in SA law (see contract-fundamentals.md), liability caps have a different risk profile than in US contracts:

1. **Court can order performance** — a liability cap limits monetary exposure but does not prevent a court from ordering the defaulting party to perform the contract in full.
2. **Interdict available** — the innocent party can obtain an interdict (court order) compelling or prohibiting specific conduct, separate from any monetary claim.
3. **Cap carve-outs** — SA practitioners typically carve out from the cap: breach of confidentiality, IP infringement, wilful misconduct, gross negligence, and specific performance obligations.

### CPA s51 — prohibition on excluding gross negligence

Where the CPA applies (see contract-fundamentals.md for the applicability threshold):

- **s51(1)(c)(i)** renders void any term purporting to limit or exempt a supplier from liability for **gross negligence**.
- This is a statutory prohibition — it cannot be waived by the consumer.
- The term is void and severable; the remainder of the contract survives.

Even where the CPA does not apply, SA courts may scrutinise the exclusion of liability for gross negligence under the public policy limitation on pacta sunt servanda (Beadica).

### High-risk flag: Uncapped liability + specific performance exposure

| Check | What to look for |
|---|---|
| Liability cap present | Is there a monetary cap on the defaulting party's liability? |
| Cap carve-outs defined | Are the standard SA carve-outs included (wilful misconduct, gross negligence, breach of confidentiality, IP infringement)? |
| Specific performance excluded | Has the contract addressed the right to claim specific performance, or is it available in addition to damages up to the cap? |
| CPA applicability | If CPA applies, gross negligence exclusion is void under s51 regardless of contract terms |
| Per-claim vs aggregate | Is the cap per-claim, per-event, or aggregate? Ambiguity creates Drax Energy risk |

**Why this matters:** US-style uncapped liability is significantly more dangerous in SA because a court can compel performance in addition to awarding damages. A party with uncapped liability and no specific performance exclusion faces both monetary and performance exposure. Where the CPA applies, the inability to exclude gross negligence further increases exposure.

---

## 4. SA indemnity conventions

SA law recognises indemnity clauses, but several SA-specific rules apply:

### Interpretation

- An indemnity is construed strictly (contra proferentem against the party seeking indemnification).
- An indemnity that purports to indemnify a party against the consequences of its own negligence must do so in **express and unambiguous terms** — general words are insufficient.
- The SA courts follow the approach in **Durban's Water Wonderland v Botha** — an indemnity against "any claim" does not, without more, cover claims arising from the indemnified party's own negligence.

### Indemnity vs damages

An indemnity operates differently from a damages claim:

| Feature | Indemnity claim | Damages claim |
|---|---|---|
| Trigger | Third-party loss or specified event | Breach of contract |
| Remoteness test | As specified in the indemnity clause | General/special damages (Lavery v Jungheinrich) |
| Interaction with penalty clause | Typically not a penalty (different trigger) | Subject to Conventional Penalties Act if penalty stipulated |
| Prescription | 3 years from when indemnity obligation arises | 3 years from breach (debt) or 6 years (other) |

### CPA constraints

Where the CPA applies, an indemnity requiring the consumer to indemnify the supplier against loss caused by the supplier's own fault is void (CPA s51).

---

## 5. Prescription Act 68 of 1969

The Prescription Act sets time limits within which claims must be brought. Once a claim prescribes, it is extinguished — it cannot be revived.

### Prescriptive periods (s11)

| Claim type | Period |
|---|---|
| Debt (including contractual claims for money) | 3 years |
| Any other claim (including specific performance, interdict) | 6 years |
| Claim against the state (State Liability Act) | 3 years |
| Mortgage bond | 30 years |
| Judgment debt | 30 years |

### When prescription begins (s12)

Prescription begins to run when the debt becomes **due** — meaning when the creditor acquires a complete cause of action, including knowledge of the identity of the debtor and the facts giving rise to the claim.

### Delay of prescription (s13)

Prescription is delayed (does not run) during certain periods:

- While the creditor is a minor, mentally ill, or under curatorship
- While the debtor is outside the Republic and the cause of action cannot be pursued in SA courts
- While the creditor and debtor are married to each other
- While there are pending negotiations that could lead to settlement (interruption, not delay)

### Barkhuizen v Napier — contractual limitation periods

The Constitutional Court held in **Barkhuizen v Napier** (2007) that a contractual limitation period shorter than the Prescription Act period is not per se unenforceable, but must meet a two-stage test:

1. **Objective fairness** — is the clause objectively reasonable, having regard to the purpose it serves?
2. **Subjective fairness** — was it fair to enforce the clause against this particular party in these circumstances?

An unconscionably short limitation period (e.g., 30 days to notify a claim) may be unenforceable on public policy grounds, even between sophisticated commercial parties.

---

## 6. Must-not-contain reference

When jurisdiction = ZA, liability review skills must not use the following US terms:

| US term | SA replacement |
|---|---|
| "liquidated damages" (US sense) | penalty stipulation (Conventional Penalties Act) |
| "Hadley v Baxendale" | SA damages taxonomy (Lavery v Jungheinrich) |
| "punitive damages" | Not available in SA contract law |
| "preliminary injunction" | interdict |
| "statute of limitations" | prescription (Prescription Act 68 of 1969) |
| "consequential damages" (undefined) | Specify heads of loss; use general/special distinction |
