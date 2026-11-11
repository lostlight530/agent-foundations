## Summary

What problem does this change address, and what changed?

## Change type

- [ ] claim / evidence / source update
- [ ] architecture / memory / tools / collaboration documentation
- [ ] validator / schema / executable helper
- [ ] bilingual consistency / documentation
- [ ] repository infrastructure / metadata
- [ ] maintenance / governance

## Affected core surfaces

List the affected Claim IDs, source IDs, `FOUNDATION/` documents, executable checks, schemas, or public metadata. Note related surfaces intentionally left unchanged.

## Evidence and status impact

Describe any change to claim state, evidence level, mapping state, implementation state, or validation state.

If external sources are involved, identify the canonical source identity, exact version/date when material, checked surface, supported proposition, and limitations.

## Validation performed

List exact commands/checks actually run and their observed results.

## Known limits / validation not performed

List material checks, source surfaces, translations, environments, or external experiments not examined or reproduced.

## Provenance and historical impact

State whether source identity, producer/revision identity, bilingual alignment, current correction status, or historical point-in-time interpretation changes.

## Security and privacy

Describe security/privacy implications and follow `SECURITY.md` for sensitive reports.

## Publication / metadata impact

State whether README, citation metadata, release metadata, or public discovery surfaces must remain synchronized. Repository DOI metadata is not external scientific evidence for a Claim.

## Rollback

Describe the smallest safe rollback.

## Review checklist

- [ ] The diff is limited to the stated purpose.
- [ ] Claim IDs and source identities remain stable or have an explicit migration.
- [ ] Checks described as passing were actually executed.
- [ ] Bilingual claim surfaces remain aligned where applicable.
- [ ] Historical evidence was not silently rewritten to match later knowledge.
- [ ] No credentials, private data, or unrelated generated/local state is included.

## Independent A1/A2 original PR acceptance (when applicable)

- [ ] Identify independent maintenance A1 vs A2 separately from repository-native task labels, Periodic Audit, successor and correction
- [ ] A1 covers the entire MonthStart..N−1 applicable input set and records every applicable file's reviewed disposition
- [ ] A2 starts from a freshly inspected main with original A1 merged, and reconciles all MonthStart..N relationships
- [ ] Record true original PR GitHub additions (minimum 100), final head/diff, merge receipt and main retention separately
- [ ] Valid content includes evidence-backed per-file decisions, provenance/SHA custody, coverage proof, relationships, counterexamples, status changes and qualified NO_FOLLOW_UP
- [ ] Do not demand 100 unrelated novel scientific findings; do not pad with duplicate/empty/fabricated lines
- [ ] Distinguish delivery, numeric gate, content validity, Native execution and checks actually run; preserve UNKNOWN and PARTIAL
- [ ] Late same-original-PR revisions must be reviewed at the final head; early Draft NOT_MET is not automatically final
- [ ] Original numeric shortfalls remain historic facts; successor additions never backfill them
- [ ] For 2026-11-01..11 reference [dated independent A1/A2 calibration](../historical-audits/2026-11/2026-11-11-a1a2-effective-pr-acceptance-reconciliation.md) without rewriting the originals
