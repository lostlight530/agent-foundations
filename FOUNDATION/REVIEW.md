> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `REVIEW CONTRACT`
> - **Role:** Current public evidence-review vocabulary
> - **Authority:** Current repository-native authority for Review disposition for claims, sources, verified-core admission and historical corrections, distinct from maintenance delivery
> - **Current meaning:** Read every claim through its explicit claim/evidence/mapping/implementation/validation fields and current repository-realization boundary. Historical research and external literature remain evidence inputs rather than automatic capability promotion
> - **Evidence / implementation boundary:** External literature, documentary support, schema/validator presence or a current path never upgrades local implementation or validation state automatically
> - **Cross-document relation:** ARCHITECTURE provides whole-system boundaries; SOURCES/EVIDENCE/PROVENANCE/REVIEW provide identity, semantics and disposition without collapsing into runtime capability
> - **Update trigger:** Update when review states, admission paths or correction/review boundaries materially change
> - **Preservation rule:** Existing claim text, source history and dated examples remain in the same file. This pass clarifies current authority and repairs confirmed drift without rewriting historical evidence

# Public Evidence Review States / 公开证据审核状态

Status: documentary review vocabulary  
Current calibration: 2026-09-17

## Purpose / 目的

This file records public review states for Agent Foundations claims, source identities, verified-core admission, and historical research corrections.

It describes evidence disposition only. It does not execute repository behavior, create implementation capability, authorize a maintenance write, or prove what Jules/private producers consumed.

`FOUNDATION/independent-gpt/README.md` has a different role: it governs memoryless maintenance recovery, concurrency, bounded repair, and Draft-PR delivery. Review state and maintenance action must not be collapsed.

## Recovery prerequisite / 恢复前提

Before assigning a current review state, recover the exact artifact/revision from current merged `main`. When maintenance or delivery state matters, also inspect relevant open pull requests, active maintenance branches, and revision-matched validation evidence.

A stale clone, prior handoff SHA, later path presence, or model recollection cannot establish current or historical execution state by itself.

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

These states are not confidence scores, execution states, or maintenance-delivery states and do not expose private reasoning.

Useful separation:

```text
review state != maintenance action
CALIBRATED != repair delivered
ACCEPTED_FOR_VERIFIED_CORE != merged
STATIC_CHECKED != semantic truth
```

## Source-registration review / 来源登记审核

Before assigning a new `Sxx` ID:

1. normalize the external source identity;
2. check the existing canonical registry;
3. for arXiv, compare the **base paper ID**, not only the cited `vN`;
4. if the source already exists, reuse the existing S ID and record the new version/revisit as provenance;
5. only genuinely new identities receive a new contiguous S ID;
6. verify title/authors/version metadata to the strongest source surface available;
7. keep paper results separate from repository implementation.

A later Daily Research Chunk does not receive a new source ID merely because it is new research activity.

Historical August reference dispositions remain point-in-time examples; they do not define September source counts by themselves.

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

- canonical source identity vs Daily research event;
- base arXiv identity vs explicit `vN`;
- version/date identity vs theorem/formula verification;
- abstract support vs theorem support;
- mechanism equation vs formal error/convergence bound;
- external result vs repository implementation;
- paper assumptions/domain vs generic LLM-agent claims;
- original historical research period vs later correction;
- source registration vs claim support;
- five-axis verified-core admission vs generation success;
- `STATIC_CHECKED` documentary review vs runtime/experimental validation;
- validator definition vs validator execution;
- current path presence vs earlier producer execution.

## History and correction discipline / 历史与纠错纪律

Keep these statements separate:

```text
historical artifact != current state
current path presence != earlier execution
later success != earlier success
correction != history rewrite
unknown != inferred success
```

Historical `docs/**` research and archived audits remain point-in-time evidence. A review finding normally changes current interpretation or the owning current verified-core/maintenance source; it does not silently rewrite historical execution.

When a historical artifact itself is the object under review, retain its producer/time identity and use an explicit erratum/reconciliation/retirement path rather than manufacturing missing evidence.

## Authority map / 权威映射

For verified-core claim interpretation:

- targeted erratum/reconciliation for the affected source/claim;
- `FOUNDATION/SOURCES.md` — canonical source identity;
- `FOUNDATION/EVIDENCE.md` — evidence semantics;
- `FOUNDATION/PROVENANCE.md` — version, producer, temporal, correction, and AI-use provenance;
- this `REVIEW.md` — review disposition vocabulary;
- domain verified-core claim maps;
- historical `docs/**` material as point-in-time context.

For maintenance/control-plane state, current merged `main`, `FOUNDATION/MAINTENANCE.md`, and `FOUNDATION/independent-gpt/README.md` govern recovery/delivery before historical audit records or prior handoffs.

An audit finding may narrow or contest an interpretation. It must not invent implementation, reproduction, theorem support, source agreement, validation execution, or producer intent.

## Relationship to maintenance repair / 与维护修复的关系

Independent review can establish that a maintenance/control-plane defect or calibration need exists. Actual repair follows `FOUNDATION/MAINTENANCE.md` and `FOUNDATION/independent-gpt/README.md`.

- no confirmed maintenance defect → `NO_CHANGE_REQUIRED`;
- safe bounded repair → `REPAIR`;
- overlapping live ownership → `COORDINATE`;
- unrecoverable authority/state or unsafe delivery → `BLOCKED`.

Review completion alone is not a reason to create an edit or PR.

## Minimal public review record / 最小公开审核记录

A durable public review record may include:

- Claim ID or historical artifact;
- exact repository revision when material;
- review state;
- canonical source ID;
- public source identity/version;
- strongest checked source surface;
- supported proposition and assumptions;
- mapping status;
- implementation/validation status;
- missing or conflicting evidence;
- erratum/reconciliation pointer;
- validation actually executed and results;
- validation not executed;
- final bounded disposition.

No private prompt, repository memory, hidden reasoning, credential, or unrelated operator context is required in this public record.

## Period-status boundary / 周期状态边界

Formal August natural-month closure remains the historical `CLOSED_WITH_MISSING_DAILY_DATE_RETAINED` result recorded after the 2026-09-01 reconciliation. That historical closure does not define the current September week/month state; current cadence state must be recovered from current repository evidence.

Final doctrine and merge authority remains with the maintainer.
