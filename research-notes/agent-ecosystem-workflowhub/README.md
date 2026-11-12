# Agent 开放生态互动研究 → WorkflowHub 三研究对象

**Status:** `RESEARCH_SYNTHESIS_CANDIDATE` · source cutoff 2026-11-08 · public GitHub evidence only · not an official platform statement

## 研究对象

这不是一次仓库审计，也不是把 GitHub 链接机械搬到 WorkflowHub

本研究把 `lostlight530` 在 Astron、Nexent 与 DeerFlow 相关公开空间中的 Discussion、Comment、维护者回复、PR 和官方架构材料，转换成三个可独立发布、可继续版本化的 WorkflowHub 研究对象

1. **Astron edition** — 从 AgentFlow 实践，经由 Entrustability、Workflow Contract、系统责任、社区维护与文件原生记忆，形成可信 Agent 工作流研究
2. **Nexent edition** — 从 RailSmart 实践，经由 MCP 接入、动态语义编排纠偏、Agent/Skill 分离、Harness、Prompt Contract 与 Skill Control Plane，形成动态编排治理研究
3. **DeerFlow edition** — 从 Research Flow 到 2.0 Super Agent Harness，研究 Sub-agent、Memory、Sandbox、Skills、Context 与 Gateway 如何构成通用 Agent 运行底座

三条研究线共享证据转换方法，但不互相冒充版本关系，也不把维护者回复、官方文档或个人参与解释成平台背书

## 已整理的公开对象

| 研究线 | GitHub 原始对象 | 当前证据结构 | 研究主轴 |
|---|---:|---|---|
| Astron / iFLYTEK ecosystem | 4 个 Astron Discussions、2 个组织 Discussions、2 个 MemFlywheel Issues | 14 条规范记录，组织 Discussion #1 内含两条独立用户评论 | 实践 → 可信执行 → 合同 → 责任 → 生态维护与记忆 |
| Nexent / ModelEngine | 1 个组织 Discussion、7 个仓库 Discussions、3 个 PR | 15 条规范记录 | 案例 → MCP → 动态编排纠偏 → Agent/Skill → Harness → Contract → Control Plane |
| DeerFlow | 固定提交与 Git blob 的官方 2.0 README | 1 条固定架构记录，公开互动层待继续补齐 | Research Flow → Super Agent Harness → 通用运行底座 |

账本目前共 30 条规范记录，其中一个 Astron 聚合记录明确表示两条同线程评论，因此“账本记录数”不能替代“GitHub 对象数”

## 从公开互动到研究对象

```text
GitHub Discussion / Comment / PR / pinned official source
        ↓
对象身份、作者、日期、回复关系与状态
        ↓
实践命题、维护者反馈、技术纠偏、架构代际与未解决问题
        ↓
平台内时间演进图与跨平台可比较研究维度
        ↓
Astron edition / Nexent edition / DeerFlow edition
```

研究转换保留四种不同事实

- **提出了什么** — 用户的案例、概念或工程建议
- **平台如何回应** — 邀请、感谢、路线图说明、技术纠偏或可复现实验建议
- **什么真正进入代码或官方材料** — PR 是否合并、合并内容属于什么、固定文档明确声明什么
- **什么仍然未知** — 未执行、未冻结、未由官方确认或无法从公开材料复现的部分

## 三研究对象的共同贡献

- 把 Agent “能力”问题转成可检查的执行合同、授权、状态、恢复与证据问题
- 把显式 AgentFlow、动态语义编排和通用 Super Agent Harness 区分开
- 把 Agent、Sub-agent、Skill、MCP、Tool、Sandbox、Memory 与 Harness 分成不同责任对象
- 把开放社区互动和官方架构演进转换成可追踪研究，而不是宣传性背书
- 为 WorkflowHub 形成可继续增加执行器、RO-Crate、测试夹具和版本说明的三对象结构

## 文件

- [Astron 研究版](./PLATFORM-EDITION-ASTRON.md)
- [Nexent 研究版](./PLATFORM-EDITION-NEXENT.md)
- [DeerFlow 研究版](./PLATFORM-EDITION-DEERFLOW.md)
- [Astron WorkflowHub 填写资料](./WORKFLOWHUB-ASTRON.md)
- [Nexent WorkflowHub 填写资料](./WORKFLOWHUB-NEXENT.md)
- [DeerFlow WorkflowHub 填写资料](./WORKFLOWHUB-DEERFLOW.md)
- [机器可读互动账本](./evidence-ledger.json)
- [研究转换与发布合同](./PROTOCOL.md)

## 边界

- 研究内容来自公开 GitHub 页面，不包含微信、私信、活动现场或其他未公开通信
- Discussion 与 Comment 是研究输入，不自动等于被平台采纳的产品需求
- Nexent #1838 是已合并的社区纪念墙数据贡献，不是核心编排代码贡献
- DeerFlow 当前以固定官方架构源为主，不能把未确认的个人互动写成公开贡献
- 当前产物是完整研究语义与 WorkflowHub 元数据候选，不宣称 WorkflowHub 已执行代码、冻结版本或签发 DOI
- 后续若加入可执行处理器，应在不改写本研究历史的前提下增加冻结输入、测试和运行回执

