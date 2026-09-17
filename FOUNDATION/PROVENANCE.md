# Reproducibility and Provenance / 可复现性与溯源

Current calibration: 2026-09-17

This file defines public source, version, claim-surface, temporal, correction, producer, and AI-assistance provenance for the Agent Foundations documentary core.

## AI-use and producer disclosure / AI 使用与生产者披露

AI assistance may be used for drafting, translation support, consistency checks, research organization, candidate-source discovery, and repository review. AI output is not automatically evidence and does not become a verified foundation claim by being generated, repeated, or incorporated into prose.

Material conclusions still require the repository's declared claim/evidence chain and, where applicable, independently inspectable repository or public-source evidence. Human maintainer review remains the final merge and governance authority.

Keep producer identity explicit when it matters. A Jules-generated artifact remains a Jules-produced repository artifact; an Independent GPT correction remains a later reviewer/maintenance action; a human merge remains a human-governed delivery decision. Later review does not retroactively change who produced the earlier artifact.

This public disclosure does not require publication or reconstruction of private prompts, Jules repository memory, hidden chain-of-thought/reasoning, credentials, tokens, personal data, or unrelated operator context. Process transparency is bounded to evidence and provenance that can be safely and independently inspected.

The repository currently has no public `AGENTS.md`; do not infer one from private task controls or historical conversation context.

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

The goal is reconstruction of the claim/evidence chain, not treating document existence, generated text, or model agreement as truth.

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

Historical August duplicate/revisit cases remain useful point-in-time examples; current source identity must still be read from the present registry and relevant corrections.

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

A successful fetch, TeX download, parser result, source registration, author correction, validator run, or model summary does not automatically establish stronger theorem/formula states.

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
- historical research logical period;
- generation/producer time;
- commit/merge time;
- later correction time;
- validator/checker execution time and revision;
- current repository presence.

A later erratum changes current interpretation without pretending the correction existed at the earlier research time. A current path does not prove an earlier execution. Later success does not prove or erase an earlier unobserved/failed run.

## Daily Research Chunk provenance

Generated bilingual Daily Research Chunks are historical evidence inputs, not automatic canonical-source registrations.

Current review may reuse an existing source ID, register a genuinely new source, correct authors/version metadata, narrow a theorem/claim, map historical wording to current vocabulary, or record `INSUFFICIENT_EVIDENCE` / `PRIMARY_SOURCE_CONFLICT` under the repository's admission rules.

Daily task completion and canonical verified-core acceptance are separate events.

## Maintenance and Independent GPT provenance

A maintenance run should retain enough public delivery information to recover the exact base `main` revision, changed owning surfaces, aggregate diff boundary, checks actually run, checks not run, overlap state, and Draft-PR head.

`FOUNDATION/REVIEW.md` records review disposition. `FOUNDATION/MAINTENANCE.md` owns maintenance policy. `FOUNDATION/independent-gpt/README.md` owns memoryless recovery/repair/delivery discipline. These roles do not imply that a historical producer consumed later governance text.

## Public provenance object / 公开溯源对象

Target claim object:

`CLAIM + CANONICAL_SOURCE_ID + SOURCE_VERSION + CHECKED_SURFACE + SCOPE + LIMITATION + CURRENT_STATUS`.

Target maintenance object when a repair is delivered:

`BASE_REVISION + OWNING_SURFACE + PRODUCER + EXECUTED_VALIDATION + UNEXECUTED_VALIDATION + AGGREGATE_DIFF + DELIVERY_HEAD`.

Historical August closure and corrections remain point-in-time evidence; current September cadence/maintenance state must be recovered from current repository truth rather than copied from an old cutoff.
