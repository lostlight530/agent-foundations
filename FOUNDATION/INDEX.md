# Agent Foundations — Verified Core / 可验证核心

Status: independently maintained foundation  
Publication: repository-only; not copied into the existing Pages site

## Purpose / 目的

`FOUNDATION/**` is the compact evidence and architecture core of Agent Foundations.

It separates:

- structured architecture/memory/tool/collaboration claims
- source identity and provenance
- evidence and review semantics
- repository implementation status
- explicit design candidates
- historical generated research and later errata

`FOUNDATION/**` 是 Agent Foundations 的紧凑证据与架构核心，用于把结构化声明、来源溯源、证据语义、实现状态与历史生成研究清晰分层。

The repository is primarily a theory, evidence, and documentary architecture base. It is **not** an implemented autonomous-agent runtime.

External equations, paper summaries, protocol mappings, SDK references, pseudocode, and architectural analogies remain `REFERENCE_ONLY`, `PROPOSED`, or another explicit non-implemented state unless a concrete repository artifact implements the claimed behavior.

本仓库主要是理论、证据和文档型架构库，并不是已经实现的自治智能体运行时。外部公式、论文结论、协议映射、SDK 参照、伪代码和架构类比，不能因为被写入文档就自动升级为本仓实现。

## Repository realization map / 仓库真实结构映射

### 1. Domain claim documents / 领域声明

The four primary domain maps are:

- [ARCHITECTURE.md](./ARCHITECTURE.md) — system/evaluation/state boundaries
- [MEMORY.md](./MEMORY.md) — memory lifecycle and limitations
- [TOOLS.md](./TOOLS.md) — tool authority, observability, failure/recovery boundaries
- [COLLABORATION.md](./COLLABORATION.md) — multi-agent coordination and failure propagation

Material domain claims use stable IDs such as `AF-ARCH-*`, `AF-MEM-*`, `AF-TOOL-*`, and `AF-COLLAB-*`.

### 2. Evidence and provenance core / 证据与溯源核心

- [EVIDENCE.md](./EVIDENCE.md) — evidence classes, theorem/claim boundaries, implementation interpretation
- [PROVENANCE.md](./PROVENANCE.md) — source identity, exact-version provenance, reproducibility limits
- [SOURCES.md](./SOURCES.md) — historical source registry S01–S32
- [SOURCES_2026_08_24.md](./SOURCES_2026_08_24.md) — current protocol/SDK/evaluation source delta S33–S37
- [REVIEW.md](./REVIEW.md) — review-state vocabulary and privacy boundary

These files can narrow or correct current interpretation. They do not turn a source into an implementation.

### 3. Structured claim contract / 结构化声明契约

`claim.schema.json` defines the machine-readable claim shape:

- claim ID
- state
- evidence class
- mapping type
- implementation status
- validation status
- source IDs
- scope
- limitations

Its enums make several distinctions explicit, including:

- `SUPPORTED` versus `PROPOSED`
- `REFERENCE_ONLY` versus `IMPLEMENTED`
- source evidence class versus implementation status
- validation state versus claim state

Schema validity is structural evidence only. It does not prove a claim's semantics.

### 4. Repository validator / 仓库验证器

`validate.py` checks documentary/core invariants such as:

- required core files
- claim metadata presence
- stable/unique Claim IDs
- registered source references
- contiguous historical source registry identity where declared
- restricted absolute-overclaim phrases
- protected-path boundaries when an explicit comparison base is supplied

The validator is a deterministic repository-structure tool. It does **not** prove:

- theorem correctness
- formula transcription accuracy
- source-version identity
- translation equivalence
- experimental reproduction
- external deployment behavior
- autonomous-agent capability

### 5. Source identity helper / 来源身份辅助工具

[arxiv_probe.py](./arxiv_probe.py) helps verify arXiv identity and submission-history version/date pairs.

It supports bibliographic provenance. It does not prove theorem semantics, formula interpretation, experimental validity, or implementation status.

### 6. Design candidates / 设计候选

`FOUNDATION/specs/**` and `FOUNDATION/plans/**` contain bounded design/specification material.

A design candidate remains non-implemented until repository evidence explicitly establishes otherwise.

For example:

[specs/2026-08-24-state-observability-boundary-design.md](./specs/2026-08-24-state-observability-boundary-design.md)

is a design candidate, not a claim that the repository already contains the described runtime.

### 7. Historical generated research / 历史生成研究

`docs/en/**` and `docs/zh/**` preserve the bilingual research stream and its historical evolution.

Historical generated text may contain source metadata or claim strength that later required correction. Preservation of that history does not make every historical sentence authoritative today.

### 8. Errata and stage synthesis / 勘误与阶段综合

- [`../docs/AUGUST_2026_W33_ERRATA.md`](../docs/AUGUST_2026_W33_ERRATA.md)
- [`../docs/AUGUST_2026_W34_ERRATA.md`](../docs/AUGUST_2026_W34_ERRATA.md)
- [`../docs/monthly/2026-08-through-23-strategic-blueprint.md`](../docs/monthly/2026-08-through-23-strategic-blueprint.md)

These records correct current interpretation while preserving the fact that the original research artifact existed.

### 9. Presentation surface / 展示层

`index.html` is the repository presentation surface. It is not the verified-core evidence engine and does not determine implementation status for foundation claims.

## Research correction authority / 研究纠正权威

When an original generated research chunk conflicts with stronger explicit correction evidence, use this precedence:

1. explicit erratum for the affected claim/source metadata
2. current exact source identity in `SOURCES.md` / source supplement
3. `EVIDENCE.md`, `PROVENANCE.md`, and `REVIEW.md` for claim/evidence semantics
4. domain claim documents for bounded architecture interpretation
5. original generated bilingual chunk for historical context

This precedence corrects **current interpretation**. It does not erase historical generation.

当历史生成研究与显式勘误或 verified-core 来源记录冲突时，以更强的当前证据解释为准，但不改写“原材料曾经真实生成”这一历史事实。

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md)
2. [ARCHITECTURE.md](./ARCHITECTURE.md)
3. [MEMORY.md](./MEMORY.md)
4. [TOOLS.md](./TOOLS.md)
5. [COLLABORATION.md](./COLLABORATION.md)
6. [SOURCES.md](./SOURCES.md)
7. [SOURCES_2026_08_24.md](./SOURCES_2026_08_24.md)
8. [PROVENANCE.md](./PROVENANCE.md)
9. [REVIEW.md](./REVIEW.md)
10. August errata and stage synthesis where the affected material requires reconciliation

## Invariants / 不变量

- Material structured claims use stable Claim IDs.
- Paired English/Chinese claims retain the same evidence and implementation state where paired maintenance is used.
- External results never automatically count as repository implementation.
- Mathematical results retain original assumptions and domain.
- Safety and convergence statements remain scoped and falsifiable.
- Source identity verification and theorem/formula verification are separate steps.
- An explicit arXiv `vN` is not version-verified until the version/date pair is checked against primary submission history.
- A mechanism equation is not promoted to a formal error/convergence bound without the theorem that supplies that bound.
- Primary-source disagreements are preserved as conflicts when they cannot be resolved from stronger evidence.
- Historical weaving or relocation does not rewrite temporal provenance.
- Session, task, context, memory, execution attempt, and authoritative external state are separate scopes.
- Trace/transcript, outcome, grader result, and reviewer decision are separate evidence surfaces.
- Public repository records expose evidence outcomes and bounded rationales, not private prompts, hidden reasoning, private memory, confidential context, or unpublished future control strategy.

## Repository status / 仓库状态

The four domain documents are specifications/evidence maps. Their individual claims explicitly declare implementation state.

Most architecture concepts remain `REFERENCE_ONLY`, `NOT_IMPLEMENTED`, or `PARTIAL_PROTOTYPE` unless a repository artifact establishes a stronger status.

AF-ARCH-007 and AF-ARCH-008 add state-scope and trajectory/outcome evidence boundaries using current external sources as references. They do not imply MCP, A2A, ADK, or OpenAI SDK runtime integration.

## Current August navigation / 当前 8 月入口

`docs/en/Monthly_Blueprint_Current.md` and `docs/zh/Monthly_Blueprint_Current.md` point to the current August provisional stage rather than the obsolete 2024-05 narrative.

The August stage synthesis records the W33/W34 source-version corrections and keeps formal August month closure open until the natural month ends.

Current partial-month synthesis:

[`../docs/monthly/2026-08-through-23-strategic-blueprint.md`](../docs/monthly/2026-08-through-23-strategic-blueprint.md)
