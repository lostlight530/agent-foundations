# August 2026 W34 Source / Provenance Errata

Status: `POST_HOC_ERRATA`

Audit date: 2026-08-24

Affected evidence window: 2026-08-17 through 2026-08-23

Authority: independent reviewer / verified-core maintenance outside the Jules Daily/Weekly SOP stream

## Purpose

This erratum records source-identity defects found in the W34 Jules-generated Daily research chunks and the 2026-08-23 Weekly cascade. It preserves the historical generated documents while correcting the current evidence interpretation.

It does **not** rewrite the original Jules run, alter Jules prompts or memory, or claim that Jules consumed this correction during generation.

## Ownership boundary

The affected research chunks and Weekly cascade are Jules-native SOP artifacts. Their commits include `google-labs-jules[bot]` as co-author.

This erratum is a separate post-hoc reviewer artifact. The two control planes must not be collapsed.

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

The paper-level mechanism/claim must remain scoped to the cited version and its assumptions. A wrong version date does not by itself falsify the paper result, but it breaks exact-version provenance until corrected.

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
- Repeated by the 2026-08-23 Weekly cascade

Primary arXiv submission history shows:

- v1: 2023-10-23
- v2: **2024-01-14**

Correct current identity:

- `arXiv:2310.14685v2`
- Version date: **2024-01-14**
- v1 date: 2023-10-23

Status: `VERSION_DATE_INVALID_IN_DAILY_AND_WEEKLY_WEAVE`

The Weekly conflict audit did not independently validate exact version/date identity. `VERIFIED_FROM_LATEX_SOURCE` in the generated document therefore cannot be interpreted as proof that the exact `v2` provenance pair was verified.

## W34 controls that did not prevent recurrence

W33 had already established that:

- an exact arXiv `vN` is not verified merely because the base identifier resolves
- v1 date cannot be reused as a later-version date
- formula/theorem verification and source-version verification are separate

A reviewer-side `arxiv_probe.py` and explicit source-identity policy existed by this period, but the W34 Jules Daily/Weekly SOP did not automatically consume that reviewer-side gate.

Therefore W34 recurrence is evidence of **control-plane separation**, not evidence that the reviewer policy failed inside Jules. The correct status is:

`PROVENANCE_PROCESS_GAP_PERSISTED_IN_JULES_STREAM`

not `JULES_COMPLIED_WITH_VERIFIED_CORE`.

## Validator / CI boundary

Several Daily commits update `FOUNDATION/validate.py` source-range bounds. That is a repository-structure change and historical verification surface; it is not evidence that a current CI verification matrix existed or executed.

The repository's dedicated `verify-foundation.yml` workflow had already been removed on 2026-08-07. This erratum does not recreate it and does not add any CI or merge gate.

## Sources checked without the same version/date defect

The version/date dimension was independently rechecked for:

- S27 `arXiv:2312.09674v1` — 2023-12-15
- S29 `arXiv:2608.10529v1` — 2026-08-11
- S30 `arXiv:2312.16609v1` — 2023-12-27
- S32 `arXiv:2403.15636v1` — 2024-03-22

`NO_SAME_VERSION_DATE_DEFECT_FOUND` means only that this specific identity field matched primary submission history. It does not certify every formula, theorem transcription, analogy, architecture mapping, or implementation claim in the generated chunks.

## Precedence

For S26, S28, and S31:

1. this erratum controls the August W34 correction record
2. corrected `FOUNDATION/SOURCES.md` controls current source identity
3. `FOUNDATION/PROVENANCE.md` controls source/version verification semantics
4. original bilingual Daily/Weekly chunks remain historical execution artifacts

Do not silently edit the historical generated chunks solely to make them appear originally correct.

## Carry-forward

Future independent review should:

- verify exact `vN` + version date before promoting source identity
- keep formula/theorem verification separate from metadata identity
- keep Weekly weaving from strengthening an unresolved Daily provenance state
- preserve explicit errata when later evidence supersedes historical generated wording

These are reviewer-side rules unless the Jules task surface separately adopts them.

## Maintenance boundary

Documentation and evidence only.

No runtime, dependency, frontend, Jules prompt/memory/cadence, GPT/cloud task control, GitHub Action, CI, merge gate, or deployment change is authorized.

Tests not run — documentation/evidence only.
