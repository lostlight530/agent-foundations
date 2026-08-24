# Agent Foundations — Verified Core / 可验证核心

Status: repository documentary/evidence core

## Purpose / 目的

`FOUNDATION/**` is the compact evidence and architecture core of Agent Foundations.

The repository is primarily a theory, evidence, and documentary architecture base. It is **not** an implemented autonomous-agent runtime.

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

[SOURCES.md](./SOURCES.md) is the canonical source registry and currently contains the contiguous range `S01–S32`.

A source being registered does not establish theorem correctness, formula accuracy, experimental reproduction, or repository implementation.

### 3. Claim vocabulary / Claim 词汇契约

[claim.schema.json](./claim.schema.json) defines the machine-readable claim vocabulary:

- Claim ID pattern
- state
- evidence class
- mapping type
- implementation status
- validation status
- source IDs
- scope
- limitations

The schema and the Markdown domain files are related documentary surfaces. Schema validity does not prove claim semantics.

### 4. Repository validator / 仓库验证器

`validate.py` currently checks:

- required verified-core files
- claim-block presence
- stable and unique Claim IDs
- required metadata labels
- references against canonical `S01–S32`
- a restricted list of absolute-overclaim phrases
- external action references for full-SHA form in existing workflow files
- protected-path changes when an explicit comparison base is supplied
- basic properties of `claim.schema.json` itself

Important boundary:

`validate.py` does **not** parse every Markdown claim into a JSON object and enforce every `claim.schema.json` enum or semantic relationship.

It also does not verify theorem meaning, formula transcription, source-version identity, translation equivalence, experimental reproduction, or agent behavior.

Therefore:

`STRUCTURAL_VALIDATOR_PRESENT != CLAIM_SEMANTICS_VERIFIED`.

### 5. arXiv provenance helper / arXiv 溯源辅助

[arxiv_probe.py](./arxiv_probe.py) supports arXiv identity and submission-history version/date checks.

It supports bibliographic provenance only. It does not certify theorem content, formulas, experimental validity, or architecture mappings.

### 6. Evidence, provenance, and review semantics / 证据、溯源与审核语义

- [EVIDENCE.md](./EVIDENCE.md) — claim/evidence/source/implementation semantics
- [PROVENANCE.md](./PROVENANCE.md) — exact-version and temporal provenance
- [REVIEW.md](./REVIEW.md) — public review-state vocabulary

These are documentary interpretation surfaces, not execution engines.

### 7. Historical generated research / 历史研究

`docs/en/**` and `docs/zh/**` preserve the broader bilingual research history.

Historical text remains evidence of what was generated/recorded at that time. Later errata can narrow its current interpretation without pretending the historical wording never existed.

### 8. Explicit August corrections / 8 月显式纠错

- [`../docs/AUGUST_2026_W33_ERRATA.md`](../docs/AUGUST_2026_W33_ERRATA.md)
- [`../docs/AUGUST_2026_W34_ERRATA.md`](../docs/AUGUST_2026_W34_ERRATA.md)
- [`../docs/monthly/2026-08-through-23-strategic-blueprint.md`](../docs/monthly/2026-08-through-23-strategic-blueprint.md)

These records correct source/version or evidence interpretation while preserving historical research artifacts.

## Current authority precedence / 当前解释优先级

When historical generated research conflicts with a stronger explicit correction:

1. explicit erratum for the affected claim/source field
2. current exact source identity in `SOURCES.md`
3. `EVIDENCE.md`, `PROVENANCE.md`, and `REVIEW.md` for evidence semantics
4. domain claim maps for bounded architecture interpretation
5. original generated bilingual material for historical context

This precedence changes current interpretation only.

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md)
2. [ARCHITECTURE.md](./ARCHITECTURE.md)
3. [MEMORY.md](./MEMORY.md)
4. [TOOLS.md](./TOOLS.md)
5. [COLLABORATION.md](./COLLABORATION.md)
6. [SOURCES.md](./SOURCES.md)
7. [PROVENANCE.md](./PROVENANCE.md)
8. [REVIEW.md](./REVIEW.md)
9. August errata/stage synthesis when historical reconciliation is relevant

## Repository-wide implementation classification / 仓库实现定位

The strongest supported repository-wide implementation statement is:

`DOCUMENTARY_AGENT_FOUNDATION_WITH_STRUCTURED_EVIDENCE_AND_PROVENANCE_SUPPORT`.

Not:

`IMPLEMENTED_AUTONOMOUS_AGENT_RUNTIME`.

Formal August monthly closure remains open in the current partial-month stage record.
