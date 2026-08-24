# Reproducibility and AI Use / 可复现性与 AI 使用

This provenance policy applies to the public `FOUNDATION/**` evidence core and committed research records.

It documents source identity, exact-version provenance, claim verification, temporal provenance, and public AI-use boundaries. It does not publish private prompts, hidden reasoning, private memory, confidential context, or unpublished future control strategy.

## Reproducibility target / 可复现目标

A reviewer should be able to:

- locate each structured Claim ID
- recover its registered primary source
- identify the exact cited source version when a version matters
- distinguish external findings from repository implementation
- identify what proposition/theorem/formula was actually checked
- inspect the deterministic repository helper that supports a structural/provenance statement where such a helper exists

本目录属于文档型基础体系。可复现的目标是恢复“声明—来源—版本—证据状态—实现状态”链条，而不是把文档存在本身当成真实性证明。

Python compatibility is revision-specific. A Python version becomes a verified environment only when relevant executable behavior was actually run under that version and the result was retained for the reviewed revision.

## Repository helpers / 仓库辅助工具

### `FOUNDATION/validate.py`

The validator checks documentary/core properties including:

- required core files
- claim metadata
- unique Claim IDs
- registered source references
- claim-schema structure
- restricted absolute-overclaim phrases
- declared protected-path comparison when a base reference is explicitly supplied

It is a structural repository validator.

It does **not** prove:

- semantic truth
- theorem correctness
- formula transcription accuracy
- translation equivalence
- source-version identity
- experimental reproduction
- external deployment behavior
- autonomous-agent capability

### `FOUNDATION/arxiv_probe.py`

The arXiv probe supports bibliographic identity checks against primary arXiv metadata/submission history.

It can support:

- normalized arXiv identifier
- exact cited `vN`
- version/date pairing
- title/author identity where needed for disambiguation

It does not prove theorem semantics or experimental validity.

## Source identity workflow / 来源身份流程

For every material arXiv source entering the verified core:

1. normalize the base identifier
2. record the exact cited `vN` when a version is specified
3. inspect primary arXiv metadata/submission history
4. pair `vN` with the date belonging to that version
5. record title/authors when needed to disambiguate identity
6. only then use that source identity for downstream claim verification

An explicit `vN` citation should not be treated as exact-version verified without either:

- `VERSION_DATE_PAIR_VERIFIED`
- or an explicit `VERSION_DATE_NOT_VERIFIED` limitation

The base page's first-submission date is not a substitute for the date of a later cited version.

### August reference failures

The W33/W34 audit found exact-version provenance errors in historical generated research where later-version identifiers were paired with corresponding v1 dates.

Current corrected examples include:

- S26 `2312.13910v3` → v3 date `2024-07-17`, not v1 date `2023-12-21`
- S28 `2309.14142v3` → v3 date `2025-02-04`, not v1 date `2023-09-25`
- S31 `2310.14685v2` → v2 date `2024-01-14`, not v1 date `2023-10-23`

Historical research remains visible, while current exact-version identity follows the corrected primary-source record.

## Claim verification workflow / 声明核验流程

Identity verification and claim verification are separate steps.

For each material proposition, record the strongest surface actually checked:

- abstract only → `ABSTRACT_SUPPORTED`
- primary full text → `FULL_TEXT_SUPPORTED`
- exact theorem/lemma → `THEOREM_TEXT_VERIFIED`
- exact equation/notation → `FORMULA_TRANSCRIPTION_VERIFIED`
- assumptions/conditions → `ASSUMPTIONS_VERIFIED`

Do not use a strong verification label merely because a source file or TeX archive was reachable.

The relevant theorem/formula and its assumptions must actually be inspected for theorem/formula-level status.

When a long equation is copied, verify the parts that materially determine its meaning, including indices, powers, parentheses, summation ranges, variable definitions, and relevant conditions.

If this was not done, keep a narrower status such as:

`PAPER_LEVEL_RESULT_SUPPORTED / LONG_FORMULA_NOT_RECERTIFIED`.

## Handling primary-source disagreement / 处理一手来源冲突

If primary surfaces disagree — for example abstract versus theorem text, different versions, or rendered text versus TeX — preserve the conflict.

Required interpretation:

- record the conflicting surfaces and versions
- mark `PRIMARY_SOURCE_CONFLICT`
- do not guess which value/wording is authoritative
- narrow downstream claims to what all checked surfaces support
- restore the stronger claim only after stronger version-specific evidence resolves the conflict

A primary-source conflict is not a reason to delete the historical research record. It is a reason to lower claim strength and improve provenance.

## Temporal provenance / 时间溯源

Research period is part of provenance.

- a W33 research chunk remains a W33 observation after later weaving or relocation
- moving text into an older section does not make it evidence from that older period
- a July section must not silently absorb August findings as if they existed in July
- errata/reconciliation may supersede current interpretation without erasing the original historical artifact
- source check time, source publication/version time, research logical period, and later correction time remain separate fields when they differ

If an observation timestamp precedes the material source event/version date recorded for that same claim, use a temporal conflict state until stronger history resolves it.

## Generated research and verified core / 生成研究与可验证核心

Generated bilingual research is historical input to the repository knowledge base, not authority by itself.

The verified core may:

- retain a generated claim as supported
- narrow its scope
- downgrade its source/evidence class
- correct version/date metadata
- mark a source-claim mismatch
- preserve a primary-source conflict
- retire a claim from current interpretation

A correction changes current interpretation, not the historical fact that the original artifact existed.

## AI use / AI 使用

AI systems may assist with source discovery, drafting, translation, consistency checks, and repository helper development.

AI output is never evidence by itself.

Material statements retain source-specific:

- assumptions
- evaluated systems
- configurations
- metrics
- exact version identity where material
- limitations

AI-assisted review must not:

- infer a later-version date from v1
- upgrade an abstract claim into a theorem
- upgrade a mechanism equation into a convergence/error bound without the theorem
- convert empirical results into mathematical guarantees
- convert external guarantees into repository guarantees
- hide unresolved source conflicts by selecting the most convenient value

## Correction model / 修正模型

For the verified core and historical research:

- generated documents are evidence inputs, not authority
- unsupported claims are removed from current verified-core authority or explicitly downgraded
- historical artifacts remain visible when useful as provenance/execution history
- material historical errors are corrected with explicit errata/reconciliation and precedence
- newer/stronger primary-source evidence supersedes conflicting secondary summaries for current interpretation
- credentials, private prompts, private memory, hidden reasoning traces, confidential context, and unpublished future strategy are not committed as provenance records

## Public evidence boundary / 公开证据边界

A public provenance record should expose enough information to reconstruct and critique a claim without exposing private reasoning process.

The desired public object is:

`CLAIM + SOURCE_IDENTITY + VERSION + CHECKED_SURFACE + SCOPE + LIMITATION + CURRENT_STATUS`

not private chain-of-thought or internal control strategy.
