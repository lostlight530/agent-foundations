# August 2026 W34 Source / Provenance Errata

Status: `POST_HOC_ERRATA`

Audit date: 2026-08-24

Affected evidence window: 2026-08-17 through 2026-08-23

Authority: current verified-core source/provenance interpretation

## Purpose

This erratum records exact-version source-identity defects found in historical W34 Daily research and the 2026-08-23 Weekly synthesis.

It preserves the historical generated documents while correcting the current evidence interpretation.

The correction is intentionally limited to public source/provenance facts. It does not encode private prompts, hidden reasoning, future control strategy, or unpublished automation rules.

## Finding 1 — S26 exact-version date mismatch

Historical source identity:

- Identifier: `arXiv:2312.13910v3`
- Persisted version date: `2023-12-21`
- Affected Daily date: 2026-08-17

Primary arXiv submission history shows:

- v1: 2023-12-21
- v3: **2024-07-17**

Correct current identity:

- `arXiv:2312.13910v3`
- Version date: **2024-07-17**

Status: `VERSION_DATE_INVALID_IN_GENERATED_CHUNK`

The paper-level mechanism/claim remains scoped to the cited version and its assumptions. A wrong version date does not by itself falsify the paper result, but it breaks exact-version provenance until corrected.

## Finding 2 — S28 exact-version date mismatch

Historical source identity:

- Identifier: `arXiv:2309.14142v3`
- Persisted version date: `2023-09-25`
- Affected Daily date: 2026-08-19

Primary arXiv submission history shows:

- v1: 2023-09-25
- v3: **2025-02-04**

Correct current identity:

- `arXiv:2309.14142v3`
- Version date: **2025-02-04**

Status: `VERSION_DATE_INVALID_IN_GENERATED_CHUNK`

## Finding 3 — S31 exact-version date mismatch and Weekly recurrence

Historical source identity:

- Identifier: `arXiv:2310.14685v2`
- Persisted version date: `2023-10-23`
- Affected Daily date: 2026-08-22
- Repeated by the 2026-08-23 Weekly synthesis

Primary arXiv submission history shows:

- v1: 2023-10-23
- v2: **2024-01-14**

Correct current identity:

- `arXiv:2310.14685v2`
- Version date: **2024-01-14**
- v1 date: 2023-10-23

Status: `VERSION_DATE_INVALID_IN_DAILY_AND_WEEKLY_WEAVE`

The Weekly synthesis did not contain independent evidence that the exact version/date pair had been checked. A strong source-verification label in the historical text therefore cannot be interpreted as proof of exact `v2` provenance identity.

## Recurrence interpretation

The same defect class had already been identified earlier in August:

- an exact arXiv `vN` is not verified merely because the base identifier resolves
- a v1 date cannot be reused as the date of a later cited version
- source-version verification and theorem/formula verification are separate evidence steps

The W34 recurrence shows that the historical generated research stream still contained a version/date provenance gap at that point in time.

Current status:

`PROVENANCE_PROCESS_GAP_RECURRED_IN_HISTORICAL_RESEARCH`.

This is a statement about committed evidence history, not about hidden producer behavior.

## Sources checked without the same version/date defect

The exact version/date dimension was independently rechecked for:

- S27 `arXiv:2312.09674v1` — 2023-12-15
- S29 `arXiv:2608.10529v1` — 2026-08-11
- S30 `arXiv:2312.16609v1` — 2023-12-27
- S32 `arXiv:2403.15636v1` — 2024-03-22

`NO_SAME_VERSION_DATE_DEFECT_FOUND` means only that this specific identity field matched primary submission history.

It does not certify every formula, theorem transcription, analogy, architecture mapping, experimental result, or implementation claim in the historical chunks.

## Precedence

For S26, S28, and S31:

1. this erratum controls the W34 correction record
2. corrected `FOUNDATION/SOURCES.md` controls current source identity
3. `FOUNDATION/PROVENANCE.md` controls source/version verification semantics
4. original bilingual Daily/Weekly chunks remain historical artifacts

Do not silently edit the historical generated chunks solely to make them appear originally correct.

## Current provenance rule

For current verified-core interpretation:

- exact `vN` and its version date are one identity pair
- formula/theorem verification remains separate from metadata identity
- a Weekly restatement cannot strengthen unresolved Daily provenance without new evidence
- explicit errata preserve the distinction between historical text and corrected current interpretation

## Maintenance boundary

Documentation and source/provenance evidence only.

No runtime, dependency, frontend, deployment state, or artifact-production configuration is changed by this erratum.
