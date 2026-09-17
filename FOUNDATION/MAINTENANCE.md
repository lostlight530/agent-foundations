# Agent Foundations maintenance contract / 长期维护契约

Status: `CANONICAL_PUBLIC_MAINTENANCE_CONTRACT`

Effective: 2026-09-17

## Scope / 范围

This contract governs the verified-core maintenance/control plane: Jules-produced research inputs as repository evidence, verified-core admission, Independent Review, Independent GPT recovery/repair, cadence interpretation, validator/checker ownership, concurrency, and delivery discipline.

It does not by itself authorize changes to historical `docs/**`, domain claim maps, sources, schemas, runtime/dependency surfaces, `.github/**`, private Jules task controls, or generated research content. Those surfaces may be read as evidence and changed only when the current owning repository authority or maintainer explicitly makes them part of a repair.

本契约负责可验证核心的维护/控制平面：Jules 产出作为仓库证据、核心准入、独立审核、Independent GPT 恢复/修复、周期解释、验证器职责、并发和交付纪律。本契约不自动授权改写历史研究流或私有 Jules 控制。

## Research cadence and admission / 科研周期与准入

A Daily research chunk records source identity, version/date/authors, source surface, claims, and limitations. Weekly cascade/conflict audits identify inheritance, duplicate identities, contradiction, and status promotion. Monthly blueprints remain provisional until the natural month ends. A historical `docs/**` chunk does not enter the verified core merely because generation succeeded.

A 30-day provisional ledger may summarize 30 logical dates, but it is not a natural-month seal. Keep `MONTH_OPEN` until the final calendar date is retained or explicitly classified as missing after it becomes due.

Verified-core admission requires canonical source deduplication plus five independent axes: Claim State, Evidence Level, Mapping State, Implementation State, and Validation State. Paper truth does not imply mapping relevance; mapping does not imply implementation; implementation does not imply validation. `STATIC_CHECKED` is documentary structure evidence, not experimental reproduction.

Canonical source identity is based on stable identifiers such as normalized arXiv identity, not date or revisit. Version, submission date, authors, and inspected source surface must be checked independently. Abstract-only inspection is `ABSTRACT_SUPPORTED`; unverified theorem/formula text cannot be promoted. English and Chinese counterparts must carry equivalent five-axis states and limitations.

## Maintenance identity and concurrency / 维护身份与并发

A maintenance run is identified by repository, maintenance surface/task, logical period when applicable, producer, exact base `main` revision, and run identifier when one exists.

Before any write:

1. recover the default branch and fresh merged `main` SHA;
2. inspect relevant open pull requests and active maintenance branches;
3. identify the owning verified-core maintenance/control file and direct synchronized projections;
4. check whether the same logical repair already exists or has merged;
5. refresh assumptions if `main` advances materially.

If another live PR or branch owns the same maintenance surface or logical period, use `COORDINATE` instead of creating a parallel repair. Never create or mutate a branch merely to test write permission.

## Correction, authority, and history / 纠错、权威与历史

Preserve historical generated text. Use errata for factual metadata, reconciliation for cross-record conflict/duplication, and retirement for superseded identities. Authority order for verified-core claim interpretation remains: targeted erratum/reconciliation; `SOURCES.md`; `EVIDENCE.md`/`PROVENANCE.md`/`REVIEW.md`; domain verified-core claims; historical `docs/**` stream.

For maintenance/control-plane state, use current merged `main` and the most specific current owning contract before historical audit records, prior handoffs, or model recollection.

Legacy `CONCEPTUAL_MAPPING` maps to `DESIGN_ANALOGY`. Legacy implementation `EVIDENCE_INSUFFICIENT` maps to `NOT_IMPLEMENTED` or `REFERENCE_ONLY`; legacy test status maps to `NOT_TESTED`. Evidence level is assigned from source type and inspected surface, never guessed from a legacy label.

Historical record != current state. Current path presence != earlier execution. Later success != earlier success. Correction != history rewrite. Unknown remains unknown.

Jules-generated research remains historical/repository input and is not self-authenticating. The verified-core validator checks declared structural/documentary surfaces only. Independent Review calibrates interpretation. Independent GPT may recover maintenance state and prepare bounded repairs. A human maintainer reviews and merges.

Private Jules task prompts, repository memory, credentials, and hidden reasoning are not reconstructed into public repository files by default. This repository currently has no public `AGENTS.md`; do not infer one from private automation or prior conversations.

## Validator and execution boundary / 验证器与执行边界

`FOUNDATION/validate.py` and `FOUNDATION.test_contract` provide revision-scoped repository evidence only when actually executed.

Keep distinct:

```text
validator contract reviewed != validator executed
validator exited 0 != semantic truth
workflow file exists != workflow ran
current file exists != historical producer consumed it
```

An unrun validator, test, command, or workflow is `NOT_EXECUTED`. Do not convert document inspection into PASS.

## Independent maintenance decision / 独立维护判定

Use repository truth first:

- no confirmed maintenance defect or drift → `NO_CHANGE_REQUIRED`; no activity-only commit/branch/PR;
- confirmed maintenance defect with safe local ownership → `REPAIR`;
- overlapping live ownership → `COORDINATE`;
- missing authority, unrecoverable state, or unsafe delivery boundary → `BLOCKED`.

`HEALTHY` or `NO_CHANGE_REQUIRED` applies only to the reviewed maintenance surface and is not a universal correctness certificate.

## Delivery, rollback, and escalation / 交付、回滚与升级

For a justified maintenance repair:

1. branch from exact fresh `main`;
2. change only the owning maintenance/control file(s) and direct synchronized projections;
3. preserve failed, missing, provisional, blocked, non-canonical, insufficient-evidence, and unknown states;
4. run available targeted validation supported by the actual environment;
5. refresh current `main` and overlap state before delivery;
6. inspect the aggregate `main...branch` diff;
7. open one Draft PR and stop for maintainer review.

Done requires unique source identity where relevant, complete five-axis state where admission is in scope, bilingual equivalence where affected, aligned authority links, retained conflicts, a clean aggregate maintenance diff, actual validation results for checks that ran, and explicit `NOT_EXECUTED` for checks that did not.

Do not push directly to `main`, rewrite history, force-push, auto-merge, or silently promote generated research into verified-core knowledge.

Revert the maintenance commit if validation or authority links regress. Escalate unresolved identity, author/version conflict, semantic translation mismatch, status promotion, overlapping ownership, or unsafe delivery to human review.

Final doctrine and merge authority remains with the maintainer.
