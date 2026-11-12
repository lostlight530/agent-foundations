# Research protocol / 三平台公开材料向 WorkflowHub 研究对象的转换合同
Status: `RESEARCH_SYNTHESIS_COMPLETE / EXECUTABLE_REPLAY_NOT_YET_ADDED`

## Research purpose

The primary result is not an audit score

It is a three-edition research corpus that turns public interaction and version-pinned architecture sources into platform-specific histories, research questions, responsibility models and WorkflowHub-ready metadata

- Astron studies the transition from AgentFlow practice to entrustability, workflow contracts and lifecycle responsibility
- Nexent studies the transition from a concrete multi-agent case to dynamic semantic orchestration, Harness contracts and Skill governance
- DeerFlow studies the transition from Research Flow to a ground-up rewritten Super Agent Harness

## Falsifiable task
For each edition, given frozen public GitHub source records, reproducibly produce a source-linked interaction/idea graph that preserves the distinction between **authored proposal**, **maintainer reply**, **implemented contribution**, **declared platform capability**, **observed runtime behavior**, and **unknown**. An output fails if it turns a comment into a new thread, a suggestion into an accepted feature, a merged non-runtime PR into implementation evidence, or an absent search hit into a universal absence claim.

## Granularity
- `source_object_id`: canonical public URL + repository / organization + object kind + number
- `interaction_id`: attributed comment or reply permalink if available; otherwise parent URL + positional note, not an invented URL
- `actor`: account ID for public GitHub, not an inferred role
- `platform_edition`: E1/E2/E3 internal grouping
- `source_version`: commit SHA, Git blob or archived response digest for a versioned source
- `head_sha` / `merge_commit_sha`: PR branch identity and merge result, kept separate because they are not interchangeable
- `observation_time`: when fetched; separate from author/publish event time; a date-only observation must not be represented as an exact timestamp
- `evidence`: `PUBLIC_PRIMARY`, `SELF_REPORTED`, `SEARCH_NO_MATCH`, `UNVERIFIED`, `CONTRADICTED`
- `preservation_status`: `PINNED_GIT_OBJECT`, `FROZEN_EXPORT`, or `LIVE_PAGE_ONLY`
- `verification_method`: the API, connector or public page used to inspect the object
- `object_state`: open, closed, closed-unmerged, merged or unknown where the platform exposes that state
- `interaction_class`: invitation, roadmap statement, correction, acknowledgement, review, merged code/data change, question, proposal
- `scientific_status`: independent of GitHub social engagement

## Research transformation workflow
```text
approved-public-source-manifest
      |
      v
bounded-fetch-or-frozen-snapshot  --(network failure/unknown preserved)
      |
      v
parse-and-deduplicate-source-identities
      |
      v
attributed-comment-and-PR-event-linking
      |
      v
topic/claim/maintainer-correction reconciliation
      |
      v
schema + source-provenance validation
      |
      v
human review / release gate
      |
      v
platform-specific research synthesis + WorkflowHub metadata + future RO-Crate
```
Direct webpage text is legitimate research input

The present release contains the completed semantic transformation and three WorkflowHub entry candidates

An executable replay with frozen fixtures and validation must still be added before representing the package as a tested computational workflow

## Edition outputs

Each edition contains

- source and interaction chronology
- research-stage evolution
- maintainer feedback or official architecture correction where present
- research questions
- WorkflowHub inputs, steps and outputs
- explicit evidence and publication boundaries

The future executable release should add `sources.jsonl`, `interactions.jsonl`, `idea-graph.jsonl`, `claims.csv`, `counterevidence.csv`, `run-receipt.json`, `ro-crate-metadata.json`, executable CWL/scripts and fixture tests

## Release/preservation
- Keep GitHub original URL, author, thread, timestamp, evidence level and exact extraction/snapshot identity separate
- Never include private DMs or NDA-covered information without affirmative disclosure rights
- Correct facts with explicit errata, preserve historical claims and actual replies
- Platform series edition E1/E2/E3 is independent of the real *version history* within each WorkflowHub entry
- Freeze WorkflowHub versions only **after** actual workflow, fixture/replay, permissions, citation metadata and signed-off evidence are present
- A WorkflowHub DOI identifies the deposited research object/its version, **not** external platform endorsement or adoption
- Long-term availability of a GitHub URL does not prove a retained immutable snapshot; record preservation state separately
- A live-page recheck can verify the current rendering but cannot retroactively create an immutable snapshot of the page as it appeared on the event date

## Primary platform/documentation references
- [WorkflowHub user guide](https://about.workflowhub.eu/docs/guide-to-using-workflowhub/)
- [WorkflowHub citable workflow and DOI guidance](https://about.workflowhub.eu/docs/citable/)
- [Original GitHub record ledger](./evidence-ledger.json)

## Review gates
G0 scope / permission: public and properly attributed only
G1 source integrity: source kind, authors, identity, date and link match
G2 epistemic: no ungrounded adoption, endorsement, runtime PASS or universal no-contribution claim
G3 execution: actual parser/validator/fixture replay with recorded command, SHA and results
G4 publication: humans approve the archive and WorkflowHub metadata, then freeze/mint DOI where appropriate

**Present state:** G0/G1/G2 research synthesis established from the identified primary pages and GitHub-plugin checks through 2026-11-08; mutable Discussion and comment bodies remain `LIVE_PAGE_ONLY`; G3 executable replay and G4 external WorkflowHub publication are **NOT_EXECUTED**.

