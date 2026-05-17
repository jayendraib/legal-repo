# Jurisdiction Expansion Skill — Design Spec

**Date:** 2026-05-17
**Status:** Approved

---

## Purpose

A project-level skill that codifies the SA overlay architecture and guides adaptation of new practice areas through a structured interview. It replaces the manual grilling process used for employment-legal with a repeatable, research-assisted workflow.

## Skill Identity

- **Name:** `jurisdiction-expansion`
- **Location:** `.claude/skills/jurisdiction-expansion/SKILL.md`
- **Invocation:** `/jurisdiction-expansion [practice-area]` (e.g., `/jurisdiction-expansion commercial-legal`)
- **Argument:** optional plugin name — if provided, skips Step 1
- **Trigger phrases:** "expand to commercial-legal", "adapt privacy-legal for SA", "add a new practice area", "jurisdiction expansion"

## Context Loaded at Start

1. `jurisdictions/za/ARCHITECTURE.md` — directory layout, file schemas, wiring mechanism, step-by-step guide for adding a practice area
2. `project/decisions/001-sa-overlay-architecture.md` — rationale for architecture decisions (so the skill can explain *why*)
3. Target plugin's skill directory listing — to assess which skills need overlays
4. `jurisdictions/za/statutes/` directory listing — to know which statutes already exist and can be shared
5. Any existing `jurisdictions/za/{plugin-name}/` content — to detect partial prior work

## Interview Structure

Eight steps with a fixed skeleton and adaptive follow-up depth. Each step has a predefined opening question but can go deeper based on the user's answers.

### Step 1: Target Plugin

- Which plugin are you adapting? (auto-filled if passed as argument)
- Read the plugin's `.claude-plugin/plugin.json`, list all skills, read the CLAUDE.md template
- Confirm the practice area scope with the user
- Check for prior partial work in `jurisdictions/za/{plugin-name}/`

### Step 2: Applicable SA Statutes

- **Research first:** Query Perplexity MCP for SA legislation governing this practice area
- Propose a list of applicable statutes with key sections
- Cross-reference against existing `jurisdictions/za/statutes/` — identify which can be reused (e.g., BCEA, EEA) and which are new
- For each new statute: identify key sections, thresholds, temporal values
- User confirms, corrects, or expands the list
- Adaptive depth: for statutes with annually-changing thresholds (monetary values, Gazette-published rates), drill into current values and source URLs

### Step 3: Skill Divergence Assessment

- For each skill in the plugin: read the SKILL.md frontmatter description and the first ~50 lines (purpose, workflow overview) to understand what the skill does
- **Research first:** Query Perplexity for the SA legal equivalent of what the skill does
- Propose HIGH / MEDIUM / LOW divergence rating with reasoning
- User confirms or overrides per skill
- Output: which skills are in scope for v1 overlays
- Apply the same prioritisation logic as employment-legal: ship the HIGH-divergence skills first, defer MEDIUM for later

### Step 4: Topic Overlay Design

- Group the in-scope skills by legal topic (not one overlay per skill — avoids duplication)
- Propose topic file names and which skills each serves
- Check for overlap with existing topic files across practice areas
- Adaptive depth: for high-divergence skills, drill into what the SA-specific checklist or framework looks like
- **Research first** on domain-specific procedures (e.g., "SA consumer protection complaints process" for commercial-legal)

### Step 5: Practice Profile Template

- Identify which sections of the US CLAUDE.md template need SA replacements
- Propose new SA-specific sections needed (equivalent of "Statutory baseline", "Dispute resolution" etc. from employment-legal)
- Define the work-product header for this practice area (may have practice-specific caveats — e.g., POPIA data processing notices for privacy-legal)
- Define seed documents the cold-start interview should request
- User confirms section-by-section

### Step 6: Cold-Start Interview Questions

- What SA-specific configuration does this practice area need at setup?
- Apply the "thin but high-leverage" principle: anchor the statutory framework, defer detail
- Categorise as must-have vs. nice-to-have at cold-start
- Check whether the cold-start interview already has a ZA fork for this plugin (from a prior expansion) or needs one added
- Adaptive depth: if the practice area has complex regulatory posture (e.g., privacy-legal with POPIA operator/responsible party distinction), drill in

### Step 7: High-Risk Flags and Checklists

- **Research first:** Query Perplexity for common SA legal risks, disputes, and regulatory actions in this practice area
- Propose a domain-specific risk flag table (equivalent of the 11 termination flags)
- Adaptive depth: this is where the deepest practitioner knowledge surfaces — follow up on any flag the user adds or modifies
- Cross-reference with statute sections from Step 2

### Step 8: Validation and Testing

- Default: 3-5 scenario eval cases per in-scope skill
- Propose fact patterns for golden-path cases (covering: straightforward case, edge case, below-threshold/special-category case)
- Any practice-area-specific validation rules (e.g., for privacy-legal: check no GDPR-specific concepts leak into POPIA overlays)
- Confirm the expert review gate applies (SA practitioner reviews content before release)

## Research-First Interview Pattern

At each step where SA legal knowledge is needed, the skill follows:

1. **Query Perplexity MCP** for relevant SA legislation, thresholds, or procedures
2. **Propose an answer** with source cited
3. **Ask the user to confirm, correct, or expand**

This reduces the burden on the user — they confirm and refine rather than dictating from memory.

**Fallback:** If Perplexity MCP is not connected, the skill falls back to model knowledge tagged `[model knowledge — verify]` and asks the user to provide or confirm. The skill does not block on the MCP being unavailable.

**Source attribution:** All research-sourced content in the final spec is tagged:
- `[Perplexity — verify]` — sourced from Perplexity, user should verify against primary source
- `[user confirmed]` — user explicitly confirmed the information
- `[model knowledge — verify]` — from training knowledge, no external verification performed

## Output Artifacts

### Artifact 1: Decision Spec

Saved to: `docs/superpowers/specs/YYYY-MM-DD-za-{plugin-name}-expansion.md`

Contents:
- Decision summary table (step → decision → source)
- Statute inventory (which YAML files to create/reuse, key sections, temporal values)
- Skill divergence matrix (skill name → rating → in scope Y/N)
- Topic overlay map (topic name → skills it serves → key content areas)
- Practice profile template design (sections to replace, sections to add, header formulation)
- Cold-start interview questions (must-have vs. nice-to-have, with question text)
- High-risk flag table (the domain-specific risk indicators)
- Eval case outline (fact patterns per skill, expected flags/statutes, must-not-contain)
- Source provenance log (which decisions came from Perplexity vs. user input)

### Artifact 2: Implementation Plan

The skill invokes `writing-plans` with the spec as input. The plan follows the same task structure as the employment-legal build:

1. Statute YAML files (new + shared references)
2. Topic overlay markdown files
3. Skill router
4. Practice profile template
5. Cold-start interview fork (or extension of existing fork)
6. Validation scripts (extend existing validators for new files)
7. Scenario eval cases
8. Final validation run

The spec is the durable artifact. The plan can be re-generated from the spec if needed.

## State Management and Resume

- If the user pauses, the skill writes a partial spec with `<!-- PAUSED AT: Step N — run /jurisdiction-expansion {plugin} to resume -->` at the top
- Each completed step writes its decisions to the spec immediately
- On re-invocation: detect partial spec, show completed decisions, resume from paused step
- State lives in the spec file itself — no separate state file or memory entries

## Inherited Architecture (Not Re-Decided)

The following decisions from ADR-001 are inherited and not re-asked:

- Additive overlays in `jurisdictions/za/` (not separate plugins)
- Hybrid file format (YAML statutes + markdown overlays)
- Temporal fields (`effective_from`/`effective_until`) on all statute entries
- Router-based skill wiring (zero upstream SKILL.md changes except cold-start)
- Separate ZA practice profile template per practice area
- Shared topic overlays by legal topic, not per skill
- Manual statute updates for v1
- MCP connectors deferred
- Validation: structural (CI) + scenario evals + expert review gate

The skill explains these decisions if the user asks why, citing the ADR.

## Constraints

- **No US legal concepts in ZA files** — enforced by the existing `test-za-overlays.sh` US concept leak check
- **One upstream file modification per plugin** — only the cold-start interview SKILL.md
- **Temporal fields mandatory** — every statute entry must have `effective_from` and `effective_until`
- **Expert review gate** — the skill reminds the user at the end that SA practitioner review is required before release
