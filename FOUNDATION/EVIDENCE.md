# Evidence Contract / 证据契约

Effective: 2026-08-17  
Machine-readable schema: [claim.schema.json](./claim.schema.json)

## Jules automation boundary / 与 Jules 自动化的边界

This contract governs the independently maintained `FOUNDATION/**` verified core and reviewer-side claim handling outside the Jules SOP automation stream.

It is not a Jules task prompt, Jules repository-memory entry, or `AGENTS.md` instruction. It does not modify existing Jules Daily/Weekly/Monthly tasks. A Jules-generated research chunk may be checked against this contract after generation, but that review is external to the Jules task loop unless the Jules task is separately configured to adopt the same rules.

本契约约束 Jules SOP 自动化之外独立维护的 `FOUNDATION/**` 可验证核心及评审侧声明处理。它不是 Jules 任务提示词、Jules 仓库记忆或 `AGENTS.md` 指令，也不会修改现有 Jules Daily/Weekly/Monthly 任务。Jules 生成的研究块可以在事后按本契约核验，但除非 Jules 任务另行配置采用这些规则，否则这种核验属于 Jules 任务循环之外。

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

## Source identity gate / 来源身份门

Source identity verification precedes claim-strength verification.

For a material source record, preserve:

- stable identifier or canonical URL
- exact cited version/revision where one exists
- date belonging to that version/revision
- title/authors or issuer when identity could be ambiguous
- retrieval/check date

For explicit arXiv `vN` citations, use `VERSION_DATE_PAIR_VERIFIED` only after the version and its date are paired from primary submission history. If that pair was not verified, use `VERSION_DATE_NOT_VERIFIED` and keep the downstream claim narrower.

The first-submission date of an arXiv record is not the date of every later version.

## Claim-surface gate / 声明表面门

Record the strongest source surface actually checked:

- `ABSTRACT_SUPPORTED`
- `FULL_TEXT_SUPPORTED`
- `THEOREM_TEXT_VERIFIED`
- `FORMULA_TRANSCRIPTION_VERIFIED`
- `ASSUMPTIONS_VERIFIED`

A successful fetch, parser, TeX download, or model summary does not by itself establish any of these states.

A theorem/bound must retain its quantifiers, assumptions, comparator, domain, and version. A mechanism equation or probability factorization is not a convergence/error bound unless a theorem or derivation actually supplies that bound.

Long formulas that were not independently transcribed/checked remain paper-level evidence only; use a limitation such as `LONG_FORMULA_NOT_RECERTIFIED`.

## Primary-source conflict / 一手来源冲突

When primary surfaces disagree, use `PRIMARY_SOURCE_CONFLICT` or `CONTESTED` rather than selecting the convenient value.

Examples include:

- abstract vs theorem text
- HTML vs versioned TeX/PDF
- different source versions
- author/project records with materially different claims

Preserve each conflicting surface, narrow the downstream proposition to the common supported core, and require re-verification before restoring the stronger claim.

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

## Temporal provenance / 时间溯源

The observation/research period is part of evidence provenance.

- moving a W33 chunk into another section does not turn it into July evidence
- a Weekly synthesis must preserve the originating research period
- errata may supersede interpretation without erasing the original historical artifact

These rules govern the independent verified core and post-hoc review; they do not alter Jules task cadence or prompts.

## Minimum claim record / 最小声明记录

Every claim block records: Claim ID, state, evidence level, mapping, implementation, validation, sources, assumptions, supported proposition, limitations, source version where material, and provenance period where relevant.

每个声明块必须记录：Claim ID、状态、证据等级、映射、实现、验证、来源、假设、最小支持命题、局限，以及必要时的来源版本与研究时间来源。
