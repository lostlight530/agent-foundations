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

## Public-release privacy preflight — 2026-10-26

This is a publication-safety procedure for Independent GPT maintenance handoffs, not a new research producer, runtime gate, or permission to disclose private control text.

1. **Allowlist:** publish only repository-visible task/cadence identity, Git refs, non-sensitive file scope, scoped findings, bounded validation results, risks, rollback, conflicts, and explicit unknowns. A public rule may state the boundary without reproducing the private instruction behind it.
2. **Inspect outgoing surfaces before publication:** check the complete `main...branch` diff and proposed PR title/body/comments, linked issues, generated reports/attachments and quoted Action logs for sensitive content. Review incoming third-party snippets before propagating them. Searching for terms such as `private memory` is only a lead, not proof of disclosure; a passing pattern scan is not a clean-history certificate.
3. **Withhold private material:** never copy credentials, tokens, session values, private prompts, private agent memory, hidden reasoning, personal or private operator details, nonpublic URLs, or off-repository confidential SOP/source text. Do not include suspect values, reversible redactions, or secret-derived fingerprints in public diagnosis, tests, screenshots or receipts.
4. **Fail closed:** if identity or publication authorization is uncertain, stop the affected write/PR/log publication; report `PUBLICATION_BLOCKED_PRIVATE_MATERIAL` using category and affected public-surface type only, with no value or private-text excerpt. Coordinate privately with the authorized maintainer; a missing or unexecuted check remains `NOT_EXECUTED`.
5. **If exposure is confirmed:** do not assume a later edit or PR close removes Git history, caches, forks or logs. Escalate privately, contain distribution, revoke/rotate affected credentials where applicable, and arrange platform-appropriate remediation with the maintainer. Preserve only non-sensitive incident/correction evidence, not the exposed payload.

This preflight does not establish that all repository history was scanned, any secret was found, or a private scheduler was shut down. Historical producer provenance and sealed research/maintenance artifacts retain their original identity.

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

## 2026-11-11 scoped independent A1/A2 effective-PR acceptance

For the 2026-11-01..11 evidence window see the [dated original PR acceptance reconciliation](../../historical-audits/2026-11/2026-11-11-a1a2-effective-pr-acceptance-reconciliation.md). This is a forward interpretation correction, not a rewrite of original PR history, bilingual native research, or periodic audit.

- Independent A1: complete applicable MonthStart..N−1 coverage, verified evidence/source/provenance custody and explicit per-file dispositions, including justified NO_FOLLOW_UP.
- Independent A2: original A1 must already be merged and reread on fresh main, followed by complete MonthStart..N bilingual/theory/source/effect relationship maintenance.
- Real per-file evidence identities, exact source paths/blob SHAs, claim-to-evidence bounds, bilingual correspondence decisions, relationship continuity, admissible inheritance, unknowns and counterexamples are meaningful maintenance content.
- Original PR additions >=100 is checked for each final merged original PR independently; never combine successor, correction, Native, Periodic Audit or other repository additions.
- A valid 100-line maintenance diff does not require 100 new scientific discoveries; neither may mechanically copied filler or fictional execution inflate the count.
- Keep DELIVERY_MERGED, NUMERIC_GATE, COVERAGE, SEMANTIC_QUALITY, BILINGUAL_CONSISTENCY, NATIVE_EXECUTION, TESTS_EXECUTED and MAIN_RETENTION distinct.
- An initial Draft NOT_MET is not necessarily the final source-reviewed original head; an author's PASS_SELF_QA is not independent Human Review.
- When the original additions are <100, retain NUMERIC_NOT_MET while acknowledging the actual bounded source maintenance; do not falsely say no work was delivered.
- Preserve all actual Native/PAC/effect verification gaps as PARTIAL/UNKNOWN/NOT_EXECUTED; GitHub merging does not establish live PAC shield enforcement.
- Nov02–11: 20/20 original independent PRs merged, 11 meet >=100 additions and nine are original numeric NOT_MET; these counts alone do not certify semantic quality.
- November and W46 remain OPEN at this cut, with W45 CLOSED; D7/D10 separate, future D14/D30 and natural month final NOT_DUE.

## Prospective ten-repository SOP vNext — repository-local execution bridge (2026-11-23)

This **prospective operating bridge** generalizes the dated November 11 acceptance clarification above to any legitimately due logical period. It is not a new Native task, periodic audit, independent review, scheduler, or retroactive PR verdict. Current merged `main` and current subject-specific Native/machine contracts remain authoritative.

### Cold-start, cadence, and evidence gates

1. Establish `repository / role / canonical task ID / logical period / timezone / cutoff / producer / run ID`. Distinguish Native, independent A1, independent A2, D7/D10/D14/D30, Governance, Correction, and Reconciliation.
2. Read exact latest `main`, owning contracts, canonical paths/blob SHAs, relevant open/Draft PRs and active overlaps, recent merged changes, dependencies, and revision-matched runner/Actions results. Historical summaries are dated evidence, not live state.
3. Determine Native Daily/Weekly/Monthly/Special/Stage eligibility under each repository's actual contract. Exclude not-yet-due periods from the missing-input denominator; keep `NOT_DUE`, `BLOCKED`, `UNKNOWN`, `NOT_EXECUTED`, `NOT_COMPUTED`, and legitimate negative results visible.
4. Do not equate a file, external source, PR merge, configured workflow, passing test, independent AI review, and human approval. Each is a separate evidence claim with its own version, producer, run and time boundary.

### Native → Independent A1 → Independent A2

5. Native output follows repository-owned IDs, dependencies and actual execution evidence. A governance note never substitutes for producer research, formal scanner, runtime, effect receipt, or source verification.
6. **Independent A1 = MonthStart → N−1**, not yesterday alone. Enumerate all applicable month-to-date Daily, Weekly, Monthly, Special and Stage inputs. For each file record canonical path/blob SHA, producer, upstream dependency, source/evidence/counterevidence, and a justified disposition (`NO_FOLLOW_UP`, `CORRECT_IN_PLACE`, `APPEND_RELATION`, `CONFLICT`, `UNKNOWN`, `NOT_DUE`).
7. Prior A1 source reviews may be inherited only when exact path/blob SHA and governing contract still match. Mark inherited and newly inspected coverage; correct only real defects and leave valid sources unchanged.
8. Each legitimate A1 run uses its own original PR. **A2 starts only after that original A1 PR is merged and reread from a fresh `main`**; pending Drafts, future successors and cleanup do not satisfy this dependency.
9. **Independent A2 = MonthStart → N**. Maintain the full month's unified source/evidence/relationship state, not only Day N. Identify supported `STRENGTHENED`, `WEAKENED`, `CHANGED`, `CONFLICT`, `INVALIDATED`, `INHERITED`, `UNKNOWN` transitions and their provenance/counterevidence.
10. Month-to-date A2 coverage is not Native Monthly `FINAL`; D7/D10/D14/D30 have separate legal windows, cutoffs, actual audit runs and original records. A partial-day audit remains partial even after PR merge.

### Original A1/A2 acceptance: seven independent axes

| Axis | Verification |
| --- | --- |
| `TASK_COMPLETENESS` | Applicable source denominator and per-file disposition |
| `NUMERIC_GATE` | Each **original A1/A2** PR's final merged GitHub additions ≥100 |
| `SEMANTIC_QUALITY` | True, necessary custody, source/decision/relation content; no filler |
| `DEPENDENCY` | Exact original A1 merge and fresh-main read for A2 |
| `DELIVERY` | Original PR number, final head SHA, merged status and merge SHA |
| `MAIN_RETENTION` | Current canonical path/blob/content checked independently |
| `EXECUTION_VALIDATION` | Only actually executed Native/checker/CI/reviewer evidence |

11. Numeric `≥100` is distinct from semantic quality and is **not** a requirement for 100 original scientific discoveries. Genuine source rows, SHA custody, justified no-change judgments, matrices and relationship updates can count; padding, invented science and fake runs cannot.
12. Evaluate the **same original PR at its final merged head**, not an earlier unfinished Draft. A numerically short but real delivery is `NUMERIC_NOT_MET`; reaching 100 lines with false content is not semantic PASS. Successor, cleanup, correction and reconciliation never backfill original additions.
13. Historical producer, failed run, PR and observation facts remain intact. Move interpretations forward through linked correction/reconciliation without altering the historical event or claiming unavailable evidence.
14. For real work: fresh isolated branch → minimal owning-file changes → actual validation and declared `NOT_EXECUTED` checks → whole `main...head` diff and public-safety review → one scoped Draft PR → concrete maintainer review/authorization → merge under repo rules → latest-main retention readback. Do not test permission with empty commits or copy private controls into public artifacts.
15. Every handoff records identity/period/cutoff, initial main SHA, owning contracts and source blob SHAs, producer/run evidence, counterevidence, checked/not-checked validation, original PR/final additions and semantic decision, approval/merge receipt, current-main retention and next legal trigger.
16. **Scope note:** an SOP governance PR implementing this bridge is **not** an original independent A1/A2 PR and is not required to meet their ≥100-additions numeric acceptance gate.

### Repository-specific Native ownership and non-transferable boundaries

- Foundations Native Daily research, Weekly evidence cascade and natural-month Monthly blueprint follow `FOUNDATION/INDEX.md`, `FOUNDATION/EVIDENCE.md`, `FOUNDATION/PROVENANCE.md`, and owned `docs/en/`/`docs/zh/` files. `CLAIM`, `EVIDENCE`, `MAPPING`, `IMPLEMENTATION`, `VALIDATION` are separate axes. A native Daily may modify a bilingual owner without a dated Daily filename; protect original producer attribution.
