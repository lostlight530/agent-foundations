# Tool System / 工具系统

## Repository realization boundary / 本仓实现边界

Agent Foundations does **not** implement an agent tool runtime, permission broker, sandbox, monitor, replay engine, idempotent side-effect layer, or approval service.

The claims below are external research/design propositions. Their `Implementation / 实现` field controls local status. `STATIC_CHECKED` means documentary/source-level checking where used; it does not mean the corresponding tool behavior ran in this repository.

本仓没有实现智能体工具运行时、权限代理、沙箱、监控器、回放引擎、幂等副作用层或审批服务。下列条目属于外部研究/设计声明，本地状态以 `Implementation / 实现` 字段为准。

## AF-TOOL-001 — Authority is explicit and per action / 权限按动作明确授予

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Tool availability is not authority. Each consequential action needs an authenticated actor, allowed operation, bounded target, validated arguments, least privilege, and an auditable result.

**ZH.** 工具可用不等于获得授权。每个有后果的动作都需要认证参与者、允许操作、受限目标、已验证参数、最小权限和可审计结果。

**Scope and limits / 范围与局限:** This repository records the principle only; it has no permission-enforcement implementation. / 本仓只记录该原则，没有权限执行实现。

## AF-TOOL-002 — Untrusted content never becomes instruction / 不可信内容不得成为指令

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S02

**EN.** Web pages, documents, tool output, retrieved memory, and inter-agent messages are data. A control layer must prevent them from silently changing goals, permissions, destinations, or approval requirements.

**ZH.** 网页、文档、工具输出、检索记忆和智能体间消息都是数据。控制层必须阻止它们静默改变目标、权限、目标地址或审批要求。

**Scope and limits / 范围与局限:** The repository has no prompt/content isolation runtime; this remains a non-implemented requirement. / 本仓没有 Prompt/内容隔离运行时，该条仍是未实现要求。

## AF-TOOL-003 — Plans are inspectable state / 计划是可检查状态

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E4_PREPRINT`
- **Mapping / 映射:** `DESIGN_ANALOGY`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S15

**EN.** Externalized plans can make supervision, localized correction, and resumption easier than opaque internal planning. A plan remains a proposal and must not substitute for state observation or permission checks.

**ZH.** 外显计划比不透明内部规划更利于监督、局部修正和恢复执行，但计划仍是提案，不能替代状态观测和权限检查。

**Scope and limits / 范围与局限:** Plover evaluates GUI workflows; this repository does not implement that interface or a plan-state runtime. / Plover 评估 GUI 工作流，本仓没有实现对应界面或计划状态运行时。

## AF-TOOL-004 — Debugging is a closed loop / 调试是闭环

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E4_PREPRINT`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S14

**EN.** Useful observability connects detection, causal attribution, recovery, and rerun while preserving the original trajectory and intervention. Logging without attribution and replay is insufficient for long-horizon failures.

**ZH.** 有效可观测性应连接检测、因果归因、恢复和重跑，并保留原始轨迹与干预。只有日志而没有归因和回放，不足以处理长时程失败。

**Scope and limits / 范围与局限:** AgentDebugX is external and model-dependent; no corresponding debugging/replay loop exists locally. / AgentDebugX 属于外部实现且依赖所测模型；本仓没有对应调试/回放闭环。

## AF-TOOL-005 — Monitors are guarded components / 监控器自身也需要防护

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S04, S05, S07

**EN.** A monitor adds a control layer but has its own observation limits, attack surface, latency, thresholds, and error rates. High-impact actions need fail-closed behavior or human review where monitor confidence is insufficient.

**ZH.** 监控器增加了一层控制，但也具有观测边界、攻击面、延迟、阈值和错误率。高影响动作在监控置信不足时需要失败关闭或人工复核。

**Scope and limits / 范围与局限:** No runtime monitor or approval gate is implemented by Agent Foundations. / Agent Foundations 没有实现运行时监控器或审批门。

## AF-TOOL-006 — Side effects are idempotent and bounded / 副作用必须幂等且受限

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Mutating tools should expose dry-run or preview where practical, use idempotency keys, verify resolved targets, record before/after state, and provide a tested compensation or rollback path.

**ZH.** 变更型工具应在可行时提供预演，使用幂等键，核验解析后的目标，记录变更前后状态，并提供经过测试的补偿或回滚路径。

**Scope and limits / 范围与局限:** This is a proposed tool-runtime requirement. Agent Foundations contains no side-effect executor or compensation engine. / 这是候选工具运行时要求；本仓没有副作用执行器或补偿引擎。