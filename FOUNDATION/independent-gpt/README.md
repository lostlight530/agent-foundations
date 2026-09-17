# Independent GPT Governance — Foundation Relay

Status: current public recovery kernel  
Calibration: 2026-09-17  
Scope: repository-local maintenance recovery, independent review handoff, reconciliation, and bounded repair

This directory is the public handoff point for a memoryless Independent GPT reviewer. It routes the reviewer to repository-native authority and retained evidence without duplicating private Jules task controls or replacing the verified-core contracts.

## Recovery order

Recover current state from current merged `main` first. For the maintenance subject under review, use the most specific current repository authority. Dated audits, ledgers, corrections, and prior handoffs remain point-in-time evidence for their own windows.

At start record current date, default branch, exact `main` SHA, relevant open pull requests, active maintenance branches, recent merged changes, and checks actually executed. Do not treat a stale clone, prior handoff SHA, later path presence, or model recollection as current state.

## Repository map

1. `FOUNDATION/INDEX.md` and `FOUNDATION/ARCHITECTURE.md` for the current verified-core map and structure.
2. `FOUNDATION/EVIDENCE.md` for evidence semantics and `FOUNDATION/PROVENANCE.md` for source/version/producer/AI-use provenance.
3. `FOUNDATION/MAINTENANCE.md` for the canonical public maintenance contract.
4. `FOUNDATION/REVIEW.md` for non-operative reviewer-side disposition states.
5. Current schemas, tests, sources, tools, specs, and implementation under `FOUNDATION/` when subject-specific machine or execution evidence is required.
6. Current Daily / Weekly / Monthly research artifacts only as repository-visible cadence/evidence inputs; they are not default maintenance edit targets.
7. `historical-audits/INDEX.md` and referenced records for corrections, period audits, non-canonical sidecars, maintenance, and reconciliation history.
8. Git history and merged/open PR chronology when producer identity, canonical status, timing, overlap, or historical/current state is disputed.

## Task identity and idempotency

Treat a maintenance run as a tuple of repository, maintenance surface/task, logical period when applicable, producer, exact base revision, and run identifier when available.

Before writing:

- confirm fresh `main`;
- inspect overlapping open PRs and active maintenance branches;
- identify the owning maintenance/control file and direct synchronized projections;
- check whether the same logical repair already exists or has merged;
- refresh assumptions if `main` advances materially.

If another live PR/branch owns the same maintenance defect, surface, or period, use `COORDINATE` rather than creating a parallel repair. Never write merely to test whether writes are possible.

## Evidence boundaries

Keep claim state, evidence level, mapping state, implementation state, validation state, producer identity, execution evidence, review disposition, and maintenance-delivery state separate.

A source reference is not proof of local implementation. A validation result proves only the surface actually checked. A non-canonical sidecar does not become canonical merely because it exists or is newer. File presence does not prove a historical producer consumed it. Later success does not erase earlier failure. A correction does not rewrite history. Unknown remains unknown.

Native Jules records remain native Jules records. GPT or other substitute material retains its actual producer and canonical status. Independent GPT may calibrate maintenance interpretation and prepare a repair, but it does not reconstruct or expose private Jules prompts, repository memory, credentials, hidden reasoning, or unrelated operator context.

`FOUNDATION/REVIEW.md` and this recovery kernel have different jobs:

```text
review state != maintenance action
CALIBRATED != repair delivered
ACCEPTED_FOR_VERIFIED_CORE != merged
validator contract reviewed != validator executed
```

An unrun validator, test, command, or workflow is `NOT_EXECUTED`.

## History discipline

Historical artifacts are point-in-time evidence. Use dated correction or reconciliation records when a historical research artifact itself requires a forward correction; otherwise prefer correcting the current owning maintenance/control source.

Preserve failed, missing, provisional, blocked, non-canonical, insufficient-evidence, and unknown states. Archive relocation is not semantic replacement.

If historical execution, provenance, producer identity, or source status cannot be recovered from repository-visible evidence, keep it `UNKNOWN` rather than reconstructing it from later state.

## Maintenance outcome

Use one of these states when useful:

- `HEALTHY` — reviewed maintenance surface has no confirmed defect;
- `REPAIR` — a confirmed maintenance defect has a safe owning-file repair;
- `COORDINATE` — another live change owns the same surface or period;
- `BLOCKED` — authority, current state, or safe delivery cannot be established.

When no confirmed maintenance defect or drift exists, the action is `NO_CHANGE_REQUIRED`: no activity-only edit, branch, or PR.

If repair is justified, change only the owning current maintenance/control file(s) and direct synchronized projections. Research content, historical research, domain claim maps, source records, and implementation remain outside this kernel unless the current owning contract or maintainer explicitly makes them part of the repair.

## Delivery discipline

For a justified repair:

1. branch from exact fresh `main`;
2. make the bounded maintenance/control-plane change;
3. run only available targeted validation and preserve the real result;
4. refresh `main` and overlap state before delivery;
5. inspect the aggregate `main...branch` diff;
6. open one Draft PR;
7. stop for maintainer review.

Do not push directly to `main`, force-push history, auto-merge, or claim a validator/CI PASS that was not actually observed.

## Handoff minimum

A durable handoff should make it possible to recover:

- base `main` SHA and current delivery head;
- maintenance scope and owning files;
- relevant logical period if any;
- overlapping PR/branch state;
- review disposition when one exists;
- checks actually run and checks not run;
- confirmed defect or `NO_CHANGE_REQUIRED` basis;
- unresolved items and negative evidence;
- whether history and producer identity were preserved;
- whether the Draft PR is clean against current `main`.

No separate audit artifact is required merely to prove that review happened. Prefer correcting the owning maintenance source and using the Draft PR description as the delivery summary.

Final merge and doctrine authority remains with the maintainer.
