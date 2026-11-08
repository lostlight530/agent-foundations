# DeerFlow 研究版｜从 Research Flow 到 Super Agent Harness

**Research identity:** DeerFlow versioned public-architecture edition

## 核心研究命题

DeerFlow 研究线关注一次明确的架构代际变化

固定在提交 [`284e0d537d1a5115704e71ed741b5ce37bf1fbb9`](https://github.com/bytedance/deer-flow/blob/284e0d537d1a5115704e71ed741b5ce37bf1fbb9/README.md) 的官方 README 将 2.0 定义为 Super Agent Harness，并明确说明 2.0 是 ground-up rewrite，与 v1 不共享代码

因此研究不能把 v1 的 Deep Research Flow 叙事直接当作 v2 实现证据，而要研究“面向研究任务的流程系统”如何转成“面向长期通用任务的 Agent 运行底座”

固定 README 的 Git blob 为 `4340b4d1dec1a41a5a5ac850aacbf742ab97d0ec`，本研究于 2026-11-08 复核

## 公开互动与来源边界

GitHub 插件在 `bytedance/deer-flow` 中检索 `lostlight530` 的 Issue、Comment 和 PR，当前搜索面未发现可归属的公开对象

这表示 `SEARCH_NO_MATCH`，不表示“从未参与”，也不允许把线下活动、私信或个人通信转换成公开贡献

DeerFlow 研究对象因此采用与 Astron、Nexent 不同的证据结构

- Astron 与 Nexent 以公开互动演进为主
- DeerFlow 以固定官方架构版本与代际边界为主
- 后续若发现可验证的公开 Discussion、Comment 或 PR，应作为新来源记录追加，不能倒填为当前已知事实

## 从 v1 研究流到 v2 Harness 的研究转换

| 维度 | 早期 Research Flow 问题 | 2.0 Super Agent Harness 问题 | WorkflowHub 转换 |
|---|---|---|---|
| 任务范围 | 深度研究流程 | 长时通用任务与多类执行 | 记录任务类型、完成条件与中断边界 |
| 角色结构 | 研究流程中的分工 | 可委派 Sub-agents | 记录委派图、角色身份与结果回收 |
| 状态 | 单次研究上下文 | Session、Memory 与长期连续性 | 记录状态版本、恢复点与来源 |
| 执行环境 | 工具调用与检索 | Sandbox、Skills、Tools、Gateway | 记录权限、环境、能力来源与副作用 |
| 可靠性 | 答案与引用质量 | 运行时恢复、隔离、控制与可观察性 | 输出事件轨迹、故障分类与验证回执 |
| 版本关系 | v1 研究系统 | v2 ground-up rewrite | 两代资料分别固定，不推断代码连续性 |

## 研究问题

1. Harness 与 Sub-agent 推理组件分别承担什么责任
2. Memory、Context、Skills、Sandbox、Gateway 与 Tool execution 的生命周期如何区分
3. 长时运行中的 Session 连续性、恢复与证据保存在哪里发生
4. 哪些结论来自固定官方文档，哪些必须通过真实运行轨迹才能成立
5. ground-up rewrite 后，哪些研究概念可以比较，哪些实现事实必须完全分账

## WorkflowHub 研究对象设计

**输入**

- 固定提交与 Git blob 的 DeerFlow 官方 README
- 后续允许加入的固定官方文档、Release 与架构说明
- v1/v2 概念注册表
- Harness 组件与责任分类规则
- 若实际执行则加入脱敏运行轨迹和测试夹具

**步骤**

1. 固定来源版本并提取明确架构声明
2. 区分 v1 叙事、v2 声明和跨代研究假设
3. 映射 Sub-agent、Memory、Context、Skill、Sandbox、Gateway 与 Tool
4. 构造责任、状态、权限和恢复边界矩阵
5. 将文档证据与未来运行证据分层输出
6. 对未验证互动和未执行结论保持 Unknown

**输出**

- v1/v2 代际边界表
- Super Agent Harness 组件图
- 责任与信任边界矩阵
- 状态、恢复与证据生命周期规范
- 固定来源清单
- 文档结论与运行结论分层报告

## 研究结论

`Research Flow → version boundary → Super Agent Harness → long-horizon runtime governance`

DeerFlow 的研究价值在于展示 Agent 系统从特定研究流程向通用运行底座转型时，研究对象也必须从“流程能否完成”扩展到“委派、记忆、隔离、能力、状态与恢复如何被治理”

当前可发布的结论限于固定官方架构来源，不宣称存在已验证的个人公开贡献

**Working title:** *DeerFlow 2.0: From Research Flow to Evidence-Grounded Super Agent Harness Boundaries*

