# August 2026 W33 Source & Provenance Errata / 2026 年 8 月 W33 来源与溯源勘误

> Status: ACTIVE
>
> Evidence window: 2026-08-10 through 2026-08-16
>
> Calibration date: 2026-08-17

## Purpose / 目的

This file records source-identity, theorem-scope, formula-scope, and temporal-provenance corrections for historical W33 bilingual research.

Where it conflicts with bibliographic metadata, evidence-strength wording, theorem interpretation, or period attribution in the historical research, this erratum controls the **current interpretation** while preserving the original artifact as history.

本文件只记录可公开核验的来源、版本、定理范围与时间溯源事实。

---

## W33-ERRATA-01 — VPP v4 version/date pairing

Affected research:

- `docs/en/Collaboration_System.md` — `Variational Policy Propagation for Multi-Agent Reinforcement Learning`
- `docs/zh/Collaboration_System.md` — corresponding Chinese section

Historical metadata identifies:

- `arXiv:2004.08883v4`
- `Published: 2020-04-19T15:42:55Z`

Primary arXiv history distinguishes:

- v1: 2020-04-19
- v4: 2022-01-29

Current interpretation:

- paper identity: retained
- cited version: `v4`
- v4 date: `2022-01-29`
- `2020-04-19` is the v1 submission date and must not be presented as the v4 date
- the paper supports its local-neighbor reward assumption and MRF-form result under the paper's stated conditions
- architecture mapping remains conceptual/reference material
- repository implementation is not established by the paper

Primary source: https://arxiv.org/abs/2004.08883

---

## W33-ERRATA-02 — Fairness paper v4 version/date pairing and computational-bound scope

Affected research:

- `docs/en/Collaboration_System.md` — `Fairness and Efficiency Compatibility under Subadditive Valuations`
- `docs/zh/Collaboration_System.md` — corresponding Chinese section

Historical metadata identifies:

- `arXiv:2407.12461v4`
- `July 17, 2024`

Primary arXiv history distinguishes:

- v1: 2024-07-17
- v4: 2025-11-07

The historical W33 text also states that a polynomial-time algorithm computes an EF1 allocation with NSW at least approximately `1/2.08` times the **optimal** allocation.

That is too strong. The transformation guarantee is stated relative to an arbitrary **input allocation**, not directly relative to the unknown optimum.

A second issue exists within the checked primary v4 surfaces:

- the arXiv abstract states a transformation factor of `1/e^(2/e) ≈ 1/2.08` relative to the input allocation
- the rendered full-text Theorem 1.3 states `1/3` relative to the input allocation

Current interpretation:

- `2024-07-17` is the v1 date, not the v4 date
- v4 date: `2025-11-07`
- the existence theorem for a complete EF1 allocation with NSW at least `1/2` of optimal remains supported by the checked primary paper
- the polynomial-time transformation guarantee is relative to an arbitrary input allocation
- the exact checked v4 transformation coefficient remains `PRIMARY_SOURCE_INTERNAL_CONFLICT_REQUIRES_TEX_REVERIFICATION`
- a strong theorem/formula verification label is not supported for that disputed coefficient until the primary surfaces are reconciled
- repository implementation is not established by the paper

Primary source: https://arxiv.org/abs/2407.12461

---

## W33-ERRATA-03 — MAC-SQL v6 version/date pairing

Affected research:

- `docs/en/Tool_System.md`
- `docs/zh/Tool_System.md`

Historical metadata identifies:

- `arXiv:2312.11242v6`
- `Date: 2023-12-18`

Primary arXiv history distinguishes:

- v1: 2023-12-18
- v6: 2025-03-18

Current interpretation:

- paper identity: retained
- cited version: `v6`
- v6 date: `2025-03-18`
- `2023-12-18` is the v1 date and must not be presented as the v6 date

Primary source: https://arxiv.org/abs/2312.11242

---

## W33-ERRATA-04 — MAC-SQL equation is not a proved repository convergence/error bound

The historical W33 MAC-SQL research records the decomposer sequential-generation factorization:

$$
P_{\mathcal{M}}(\mathcal{Y} | \mathcal{Q}, \mathcal{S}^{'}, \mathcal{K}) = \prod_{j=1}^{L} P_{\mathcal{M}}(\mathcal{Y}^{j} | \mathcal{Y}^{<j}; \mathcal{Q}^{j}, \mathcal{S}^{'}, \mathcal{K})
$$

Current calibration:

- the equation supports the paper's decomposed sequential-generation formulation
- the paper supports the Decomposer + Selector + Refiner mechanism and reports empirical execution-accuracy results
- the equation is not, by itself, a theorem proving a numerical error-accumulation bound
- it is not a convergence theorem for Agent Foundations
- claims about reduced practical difficulty or error propagation should remain paper-attributed design rationale / empirical interpretation unless a specific formal theorem establishes a bound
- repository implementation is not established by the paper

Current evidence label:

`PAPER_MECHANISM_SUPPORTED / FORMAL_REPOSITORY_ERROR_BOUND_NOT_ESTABLISHED`

Primary source: https://arxiv.org/abs/2312.11242

---

## W33-ERRATA-05 — Robust decentralized bandit v2 version/date pairing

Affected research:

- `docs/en/Collaboration_System.md` — `Reputation-Based Validator Selection for Robust Consensus`
- `docs/zh/Collaboration_System.md` — corresponding Chinese section

Historical metadata identifies:

- `arXiv:2402.04417v2`
- `Submitted 2024-02-06`

Primary arXiv history distinguishes:

- v1: 2024-02-06
- v2: 2024-07-25

The primary abstract supports the bounded paper-level claims that the framework uses validators, digital-signature-based consensus, secure multi-party computation, UCB-style learning, and gives honest-participant regret bounded by `O(log T)` under its assumptions.

Current interpretation:

- `2024-02-06` is the v1 date, not the v2 date
- v2 date: `2024-07-25`
- security and regret statements remain conditional on the paper's model/assumptions
- long formulas in the historical research are not independently re-certified merely because paper identity and abstract-level results are supported
- architecture mapping remains conceptual unless separately implemented

Primary source: https://arxiv.org/abs/2402.04417

---

## W33-ERRATA-06 — W33 material was attached to a 2026-07 heading

Affected historical containers:

- `docs/en/Tool_System.md`
- `docs/zh/Tool_System.md`

MAC-SQL-specific W33 material was woven beneath the pre-existing heading:

`🔗 [Weekly Sync Report] 本周文档级联编织与动态冲突审计 2026-07`

This mixes two historical periods.

Current provenance:

- the pre-existing `2026-07` heading remains a July label
- the later MAC-SQL integration and associated W33 conclusions belong to `2026-W33`, not July
- those statements must not be cited as evidence of what the July research state observed
- physical document placement does not override temporal provenance

Current W33 record:

- integrated item: `MAC-SQL`
- target container: `Tool System`
- source: `arXiv:2312.11242v6`
- v6 date: `2025-03-18`
- paper mechanism: `SUPPORTED_FROM_PRIMARY_PAPER`
- formal repository error/convergence bound: `NOT_ESTABLISHED`
- repository implementation: `EVIDENCE_INSUFFICIENT`
- historical-period attribution: `2026-W33`

---

## W33-ERRATA-07 — Absolute-safety language remains non-authoritative

Historical Tool System prose contains an `unbreakable wall` / `100% safety` metaphor around a Control Barrier Function analogy.

Current interpretation:

- the metaphor is not an evidence-backed repository guarantee
- CBF-style guarantees are conditional on a specified model, dynamics, safety set, feasibility, and assumptions
- unmodeled hazards, implementation defects, observation errors, and out-of-scope conditions are not covered by the metaphor

Use:

`CONDITIONAL_FORMAL_BOUND_WITHIN_MODELED_ASSUMPTIONS`

not:

`UNIVERSAL_100_PERCENT_SAFETY`.

The historical prose remains visible; the stronger interpretation is retired.

---

## W33-ERRATA-08 — Repeated exact-version metadata defect

Several W33 research additions paired an explicit later arXiv version with the corresponding v1 date:

- `2004.08883v4` + v1 date
- `2407.12461v4` + v1 date
- `2312.11242v6` + v1 date
- `2402.04417v2` + v1 date

This is one recurring provenance defect class rather than four independent source facts.

A source-identity helper existing in the repository is not evidence that a historical research record used it. Current source identity must be judged from the evidence retained with the claim or from later explicit reconciliation.

Current verified-core interpretation:

- an explicit `vN` requires the date belonging to that exact version
- base identifier, v1 submission date, current version, and last-revised date are distinct fields
- `VERSION_DATE_PAIR_VERIFIED` is appropriate only when the exact pair is actually supported by primary submission history
- source identity verification remains separate from theorem/formula verification

Status:

`RECURRING_EXACT_VERSION_PROVENANCE_DEFECT / CURRENT_IDENTITY_RECONCILED`.

---

## W33 items checked without the same-class correction

The W33 review also inspected the identity/evidence boundaries of:

- `arXiv:2307.11044v1` — On the Convergence of Bounded Agents
- `arXiv:2412.20203v1` — No-regret learning in harmonic games
- `arXiv:2312.15549v1` — Finite-Time Frequentist Regret Bounds of Multi-Agent Thompson Sampling on Sparse Hypergraphs

The checked primary abstracts support the bounded research framing used by the historical chunks: bounded-agent convergence definitions; FTRL cycling versus extrapolated FTRL convergence with `O(1)` regret in harmonic games; and sublinear frequentist regret for epsilon-MATS on sufficiently sparse hypergraphs.

This does not certify every analogy, architecture mapping, long-form equation, or repository implementation claim.

---

## Precedence / 当前解释优先级

For the affected W33 material:

1. this erratum controls the explicit W33 corrections
2. current `FOUNDATION/SOURCES.md` controls exact source identity where registered
3. `FOUNDATION/PROVENANCE.md` controls source/version semantics
4. original bilingual research remains historical context

Historical content is not silently rewritten solely to make the original record appear correct.

## Final W33 provenance status

- bibliographic identity: `CALIBRATED`
- version-specific dates: `CORRECTED_WHERE_PRIMARY_HISTORY_CONFLICTED`
- fairness computational-bound claim: `SCOPED_TO_INPUT_ALLOCATION / EXACT_V4_COEFFICIENT_REQUIRES_TEX_REVERIFICATION`
- MAC-SQL formal-bound language: `PAPER_MECHANISM_SUPPORTED / FORMAL_REPOSITORY_ERROR_BOUND_NOT_ESTABLISHED`
- robust-bandit abstract-level result: `PRIMARY_SOURCE_SUPPORTED / LONG_FORMULA_NOT_RECERTIFIED`
- July/W33 period mixing: `EXPLICITLY_RECONCILED`
- repeated version/date defect: `RECONCILED_AS_ONE_PROVENANCE_FAILURE_CLASS`
- repository implementation boundary: `PRESERVED`
