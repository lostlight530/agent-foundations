# Agent Foundations — Verified Core / 可验证核心

Status: repository documentary/evidence core  
Current calibration: 2026-11-15 (repository-source and documentary authority only)

`FOUNDATION/**` is the long-lived theory, evidence, provenance, and architecture core of Agent Foundations. The repository is **not** an implemented autonomous-agent runtime.

The verified core exists to keep four things separable and inspectable:

```text
theory / architecture claim
+ external source identity
+ repository implementation state
+ repository validation state
```

External equations, papers, protocol mappings, pseudocode, and architecture analogies remain external/reference claims unless a concrete repository artifact implements the behavior.

## November 2026 overview — one core, four bounded subjects / 11 月总论

At the inspected `main` revision `608bf59eb503effdf211aa2f9b448f24d3ede0dc`, this repository has **23 canonical domain claims** (6 Architecture, 5 Memory, 6 Tools, 6 Collaboration), indexed under stable `AF-*` IDs, and **67 distinct, contiguous registered source identifiers S01–S67** in `SOURCES.md` — these are documentary inventory counts, **not** counts of validated agent capabilities, reproduced papers or independent tests

| Current subject owner | Unit of analysis | Core falsification boundary | Local implementation state |
| --- | --- | --- | --- |
| `ARCHITECTURE.md` | Configured model, harness, tools, authority, memory, environment and evaluator as one agent system | Theorem scope or model ID does not prove system-wide safety and reproducibility | Documentary claims and validator only, no autonomous runtime |
| `MEMORY.md` | Source-bound memory object, authenticated role, lifecycle, compaction and retention | Content-preserving summaries can lose origin and authorization | No ingestion, compaction or cross-session memory service |
| `TOOLS.md` | Action-specific authority, target and arguments, invocation, sink-side effect and reconciliation | Available tool or successful request does not establish valid authorization or completed effect | No executor, sandbox or permission broker |
| `COLLABORATION.md` | Typed agreement subject, topology, delivery/failure model, external factuality check | Agent agreement is not a truth oracle or proof of replicated-state convergence | No multi-agent transport or consensus implementation |

The recommended **general-to-specific** reading order is: this index → `EVIDENCE.md` + `SOURCES.md` + `PROVENANCE.md` → domain-specific `AF-*` Claim maps → historical/theoretical English/Chinese long-form discussions in `docs/en` and `docs/zh`, with current-reading guides in [English](../docs/en/README.md) and [中文](../docs/zh/README.md)

The five dimensions **Claim State / Evidence Level / Mapping State / Implementation State / Validation State** remain independent, including when prose makes a mathematically strong-sounding claim, a paper supplies a bound, or bilingual passages repeat one proposition

**Source identity warning:** `SOURCES.md` documents a historical `S63` collision between two different scholarly objects, so historical `S63` alone is insufficient for identification, resolve by arXiv identifier, title, version and source/provenance record, do not silently allocate or alias a source ID

**Evidence boundary:** repository source and text inspected, external theorem verification `NOT_REVERIFIED`, new runtime experiments and full validator command `NOT_EXECUTED` in this revision, no periodical record or delivery mechanism is used to infer domain correctness

## Domain maps / 领域知识图

These files carry the repository's durable subject-matter claims:

- [ARCHITECTURE.md](./ARCHITECTURE.md) — system boundary, evaluation, governed policies, theorem scope, release reconstruction.
- [MEMORY.md](./MEMORY.md) — memory selection, provenance, retrieval, compaction, retention, correction, and deletion boundaries.
- [TOOLS.md](./TOOLS.md) — per-action authority, tool input/output boundaries, observability, idempotency, recovery, and untrusted-input handling.
- [COLLABORATION.md](./COLLABORATION.md) — coordination topology, failure propagation, message contracts, preserved trajectories, and consensus limits.

Stable Claim IDs use `AF-ARCH-*`, `AF-MEM-*`, `AF-TOOL-*`, and `AF-COLLAB-*`.

A domain document may contain `SUPPORTED`, `PROPOSED`, or other claim states side by side. File presence is not a blanket endorsement of every mechanism described in the file.

## Evidence and source core / 证据与来源核心

- [EVIDENCE.md](./EVIDENCE.md) defines claim state, evidence level, mapping state, implementation state, validation state, and admission rules.
- [SOURCES.md](./SOURCES.md) is the canonical `Sxx` external-source registry.
- [PROVENANCE.md](./PROVENANCE.md) defines source/version/producer/revision/correction/publication provenance.
- [claim.schema.json](./claim.schema.json) defines the machine-readable claim vocabulary.

The exact current source-ID range is recovered from current `main`; an old audit cutoff must not be frozen into a current count.

Keep these distinctions explicit:

```text
source registered != claim supported
claim supported != repository implementation
repository implementation != validation complete
repository publication DOI != external scientific source
validator definition != validator execution
```

## Repository validation helpers / 仓库验证辅助

`validate.py` checks structural/documentary properties declared by its implementation: required verified-core files, Claim IDs/metadata, source references, schema structure, restricted overclaim phrases, action-reference pin form, and protected paths when a comparison base is supplied.

`arxiv_probe.py` supports bibliographic identity and submission-history checks.

Neither helper proves theorem meaning, mathematical correctness, experimental reproduction, semantic truth, or autonomous-agent behavior.

When validation is claimed, retain exact revision, command, environment, exit status, and relevant output. An unrun checker is `NOT_EXECUTED`.

## Review and maintenance layer / 评审与维护层

Repository knowledge and repository maintenance are related but distinct:

- [REVIEW.md](./REVIEW.md) — review disposition vocabulary; review state is not a repository mutation.
- [MAINTENANCE.md](./MAINTENANCE.md) — public maintenance/control contract for the verified core.
- [independent-gpt/README.md](./independent-gpt/README.md) — memoryless maintenance recovery and bounded delivery guidance.

These files describe how the core is maintained. They do not redefine the scientific/theoretical meaning of the domain documents above.

```text
research generation != verified-core admission
verified-core admission != implementation
review state != maintenance action
maintenance action != scientific evidence
```

## Generated and historical material / 生成与历史材料

`docs/en/**` and `docs/zh/**` preserve the broader bilingual generated research stream. `historical-audits/**` preserves point-in-time corrections, reconciliations, document audits, and evidence/closure ledgers.

Those materials remain useful evidence inputs and historical records. They do not outrank the current canonical source registry and verified-core claim documents, and later correction does not pretend the original text never existed.

## Scholarly publication identity / 学术软件出版身份

Agent Foundations has a public software publication DOI: `10.5281/zenodo.22791169`, publication date 2026-09-16.

That DOI identifies an archived publication object. It is not an `Sxx` external source, does not independently support an `AF-*` claim, does not prove validator execution, and does not make a later `main` revision semantically identical to the archive.

Use `CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` for repository publication/citation metadata; use `SOURCES.md` for external scientific/source identity.

## Current authority precedence / 当前解释优先级

For verified-core claim interpretation:

1. current repository implementation when an implementation claim is made;
2. explicit current erratum/reconciliation for the affected source/claim;
3. canonical source identity in `SOURCES.md` and exact checked source version/surface;
4. `EVIDENCE.md` and `PROVENANCE.md` semantics;
5. the owning domain claim document;
6. generated/historical material for point-in-time context.

For maintenance state, use current merged repository truth and the most specific current maintenance/review contract. Maintenance precedence changes current interpretation or delivery behavior only; it does not rewrite research history.

## Recommended reading order / 推荐阅读顺序

For the repository's subject matter:

1. [EVIDENCE.md](./EVIDENCE.md)
2. [ARCHITECTURE.md](./ARCHITECTURE.md)
3. [MEMORY.md](./MEMORY.md)
4. [TOOLS.md](./TOOLS.md)
5. [COLLABORATION.md](./COLLABORATION.md)
6. [SOURCES.md](./SOURCES.md)
7. [PROVENANCE.md](./PROVENANCE.md)

For review/maintenance work, continue with [REVIEW.md](./REVIEW.md), [MAINTENANCE.md](./MAINTENANCE.md), and the independent recovery guide only as needed.

## Repository-wide implementation classification

Strongest supported repository-wide statement:

`DOCUMENTARY_AGENT_FOUNDATION_WITH_STRUCTURED_EVIDENCE_AND_PROVENANCE_SUPPORT`

Not:

`IMPLEMENTED_AUTONOMOUS_AGENT_RUNTIME`

Historical period-closure labels remain authoritative only for their recorded windows. Current state is recovered from current repository truth, not copied from an older cutoff.


## 2026-10-04 special verified-core closeout

The Collaboration domain now includes `AF-COLLAB-006`, a bounded S57-backed claim that keeps consensus/agreement separate from factual correctness.

Current documentary disposition:

```text
S57
→ AF-COLLAB-006
→ SUPPORTED
→ E4_PREPRINT
→ COUNTEREVIDENCE
→ REFERENCE_ONLY
→ NOT_TESTED
```

This is a verified-core documentary admission, not an autonomous-agent runtime expansion.

## 2026-11-15 domain-depth cross-reading note

The existing domain Claim IDs and source registry remain authoritative. Current professional-document expansion makes each area’s key **counterexample** explicit, without reclassifying literature as local behavior:

- **Architecture:** model ID does not identify a complete agent system; runtime configuration and evaluation setup are part of the evaluated object.
- **Memory:** content-preserving compression can lose authenticated role and provenance; text fidelity is not authority fidelity.
- **Tools:** tool availability, approval, attempted invocation and independently verified side effect are different states.
- **Collaboration:** agreement between participants, replicated-state convergence and independently established factual correctness are different propositions.

The broader bilingual `docs/en/**` and `docs/zh/**` contain historical research formulations and illustrative pseudo-code. For present five-axis interpretation, read these sections against their corresponding canonical `FOUNDATION/{ARCHITECTURE,MEMORY,TOOLS,COLLABORATION}.md` claim maps, `SOURCES.md`, `EVIDENCE.md` and `PROVENANCE.md`. This is a domain research clarification, not a new autonomous runtime, new source identity, or validation execution.
