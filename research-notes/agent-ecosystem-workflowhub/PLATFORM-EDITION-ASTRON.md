# Astron 研究版｜从 AgentFlow 实践到可信工作流合同

**Research identity:** Astron Agent / iFLYTEK ecosystem public-interaction edition

## 核心研究命题

Astron 研究线不是“一个简历 Agent 的介绍”，而是一条从具体 AgentFlow 实践逐步外推到可信执行、结构合同、系统责任、生态维护与长期记忆的公开研究轨迹

它提出的关键问题是：当 Agent 工作流从演示进入长期真实任务后，哪些能力必须由可检查结构、可恢复状态、授权边界、记忆版本和维护责任共同承担

## 全部公开 Discussion 与 Comment 精华

| 日期 | 公开对象 | 提取的研究命题 | 回复或修正 | 转换后的研究作用 |
|---|---|---|---|---|
| 2026-01-08 | [Astron #824](https://github.com/iflytek/astron-agent/discussions/824) | ResumeZhiYoutong 把 OCR/PDF、多模型协作、双模式分支、多轮状态与结构化建议组合成 AgentFlow 案例 | 2026-01-10 FenjuFu 邀请整理 Awesome Astron Workflow 文章；2026-01-11 作者补充事件驱动输入与 Master–Worker 架构；同日另有一条无可见正文的作者评论 | 作为实践基线，区分“作者描述的系统设计”与“已复现实验结果” |
| 2026-04-04 | [Astron #1138](https://github.com/iflytek/astron-agent/discussions/1138) | Entrustability 将问题从模型会不会做，推进到真实任务能否稳定托付 | 2026-10-14 FenjuFu 将抽象问题落到三类可复现实验：写副作用重试幂等性、审批与恢复输入一致性、记忆版本与来源 | 形成可信执行评测框架，而不是停留在概念口号 |
| 2026-05-31 | [Astron #1359](https://github.com/iflytek/astron-agent/discussions/1359) | Workflow 是角色、步骤、工具、错误与边界的显式合同 | 当前账本未纳入公开维护者回复 | 形成结构合同层，要求工作流可检查而非仅依赖 Prompt |
| 2026-05-31 | [Astron #1360](https://github.com/iflytek/astron-agent/discussions/1360) | 合同之后仍有连续性、控制权、责任与长期运行问题 | 当前账本未纳入公开维护者回复 | 把研究从单次执行扩展到生命周期治理 |
| 2026-07-25 | [iFLYTEK org #4](https://github.com/orgs/iflytek/discussions/4) | 社区 Demo、Zeabur 部署、官方服务、成本、入口与维护责任不可混同 | 该对象是用户评论，不构成官方服务承诺 | 加入服务边界与社区可持续性维度 |
| 2026-08-01 | [iFLYTEK org #1](https://github.com/orgs/iflytek/discussions/1) | 两条中英文评论把 Astron Agent、Skills、RPA 与 MemFlywheel 组织成生态导航 | 同线程两条评论，不计成两个独立 Discussion | 形成平台生态层次与对象关系图 |
| 2026-09-20 | [MemFlywheel #72 用户评论](https://github.com/iflytek/memflywheel/issues/72#issuecomment-5750056853) | 将记忆系统拆成 host、adapter、SDK、core 与 data，并关联 extraction、recall、dream、skill | [FenjuFu 2026-09-27 回复](https://github.com/iflytek/memflywheel/issues/72#issuecomment-5857588519)确认解释与 `architecture.md` 一致 | 将个人架构理解升级为有维护者校准的生态结构证据，但不等于技术方案被采纳 |
| 2026-09-20 | [MemFlywheel #18 用户评论](https://github.com/iflytek/memflywheel/issues/18#issuecomment-5750057816) | 提出跨环境、文件原生、可携带的长期记忆与经验循环实践 | [FenjuFu 2026-09-27 回复](https://github.com/iflytek/memflywheel/issues/18#issuecomment-5857589250)感谢实际使用经验 | 将记忆放回长期 Agent 连续性问题，回复仅构成致谢与实践确认 |

## 演进结构

### 阶段一｜具体 AgentFlow 实践

`#824` 给出真实任务中的输入分支、OCR、模型协作、状态和结构化输出，为后续抽象提供可指认的工程起点

### 阶段二｜从 Capability 到 Entrustability

`#1138` 不再问模型能否生成答案，而是问系统能否在重试、审批、恢复和记忆变化中保持一致且可追溯

维护者回复让研究得到三个可检验入口

1. 有副作用的写操作在重试时是否幂等
2. 人工批准前后的输入是否保持同一身份
3. 恢复运行是否携带明确的记忆版本与来源

### 阶段三｜Workflow 作为结构合同

`#1359` 把角色、工具、错误和边界从隐含 Prompt 中拆出，使执行结构可以审查、测试和替换

### 阶段四｜合同之后的系统责任

`#1360` 说明合同并不自动解决状态连续性、长期所有权、故障处置和维护责任，可信系统还需要生命周期层

### 阶段五｜生态维护与文件原生记忆

组织 Discussion 与 MemFlywheel 评论把单仓工作流扩展为生态研究

- 社区 Demo 与正式服务具有不同承诺
- 工具入口、部署模板与持续维护属于责任结构
- 长期记忆需要版本、来源、可携带性和跨环境边界

## WorkflowHub 研究对象设计

**研究问题**

怎样把 AgentFlow 的公开工程轨迹转换成可复现的可信执行评测，并保留“作者命题、维护者反馈、已实现事实、未知项”之间的差异

**输入**

- Astron Discussions 与独立回复清单
- iFLYTEK 组织 Discussion 评论
- MemFlywheel Issue 评论及维护者回应
- 主题注册表与互动分类规则
- 三类最小可信执行测试夹具

**步骤**

1. 规范化线程、评论、作者、时间与回复边
2. 将内容归入实践、Entrustability、合同、责任、生态、记忆六类主题
3. 对邀请、致谢、确认、复现实验建议分别分类
4. 构造副作用重试、审批恢复、记忆版本三个受控场景
5. 输出命题、反馈、反证、未知项与运行回执

**输出**

- 公开互动时间线
- 命题与维护者反馈矩阵
- Astron 可信执行概念图
- 三类受控测试规范
- 来源与限制清单
- 可继续扩展为 RO-Crate 的研究包

## 研究结论

`实践结构 → 可信执行 → 工作流合同 → 生命周期责任 → 生态与记忆连续性`

Astron 研究线的价值不在于证明某个平台“最好”，而在于从真实 AgentFlow 出发形成可检验路径，维护者互动的最大作用是把抽象可信性问题压缩为可复现实验，而不是为全部后续理论背书

**Working title:** *Astron Agent: From AgentFlow Practice to Entrustable Workflow Contracts and Lifecycle Responsibility*

