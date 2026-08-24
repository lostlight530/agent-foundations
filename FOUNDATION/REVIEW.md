# Public Evidence Review States / 公开证据审核状态

Status: documentary review vocabulary

## Purpose / 目的

This file records public review states for Agent Foundations claims and historical research corrections.

It describes evidence disposition only. It does not execute repository behavior or create implementation capability.

## Review states / 审核状态

1. `REVIEW_PENDING`
   - material is awaiting evidence review
2. `SOURCE_IDENTITY_VERIFIED`
   - material source identity and exact cited version are verified where material
3. `CLAIM_SURFACE_VERIFIED`
   - the strongest inspected source surface is identified and bounded
4. `PRIMARY_SOURCE_CONFLICT`
   - checked primary surfaces disagree
5. `INSUFFICIENT_EVIDENCE`
   - available evidence cannot support the requested claim strength
6. `MAPPING_SCOPED`
   - external evidence is classified as requirement, analogy, candidate mechanism, counterevidence, or out of scope
7. `IMPLEMENTATION_SEPARATED`
   - external evidence and repository implementation status are explicitly separated
8. `CALIBRATION_REQUIRED`
   - historical material remains useful but requires explicit correction or narrowing
9. `CALIBRATED`
   - an explicit erratum/reconciliation records the corrected current interpretation
10. `ACCEPTED_FOR_VERIFIED_CORE`
   - the bounded proposition fits the current documentary evidence contract

These states describe the public evidence record. They are not confidence scores and do not expose private reasoning.

## Supported review paths / 支持的审核路径

A straightforward supported claim can move through:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → CLAIM_SURFACE_VERIFIED → MAPPING_SCOPED → IMPLEMENTATION_SEPARATED → ACCEPTED_FOR_VERIFIED_CORE`.

A historical correction may use:

`CALIBRATION_REQUIRED → CALIBRATED`.

A primary-source disagreement can stop at:

`PRIMARY_SOURCE_CONFLICT`.

An evidence-limited claim can stop at:

`INSUFFICIENT_EVIDENCE`.

No state transition makes an external result an implementation unless a concrete repository artifact independently establishes implementation.

## Review checks / 审核检查

When material, review checks should preserve these distinctions:

- exact arXiv `vN` identity vs base arXiv identity
- version/date identity vs theorem/formula verification
- abstract support vs theorem support
- mechanism equation vs formal error/convergence bound
- external result vs repository implementation
- paper assumptions/domain vs generic LLM-agent claims
- original historical research period vs later document placement
- source registration vs claim support
- `STATIC_CHECKED` documentary review vs runtime/experimental validation

## Authority map / 权威映射

- `FOUNDATION/EVIDENCE.md` — claim/evidence/implementation semantics
- `FOUNDATION/SOURCES.md` — canonical `S01–S32` source identities
- `FOUNDATION/PROVENANCE.md` — exact-version and temporal provenance
- domain claim maps — bounded architecture/memory/tool/collaboration claims
- explicit August errata — current correction records for affected historical research
- original bilingual research — historical context

An audit finding may narrow or contest an interpretation. It must not invent implementation, reproduction, theorem support, source agreement, or test success.

## Minimal public review record / 最小公开审核记录

A durable public review record may include:

- Claim ID or artifact
- review state
- public source identity/version
- strongest checked source surface
- supported proposition and assumptions
- mapping status
- implementation/validation status
- missing or conflicting evidence
- erratum pointer when applicable
- final bounded disposition

The review record should contain only information necessary to understand and audit the public evidence decision.
