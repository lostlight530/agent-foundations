> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Role:** Current provenance and reproducibility contract for sources, versions, claim surfaces, corrections, producers, software publication, and AI assistance
> - **Authority:** Current provenance authority for reconstructing documentary claim/evidence chains
> - **Current meaning:** Keep external scientific source identity, repository DOI, Git revision, producer identity, and revision-matched validation as separate objects
> - **Evidence / implementation boundary:** A DOI, path, generated artifact, validator definition, or later correction does not prove historical execution, source truth, experimental reproduction, or exact archive-to-Git equivalence
> - **Cross-document relation:** SOURCES supplies canonical identities; EVIDENCE supplies semantics; REVIEW supplies disposition; current Git main supplies repository-state truth
> - **Preservation rule:** The existing subject text remains the owning repository document. This pass clarifies current interpretation and corrects only confirmed current-authority drift; historical examples and dated evidence retain their original time boundary.

# Reproducibility and Provenance / 可复现性与溯源

Current calibration: 2026-09-17

This file defines public source, version, claim-surface, temporal, correction, producer, software-publication, and AI-assistance provenance for the Agent Foundations documentary core.

## AI-use and producer disclosure / AI 使用与生产者披露

AI assistance may be used for drafting, translation support, consistency checks, research organization, candidate-source discovery, and repository review. AI output is not automatically evidence and does not become a verified foundation claim by being generated, repeated, or incorporated into prose.

Material conclusions still require the repository's declared claim/evidence chain and, where applicable, independently inspectable repository or public-source evidence. Human maintainer review remains the final merge and governance authority.

Keep producer identity explicit when it matters. A generated artifact remains attached to its original producer; a later correction is a later review/maintenance action; a human merge is a human-governed delivery decision. Later review does not retroactively change who produced the earlier artifact.

This public disclosure does not require publication or reconstruction of private prompts, repository memory, hidden chain-of-thought/reasoning, credentials, tokens, personal data, or unrelated operator context. Process transparency is bounded to evidence and provenance that can be safely and independently inspected.

## Reproducibility target / 可复现目标

A public claim should make it possible to recover:

- stable Claim ID;
- canonical source identity;
- exact cited source version when material;
- date belonging to that version when verified;
- strongest source surface actually inspected;
- supported proposition and assumptions;
- repository mapping/implementation state;
- validation surface and exact command/result when validation is claimed;
- producer/revision identity when material;
- current correction status when historical material was later calibrated.

The goal is reconstruction of the claim/evidence chain, not treating document existence, generated text, model agreement, a DOI, or repository popularity as truth.

## Repository publication provenance / 仓库出版溯源

Agent Foundations has a public software publication at DOI `10.5281/zenodo.22791169`, with publication date 2026-09-16.

This establishes an externally addressable archived publication identity for the repository. It does **not** establish:

- that the DOI is an `Sxx` scientific source for an `AF-*` claim;
- that every claim in the archived object is scientifically supported;
- that a validator/test was executed for the archived object;
- that an external experiment was reproduced;
- that the archive is byte-identical or semantically equivalent to every later `main` revision;
- an exact archive-to-Git-SHA mapping unless that mapping is explicitly retained and independently inspectable.

Keep three identities separate:

```text
external scientific source identity (`Sxx`)
!= repository software-publication identity (DOI)
!= exact executable/document revision identity (Git SHA)
```

`CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` are the public repository-publication metadata surfaces. `SOURCES.md` remains the canonical external evidence-source registry.

## Repository helper boundaries / 仓库辅助工具边界

### `FOUNDATION/validate.py`

The validator is a structural/documentary checker.

It checks declared repository surfaces including required verified-core files, claim-block metadata, unique Claim IDs, canonical source registration/duplication rules, source references, restricted overclaim phrases, pinned action-reference form, protected-path changes when a comparison base is supplied, and basic `claim.schema.json` properties.

It does **not** convert every Markdown Claim into JSON and validate all schema semantics. It also does not prove theorem correctness, formula accuracy, translation equivalence, exact source-version date, experimental reproduction, semantic truth, or agent behavior.

A validator definition in the repository is not an executed validator result. Record the exact revision, command, environment, exit status, and relevant output when claiming validation. If it was not run, use `NOT_EXECUTED`.

### `FOUNDATION/arxiv_probe.py`

The arXiv helper supports bibliographic identity/submission-history checks. It can help recover base identifier, cited `vN`, version/date pairing, and title/author identity.

It does not prove theorem semantics or experimental validity. A successful fetch or parse does not independently verify a downstream claim.

## Canonical source registry / canonical 来源登记

The canonical source registry is `FOUNDATION/SOURCES.md`. The exact current contiguous range must be recovered from current `main`; do not freeze a historical upper bound from an earlier audit into a current maintenance conclusion.

A registered source is eligible documentary evidence. Registration does not imply local implementation.

### Canonical identity uniqueness

A single external source must not have multiple canonical `Sxx` identities.

For arXiv, `arXiv:<base-id>` is the canonical paper identity. Therefore `v1`, `v2`, `v3`, and later revisits are provenance revisions of the same paper, not new source identities by themselves.

Historical duplicate/revisit cases remain useful point-in-time examples; current source identity must still be read from the present registry and relevant corrections.

## Exact-version workflow / 精确版本流程

For a material arXiv source:

1. normalize the base identifier;
2. determine whether that base identifier already has a canonical S ID;
3. record the exact cited `vN` when a version is specified;
4. inspect primary submission history when the version date matters;
5. pair the cited `vN` with its own date only when verified;
6. record title/authors when needed to disambiguate identity;
7. use the existing S ID for later versions/revisits of the same paper;
8. only then use the versioned source in downstream claim interpretation.

The first-submission date is not automatically the date of every later version.

Use `VERSION_DATE_PAIR_VERIFIED` or `VERSION_DATE_NOT_VERIFIED` as appropriate. Historical corrections remain historical evidence and are not silently rewritten into earlier records.

## Claim-surface provenance / 声明表面溯源

Source identity verification and claim verification are separate.

Useful source-surface states include:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

A successful fetch, TeX download, parser result, source registration, author correction, validator run, model summary, or repository publication does not automatically establish stronger theorem/formula states.

A theorem or bound retains assumptions, comparator, domain, quantifiers, and source version.

## Primary-source conflict / 一手来源冲突

When checked primary surfaces disagree:

- record the conflicting surfaces/versions;
- use `PRIMARY_SOURCE_CONFLICT`;
- do not select a convenient value without stronger evidence;
- narrow downstream interpretation to the common supported core.

A conflict lowers claim strength; it does not require erasing historical research.

## Temporal and execution provenance / 时间与执行溯源

Keep separate when relevant:

- source publication/version date;
- source check time;
- repository software-publication date;
- historical research logical period;
- generation/producer time;
- Git revision time;
- commit/merge time;
- later correction time;
- validator/checker execution time and revision;
- current repository presence.

A later erratum changes current interpretation without pretending the correction existed at the earlier research time. A current path does not prove an earlier execution. Later success does not prove or erase an earlier unobserved/failed run. A DOI publication date does not substitute for the exact revision and environment of a validation run.

## Generated research provenance

Generated bilingual research chunks are historical evidence inputs, not automatic canonical-source registrations.

Current review may reuse an existing source ID, register a genuinely new source, correct authors/version metadata, narrow a theorem/claim, map historical wording to current vocabulary, or record `INSUFFICIENT_EVIDENCE` / `PRIMARY_SOURCE_CONFLICT` under the repository's admission rules.

Task completion and canonical verified-core acceptance are separate events.

## Maintenance provenance

A maintenance run should retain enough public delivery information to recover the exact base `main` revision, changed owning surfaces, aggregate diff boundary, checks actually run, checks not run, overlap state, and delivery head when those facts are material.

`FOUNDATION/REVIEW.md` records review disposition. `FOUNDATION/MAINTENANCE.md` owns maintenance policy. The memoryless recovery guide owns its declared recovery/delivery discipline. These roles do not imply that a historical producer consumed later governance text.

## Public provenance objects / 公开溯源对象

Target claim object:

`CLAIM + CANONICAL_SOURCE_ID + SOURCE_VERSION + CHECKED_SURFACE + SCOPE + LIMITATION + CURRENT_STATUS`.

Target repository-publication object:

`DOI + PUBLICATION_DATE + ARCHIVED_OBJECT + EXPLICIT_REVISION_MAPPING_WHEN_AVAILABLE`.

Target revision-matched validation object:

`GIT_REVISION + ENVIRONMENT + COMMAND + INPUT/FIXTURE + RESULT + UNTESTED_BOUNDARY`.

These objects are intentionally distinct and must not inherit authority from one another.
