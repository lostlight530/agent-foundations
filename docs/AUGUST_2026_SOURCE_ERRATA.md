# August 2026 Source Errata / 2026 年 8 月来源勘误

> Status: ACTIVE
>
> Audit date: 2026-08-10
>
> Purpose: preserve the original Jules-generated research history while correcting source metadata that was independently verified against the primary arXiv records

This file has precedence over conflicting bibliographic metadata in the affected August research chunks until those large bilingual core documents are regenerated or rewritten from the corrected primary records.

本文件优先于受影响的 8 月研究块中与之冲突的书目元数据，直到对应的大型中英双语核心文档基于正确的一手来源重新生成或重写

---

## ERRATA-2026-08-01 — AV-AIVAT arXiv identifier and date

Affected August research chunk:

- `docs/en/Architecture_Principles.md` — `Certified Anytime-Valid Stopping for Evaluation (AV-AIVAT)`
- `docs/zh/Architecture_Principles.md` — `评估验证的随时有效自适应停止 (AV-AIVAT)`
- Original Jules integration date: 2026-08-08

### Incorrect metadata currently preserved in the historical chunk

- `https://arxiv.org/abs/2408.06362v1`
- `v1, 2024-08-06`

### Correct primary-source metadata

- **Title:** AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games
- **Authors:** Boning Li, Yu Chen, Longbo Huang
- **arXiv:** `2608.06362v1`
- **Canonical URL:** `https://arxiv.org/abs/2608.06362`
- **v1 submitted:** 2026-08-06 17:57:11 UTC

### Correction scope

This erratum corrects the arXiv identifier and publication date only. The primary arXiv abstract independently supports the paper identity, the AV-AIVAT/AIVAT framing, continuously monitored confidence sequences, and the reported median `74×` stopping-efficiency comparison under the stated evaluation setting. No repository implementation or test status is promoted by this correction.

本勘误仅修正 arXiv 编号与版本日期，不把论文结论扩大为本仓库已经实现或验证的能力

---

## ERRATA-2026-08-02 — Collaborative Mean Estimation v3 date

Affected August research chunk:

- `docs/en/Collaboration_System.md` — `Collaborative Mean Estimation Among Heterogeneous Strategic Agents`
- `docs/zh/Collaboration_System.md` — `异构策略智能体间的协作均值估计`
- Original Jules integration date: 2026-08-07

### Mixed metadata currently preserved in the historical chunk

The chunk correctly identifies `arXiv:2407.15881v3`, but pairs that version with `Date: 2024-07-20`

`2024-07-20` is the **v1 submission date**, not the v3 date

### Correct primary-source version history

- **Current title:** Collaborative Mean Estimation Among Heterogeneous Strategic Agents: Individual Rationality, Fairness, and Truthful Contribution
- **Authors:** Alex Clinton, Yiding Chen, Xiaojin Zhu, Kirthevasan Kandasamy
- **arXiv:** `2407.15881v3`
- **v1:** 2024-07-20 17:45:40 UTC
- **v2:** 2025-06-23 05:32:45 UTC
- **v3:** 2025-08-14 04:41:26 UTC
- **Current-version date:** 2025-08-14

### Correction scope

This erratum corrects the version/date pairing. The current v3 primary record supports the paper's collaborative mean-estimation setting, strategic/non-collection/data-fabrication problem, Nash-equilibrium framing, `O(sqrt(m))` worst-case approximation, `O(1)` favorable-case approximation, and the stated hardness direction. Repository implementation and test status remain unchanged.

本勘误修正的是版本与日期的配对，不改变 `PAPER_ONLY / CONCEPTUAL_MAPPING / EVIDENCE_INSUFFICIENT` 等实现边界

---

## Audit boundary / 审计边界

- Original generated research chunks are not deleted or silently rewritten by this errata commit
- Historical mistakes remain visible as historical evidence and are explicitly superseded here
- Only claims independently checked against primary arXiv records are corrected
- No unverified equation, theorem number, implementation status, or repository behavior is invented
- Future August source reconciliation should resolve a conflict in favor of this errata file unless a newer primary-source correction supersedes it

## Verification status

- AV-AIVAT metadata correction: `PRIMARY_SOURCE_VERIFIED`
- Collaborative Mean Estimation version-history correction: `PRIMARY_SOURCE_VERIFIED`
- Repository implementation changes: `NONE`
- Repository test claims added: `NONE`
