# Independent A2 — agent-foundations — 2026-11-09 month relations

## Identity and fresh-main gate
- Repository: `lostlight530/agent-foundations`; task: `independent-maintenance/A2`.
- Logical date: 2026-11-09 Asia/Shanghai; review cut: 2026-11-09 23:20:01 +08:00.
- A1-before-A2 order: satisfied. A1 [PR #401](https://github.com/lostlight530/agent-foundations/pull/401) is merged.
- Fresh main after A1 merge: `e7154f055a2c33cd014cb723836f7ddc1ad60a21`.
- Exact merged A1 blob: `a683fb9706605c56f9256f55731c08f594e7d24b`.
- Prior A2 Nov08: `historical-audits/2026-11/2026-11-08-a2-foundations-month-relations.md` @ `a22a2c52fa0a69bd4b73dde44f5871d951702a24`.
- Open Draft PR #378 (WorkflowHub editions) remains a separate contribution; it is not this A2's upstream input and is not treated as merged evidence.

## Nov09 source objects
| Object | Exact blob | Relation |
|---|---|---|
| `docs/en/Tool_System.md` | `d867f354f75ee77b455cf0a42944fc560f6a3b7d` | FAVA research append |
| `docs/zh/Tool_System.md` | `9701ba58516556feaef12edc8aa91376b3439703` | Chinese mirror of the same paper lineage |
| Source paper | `arXiv:2607.27267v1` | original v1 dated 2026-07-29; re-read 2026-11-09 |

## Month-relation judgments
1. The FAVA source is a July29 preprint re-read on Nov09; it is not a newly published November paper.
2. The Nov09 Tool System entry is a W46 research unit. Its presence in current main does not retroactively add it to the closed W45 weekly cohort.
3. FAVA separates LLM extraction of Permission IR from deterministic graph lowering, SMT solving and a just-in-time gateway; the paper's formal claims are conditional on the graph and trusted lowering being complete.
4. Inferred graph edges are not automatically authoritative runtime facts; source provenance and trust labels remain necessary.
5. Finite-graph soundness does not prove that natural-language extraction, implicit flows, credential state or downstream backends are completely represented.
6. The taint-only monotonicity result is restricted to graph extension under fixed policy and without new trusted sanitizers/declassification or positive obligation facts.
7. A fresh authenticated `tests_passed` fact can satisfy a positive guard; the theorem is not a universal deny-only monotonicity claim.
8. The authors report 90.5% Decision Compliance Rate over 801 benchmark replay cases. This is an author-reported mixed allow/block classification metric, not an independent safety probability or repository test result.
9. False-positive blocks and false-negative permissions are both counted by DCR; a high aggregate score does not establish complete policy extraction or effect correctness.
10. The paper is not registered in `FOUNDATION/SOURCES.md`; no Sxx ID is assigned by this A2.
11. English and Chinese Tool System entries are one source lineage, not two studies or independent replications.
12. No local Permission IR implementation, SMT solver replay, gateway, benchmark replay, theorem proof check or external action broker was executed.
13. The 11/08 STEAD paper and Nov09 FAVA paper are distinct objects; their theoretical guarantees and failure modes must not be conflated.
14. W45 Weekly Cascade remains closed 7/7; Collaboration had no newly dated W45 Daily research chunk, a legitimate negative input.
15. W46 opens with the Nov09 FAVA entry; weekly cascade is NOT_DUE until W46 closes. November Monthly Blueprint remains rolling/open.
16. A2 does not promote any AF-* claim, Verified Core state, SOURCE registry entry or implementation status.
17. A1/A2 maintenance records are separate from the native research append and from the open WorkflowHub PR #378.

## Current calendar and ownership matrix
| Owner | Current state | A2 decision |
|---|---|---|
| November 2026 | OPEN / rolling blueprint | continue |
| W44 | FINAL; Nov01 | preserve |
| W45 | FINAL 7/7; Nov02–08 | preserve |
| W46 | OPEN 1/7; Nov09 FAVA | APPEND_CURRENT_RELATION |
| W46 weekly cascade | NOT_DUE | wait for week close |
| November monthly final | NOT_DUE | wait for month close |

- A2 follows merged A1 #401 and a fresh main read.
- No SOURCE registry, Verified Core, implementation, workflow, protected Jules record or prior W45 artifact is modified.
- Result: `A2_MONTH_RELATION_DELIVERED / NOVEMBER_OPEN / W45_FINAL / W46_OPEN_1_OF_7`.
