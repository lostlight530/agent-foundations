# Agent Foundations — 中文专业研究导读

**当前解释校准：2026-11-15** · **源码基线：** `main@608bf59eb503effdf211aa2f9b448f24d3ede0dc` · **文档身份：** 当前专业导航，不是实验产物或历史周期记录

## 总论：本仓库究竟是什么

Agent Foundations 是用于研究 **Agent Systems 理论、证据契约和架构判断**的双语知识基础，并非已部署的确定性 Agent、工具权限服务、跨会话记忆引擎或分布式协作运行时

在上述源码基线下，`FOUNDATION/` 四领域共有 **23 条规范性 Claim**：Architecture 6、Memory 5、Tools 6、Collaboration 6；`FOUNDATION/SOURCES.md` 登记 **S01–S67 共 67 个连续来源 ID**，这只是文档来源身份的清单，**不是 67 篇论文被独立复现**，历史研究正文存在已披露的 `S63` 标签冲突，检索时必须使用论文题目、arXiv ID、版本和对应出处消歧，不能仅凭编号继承论证

当前解释顺序：[Verified Core 索引](../../FOUNDATION/INDEX.md) → [证据语义](../../FOUNDATION/EVIDENCE.md)、[来源登记](../../FOUNDATION/SOURCES.md)、[溯源契约](../../FOUNDATION/PROVENANCE.md)、[评审语义](../../FOUNDATION/REVIEW.md) → 四领域原生 Claim 文档，外部论文、数学公式、示例伪代码和既有类比都不能自行升级为 `IMPLEMENTED`、`REPRODUCED` 或通用安全证明

## 分论：四个领域及对应原生知识

| 专业理论长文 | 当前规范性 Claim | 研究对象与实现边界 |
| --- | --- | --- |
| [架构原则与梯度熵](./Architecture_Principles.md) | [Architecture](../../FOUNDATION/ARCHITECTURE.md) · `AF-ARCH-001..006` | 完整 Model + Harness + Tools + Evaluator 的系统身份、定理假设、可比性；**没有通用 Agent 收敛或安全运行时证明** |
| [记忆与表征学习](./Memory_System.md) | [Memory](../../FOUNDATION/MEMORY.md) · `AF-MEM-001..005` | 来源、检索、压缩保真、授权角色、保留与纠错；**没有已实现的跨会话记忆服务** |
| [工具与策略优化](./Tool_System.md) | [Tools](../../FOUNDATION/TOOLS.md) · `AF-TOOL-001..006` | 工具可用性、动作授权、调用、真实副作用、未知结果及恢复；**没有本仓工具执行／权限代理** |
| [多 Agent 协作与拓扑](./Collaboration_System.md) | [Collaboration](../../FOUNDATION/COLLABORATION.md) · `AF-COLLAB-001..006` | 通信拓扑、消息一致性、复制状态收敛与事实正确性的分离；**没有本仓协作运行时** |

## 阅读方法与证据边界

四篇专业长文保留过去的研究构思、公式、论文记录、类比与伪代码，是可继续核查、修正和扩展的研究资产，历史段落使用的「绝对安全」「必定收敛」「永不丢失记忆」「零工具风险」等，不构成当前已经实现的事实或普适定理

每个重要命题都应分别说明 **Claim State、Evidence Level、Mapping State、Implementation State、Validation State**，以及来源论文的精确版本、适用假设、实现路径、反例和实际结果，论文定理的对象不自动等同完整 Agent 系统；来源登记、静态源码、测试定义和实际运行也不是同一种证据

**本次校准边界：** 已对照仓库实现与 Claim 文件；未重新证明外部论文全部公式，状态为 `NOT_REVERIFIED`；未执行新增 Agent 实验，状态为 `NOT_EXECUTED`，历史正文和原有时间点记录保持独立，不由当前说明追溯改写
