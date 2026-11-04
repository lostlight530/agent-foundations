# E3 · DeerFlow / 从 Research Flow 到 Super Agent Harness 的架构观察
**Status:** `ARCHITECTURE_REFERENCE_ONLY / PERSONAL_INTERACTION_NOT_PUBLICLY_CORROBORATED`

## Correct boundary
The [official bytedance/deer-flow repository](https://github.com/bytedance/deer-flow) describes the current 2.0 project as a **super agent harness** with subagents, memory, sandbox, Skills, context engineering and other platform runtime facilities. The official README says **2.0 is a ground-up rewrite and shares no code with 1.x**. Therefore a historical Deep Research v1 narrative is not automatically evidence about the current v2 implementation.

Prior personal context reports an author/maintainer encounter around WAIC and subsequent direct communication. Those are **self-reported off-platform interactions** and not GitHub issue/discussion comments, public contribution, or formal collaboration without corroborating shareable artifacts. Keep all private messages, identities beyond already-public facts, NDA and event context outside a public WorkflowHub release.

## Checked negative results
The connected GitHub issue search for `author:lostlight530` and `commenter:lostlight530` within `bytedance/deer-flow`, plus user PR search, returned **no matches in that search surface** at the 2026-11-04 check. This is **SEARCH_NO_MATCH**, not `NO_PARTICIPATION_EVER`. GitHub Discussions and issue-search coverage can be incomplete.

## Research questions (hypotheses; no user contribution inferred)
- What does **Harness** own vs the sub-agent reasoning component?
- How do Memory, Context, Skills, Sandbox, permissions and tool execution differ in terms of lifecycle and trust?
- Where does run/session continuity live, and what evidence remains after long-horizon execution or recovery?
- What 1.x/2.0 claims are version-specific, and which need runtime traces before being asserted?

## WorkflowHub admission gate
Do **not** publish a "DeerFlow community-interaction archive" while original attributed community records are absent. A legitimate E3 could instead be a clearly named **public architecture-source cartography workflow** if it processes real pinned official materials, records source versions and produces a reproducible provenance-based artifact. Label it `external architecture observation`, not `developer contribution history`.

Potential non-sensitive evidence slots: pinned public README commit, public docs, official issues/discussions with verified authors, reproduced local experiments **if actually run**. Unknown observations must remain unknown.

**Working title:** *DeerFlow 2.0: Harness Runtime Boundaries and Evidence-Grounded Architecture Cartography*