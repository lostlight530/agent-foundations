# Memory System / 记忆系统

## Repository realization boundary / 本仓实现边界

Agent Foundations does **not** implement an agent memory runtime, vector store, retrieval service, compaction engine, retention engine, or cross-session memory service.

The claims below are research/evidence propositions. Their `Implementation / 实现` field is authoritative for local implementation status. `REFERENCE_ONLY` and `NOT_IMPLEMENTED` must not be read as hidden or partial runtime capability.

本仓没有实现智能体记忆运行时、向量库、检索服务、压缩引擎、保留策略引擎或跨会话记忆服务。下列条目属于研究/证据声明，本地实现状态以每条 Claim 的 `Implementation / 实现` 字段为准。

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

**Scope and limits / 范围与局限:** The numerical result belongs to the paper’s models, configurations, and metric; `STATIC_CHECKED` here is documentary/source review, not a local memory experiment. / 数值结果只属于论文所测模型、配置和指标；此处 `STATIC_CHECKED` 指文档/来源核对，不是本仓记忆实验。

## AF-MEM-003 — Provenance precedes persistence / 持久化之前先有来源

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** A memory record should carry origin, actor, time, scope, confidence, transformation history, retention rule, and revocation state before it becomes durable or influences a privileged action.

**ZH.** 记忆记录在持久化或影响高权限动作前，应携带来源、参与者、时间、作用域、置信度、变换历史、保留规则和撤销状态。

**Scope and limits / 范围与局限:** This is a proposed design requirement, not an implemented memory-record schema in this repository. / 这是候选设计要求，并非本仓已实现的 memory-record schema。

## AF-MEM-004 — Compaction requires fidelity checks / 压缩需要保真检查

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S03, S09

**EN.** Compaction is a lossy transformation unless critical constraints, unresolved decisions, evidence links, and deferred intentions survive explicit checks. Token reduction alone is not success.

**ZH.** 若关键约束、未决决定、证据链接和延迟意图没有通过明确检查，压缩就是有损变换。仅减少 Token 不代表成功。

**Scope and limits / 范围与局限:** No compaction engine or fidelity metric is implemented here. / 本仓没有实现压缩引擎或保真指标。

## AF-MEM-005 — Versioning enables correction, not correctness / 版本化支持纠错而非自动正确

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Append-only revisions, explicit supersession, rollback, and deletion tombstones make memory changes inspectable. They do not decide which version is true; validation and authority rules remain necessary.

**ZH.** 追加式修订、明确替代、回滚和删除墓碑使记忆变更可检查，但不会自动决定哪个版本为真；仍需验证和权限规则。

**Scope and limits / 范围与局限:** The repository preserves versioned source/research history, but that documentary history is not an implemented agent-memory versioning service. / 本仓保留版本化来源与研究历史，但这种文档历史不是智能体记忆版本服务。