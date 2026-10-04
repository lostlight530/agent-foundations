# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, research-production method, scholarly-metadata boundaries, and semantic-drift governance

## Language policy / 语言政策

English is the canonical and default language for this open-research contract. Chinese text is provided as an accessibility and interpretation aid. If wording diverges, the English normative text governs; repository evidence and current owning contracts remain authoritative over both.

英文是本开放科研契约的默认与规范语言；中文用于辅助理解与可访问性。若中英文表述有差异，以英文规范文本为准；仓库事实与当前 owning contract 的权威仍高于任何翻译。


## Authority

This guide does not replace the verified core, evidence vocabulary, provenance rules, implementation-status rules, validation-status rules, maintenance, release, or historical research.

```text
current repository truth
→ FOUNDATION verified core / evidence / provenance contracts
→ OPEN_RESEARCH.md
→ RESEARCH_TEMPLATE.md
→ prospective research records
→ scholarly metadata / downstream indexes
```

A stricter repository-native contract wins.

## Canonical positioning

**Canonical Type:** Bilingual foundational agent-systems research and evidence framework

**One-line positioning:** Bilingual theory, evidence, and architecture-decision foundation for reasoning about AI agent systems with explicit claim, implementation, and validation boundaries

**Primary domains:** agent systems; agent architecture; knowledge representation; epistemology; AI evaluation

**Non-goals:** building foundation; physical-action theory; implemented general agent runtime; autonomous research system; proof that cited mechanisms are locally implemented

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Scholarly Graph Representation != Repository Self-Definition
```

## Research scope and workflows / 科研范围与工作流

Repository positioning follows its declared purpose, implemented or studied research objects, and applicable public contracts. Existing canonical positioning remains unchanged.

Repository-owned workflows may implement research methods and produce bounded observations. Their substantive research role remains intact; the execution mechanism alone does not establish a research domain or scientific validity.

仓库现有定位保持不变；自有工作流的科研作用保留，执行机制本身不构成研究领域或科学有效性的证明

## Research-production method

The shared ten-repository epistemic skeleton requires recoverable question, falsifiability, evidence/source identity, fixed object/revision identity, procedure actually executed or inspected, raw observation, counterexample, bounded conclusion, research increment, and retest condition.

Agent Foundations additionally keeps claim state, evidence level, architecture mapping, implementation status, and validation status distinct. Citation presence or conceptual mapping does not imply local implementation or reproduction.

## Repository-specific method

Every claim-oriented research unit should preserve the five axes when applicable
- Claim State
- Evidence Level
- Mapping State
- Implementation Status
- Validation Status

Also record supported proposition, assumptions, limitations, counterevidence, source identity, and admission decision

Use `FOUNDATION/EVIDENCE.md` as the detailed evidence vocabulary

Bilingual presentation does not relax claim/evidence requirements. Translation agreement is not scientific validation.

## Evidence and execution discipline

```text
canonical source != reproduced result
claim support != implementation
implementation != validation
conceptual mapping != runtime evidence
AI assistance != evidence
```

Unknown and untested states stay explicit. External sources remain independently identified from repository publication metadata.

## Open-science file responsibilities

- `README.md` — public orientation and stable entry points.
- `OPEN_RESEARCH.md` — durable open-research method and positioning.
- `RESEARCH_TEMPLATE.md` — prospective bounded research records.
- `AUTHORS`, `LICENSE`, `CITATION.cff`, `codemeta.json` — authorship, reuse, citation/software metadata.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` — contribution/community/security governance.
- `RELEASE_POLICY.md` — release/archive semantics.
- `.github/ISSUE_TEMPLATE/**` and pull-request template — reviewable intake.

These support open research; they do not create claim support or reproduction evidence.

## Scholarly metadata discipline

Preserve Canonical Type, One-line Positioning, Primary Domains, Non-goals, accurate structured subjects where supported, and 5–7 defining keywords before future metadata publication. Avoid vendor keyword stuffing or classifier-facing marketing copy.

## Shadow classification

Candidate title + abstract/description may be checked against downstream topic/keyword inference.

```text
ALIGNED
PARTIALLY_ALIGNED
MISCLASSIFIED
CLASSIFIER_NOISE
```

Execution state is separately `RUN` or `NOT_RUN`. Repair owning metadata only for genuine upstream ambiguity; otherwise record classifier noise.

## Semantic drift audit

Compare canonical positioning with `CITATION.cff`, CodeMeta, archive/DOI metadata, OpenAIRE, and OpenAlex representations.

- **CANONICAL_DRIFT**
- **TRANSPORT_DRIFT**
- **DERIVATION_DRIFT**
- **VERSION_SKEW**

`DERIVATION_DRIFT != REPOSITORY_DEFECT`.

## History and correction

```text
CURRENT_STATE != TASK_TIME_STATE
LATER_SUCCESS != EARLIER_SUCCESS
PUBLICATION_IDENTITY != CURRENT_MAIN
RESEARCH_PRODUCTION != MAINTENANCE != PERIODIC_AUDIT
```

Preserve earlier claim/evidence states. Correct current interpretation through explicit correction, reconciliation, or a new timepoint record.

## Contribution and review

Use `OPEN_RESEARCH.md` for method/positioning changes and `RESEARCH_TEMPLATE.md` for new bounded research records. Preserve the repository's claim/evidence/mapping/implementation/validation axes and state exactly what was inspected, executed, reproduced, or left untested.

## Permanent boundary

```text
research record != capability claim
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
external indexing != repository self-definition
```


## 中文摘要

本文件定义仓库长期开放科研方法，而不是替代现有 verified core、research/artifact contract、maintenance contract 或历史记录。共同科研骨架要求：研究问题、可证伪假设、证据/来源身份、固定对象/版本/环境、实际执行程序、原始观测、反例检查、有界结论、研究增量与复验条件。

仓库自身的实现、证据、provenance、artifact/claim contract 与历史记录继续拥有原生 authority。外部 scholarly graph 或分类系统只能派生表示，不能反向成为 repository identity。

未来 scholarly metadata 应保持 canonical type、one-line positioning、primary domains、non-goals、少量准确 subjects 与 5–7 个定义性 keywords；若外部分类漂移，先修真实 upstream ambiguity，否则记录 classifier noise。
