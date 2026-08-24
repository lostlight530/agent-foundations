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

The current validator checks structural/documentary properties including:

- required core files
- required metadata labels in domain claim blocks
- unique Claim IDs
- source references against the canonical S01–S32 registry
- contiguous S01–S32 source headings
- basic `claim.schema.json` file properties such as declared Draft 2020-12 and closed top-level properties
- restricted absolute-overclaim phrases
- selected repository reference/path rules

Important limitation:

`validate.py` does **not** transform Markdown claim blocks into JSON and validate each block against every `claim.schema.json` enum/property rule.

It also does not establish source-version correctness, theorem semantics, formula accuracy, translation equivalence, or agent behavior.

### `FOUNDATION/test_contract.py`

This file contains selected parser/schema/protected-path/README contract tests for the validator helpers.

Its presence describes repository test coverage design. It is not evidence that those tests were executed for a particular documentation revision.

### `FOUNDATION/arxiv_probe.py`

The arXiv helper supports bibliographic identity and submission-history checks, including exact version/date pairing.

It does not verify theorem meaning, equation transcription, experimental validity, or local implementation.

## Canonical source registry / 规范来源登记

The current verified-core registry recognized by `validate.py` is:

`S01–S32` in [SOURCES.md](./SOURCES.md).

A registered source is eligible documentary evidence. Registration does not imply that its mechanism is implemented by this repository.

## Exact-version workflow / 精确版本流程

For a material arXiv source:

1. normalize the base identifier
2. record explicit `vN` when cited
3. inspect primary arXiv metadata/submission history
4. pair that version with the date belonging to it
5. preserve title/authors where needed for identity
6. only then use that exact version identity in a stronger downstream claim

The first-submission date is not automatically the date of a later version.

### August corrected examples

- S26 `2312.13910v3` → v3 date `2024-07-17`
- S28 `2309.14142v3` → v3 date `2025-02-04`
- S31 `2310.14685v2` → v2 date `2024-01-14`

The original generated research remains historical evidence; current source identity follows the corrected record.

## Source identity and claim verification / 来源身份与声明核验

Identity verification and proposition verification are separate.

Useful public claim-surface states include:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

A source file, TeX archive, or page being reachable does not establish theorem/formula-level verification.

A mechanism equation is not a formal convergence/error bound unless the relevant theorem/derivation supplies such a bound.

Long formulas not independently checked remain bounded paper-level evidence.

## Primary-source disagreement / 一手来源冲突

When checked primary surfaces disagree:

- record the conflicting surfaces/versions
- use `PRIMARY_SOURCE_CONFLICT`
- do not select a convenient value without stronger evidence
- narrow downstream interpretation to the common supported core

A conflict is a provenance state, not a reason to erase the historical research record.

## Temporal provenance / 时间溯源

Research period, source version/date, and later correction time remain distinct.

- later weaving does not backdate a research observation
- moving text does not change its originating period
- an erratum changes current interpretation, not the original historical timestamp
- if persisted observation time precedes the material source event/version time, record a temporal conflict until stronger history resolves it

## Historical generated research / 历史生成研究

Generated bilingual research is a historical evidence input, not final authority by itself.

Current verified-core interpretation may:

- retain a claim
- narrow its scope
- downgrade evidence/source strength
- correct version/date identity
- mark a source-claim mismatch
- preserve a source conflict
- retire a claim from current authority

These corrections preserve the original artifact as historical provenance.

## AI-use boundary / AI 使用边界

AI-assisted drafting, translation, discovery, or consistency checking does not count as evidence by itself.

Material claims remain tied to public source identity, checked surface, assumptions, implementation state, and limitations.

The public provenance object is therefore:

`CLAIM + SOURCE_IDENTITY + VERSION + CHECKED_SURFACE + SCOPE + LIMITATION + CURRENT_STATUS`.