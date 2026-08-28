# Agent Foundations maintenance contract / 长期维护契约

Status: `CANONICAL_PUBLIC_MAINTENANCE_CONTRACT`

Effective: 2026-08-28

## Research cadence and admission

A Daily research chunk records source identity, version/date/authors, source surface, claims, and limitations. Weekly cascade/conflict audits identify inheritance, duplicate identities, contradiction, and status promotion. Monthly blueprints remain provisional until the natural month ends. A historical `docs/**` chunk does not enter the verified core merely because generation succeeded.

Verified-core admission requires canonical source deduplication plus five independent axes: Claim State, Evidence Level, Mapping State, Implementation State, and Validation State. Paper truth does not imply mapping relevance; mapping does not imply implementation; implementation does not imply validation. `STATIC_CHECKED` is documentary structure evidence, not experimental reproduction.

Canonical source identity is based on stable identifiers such as normalized arXiv identity, not date or revisit. Version, submission date, authors, and inspected source surface must be checked independently. Abstract-only inspection is `ABSTRACT_SUPPORTED`; unverified theorem/formula text cannot be promoted. English and Chinese counterparts must carry equivalent five-axis states and limitations.

## Correction and authority

Preserve historical generated text. Use errata for factual metadata, reconciliation for cross-record conflict/duplication, and retirement for superseded identities. Authority order: targeted erratum/reconciliation; `SOURCES.md`; `EVIDENCE.md`/`PROVENANCE.md`/`REVIEW.md`; domain verified-core claims; historical `docs/**` stream.

Legacy `CONCEPTUAL_MAPPING` maps to `DESIGN_ANALOGY`. Legacy implementation `EVIDENCE_INSUFFICIENT` maps to `NOT_IMPLEMENTED` or `REFERENCE_ONLY`; legacy test status maps to `NOT_TESTED`. Evidence level is assigned from source type and inspected surface, never guessed from a legacy label.

Jules-generated research remains historical input. The verified-core validator checks structure only. Independent review calibrates claims; a human merges. This contract does not authorize private SOP/control changes, a runtime, dependencies, frontend, `.github/**`, or CI changes.

## Done, rollback, escalation

Done requires unique source identity, complete five-axis state, bilingual equivalence, updated authority links, retained conflicts, passing targeted validation with recorded environment/exit code, and explicit unrun checks. Revert the maintenance commit if validation or authority links regress. Escalate unresolved identity, author/version conflict, semantic translation mismatch, or status promotion to human review.
