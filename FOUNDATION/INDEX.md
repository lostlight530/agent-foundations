# Agent Foundations — Verified Core / 可验证核心

Status: repository documentary/evidence core  
Current calibration: 2026-08-30

Current maintenance authority: [MAINTENANCE.md](./MAINTENANCE.md)

August 1–30 evidence ledger: [../docs/AUGUST_2026_01_30_EVIDENCE_LEDGER.md](../docs/AUGUST_2026_01_30_EVIDENCE_LEDGER.md)

Full public-document audit: [2026-08-28-DOCUMENT-AUDIT.md](./2026-08-28-DOCUMENT-AUDIT.md)

## Purpose / 目的

`FOUNDATION/**` is the compact evidence and architecture core of Agent Foundations.

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

[SOURCES.md](./SOURCES.md) is the canonical source registry and currently contains the contiguous range `S01–S37`.

Source IDs are identities, not a daily counter. The same canonical source must not be re-registered under another ID merely because a later research chunk revisits it or cites another version.

August reference cases: the 2026-08-27 RAFA revisit resolves to S10; the 2026-08-29 MATS revisit resolves to S25. S36 and S37 are distinct new identities.

### 3. Claim vocabulary / Claim 词汇契约

[claim.schema.json](./claim.schema.json) defines the machine-readable claim vocabulary for state, evidence class, mapping, implementation, validation, sources, scope, and limitations.

Schema structure does not prove claim semantics.

### 4. Repository validator / 仓库验证器

`validate.py` currently checks structural/documentary properties including:

- required verified-core files
- stable/unique Claim IDs and required metadata labels
- source IDs form a contiguous range from S01 through the current highest source ID
- each registered source exposes a canonical Identifier or URL identity
- duplicate canonical source identities are rejected, including arXiv version/revisit duplicates
- Claim source references resolve to registered IDs
- restricted absolute-overclaim phrases
- existing workflow action-reference pin form
- protected-path changes when an explicit comparison base is supplied
- basic `claim.schema.json` properties

Important boundary:

`validate.py` does **not** parse every Markdown Claim into a JSON object and enforce all schema semantics. It also does not verify theorem meaning, formula transcription, exact version date, translation equivalence, experimental reproduction, or agent behavior.

`STRUCTURAL_VALIDATOR_PRESENT != CLAIM_SEMANTICS_VERIFIED`.

### 5. arXiv provenance helper / arXiv 溯源辅助

[arxiv_probe.py](./arxiv_probe.py) supports bibliographic identity and submission-history checks. It does not certify theorem content or experiments.

### 6. Evidence, provenance, and review semantics

- [EVIDENCE.md](./EVIDENCE.md)
- [PROVENANCE.md](./PROVENANCE.md)
- [REVIEW.md](./REVIEW.md)

These are documentary interpretation surfaces, not execution engines.

### 7. Historical generated research / 历史研究

`docs/en/**` and `docs/zh/**` preserve broader bilingual research history.

Historical Daily Research Chunks remain evidence of what was generated/recorded at that time. Later reconciliation can correct source identity, author metadata, scope, or mapping without pretending the original text never existed.

### 8. Explicit August corrections / 8 月显式纠错

- [`../docs/AUGUST_2026_W33_ERRATA.md`](../docs/AUGUST_2026_W33_ERRATA.md)
- [`../docs/AUGUST_2026_W34_ERRATA.md`](../docs/AUGUST_2026_W34_ERRATA.md)
- [`../docs/AUGUST_2026_24_27_RECONCILIATION.md`](../docs/AUGUST_2026_24_27_RECONCILIATION.md)
- [`../docs/monthly/2026-08-through-27-strategic-blueprint.md`](../docs/monthly/2026-08-through-27-strategic-blueprint.md)
- [`../docs/AUGUST_2026_01_30_EVIDENCE_LEDGER.md`](../docs/AUGUST_2026_01_30_EVIDENCE_LEDGER.md)
- [`../docs/monthly/2026-08-through-30-strategic-blueprint.md`](../docs/monthly/2026-08-through-30-strategic-blueprint.md)

## Current authority precedence / 当前解释优先级

When historical generated research conflicts with stronger current evidence:

1. explicit erratum/reconciliation for the affected source/claim
2. current canonical source identity in `SOURCES.md`
3. `EVIDENCE.md`, `PROVENANCE.md`, `REVIEW.md`
4. domain claim maps
5. original generated bilingual material for historical context

This precedence changes current interpretation only.

## Reading order / 阅读顺序

1. [EVIDENCE.md](./EVIDENCE.md)
2. [ARCHITECTURE.md](./ARCHITECTURE.md)
3. [MEMORY.md](./MEMORY.md)
4. [TOOLS.md](./TOOLS.md)
5. [COLLABORATION.md](./COLLABORATION.md)
6. [SOURCES.md](./SOURCES.md)
7. [PROVENANCE.md](./PROVENANCE.md)
8. [REVIEW.md](./REVIEW.md)
9. August reconciliation/stage synthesis when historical correction is relevant

## Repository-wide implementation classification

Strongest supported repository-wide statement:

`DOCUMENTARY_AGENT_FOUNDATION_WITH_STRUCTURED_EVIDENCE_AND_PROVENANCE_SUPPORT`.

Not:

`IMPLEMENTED_AUTONOMOUS_AGENT_RUNTIME`.

Formal August monthly closure remains `OPEN` at the 2026-08-30 cutoff.
