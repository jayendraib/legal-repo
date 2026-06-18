# Boolean / Terms-and-Connectors syntax — per-database reference

A reference for the `boolean-search` skill. The controlling authority is **each database's own current search guide** —
connector grammars are stable but field/segment names and the specialist databases' operators change. Tag anything
beyond the core connectors below `[verify against the database's current search guide]`.

The two primary databases have full Terms-and-Connectors grammar. The three specialists have weak or partial Boolean —
build a tight Boolean for Westlaw/Lexis and a stripped-down keyword/phrase version for the specialists.

---

## The one difference that breaks ported searches

**A space between two words is not the same operator across databases.**

- **Westlaw:** a space = **OR**. `breach contract` finds documents with *breach* OR *contract*.
- **Lexis:** adjacent words with no connector = a **phrase**. `breach contract` finds the phrase "breach contract".

The identical string is a broad OR on one database and a narrow phrase on the other. Always translate the space
deliberately when porting, and never hand over a string without naming its database.

---

## Westlaw — Terms and Connectors

| Function | Operator | Example | Notes |
|---|---|---|---|
| OR | *(a space)* | `car automobile vehicle` | the default between terms |
| AND | `&` or `and` | `negligence & damages` | |
| Phrase | `"..."` | `"res ipsa loquitur"` | exact phrase |
| Same paragraph | `/p` | `landlord /p repair!` | |
| Same sentence | `/s` | `damag! /s remote!` | |
| Within n terms (either order) | `/n` | `breach /5 contract` | n = 1–255 |
| Order-sensitive within sentence | `+s` | `donor +s gift` | first term precedes second, same sentence |
| Order-sensitive within n terms | `+n` | `prior +3 art` | first precedes second within n |
| BUT NOT (exclude) | `%` | `damages % punitive` | excludes documents with the second term |
| Root expander (truncation) | `!` | `negligen!` | unlimited trailing characters |
| Universal character (one char) | `*` | `wom*n` → woman/women | one `*` per character; trailing `*`s cap word length |
| Turn off plurals/equivalents | `#` | `#fee` | forces the exact form only |
| Field/segment restriction | `field(...)` | `ti("hadley" "baxendale")` | e.g. `ti()` title, `sy,di()` synopsis/digest, `he()` headnote — `[verify field names]` |

Westlaw auto-retrieves regular and irregular plurals and possessives; use `#` to suppress.

---

## Lexis (Lexis+) — Terms and Connectors

| Function | Operator | Example | Notes |
|---|---|---|---|
| OR | `or` | `car or automobile` | spelled out — a space is *not* OR here |
| AND | `and` or `&` | `negligence and damages` | |
| Phrase | adjacency or `"..."` | `res ipsa loquitur` | consecutive words are read as a phrase |
| Same paragraph | `w/p` | `landlord w/p repair!` | |
| Same sentence | `w/s` | `damag! w/s remote!` | |
| Within n words (either order) | `w/n` | `breach w/5 contract` | |
| Order-sensitive within n | `pre/n` | `prior pre/3 art` | first term precedes second within n |
| Not within n | `not w/n` | `bank not w/3 river` | excludes when within n words |
| AND NOT (exclude) | `and not` | `damages and not punitive` | place last in the query |
| Same segment | `w/seg` | `name(smith) w/seg ...` | segment-scoped proximity |
| Root expander (truncation) | `!` | `negligen!` | unlimited trailing characters |
| Universal character (one char) | `*` | `wom*n` | one `*` per character |
| Segment restriction | `segment(...)` | `name(hadley)` | e.g. `name()`, `writtenby()`, `headline()` — `[verify segment names]` |

Lexis auto-retrieves plurals and possessives.

### Westlaw ↔ Lexis quick port

| Concept | Westlaw | Lexis |
|---|---|---|
| OR | *(space)* | `or` |
| AND | `&` | `and` |
| same sentence | `/s` | `w/s` |
| same paragraph | `/p` | `w/p` |
| within n | `/n` | `w/n` |
| ordered within n | `+n` | `pre/n` |
| exclude | `%` | `and not` |
| phrase | `"..."` | adjacency or `"..."` |

Lossy spots to flag on every port: Westlaw `+s` (ordered, same sentence) has no clean Lexis equivalent — approximate
with `pre/n` and flag; Westlaw's space-as-OR silently becomes a Lexis phrase if not rewritten.

---

## Specialist databases — weak / partial Boolean

These cover international, comparative, and investment-treaty material that Westlaw/Lexis cover thinly. Their search
engines are built more for browsing and semantic retrieval than for Boolean precision. **Graceful degradation:** drop
proximity connectors (they are typically ignored), keep phrases and AND/OR, and tell the user what you dropped and why.
Treat every operator below as `[verify against the database's current search guide]`.

### Kluwer Arbitration

- Generally supports basic `AND`, `OR`, `NOT`, quoted `"phrases"`, and a `*` wildcard; offers fielded/advanced search
  (by title, author, institution, date) but limited or no reliable proximity connectors.
- Strategy: a few quoted terms of art joined by AND, plus the fielded filters; rely on the filters, not proximity.

### Jus Mundi

- Built around **semantic / natural-language** search across multilingual treaty and case material; Boolean support is
  limited. Quoted exact phrases are the most reliable precision lever; AND/OR may be partial.
- Strategy: feed it the concept as a natural-language phrase plus one or two quoted terms of art; do not expect
  proximity or nested Boolean to behave. Lean on its filters (instrument, decision type, date, jurisdiction).

### ITA Law (italaw.com)

- Primarily a **document repository** with a simple site search; weak Boolean — effectively keyword + quoted phrase.
- Strategy: a small set of quoted terms; as a fallback, a Google site-restricted search often outperforms the on-site
  engine: `site:italaw.com "fair and equitable treatment" "legitimate expectations"`.

---

## Building blocks (database-agnostic method)

1. **Buckets joined by AND.** A good search is 2–4 concept buckets joined by AND; each bucket is an OR-set of expanded
   terms. `(bucket A terms) AND (bucket B terms) AND (bucket C terms)`.
2. **Expand each bucket** with cognates (root expander, aimed to avoid over-reach) and alternative expressions
   (enumerated OR-set — synonyms do not share a root).
3. **Tie related terms with proximity,** not bare AND, where they must relate to each other to be on point — `/s` or
   `/p` (Westlaw) / `w/s` or `w/p` (Lexis) — to hold precision up without dropping recall to document-level co-occurrence.
4. **Parenthesise** every OR-set before joining with AND, so precedence is explicit.
5. **Truncate deliberately.** `repudiat!` is safe; `cler!` over-reaches (clerical/clergy/clerk) — prefer an explicit
   OR-list when a root bleeds into unrelated words.
