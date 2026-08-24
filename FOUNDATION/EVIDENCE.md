# Evidence Contract / 证据契约

Effective: 2026-08-24  
Machine-readable vocabulary: [claim.schema.json](./claim.schema.json)

## Purpose / 目的

This contract defines how Agent Foundations records public claims, evidence strength, mapping, implementation status, validation status, source identity, and limitations.

It is a documentary evidence contract. It is not an agent runtime, evaluator, source-truth oracle, or theorem prover.

## Claim states / 声明状态

Current `claim.schema.json` vocabulary:

- `OBSERVED` — directly observed in a named repository artifact/result
- `SUPPORTED` — supported within named evidence and assumptions
- `PROPOSED` — proposed repository/research direction, not established implementation
- `HYPOTHESIS` — falsifiable research proposition
- `CONTESTED` — credible evidence supports competing conclusions
- `RETIRED` — preserved as a superseded position

`SUPPORTED` is always bounded by the cited system, data, assumptions, metric, version, and evidence surface.

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

External evidence can support or bound a proposition without creating a local implementation.

## Mapping vocabulary / 映射词汇

Current schema vocabulary:

- `DIRECT_REQUIREMENT`
- `DESIGN_ANALOGY`
- `CANDIDATE_MECHANISM`
- `COUNTEREVIDENCE`
- `OUT_OF_SCOPE`

A mapping records how an external result is used in this documentary foundation. It does not execute the mapped mechanism.

## Implementation states / 实现状态

Current schema vocabulary:

- `NOT_IMPLEMENTED`
- `REFERENCE_ONLY`
- `PARTIAL_PROTOTYPE`
- `IMPLEMENTED`

`IMPLEMENTED` requires an identifiable repository artifact that actually performs the claimed behavior.

A paper, equation, protocol description, or architecture analogy is not implementation evidence.

## Validation states / 验证状态

Current schema vocabulary:

- `NOT_TESTED`
- `STATIC_CHECKED`
- `EXPERIMENTALLY_TESTED`
- `REPRODUCED`
- `EXTERNALLY_REVIEWED`

These labels describe the strongest recorded validation state for the claim; they do not erase the claim's scope or limitations.

## Source registry / 来源登记

The canonical registry recognized by the current repository validator is [SOURCES.md](./SOURCES.md), containing `S01–S32`.

For a material source preserve, where applicable:

- stable identifier or canonical URL
- exact cited version/revision
- date belonging to that version/revision
- title/authors or issuer when identity could be ambiguous
- retrieval/check context

For explicit arXiv `vN` citations, the version-specific date comes from primary submission history rather than automatically reusing the v1 date.

## Source identity != claim support / 来源身份不等于声明支持

Keep separate:

1. source identity
2. exact source version
3. strongest source surface actually inspected
4. proposition supported by that surface
5. local architecture mapping
6. local implementation state

A successful fetch or correct citation does not prove the theorem interpretation or every downstream architecture claim.

Recommended claim-surface labels include:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

A long formula that was not independently checked remains bounded paper-level evidence.

## Mathematical discipline / 数学纪律

A theorem or formal bound retains its original:

- assumptions
- quantified domain
- comparator/objective
- model class
- version

A mechanism equation or probability factorization is not itself a convergence/error bound unless a theorem or derivation supplies that bound.

An external mathematical result does not become an Agent Foundations runtime guarantee.

## Primary-source conflict / 一手来源冲突

When primary surfaces disagree, preserve the disagreement as `PRIMARY_SOURCE_CONFLICT` or `CONTESTED` rather than selecting a convenient value.

A stronger claim returns only after stronger evidence resolves the conflict.

## Temporal provenance / 时间溯源

Research period and source version are part of provenance.

- moving/weaving a research chunk does not change when the underlying observation occurred
- a later erratum can correct current interpretation without pretending the corrected metadata existed in the original generated artifact
- exact-version corrections remain explicit historical corrections

## Actual validator boundary / 当前 validator 边界

`FOUNDATION/validate.py` currently checks documentary structure including:

- required verified-core files
- claim headings and required metadata labels
- unique Claim IDs
- source references against S01–S32
- contiguous S01–S32 source registry
- restricted absolute-overclaim phrases
- selected repository path/reference rules

Important limitation:

`validate.py` does **not** parse each Markdown claim into `claim.schema.json` and does not automatically validate every enum value or semantic proposition against that JSON Schema.

`test_contract.py` checks selected parser/schema/protected-path/README invariants, but the existence of that file is not evidence that any command ran for a documentation change.

Therefore:

`STRUCTURAL_VALIDATOR_PRESENT != CLAIM_SEMANTICS_VERIFIED`.

## Minimum public claim record / 最小公开声明记录

A domain claim should retain:

- Claim ID
- state
- evidence class
- mapping
- implementation state
- validation state
- registered source IDs
- supported proposition
- scope/limitations

These fields keep theory, evidence, implementation, and validation from collapsing into one status.