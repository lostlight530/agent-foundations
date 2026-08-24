# Reproducibility and Provenance / 可复现性与溯源

This file defines public source, version, claim-surface, temporal, and correction provenance for the Agent Foundations documentary core.

## Reproducibility target / 可复现目标

A public claim should make it possible to recover:

- stable Claim ID
- registered source identity
- exact cited source version when material
- date belonging to that version
- strongest source surface actually inspected
- supported proposition and assumptions
- repository mapping/implementation state
- current correction status when historical material was later calibrated

The goal is reconstruction of the claim/evidence chain, not treating document existence as truth.

## Repository helper boundaries / 仓库辅助工具边界

### `FOUNDATION/validate.py`

The current validator is a structural/documentary checker.

It checks:

- required verified-core files
- claim-block presence
- required metadata labels
- unique Claim IDs
- registered source references against canonical `S01–S32`
- restricted absolute-overclaim phrases
- full-SHA form of external action references in existing workflow files
- declared protected-path changes when a comparison base is supplied
- basic `claim.schema.json` file properties

It does **not** convert every Markdown Claim into a JSON object and validate all claim fields against the schema enums.

It also does not prove:

- semantic truth
- theorem correctness
- formula transcription accuracy
- translation equivalence
- source-version identity
- experimental reproduction
- external deployment behavior
- autonomous-agent capability

### `FOUNDATION/arxiv_probe.py`

The arXiv helper supports bibliographic identity checks against primary arXiv metadata/submission history.

It can support:

- normalized arXiv identifier
- exact cited `vN`
- version/date pairing
- title/author identity where needed for disambiguation

It does not prove theorem semantics or experimental validity.

## Canonical source registry / canonical 来源登记

The current verified-core source registry is the contiguous range:

`S01–S32` in [SOURCES.md](./SOURCES.md).

A registered source is eligible documentary evidence. Registration does not imply that its mechanism is implemented by this repository.

## Exact-version workflow / 精确版本流程

For a material arXiv source:

1. normalize the base identifier
2. record the exact cited `vN` when a version is specified
3. inspect primary arXiv submission history
4. pair that `vN` with the date belonging to the cited version
5. record title/authors when needed to disambiguate identity
6. only then use that exact-version identity in downstream claim interpretation

The first-submission date is not a substitute for the date of every later version.

Use:

- `VERSION_DATE_PAIR_VERIFIED` when the exact pair is supported
- `VERSION_DATE_NOT_VERIFIED` when it is not

### August reference failures

Current explicit corrections include:

- S26 `2312.13910v3` → v3 date `2024-07-17`, not v1 date `2023-12-21`
- S28 `2309.14142v3` → v3 date `2025-02-04`, not v1 date `2023-09-25`
- S31 `2310.14685v2` → v2 date `2024-01-14`, not v1 date `2023-10-23`

The historical records remain visible; current source identity follows the corrected primary-source record and explicit errata.

## Claim-surface provenance / 声明表面溯源

Source identity verification and claim verification are separate.

Useful source-surface states include:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

A successful fetch, TeX download, parser result, or source registration does not automatically establish one of these stronger states.

A theorem/bound retains its assumptions, comparator, domain, quantifiers, and source version.

A mechanism equation or probability factorization is not a convergence/error bound unless a theorem or derivation supplies that bound.

Long formulas that were not independently checked remain paper-level evidence, for example:

`PAPER_LEVEL_RESULT_SUPPORTED / LONG_FORMULA_NOT_RECERTIFIED`.

## Primary-source conflict / 一手来源冲突

When checked primary surfaces disagree:

- record the conflicting surfaces/versions
- use `PRIMARY_SOURCE_CONFLICT`
- do not select a convenient value without stronger evidence
- narrow downstream interpretation to the common supported core

A primary-source conflict lowers claim strength; it does not require erasing the historical research artifact.

## Temporal provenance / 时间溯源

Research period and evidence time remain part of provenance.

Keep separate when relevant:

- source publication/version date
- source check time
- historical research period
- later correction time

Moving a W33 research chunk into another location does not turn it into July evidence.

A later erratum can change current interpretation without pretending the correction existed at the earlier research time.

## Generated research and current interpretation / 生成研究与当前解释

Generated bilingual research is a historical evidence input, not final authority by itself.

Current verified-core interpretation may:

- retain a claim
- narrow its scope
- downgrade evidence strength
- correct version/date metadata
- record a source-claim mismatch
- preserve a primary-source conflict
- retire an unsupported stronger interpretation

A correction changes current interpretation, not the historical fact that the original artifact existed.

## AI-assisted evidence work / AI 辅助证据工作

AI systems may assist with source discovery, drafting, translation, and consistency checking.

AI output is not evidence by itself.

Material statements remain tied to public source identity, checked source surface, assumptions, scope, implementation state, and limitations.

## Public provenance object / 公开溯源对象

The target public object is:

`CLAIM + SOURCE_IDENTITY + VERSION + CHECKED_SURFACE + SCOPE + LIMITATION + CURRENT_STATUS`.
