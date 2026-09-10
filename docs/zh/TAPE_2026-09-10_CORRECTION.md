# TAPE 证据校正 — 2026-09-10

状态: `CURRENT_INTERPRETATION_CORRECTION`
仓库: `lostlight530/agent-foundations`
系统容器: `Collaboration System`
规范来源: `S40`
来源身份: `arXiv:2312.15667v3`
受影响的历史生成块: PR #155 于 2026-09-08 添加的 `AF-COLLAB-003`
相关较早编织: 2026-09-06 PR #151

本文件采用前向校正方式。它不删除、不改写历史生成块，也不改写其 PR 历史。

## 当前来源支持的解释

经核验的 TAPE 论文支持以下有限结论：

- TAPE 为协作式多智能体策略梯度学习引入 Agent Topology。拓扑决定策略梯度学习时纳入哪些其他智能体的 utility，并通过 coalition utility 表达局部协作，而不是要求每次更新都使用全体智能体的全局 utility。
- 论文提出 stochastic TAPE 与 deterministic TAPE 两种变体。
- 对 stochastic TAPE，已核验的 policy-improvement theorem 以 tabular policy expressions 和足够小的更新条件为前提，并在这些条件下得到单调目标改进：更新后的策略在该定理所定义的目标上不差于更新前策略。
- 论文研究 Barabási–Albert、Watts–Strogatz 和 Erdős–Rényi 三类图模型。作者在多数实验中采用 Erdős–Rényi，是因为其研究中该模型产生了更丰富的拓扑变化。
- 已核验的第二项理论结果把 stochastic TAPE 相对 DOP 的参数更新方差与 Erdős–Rényi 连接概率 `p` 联系起来；更稠密的拓扑可以提高更新多样性，同时也可能重新增加 centralized-decentralized mismatch 压力。

## 2026-09-08 生成块中不得继续作为当前来源证据的声明

以下表述除非未来有新的独立重认证，否则不得继续作为 TAPE 来源已证明的事实复用：

- `Erdős–Rényi 拓扑是 policy-improvement theorem 的核心或普遍假设。` 已核验论文允许任意 Agent Topology，并研究多类图；Erdős–Rényi 只是其中一个分析和实验模型。
- `收敛速率受通信图 algebraic connectivity 或其他谱性质约束。` 本次核验未在来源正文中找到该声明。
- `TAPE 收敛到真实目标的 stationary point。` 这不是本次核验到的定理表述；当前核验的是带明确条件的 policy-improvement 结果。
- `每次策略更新都通过生成块中的邻居消息 m_N 条件化 local-Q 公式实现。` 已核验论文采用 coalition utility / topology 表述；生成块中的 message-conditioned 公式未被认证为论文公式。
- 初学者类比中“只要连接充分就由数学保证整个组织达到全局最优结果”的说法。该外推超出了论文定理边界。

## 五轴状态

- Claim State: `SUPPORTED_WITH_SCOPE_CORRECTION`
- Evidence Level: `E4_PREPRINT / PEER-REVIEWED_PUBLICATION_IDENTITY_PRESENT`
- Mapping State: `DESIGN_ANALOGY`
- Implementation State: `REFERENCE_ONLY`
- Validation State: `NOT_TESTED`
- 本次公式/定理重认证: `PARTIAL — 仅限上面列出的定理与结果表面`

AAAI 发表身份的存在不会自动把论文定理转化为仓库实现或验证结果。

## 已核验来源表面

- arXiv: https://arxiv.org/abs/2312.15667
- AAAI publication: https://ojs.aaai.org/index.php/AAAI/article/view/29699

## 后续 Weekly 级联要求

后续 Weekly document cascade 可以把本校正编织回规范 Collaboration System 文档。编织时必须保留历史 source-revisit provenance，并且不得把 2026-09-08 对 S40 的重复访问计为新的独立支持。
