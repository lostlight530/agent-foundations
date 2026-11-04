# Research protocol / 证据整理、版本与发布合同
Status: `DESIGN_ONLY` — proposed, not executed, not a current WorkflowHub registration

## Falsifiable task
For each edition, given frozen public GitHub source records, reproducibly produce a source-linked interaction/idea graph that preserves the distinction between **authored proposal**, **maintainer reply**, **implemented contribution**, **declared platform capability**, **observed runtime behavior**, and **unknown**. An output fails if it turns a comment into a new thread, a suggestion into an accepted feature, a merged non-runtime PR into implementation evidence, or an absent search hit into a universal absence claim.

## Granularity
- `source_object_id`: canonical public URL + repository / organization + object kind + number
- `interaction_id`: attributed comment or reply permalink if available; otherwise parent URL + positional note, not an invented URL
- `actor`: account ID for public GitHub, not an inferred role
- `platform_edition`: E1/E2/E3 internal grouping
- `source_version`: commit SHA or archived timestamp/response digest when actually captured
- `observation_time`: when fetched; separate from author/publish event time
- `status`: `CONFIRMED_PRIMARY`, `SELF_REPORTED`, `SEARCH_NO_MATCH`, `UNVERIFIED`, `CONTRADICTED`
- `interaction_class`: invitation, roadmap statement, correction, acknowledgement, review, merged code/data change, question, proposal
- `scientific_status`: independent of GitHub social engagement

## Intended computational workflow
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
platform-specific evidence package + RO-Crate metadata
```
Direct webpage text can serve as data; an **executable process with pinned fixtures and validation** must be built before representing this as a tested computational workflow. Prefer a small, auditable transformer and official APIs; use exported frozen fixtures where API does not support Discussions. Do not invent action or retrieval success.

## Expected files for a future genuine release
`sources.jsonl` · `interactions.jsonl` · `idea-graph.jsonl` · `claims.csv` · `counterevidence.csv` · `run-receipt.json` · `ro-crate-metadata.json` · actual executable CWL/scripts · fixture tests · README and citation metadata

## Release/preservation
- Keep GitHub original URL, author, thread, timestamp, evidence level and exact extraction/snapshot identity separate
- Never include private DMs or NDA-covered information without affirmative disclosure rights
- Correct facts with explicit errata, preserve historical claims and actual replies
- Platform series edition E1/E2/E3 is independent of the real *version history* within each WorkflowHub entry
- Freeze WorkflowHub versions only **after** actual workflow, fixture/replay, permissions, citation metadata and signed-off evidence are present
- A WorkflowHub DOI identifies the deposited research object/its version, **not** external platform endorsement or adoption
- Long-term availability of a GitHub URL does not prove a retained immutable snapshot; record preservation state separately

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

**Present state:** G0/G1 partially established by primary-page and connector inspection; G2 policy drafted; G3 and G4 **NOT_EXECUTED**.