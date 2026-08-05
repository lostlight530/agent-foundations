# Collaboration System / 协作系统

## AF-COLLAB-001 — Topology is a tradeoff, not an ideology / 拓扑是权衡而非信条

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `COUNTEREVIDENCE`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S11

**EN.** Centralized, hierarchical, and decentralized coordination expose different failure, observability, latency, and consistency properties. CHMAS is a concrete counterexample to rejecting every central strategic component while retaining distributed tactical execution.

**ZH.** 中心化、分层和去中心化协作具有不同的故障、可观测性、延迟和一致性属性。CHMAS 是“保留分布式战术执行但不排除中心战略层”的具体反例。

**Scope and limits / 范围与局限:** CHMAS results belong to its MARL setting and assumptions, not general LLM teams. / CHMAS 结果属于其 MARL 设置和假设，不代表一般 LLM 团队。

## AF-COLLAB-002 — Decentralization removes only specified single points / 去中心化只消除特定单点

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E4_PREPRINT`
- **Mapping / 映射:** `COUNTEREVIDENCE`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S12

**EN.** Removing a central dispatcher can remove one availability dependency, but semantic errors can still propagate through peer communication and topology. Resilience claims must name the failure model.

**ZH.** 移除中心调度器可以消除一个可用性依赖，但语义错误仍可能沿对等通信和拓扑传播。韧性声明必须明确故障模型。

**Scope and limits / 范围与局限:** HalluProp estimates risk; it does not prove prevention. / HalluProp 估计风险，并不证明能够阻止故障。

## AF-COLLAB-003 — Attribution requires preserved trajectories / 归因需要保留轨迹

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S13, S14

**EN.** Multi-agent failure localization needs ordered messages, tool calls, state changes, role assignments, and evaluator decisions. Final output alone is weak evidence of the responsible agent or earliest decisive step.

**ZH.** 多智能体故障定位需要有序消息、工具调用、状态变化、角色分配和评估器判断。只有最终输出，难以证明责任智能体或最早决定性错误步骤。

**Scope and limits / 范围与局限:** LLM-based judges introduce their own uncertainty and require calibration. / 基于 LLM 的评判器会引入新的不确定性，需要校准。

## AF-COLLAB-004 — Messages carry contracts and provenance / 消息携带契约与来源

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Inter-agent messages should declare schema version, sender, intended recipient, task and correlation IDs, authority, evidence references, expiry, and integrity metadata. Receivers validate them as untrusted input.

**ZH.** 智能体间消息应声明 Schema 版本、发送者、预期接收者、任务与关联 ID、权限、证据引用、过期时间和完整性元数据。接收方必须按不可信输入进行验证。

**Scope and limits / 范围与局限:** Integrity metadata does not establish the truth of message content. / 完整性元数据不能证明消息内容为真。

## AF-COLLAB-005 — Consensus has typed subjects / 共识必须指明对象

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S10, S11, S12

**EN.** Agreement on parameters, replicated state, task ownership, evidence sufficiency, and factual truth are different consensus problems. A convergence result for one typed state must not be presented as agreement on another.

**ZH.** 参数、复制状态、任务归属、证据充分性和事实真伪是不同的共识问题。某类状态的收敛结果不能表述为另一类对象已经达成一致。

**Scope and limits / 范围与局限:** Each protocol needs a threat model, quorum rule, termination condition, and conflict policy. / 每个协议都需要威胁模型、法定人数规则、终止条件和冲突策略。
