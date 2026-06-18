# Changelog — singapore-court-legal

## 0.2.0 — guided analysis
- New tool: `analyze_situation` — a structured guided memo over a fact pattern (situation summary, relevance-gated reasoning chain, abstentions, perceived facts, attached case authorities). Full parity with the web guided path: same core, same gates, same citation firewall.
- Reasoning chains in the guided memo are **relevance-gated** (doctrine-coherent corridors only); chain coverage varies by doctrine and honest chain-absence is surfaced, never padded.
- Three-tool routing documented (`ask` · `conversation_turn` · `analyze_situation`).
- Bounds (rate, input ceiling, monthly token budget) apply to the guided turn as to the others.

## 0.1.0 — initial packaging (marketplace-submission candidate)
- MikeROS MCP connector over the Singapore Rules of Court 2021 reasoning server.
- Tools: `ask` (single-shot), `conversation_turn` (durable multi-turn).
- Coverage: 67 Orders / 738 rules; staged case authorities (O5/O21 today); verified chains.
- API-key auth (operator-issued); per-key bounds (20/min, 4k input, 5M tokens/month).
- Results carry provenance (source + retrieval timestamp + citation identifiers); honest-claims SKILL.md; per-key isolation + 7-day retention.
