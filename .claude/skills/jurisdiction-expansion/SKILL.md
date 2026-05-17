---
name: jurisdiction-expansion
description: >
  Guide adaptation of a claude-for-legal plugin for South African law.
  Runs a structured, research-assisted interview to capture statute
  inventories, skill divergence assessments, topic overlay designs,
  practice profile templates, cold-start questions, and high-risk flags.
  Produces a decision spec and invokes writing-plans for implementation.
  Use when the user says "expand to [plugin]", "adapt [plugin] for SA",
  "add a new practice area", or "jurisdiction expansion".
argument-hint: "[plugin-name, e.g. commercial-legal]"
---

# /jurisdiction-expansion

Adapt a claude-for-legal plugin for South African law through a structured interview.

## Before you begin

1. Read `jurisdictions/za/ARCHITECTURE.md` — this is the operating manual. It defines the directory layout, file schemas, wiring mechanism, and the step-by-step process for adding a practice area. Follow it.
2. Read `project/decisions/001-sa-overlay-architecture.md` — this is the rationale. If the user asks "why do we do it this way?", cite this document.
3. List the contents of `jurisdictions/za/statutes/` — know which statutes already exist and can be shared across practice areas.
4. Check for prior partial work: does `jurisdictions/za/{plugin-name}/` already exist? If it has a partial spec (with `<!-- PAUSED AT: -->` marker), offer to resume.

## Architecture — inherited, not re-decided

These decisions are settled (ADR-001). Do not re-ask them. If the user asks why, cite the ADR.

- Additive overlays in `jurisdictions/za/` (not separate plugins, not in-place rewrites)
- Hybrid file format: YAML for statutes/thresholds, markdown for workflow overlays
- Temporal fields (`effective_from`/`effective_until`) on every statute entry
- Router-based skill wiring: zero upstream SKILL.md changes except cold-start interview
- Separate ZA practice profile template per practice area
- Shared topic overlays organized by legal topic, not per skill
- Manual statute updates for v1; automated monitoring is phase 2
- MCP connectors deferred; requirements documented
- Validation: structural (CI) + scenario evals + expert review gate

## Research-first interview pattern

At every step where SA legal knowledge is needed, follow this pattern:

1. **Research first.** Query Perplexity MCP (`mcp__perplexity__*` or equivalent search tool) for the relevant SA legislation, thresholds, or procedures. If Perplexity is not connected, use model knowledge.
2. **Propose an answer** with the source cited.
3. **Ask the user to confirm, correct, or expand.**

The user confirms and refines — they should not have to dictate statutes from memory.

**Source tags for the spec:**
- `[Perplexity — verify]` — sourced from Perplexity search
- `[user confirmed]` — user explicitly confirmed
- `[model knowledge — verify]` — from training knowledge, unverified

## Interview pacing

- **One question at a time.** Never ask more than 2-3 answerable prompts per turn.
- **Adaptive depth.** Each step has a fixed opening question. Go deeper based on the user's answers — the most valuable insights come from follow-up questions.
- **Pause and resume.** If the user says "pause", "stop", or "let me come back to this", write the partial spec immediately (see State Management below) and close with: "Progress saved. Run `/jurisdiction-expansion {plugin}` to resume from Step N."

## The interview

### Opening

Determine the target plugin. If the user passed an argument (e.g., `/jurisdiction-expansion commercial-legal`), use it. Otherwise ask:

> Which plugin are you adapting for South African law? The available first-party plugins are:
>
> commercial-legal, privacy-legal, product-legal, corporate-legal, employment-legal, regulatory-legal, ai-governance-legal, litigation-legal, ip-legal, law-student, legal-clinic, legal-builder-hub
>
> (employment-legal is already adapted — pick another.)

Once you have the target:

1. Read `{plugin}/.claude-plugin/plugin.json` for the plugin name, description, and version
2. List all skills in `{plugin}/skills/` — you will assess each for SA divergence
3. Read `{plugin}/CLAUDE.md` (the practice profile template) — you will design the ZA variant
4. Check if `jurisdictions/za/{plugin}/` already exists

Tell the user: "I'll walk you through 8 steps to design the SA overlay for **{plugin}**. I'll research SA law at each step and propose answers — you confirm or correct. This produces a decision spec and an implementation plan."

---

### Step 1: Target plugin confirmation

- Show the plugin's description from `plugin.json`
- List the skill count: "{plugin} has N skills. I'll assess each for SA divergence in Step 3."
- Confirm scope: "We're adapting {plugin} for South African law. The overlay will add SA-specific statute data, topic overlays, a practice profile template, and cold-start interview questions — without modifying the existing skills (except the cold-start interview). Correct?"
- Check for partial prior work in `jurisdictions/za/{plugin}/`

**Write to spec after this step:** Plugin name, description, skill count.

---

### Step 2: Applicable SA statutes

**Research first.** Query Perplexity: "South African statutes governing {practice area description from plugin.json}"

Then:

1. Propose a list of applicable SA statutes with:
   - Full Act name and number
   - Key sections relevant to this practice area
   - Whether the statute already exists in `jurisdictions/za/statutes/` (check the directory)
2. For each NEW statute (not already in `jurisdictions/za/statutes/`):
   - Identify key sections that need entries (thresholds, timelines, definitions)
   - Flag any annually-changing values (monetary thresholds, Gazette-published rates)
   - Propose a `source_url`
3. For EXISTING statutes: note which sections are already covered and whether new sections need to be added
4. Ask the user to confirm, correct, or add statutes

**Adaptive depth:** For statutes with Gazette-published thresholds, research current values and effective dates.

**Write to spec after this step:** Statute inventory table (statute name → new/existing → key sections → temporal values).

---

### Step 3: Skill divergence assessment

For each skill in the plugin:

1. Read the SKILL.md frontmatter description and first ~50 lines
2. **Research first.** Query Perplexity: "South African law equivalent of {what the skill does}" — e.g., for a `dpa-review` skill in privacy-legal: "South African POPIA equivalent of GDPR DPA review"
3. Assess divergence:
   - **HIGH** — US defaults produce wrong legal guidance for SA. Needs overlay.
   - **MEDIUM** — Process is portable but legal framing differs. May need overlay.
   - **LOW** — Jurisdiction-neutral infrastructure. No overlay needed.
4. Present a table: skill name | description (1 line) | divergence | reasoning
5. Ask the user to confirm or override ratings

Then: "Which skills are in scope for v1? My recommendation: all HIGH-divergence skills, plus any MEDIUM skills you consider critical."

**Write to spec after this step:** Skill divergence matrix with in-scope Y/N column.

---

### Step 4: Topic overlay design

Using only the in-scope skills from Step 3:

1. Group skills by legal topic — one overlay file per topic, not per skill
2. Propose topic file names and which skills each topic serves
3. Check for overlap with existing topic files in other practice areas (e.g., `jurisdictions/za/employment-legal/topics/` might have overlapping content)
4. **Research first** on domain-specific procedures for each topic: query Perplexity for SA-specific frameworks
5. For each topic, outline the key content areas (statutory framework, procedural checklists, flag tables)
6. Present the topic map and ask the user to confirm

**Adaptive depth:** For HIGH-divergence topics, drill into what the SA-specific checklist or framework looks like — this is where the substantive legal content gets shaped.

**Write to spec after this step:** Topic overlay map (topic name → skills served → key content areas).

---

### Step 5: Practice profile template

1. Read the plugin's US CLAUDE.md template (`{plugin}/CLAUDE.md`)
2. Identify sections that are US-specific and need SA replacements
3. Propose SA-specific sections to add (equivalent of employment-legal's "Statutory baseline", "Employment equity and BEE", "Dispute resolution", "Leave and conditions")
4. Design the work-product header for this practice area:
   - Does it need practice-specific privilege caveats beyond the standard SA privilege caveat?
   - Example: privacy-legal might need a POPIA-specific data processing notice
5. Propose seed documents the cold-start interview should request
6. Walk through section-by-section with the user

**Write to spec after this step:** Section replacement table, new sections list, header formulation, seed document list.

---

### Step 6: Cold-start interview questions

1. What SA-specific configuration does this practice area need at setup?
2. Apply the "thin but high-leverage" principle: capture enough to anchor the statutory framework without asking for details that can be inferred later from documents
3. Categorise each question as must-have or nice-to-have
4. Check whether the plugin's cold-start interview SKILL.md already has a ZA fork:
   - If yes (from a prior expansion): note what's there and what needs to be added
   - If no: the implementation will add one, following the same pattern as employment-legal (fork after Part 0)
5. Present the question list and ask the user to confirm

**Adaptive depth:** For practice areas with complex regulatory posture, drill into what the key configuration dimensions are.

**Write to spec after this step:** Cold-start questions (must-have vs. nice-to-have) with question text.

---

### Step 7: High-risk flags and checklists

**Research first.** Query Perplexity: "common South African {practice area} legal risks disputes regulatory actions penalties"

1. Propose a domain-specific risk flag table (equivalent of the 11 termination flags in employment-legal's `dismissal.md`)
2. Each flag should have: flag name, why it's high-risk, what to check
3. Cross-reference flags with statute sections from Step 2
4. Ask the user to confirm, add, remove, or refine flags

**Adaptive depth:** This is where the deepest practitioner knowledge surfaces. Follow up on any flag the user adds or modifies — ask why it's important and what the check should look for.

**Write to spec after this step:** High-risk flag table.

---

### Step 8: Validation and testing

1. Default: 3-5 scenario eval cases per in-scope skill
2. Propose fact patterns for golden-path cases covering:
   - Straightforward case (the "happy path" that should work cleanly)
   - Edge case (borderline scenario, threshold boundary)
   - Special category (below-threshold employee, specific sector, protected group)
3. For each case: describe the input scenario, expected flags, expected statutes, and US concepts that must NOT appear
4. Any practice-area-specific validation rules? (e.g., for privacy-legal: check no GDPR-specific concepts like "data controller" leak in — POPIA uses "responsible party")
5. Confirm the expert review gate: "Before release, an SA practitioner should review the overlay content. This is a process gate, not an automated test."

**Write to spec after this step:** Eval case outlines.

---

## After the interview: write the spec

When all 8 steps are complete:

1. **Summarise decisions** in a table:

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | {plugin} — {N} skills, {M} in scope | user confirmed |
| 2 | Statutes | {list} | Perplexity + user confirmed |
| ... | ... | ... | ... |

2. **Ask for final confirmation:** "Here's the complete decision map for {plugin}. Any decisions you want to revisit before I write the spec?"

3. **Write the spec** to `docs/superpowers/specs/YYYY-MM-DD-za-{plugin}-expansion.md` with all sections from the interview:
   - Decision summary table
   - Statute inventory
   - Skill divergence matrix
   - Topic overlay map
   - Practice profile template design
   - Cold-start interview questions
   - High-risk flag table
   - Eval case outline
   - Source provenance log

4. **Commit** the spec

5. **Invoke `writing-plans`** to produce the implementation plan from the spec. The plan follows the same task structure as the employment-legal build:
   1. Statute YAML files (new + extend existing)
   2. Topic overlay markdown files
   3. Skill router
   4. Practice profile template
   5. Cold-start interview fork
   6. Validation scripts (extend existing validators)
   7. Scenario eval cases
   8. Final validation run

## State management — pause and resume

If the user pauses mid-interview:

1. Write all completed steps to `docs/superpowers/specs/YYYY-MM-DD-za-{plugin}-expansion.md` immediately
2. Add `<!-- PAUSED AT: Step {N} — run /jurisdiction-expansion {plugin} to resume -->` at the top
3. Close with: "Progress saved to `docs/superpowers/specs/{filename}`. Run `/jurisdiction-expansion {plugin}` to resume from Step {N}."

On re-invocation:

1. Check `docs/superpowers/specs/` for a file matching `*-za-{plugin}-expansion.md` with a `PAUSED AT` marker
2. If found: read it, show a summary of completed steps, ask "Resume from Step {N}, or start over?"
3. If resuming: load the completed decisions as context and continue from the paused step

## Reference: employment-legal as the worked example

When the user asks "what did this look like for employment-legal?", point them to:
- `project/decisions/001-sa-overlay-architecture.md` — the 13 architecture decisions
- `project/prd-sa-employment-overlay.md` — the full PRD with 26 user stories
- `jurisdictions/za/ARCHITECTURE.md` — the operating manual
- `jurisdictions/za/employment-legal/` — the actual implementation (statute files, topic overlays, router, practice profile template)

Employment-legal is the reference implementation. This skill produces the same artifacts for new practice areas.
