# Independent GPT Governance — Foundation Relay

Status: current public recovery kernel
Scope: repository-local recovery, independent audit, reconciliation, and bounded repair

This directory is the public handoff point for a memoryless independent reviewer. It routes the reviewer to repository-native authority and retained evidence without duplicating native task controls.

## Recovery order

Recover current state from current merged `main` first. For the subject under review, use the most specific current repository authority. Dated audits and maintenance records remain point-in-time evidence for their own windows.

At audit start record the current date, default branch, `main` SHA, relevant open pull requests, recent merged changes, and checks actually executed.

## Repository map

1. `FOUNDATION/INDEX.md` and `FOUNDATION/ARCHITECTURE.md` for the current foundation map and structure.
2. `FOUNDATION/EVIDENCE.md` for evidence semantics and `FOUNDATION/PROVENANCE.md` for provenance requirements.
3. `FOUNDATION/MAINTENANCE.md` for the current public maintenance contract and `FOUNDATION/REVIEW.md` for reviewer boundaries.
4. Current schemas, tests, sources, tools, specs, and implementation under `FOUNDATION/` for subject-specific machine and execution evidence.
5. Current Daily / Weekly / Monthly research artifacts for repository-visible cadence evidence.
6. `historical-audits/INDEX.md` and referenced records for corrections, period audits, non-canonical sidecars, maintenance, and reconciliation history.
7. Git history and merged PR chronology when producer identity, canonical status, timing, or historical state is disputed.

## Evidence boundaries

Keep claim, evidence, mapping, implementation, validation, and publication status separate. A source reference is not itself proof of local implementation. A validation result proves only the surface actually checked. A non-canonical sidecar does not become canonical merely because it exists or is newer.

Native Jules records remain native Jules records. GPT or other substitute material retains its actual producer and canonical status. Independent governance calibrates interpretation; it does not rewrite historical execution.

## History discipline

Historical artifacts are immutable point-in-time evidence. Use dated correction or reconciliation records when later evidence changes current interpretation. Preserve failed, missing, provisional, blocked, non-canonical, insufficient-evidence, and unknown states. Archive relocation is not semantic replacement.

If a historical execution or provenance fact cannot be recovered from repository-visible evidence, keep it `UNKNOWN` rather than reconstructing it from later state.

## Independent audit outcome

Separate current facts, historical facts, corrections, external claims, execution evidence, inference, and unknown state. When a concise governance status is useful, use:

- `HEALTHY`
- `REPAIR`
- `COORDINATE`
- `BLOCKED`

`HEALTHY` means no repair is required for the audited surface; it is not a universal correctness certificate.

If repair is justified, change only the owning current file(s) and the contracts, indexes, or projections that must remain synchronized. Do not create activity-only edits or fabricated backfill.

## Public boundary

This recovery kernel is intentionally repository-bounded. It relies on repository-visible evidence and public sources where needed. It does not require reconstruction of unavailable operator context, credentials, hidden memory, or unrelated orchestration.

## Handoff minimum

A durable independent audit should leave the next reviewer able to identify the base `main` SHA, scope and evidence window, authority used, checks run, checks not run, current findings, historical findings, corrections, unresolved items, and whether history and negative evidence were preserved.

Independent governance may recommend or prepare bounded changes. Final merge and doctrine authority remains with the maintainer.
