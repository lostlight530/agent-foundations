# Reproducibility and AI Use / 可复现性与 AI 使用

## Reproducibility target / 可复现目标

This is a documentary foundation. A reviewer must be able to locate each Claim ID, recover its primary source and version, distinguish external findings from repository implementation, and rerun deterministic repository checks.

本目录属于文档型基础体系。评审者必须能够定位每个 Claim ID、恢复其一手来源和版本、区分外部发现与仓库实现，并重新运行确定性仓库检查。

Supported environment: Python 3.12 or 3.14, Git, and no third-party Python packages.

支持环境：Python 3.12 或 3.14、Git，不依赖第三方 Python 包。

```bash
python FOUNDATION/validate.py
python -m unittest FOUNDATION/test_contract.py -v
python FOUNDATION/validate.py --base-ref origin/main
```

The validator checks required files, claim metadata, unique IDs, registered source references, JSON Schema structure, restricted overclaims, complete GitHub Action SHA pinning, and protected paths when a base ref is supplied.

验证器检查必需文件、声明元数据、唯一 ID、已登记来源引用、JSON Schema 结构、受限过度声明、GitHub Action 完整 SHA 固定，以及提供基准引用时的保护路径。

It does not prove semantic truth, mathematical correctness, translation quality, or external experimental reproduction.

它不能证明语义真伪、数学正确性、翻译质量或外部实验复现。

## AI use / AI 使用

AI systems may assist with source discovery, drafting, translation, consistency checks, and validator code. AI output is never evidence. Material statements are checked against primary sources and retain source-specific assumptions, evaluated systems, configurations, metrics, and limits.

AI 系统可以辅助来源发现、起草、翻译、一致性检查和验证器代码。AI 输出不构成证据。实质性陈述必须对照一手来源，并保留来源特定的假设、被测系统、配置、指标和局限。

For the 2026 verified core:

- GitHub `main` was the repository record at the start of work.
- Existing SOP-generated documents were treated as inputs, not authority.
- Primary standards, official documentation, system cards, and original paper pages were preferred.
- Unsupported claims were removed rather than cosmetically softened.
- No credentials, private prompts, personal memory, or hidden reasoning traces are committed.
- Maintainer review remains required before merge.

2026 可验证核心遵循：以工作开始时 GitHub `main` 为记录；现有 SOP 文档只作输入；优先一手标准、官方文档、系统卡和原论文页面；不支持的结论直接移除；不提交凭据、私有 Prompt、个人记忆或隐藏推理轨迹；合并前仍需维护者评审。
