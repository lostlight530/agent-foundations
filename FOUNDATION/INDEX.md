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

Jules 生成的研究块可以在事后由本核心纠正或核验，但这不表示 Jules 在生成时已经读取或执行这些规则。本维护不创建或修改 `AGENTS.md`、Jules 任务提示词、Jules 仓库记忆、GPT/云端任务控制、GitHub Actions 或 CI。

## Research correction authority / 研究纠正权威

Generated `docs/en/**` and `docs/zh/**` files preserve research history and may contain wording or metadata that was later calibrated. Keeping that history does not make every historical sentence authoritative.

自动生成的 `docs/en/**` 与 `docs/zh/**` 文件保留研究历史，其中可能包含后来已被校准的措辞或元数据。保留历史不等于历史中的每一句话仍具有最终权威。

For affected August material, use the following precedence when sources conflict:

1. explicit August errata for the affected claim, including W33 and W34 correction records
2. `SOURCES.md` plus current source supplements for exact source/version identity
3. `EVIDENCE.md`, `PROVENANCE.md`, and `REVIEW.md` for claim semantics
4. `ARCHITECTURE.md` / domain maps for bounded repository interpretation
5. original generated bilingual chunk for historical context

对于受影响的 8 月材料，来源或解释冲突时按以下优先级读取：

1. 针对该声明的显式 8 月勘误，包括 W33 与 W34 纠正记录
2. `SOURCES.md` 与当前来源增量，用于准确来源/版本身份
3. `EVIDENCE.md`、`PROVENANCE.md` 与 `REVIEW.md`，用于声明与证据语义
4. `ARCHITECTURE.md` / 各领域映射，用于有边界的仓库解释
5. 原始生成的双语研究块，用于保留历史上下文

Where an original generated chunk conflicts with an explicit erratum or verified-core source record, the corrected evidence interpretation supersedes the conflicting claim or metadata **without erasing the fact that the original chunk was generated**.

当原始生成研究块与显式勘误或 verified-core 来源记录冲突时，以校准后的证据解释为当前解释；这只纠正冲突的声明或元数据，**不抹去原研究块曾真实生成这一历史事实**。

This authority rule applies to committed repository artifacts only. It is not evidence that Jules or any GPT/cloud producer consumed the correction during generation.

这一权威规则只作用于已提交的仓库材料，不代表 Jules 或任何 GPT/云端生产者在生成阶段读取了这些纠正。

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md) — claim, source-identity, theorem, and evidence contract / 声明、来源身份、定理与证据契约
2. [ARCHITECTURE.md](./ARCHITECTURE.md) — system boundary, state scope, evaluation, and observability / 系统边界、状态作用域、评估与可观测性
3. [MEMORY.md](./MEMORY.md) — memory lifecycle and limits / 记忆生命周期与边界
4. [TOOLS.md](./TOOLS.md) — tool authority, observability, recovery / 工具权限、可观测性与恢复
5. [COLLABORATION.md](./COLLABORATION.md) — multi-agent coordination and failure propagation / 多智能体协作与故障传播
6. [SOURCES.md](./SOURCES.md) — historical primary-source registry S01–S32, including corrected exact-version dates for S26/S28/S31 / 历史一手来源登记 S01–S32，并包含 S26/S28/S31 当前已纠正的精确版本日期
7. [SOURCES_2026_08_24.md](./SOURCES_2026_08_24.md) — current protocol/SDK/evaluation source delta S33–S37 / 当前协议、SDK 与评估来源增量 S33–S37
8. [PROVENANCE.md](./PROVENANCE.md) — reproducibility, arXiv version gates, temporal provenance, and AI-use disclosure / 可复现性、arXiv 版本门、时间溯源与 AI 使用披露
9. [REVIEW.md](./REVIEW.md) — independent post-hoc review states and privacy boundary / 独立事后审核状态与隐私边界
10. [`../docs/AUGUST_2026_W33_ERRATA.md`](../docs/AUGUST_2026_W33_ERRATA.md) — W33 post-hoc source/theorem reconciliation / W33 事后来源与定理纠正
11. [`../docs/AUGUST_2026_W34_ERRATA.md`](../docs/AUGUST_2026_W34_ERRATA.md) — W34 exact-version provenance recurrence and correction / W34 精确版本溯源复发与纠正
12. [specs/2026-08-24-state-observability-boundary-design.md](./specs/2026-08-24-state-observability-boundary-design.md) — non-implemented architecture design candidate / 未实现的架构设计候选

Stage synthesis / 阶段综合：[`../docs/monthly/2026-08-through-23-strategic-blueprint.md`](../docs/monthly/2026-08-through-23-strategic-blueprint.md)

Helper: [arxiv_probe.py](./arxiv_probe.py) verifies arXiv identity and submission-history version/date pairs. It assists provenance; it does not prove theorem semantics.

辅助工具：[arxiv_probe.py](./arxiv_probe.py) 用于核验 arXiv 身份与 submission history 中的版本/日期配对。它辅助溯源，不证明定理语义。

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
- A Weekly conflict audit does not independently certify Daily source identity unless the exact source/version check is itself evidenced.
- Reviewer-side policy or tooling does not imply that Jules consumed or enforced that control during generation.
- Session, task, context, memory, attempt, and external-state scopes are not collapsed into one unqualified `state` claim.
- Trace/transcript, outcome, grader result, and reviewer decision remain separate evidence surfaces.
- Independent review remains non-operative and must not modify Jules/GPT automation, GitHub Actions, CI, deployment, repository memory, or runtime behavior.
- Public review records expose evidence outcomes and bounded rationales, not private prompts, private memory, hidden reasoning, or confidential context.

- 每项实质性陈述进入 verified-core 结构化声明后，都应具有稳定的 Claim ID。
- 维护成对声明时，中英文共享同一 Claim ID 与证据状态。
- 外部研究结果永远不自动等同于本仓实现。
- 数学结果必须保留其原始假设与适用域。
- 安全与收敛表述必须有边界且可证伪。
- 自动生成内容只是审核输入，本身不自动成为权威。
- 显式勘误与 verified-core 来源记录可以纠正已提交的生成研究，但不能改写其生成历史。
- 明确引用 arXiv `vN` 时，必须从一手 submission history 核验对应版本和日期后才视为版本身份已验证。
- 来源身份核验与定理/公式核验是两个独立步骤。
- 机制公式在没有对应定理提供边界前，不得升级为形式化误差界或收敛界。
- 一手来源内部冲突必须保留为冲突，不能按方便程度静默选值。
- Weekly 编织必须保留原研究周期；移动文本不能改写时间溯源。
- Weekly 冲突审计只有在精确来源/版本核验本身有证据时，才能独立证明 Daily 的来源身份已验证。
- reviewer 侧规则或工具存在，不代表 Jules 在生成阶段读取或执行了该控制。
- Session、Task、Context、Memory、执行 Attempt 与外部权威状态不能被压成一个没有限定的 `state` 声明。
- Trace/transcript、Outcome、Grader 结果与 Reviewer 决策必须保持为不同证据面。
- 独立审核保持非执行性，不修改 Jules/GPT 自动化、GitHub Actions、CI、部署、仓库记忆或运行时行为。
- 公开审核记录只暴露证据结论与有边界的理由，不公开私有提示、私有记忆、隐藏推理或机密上下文。

These invariants govern the independent verified core and reviewer-side maintenance. They are not assertions that Jules automation enforces the same invariants during generation.

这些不变量约束独立 verified-core 与评审侧维护，并不代表 Jules 自动化在生成阶段已经执行同一组约束。

## Repository status / 仓库状态

The four domain documents are specifications and evidence maps. Their default implementation state is `NOT_IMPLEMENTED` or `REFERENCE_ONLY`. A future runtime may satisfy these contracts, but this repository does not claim that it already does.

四个领域文档是规范与证据映射。其默认实现状态为 `NOT_IMPLEMENTED` 或 `REFERENCE_ONLY`。未来运行时可以实现这些契约，但本仓不声称当前已经实现。

AF-ARCH-007 and AF-ARCH-008 add explicit state-scope and trajectory/outcome evidence boundaries using current sources as references. AF-ARCH-008 is deliberately calibrated to the weaker applicable evidence class where a combined claim uses both a formal SDK reference and first-party engineering guidance. These records do not add MCP, A2A, ADK, or OpenAI SDK dependencies.

AF-ARCH-007 与 AF-ARCH-008 使用当前来源作为参照，补充显式状态作用域边界以及 trajectory/outcome 证据边界。AF-ARCH-008 在组合声明同时依赖正式 SDK 资料与一方工程指导时，刻意采用适用的较弱证据等级，而不是继承最强来源等级。这些记录不会因此引入 MCP、A2A、ADK 或 OpenAI SDK 依赖。

## Current monthly navigation / 当前月度入口

`docs/en/Monthly_Blueprint_Current.md` and `docs/zh/Monthly_Blueprint_Current.md` point to the 2026-08-01 through 2026-08-23 provisional stage rather than the obsolete 2024-05 narrative. The stage synthesis now records the W34 source-version reconciliation and explicit Jules-versus-reviewer ownership boundary. The formal August monthly lifecycle remains open until the natural month closes.

`docs/en/Monthly_Blueprint_Current.md` 与 `docs/zh/Monthly_Blueprint_Current.md` 当前指向 2026-08-01 至 2026-08-23 的 provisional 阶段，而不再让过时的 2024-05 叙事冒充 Current。阶段综合现已记录 W34 来源版本纠正，并明确 Jules 与 reviewer 的控制平面边界。正式 8 月月度生命周期仍保持 `OPEN`，直到自然月真正闭合。

## Documentation-only maintenance / 纯文档维护

Evidence/provenance/review-only changes may state `tests not run — documentation/evidence only` when executable behavior is untouched. This never upgrades implementation or validation status; it only avoids fabricating irrelevant runtime evidence for documentary maintenance.

当变更仅涉及 evidence/provenance/review 且完全未触碰可执行行为时，可以明确记录 `tests not run — documentation/evidence only`。这不会提升任何实现或验证状态，只是避免为纯文档维护伪造无关的运行时证据。