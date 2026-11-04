# E1 · Astron Agent / 从 AgentFlow 到可信执行的开放研究
**Status:** documented public-interaction history + prospective evidence-workflow design, not Astron runtime integration

## Why this edition
Astron has the clearest link between a concrete training-camp AgentFlow artifact and later reflections on execution contracts. Distinguish authored proposal, observed artifact description, official platform mechanics, maintainer invitation, and reproducible run evidence.

## Public chronology / 原始来源
| Date | Source | Object and claim boundary |
|---|---|---|
| 2026-01-08 | [#824](https://github.com/iflytek/astron-agent/discussions/824) | ResumeZhiYoutong (简历智优通): OCR/PDF, model orchestration, two-mode branch, state-driven interaction, structured advice; **author-described design**, not independently replayed result |
| 2026-01-10 | [#824 maintainer reply](https://github.com/iflytek/astron-agent/discussions/824) | FenjuFu invited an article for Awesome Astron Workflow; invitation ≠ verified publication |
| 2026-01-11 | [#824 author detailed reply](https://github.com/iflytek/astron-agent/discussions/824) | Extended architecture; preserve reply as separate authored edge, not a second Discussion. The page also shows a second author comment with **no visible body**, indexed as presence only |
| 2026-04-04 | [#1138](https://github.com/iflytek/astron-agent/discussions/1138) | Entrustability: actual real-task execution reliability beyond capability; **2026-10-14 FenjuFu public reply** proposes reproducible checks for idempotent write retries, approval/recovery input consistency, and memory-version provenance (proposal, not tests run) |
| 2026-05-31 | [#1359](https://github.com/iflytek/astron-agent/discussions/1359) | Workflow as explicit structural contract; **author's interpretation**, not official spec |
| 2026-05-31 | [#1360](https://github.com/iflytek/astron-agent/discussions/1360) | What remains after contract: continuity, authority, long-term responsibility |
| 2026-07-25 | [iFLYTEK org Discussion #4](https://github.com/orgs/iflytek/discussions/4) | User comment re public demos, community uptime vs official service/SLA, deployment templates |
| 2026-08-01 | [iFLYTEK org Discussion #1](https://github.com/orgs/iflytek/discussions/1) | Two user comments providing Chinese and English ecosystem navigation: Astron Agent/Skills/RPA/MemFlywheel |
| date separately verify | [MemFlywheel issue #72, user comment](https://github.com/iflytek/memflywheel/issues/72#issuecomment-5750056853) | Host/adapter/SDK/core/data architecture explanation; maintainer [confirms alignment with architecture.md](https://github.com/iflytek/memflywheel/issues/72#issuecomment-5857588519), not an official research partnership |
| date separately verify | [MemFlywheel issue #18, user comment](https://github.com/iflytek/memflywheel/issues/18#issuecomment-5750057816) | File-native long-term memory and extraction/recall/dream/skills observations; maintainer [acknowledgement](https://github.com/iflytek/memflywheel/issues/18#issuecomment-5857589250) |

The two MemFlywheel Issues belong to the **iFLYTEK ecosystem annex**, **not** the astron-agent Issue count. Their issue authors are other GitHub accounts. Never collapse the ecosystem into one repository or treat replies as platform implementation approvals.

## Research questions
1. How does a specific AgentFlow case motivate a later **workflow-as-contract** abstraction without implying deterministic LLM output?
2. Which responsibilities are explicit in a flow graph, and which remain in host, runtime, tool authorization, context, trace and human approval?
3. How do platform public-service expectations and long-term memory components affect **stewardship** beyond the workflow itself?
4. When did feedback acknowledge a design, invite more participation, or merely express appreciation? Classify each separately.

## Prospective WorkflowHub asset
Input: curated public URL records and permitted excerpts, source IDs, author/role, checked timestamp, theme registry, assertions and unresolved questions
Steps (to implement): fetch or ingest frozen public fixtures → normalize attributed entities → link discussion/reply edges → claim/counterclaim classification → provenance and schema validation → human review / release gate
Output: sources.jsonl, interaction-edges.jsonl, topic-map.json, claims-and-limits.md, provenance.json and verifiable receipt
No real private correspondence is packaged; no claims of current external registration or tested CWL yet.

**Working title:** *Astron Agent: From AgentFlow to Verifiable Workflow Contracts and Entrustability*