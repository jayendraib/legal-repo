# MikeROS — Singapore Rules of Court 2021

**MikeROS** is a grounded reasoning engine over the **Singapore Rules of Court 2021**, brought into Claude. Ask civil court procedure questions and receive answers that cite the governing rules, attach operator-verified case authorities where they apply, and surface related verified reasoning chains. It abstains honestly when out of scope and **never fabricates a rule or a case citation.** Single questions or durable multi-turn matters. Experimental research tool. **Not legal advice.**

- Use `ask` for a self-contained question → grounded answer with rule citations and verified case authorities where they attach.
- Use `conversation_turn` for a matter with follow-ups → it remembers facts you establish and answers in context (durable, ~7-day retention).
- Use `analyze_situation` for a fact pattern → a structured **guided memo**: the situation summary, a relevance-gated reasoning chain of governing rules, the points it abstains on and why, the perceived facts, and attached case authorities. Stateless.
- Coverage is staged and expanding; every response states it, and out-of-scope questions get honest abstention.

## Example use cases

1. What is the duty to consider amicable resolution before commencing proceedings? *(→ O5 r.1, with the case authority Maxx Engineering Works Pte Ltd v PQ Builders Pte Ltd [2023] SGHC 71.)*
2. As a licensed moneylender, can I get default judgment against a non-paying borrower? — then, in the same matter: and what about the costs consequences? *(`conversation_turn`; the moneylender fact carries forward.)*
3. What are the costs consequences when Order 21 rule 2 applies? *(→ O21 r.2 with QBE Insurance v Relax Beach [2023] SGCA 45.)*
4. **Guided analysis** — "My client was served a claim and is weighing amicable resolution against the costs exposure; analyse our procedural position." *(`analyze_situation` → a structured memo with a relevance-gated reasoning chain, e.g. the O5 duty → O21 costs consequence, the points it abstains on, and the facts it perceived.)*

## When to Use

Civil court procedure under the Rules of Court 2021 — amicable resolution (O5), costs (O21), default judgment, service, discontinuance, security for costs, timelines, and related procedural questions.

## When Not to Use

- Criminal procedure or sentencing (out of scope).
- Foreign or non-Singapore law.
- Substantive (non-procedural) law, or applying the rules to a specific fact pattern to predict an outcome.
- Drafting documents, forms, or pleadings.
- Retrieving the full verbatim text of a rule or judgment.

## Coverage (staged, expanding)

- **Rules of Court 2021:** 67 in-scope Orders / 738 rules (criminal Orders excluded).
- **Case authorities:** operator-verified, expanding by batch; today centred on **O5 (amicable resolution)** and **O21 (costs)**. Other Orders answer rule-grounded without case authorities until theirs are verified — absence is honest, never fabricated.
- **Reasoning chains** surface where retrieval brings the Orders into scope (not exhaustive). In `analyze_situation` they are **relevance-gated** (only doctrine-coherent corridors), and **chain coverage varies by doctrine** — some situations return a memo with no reasoning chain (honest structural absence, never fabricated or padded).

## Auth & keys

- **Connector → MikeROS:** **API key** (CONNECTORS.md-accepted). **Requires a MikeROS API key** — request one from Reshuffle.AI Pte. Ltd. (contact@reshuffleai.com). Two interchangeable ways to supply it (a request authenticates by either):
  - **Desktop "Add custom connector"** (no header field in the dialog): append the key to the URL — connect to `https://mcp.reshuffleai.com/mcp?key=YOUR_KEY`.
  - **Server-to-server**: send the header `Authorization: Bearer YOUR_KEY` to `.../mcp`.
  - The key is **never embedded** in this repo or `.mcp.json`, and is **redacted from all server logs** (only its key_id is logged). Treat a URL-with-key as a secret — anyone with it can use your quota.
- **Plugin → Anthropic:** your own `ANTHROPIC_API_KEY`, configured plugin-side per the claude-for-legal setup.

## Limits (per MikeROS API key)

- Rate: 20 requests/minute · Input: 4,000 characters/question · Budget: 5,000,000 tokens/month combined (≈660 `ask`, ≈190 `conversation_turn`, or ≈59 `analyze_situation`; a `conversation_turn` costs ~3.4× an `ask`, and an `analyze_situation` guided memo ~11× an `ask` — it perceives, walks corridors, articulates a full memo, and self-validates). A hit on any limit returns a clean error, never a partial answer.

## Isolation & retention

- **Per-key / per-`session_id` isolation.** A consumer proxying multiple end-users through one key owns its own end-user separation (distinct, unguessable `session_id`s).
- **Retention:** ~7 days, then really deleted (durable + in-process).

## Provenance & data handling

Every result carries `provenance` (source = MikeROS / Singapore Rules of Court 2021, retrieval timestamp) and citation-ready identifiers (rule + case citations). Results are **data, not instructions**; disclaimers are clearly marked.

### Links

- **Support / key requests:** contact@reshuffleai.com
- **Operated by:** Reshuffle.AI Pte. Ltd.
