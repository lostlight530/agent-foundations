# Public Evidence Review States / 公开证据审核状态

Status: documentary review vocabulary  
Current calibration: 2026-09-01

## Purpose / 目的

This file records public review states for Agent Foundations claims, source identities, and historical research corrections.

It describes evidence disposition only. It does not execute repository behavior or create implementation capability.

## Review states / 审核状态

1. `REVIEW_PENDING`
2. `SOURCE_IDENTITY_VERIFIED`
3. `CLAIM_SURFACE_VERIFIED`
4. `PRIMARY_SOURCE_CONFLICT`
5. `INSUFFICIENT_EVIDENCE`
6. `MAPPING_SCOPED`
7. `IMPLEMENTATION_SEPARATED`
8. `CALIBRATION_REQUIRED`
9. `CALIBRATED`
10. `ACCEPTED_FOR_VERIFIED_CORE`

These states are not confidence scores and do not expose private reasoning.

## Source-registration review / 来源登记审核

Before assigning a new `Sxx` ID:

1. normalize the external source identity
2. check the existing canonical registry
3. for arXiv, compare the **base paper ID**, not only the cited `vN`
4. if the source already exists, reuse the existing S ID and record the new version/revisit as provenance
5. only genuinely new identities receive a new contiguous S ID
6. verify title/authors/version metadata to the strongest source surface available
7. keep paper results separate from repository implementation

A later Daily Research Chunk does not receive a new source ID merely because it is new research activity.

Reference dispositions:

- S33: retained as new canonical source
- S34: retained as new canonical source
- S35: retained, with author metadata corrected
- attempted S36 on 08-27: not retained; duplicate of existing S10 RAFA
- S36 on 08-28: retained as the distinct memory-regret source
- 08-29 revisit: resolves to S25
- S37 on 08-30: retained as distinct joint-Lyapunov source
- S38 on 08-31: retained as distinct Independent NPG source after source/venue/version reconciliation

## Supported review paths / 支持的审核路径

Straightforward claim:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → CLAIM_SURFACE_VERIFIED → MAPPING_SCOPED → IMPLEMENTATION_SEPARATED → ACCEPTED_FOR_VERIFIED_CORE`.

Historical correction:

`CALIBRATION_REQUIRED → CALIBRATED`.

Primary-source disagreement:

`PRIMARY_SOURCE_CONFLICT`.

Evidence-limited claim:

`INSUFFICIENT_EVIDENCE`.

A repeated/revisited source can stop at:

`SOURCE_IDENTITY_VERIFIED → EXISTING_CANONICAL_SOURCE_REUSED`.

`EXISTING_CANONICAL_SOURCE_REUSED` is a documentary disposition phrase, not a new schema enum.

## Review checks / 审核检查

When material, preserve these distinctions:

- canonical source identity vs Daily research event
- base arXiv identity vs explicit `vN`
- version/date identity vs theorem/formula verification
- abstract support vs theorem support
- mechanism equation vs formal error/convergence bound
- external result vs repository implementation
- paper assumptions/domain vs generic LLM-agent claims
- original historical research period vs later correction
- source registration vs claim support
- `STATIC_CHECKED` documentary review vs runtime/experimental validation

## Authority map / 权威映射

- `FOUNDATION/EVIDENCE.md` — evidence and source-identity semantics
- `FOUNDATION/SOURCES.md` — canonical `S01–S38` source identities
- `FOUNDATION/PROVENANCE.md` — exact-version, duplicate-identity, and temporal provenance
- domain claim maps — bounded architecture/memory/tool/collaboration claims
- explicit August errata/reconciliations — current corrections
- `docs/AUGUST_2026_01_31_EVIDENCE_LEDGER.md` — final natural-month documentary ledger
- original bilingual research — historical context

An audit finding may narrow or contest an interpretation. It must not invent implementation, reproduction, theorem support, source agreement, or test success.

## Minimal public review record / 最小公开审核记录

A durable public review record may include:

- Claim ID or historical artifact
- review state
- canonical source ID
- public source identity/version
- strongest checked source surface
- supported proposition and assumptions
- mapping status
- implementation/validation status
- missing or conflicting evidence
- erratum/reconciliation pointer
- final bounded disposition

Formal August natural-month closure is `CLOSED_WITH_MISSING_DAILY_DATE_RETAINED` after the 2026-09-01 reconciliation. W36 remains `WEEK_IN_PROGRESS / NO_WEEKLY_CLOSURE`.
