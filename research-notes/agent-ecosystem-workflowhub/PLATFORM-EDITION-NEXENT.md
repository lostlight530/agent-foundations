# E2 · Nexent / 从语义动态编排到 Harness 与 Skill Control Plane
**Status:** public evidence synthesis + prospective workflow research object; not official Nexent roadmap, integration, or adoption

## Why this edition
Nexent is not merely another Astron flowchart engine. The [maintainer's 2025-12-12 correction](https://github.com/ModelEngine-Group/nexent/discussions/2056) distinguishes **runtime-generated, context-driven semantic tool orchestration** from predeclared static Workflow. This is primary evidence for a different research question.

## Seven confirmed authored repository Discussions
| Date | Thread | Research role |
|---|---|---|
| 2025-11-23 | [#1816 RailSmart](https://github.com/ModelEngine-Group/nexent/discussions/1816) | DeepSeek-V3/MCP multi-agent travel decision system competition submission; includes attached JSON and DOCX; [geruihappy-creator replied positively 2025-12-15](https://github.com/ModelEngine-Group/nexent/discussions/1816) |
| 2025-12-02 | [#1982 Product suggestions](https://github.com/ModelEngine-Group/nexent/discussions/1982) | One-click pre-deployed MCP import and synchronization; YehongPan replied 2025-12-03 about current Streamable HTTP work and **planned** import tooling; user made follow-up comment |
| 2025-12-10 | [#2056 MCP and semantic workflow visualization](https://github.com/ModelEngine-Group/nexent/discussions/2056) | Explicit proposal; loveTsong's 2025-12-12 reply clarifies dynamic semantic orchestration, potential future workflow representation |
| 2025-12-31 | [#2179 Collaborative agents ≠ Skills](https://github.com/ModelEngine-Group/nexent/discussions/2179) | Distinguish autonomous subtask cognition from reuse of stable execution knowledge |
| 2026-04-04 | [#2757 Harness Engineering](https://github.com/ModelEngine-Group/nexent/discussions/2757) | Permission/memory/failure recovery/audit as product control obligations |
| 2026-05-31 | [#3148 Prompt Evolves Into Contract](https://github.com/ModelEngine-Group/nexent/discussions/3148) | Prompt as intent declaration; platform runtime role allocation; author's conceptual claim |
| 2026-08-02 | [#3568 Skill Ecosystem Control Plane](https://github.com/ModelEngine-Group/nexent/discussions/3568) | Governance as executable Skill kinds diverge: instruction, CLI, script, platform tool, installer/discovery |

## Actual Git contribution ledger (distinct from discussions)
- [PR #1825](https://github.com/ModelEngine-Group/nexent/pull/1825): community memorial wall, closed without merge
- [PR #1826](https://github.com/ModelEngine-Group/nexent/pull/1826): community memorial wall, closed without merge
- [PR #1838](https://github.com/ModelEngine-Group/nexent/pull/1838): community memorial wall, **merged 2025-11-25**; it is not a core orchestration code PR

## Research questions
1. When the workflow is dynamically generated, **where** are execution plan, provenance and decision responsibilities observable?
2. How are Sub-agents, Skills, MCP servers and tools distinguished as separate authority/runtime objects?
3. Which meanings of `contract` are **research interpretations** and which are explicit platform guarantees?
4. What governance is needed for instruction-only Skills versus bundled executable scripts/CLI, and how does approval differ?
5. How does maintainer correction revise the researcher's earlier static-visualization assumption?

## Proposed WorkflowHub edition
Use the same documentary evidence processing contract as E1, but Nexent-specific vocabulary and contradiction-aware temporal evidence:
`railsmart → mcp-ux → dynamic-workflow-correction → skill-reuse → harness → intent-contract → skill-governance`.
Outputs should include `interaction graph`, `maintainer-response timeline`, `architecture claims and scope`, `issue/PR status separate ledger`, and `unknowns`.
**Do not interpret a planned feature as deployed, or a merged memorial-wall PR as technical adoption**.

**Working title:** *Nexent: From Semantic Agent Orchestration to Harness Contracts and Skill Ecosystem Governance*