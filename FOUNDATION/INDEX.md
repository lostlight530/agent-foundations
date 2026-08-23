# Agent Foundations — Verified Core / 可验证核心

Status: independent maintained foundation  
Publication: repository-only; not copied into the existing Pages site

## Purpose / 目的

This directory is the compact, independently maintained core of Agent Foundations. It separates evidence, architecture decisions, source provenance, and repository status from the existing SOP-generated research stream.

本目录是 Agent Foundations 的紧凑、独立维护核心。它把证据、架构判断、来源溯源和仓库实现状态与现有 SOP 自动生成研究流分离。

The repository is a theory and evidence base. It is not an implemented autonomous-agent runtime. Equations, paper summaries, pseudocode, architecture analogies, protocol mappings, and SDK references remain references until an executable artifact and repository test exist.

本仓库是理论与证据库，不是已实现的自治智能体运行时。公式、论文摘要、伪代码、架构类比、协议映射与 SDK 参照，在出现可执行产物及仓库测试前均只属于参考材料。

## Jules automation boundary / 与 Jules 自动化的边界

`FOUNDATION/**` is an independent verified-core and reviewer-governance layer outside the existing Jules Daily/Weekly/Monthly SOP automation stream.

`FOUNDATION/**` 不是 Jules 的任务提示词、仓库记忆或自动化规则文件，也不自动修改现有 Jules 任务的行为。它用于在 Jules 产物生成后进行独立核验、证据校准、架构判断与长期知识维护。

A Jules-generated research chunk may later be corrected or checked against this core, but that does not mean Jules consumed or followed these rules during generation. This maintenance intentionally does not create or modify `AGENTS.md`, Jules task prompts, Jules repository memory, GPT/cloud task controls, GitHub Actions, or CI.

## Research correction authority / 研究纠正权威

Generated `docs/en/**` and `docs/zh/**` files preserve research history and may contain wording or metadata that was later calibrated. Keeping that history does not make every historical sentence authoritative.

For affected August material, use the following precedence when sources conflict:

1. explicit August errata for the affected claim
2. `SOURCES.md` plus current source supplements for exact source/version identity
3. `EVIDENCE.md`, `PROVENANCE.md`, and `REVIEW.md` for claim semantics
4. `ARCHITECTURE.md` / domain maps for bounded repository interpretation
5. original generated bilingual chunk for historical context

Where an original generated chunk conflicts with an explicit erratum or verified-core source record, the corrected evidence interpretation supersedes the conflicting claim or metadata **without erasing the fact that the original chunk was generated**.

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md) — claim, source-identity, theorem, and evidence contract
2. [ARCHITECTURE.md](./ARCHITECTURE.md) — system boundary, state scope, evaluation, and observability
3. [MEMORY.md](./MEMORY.md) — memory lifecycle and limits
4. [TOOLS.md](./TOOLS.md) — tool authority, observability, recovery
5. [COLLABORATION.md](./COLLABORATION.md) — multi-agent coordination and failure propagation
6. [SOURCES.md](./SOURCES.md) — historical primary-source registry S01–S32
7. [SOURCES_2026_08_24.md](./SOURCES_2026_08_24.md) — current protocol/SDK/evaluation source delta S33–S37
8. [PROVENANCE.md](./PROVENANCE.md) — reproducibility, arXiv version gates, temporal provenance, and AI-use disclosure
9. [REVIEW.md](./REVIEW.md) — independent post-hoc review states and privacy boundary
10. [specs/2026-08-24-state-observability-boundary-design.md](./specs/2026-08-24-state-observability-boundary-design.md) — non-implemented architecture design candidate

Stage synthesis: [`../docs/monthly/2026-08-through-23-strategic-blueprint.md`](../docs/monthly/2026-08-through-23-strategic-blueprint.md)

Helper: [arxiv_probe.py](./arxiv_probe.py) verifies arXiv identity and submission-history version/date pairs. It assists provenance; it does not prove theorem semantics.

## Invariants / 不变量

- Every material statement has one stable Claim ID when it enters verified-core structured claims.
- English and Chinese text share the same Claim ID and evidence state where paired claims are maintained.
- External results never count as repository implementation.
- Mathematical results retain their original assumptions and domain.
- Safety and convergence statements remain scoped and falsifiable.
- Generated content is input to review, never authority by itself.
- Explicit errata and verified-core source records may correct committed generated research without rewriting its generation history.
- An explicit arXiv `vN` is not verified until the cited version and its date are paired from primary submission history.
- Source identity verification and theorem/formula verification are separate steps.
- A mechanism equation is not promoted to a formal error/convergence bound without the theorem that supplies the bound.
- Primary-source disagreements are preserved as conflicts, not silently resolved by convenience.
- Weekly weaving preserves the original research period; moving text does not rewrite temporal provenance.
- Session, task, context, memory, attempt, and external-state scopes are not collapsed into one unqualified `state` claim.
- Trace/transcript, outcome, grader result, and reviewer decision remain separate evidence surfaces.
- Independent review remains non-operative and must not modify Jules/GPT automation, GitHub Actions, CI, deployment, repository memory, or runtime behavior.
- Public review records expose evidence outcomes and bounded rationales, not private prompts, private memory, hidden reasoning, or confidential context.

## Repository status / 仓库状态

The four domain documents are specifications and evidence maps. Their default implementation state is `NOT_IMPLEMENTED` or `REFERENCE_ONLY`. A future runtime may satisfy these contracts, but this repository does not claim that it already does.

AF-ARCH-007 and AF-ARCH-008 add explicit state-scope and trajectory/outcome evidence boundaries using current primary standards as references. They do not add MCP, A2A, ADK, or OpenAI SDK dependencies.

## Current monthly navigation / 当前月度入口

`docs/en/Monthly_Blueprint_Current.md` and `docs/zh/Monthly_Blueprint_Current.md` now point to the 2026-08-01 through 2026-08-23 provisional stage rather than the obsolete 2024-05 narrative. The formal August monthly lifecycle remains open until the natural month closes.

## Documentation-only maintenance / 纯文档维护

Evidence/provenance/review-only changes may state `tests not run — documentation/evidence only` when executable behavior is untouched. This never upgrades implementation or validation status; it only avoids fabricating irrelevant runtime evidence for documentary maintenance.
