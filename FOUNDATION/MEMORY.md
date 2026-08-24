# Memory System / 记忆系统

## Repository realization boundary / 本仓实现边界

Agent Foundations does **not** implement an agent-memory runtime, vector store, retrieval service, compaction engine, consolidation service, retention engine, or cross-session memory service.

The claims below are research/evidence maps. Their implementation and validation fields describe the local repository state; external literature does not upgrade those fields automatically.

本仓没有实现 Agent memory runtime、vector store、retrieval service、compaction engine、consolidation service、retention engine 或 cross-session memory service。下列 Claim 属于研究/证据映射，本地实现与验证状态以明确字段为准。

## AF-MEM-001 — Memory is a lifecycle / 记忆是生命周期

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E3_REPRODUCIBLE_PREPRINT`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S09

**EN.** Agent memory includes selection, ingestion, provenance, scope, retrieval, anticipation, compaction, consolidation, retention, and deletion. A vector store alone does not implement this lifecycle.

**ZH.** 智能体记忆包含选择、摄取、来源、作用域、检索、预期、压缩、合并、保留和删除。单一向量库不等于完整记忆生命周期。

**Scope and limits / 范围与局限:** S09 reports a specific reference implementation; this repository has none. / S09 报告的是特定参考实现，本仓没有对应实现。

## AF-MEM-002 — Prospective memory remains fallible / 前瞻记忆仍会失败

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `COUNTEREVIDENCE`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S08

**EN.** PM-Bench reports substantial failure on delayed intentions even in its strongest tested configuration. Reliable recall cannot be inferred from context length, retrieval availability, or a single benchmark score.

**ZH.** PM-Bench 表明，即便最强测试配置在延迟意图任务上仍存在显著失败。不能从上下文长度、可用检索或单个基准分数推断可靠记忆。

**Scope and limits / 范围与局限:** The numerical result belongs to the paper’s models, configurations, and metric. `STATIC_CHECKED` here is documentary/source review only. / 数值结果只属于论文所测模型、配置和指标；此处 `STATIC_CHECKED` 仅指文档/来源核对。

## AF-MEM-003 — Provenance precedes persistence / 持久化之前先有来源

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** A memory record should carry origin, actor, time, scope, confidence, transformation history, retention rule, and revocation state before it becomes durable or influences a privileged action.

**ZH.** 记忆记录在持久化或影响高权限动作前，应携带来源、参与者、时间、作用域、置信度、变换历史、保留规则和撤销状态。

**Scope and limits / 范围与局限:** This is a proposed memory-record contract. Agent Foundations does not implement the persistence layer. / 这是候选记忆记录契约；Agent Foundations 没有实现对应持久化层。

## AF-MEM-004 — Compaction requires fidelity checks / 压缩需要保真检查

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S03, S09

**EN.** Compaction is a lossy transformation unless critical constraints, unresolved decisions, evidence links, and deferred intentions survive explicit checks. Token reduction alone is not success.

**ZH.** 若关键约束、未决决定、证据链接和延迟意图没有通过明确检查，压缩就是有损变换。仅减少 Token 不代表成功。

**Scope and limits / 范围与局限:** This repository has no compaction implementation or task-specific fidelity benchmark. / 本仓没有压缩实现，也没有对应任务级保真 benchmark。

## AF-MEM-005 — Versioning enables correction, not correctness / 版本化支持纠错而非自动正确

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Append-only revisions, explicit supersession, rollback, and deletion tombstones make memory changes inspectable. They do not decide which version is true; validation and authority rules remain necessary.

**ZH.** 追加式修订、明确替代、回滚和删除墓碑使记忆变更可检查，但不会自动决定哪个版本为真；仍需验证和权限规则。

**Scope and limits / 范围与局限:** This is a proposed lifecycle principle; Agent Foundations has no memory-versioning runtime. / 这是候选生命周期原则；Agent Foundations 没有 memory-versioning runtime。
