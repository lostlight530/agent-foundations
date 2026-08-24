# Architecture Principles / 架构原则

## AF-ARCH-001 — System boundary / 系统边界

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S01, S03

**EN.** An evaluated agent is the complete configured system: model, instructions, tools, permissions, memory, control loop, safeguards, retries, budgets, environment, and scoring procedure. Model identity alone is insufficient to reproduce or compare an agent result.

**ZH.** 被评估的智能体是完整配置系统：模型、指令、工具、权限、记忆、控制循环、防护、重试、预算、环境和评分过程。仅凭模型名称不足以复现或比较智能体结果。

**Scope and limits / 范围与局限:** This is an evaluation/documentation boundary. The repository does not contain an agent runtime. / 这是评估与文档边界；本仓不包含智能体运行时。

## AF-ARCH-002 — Deterministic shell, stochastic component / 确定性外壳与随机组件

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `CANDIDATE_MECHANISM`
- **Implementation / 实现:** `NOT_IMPLEMENTED`
- **Validation / 验证:** `NOT_TESTED`
- **Sources / 来源:** S01, S02, S03

**EN.** Deterministic validation, schemas, permissions, budgets, idempotency keys, and state transitions can constrain an agent without making the underlying model deterministic. The correct engineering claim is bounded behavior at enforced interfaces, not deterministic cognition.

**ZH.** 确定性验证、Schema、权限、预算、幂等键和状态迁移可以约束智能体，但不会使底层模型变成确定性系统。正确工程表述是“在强制接口上约束行为”，而不是“确定性认知”。

**Scope and limits / 范围与局限:** This is a proposed architecture principle only; Agent Foundations does not implement the described runtime controls. / 这只是候选架构原则；Agent Foundations 未实现这些运行时控制。

## AF-ARCH-003 — Theorem scope is not agent scope / 定理适用域不等于智能体适用域

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E2_PEER_REVIEWED`
- **Mapping / 映射:** `COUNTEREVIDENCE`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S10, S11

**EN.** RAFA’s regret result and CHMAS’s convergence result apply under their stated formal models and assumptions. They do not establish convergence, safety, or sample efficiency for arbitrary LLM-agent deployments.

**ZH.** RAFA 的遗憾界和 CHMAS 的收敛结果只在各自形式模型与假设下成立，不能证明任意 LLM 智能体部署的收敛性、安全性或样本效率。

**Scope and limits / 范围与局限:** Exact assumptions must accompany any reused formula or bound. / 复用任何公式或边界时必须同时保留精确假设。

## AF-ARCH-004 — Evaluators create evidence, not truth / 评估器产生证据而非真理

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S03, S04, S05, S17

**EN.** Executable evaluators, trace inspection, and independent review can strengthen a claim. Their coverage, false positives, false negatives, contamination, reward hacking, and evaluation awareness remain part of the result.

**ZH.** 可执行评估器、轨迹检查和独立评审可以增强证据，但其覆盖率、误报、漏报、污染、奖励投机和评估意识仍属于结果的一部分。

**Scope and limits / 范围与局限:** Passing a finite evaluator establishes only the tested properties; this repository's own validator is structural and documentary, not an agent evaluator. / 通过有限评估器只证明被检查属性；本仓自身 validator 属于结构/文档检查器，并不是智能体评估器。

## AF-ARCH-005 — Constitutions are governed policies / 宪法是受治理的策略

- **State / 状态:** `SUPPORTED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DESIGN_ANALOGY`
- **Implementation / 实现:** `REFERENCE_ONLY`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S06, S07, S16

**EN.** Natural-language constitutions and policies can shape behavior, yet compliance is empirical and revision remains necessary. Policy generation and policy following are different capabilities.

**ZH.** 自然语言宪法和策略可以塑造行为，但遵循程度必须通过实证评估，且需要持续修订。策略生成与策略遵循是不同能力。

**Scope and limits / 范围与局限:** A document is neither a runtime guard nor a safety proof; this repository does not implement a constitution-execution engine. / 文档既不是运行时防护，也不是安全证明；本仓没有实现宪法执行引擎。

## AF-ARCH-006 — Release claims require reconstructable records / 发布声明需要可重建记录

- **State / 状态:** `PROPOSED`
- **Evidence / 证据:** `E1_PRIMARY_STANDARD`
- **Mapping / 映射:** `DIRECT_REQUIREMENT`
- **Implementation / 实现:** `PARTIAL_PROTOTYPE`
- **Validation / 验证:** `STATIC_CHECKED`
- **Sources / 来源:** S01, S03, S18

**EN.** A release claim should identify the relevant tree/revision, configuration, fixtures or evidence inputs, commands/results where they actually exist, metrics, and limitations. The repository's current partial prototype is its structured evidence/document core, not a release orchestrator.

**ZH.** 发布声明应标识相关代码树/版本、配置、夹具或证据输入，以及真实存在时的命令/结果、指标与局限。本仓当前的部分原型是结构化证据/文档核心，而不是发布编排器。

**Scope and limits / 范围与局限:** `claim.schema.json`, domain claim documents, source registry, provenance records, validator, and arXiv helper support documentary reconstruction only; they do not reproduce external experiments or execute an agent runtime. / `claim.schema.json`、领域声明、来源登记、溯源记录、validator 与 arXiv helper 只支持文档型重建，不复现外部实验，也不执行智能体运行时。

## Repository realization / 本仓真实实现

The six architecture claims above are theory/evidence statements. Agent Foundations itself is implemented primarily as documentary and provenance infrastructure.

| Repository surface | Actual repository function | Evidence boundary |
|---|---|---|
| `ARCHITECTURE.md`, `MEMORY.md`, `TOOLS.md`, `COLLABORATION.md` | structured domain claim maps with stable Claim IDs and explicit implementation states | claims remain bounded by their source/evidence fields |
| `claim.schema.json` | machine-readable claim-record vocabulary/enums | schema validity is structural, not semantic truth |
| `validate.py` | required-file, Claim-ID/metadata, S01–S32 source-reference, restricted-overclaim, action-reference and protected-path checks | does not verify theorem meaning, formula accuracy, source-version identity, or agent behavior |
| `arxiv_probe.py` | arXiv identity and submission-history version/date helper | bibliographic identity only; does not verify theorem semantics |
| `SOURCES.md` | canonical S01–S32 source registry | source registration does not imply implementation |
| `EVIDENCE.md`, `PROVENANCE.md`, `REVIEW.md` | public claim/evidence/provenance/review semantics | documentary interpretation only |
| August errata | explicit corrections to historical generated research | correction does not rewrite original generation history |

Current repository-wide implementation classification:

`DOCUMENTARY_AGENT_FOUNDATION_WITH_STRUCTURED_EVIDENCE_AND_PROVENANCE_SUPPORT`

not:

`IMPLEMENTED_AUTONOMOUS_AGENT_RUNTIME`.