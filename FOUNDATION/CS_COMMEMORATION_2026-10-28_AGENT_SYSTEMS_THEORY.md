# agent-foundations 仓库纪念｜2026-10-28｜CS：智能体系统理论与架构证据
# Repository Commemoration · 2026-10-28 · Computer Science: Agent Systems Theory, Architecture, and Evidence

> **Identity / 记录身份：** Independent bilingual commemorative disciplinary study · 独立新增的中英双语学科研究纪念；static inspection of repository-native scripts and research documents / 基于原生脚本与研究文档的静态核查；not a historical rewrite, runtime execution report, or certification / 不改写历史、不声称执行或认证。
>
> **CS2023 alignment / 学科坐标：** AI (Agents and Cognitive Systems); SE (Software Architecture); DM; SEC. These are scholarly comparisons, not endorsements or exact implementation equivalences / 研究分类而非外部机构背书或实现等价。

## 1. 专业归属：这是 CS 的哪一类？ / Disciplinary Position

**中文** — 这是复杂智能体系统的**理论与设计论证层**。AI 不是只有语言模型：完整的 Agent 系统还包含记忆、工具、协作、指令、权限、预算、环境与评价。CS 的系统架构研究关注各部分如何组合、哪些要求能成立，以及边界失败时如何解释；本仓使用可标识的 Claim 与来源关系把这些问题变成可公开质询的知识对象。它不以一个可运行的通用 Agent 自居。

**English** — This repository is the **theory and design-argument layer for complex agent systems**. In computer science, an agent is not merely a language model: tools, memory, authorization, collaborators, environment, budgets, control loops, and evaluation belong to the configured system boundary. The repository makes architectural propositions accountable by attaching claim identity, source, mapping, implementation status, and validation status. It does not present itself as a deployed general-purpose agent runtime.

## 2. 仓库自身如何体现？ / Repository-native Architecture and Evidence

**中文** — `FOUNDATION/ARCHITECTURE.md` 讨论系统边界、确定性外壳与随机组件、证明适用域以及可重建发布；`MEMORY.md` 讨论摄取、检索、压缩、保留与纠错；`TOOLS.md` 讨论逐行动授权、不可信输入、恢复和幂等性；`COLLABORATION.md` 讨论多 Agent 拓扑与失败传播。`EVIDENCE.md`、`SOURCES.md`、`PROVENANCE.md` 与 `claim.schema.json` 把 Claim、来源身份、实现和验证分开；`validate.py` 和 `arxiv_probe.py` 是**结构及来源辅助程序**，不是定理证明器。`FOUNDATION/INDEX.md` 记录当前原生知识入口。

**English** — The native subject corpus consists of `FOUNDATION/ARCHITECTURE.md` (whole-system boundaries, deterministic shell, theorem scope, reconstructable release evidence), `MEMORY.md` (retrieval, compaction, retention, correction), `TOOLS.md` (per-action authority, untrusted inputs, idempotency, recovery), and `COLLABORATION.md` (coordination topology and failure propagation). `EVIDENCE.md`, `SOURCES.md`, `PROVENANCE.md`, and `claim.schema.json` distinguish claim status from source identity, local implementation, and validation. `validate.py` and `arxiv_probe.py` are documentary and bibliographic helpers, not proof engines.

## 3. 人话解释 / In Plain Language

**中文** — 普通人可以把它看成**建造复杂 AI 系统前的设计蓝图与验收问题库**：有人说“智能体已经学会记忆”，本仓会追问记忆从何而来、是否仍可追溯、删改后如何纠正、能否在另一会话重现。先把问题问准确，才能谈系统可靠。

**English** — Think of this as a **blueprint and evidence ledger for a complex AI building**. If someone says an agent remembers reliably, this layer asks whose memory, under what scope, how it was tested, and how a wrong memory is corrected. It defines what must be explained before anyone claims the building is safe or complete.

## 4. 如何读懂而不夸大？ / Verification and Non-claim Boundaries

**中文** — 论文支持某个命题，不意味着本仓已实现机制；通过 `FOUNDATION.test_contract` 等结构校验，不意味着数学或社会科学结论已实测。认知架构 Soar/ACT-R 以及多智能体系统文献是学术参照，不是本仓实现认证。必须保留 `NOT_IMPLEMENTED`、`REFERENCE_ONLY` 和 `NOT_TESTED` 的真实含义。

**English** — A cited paper is not local code. Passing structural validators cannot establish theorem correctness or operational agent behavior. Soar, ACT-R, and multi-agent systems are disciplinary comparators, not certified implementations here. Explicit `NOT_IMPLEMENTED`, `REFERENCE_ONLY`, and `NOT_TESTED` states remain meaningful.

## 5. 十仓中的独特贡献 / Place in the Ten-repository Research System

**中文** — 它回答十仓共同的 **WHY / 为什么要这样设计**。Axiom-0 探索执行规格，Zero-Entropy Lab 探索可靠性，Welcome 探索知识生命周期，Reflective Continuum 探索反思性观测；后三个科研工程仓及两个观察站各有独立技术对象。跨仓理论关联不构成自动代码依赖。

**English** — Its portfolio contribution is **WHY: architectural premises and evidence discipline**. Axiom-0 covers bounded executable specifications; Zero-Entropy Lab explores runtime reliability; Welcome hosts knowledge lifecycle; Reflective Continuum examines observable self-checks. Research-engineering and observatory repositories operate on different objects. Disciplinary coherence does not imply automatic software integration.

## 6. 纪念与升华 / Commemoration and Wider Meaning

**中文** — **纪念的不是一个万能模型，而是一个可公开反驳的系统观点**：Agent 越能行动，越需要解释行动的范围、来源与责任。成熟的复杂 AI 研究，应允许自己的理论被修正。

**English** — **This commemorates an accountable systems argument, not an omnipotent model.** The greater an agent's capacity to act, the greater its obligation to expose assumptions, authority, evidence, and correction paths.

## 外部学科对照 / External Disciplinary Anchors

- [CS2023 knowledge areas](https://csed.acm.org/knowledge-areas/)
- [CS2023 AI—Agents and Cognitive Systems](https://csed.acm.org/mockup-artificial-intelligence/)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

> **Provenance / 证据说明：** GitHub repository-native artifacts were read at the 2026-10-28 review cutoff. External sources establish disciplinary context only; independent reproduction, external certification and newly executed tests are **NOT_CLAIMED**. / 原生文件按本次时间点核读；外部来源只用于学科对照；**不声称本轮重新执行测试、独立复现或第三方认证**。
