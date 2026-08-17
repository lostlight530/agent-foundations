# Agent Foundations — Verified Core / 可验证核心

Status: independent maintained foundation  
Publication: repository-only; not copied into the existing Pages site

## Purpose / 目的

This directory is the compact, independently maintained core of Agent Foundations. It separates evidence, architecture decisions, source provenance, and repository status from the existing SOP-generated research stream.

本目录是 Agent Foundations 的紧凑、独立维护核心。它把证据、架构判断、来源溯源和仓库实现状态与现有 SOP 自动生成研究流分离。

The repository is a theory and evidence base. It is not an implemented autonomous-agent runtime. Equations, paper summaries, pseudocode, and architecture analogies remain references until an executable artifact and repository test exist.

本仓库是理论与证据库，不是已实现的自治智能体运行时。公式、论文摘要、伪代码和架构类比，在出现可执行产物及仓库测试前均只属于参考材料。

## Jules automation boundary / 与 Jules 自动化的边界

`FOUNDATION/**` is an independent verified-core and reviewer-governance layer outside the existing Jules Daily/Weekly/Monthly SOP automation stream.

`FOUNDATION/**` 不是 Jules 的任务提示词、仓库记忆或自动化规则文件，也不自动修改现有 Jules 任务的行为。它用于在 Jules 产物生成后进行独立核验、证据校准、架构判断与长期知识维护。

A Jules-generated research chunk may later be corrected or checked against this core, but that does not mean Jules consumed or followed these rules during generation. This maintenance intentionally does not create or modify `AGENTS.md`, Jules task prompts, Jules repository memory, GPT/cloud task controls, GitHub Actions, or CI.

Jules 自动生成的研究块可以在事后被本核心纠正或核验，但这不表示 Jules 在生成时读取或遵循了这些规则。本维护明确不创建或修改 `AGENTS.md`、Jules 任务提示词、Jules 仓库记忆、GPT/云端任务控制、GitHub Actions 或 CI。

## Research correction authority / 研究纠正权威

Generated `docs/en/**` and `docs/zh/**` files preserve the research history and may contain wording or metadata that was later calibrated. Keeping that history does not make every historical sentence authoritative.

自动生成的 `docs/en/**` 与 `docs/zh/**` 保留研究历史，其中可能存在后来已经被校准的措辞或元数据。保留历史不等于历史中的每一句话继续具有最终权威。

For affected W33 material, read the evidence in this order:

1. [`docs/AUGUST_2026_W33_ERRATA.md`](../docs/AUGUST_2026_W33_ERRATA.md) for explicit corrections to version/date pairs, theorem strength, formula interpretation, and weekly provenance
2. [`SOURCES.md`](./SOURCES.md) for exact primary-source identity and version-specific provenance
3. [`EVIDENCE.md`](./EVIDENCE.md) and [`PROVENANCE.md`](./PROVENANCE.md) for claim/evidence semantics
4. the original generated bilingual chunk for historical context and the research path that produced it

对于受影响的 W33 材料，读取顺序为：先看 W33 勘误，再看准确来源登记和证据/溯源契约，最后回到原自动生成双语研究块理解历史上下文。

Where an original generated chunk conflicts with an explicit erratum or verified-core source record, the corrected evidence interpretation supersedes the conflicting claim or metadata **without erasing the fact that the original chunk was generated**.

当原生成研究块与显式勘误或可验证核心来源记录冲突时，以校准后的证据解释为准；这只纠正声明或元数据，不抹去原研究块曾真实生成这一历史事实。

This authority rule applies to committed repository artifacts only. It is not evidence that Jules or any GPT/cloud producer consumed the correction during generation.

该权威规则只作用于已提交的仓库材料，不表示 Jules 或任何 GPT/云端生产者在生成阶段读取了这些纠正。

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md) — claim, source-identity, theorem, and evidence contract / 声明、来源身份、定理与证据契约
2. [ARCHITECTURE.md](./ARCHITECTURE.md) — system boundary and evaluation / 系统边界与评估
3. [MEMORY.md](./MEMORY.md) — memory lifecycle and limits / 记忆生命周期与边界
4. [TOOLS.md](./TOOLS.md) — tool authority, observability, recovery / 工具权限、可观测性与恢复
5. [COLLABORATION.md](./COLLABORATION.md) — multi-agent coordination and failure propagation / 多智能体协作与故障传播
6. [SOURCES.md](./SOURCES.md) — primary-source registry with explicit version identities / 带准确版本身份的一手来源登记
7. [PROVENANCE.md](./PROVENANCE.md) — reproducibility, arXiv version gates, temporal provenance, and AI-use disclosure / 可复现性、arXiv 版本门、时间溯源与 AI 使用披露
8. [REVIEW.md](./REVIEW.md) — independent post-hoc review states, global-practice alignment, and privacy boundary / 独立事后审核状态、全球实践对齐与隐私边界

Helper: [arxiv_probe.py](./arxiv_probe.py) verifies arXiv identity and submission-history version/date pairs. It assists provenance; it does not prove theorem semantics.

辅助工具：[arxiv_probe.py](./arxiv_probe.py) 用于核验 arXiv 身份与版本/日期配对。它辅助溯源，不证明定理语义。

## Invariants / 不变量

- Every material statement has one stable Claim ID.
- English and Chinese text share the same Claim ID and evidence state.
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
- Independent review remains non-operative and must not modify Jules/GPT automation, GitHub Actions, CI, deployment, repository memory, or runtime behavior.
- Public review records expose evidence outcomes and bounded rationales, not private prompts, private memory, hidden reasoning, or confidential context.

- 每项实质性陈述都具有稳定的 Claim ID。
- 中英文共享同一 Claim ID 与证据状态。
- 外部研究结果不等同于本仓实现。
- 数学结果必须保留原始假设和适用域。
- 安全与收敛表述必须有边界且可证伪。
- 自动生成内容只是审核输入，本身不自动成为权威。
- 显式勘误与可验证核心来源记录可以纠正已提交的自动生成研究，但不改写其生成历史。
- 明确引用 arXiv `vN` 时，必须从一手 submission history 核验该版本及对应日期后才视为版本身份已验证。
- 来源身份核验与定理/公式核验是两个独立步骤。
- 机制公式在没有对应定理提供边界前，不得升级为形式化误差/收敛界。
- 一手来源内部冲突必须保留为冲突，不按方便程度静默选值。
- Weekly 编织必须保留原研究周期；移动文本不能改写时间溯源。
- 独立审核保持非执行性，不修改 Jules/GPT 自动化、GitHub Actions、CI、部署、仓库记忆或运行时行为。
- 公开审核记录只暴露证据结论与有界理由，不公开私有提示、私有记忆、隐藏推理或机密上下文。

These invariants govern the independent verified core and reviewer-side maintenance. They are not assertions that Jules automation enforces the same invariants during generation.

这些不变量约束独立可验证核心和评审侧维护，不代表 Jules 自动化在生成阶段已经执行同一组约束。

## Repository status / 仓库状态

The four domain documents are specifications and evidence maps. Their default implementation state is `NOT_IMPLEMENTED` or `REFERENCE_ONLY`. A future runtime may satisfy these contracts, but this repository does not claim that it already does.

四个领域文档是规范与证据映射。其默认实现状态为 `NOT_IMPLEMENTED` 或 `REFERENCE_ONLY`。未来运行时可以实现这些契约，但本仓不声称已经实现。

## Documentation-only maintenance / 纯文档维护

Evidence/provenance/review-only changes may state `tests not run — documentation/evidence only` when executable behavior is untouched. This never upgrades implementation or validation status; it only avoids fabricating irrelevant runtime evidence for documentary maintenance.
