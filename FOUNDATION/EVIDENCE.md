# Evidence Contract / 证据契约

Effective: 2026-08-27  
Machine-readable vocabulary: [claim.schema.json](./claim.schema.json)

## Purpose / 目的

This contract defines how Agent Foundations records public claims, evidence strength, mapping, implementation status, validation status, source identity, and limitations.

It is a documentary evidence contract. It is not an agent runtime, evaluator, source-truth oracle, theorem prover, or research-paper execution engine.

## Claim states / 声明状态

- `OBSERVED`
- `SUPPORTED`
- `PROPOSED`
- `HYPOTHESIS`
- `CONTESTED`
- `RETIRED`

`SUPPORTED` means supported only within the cited system, assumptions, data, configuration, metric, and source version.

## Evidence levels / 证据等级

- `E0_REPOSITORY_TEST`
- `E1_PRIMARY_STANDARD`
- `E2_PEER_REVIEWED`
- `E3_REPRODUCIBLE_PREPRINT`
- `E4_PREPRINT`
- `E5_BACKGROUND`
- `E6_UNVERIFIED`

An evidence class describes the evidence object. It does not automatically determine implementation status.

## Mapping states / 映射状态

- `DIRECT_REQUIREMENT`
- `DESIGN_ANALOGY`
- `CANDIDATE_MECHANISM`
- `COUNTEREVIDENCE`
- `OUT_OF_SCOPE`

A mapping is documentary interpretation, not runtime implementation.

Historical generated chunks may contain older labels. Current canonical interpretation must map them onto this vocabulary or explicitly mark them as historical/non-canonical wording.

## Implementation status / 实现状态

- `NOT_IMPLEMENTED`
- `REFERENCE_ONLY`
- `PARTIAL_PROTOTYPE`
- `IMPLEMENTED`

`IMPLEMENTED` requires a concrete repository artifact implementing the claimed behavior. A paper, formula, schema, source registry, or research summary cannot create an implementation by citation.

## Validation status / 验证状态

- `NOT_TESTED`
- `STATIC_CHECKED`
- `EXPERIMENTALLY_TESTED`
- `REPRODUCED`
- `EXTERNALLY_REVIEWED`

`STATIC_CHECKED` on a documentary/reference claim is not a runtime experiment.

## Canonical source identity / canonical 来源身份

The current canonical registry is the contiguous range:

`S01–S35` in [SOURCES.md](./SOURCES.md).

Source IDs are documentary identifiers, not a daily counter.

### Identity rule

One external source identity must have one canonical `Sxx` ID.

For arXiv, canonical identity is the **base arXiv paper identifier**. Therefore:

- a later `vN` is provenance for the same source, not a new source
- a later Daily Research Chunk revisiting the same paper is not a new source
- a changed title rendering or citation style is not a new source

The August 27 RAFA revisit is the reference case: `arXiv:2309.17382` was already S10, so the later attempted S36 registration is retired as a duplicate identity while the historical research chunk remains preserved.

### Version provenance

For explicit arXiv `vN` citations, keep distinct:

- base paper identity
- cited version
- date belonging to that version

Use `VERSION_DATE_PAIR_VERIFIED` only when that exact version/date pair is checked. Otherwise use `VERSION_DATE_NOT_VERIFIED` or a narrower source-identity statement.

## Claim-surface evidence / 声明表面证据

Useful labels include:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

Source reachability or registry presence does not automatically establish theorem/formula-level verification.

A theorem/bound retains its assumptions, comparator, domain, quantifiers, and source version.

## Repository validator boundary / 仓库 validator 边界

`FOUNDATION/validate.py` is a structural/documentary validator.

It currently checks, among other things:

- required verified-core files
- Claim block/metadata presence
- unique Claim IDs
- source IDs form one contiguous range from S01 through the current highest ID
- every source block exposes a canonical Identifier or URL identity
- the same canonical source identity is not registered under multiple S IDs
- domain Claim source references resolve to registered sources
- restricted absolute-overclaim phrases
- existing workflow action references use the repository's full-SHA rule
- protected-path changes when a comparison base is supplied
- basic `claim.schema.json` properties

The validator **does not** require code edits whenever a legitimate new source is appended. It derives the current contiguous range from `SOURCES.md`.

It also does not prove:

- source truth
- theorem meaning
- formula transcription accuracy
- source-version date identity
- translation equivalence
- experimental reproduction
- agent behavior

Therefore:

`STRUCTURAL_VALIDATOR_PRESENT != CLAIM_SEMANTICS_VERIFIED`.

## Daily research → verified core SOP

A Daily Research Chunk is historical research input, not automatic verified-core expansion.

A later canonical review decides separately:

1. whether the external source identity is new or already registered
2. whether bibliographic metadata is correct
3. what source surface was actually inspected
4. what proposition/assumptions are supported
5. which mapping vocabulary applies
6. whether any local implementation exists
7. whether the chunk requires an erratum/reconciliation

A valid Daily research addition can therefore end in any of these states:

- new canonical source registered
- existing canonical source reused
- source metadata corrected
- claim narrowed
- mapping downgraded
- insufficient evidence
- source/claim conflict

Daily generation success is not itself `ACCEPTED_FOR_VERIFIED_CORE`.

## Weekly / monthly synthesis SOP

Weekly/monthly synthesis may aggregate and calibrate research history but must not:

- turn repeated use of one paper into independent corroboration
- turn a paper mechanism into repository implementation
- convert unverified formulas into verified theorems
- silently change historical research dates
- manufacture future-day research

At the 2026-08-27 cutoff the August month is still `OPEN`.

## Historical and temporal interpretation / 历史与时间解释

Historical generated research remains point-in-time evidence. Later reconciliation changes current interpretation without pretending the correction existed at the earlier research time.

Keep separate:

- research logical date
- source publication/version date
- source check time
- later correction time
- canonical source identity
- current verified-core disposition

## Minimum public claim record / 最小公开声明记录

A domain claim retains:

- stable Claim ID
- state
- evidence class
- mapping
- implementation status
- validation status
- canonical source IDs
- supported proposition
- scope/assumptions
- limitations

Structure improves consistency. It does not prove the proposition itself.
