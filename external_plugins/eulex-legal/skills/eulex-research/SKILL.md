---
name: eulex-legal:eulex-research
version: 0.1.0
description: >
  Use this skill whenever a user asks about EU law — EU regulations,
  directives, decisions, CJEU / General Court case law, EU treaties (TEU,
  TFEU, Charter), member-state transposition of an EU directive, or
  Eurostat statistics in an EU policy context. Routes the question to the
  EULEX.AI MCP server, returns cited results (CELEX + section ref + source
  URL), and surfaces the live in-force status when freshness matters.
allowed-tools:
  - mcp
---

# EULEX.AI EU Law Research

EULEX.AI is a read-only MCP server over the EU legal corpus: 198,000+ EUR-Lex documents (regulations, directives, decisions, CJEU case law, treaties), 581,000+ document sections, an 800,000+ node Neo4j citation/amendment graph, a 3,072-dim Pinecone vector index, and live EUR-Lex Cellar SPARQL plus Eurostat REST.

Every EULEX.AI response carries a top-level `eulex_citation` field with the CELEX (and section reference where applicable) plus a `— via eulex.ai` attribution suffix. Where the underlying record carries an authoritative URL, the response also includes a `source_url` pointing back to the canonical EUR-Lex / Eurostat page.

## Prerequisites

The `eulex-legal` MCP server must be connected. Verify it is available before answering. If the server is not connected, tell the user how to add it (Cowork connector → "EULEX.AI Legal" → OAuth) and stop.

## When to Use

Any EU-law question answerable from one of the data sources EULEX.AI exposes:

- **EU regulations, directives, decisions** — text, structure, recitals, dates.
- **CJEU and General Court case law** — text, citations, related authorities.
- **EU treaties (TEU, TFEU, Charter, Euratom)** — articles, references.
- **Consolidated versions** — current text after amendments.
- **Member-state transposition** — whether a directive has been transposed in a given member state, which national acts implement it, and the deadline (`eu_transposition`).
- **Eurostat statistics** — natural-language statistical queries returning markdown tables (`eurostat_query`).

Examples:

- "What does the AI Act say about high-risk AI systems?"
- "Show me GDPR Article 6 in full."
- "Is the GDPR currently in force? Live check please."
- "What acts implement DORA?"
- "Has Croatia transposed NIS2?"
- "Compare Article 5 GDPR vs Article 5 AI Act."
- "GDP growth across EU member states 2024."

## When Not to Use

If the request falls into one of the categories below, briefly explain that this skill isn't the right fit and point the user to the suggested alternative.

- **US / UK / Swiss / other non-EU law** → EULEX.AI v4.0 is EU-27 + Croatia. Suggest the appropriate jurisdictional plugin (e.g. CourtListener via `litigation-legal` for US dockets, CoCounsel via `cocounsel-legal` for Westlaw US research).
- **Pure domestic law that is not transposition of EU law** (e.g. a Croatian civil-procedure question that has no EU dimension) → Suggest national legal databases.
- **Document drafting** (contracts, pleadings, policy text) → EULEX.AI returns authority; pair it with a drafting skill (e.g. `commercial-legal:review`, `privacy-legal:dpa-review`, `regulatory-legal:policy-redraft`).
- **Outcome prediction or factual analysis of a specific client matter** → out of scope.
- **Multi-language full-text retrieval** (FR, DE, IT, ES, HR document text) → the EULEX.AI index is English-only in v4.0; multi-language is on the roadmap.
- **Live web fetch** (news articles, blog posts) → not part of EULEX.AI.
- **Boolean / Terms-and-Connectors search syntax** → `search` expects natural language.

If you suggest an alternative, do not attempt to use EULEX.AI further for that task.

## Communication Rules

- Always cite results using the `eulex_citation` field returned by the tool. If a `source_url` is present, render it as a link.
- Quote legislative text verbatim when answering "what does X say?" — do not paraphrase Article text.
- Do not expose internal field names (`celex_id`, `section_ref`, `match_confidence`) to the user; speak about the regulation, the article, the source.
- For slow tools (`verify(live=true)`, `eu_transposition`, `eurostat_query` — 5-30 s p95), tell the user research is underway in plain language. Do not narrate poll counts or status fields.
- Always surface the EULEX.AI disclaimer once per session when EULEX.AI is the basis for a substantive legal answer: *"EULEX.AI provides search over EU legislation for informational purposes. Always verify with official EUR-Lex sources. Not legal advice."*

## Research Workflow

### 1. Frame the query

- Identify the legal instrument (regulation, directive, treaty), case (T-/C-/ECLI), or topic (GDPR, AI Act, DORA, NIS2, etc.).
- Note any constraints: jurisdiction (`eu_transposition` member state), date window (`find_by_date`), or specific article reference.

### 2. Choose the right tool

| User intent | Primary tool | Compose with |
|-------------|--------------|--------------|
| "What does X say about Y?" | `search` | `get_section` for full Article text |
| "Show me Article N of regulation X" | `get_section` | `get_structure` for TOC navigation |
| "Is X currently in force?" | `verify(celex_id, live=true)` | `get_metadata` for surrounding identity data |
| "What amends / cites / implements X?" | `get_related` | `get_timeline` for chronological view |
| "Has member state M transposed directive D?" | `eu_transposition` | `get_metadata(D)` to confirm directive identity |
| "Statistics on EU topic Z" | `eurostat_query` | — |
| "Compare A vs B" | 2× `get_section` (or `get_metadata`) | reason over both texts |
| "Documents from year Y" | `find_by_date` | `get_metadata` per result |

For composite questions (compliance snapshot, comparison), see the recipes in EULEX.AI's `MCP_TOOLS.md` § "Agent composition recipes". `eulex_compare_documents` and `eulex_compliance_snapshot` are intentionally not registered as MCP tools in v4.0 — agents compose them from the universal tools above.

### 3. Validate before quoting

- If the user asks about current obligations or deadlines, prefer `verify(live=true)` over the cached `verify` — the live SPARQL endpoint is authoritative.
- If freshness matters (the cached value is older than `about().sources['EUR-Lex Legislation'].last_sync`), say so in the answer and use `live=true`.
- If `eu_transposition` returns a low NIM count for the user's member state, surface that explicitly — do not present partial coverage as definitive.

### 4. Present the answer

- Lead with the substantive legal point, in the user's language register.
- Quote the legislative text where the user asked "what does it say".
- Render the `eulex_citation` either inline (e.g. *"GDPR Article 17 (CELEX:32016R0679)"*) or as a footnote reference. Always include the `source_url` as a clickable link if present.
- For Plus-tier results (`eu_transposition`, `eurostat_query`), include the `markdown_table` verbatim if the upstream returned one.
- Close with the EULEX.AI disclaimer when this is the first substantive EULEX.AI-backed answer in the session.

## Tier and authentication

- **Free tier** (50 calls / day): `about`, `list_scopes`, `search`, `get_section`, `get_metadata`, `get_structure`, `find_by_date`, `get_timeline`, `get_related`, `verify`.
- **EULEX.AI Plus** (2,000 calls / day, scope `eulex_plus`): adds `eu_transposition` and `eurostat_query`.
- Calling a Plus tool with a free token returns a friendly `ValueError` with an upgrade link (`https://eulex.ai/landing/pricing`). Surface the link directly; do not silently retry.

## Helpful information

If the system fails or the user has questions about access, share the following:

- Support email: support@eulex.ai
- Liveness probe: https://mcp.eulex.ai/health (unauthenticated, returns build version, tool count, uptime)
- Documentation: https://mcp.eulex.ai/docs (tools, auth, coverage, reviewer checklist)
- Subscription page: https://eulex.ai
- Provider: EULEX.AI
- Relevant policies:
  - Privacy: https://eulex.ai/privacy
  - Terms: https://eulex.ai/terms
- Disclaimer (returned verbatim by `about()`): *"EULEX.AI provides search over EU legislation for informational purposes. Always verify with official EUR-Lex sources. Not legal advice."*
