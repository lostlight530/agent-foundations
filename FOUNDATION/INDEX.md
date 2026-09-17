# Agent Foundations — Verified Core / 可验证核心

Status: repository documentary/evidence core  
Current calibration: 2026-09-17

Current maintenance authority: [MAINTENANCE.md](./MAINTENANCE.md)  
Independent review vocabulary: [REVIEW.md](./REVIEW.md)  
Memoryless maintenance recovery: [independent-gpt/README.md](./independent-gpt/README.md)

## Purpose / 目的

`FOUNDATION/**` is the compact evidence, provenance, review, and maintenance core of Agent Foundations.

The repository is primarily a theory, evidence, and documentary architecture base. It is **not** an implemented autonomous-agent runtime.

External equations, papers, protocol mappings, pseudocode, and architecture analogies remain external/reference claims unless a concrete repository artifact implements the behavior.

## Repository realization map / 仓库真实结构映射

### 1. Domain claim maps / 领域声明

- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [MEMORY.md](./MEMORY.md)
- [TOOLS.md](./TOOLS.md)
- [COLLABORATION.md](./COLLABORATION.md)

Stable claim IDs use `AF-ARCH-*`, `AF-MEM-*`, `AF-TOOL-*`, and `AF-COLLAB-*`.

### 2. Canonical source registry / 来源登记

[SOURCES.md](./SOURCES.md) is the canonical source registry. The exact current source-ID range is recovered from current `main`; do not reuse an old audit cutoff as a current count.

Source IDs are identities, not a daily counter. The same canonical source must not be re-registered under another ID merely because a later research chunk revisits it or cites another version.

Historical duplicate/revisit cases remain point-in-time examples and do not replace current registry inspection.

### 3. Claim vocabulary / Claim 词汇契约

[claim.schema.json](./claim.schema.json) defines the machine-readable claim vocabulary for state, evidence class, mapping, implementation, validation, sources, scope, and limitations.

Schema structure does not prove claim semantics.

### 4. Repository validator / 仓库验证器

`validate.py` checks structural/documentary properties declared by the current implementation, including required verified-core files, Claim IDs/metadata, canonical source registration and references, restricted overclaim phrases, workflow action-reference pin form, protected paths with an explicit comparison base, and basic claim-schema properties.

Important boundary:

`validate.py` does **not** prove theorem meaning, formula transcription, exact version date, translation equivalence, experimental reproduction, semantic truth, or agent behavior.

`STRUCTURAL_VALIDATOR_PRESENT != VALIDATOR_EXECUTED != CLAIM_SEMANTICS_VERIFIED`.

When validation is claimed, retain the exact revision, command, environment, exit status, and relevant output. An unrun validator is `NOT_EXECUTED`.

### 5. arXiv provenance helper / arXiv 溯源辅助

[arxiv_probe.py](./arxiv_probe.py) supports bibliographic identity and submission-history checks. It does not certify theorem content or experiments.

### 6. Evidence, provenance, review, maintenance, and independent recovery

- [EVIDENCE.md](./EVIDENCE.md) — evidence and five-axis admission semantics.
- [PROVENANCE.md](./PROVENANCE.md) — source/version/producer/temporal/correction/AI-use provenance.
- [REVIEW.md](./REVIEW.md) — non-operative review disposition states.
- [MAINTENANCE.md](./MAINTENANCE.md) — canonical public maintenance/control-plane contract.
- [independent-gpt/README.md](./independent-gpt/README.md) — public cold-start recovery, bounded repair, and Draft-PR delivery kernel.

These roles are distinct:

```text
research generation != verified-core admission
review state != maintenance action
validator definition != validator execution
Independent GPT != private Jules task control
```

### 7. Historical generated research / 历史研究

`docs/en/**` and `docs/zh/**` preserve the broader bilingual SOP-generated research stream.

Historical Daily Research Chunks remain evidence of what was generated/recorded at that time. Later reconciliation can correct source identity, author metadata, scope, or mapping without pretending the original text never existed.

Historical research is an evidence input to maintenance/review, not a default maintenance edit target.

### 8. Historical corrections and ledgers / 历史纠错与总账

`historical-audits/**` preserves point-in-time corrections, reconciliations, document audits, and period/evidence ledgers. Read the relevant record when historical interpretation matters, but recover current maintenance state from current merged `main` and current owning contracts.

## Current authority precedence / 当前解释优先级

For verified-core claim interpretation, when historical generated research conflicts with stronger current evidence:

1. explicit erratum/reconciliation for the affected source/claim;
2. current canonical source identity in `SOURCES.md`;
3. `EVIDENCE.md`, `PROVENANCE.md`, `REVIEW.md`;
4. domain claim maps;
5. original generated bilingual material for historical context.

For maintenance/control-plane state:

```text
current merged main / repository facts
> most specific current owning contract
> FOUNDATION/MAINTENANCE.md
> verified revision-matched execution evidence
> current review/provenance interpretation
> historical audits / prior handoffs / model recollection
```

This precedence changes current interpretation only; it does not rewrite history.

## Maintenance recovery and delivery / 维护恢复与交付

A maintenance reviewer starts from fresh `main`, inspects live PR/branch ownership, identifies the owning control surface, and uses:

- `NO_CHANGE_REQUIRED` when no maintenance defect is confirmed;
- `REPAIR` for a bounded owning-file repair;
- `COORDINATE` for overlapping live ownership;
- `BLOCKED` when authority/current state/safe delivery cannot be established.

A justified repair records actual validation, marks unrun checks `NOT_EXECUTED`, reviews the aggregate `main...branch` diff, opens one Draft PR, and stops for maintainer review.

Private Jules prompts, repository memory, credentials, or hidden reasoning are not reconstructed into public control files by default. This repository currently has no public `AGENTS.md`.

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md)
2. [ARCHITECTURE.md](./ARCHITECTURE.md)
3. [MEMORY.md](./MEMORY.md)
4. [TOOLS.md](./TOOLS.md)
5. [COLLABORATION.md](./COLLABORATION.md)
6. [SOURCES.md](./SOURCES.md)
7. [PROVENANCE.md](./PROVENANCE.md)
8. [REVIEW.md](./REVIEW.md)
9. [MAINTENANCE.md](./MAINTENANCE.md) for maintenance policy
10. [independent-gpt/README.md](./independent-gpt/README.md) for memoryless maintenance recovery/delivery
11. relevant historical corrections/ledgers only when their time window is needed

## Repository-wide implementation classification

Strongest supported repository-wide statement:

`DOCUMENTARY_AGENT_FOUNDATION_WITH_STRUCTURED_EVIDENCE_AND_PROVENANCE_SUPPORT`.

Not:

`IMPLEMENTED_AUTONOMOUS_AGENT_RUNTIME`.

Historical period-closure labels remain authority for their own recorded windows. Current September cadence state must be recovered from current repository evidence rather than copied from an older cutoff.

Final doctrine and merge authority remains with the maintainer.
