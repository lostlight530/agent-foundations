# Monthly Strategic Blueprints

This directory contains time-bounded monthly strategic synthesis for Agent Foundations.

Monthly blueprints summarize the repository's **current supported architecture/evidence position** for a declared window. They are not runtime specifications and they do not upgrade external references into implemented capability.

## Record classes

### Time-bounded monthly blueprint

A dated file such as [`2026-08-through-23-strategic-blueprint.md`](./2026-08-through-23-strategic-blueprint.md) records the strongest supportable synthesis for its explicit evidence window.

Its claims must remain compatible with the verified core:

- `FOUNDATION/EVIDENCE.md`
- `FOUNDATION/ARCHITECTURE.md`
- `FOUNDATION/MEMORY.md`
- `FOUNDATION/TOOLS.md`
- `FOUNDATION/COLLABORATION.md`
- `FOUNDATION/SOURCES.md` and dated source supplements
- `FOUNDATION/PROVENANCE.md`
- `FOUNDATION/REVIEW.md`

### `Monthly_Blueprint_Current.md`

`docs/en/Monthly_Blueprint_Current.md` and `docs/zh/Monthly_Blueprint_Current.md` are **current-view aliases**, not timeless theory documents.

They should:

- state their evidence cutoff/window
- identify whether they are provisional or final
- summarize only claims compatible with the current verified core
- link or name the authoritative time-bounded blueprint
- preserve `REFERENCE_ONLY`, `DESIGN_CANDIDATE`, `NOT_IMPLEMENTED`, and validation states
- be refreshed when the current-view synthesis materially changes

They must not silently retain obsolete absolute claims merely because an older monthly narrative used them.

## Provisional versus final

A partial natural-month blueprint must be clearly labeled `PROVISIONAL` or equivalent.

Before the month closes, it must not claim to be the final monthly seal. A final month-end synthesis should be created only from the actual completed evidence window and should preserve unresolved evidence rather than forcing closure.

## Claim-state discipline

Monthly prose does not override verified-core evidence states.

Keep these distinctions explicit:

- external primary source != repository implementation
- protocol/SDK reference != runtime dependency
- architecture analogy != executable feature
- design candidate != accepted implementation
- document review != runtime validation
- trajectory/trace evidence != outcome evidence
- session/task/context/memory/external state != one undifferentiated state scope
- mathematical mechanism != universal guarantee

Avoid unconditional language such as `fully immune`, `always converges`, `mathematically guarantees`, or `entirely deprecated` unless a scoped authoritative result actually establishes that exact claim.

## Source and temporal provenance

A monthly blueprint should identify material source/version changes that affect interpretation. When a current official protocol or SDK version differs from a historical research chunk, preserve the old chunk as history and correct the current blueprint/verified-core interpretation rather than pretending the historical text was never generated.

## Reading precedence

When a monthly blueprint conflicts with a stronger repository authority, use:

1. explicit erratum affecting the claim
2. verified-core source/provenance/evidence record
3. verified-core architecture/domain map
4. dated monthly blueprint
5. generated historical research chunk for context

A monthly blueprint is synthesis, not evidence-source identity by itself.

## Repository boundary

These files do not authorize:

- Jules prompt/memory/cadence changes
- GPT/cloud control changes
- runtime dependencies or executable agent features
- frontend changes
- `.github/**`, Actions, or CI changes
- new merge/production gates

Documentation and architecture status must remain honest about what is implemented, referenced, designed, and unverified.