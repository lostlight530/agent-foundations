# Agent Foundations — Verified Core / 可验证核心

Version: 2026-08-17  
Status: independent maintained foundation  
Publication: repository-only; not copied into the existing Pages site

## Purpose / 目的

This directory is the compact, independently maintained core of Agent Foundations. It separates evidence, architecture decisions, source provenance, and repository status from the existing SOP-generated research stream.

本目录是 Agent Foundations 的紧凑、独立维护核心。它把证据、架构判断、来源溯源和仓库实现状态与现有 SOP 自动生成研究流分离。

The repository is a theory and evidence base. It is not an implemented autonomous-agent runtime. Equations, paper summaries, pseudocode, and architecture analogies remain references until an executable artifact and repository test exist.

本仓库是理论与证据库，不是已实现的自治智能体运行时。公式、论文摘要、伪代码和架构类比，在出现可执行产物及仓库测试前均只属于参考材料。

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md) — claim, source-identity, theorem, and evidence contract / 声明、来源身份、定理与证据契约
2. [ARCHITECTURE.md](./ARCHITECTURE.md) — system boundary and evaluation / 系统边界与评估
3. [MEMORY.md](./MEMORY.md) — memory lifecycle and limits / 记忆生命周期与边界
4. [TOOLS.md](./TOOLS.md) — tool authority, observability, recovery / 工具权限、可观测性与恢复
5. [COLLABORATION.md](./COLLABORATION.md) — multi-agent coordination and failure propagation / 多智能体协作与故障传播
6. [SOURCES.md](./SOURCES.md) — primary-source registry with explicit version identities / 带准确版本身份的一手来源登记
7. [PROVENANCE.md](./PROVENANCE.md) — reproducibility, arXiv version gates, temporal provenance, and AI-use disclosure / 可复现性、arXiv 版本门、时间溯源与 AI 使用披露

Helper: [arxiv_probe.py](./arxiv_probe.py) verifies arXiv identity and submission-history version/date pairs. It assists provenance; it does not prove theorem semantics.

辅助工具：[arxiv_probe.py](./arxiv_probe.py) 用于核验 arXiv 身份与版本/日期配对。它辅助溯源，不证明定理语义。

## Invariants / 不变量

- Every material statement has one stable Claim ID.
- English and Chinese text share the same Claim ID and evidence state.
- External results never count as repository implementation.
- Mathematical results retain their original assumptions and domain.
- Safety and convergence statements remain scoped and falsifiable.
- Generated content is input to review, never authority.
- An explicit arXiv `vN` is not verified until the cited version and its date are paired from primary submission history.
- Source identity verification and theorem/formula verification are separate steps.
- A mechanism equation is not promoted to a formal error/convergence bound without the theorem that supplies the bound.
- Primary-source disagreements are preserved as conflicts, not silently resolved by convenience.
- Weekly weaving preserves the original research period; moving text does not rewrite temporal provenance.

- 每项实质性陈述都具有稳定的 Claim ID。
- 中英文共享同一 Claim ID 与证据状态。
- 外部研究结果不等同于本仓实现。
- 数学结果必须保留原始假设和适用域。
- 安全与收敛表述必须有边界且可证伪。
- 自动生成内容只作为评审输入，不构成权威。
- 明确引用 arXiv `vN` 时，必须从一手 submission history 核验该版本及对应日期后才视为版本身份已验证。
- 来源身份核验与定理/公式核验是两个独立步骤。
- 机制公式在没有对应定理提供边界前，不得升级为形式化误差/收敛界。
- 一手来源内部冲突必须保留为冲突，不按方便程度静默选值。
- Weekly 编织必须保留原研究周期；移动文本不能改写时间溯源。

## Repository status / 仓库状态

The four domain documents are specifications and evidence maps. Their default implementation state is `NOT_IMPLEMENTED` or `REFERENCE_ONLY`. A future runtime may satisfy these contracts, but this repository does not claim that it already does.

四个领域文档是规范与证据映射。其默认实现状态为 `NOT_IMPLEMENTED` 或 `REFERENCE_ONLY`。未来运行时可以实现这些契约，但本仓不声称已经实现。

## Documentation-only maintenance / 纯文档维护

Evidence/provenance-only changes may state `tests not run — documentation/evidence only` when executable behavior is untouched. This never upgrades implementation or validation status; it only avoids fabricating irrelevant runtime evidence for documentary maintenance.
