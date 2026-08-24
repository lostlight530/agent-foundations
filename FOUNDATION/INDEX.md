# Agent Foundations — Verified Core / 可验证核心

Status: repository evidence and architecture core

## Purpose / 目的

`FOUNDATION/**` is the compact documentary architecture, evidence, source, and provenance core of Agent Foundations.

It is not an autonomous-agent runtime.

External equations, papers, protocol mappings, pseudocode, and architecture analogies remain external/reference claims unless a concrete repository artifact implements the behavior.

## Repository realization map / 仓库真实结构映射

### 1. Domain claim maps / 领域声明

- [ARCHITECTURE.md](./ARCHITECTURE.md) — architecture/evaluation boundaries
- [MEMORY.md](./MEMORY.md) — memory research and lifecycle claims
- [TOOLS.md](./TOOLS.md) — tool/control/observability claims
- [COLLABORATION.md](./COLLABORATION.md) — multi-agent coordination claims

These files use stable IDs:

- `AF-ARCH-*`
- `AF-MEM-*`
- `AF-TOOL-*`
- `AF-COLLAB-*`

Each claim separately declares state, evidence class, mapping, implementation status, validation status, sources, and scope/limits.

### 2. Canonical source registry / 来源登记

[SOURCES.md](./SOURCES.md) is the canonical source registry currently recognized by the repository validator.

Current contract:

`S01–S32`.

The registry includes corrected exact-version dates for affected August sources. Source registration does not mean the sourced mechanism is implemented locally.

### 3. Claim vocabulary / 声明词汇

`claim.schema.json` defines the machine-readable vocabulary for:

- claim ID
- claim state
- evidence class
- mapping type
- implementation state
- validation state
- sources
- scope
- limitations

The schema and the Markdown domain files are related documentary surfaces. Schema validity does not prove claim semantics.

### 4. Repository validator / 仓库验证器

`validate.py` currently checks:

- required verified-core files
- claim headings and required metadata labels
- unique Claim IDs
- source references against the canonical S01–S32 registry
- the contiguous S01–S32 source range
- restricted absolute-overclaim phrases
- action references where the repository workflow directory is present
- protected-path changes when a base ref is supplied

Its scope is structural/documentary.

It does **not** verify:

- source-version identity
- theorem correctness
- equation transcription
- translation equivalence
- external experiment reproduction
- runtime agent capability

### 5. arXiv provenance helper / arXiv 溯源辅助

[arxiv_probe.py](./arxiv_probe.py) verifies arXiv identity and submission-history version/date pairs.

It supports bibliographic provenance only. It does not certify theorem content or architecture mappings.

### 6. Evidence, provenance, and review semantics / 证据、溯源与审核语义

- [EVIDENCE.md](./EVIDENCE.md) — claim/evidence/source/implementation semantics
- [PROVENANCE.md](./PROVENANCE.md) — exact-version and temporal provenance
- [REVIEW.md](./REVIEW.md) — public review-state vocabulary

These files can narrow current interpretation but do not execute agent behavior.

### 7. Historical research and correction / 历史研究与纠正

`docs/en/**` and `docs/zh/**` preserve the bilingual research stream.

Explicit August corrections include:

- [`../docs/AUGUST_2026_W33_ERRATA.md`](../docs/AUGUST_2026_W33_ERRATA.md)
- [`../docs/AUGUST_2026_W34_ERRATA.md`](../docs/AUGUST_2026_W34_ERRATA.md)
- [`../docs/monthly/2026-08-through-23-strategic-blueprint.md`](../docs/monthly/2026-08-through-23-strategic-blueprint.md)

A correction supersedes the conflicting current interpretation without pretending the original generated text was originally correct.

### 8. Presentation surface / 展示层

`index.html` is a presentation surface. It does not determine verified-core implementation state or evidence strength.

## Interpretation precedence / 解释优先级

For an affected historical claim:

1. explicit erratum for that claim/source metadata
2. current canonical source identity in `SOURCES.md`
3. `EVIDENCE.md`, `PROVENANCE.md`, and `REVIEW.md`
4. bounded domain claim map
5. original generated research for historical context

This is interpretation precedence, not runtime execution precedence.

## Core invariants / 核心不变量

- external research never automatically becomes repository implementation
- mathematical results retain their assumptions/domain
- source identity and claim support are separate
- source identity and theorem/formula verification are separate
- explicit arXiv versions use the date belonging to the cited version
- mechanism equations are not promoted into formal bounds without the supplying theorem
- unresolved primary-source conflicts remain conflicts
- historical period/provenance is not rewritten by later weaving
- implementation state and evidence state remain distinct
- the validator's structural checks are not semantic truth checks

## Repository status / 仓库状态

The strongest current implementation description is:

`DOCUMENTARY_AGENT_FOUNDATION_WITH_STRUCTURED_EVIDENCE_AND_PROVENANCE_SUPPORT`.

The domain documents contain many `REFERENCE_ONLY`, `NOT_IMPLEMENTED`, and `PROPOSED` concepts by design.

Formal August month closure remains open until the natural month closes.

Current stage synthesis:

[`../docs/monthly/2026-08-through-23-strategic-blueprint.md`](../docs/monthly/2026-08-through-23-strategic-blueprint.md)