# Nexent 研究版｜从动态语义编排到 Harness 与 Skill Control Plane

**Research identity:** Nexent / ModelEngine public-interaction edition

## 核心研究命题

Nexent 研究线从 RailSmart 实际案例开始，先触及 MCP 接入体验，再因维护者纠偏改变了对 Workflow 的理解，随后连续发展出 Agent/Skill 分离、Harness Engineering、Prompt Contract 与 Skill Ecosystem Control Plane

核心不是“再画一张工作流图”，而是研究动态语义编排中计划、权限、工具、状态、失败、复用与治理如何被观察和控制

## 全部公开 Discussion、Comment 与 PR 精华

| 日期 | 公开对象 | 提取的研究命题 | 回复或状态 | 转换后的研究作用 |
|---|---|---|---|---|
| 2025-11-22 | [ModelEngine org #14](https://github.com/orgs/ModelEngine-Group/discussions/14) | RailSmart 的组织级竞赛入口 | Closed，0 comments | 保留为同一案例的组织级身份，不重复计算成第二套实现 |
| 2025-11-23 | [Nexent #1816](https://github.com/ModelEngine-Group/nexent/discussions/1816) | DeepSeek-V3、MCP 与多 Agent 铁路出行决策案例，附 JSON 与 DOCX | 2025-12-15 geruihappy-creator 留下正向反馈 | 作为实践基线，反馈不等于正式验收 |
| 2025-12-02 | [Nexent #1982](https://github.com/ModelEngine-Group/nexent/discussions/1982) | 预部署 MCP Server 一键导入与同步，暴露能力复用和接入摩擦 | 2025-12-03 YehongPan 说明当时正在推进 Streamable HTTP，并计划导入工具；作者随后致谢 | 将产品摩擦转换为能力发现、同步、版本和部署合同问题，路线图陈述不写成已交付 |
| 2025-12-10 | [Nexent #2056](https://github.com/ModelEngine-Group/nexent/discussions/2056) | 提议 MCP 插件机制、能力市场与语义工作流可视化 | 2025-12-12 loveTsong 纠正：Nexent 的执行由上下文动态生成语义编排，并非预声明静态 DAG | 将研究从“展示固定图”改为“记录动态计划、决策依据与可回放轨迹” |
| 2025-12-31 | [Nexent #2179](https://github.com/ModelEngine-Group/nexent/discussions/2179) | 协作 Agent 不等于 Skill，前者承担独立认知与任务分解，后者承载稳定复用知识 | 作者概念命题，未写成官方规范 | 建立 Agent、Sub-agent、Skill、Tool 的责任分层 |
| 2026-04-04 | [Nexent #2757](https://github.com/ModelEngine-Group/nexent/discussions/2757) | Harness Engineering 将权限、记忆、失败恢复与审计变成平台责任 | 研究问题，不宣称现有实现全部满足 | 形成运行时治理与验收维度 |
| 2026-05-31 | [Nexent #3148](https://github.com/ModelEngine-Group/nexent/discussions/3148) | Prompt 从自由文本演进为意图声明和能力边界合同 | 作者解释性假设 | 将 Prompt 与运行时角色分配、工具许可和输出合同连接 |
| 2026-08-02 | [Nexent #3568](https://github.com/ModelEngine-Group/nexent/discussions/3568) | Skill 类型分化为说明、CLI、脚本、平台工具、安装与发现对象 | 作者架构提案 | 形成来源、权限、安装、执行、升级与撤销的 Skill 控制面研究 |
| 2025-11-23 | [PR #1825](https://github.com/ModelEngine-Group/nexent/pull/1825) | 社区纪念墙内容贡献 | Closed without merge，head `1e344976eaf476f993aefe9516b4d4605c3de2e0` | 证明实际 Git 互动，不构成运行时代码贡献 |
| 2025-11-23 | [PR #1826](https://github.com/ModelEngine-Group/nexent/pull/1826) | 社区纪念墙内容修订 | Closed without merge，head `fe76a3a142a03529fefdef02389a4aa646da4f23` | 与 #1825 分开保留，不把关闭 PR 写成已进入主干 |
| 2025-11-24 | [PR #1838](https://github.com/ModelEngine-Group/nexent/pull/1838) | 社区纪念墙内容贡献 | Merged 2025-11-25，merge commit `7b314fc6bed6d57763d906800c8de52a4a72bc67` | 构成已合并社区数据贡献，仍不等于核心编排实现被采用 |

## 演进结构

### 阶段一｜RailSmart 实践基线

组织 Discussion 与仓库 Discussion 指向同一 RailSmart 案例，研究中保留两个 GitHub 身份，但只认定一套实践对象

### 阶段二｜MCP 接入与能力复用

`#1982` 将一键导入和同步问题显式化，背后涉及 MCP Server 身份、配置、版本、传输、部署状态与平台发现能力

### 阶段三｜维护者纠偏改变研究模型

`#2056` 是整条研究线最关键的外部修正

原假设倾向于把 Nexent 表达为可预声明和可视化的工作流，维护者指出其核心是上下文驱动的动态语义编排，因此研究对象从静态 DAG 转为以下可观察问题

- 运行时为何选择某个工具或 Agent
- 动态计划何时生成、修改和终止
- 决策、输入、状态与工具结果如何关联
- 同一输入在不同上下文下如何比较
- 如何回放、审计和解释失败

### 阶段四｜Agent 与 Skill 的责任分离

`#2179` 将独立认知主体与稳定执行知识拆开，避免用 Skill 同时代表推理者、脚本、说明书和工具包

### 阶段五｜Harness 成为产品控制层

`#2757` 将权限、状态、记忆、恢复、预算和审计放入 Harness，而不是把可靠性全部推给模型

### 阶段六｜Prompt Contract 与 Skill Control Plane

`#3148` 与 `#3568` 将意图合同和异构 Skill 治理连接起来，形成来源、能力、许可、执行与生命周期控制面

## WorkflowHub 研究对象设计

**研究问题**

怎样从公开互动重建 Nexent 研究思想的演进，并为动态语义编排建立可观察、可比较和可治理的研究合同

**输入**

- 组织与仓库 Discussions
- 独立 Comment 与维护者纠偏
- 三个 PR 的状态和提交身份
- 动态编排事件模型
- Agent、Skill、MCP、Tool、Harness 类型注册表

**步骤**

1. 规范化同一 RailSmart 案例的多个 GitHub 身份
2. 建立 Discussion、Comment、PR 与角色关系
3. 提取“原命题 → 维护者纠偏 → 修正研究问题”链
4. 将七个仓库 Discussion 映射为连续概念阶段
5. 构造动态计划、工具选择、授权、状态与失败事件模式
6. 输出时间线、纠偏矩阵、控制面模型与未知项

**输出**

- Nexent 公开互动时间线
- RailSmart 单案例身份映射
- MCP 接入与动态编排问题图
- 维护者纠偏前后模型差异
- Agent/Skill/MCP/Tool/Harness 责任矩阵
- Skill Control Plane 研究规范
- 来源、PR 状态与限制清单

## 研究结论

`RailSmart → MCP 接入 → 动态语义编排纠偏 → Agent/Skill 分层 → Harness → Prompt Contract → Skill Control Plane`

Nexent 研究线的关键进步来自公开技术纠偏，动态 Agent 平台的 WorkflowHub 研究对象不应只保存静态流程图，还应保存决策轨迹、工具调用、权限、状态变化、失败恢复与来源关系

**Working title:** *Nexent: From Dynamic Semantic Orchestration to Harness Contracts and Skill Ecosystem Governance*

