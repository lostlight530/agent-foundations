# Tool System / 工具系统

## AF-TOOL-001 — Authority is explicit and per action / 权限按动作明确授予

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Tool availability is not authority. Each consequential action needs an authenticated actor, allowed operation, bounded target, validated arguments, least privilege, and an auditable result.

**ZH.** 工具可用不等于获得授权。每个有后果的动作都需要认证参与者、允许操作、受限目标、已验证参数、最小权限和可审计结果。

**Scope and limits / 范围与局限:** Authorization controls known interfaces; compromised dependencies and hidden side effects remain separate risks. / 授权只控制已知接口；依赖被攻陷和隐藏副作用属于独立风险。

## AF-TOOL-002 — Untrusted content never becomes instruction / 不可信内容不得成为指令

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S02

**EN.** Web pages, documents, tool output, retrieved memory, and inter-agent messages are data. A control layer must prevent them from silently changing goals, permissions, destinations, or approval requirements.

**ZH.** 网页、文档、工具输出、检索记忆和智能体间消息都是数据。控制层必须阻止它们静默改变目标、权限、目标地址或审批要求。

**Scope and limits / 范围与局限:** Classification and isolation reduce prompt-injection risk but require adversarial testing. / 分类和隔离可降低 Prompt 注入风险，但必须进行对抗测试。

## AF-TOOL-003 — Plans are inspectable state / 计划是可检查状态

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E4_PREPRINT`
- **Mapping / 映射:** `DESIGN_ANALOGY`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S15

**EN.** Externalized plans can make supervision, localized correction, and resumption easier than opaque internal planning. A plan remains a proposal and must not substitute for state observation or permission checks.

**ZH.** 外显计划比不透明内部规划更利于监督、局部修正和恢复执行，但计划仍是提案，不能替代状态观测和权限检查。

**Scope and limits / 范围与局限:** Plover evaluates GUI workflows; this repository does not implement that interface. / Plover 评估的是 GUI 工作流，本仓不实现该界面。

## AF-TOOL-004 — Debugging is a closed loop / 调试是闭环

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E4_PREPRINT`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S14

**EN.** Useful observability connects detection, causal attribution, recovery, and rerun while preserving the original trajectory and intervention. Logging without attribution and replay is insufficient for long-horizon failures.

**ZH.** 有效可观测性应连接检测、因果归因、恢复和重跑，并保留原始轨迹与干预。只有日志而没有归因和回放，不足以处理长时程失败。

**Scope and limits / 范围与局限:** AgentDebugX results are external and model-dependent. / AgentDebugX 结果属于外部实现并依赖所测模型。

## AF-TOOL-005 — Monitors are guarded components / 监控器自身也需要防护

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S04, S05, S07

**EN.** A monitor adds a control layer but has its own observation limits, attack surface, latency, thresholds, and error rates. High-impact actions need fail-closed behavior or human review where monitor confidence is insufficient.

**ZH.** 监控器增加了一层控制，但也具有观测边界、攻击面、延迟、阈值和错误率。高影响动作在监控置信不足时需要失败关闭或人工复核。

**Scope and limits / 范围与局限:** Human review also has capacity and consistency limits. / 人工评审同样存在容量和一致性限制。

## AF-TOOL-006 — Side effects are idempotent and bounded / 副作用必须幂等且受限

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Mutating tools should expose dry-run or preview where practical, use idempotency keys, verify resolved targets, record before/after state, and provide a tested compensation or rollback path.

**ZH.** 变更型工具应在可行时提供预演，使用幂等键，核验解析后的目标，记录变更前后状态，并提供经过测试的补偿或回滚路径。

**Scope and limits / 范围与局限:** Some physical or external actions are not fully reversible and require stronger pre-authorization. / 部分物理或外部动作无法完全回滚，因此需要更严格的事前授权。
