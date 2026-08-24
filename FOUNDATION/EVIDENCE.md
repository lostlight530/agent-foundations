# Evidence Contract / 证据契约

Effective: 2026-08-24  
Machine-readable vocabulary: [claim.schema.json](./claim.schema.json)

## Purpose / 目的

This contract defines how Agent Foundations records public claims, evidence strength, mapping, implementation status, validation status, source identity, and limitations.

It is a documentary evidence contract. It is not an agent runtime, evaluator, source-truth oracle, or theorem prover.

## Claim states / 声明状态

Current schema vocabulary:

- `OBSERVED`
- `SUPPORTED`
- `PROPOSED`
- `HYPOTHESIS`
- `CONTESTED`
- `RETIRED`

`SUPPORTED` means supported only within the cited system, assumptions, data, configuration, metric, and source version.

## Evidence levels / 证据等级

Current schema vocabulary:

- `E0_REPOSITORY_TEST`
- `E1_PRIMARY_STANDARD`
- `E2_PEER_REVIEWED`
- `E3_REPRODUCIBLE_PREPRINT`
- `E4_PREPRINT`
- `E5_BACKGROUND`
- `E6_UNVERIFIED`

An evidence class describes the evidence object. It does not automatically determine implementation status.

A repository capability claim needs direct local implementation evidence; an external paper, standard, SDK, or system card cannot create a local capability by citation.

## Mapping states / 映射状态

Current schema vocabulary:

- `DIRECT_REQUIREMENT`
- `DESIGN_ANALOGY`
- `CANDIDATE_MECHANISM`
- `COUNTEREVIDENCE`
- `OUT_OF_SCOPE`

A mapping describes how external evidence is interpreted locally. It is not an implementation state.

## Implementation status / 实现状态

Current schema vocabulary:

- `NOT_IMPLEMENTED`
- `REFERENCE_ONLY`
- `PARTIAL_PROTOTYPE`
- `IMPLEMENTED`

`IMPLEMENTED` requires a concrete repository artifact implementing the claimed behavior.

A documentary schema, validator, source registry, or research summary cannot by itself upgrade an agent-runtime concept to `IMPLEMENTED`.

## Validation status / 验证状态

Current schema vocabulary:

- `NOT_TESTED`
- `STATIC_CHECKED`
- `EXPERIMENTALLY_TESTED`
- `REPRODUCED`
- `EXTERNALLY_REVIEWED`

Validation status is separate from claim state and implementation status.

For this repository, `STATIC_CHECKED` on a documentary/reference claim must not be read as a runtime experiment.

`EXPERIMENTALLY_TESTED` requires retained evidence for the actual tested artifact/configuration/result.

## Source identity / 来源身份

The canonical source registry is:

`S01–S32` in [SOURCES.md](./SOURCES.md).

A material source record should preserve:

- stable identifier/canonical URL
- exact version/revision when material
- date belonging to that version
- title/authors or issuer when identity is ambiguous
- source/check provenance sufficient to distinguish later correction from original research history

For explicit arXiv `vN` citations:

- `VERSION_DATE_PAIR_VERIFIED` means the exact version/date pair was checked against primary submission history
- `VERSION_DATE_NOT_VERIFIED` means it was not

A v1 date must not be silently reused for a later cited version.

## Claim-surface evidence / 声明表面证据

Useful source-surface labels include:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

A reachable source, downloaded TeX archive, parser output, or summary does not automatically establish theorem/formula-level verification.

A theorem/bound retains its assumptions, comparator, domain, quantifiers, and version.

A mechanism equation or factorization is not a formal error/convergence bound unless a theorem/derivation actually supplies that bound.

## Primary-source conflict / 一手来源冲突

When checked primary surfaces disagree:

- retain the disagreement
- use `PRIMARY_SOURCE_CONFLICT`
- narrow downstream interpretation to what the checked surfaces jointly support
- do not silently choose the convenient value

## Repository validator boundary / 仓库 validator 边界

`FOUNDATION/validate.py` currently checks structural/documentary properties including:

- required core files
- Claim block/metadata presence
- unique Claim IDs
- registered references against canonical `S01–S32`
- restricted absolute-overclaim phrases
- external action-reference pin form in existing workflow files
- protected-path changes when an explicit comparison base is supplied
- basic properties of `claim.schema.json`

It does **not** serialize every Markdown Claim into a JSON object and enforce every schema enum/semantic relationship.

It also does not verify source-version identity, theorem meaning, formula accuracy, translation equivalence, experimental reproduction, or agent behavior.

Therefore:

`STRUCTURAL_VALIDATOR_PRESENT != CLAIM_SEMANTICS_VERIFIED`.

## Historical and temporal interpretation / 历史与时间解释

Historical generated research remains point-in-time evidence.

Keep separate:

- historical research period
- source publication/version date
- source check time
- later correction date

A later erratum can supersede current interpretation without pretending the corrected fact was present in the original generated chunk.

## Minimum public claim record / 最小公开声明记录

A domain claim should retain:

- stable Claim ID
- state
- evidence class
- mapping
- implementation status
- validation status
- registered source IDs
- supported proposition
- scope/assumptions
- limitations

Schema/document structure improves consistency. It does not prove the proposition itself.
