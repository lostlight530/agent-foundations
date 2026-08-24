# Architecture Principles / 架构原则

## AF-ARCH-001 — System boundary / 系统边界

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S01, S03

**EN.** An evaluated agent is the complete configured system: model, instructions, tools, permissions, memory, control loop, safeguards, retries, budgets, environment, and scoring procedure. Model identity alone is insufficient to reproduce or compare an agent result.

**ZH.** 被评估的智能体是完整配置系统：模型、指令、工具、权限、记忆、控制循环、防护、重试、预算、环境和评分过程。仅凭模型名称不足以复现或比较智能体结果。

**Scope and limits / 范围与局限:** This is an evaluation and documentation boundary. The repository does not contain an agent runtime. / 这是评估与文档边界；本仓不包含智能体运行时。

## AF-ARCH-002 — Deterministic shell, stochastic component / 确定性外壳与随机组件

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02, S03

**EN.** Deterministic validation, schemas, permissions, budgets, idempotency keys, and state transitions can constrain an agent without making the underlying model deterministic. The correct engineering claim is bounded behavior at enforced interfaces, not deterministic cognition.

**ZH.** 确定性验证、Schema、权限、预算、幂等键和状态迁移可以约束智能体，但不会使底层模型变成确定性系统。正确工程表述是“在强制接口上约束行为”，而不是“确定性认知”。

**Scope and limits / 范围与局限:** Constraints cover only modeled paths and correctly enforced controls. / 约束只覆盖已建模路径和正确执行的控制。

## AF-ARCH-003 — Theorem scope is not agent scope / 定理适用域不等于智能体适用域

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `COUNTEREVIDENCE`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S10, S11

**EN.** RAFA’s regret result and CHMAS’s convergence result apply under their stated formal models and assumptions. They do not establish convergence, safety, or sample efficiency for arbitrary LLM-agent deployments.

**ZH.** RAFA 的遗憾界和 CHMAS 的收敛结果只在各自形式模型与假设下成立，不能证明任意 LLM 智能体部署的收敛性、安全性或样本效率。

**Scope and limits / 范围与局限:** Exact assumptions must accompany any reused formula or bound. / 复用任何公式或边界时必须同时保留精确假设。

## AF-ARCH-004 — Evaluators create evidence, not truth / 评估器产生证据而非真理

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S03, S04, S05, S17

**EN.** Executable evaluators, trace inspection, and independent review can strengthen a claim. Their coverage, false positives, false negatives, contamination, reward hacking, and evaluation awareness remain part of the result.

**ZH.** 可执行评估器、轨迹检查和独立评审可以增强证据，但其覆盖率、误报、漏报、污染、奖励投机和评估意识仍属于结果的一部分。

**Scope and limits / 范围与局限:** Passing a finite evaluator establishes only the tested properties. / 通过有限评估器只证明被测试的属性。

## AF-ARCH-005 — Constitutions are governed policies / 宪法是受治理的策略

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DESIGN_ANALOGY`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S06, S07, S16

**EN.** Natural-language constitutions and policies can shape behavior, yet compliance is empirical and revision remains necessary. Policy generation and policy following are different capabilities.

**ZH.** 自然语言宪法和策略可以塑造行为，但遵循程度必须通过实证评估，且需要持续修订。策略生成与策略遵循是不同能力。

**Scope and limits / 范围与局限:** A document is neither a runtime guard nor a safety proof. / 文档既不是运行时防护，也不是安全证明。

## AF-ARCH-006 — Release claims require reconstructable records / 发布声明需要可重建记录

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `PARTIAL_PROTOTYPE`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S01, S03, S18

**EN.** A release claim should identify the tested tree, configuration, fixtures, commands, budgets, metrics, raw results, and reviewer decision. This directory’s validator establishes documentary structure but does not reproduce external experiments.

**ZH.** 发布声明应标识被测代码树、配置、夹具、命令、预算、指标、原始结果和评审决定。本目录验证器只建立文档结构，不复现外部实验。

**Scope and limits / 范围与局限:** Supply-chain provenance and behavioral evidence are complementary, not interchangeable. / 供应链来源与行为证据互补但不可互换。

## AF-ARCH-007 — State scope must be explicit / 状态作用域必须显式

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DESIGN_REQUIREMENT`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `DOCUMENT_REVIEW_ONLY`
- **Sources / 来源:** S34, S37 in `SOURCES_2026_08_24.md`

**EN.** Session history, task lifecycle, current-session state, cross-session memory, protocol context, and external authoritative state are different scopes. Architecture records should name the scope and identity before claiming persistence, continuity, or ownership.

**ZH.** 会话历史、任务生命周期、当前会话状态、跨会话记忆、协议上下文与外部权威状态属于不同作用域。任何持久化、连续性或所有权声明，都应先明确状态作用域与身份。

**Scope and limits / 范围与局限:** A2A and Google ADK provide concrete external data-model examples. This repository does not implement either runtime. / A2A 与 Google ADK 只是外部数据模型参照，本仓并未实现对应运行时。

## AF-ARCH-008 — Trajectory and outcome are complementary evidence / 轨迹与结果是互补证据

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E5_BACKGROUND`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `DOCUMENT_REVIEW_ONLY`
- **Sources / 来源:** S35 (`E1_PRIMARY_STANDARD`) and S36 (`E5_BACKGROUND`) in `SOURCES_2026_08_24.md`

**EN.** A trace or transcript describes how an execution unfolded; an outcome describes the resulting environment or artifact state; graders interpret selected properties of one or both. None of these should silently substitute for the others.

**ZH.** Trace 或 transcript 描述执行过程，outcome 描述最终环境或产物状态，grader 对其中部分属性进行判断。三者不能静默互相替代。

**Scope and limits / 范围与局限:** OpenAI Agents SDK tracing supplies a first-party SDK trace/span reference, while Anthropic's task/trial/grader/trajectory/outcome/harness decomposition is first-party engineering guidance rather than a formal standard. The combined architecture claim therefore keeps the lower `E5_BACKGROUND` evidence class instead of inheriting the strongest source class. Neither source proves that a particular trace is complete or that an outcome is correct. / OpenAI Agents SDK tracing 提供一方 SDK 的 trace/span 参照；Anthropic 的 task/trial/grader/trajectory/outcome/harness 分解属于一方工程指导而非正式标准。因此组合后的架构声明保留较低的 `E5_BACKGROUND` 证据等级，而不继承其中最强来源等级。两者都不能证明某条轨迹必然完整或某个结果必然正确。
