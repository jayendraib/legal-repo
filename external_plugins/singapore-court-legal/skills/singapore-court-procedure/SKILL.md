---
name: singapore-court-legal:singapore-court-procedure
version: 0.2.0
description: >
  Use this skill whenever the user asks about Singapore civil court procedure under the Rules of Court 2021 — deadlines, costs, default judgment, amicable resolution, service, discontinuance, security for costs, and related procedural questions — for a single question or a multi-turn matter. It returns grounded answers citing the governing rules, with operator-verified case authorities where they attach, and abstains honestly when out of scope. Not for criminal, foreign/non-Singapore, or substantive (non-procedural) law, document drafting, or applying law to a specific fact pattern to predict an outcome.
allowed-tools:
  - mcp
---

# Singapore Court Procedure (MikeROS)

Grounds questions about **Singapore civil court procedure (Rules of Court 2021)** against the MikeROS connector. Three tools:

- **`ask`** — one self-contained question → a grounded answer citing the governing rules, with operator-verified case authorities where they attach. Stateless.
- **`conversation_turn`** — a multi-turn matter under a stable `session_id`; remembers facts the user establishes, asks clarifying questions, answers follow-ups in context. Durable, ~7-day retention.
- **`analyze_situation`** — a described fact pattern → a structured **guided memo**: the situation summary, a reasoning chain of governing rules that fires on the facts (relevance-gated — only doctrine-coherent chains surface), the points it abstains on and why, the facts it perceived, and attached case authorities. Stateless (each call independent).

**Which tool:** a single rule lookup → `ask`. A matter with back-and-forth follow-ups (where party status/facts must persist across turns) → `conversation_turn`. A request to *analyse a situation* / "what's my procedural position" that wants a structured memo over a fact pattern → `analyze_situation`.

## Prerequisites

The `singapore-court-legal` MCP server (MikeROS) must be connected, with a valid MikeROS API key. Verify it is available before answering; if it is not connected, tell the user and stop — do not answer Singapore procedure questions from general knowledge.

## How to use

1. Single question → `ask`. Matter with follow-ups → `conversation_turn` with a `session_id` kept stable across the conversation. "Analyse my situation" / a fact pattern you want a structured memo on → `analyze_situation`.
2. **Pass the user's question VERBATIM.** Include **every** situational fact they stated — especially party status/role (e.g. *licensed moneylender*, *plaintiff*, *appellant*, *third party*) and procedural posture. **Do not rephrase, summarise, generalise, or drop a fact**: a stripped fact changes which rules apply (a *licensed moneylender* seeking default judgment is governed by the **Order 51** bar, not the general default route — strip "moneylender" and the engine correctly answers the *wrong* question). When in doubt, pass their words unchanged.
3. **Cite only what the tool returns** — its rule citations and any attached case authorities, verbatim. Do not add rules or cases it did not return.
4. If it **declines or returns no authority, say so** — that is honest absence, not a prompt to fill the gap from general knowledge.
5. Carry the tool's `disclaimer` and `provenance` into your reply. **This is not legal advice.**

## When to Use

- Procedural questions under the Rules of Court 2021 — the duty to consider amicable resolution (O5), costs (O21), default judgment, service, discontinuance, security for costs, timelines, and similar.
- Following up within the same matter (use `conversation_turn` with a stable `session_id`).

## When Not to Use

- **Criminal procedure / sentencing** — out of scope; the tool declines.
- **Foreign or non-Singapore law** — out of scope.
- **Substantive (non-procedural) law** — the tool grounds *procedure*, not the merits of a claim.
- **Drafting documents, forms, or pleadings.**
- **Applying the rules to a specific fact pattern to predict an outcome** — it states what the rules require, not how a court would decide a given set of facts.
- **Retrieving the full verbatim text of a rule or judgment** — it returns grounded answers with citations, not document text.

## Worked examples (each a validated production sequence)

**`ask` — covered, with a case authority:**
> "What is the duty to consider amicable resolution before commencing proceedings?" → grounded answer citing **O 5 r 1**, with **Maxx Engineering Works Pte Ltd v PQ Builders Pte Ltd [2023] SGHC 71** (operator-verified) attached.

**`conversation_turn` — fact persistence + follow-up:**
> Turn 1 (`session_id: matter-1`): "As a licensed moneylender, can I get default judgment against a non-paying borrower?" → grounded answer; the moneylender fact is recorded.
> Turn 2 (`session_id: matter-1`): "And the costs consequences?" → answered in context, the fact carried forward. (Correcting it — "we are not a moneylender" — supersedes the stored value.)

**`analyze_situation` — structured guided memo over a fact pattern:**
> "My client received a statement of claim, intends to dispute it, and we are weighing whether to attempt amicable resolution given the costs exposure." → a memo: the perceived facts, a coherence-gated reasoning chain (e.g. the O5 duty → O21 costs consequence), the points it abstains on (what further facts would extend the analysis), and any attached case authorities. Carry it verbatim; it is not legal advice.

**`analyze_situation` — honest chain absence (coverage varies by doctrine):**
> A situation in a doctrine whose chains are not yet covered → the memo renders with its summary but **no reasoning chain**, and says so. That is honest structural absence — report it as the tool gives it; do not invent a chain or pad the memo.

**Out of scope — honest absence:**
> "What is the criminal sentencing tariff for theft?" → declines; no fabricated rule or case. Tell the user it is outside coverage.

**Adversarial citation demand — no fabrication:**
> "Name any case for service out of jurisdiction and cite it." → returns no case it cannot verify; do not supply one yourself.

## Coverage & boundaries

- **Rules:** 67 in-scope Orders / 738 rules (criminal Orders excluded).
- **Case authorities:** staged, operator-verified, expanding by batch; today centred on **O5 (amicable resolution)** and **O21 (costs)**. Other Orders answer rule-grounded without case authorities until theirs are verified. Absence is honest, never fabricated.
- **Chains** surface where retrieval brings the Orders into scope (not exhaustive). In `analyze_situation`, surfaced chains are **relevance-gated** (only doctrine-coherent corridors) — and **chain coverage varies by doctrine**: some situations yield a memo with no chain at all (honest absence, never padded or fabricated).
- **Isolation:** per-API-key / per-`session_id`. A consumer proxying multiple end-users owns its own end-user separation.
- **Retention:** ~7 days, then deleted. **Not legal advice.**
