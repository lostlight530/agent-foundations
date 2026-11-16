# Agent Foundations — English research guide

## 中文权威导读 / Chinese authoritative reading guide

Agent Foundations 是针对 Agent System 的架构、记忆、工具与协作研究知识库，不是通用 Agent Runtime、沙箱、记忆服务或可直接部署的多 Agent 协作系统

当前规范层按 `FOUNDATION/INDEX.md` 的四领域 23 条 Claim、`FOUNDATION/EVIDENCE.md` 的 Claim/Evidence/Mapping/Implementation/Validation 五轴、`FOUNDATION/SOURCES.md` 的来源身份及 `FOUNDATION/PROVENANCE.md` 的溯源门禁解释，不从历史研究正文推断功能实现或科学复现

本仓的独立中文领域全文对应于 [中文阅读入口](../zh/README.md)，双语理论正文按领域分别对应 [Architecture](../zh/Architecture_Principles.md)、[Memory](../zh/Memory_System.md)、[Tools](../zh/Tool_System.md)、[Collaboration](../zh/Collaboration_System.md)，历史 `S63` 是两个不同论文对象的标签冲突，不能仅凭 S63 编号迁移 Claim

**English authority reminder:** The English and Chinese long-form research files are complementary historical narratives, while the current verified-core Claim maps and source identities remain in `FOUNDATION/**`, and a local structural check does not establish model behavior or theorem validity


**Current interpretation: 2026-11-15** · **Reference:** repository `main` at `608bf59eb503effdf211aa2f9b448f24d3ede0dc` · **Document class:** current public navigation, not an experiment or historical producer record

## Overview — what this repository establishes

Agent Foundations is a bilingual **Agent Systems research, evidence, and architecture-documentation core**. It is not a deployed deterministic or autonomous agent, tool-control service, persistent-memory engine, or distributed-consensus runtime. The repository provides versioned `AF-*` claim maps, an external-source registry, explicit evidence/mapping/implementation/validation dimensions, JSON Schema, and documentary validators.

**At the inspected revision:** four canonical domains contain **23 claims** (Architecture 6, Memory 5, Tools 6, Collaboration 6); `FOUNDATION/SOURCES.md` declares **S01–S67** with 67 distinct contiguous registered identifiers. This is an inventory of documentary artifacts, **not** 67 independently reproduced scientific results. A documented historical `S63` collision remains unresolved across historical prose; identify the exact paper and version rather than relying on the `S63` label alone.

Current authority: [verified-core index](../../FOUNDATION/INDEX.md) → [claim/evidence semantics](../../FOUNDATION/EVIDENCE.md), [canonical sources](../../FOUNDATION/SOURCES.md), [provenance](../../FOUNDATION/PROVENANCE.md), [review](../../FOUNDATION/REVIEW.md) → four domain Claim maps. A theorem, formula or pseudocode in the long-form series must be read through these owning records. Neither old promotional wording nor a source citation promotes a mechanism to `IMPLEMENTED` or `REPRODUCED`.

## Four research domains — the detailed reading path

| Long-form research and examples | Canonical current Claim map | Central research question and implementation limit |
| --- | --- | --- |
| [Architecture Principles / Gradient Entropy](./Architecture_Principles.md) | [Architecture](../../FOUNDATION/ARCHITECTURE.md), `AF-ARCH-001..006` | What does a theorem actually constrain in a configured model + harness + tools + evaluator? **No whole-agent convergence/safety proof or runtime here** |
| [Memory / SimCLR and representation learning](./Memory_System.md) | [Memory](../../FOUNDATION/MEMORY.md), `AF-MEM-001..005` | How do retention, retrieval, compaction, authenticated origin, expiry and correction preserve critical state? **No memory engine here** |
| [Tools / policy optimization](./Tool_System.md) | [Tools](../../FOUNDATION/TOOLS.md), `AF-TOOL-001..006` | How are tool availability, delegated authority, execution, effect evidence and unknown outcomes distinguished? **No executor/permission broker here** |
| [Collaboration / decentralized optimization](./Collaboration_System.md) | [Collaboration](../../FOUNDATION/COLLABORATION.md), `AF-COLLAB-001..006` | What exactly converges—messages, replica state or independently verified truth—and under which topology/failure model? **No multi-agent runtime here** |

## How to interpret the underlying long-form research

These articles preserve substantial historical literature notes, analogies, mathematical expressions, candidate mechanisms and pseudocode. Their age or their length is **not** evidence that the repository implements the mechanisms. Older text saying "absolutely safe," "guaranteed convergence," "perfect memory" or "zero tool risk" is historical design rhetoric or a research hypothesis, **not the current technical conclusion**.

For any claim, separately identify **Claim State, Evidence Level, Mapping State, Implementation State, Validation State**, source paper/version, assumptions, actual local code, counterexample and result. External theorem scope is not agent-system scope. A source registry entry, Git commit, validator definition, test fixture and actual test execution are distinct evidence objects.

**Revision boundary:** this 2026-11-15 guide is grounded in repository source/document reading. External mathematical proofs and all historical paper transcriptions were **NOT_REVERIFIED** by this edit; newly proposed runtime experiments were **NOT_EXECUTED**. Earlier research and dated records remain preserved, without retroactive status change.
