# Evidence Contract / 证据契约

Effective: 2026-08-05  
Machine-readable schema: [claim.schema.json](./claim.schema.json)

## Claim states / 声明状态

- `OBSERVED`: directly measured in a named repository artifact or run / 在指定仓库产物或运行中直接观测。
- `SUPPORTED`: supported within named evidence and assumptions / 在明确证据与假设内获得支持。
- `PROPOSED`: an architecture decision awaiting implementation / 尚待实现的架构决策。
- `HYPOTHESIS`: a falsifiable research question / 可证伪研究假设。
- `CONTESTED`: credible evidence supports competing conclusions / 可信证据支持不同结论。
- `RETIRED`: retained only as a superseded position / 仅为记录已废止立场而保留。

`SUPPORTED` never means universally true. It is bounded by the cited system, task, data, model, harness, budget, metric, and source version.

`SUPPORTED` 从不表示普遍真理；它受所引用系统、任务、数据、模型、Harness、预算、指标和来源版本约束。

## Evidence levels / 证据等级

- `E0_REPOSITORY_TEST`: executable repository artifact, fixture, command, and result.
- `E1_PRIMARY_STANDARD`: official standard, specification, or primary system card.
- `E2_PEER_REVIEWED`: peer-reviewed research with sufficient method detail.
- `E3_REPRODUCIBLE_PREPRINT`: preprint with runnable artifact or inspectable data.
- `E4_PREPRINT`: preprint not reproduced by this repository.
- `E5_BACKGROUND`: survey, commentary, analogy, or secondary material.
- `E6_UNVERIFIED`: incomplete provenance or support.

Repository capability claims require `E0_REPOSITORY_TEST`. External evidence may motivate a design but cannot upgrade implementation status.

仓库能力声明必须具有 `E0_REPOSITORY_TEST`。外部证据可以启发设计，但不能提升仓库实现状态。

## Mapping states / 映射状态

- `DIRECT_REQUIREMENT`: a source requirement explicitly adopted here.
- `DESIGN_ANALOGY`: a bounded structural analogy.
- `CANDIDATE_MECHANISM`: a mechanism worth implementing and testing.
- `COUNTEREVIDENCE`: evidence limiting or contradicting a repository position.
- `OUT_OF_SCOPE`: field-relevant but outside this repository boundary.

Terms from optimization, control, neuroscience, or information theory are not transferred to LLM-agent behavior without an explicit bridge and validation plan.

优化、控制、神经科学或信息论术语，若无明确推理桥梁与验证计划，不得直接迁移为 LLM 智能体行为结论。

## Implementation and validation / 实现与验证

Implementation: `NOT_IMPLEMENTED`, `REFERENCE_ONLY`, `PARTIAL_PROTOTYPE`, `IMPLEMENTED`.

Validation: `NOT_TESTED`, `STATIC_CHECKED`, `EXPERIMENTALLY_TESTED`, `REPRODUCED`, `EXTERNALLY_REVIEWED`.

`IMPLEMENTED` requires a repository path. `EXPERIMENTALLY_TESTED` requires a command, fixture, configuration, metric, and result.

`IMPLEMENTED` 必须指向仓库路径；`EXPERIMENTALLY_TESTED` 必须记录命令、夹具、配置、指标和结果。

## Mathematical discipline / 数学纪律

A theorem or bound retains its assumptions and quantified domain. A result for a Bayesian adaptive MDP, convex objective, stochastic optimizer, or specified graph does not establish the behavior of general LLM agents.

定理或边界必须保留其假设与量化域。贝叶斯自适应 MDP、凸目标、随机优化器或特定图上的结果，不能证明一般 LLM 智能体的行为。

Pseudocode is `REFERENCE_ONLY` unless it executes and is covered by repository tests. Translation, notation changes, and prompt-generated examples are not replication.

伪代码在可执行且具有仓库测试前均为 `REFERENCE_ONLY`。翻译、符号改写和 Prompt 生成示例均不属于复现。

## Minimum claim record / 最小声明记录

Every claim block records: Claim ID, state, evidence level, mapping, implementation, validation, sources, assumptions, supported proposition, and limitations.

每个声明块必须记录：Claim ID、状态、证据等级、映射、实现、验证、来源、假设、最小支持命题和局限。
