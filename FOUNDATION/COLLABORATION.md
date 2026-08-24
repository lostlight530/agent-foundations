# Collaboration System / 协作系统

## Repository realization boundary / 本仓实现边界

Agent Foundations does **not** implement a multi-agent collaboration runtime, inter-agent transport, consensus protocol, task arbiter, role router, or trajectory-capture service.

The claims below are research/evidence maps. `REFERENCE_ONLY` and `NOT_IMPLEMENTED` describe their local implementation state and must not be promoted by analogy, source prestige, or repeated discussion.

本仓没有实现多智能体协作运行时、Agent 间传输、共识协议、任务仲裁器、角色路由器或轨迹捕获服务。下列条目属于研究/证据映射，本地实现状态以每条 Claim 的明确字段为准。

## AF-COLLAB-001 — Topology is a tradeoff, not an ideology / 拓扑是权衡而非信条

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `COUNTEREVIDENCE`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S11

**EN.** Centralized, hierarchical, and decentralized coordination expose different failure, observability, latency, and consistency properties. CHMAS is a concrete counterexample to rejecting every central strategic component while retaining distributed tactical execution.

**ZH.** 中心化、分层和去中心化协作具有不同的故障、可观测性、延迟和一致性属性。CHMAS 是“保留分布式战术执行但不排除中心战略层”的具体反例。

**Scope and limits / 范围与局限:** CHMAS results belong to its MARL setting and assumptions, not general LLM teams. `STATIC_CHECKED` here is documentary/source review only. / CHMAS 结果属于其 MARL 设置和假设，不代表一般 LLM 团队；此处 `STATIC_CHECKED` 仅指文档/来源核对。

## AF-COLLAB-002 — Decentralization removes only specified single points / 去中心化只消除特定单点

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E4_PREPRINT`
- **Mapping / 映射:** `COUNTEREVIDENCE`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S12

**EN.** Removing a central dispatcher can remove one availability dependency, but semantic errors can still propagate through peer communication and topology. Resilience claims must name the failure model.

**ZH.** 移除中心调度器可以消除一个可用性依赖，但语义错误仍可能沿对等通信和拓扑传播。韧性声明必须明确故障模型。

**Scope and limits / 范围与局限:** HalluProp estimates risk; it does not prove prevention or an Agent Foundations resilience property. / HalluProp 估计风险，并不证明能够阻止故障，也不证明 Agent Foundations 具有对应韧性。

## AF-COLLAB-003 — Attribution requires preserved trajectories / 归因需要保留轨迹

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S13, S14

**EN.** Multi-agent failure localization needs ordered messages, tool calls, state changes, role assignments, and evaluator decisions. Final output alone is weak evidence of the responsible agent or earliest decisive step.

**ZH.** 多智能体故障定位需要有序消息、工具调用、状态变化、角色分配和评估器判断。只有最终输出，难以证明责任智能体或最早决定性错误步骤。

**Scope and limits / 范围与局限:** This repository does not implement trajectory capture or multi-agent attribution. / 本仓没有实现轨迹捕获或多智能体归因。

## AF-COLLAB-004 — Messages carry contracts and provenance / 消息携带契约与来源

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02

**EN.** Inter-agent messages should declare schema version, sender, intended recipient, task and correlation IDs, authority, evidence references, expiry, and integrity metadata. Receivers validate them as untrusted input.

**ZH.** 智能体间消息应声明 Schema 版本、发送者、预期接收者、任务与关联 ID、权限、证据引用、过期时间和完整性元数据。接收方必须按不可信输入进行验证。

**Scope and limits / 范围与局限:** This is a proposed message-contract requirement; no inter-agent message schema/transport is implemented here. / 这是候选消息契约要求；本仓没有实现 Agent 间消息 schema 或传输层。

## AF-COLLAB-005 — Consensus has typed subjects / 共识必须指明对象

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S10, S11, S12

**EN.** Agreement on parameters, replicated state, task ownership, evidence sufficiency, and factual truth are different consensus problems. A convergence result for one typed state must not be presented as agreement on another.

**ZH.** 参数、复制状态、任务归属、证据充分性和事实真伪是不同的共识问题。某类状态的收敛结果不能表述为另一类对象已经达成一致。

**Scope and limits / 范围与局限:** Agent Foundations has no consensus protocol; the claim only bounds how external convergence results may be interpreted. / Agent Foundations 没有共识协议；该条只约束如何解释外部收敛结果。
