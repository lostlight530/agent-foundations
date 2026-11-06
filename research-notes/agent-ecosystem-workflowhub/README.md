# Agent Open Ecosystem → WorkflowHub / GitHub 公开技术讨论科研化
**Status:** `RESEARCH_DESIGN_DRAFT` · checked 2026-11-04 · public-source-only · no DOI, no demonstrated WorkflowHub registration, no executable workflow claimed

## Purpose / 目的
Reconstitute inspectable, platform-separated research objects from the researcher's **own** public GitHub Discussions, Issues, individual Comments, PRs, and the actual responses of maintainers. Our object of study is **the evolution of engineering reasoning and public collaboration**, not a contest between commercial Agent runtimes, an official collaboration dossier, a product adoption claim, or a promotional aggregate.

核心转换：**GitHub original object → source identity and interaction edge → bounded knowledge / counterevidence → versioned research-workflow package → WorkflowHub discovery / citation / re-use**. A Discussion is source data; a future runnable evidence-aggregation workflow is the publishable computational method. A prose-only upload should never be advertised as an executed WorkflowHub workflow.

## Platform editions / 平台版次
| Research series edition | Topic | Evidence status | Own WorkflowHub version |
|---|---|---|---|
| E1 Astron | AgentFlow → Workflow Contract → Entrustability; iFLYTEK organization and MemFlywheel ecosystem separate annex | public practice + discussions + issue comments | separate entry/revision series |
| E2 Nexent | RailSmart → dynamic semantic orchestration / MCP → Skills ≠ subagents → Harness / control plane | 7 repo Discussions + one organization Discussion + maintainer replies + 3 community PRs | separate entry/revision series |
| E3 DeerFlow | Research Flow → Super Agent Harness, state, sandbox, memory, skills, subagents | primary software documentation; user GitHub participation not yet corroborated | separate entry only if a meaningful executable research object exists |

Here `E1/E2/E3` are **our collection's platform editions**, *not* a claim that a Nexent upload is a successor revision of an Astron executable workflow. Each platform gets a separate workflow/RO-Crate when validated, then its own genuine revision history. No mixing of publisher versions, source revisions, and inferred implementation histories.

## Core source classes
- `discussion`: one GitHub thread; `discussion_comment`: independently attributed response within that thread
- `issue_comment`: separately attributed comment under an Issue someone else may own
- `pull_request`: distinguish merged / closed-unmerged / changes actually contributed
- `official_repository`: architectural reference, **not** evidence that the user contributed
- `private_account`: personal event or private correspondence must not be shipped into public WorkflowHub assets by default

See [machine-readable ledger](./evidence-ledger.json), [Astron](./PLATFORM-EDITION-ASTRON.md), [Nexent](./PLATFORM-EDITION-NEXENT.md), [DeerFlow](./PLATFORM-EDITION-DEERFLOW.md), and [research/release protocol](./PROTOCOL.md).

## Audit boundaries / 已检查与尚未检查
- GitHub account: `lostlight530` from the connected GitHub account
- Public sources checked using GitHub-linked search, PR API / issue-comment APIs, and primary GitHub Discussion pages
- A search returning zero Issues is **not** global proof of no contributions; GitHub Discussions and all reply threads are not fully exposed through this connector's REST fetch
- Counts concern different object classes: 7 Nexent Discussion threads ≠ 7 comments; Nexent's one merged memorial-wall PR ≠ core runtime contribution
- DeerFlow author/event/DM contact reported in earlier personal discussions remains **self-reported external context**; do not publish correspondence or claim formal invitation/adoption on public research-object metadata without independently shareable evidence

## Non-goals
No update to `FOUNDATION/**` verified core, canonical Sxx sources, research producers, Actions, release metadata, OSF preregistration, or existing Zenodo / WorkflowHub freezes. This is a **research-notes sidecar** intended for human review before any scientific claim admission.

## Independent significance
From **open engineering dialogue** to **verifiable research objects**: we can preserve disagreement, maintainer correction, boundary conditions and interaction chronology, without attributing official status to personal theories. That is the transferable RSE/Open Science method, not simply cross-posting discussions.