# Agent Foundations / 智能体理论与证据基础

Agent Foundations is a bilingual theory, evidence, and architecture-decision base for reasoning about agent systems. It is not an implemented autonomous-agent runtime. Claims in this repository are bounded by named evidence, assumptions, implementation status, and validation status.

Agent Foundations 是用于研究智能体系统的双语理论、证据与架构决策基础，不是已实现的自治智能体运行时。本仓库的声明均受明确证据、假设、实现状态与验证状态约束。

## English

### Repository boundary

The independently maintained `FOUNDATION/` core separates evidence records and architecture decisions from the existing SOP-generated documentation stream. Equations, paper summaries, analogies, and pseudocode remain references until an executable repository artifact and test exist. External results can motivate a design, but they do not establish a repository capability.

### Verified-core reading order

1. [Evidence contract](FOUNDATION/EVIDENCE.md) — claim and evidence rules.
2. [Architecture principles](FOUNDATION/ARCHITECTURE.md) — system boundary and evaluation.
3. [Memory system](FOUNDATION/MEMORY.md) — memory lifecycle and limits.
4. [Tool system](FOUNDATION/TOOLS.md) — authority, observability, and recovery.
5. [Collaboration system](FOUNDATION/COLLABORATION.md) — coordination and failure propagation.
6. [Source registry](FOUNDATION/SOURCES.md) — primary-source records.
7. [Provenance](FOUNDATION/PROVENANCE.md) — reproducibility and AI-use disclosure.
8. [Maintenance contract](FOUNDATION/MAINTENANCE.md) — evidence cadence, five-axis admission, correction, and bilingual consistency.
9. [August 1–27 evidence ledger](docs/AUGUST_2026_01_27_EVIDENCE_LEDGER.md) — commit-backed provisional daily/weekly map; `MONTH_OPEN`.

Each material statement in the core has a stable Claim ID. English and Chinese text for a claim share that ID and the same evidence state.

### Evidence and status contract

Claim states are `OBSERVED`, `SUPPORTED`, `PROPOSED`, `HYPOTHESIS`, `CONTESTED`, and `RETIRED`. `SUPPORTED` is always limited to the cited system, task, data, configuration, metric, assumptions, and source version.

Evidence levels are:

- `E0_REPOSITORY_TEST`: executable artifact, fixture, command, and result in this repository.
- `E1_PRIMARY_STANDARD`: official standard, specification, or primary system card.
- `E2_PEER_REVIEWED`: peer-reviewed research with sufficient method detail.
- `E3_REPRODUCIBLE_PREPRINT`: preprint with a runnable artifact or inspectable data.
- `E4_PREPRINT`: preprint not reproduced by this repository.
- `E5_BACKGROUND`: survey, commentary, analogy, or secondary material.
- `E6_UNVERIFIED`: incomplete provenance or support.

Mapping states are `DIRECT_REQUIREMENT`, `DESIGN_ANALOGY`, `CANDIDATE_MECHANISM`, `COUNTEREVIDENCE`, and `OUT_OF_SCOPE`. They distinguish an adopted requirement from an analogy, possible mechanism, limiting evidence, or excluded subject.

Implementation states are `NOT_IMPLEMENTED`, `REFERENCE_ONLY`, `PARTIAL_PROTOTYPE`, and `IMPLEMENTED`. Validation states are `NOT_TESTED`, `STATIC_CHECKED`, `EXPERIMENTALLY_TESTED`, `REPRODUCED`, and `EXTERNALLY_REVIEWED`. An `IMPLEMENTED` claim must name a repository path; an `EXPERIMENTALLY_TESTED` claim must record its command, fixture, configuration, metric, and result.

### Four bounded research domains

| Domain | What the core records | Current boundary |
| --- | --- | --- |
| Architecture | Complete-system evaluation boundaries, enforceable interfaces, theorem scope, and reconstructable release evidence. | Specifications and evidence maps do not make the underlying model deterministic or constitute a runtime. |
| Memory | Selection, provenance, retrieval, compaction, retention, correction, and deletion as a lifecycle. | Most mechanisms are proposed or reference-only; this repository has no memory runtime. |
| Tools | Per-action authority, untrusted-input handling, inspectable plans, observability, monitors, idempotency, and recovery. | These are requirements and candidate mechanisms, not an implemented tool-control plane. |
| Collaboration | Topology tradeoffs, failure propagation, preserved trajectories, message contracts, and typed consensus. | External coordination results retain their original assumptions; no collaboration protocol is deployed here. |

### Executable repository evidence

The validator, schema, and contract tests provide executable evidence for documentary structure. Run them with Python 3.12 or 3.14 and no third-party Python packages:

```bash
python FOUNDATION/validate.py
python -m unittest FOUNDATION.test_contract -v
python FOUNDATION/validate.py --base-ref origin/main
```

The checks cover required files, claim metadata, unique IDs, registered sources, schema structure, restricted overclaims, pinned Actions, and protected paths. They do not establish semantic truth, mathematical correctness, translation quality, or reproduction of external experiments.

### Ownership and limitations

`FOUNDATION/` is the independently maintained verified core. `docs/` remains the existing SOP-generated research stream and is not silently upgraded into verified evidence by this README. The root README is an entry point; Claim IDs and source-specific records remain authoritative within the core.

This repository contains no autonomous-agent runtime, deployed memory system, tool-control plane, or collaboration protocol. Mathematical results retain their formal domain. Safety, reliability, and convergence must be evaluated for a named system and failure model; no universal conclusion is asserted here. AI output may assist drafting or consistency checks, but it is not evidence and maintainer review remains required.

## 中文

### 仓库边界

独立维护的 `FOUNDATION/` 核心把证据记录与架构决策同现有 SOP 自动生成文档流分开。公式、论文摘要、类比和伪代码在具备可执行仓库产物与测试之前都只是参考材料。外部结果可以启发设计，但不能证明本仓库已经具备相应能力。

### 可验证核心阅读顺序

1. [证据契约](FOUNDATION/EVIDENCE.md) — 声明与证据规则。
2. [架构原则](FOUNDATION/ARCHITECTURE.md) — 系统边界与评估。
3. [记忆系统](FOUNDATION/MEMORY.md) — 记忆生命周期与局限。
4. [工具系统](FOUNDATION/TOOLS.md) — 权限、可观测性与恢复。
5. [协作系统](FOUNDATION/COLLABORATION.md) — 协调与故障传播。
6. [来源登记](FOUNDATION/SOURCES.md) — 一手来源记录。
7. [来源与复现](FOUNDATION/PROVENANCE.md) — 可复现性与 AI 使用披露。
8. [长期维护契约](FOUNDATION/MAINTENANCE.md) — 证据周期、五轴准入、纠错与中英文一致性。
9. [8 月 1–27 日证据总账](docs/AUGUST_2026_01_27_EVIDENCE_LEDGER.md) — 基于提交的临时日/周映射；`MONTH_OPEN`。

核心中的每项实质性陈述都有稳定的 Claim ID。同一声明的中英文共享该 ID 与相同证据状态。

### 证据与状态契约

声明状态包括 `OBSERVED`、`SUPPORTED`、`PROPOSED`、`HYPOTHESIS`、`CONTESTED` 和 `RETIRED`。`SUPPORTED` 始终受所引系统、任务、数据、配置、指标、假设与来源版本约束。

证据等级包括：

- `E0_REPOSITORY_TEST`：本仓库中的可执行产物、夹具、命令与结果。
- `E1_PRIMARY_STANDARD`：官方标准、规范或一手系统卡。
- `E2_PEER_REVIEWED`：方法细节充分的同行评审研究。
- `E3_REPRODUCIBLE_PREPRINT`：带可运行产物或可检查数据的预印本。
- `E4_PREPRINT`：本仓库尚未复现的预印本。
- `E5_BACKGROUND`：综述、评论、类比或二手材料。
- `E6_UNVERIFIED`：来源或支持不完整。

映射状态包括 `DIRECT_REQUIREMENT`、`DESIGN_ANALOGY`、`CANDIDATE_MECHANISM`、`COUNTEREVIDENCE` 和 `OUT_OF_SCOPE`，用于区分已采纳要求、结构类比、候选机制、限制性证据和范围外主题。

实现状态包括 `NOT_IMPLEMENTED`、`REFERENCE_ONLY`、`PARTIAL_PROTOTYPE` 和 `IMPLEMENTED`。验证状态包括 `NOT_TESTED`、`STATIC_CHECKED`、`EXPERIMENTALLY_TESTED`、`REPRODUCED` 和 `EXTERNALLY_REVIEWED`。`IMPLEMENTED` 必须指向仓库路径；`EXPERIMENTALLY_TESTED` 必须记录命令、夹具、配置、指标和结果。

### 四个有边界的研究领域

| 领域 | 核心记录内容 | 当前边界 |
| --- | --- | --- |
| 架构 | 完整系统评估边界、可执行接口、定理适用域和可重建发布证据。 | 规范和证据映射不会使底层模型变成确定性系统，也不构成运行时。 |
| 记忆 | 把选择、来源、检索、压缩、保留、纠错和删除视为完整生命周期。 | 多数机制为提案或仅供参考；本仓没有记忆运行时。 |
| 工具 | 按动作授权、不可信输入处理、可检查计划、可观测性、监控、幂等与恢复。 | 这些是要求和候选机制，不是已实现的工具控制平面。 |
| 协作 | 拓扑权衡、故障传播、轨迹保留、消息契约和分类型共识。 | 外部协调结果保留其原始假设；本仓没有已部署的协作协议。 |

### 可执行仓库证据

验证器、Schema 和契约测试为文档结构提供可执行证据。支持 Python 3.12 或 3.14，不依赖第三方 Python 包：

```bash
python FOUNDATION/validate.py
python -m unittest FOUNDATION.test_contract -v
python FOUNDATION/validate.py --base-ref origin/main
```

检查范围包括必需文件、声明元数据、唯一 ID、已登记来源、Schema 结构、受限过度声明、Action SHA 固定和保护路径。它们不能证明语义真伪、数学正确性、翻译质量或外部实验复现。

### 所有权与局限

`FOUNDATION/` 是独立维护的可验证核心。`docs/` 仍属于现有 SOP 自动生成研究流，不会因本 README 而自动升级为已验证证据。根 README 是入口；核心内部仍以 Claim ID 和来源特定记录为准。

本仓库不包含自治智能体运行时、已部署记忆系统、工具控制平面或协作协议。数学结果必须保留其形式适用域。安全性、可靠性与收敛性必须针对明确系统和故障模型进行评估，本仓不作普遍结论。AI 输出可以辅助起草或一致性检查，但不构成证据；合并前仍需维护者评审。
