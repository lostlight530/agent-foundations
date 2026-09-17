# Agent Foundations / 智能体理论与证据基础

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22791169.svg)](https://doi.org/10.5281/zenodo.22791169)

Agent Foundations is a bilingual theory, evidence, and architecture-decision base for reasoning about agent systems. It is not an implemented autonomous-agent runtime. Claims are bounded by named evidence, assumptions, mapping state, implementation state, and validation state.

Agent Foundations 是用于研究智能体系统的双语理论、证据与架构决策基础，不是已实现的自治智能体运行时。本仓库的声明受明确证据、假设、映射状态、实现状态与验证状态约束。

## Current verified core / 当前可验证核心

The current entry point is [`FOUNDATION/INDEX.md`](FOUNDATION/INDEX.md). The core separates current claim/evidence contracts from generated research streams and historical audit records.

当前入口为 [`FOUNDATION/INDEX.md`](FOUNDATION/INDEX.md)。核心层把当前声明/证据契约与生成式研究流、历史审计记录明确分开。

Recommended reading order / 建议阅读顺序：

1. [Index / 索引](FOUNDATION/INDEX.md) — current navigation and authority routing / 当前导航与权威路由。
2. [Evidence / 证据契约](FOUNDATION/EVIDENCE.md) — claim states, evidence levels, mapping, implementation, and validation semantics / 声明、证据、映射、实现与验证语义。
3. [Sources / 来源登记](FOUNDATION/SOURCES.md) — canonical external-source identities / 规范外部来源身份。
4. [Provenance / 溯源与复现](FOUNDATION/PROVENANCE.md) — source/version, producer, reproducibility, correction, and AI-use boundaries / 来源版本、生产者、复现、纠错与 AI 使用边界。
5. [Architecture / 架构](FOUNDATION/ARCHITECTURE.md) — system boundaries and evaluation principles / 系统边界与评估原则。
6. [Memory / 记忆](FOUNDATION/MEMORY.md) — memory lifecycle and limits / 记忆生命周期与局限。
7. [Tools / 工具](FOUNDATION/TOOLS.md) — authority, observability, and recovery / 权限、可观测性与恢复。
8. [Collaboration / 协作](FOUNDATION/COLLABORATION.md) — coordination and failure propagation / 协调与故障传播。
9. [Review / 审查](FOUNDATION/REVIEW.md) — review disposition and evidence calibration / 审查结论与证据校准。
10. [Maintenance / 长期维护](FOUNDATION/MAINTENANCE.md) — verified-core maintenance and correction policy / 可验证核心维护与纠错规则。

Historical ledgers and audit records under `historical-audits/` remain point-in-time evidence. They are not part of the current verified-core reading order and must not be treated as current status merely because they remain accessible.

`historical-audits/` 下的总账与审计记录属于时间点证据，不属于当前 verified-core 阅读顺序；文件仍可访问并不代表其中状态仍是当前状态。

## Evidence model / 证据模型

Claim states / 声明状态：

`OBSERVED · SUPPORTED · PROPOSED · HYPOTHESIS · CONTESTED · RETIRED`

Evidence levels / 证据等级：

- `E0_REPOSITORY_TEST` — executable repository artifact, fixture, command, and result / 本仓库可执行产物、夹具、命令与结果。
- `E1_PRIMARY_STANDARD` — official standard, specification, or primary system card / 官方标准、规范或一手系统卡。
- `E2_PEER_REVIEWED` — peer-reviewed research with sufficient method detail / 方法细节充分的同行评审研究。
- `E3_REPRODUCIBLE_PREPRINT` — preprint with runnable artifact or inspectable data / 带可运行产物或可检查数据的预印本。
- `E4_PREPRINT` — preprint not reproduced by this repository / 本仓尚未复现的预印本。
- `E5_BACKGROUND` — survey, commentary, analogy, or secondary material / 综述、评论、类比或二手材料。
- `E6_UNVERIFIED` — incomplete provenance or support / 来源或支持不完整。

Mapping states are `DIRECT_REQUIREMENT`, `DESIGN_ANALOGY`, `CANDIDATE_MECHANISM`, `COUNTEREVIDENCE`, and `OUT_OF_SCOPE`.

Implementation states are `NOT_IMPLEMENTED`, `REFERENCE_ONLY`, `PARTIAL_PROTOTYPE`, and `IMPLEMENTED`.

Validation states are `NOT_TESTED`, `STATIC_CHECKED`, `EXPERIMENTALLY_TESTED`, `REPRODUCED`, and `EXTERNALLY_REVIEWED`.

A source registration, implementation path, validator result, or review disposition advances only the dimension it actually supports.

来源登记、实现路径、验证器结果或审查结论，只能推进其实际支持的维度。

## Four bounded research domains / 四个有边界的研究领域

| Domain / 领域 | Core concern / 核心问题 | Boundary / 边界 |
| --- | --- | --- |
| Architecture / 架构 | complete-system evaluation, enforceable interfaces, theorem scope, reconstructable release evidence | specifications and evidence maps do not constitute an autonomous runtime |
| Memory / 记忆 | selection, provenance, retrieval, compaction, retention, correction, deletion | most mechanisms are proposed or reference-only; no memory runtime is deployed here |
| Tools / 工具 | per-action authority, untrusted input, observability, idempotency, recovery | requirements and candidate mechanisms are not an implemented tool-control plane |
| Collaboration / 协作 | topology, failure propagation, trajectories, message contracts, typed consensus | external coordination results retain their original assumptions; no collaboration protocol is deployed here |

## Executable repository evidence / 可执行仓库证据

The repository's validator, schema, and contract tests provide executable evidence for documentary structure:

```bash
python FOUNDATION/validate.py
python -m unittest FOUNDATION.test_contract -v
python FOUNDATION/validate.py --base-ref origin/main
```

These checks cover repository contracts such as required files, Claim IDs, source registration, schema structure, restricted overclaims, action references, and protected paths. They do not prove theorem correctness, translation quality, semantic truth, or reproduction of external experiments.

这些检查验证仓库结构契约，不证明定理正确性、翻译质量、语义真值或外部实验复现。

## Publication, source, and revision identity / 出版、来源与版本身份

The DOI above identifies an archived Agent Foundations software publication. It is repository-publication provenance, not an `Sxx` external scientific source and not direct support for a Foundation Claim.

上方 DOI 标识一个已归档的 Agent Foundations 软件出版对象。它属于仓库出版溯源，不是 `Sxx` 外部科研来源，也不会直接支持某个 Foundation Claim。

Keep these identities separate:

```text
repository DOI != canonical external source ID
repository DOI != claim support
canonical source registration != local implementation
Git revision != executed validation
archived publication != later main revision
```

When reproducibility depends on implementation state, record the exact Git revision and executed command/environment in addition to any publication citation. See [`FOUNDATION/PROVENANCE.md`](FOUNDATION/PROVENANCE.md).

## Repository streams and historical evidence / 仓库研究流与历史证据

`FOUNDATION/` is the independently maintained verified core. `docs/` and historical research streams may supply inputs and research history, but they are not silently promoted into verified-core evidence merely by existing in the repository.

`FOUNDATION/` 是独立维护的可验证核心。`docs/` 与历史研究流可以提供输入和研究历史，但不会因为存在于仓库中就自动升级为 verified-core 证据。

A later correction changes current interpretation without pretending that the corrected statement existed at the earlier observation time.

## AI assistance and limitations / AI 辅助与局限

AI assistance may support drafting, translation support, research organization, consistency checks, or candidate-source discovery. AI output is not evidence by itself. Material conclusions still require the repository's declared claim/evidence chain and inspectable support.

AI 可以辅助起草、翻译、研究组织、一致性检查和候选来源发现，但 AI 输出本身不构成证据。实质性结论仍需满足本仓声明的 claim/evidence 链和可检查支持。

This repository contains no autonomous-agent runtime, deployed memory system, tool-control plane, or collaboration protocol. Mathematical and empirical results retain their original formal and experimental scope. Safety, reliability, and convergence claims must name the system and failure model to which they apply.

本仓库不包含自治智能体运行时、已部署记忆系统、工具控制平面或协作协议。数学与实验结果保留其原始适用域；安全性、可靠性和收敛性声明必须明确适用系统与故障模型。
