# 月度战略蓝图 — 当前状态

当前证据窗口：**2026-08-01 至 2026-08-27**  
状态：**PROVISIONAL — 自然月尚未结束**  
权威阶段记录：[`../monthly/2026-08-through-27-strategic-blueprint.md`](../monthly/2026-08-through-27-strategic-blueprint.md)

## 当前定位

Agent Foundations 是一个**理论、证据与文档型架构仓库**，不是已经实现的自治智能体运行时

## verified-core 当前边界

当前可验证核心以这些真实仓库表面为准：

- Architecture、Memory、Tools、Collaboration 四个领域 Claim 映射
- `FOUNDATION/SOURCES.md` 中 canonical `S01–S35` 来源登记
- `FOUNDATION/claim.schema.json` 中的 Claim vocabulary
- `FOUNDATION/validate.py` 的结构/文档检查
- `FOUNDATION/arxiv_probe.py` 的 arXiv 身份与版本日期辅助核验
- Evidence、Provenance、Review 与显式 reconciliation 记录

当前 validator 不再把来源总数硬编码在程序里，而是从 registry 推导连续编号，并拒绝重复 canonical source identity。对于 arXiv，同一 base paper 的后续版本或隔日重访都不能获得第二个 S ID。

`STRUCTURAL_VALIDATOR_PRESENT != CLAIM_SEMANTICS_VERIFIED`

## 8 月 24–27 日纠错

- S33、S34、S35 作为三个不同来源保留
- S35 作者信息修正为 **Ayush Rai、Shaoshuai Mou**
- 原尝试登记的 S36 被撤销，因为 RAFA（`arXiv:2309.17382`）已经是 S10
- 2026-08-27 的 RAFA 双语 Daily Research Chunk 继续作为历史研究保留，但当前 provenance 统一解析到 S10

详见 [`../AUGUST_2026_24_27_RECONCILIATION.md`](../AUGUST_2026_24_27_RECONCILIATION.md)

## 研究生命周期

Daily Research Chunk 是候选证据输入，不自动进入 verified core。Weekly / Monthly 可以做汇总、校准和纠错，但不能把同一来源反复引用升级成独立佐证，也不能把外部论文结果升级成本仓实现。

## 四个领域的本地实现状态

- **Architecture**：文档/证据映射，没有 Agent runtime
- **Memory**：没有 memory runtime、vector store、retrieval service、compaction engine 或 cross-session memory service
- **Tools**：没有 tool runtime、permission broker、sandbox、monitor、replay engine 或副作用控制层
- **Collaboration**：没有 multi-agent transport、consensus runtime、task arbiter、role router 或 trajectory-capture service

## 月度边界

这不是最终 August Monthly Strategic Blueprint。2026-08-27 之后的证据尚未合成进本阶段记录。

正式状态：`MONTH_OPEN`
