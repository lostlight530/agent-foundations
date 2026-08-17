# Reproducibility and AI Use / 可复现性与 AI 使用

## Reproducibility target / 可复现目标

This is a documentary foundation. A reviewer must be able to locate each Claim ID, recover its primary source and exact cited version, distinguish external findings from repository implementation, identify what proposition/theorem was actually verified, and rerun deterministic repository checks where executable artifacts exist.

本目录属于文档型基础体系。评审者必须能够定位每个 Claim ID、恢复其一手来源与准确引用版本、区分外部发现与仓库实现、识别真正核验过的命题/定理，并在存在可执行产物时重新运行确定性仓库检查。

Supported environment: Python 3.12 or 3.14, Git, and no third-party Python packages.

支持环境：Python 3.12 或 3.14、Git，不依赖第三方 Python 包。

```bash
python FOUNDATION/validate.py
python -m unittest FOUNDATION/test_contract.py -v
python FOUNDATION/validate.py --base-ref origin/main
```

The validator checks required files, claim metadata, unique IDs, registered source references, JSON Schema structure, restricted overclaims, complete GitHub Action SHA pinning, and protected paths when a base ref is supplied.

验证器检查必需文件、声明元数据、唯一 ID、已登记来源引用、JSON Schema 结构、受限过度声明、GitHub Action 完整 SHA 固定，以及提供基准引用时的保护路径。

It does not prove semantic truth, mathematical correctness, translation quality, source-version identity, formula transcription, theorem interpretation, or external experimental reproduction unless those items are independently checked and recorded.

它不能自动证明语义真伪、数学正确性、翻译质量、来源版本身份、公式抄录、定理解释或外部实验复现；这些项目必须独立核验并记录。

## Source identity workflow / 来源身份流程

For every material arXiv source:

1. normalize the base identifier
2. record the exact cited `vN` when a version is specified
3. inspect primary arXiv metadata and submission history
4. pair `vN` with the date belonging to that version
5. record title and authors when needed to disambiguate identity
6. only then use the source for claim verification

Use:

```bash
python FOUNDATION/arxiv_probe.py <arxiv-id-or-url>
python FOUNDATION/arxiv_probe.py <arxiv-id-or-url> --expect-version N --expect-date YYYY-MM-DD
```

An explicit `vN` citation should not enter a verified research chunk without `VERSION_DATE_PAIR_VERIFIED` or an explicit `VERSION_DATE_NOT_VERIFIED` limitation.

The base arXiv page's first-submission date is not a substitute for the date of a later cited version.

## Claim verification workflow / 声明核验流程

Identity verification and claim verification are separate steps.

For each material proposition, record the strongest surface actually checked:

- abstract only → `ABSTRACT_SUPPORTED`
- primary full text → `FULL_TEXT_SUPPORTED`
- exact theorem/lemma → `THEOREM_TEXT_VERIFIED`
- exact equation/notation → `FORMULA_TRANSCRIPTION_VERIFIED`
- assumptions/conditions → `ASSUMPTIONS_VERIFIED`

Do not use `VERIFIED_FROM_LATEX_SOURCE` merely because a TeX-source link exists or a retrieval script succeeded. The relevant theorem/formula and its assumptions must actually be inspected.

When a long equation is copied, verify punctuation, indices, powers, parentheses, summation ranges, and variable definitions. If this audit was not performed, use a narrower status such as `PAPER_LEVEL_RESULT_SUPPORTED / LONG_FORMULA_NOT_RECERTIFIED`.

## Handling primary-source disagreement / 处理一手来源冲突

If primary surfaces disagree — for example abstract vs rendered theorem text, different versions, or HTML vs TeX — preserve the conflict.

Required behavior:

- record the conflicting surfaces and versions
- mark `PRIMARY_SOURCE_CONFLICT`
- do not guess which coefficient/theorem wording is authoritative
- narrow downstream claims to what all checked surfaces support
- reverify from versioned TeX/PDF or an author correction before restoring the stronger claim

A primary-source conflict is not a reason to delete the research record; it is a reason to lower claim strength and improve provenance.

## Temporal provenance / 时间溯源

Research period is part of provenance.

- a W33 research chunk remains a W33 observation after weekly weaving
- moving content into an older section does not make it evidence from that older period
- a July sync heading must not absorb August/W33 findings without an explicit new-period marker
- errata/reconciliation may supersede interpretation without erasing the original historical artifact

## AI use / AI 使用

AI systems may assist with source discovery, drafting, translation, consistency checks, and validator code. AI output is never evidence. Material statements are checked against primary sources and retain source-specific assumptions, evaluated systems, configurations, metrics, exact version, and limits.

AI 系统可以辅助来源发现、起草、翻译、一致性检查和验证器代码。AI 输出不构成证据。实质性陈述必须对照一手来源，并保留来源特定的假设、被测系统、配置、指标、准确版本和局限。

AI assistance must not:

- infer a later-version date from v1
- upgrade an abstract claim into a theorem
- upgrade a mechanism equation into a convergence/error bound without the theorem
- convert empirical results into mathematical guarantees
- convert paper guarantees into repository guarantees
- hide an unresolved source conflict by selecting the most convenient value

## Correction model / 修正模型

For the verified core and the SOP-generated research stream:

- existing generated documents are inputs, not authority
- unsupported claims are removed or explicitly downgraded in the verified core
- historical generated artifacts may remain visible when useful as execution history
- material historical errors are corrected with explicit errata/reconciliation and precedence, not silent retroactive perfection
- newer primary-source evidence supersedes conflicting secondary summaries
- no credentials, private prompts, personal memory, or hidden reasoning traces are committed
- maintainer review remains required before merge

## Documentation-only maintenance / 纯文档维护

A provenance/evidence-only change may intentionally avoid runtime tests when executable behavior is untouched. In that case the change must state `tests not run — documentation/evidence only` rather than implying validation occurred.

This exception does not permit implementation claims without tests; it only prevents documentation maintenance from fabricating irrelevant runtime evidence.
