# August 2026 W33 Source & Provenance Errata / 2026 年 8 月 W33 来源与溯源勘误

> Status: ACTIVE
>
> Audit window: 2026-08-10 through 2026-08-16
>
> Audit date: 2026-08-17
>
> Purpose: extend `docs/AUGUST_2026_SOURCE_ERRATA.md` with W33 corrections while preserving the original Jules-generated bilingual research history

This file is a newer primary-source correction for W33. Where it conflicts with bibliographic metadata, evidence-strength wording, or weekly provenance introduced during W33, this file takes precedence.

本文件延续已有 August Errata 的原则：保留历史生成内容，不静默改写；只对经一手来源核验的字段和明确越界的证据语义进行后验校准。

---

## W33-ERRATA-01 — VPP v4 version/date pairing

Affected W33 research chunk:

- `docs/en/Collaboration_System.md` — `Variational Policy Propagation for Multi-Agent Reinforcement Learning`
- `docs/zh/Collaboration_System.md` — corresponding Chinese section
- W33 integration: PR #111

Historical chunk identifies:

- `arXiv:2004.08883v4`
- `Published: 2020-04-19T15:42:55Z`

Primary arXiv history distinguishes:

- v1: 2020-04-19
- v4: 2022-01-29

Calibrated interpretation:

- paper identity: retained
- requested version: `v4`
- v4 date: `2022-01-29`
- `2020-04-19` is the v1 submission date and must not be presented as the v4 publication/submission date
- architecture mapping remains `CONCEPTUAL_MAPPING`
- repository implementation/test remain `EVIDENCE_INSUFFICIENT`

Primary source: https://arxiv.org/abs/2004.08883

---

## W33-ERRATA-02 — Fairness paper v4 version/date pairing

Affected W33 research chunk:

- `docs/en/Collaboration_System.md` — `Fairness and Efficiency Compatibility under Subadditive Valuations`
- `docs/zh/Collaboration_System.md` — corresponding Chinese section
- W33 integration: PR #113

Historical chunk identifies:

- `arXiv:2407.12461v4`
- `July 17, 2024`

Primary arXiv history distinguishes:

- v1: 2024-07-17
- v4: 2025-11-07

Calibrated interpretation:

- `2024-07-17` is the v1 date, not the v4 date
- v4 should be associated with `2025-11-07`
- the paper-level fairness / Nash-welfare claims remain scoped to the paper and its assumptions
- the `1/2` existential guarantee and the polynomial-time `1/e^(2/e) ≈ 1/2.08` approximation must not be collapsed into a repository capability claim
- repository implementation/test remain `EVIDENCE_INSUFFICIENT`

Primary source: https://arxiv.org/abs/2407.12461

---

## W33-ERRATA-03 — MAC-SQL v6 version/date pairing

Affected W33 research chunks:

- `docs/en/Tool_System.md`
- `docs/zh/Tool_System.md`
- Daily integration: PR #114
- Weekly weaving: PR #116

Historical Daily chunk identifies:

- `arXiv:2312.11242v6`
- `Date: 2023-12-18`

Primary arXiv history distinguishes:

- v1: 2023-12-18
- v6: 2025-03-18

Calibrated interpretation:

- paper identity: retained
- requested version: `v6`
- v6 date: `2025-03-18`
- `2023-12-18` is the v1 date and must not be presented as the v6 date

Primary source: https://arxiv.org/abs/2312.11242

---

## W33-ERRATA-04 — MAC-SQL equation is not a proved repository convergence/error bound

The W33 MAC-SQL chunk records the decomposer sequential-generation factorization:

$$
P_{\mathcal{M}}(\mathcal{Y} | \mathcal{Q}, \mathcal{S}^{'}, \mathcal{K}) = \prod_{j=1}^{L} P_{\mathcal{M}}(\mathcal{Y}^{j} | \mathcal{Y}^{<j}; \mathcal{Q}^{j}, \mathcal{S}^{'}, \mathcal{K})
$$

The historical W33 wording then describes token-by-token error accumulation as being theoretically bounded / constrained by decomposition and describes the joint probability space as reduced at every step.

Calibration:

- the equation supports the paper's decomposed sequential-generation formulation
- it is not, by itself, a theorem proving a numerical error-accumulation bound
- it is not a convergence theorem for Agent Foundations
- claims that decomposition reduces practical difficulty or error propagation should be attributed to the MAC-SQL design rationale and empirical results unless a specific formal theorem is cited
- `Agent Architecture Mapping: DESIGN_CANDIDATE` is retained
- `Repository Implementation Status: EVIDENCE_INSUFFICIENT` is retained
- `Repository Test Status: EVIDENCE_INSUFFICIENT` is retained

Calibrated evidence label:

`PAPER_MECHANISM_SUPPORTED / FORMAL_REPOSITORY_ERROR_BOUND_NOT_ESTABLISHED`

Primary source: https://arxiv.org/abs/2312.11242

---

## W33-ERRATA-05 — Robust decentralized bandit v2 version/date pairing

Affected W33 research chunk:

- `docs/en/Collaboration_System.md` — `Reputation-Based Validator Selection for Robust Consensus`
- `docs/zh/Collaboration_System.md` — corresponding Chinese section
- W33 integration: PR #115

Historical chunk identifies:

- `arXiv:2402.04417v2`
- `Submitted 2024-02-06`

Primary arXiv history distinguishes:

- v1: 2024-02-06
- v2: 2024-07-25

Calibrated interpretation:

- `2024-02-06` is the v1 date, not the v2 date
- v2 should be associated with `2024-07-25`
- theoretical regret/security statements remain bounded by the paper's model and assumptions
- architecture mapping remains conceptual unless separately implemented
- repository implementation/test remain `EVIDENCE_INSUFFICIENT`

Primary source: https://arxiv.org/abs/2402.04417

---

## W33-ERRATA-06 — Weekly provenance was attached to a 2026-07 label

Affected W33 weaving:

- PR #116
- `docs/en/Tool_System.md`
- `docs/zh/Tool_System.md`

The W33 weave integrated MAC-SQL into the Tool System, but the patch also rewrote content directly under the pre-existing heading:

`🔗 [Weekly Sync Report] 本周文档级联编织与动态冲突审计 2026-07`

with MAC-SQL-specific W33 conclusions.

This mixes two historical periods.

Calibrated provenance:

- the pre-existing `2026-07` heading remains a July historical label
- MAC-SQL integration and the MAC-SQL-specific conflict/bilingual conclusions introduced by PR #116 belong to `2026-W33`, not July
- those W33 statements must not be cited as evidence of what the July weekly audit observed
- a future document regeneration may physically separate the two sections, but historical provenance is already corrected by this erratum

Calibrated W33 weekly record:

- W33 integrated item: `MAC-SQL`
- target container: `Tool System`
- mapping: `DESIGN_CANDIDATE`
- source version: `arXiv:2312.11242v6`
- source v6 date: `2025-03-18`
- paper mechanism: `SUPPORTED_FROM_PRIMARY_PAPER`
- formal repository error/convergence bound: `NOT_ESTABLISHED`
- repository implementation: `EVIDENCE_INSUFFICIENT`
- repository test status: `EVIDENCE_INSUFFICIENT`
- bilingual alignment: `SEMANTICALLY_ALIGNED_ON_CHECKED_FIELDS`
- paradigm relationship: `COMPATIBLE_WITH_QUALIFICATIONS`

---

## W33-ERRATA-07 — Absolute-safety language remains non-authoritative

During W33 Tool System weaving, surrounding pre-existing prose still contains absolute safety metaphors such as an `unbreakable wall` / `100% safety` formulation for a Control Barrier Function analogy.

Calibration:

- this absolute metaphor is not an evidence-backed repository guarantee
- CBF-style guarantees are conditional on the specified model, dynamics, safety set, feasibility, and assumptions
- unmodeled hazards, implementation defects, observation errors, and out-of-scope conditions are not covered by the metaphor
- the authoritative interpretation is therefore `CONDITIONAL_FORMAL_BOUND_WITHIN_MODELED_ASSUMPTIONS`, not `UNIVERSAL_100_PERCENT_SAFETY`

This erratum does not silently rewrite the earlier prose; it prevents the W33 conflict audit from being interpreted as validating the absolute wording.

---

## W33 items checked without a same-class correction in this audit

The W33 review also inspected the identity/evidence boundaries of the following research additions and found no same-class correction requiring an erratum here:

- `arXiv:2307.11044v1` — On the Convergence of Bounded Agents
- `arXiv:2412.20203v1` — No-regret learning in harmonic games
- `arXiv:2312.15549v1` — Finite-Time Frequentist Regret Bounds of Multi-Agent Thompson Sampling on Sparse Hypergraphs

This statement is deliberately narrow. It does not claim every analogy, architecture mapping, or copied formula has been independently re-proven by this repository.

---

## Audit boundary / 审计边界

- Original W33 research history rewritten: `NO`
- Existing `docs/AUGUST_2026_SOURCE_ERRATA.md` replaced: `NO`
- This file extends and, for W33 conflicts, supersedes older generated metadata: `YES`
- Paper claims promoted to repository implementation: `NO`
- Missing theorem or error bound invented: `NO`
- CI / GitHub Actions modified: `NO`
- Tests rerun for this errata task: `NO`
- Core research-route change authorized by this errata: `NO`

## Final W33 provenance status

- bibliographic identity: `CALIBRATED`
- version-specific dates: `CORRECTED_WHERE_PRIMARY_HISTORY_CONFLICTED`
- MAC-SQL formal-bound language: `DOWNGRADED_TO_PAPER_MECHANISM_AND_EMPIRICAL_DESIGN_RATIONALE`
- July/W33 weekly provenance mixing: `EXPLICITLY_RECONCILED`
- repository implementation boundary: `PRESERVED`
- repository test boundary: `PRESERVED`
