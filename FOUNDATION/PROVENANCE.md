# Reproducibility and Provenance / 可复现性与溯源

Current calibration: 2026-09-01

This file defines public source, version, claim-surface, temporal, and correction provenance for the Agent Foundations documentary core.

## Reproducibility target / 可复现目标

A public claim should make it possible to recover:

- stable Claim ID
- canonical source identity
- exact cited source version when material
- date belonging to that version when verified
- strongest source surface actually inspected
- supported proposition and assumptions
- repository mapping/implementation state
- current correction status when historical material was later calibrated

The goal is reconstruction of the claim/evidence chain, not treating document existence as truth.

## Repository helper boundaries / 仓库辅助工具边界

### `FOUNDATION/validate.py`

The validator is a structural/documentary checker.

It checks:

- required verified-core files
- claim-block presence and required labels
- unique Claim IDs
- source-ID contiguity from S01 through the current highest source ID
- canonical source identity presence
- duplicate canonical source identities, with arXiv versions collapsed to the base paper identity
- Claim source references against the canonical registry
- restricted absolute-overclaim phrases
- existing action-reference pin form
- protected-path changes when a comparison base is supplied
- basic `claim.schema.json` properties

It does **not** convert every Markdown Claim into JSON and validate all schema semantics.

It also does not prove theorem correctness, formula accuracy, translation equivalence, exact source-version date, experimental reproduction, or agent behavior.

### `FOUNDATION/arxiv_probe.py`

The arXiv helper supports bibliographic identity/submission-history checks. It can help recover base identifier, cited `vN`, version/date pairing, and title/author identity.

It does not prove theorem semantics or experimental validity.

## Canonical source registry / canonical 来源登记

The current verified-core source registry is:

`S01–S38` in [SOURCES.md](./SOURCES.md).

A registered source is eligible documentary evidence. Registration does not imply local implementation.

### Canonical identity uniqueness

A single external source must not have multiple canonical `Sxx` identities.

For arXiv:

`arXiv:<base-id>` is the canonical paper identity.

Therefore:

- `v1`, `v2`, `v3`, etc. are provenance revisions of the same paper
- a later Daily Research Chunk is a revisit, not a new source identity
- a later citation with expanded author/title metadata is not a new source identity

August reference cases:

- S10 already represents RAFA, `arXiv:2309.17382`
- the 2026-08-27 research task attempted to append the same paper as S36
- current canonical registry retires that duplicate identity; the historical Daily research chunk remains preserved and resolves to S10
- the 2026-08-31 Independent NPG paper has distinct base identity `arXiv:2310.09727` and is therefore registered as S38

## Exact-version workflow / 精确版本流程

For a material arXiv source:

1. normalize the base identifier
2. determine whether that base identifier already has a canonical S ID
3. record the exact cited `vN` when a version is specified
4. inspect primary submission history when the version date matters
5. pair the cited `vN` with its own date only when verified
6. record title/authors when needed to disambiguate identity
7. use the existing S ID for later versions/revisits of the same paper
8. only then use the versioned source in downstream claim interpretation

The first-submission date is not automatically the date of every later version.

Use:

- `VERSION_DATE_PAIR_VERIFIED`
- `VERSION_DATE_NOT_VERIFIED`

### August reference corrections

Retained corrections include:

- S26 `2312.13910v3` → v3 date `2024-07-17`, not v1 date `2023-12-21`
- S28 `2309.14142v3` → v3 date `2025-02-04`, not v1 date `2023-09-25`
- S31 `2310.14685v2` → v2 date `2024-01-14`, not v1 date `2023-10-23`
- S35 `2312.04719v1` → canonical authors `Ayush Rai, Shaoshuai Mou`; earlier generated author attribution is corrected by the 2026-08-27 reconciliation
- attempted S36 → duplicate identity of S10 RAFA; no second canonical source ID retained
- S38 `2310.09727v2` → v2 date `2023-10-27`; official NeurIPS proceedings confirm the NeurIPS 2023 Main Conference Track publication and author list

S33 cites `2312.15847v3`; the August source-identity review rechecked base source identity/authors and keeps the exact v3 date as `VERSION_DATE_NOT_RECERTIFIED_IN_THIS_PASS` rather than guessing from a v1/base date.

## Claim-surface provenance / 声明表面溯源

Source identity verification and claim verification are separate.

Useful source-surface states include:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

A successful fetch, TeX download, parser result, source registration, or author correction does not automatically establish stronger theorem/formula states.

A theorem/bound retains assumptions, comparator, domain, quantifiers, and source version.

For S38, the 2026-09-01 maintenance admission is bounded to independently checked bibliographic/venue/version identity and abstract-level proposition. The exact equations recorded by the historical 08-31 Daily chunk were `NOT_RECERTIFIED_IN_THIS_PASS`.

## Primary-source conflict / 一手来源冲突

When checked primary surfaces disagree:

- record the conflicting surfaces/versions
- use `PRIMARY_SOURCE_CONFLICT`
- do not select a convenient value without stronger evidence
- narrow downstream interpretation to the common supported core

A conflict lowers claim strength; it does not require erasing historical research.

## Temporal provenance / 时间溯源

Keep separate when relevant:

- source publication/version date
- source check time
- historical research logical period
- generation/commit time
- later correction time

A later erratum changes current interpretation without pretending the correction existed at the earlier research time.

## Daily Research Chunk provenance

Generated bilingual Daily Research Chunks are historical evidence inputs, not automatic canonical-source registrations.

Current review may:

- reuse an existing S ID
- register a genuinely new source
- correct authors/version metadata
- narrow a theorem/claim
- map historical wording to current vocabulary
- record `INSUFFICIENT_EVIDENCE`
- record `PRIMARY_SOURCE_CONFLICT`

Daily task completion and canonical verified-core acceptance are separate events.

## Public provenance object / 公开溯源对象

Target public object:

`CLAIM + CANONICAL_SOURCE_ID + SOURCE_VERSION + CHECKED_SURFACE + SCOPE + LIMITATION + CURRENT_STATUS`.

Current August authority: `docs/AUGUST_2026_01_31_EVIDENCE_LEDGER.md` plus targeted errata/reconciliations.
Formal August natural-month status: `CLOSED_WITH_MISSING_DAILY_DATE_RETAINED`.
W36 status: `WEEK_IN_PROGRESS / NO_WEEKLY_CLOSURE`.
