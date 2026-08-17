# Evidence Contract / 证据契约

Effective: 2026-08-17  
Machine-readable schema: [claim.schema.json](./claim.schema.json)

## Claim states / 声明状态

- `OBSERVED`: directly measured in a named repository artifact or run / 在指定仓库产物或运行中直接观测。
- `SUPPORTED`: supported within named evidence and assumptions / 在明确证据与假设内获得支持。
- `PROPOSED`: an architecture decision awaiting implementation / 尚待实现的架构决策。
- `HYPOTHESIS`: a falsifiable research question / 可证伪研究假设。
- `CONTESTED`: credible evidence supports competing conclusions / 可信证据支持不同结论。
- `RETIRED`: retained only as a superseded position / 仅为记录已废止立场而保留。

`SUPPORTED` never means universally true. It is bounded by the cited system, task, data, model, harness, budget, metric, source version, and exact proposition verified.

`SUPPORTED` 从不表示普遍真理；它受所引用系统、任务、数据、模型、Harness、预算、指标、来源版本与已核验命题约束。

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

Terms from optimization, control, neuroscience, information theory, game theory, or bandit theory are not transferred to general LLM-agent behavior without an explicit bridge and validation plan.

优化、控制、神经科学、信息论、博弈论或 Bandit 理论术语，若无明确推理桥梁与验证计划，不得直接迁移为一般 LLM 智能体行为结论。

## Source identity gate / 来源身份门

Before a source can support a material claim, its bibliographic identity must be fixed.

For an explicit arXiv `vN` citation, record or verify:

- canonical arXiv base identifier
- exact requested version `vN`
- title
- authors when material to identity
- the submission/revision date belonging to `vN`
- retrieval date

Do not pair an explicit `vN` with the v1 submission date merely because the base arXiv record first appeared on that date.

Recommended provenance statuses:

- `IDENTITY_VERIFIED`: base identifier/title correspond to the intended work.
- `VERSION_DATE_PAIR_VERIFIED`: explicit `vN` and that version's submission/revision date correspond.
- `VERSION_DATE_NOT_VERIFIED`: version/date pairing was not established; do not guess.
- `PRIMARY_SOURCE_CONFLICT`: primary surfaces disagree materially; preserve the conflict until resolved.

`FOUNDATION/arxiv_probe.py` is the repository helper for arXiv identity/version history. If it is unavailable or fails, inspect the primary arXiv submission history manually rather than substituting search snippets.

## Proposition and theorem gate / 命题与定理门

Source identity verification is not theorem verification.

Use the narrowest status justified by what was actually checked:

- `ABSTRACT_SUPPORTED`: the primary abstract directly supports the proposition.
- `FULL_TEXT_SUPPORTED`: the proposition was checked in the primary paper text.
- `THEOREM_TEXT_VERIFIED`: theorem/lemma statement, conditions, and conclusion were located in primary full text.
- `FORMULA_TRANSCRIPTION_VERIFIED`: the exact formula and notation were checked against primary full text or TeX source.
- `ASSUMPTIONS_VERIFIED`: assumptions required for the quoted result were explicitly checked.

`VERIFIED_FROM_LATEX_SOURCE` or an equivalent strong label is allowed only when the relevant formula/theorem and its assumptions were actually traced to the source, not merely when TeX was available.

A formula may be authentic while the explanatory sentence around it is over-strong. Verify both transcription and interpretation.

## Primary-source conflict / 一手来源冲突

Primary sources can contain internal inconsistencies across abstract, rendered HTML, theorem text, TeX, or versions.

When two primary surfaces disagree materially:

1. do not select the preferred value by intuition
2. record both surfaces and versions
3. mark the claim `CONTESTED` or provenance `PRIMARY_SOURCE_CONFLICT` as appropriate
4. narrow downstream claims to the common supported proposition
5. reverify from the versioned TeX/PDF or a later author correction before restoring a stronger claim

An unresolved primary-source conflict cannot receive an unqualified `VERIFIED_FROM_LATEX_SOURCE` label.

## Mechanism vs bound / 机制与边界

A decomposition, factorization, pseudocode equation, objective, or update rule is not automatically a convergence theorem or numerical error bound.

To call a result a formal bound, record the theorem or proposition that supplies:

- bounded quantity
- comparison/baseline quantity
- domain and assumptions
- constants or asymptotic terms where relevant
- exact relation (`≤`, `≥`, approximation factor, regret order, etc.)

Empirical improvement and formal convergence are different evidence classes.

## Implementation and validation / 实现与验证

Implementation: `NOT_IMPLEMENTED`, `REFERENCE_ONLY`, `PARTIAL_PROTOTYPE`, `IMPLEMENTED`.

Validation: `NOT_TESTED`, `STATIC_CHECKED`, `EXPERIMENTALLY_TESTED`, `REPRODUCED`, `EXTERNALLY_REVIEWED`.

`IMPLEMENTED` requires a repository path. `EXPERIMENTALLY_TESTED` requires a command, fixture, configuration, metric, and result.

`IMPLEMENTED` 必须指向仓库路径；`EXPERIMENTALLY_TESTED` 必须记录命令、夹具、配置、指标和结果。

## Mathematical discipline / 数学纪律

A theorem or bound retains its assumptions and quantified domain. A result for a Bayesian adaptive MDP, convex objective, stochastic optimizer, harmonic game, subadditive valuation model, sparse hypergraph, or specified graph does not establish the behavior of general LLM agents.

定理或边界必须保留其假设与量化域。贝叶斯自适应 MDP、凸目标、随机优化器、调和博弈、次可加估值、稀疏超图或特定图上的结果，不能证明一般 LLM 智能体的行为。

Pseudocode is `REFERENCE_ONLY` unless it executes and is covered by repository tests. Translation, notation changes, analogies, and prompt-generated examples are not replication.

伪代码在可执行且具有仓库测试前均为 `REFERENCE_ONLY`。翻译、符号改写、类比和 Prompt 生成示例均不属于复现。

## Daily research → weekly weaving / 日研究到周编织

Weekly weaving may reorganize a Daily chunk into a system document, but it must preserve:

- source identity and version
- claim/evidence level
- assumptions and limitations
- implementation/test boundary
- unresolved source conflicts
- original research period provenance

A W33 integration must not be represented as a July observation merely because it is inserted near a July sync heading. Temporal provenance is part of evidence.

## Minimum claim record / 最小声明记录

Every claim block records: Claim ID, state, evidence level, mapping, implementation, validation, sources, assumptions, supported proposition, and limitations.

Every material external-paper claim additionally records or can recover: exact source version, version-date status, proposition/theorem verification status, and unresolved source conflicts.

每个声明块必须记录：Claim ID、状态、证据等级、映射、实现、验证、来源、假设、最小支持命题和局限。实质性论文声明还必须能够恢复准确版本、版本日期核验状态、命题/定理核验状态及未解决的一手来源冲突。
