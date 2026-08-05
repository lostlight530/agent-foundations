# Agent Foundations — Verified Core / 可验证核心

Version: 2026-08-05  
Status: independent maintained foundation  
Publication: repository-only; not copied into the existing Pages site

## Purpose / 目的

This directory is the compact, independently maintained core of Agent Foundations. It separates evidence, architecture decisions, and repository status from the existing SOP-generated research stream.

本目录是 Agent Foundations 的紧凑、独立维护核心。它把证据、架构判断和仓库实现状态与现有 SOP 自动生成研究流分离。

The repository is a theory and evidence base. It is not an implemented autonomous-agent runtime. Equations, paper summaries, pseudocode, and architecture analogies remain references until an executable artifact and repository test exist.

本仓库是理论与证据库，不是已实现的自治智能体运行时。公式、论文摘要、伪代码和架构类比，在出现可执行产物及仓库测试前均只属于参考材料。

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md) — claim and evidence contract / 声明与证据契约
2. [ARCHITECTURE.md](./ARCHITECTURE.md) — system boundary and evaluation / 系统边界与评估
3. [MEMORY.md](./MEMORY.md) — memory lifecycle and limits / 记忆生命周期与边界
4. [TOOLS.md](./TOOLS.md) — tool authority, observability, recovery / 工具权限、可观测性与恢复
5. [COLLABORATION.md](./COLLABORATION.md) — multi-agent coordination and failure propagation / 多智能体协作与故障传播
6. [SOURCES.md](./SOURCES.md) — primary-source registry / 一手来源登记
7. [PROVENANCE.md](./PROVENANCE.md) — reproducibility and AI-use disclosure / 可复现性与 AI 使用披露

## Invariants / 不变量

- Every material statement has one stable Claim ID.
- English and Chinese text share the same Claim ID and evidence state.
- External results never count as repository implementation.
- Mathematical results retain their original assumptions and domain.
- Safety and convergence statements remain scoped and falsifiable.
- Generated content is input to review, never authority.

- 每项实质性陈述都具有稳定的 Claim ID。
- 中英文共享同一 Claim ID 与证据状态。
- 外部研究结果不等同于本仓实现。
- 数学结果必须保留原始假设和适用域。
- 安全与收敛表述必须有边界且可证伪。
- 自动生成内容只作为评审输入，不构成权威。

## Repository status / 仓库状态

The four domain documents are specifications and evidence maps. Their default implementation state is `NOT_IMPLEMENTED` or `REFERENCE_ONLY`. A future runtime may satisfy these contracts, but this repository does not claim that it already does.

四个领域文档是规范与证据映射。其默认实现状态为 `NOT_IMPLEMENTED` 或 `REFERENCE_ONLY`。未来运行时可以实现这些契约，但本仓不声称已经实现。
