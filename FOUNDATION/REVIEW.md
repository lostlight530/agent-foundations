# Independent Verified-Core Review / 独立可验证核心审核

Status: public post-hoc review contract / 公开事后审核契约

## Purpose / 目的

This file defines a reviewer-side state machine for independently auditing committed Agent Foundations material after it is produced.

本文件定义一个评审侧状态机，用于在 Agent Foundations 内容生成并提交后进行独立审核。

It is deliberately outside Jules Daily/Weekly/Monthly automation, GPT/cloud maintenance sessions, GitHub Actions, CI, deployment, and any future runtime. It is not a task prompt, repository-memory entry, `AGENTS.md` instruction, workflow, CI gate, or executable policy.

本审核层明确位于 Jules Daily/Weekly/Monthly 自动化、GPT/云端维护、GitHub Actions、CI、部署与任何未来运行时之外。它不是任务提示词、仓库记忆、`AGENTS.md` 指令、工作流、CI 门或可执行策略。

## Public review states / 公开审核状态

These states describe review status only. They do not expose private reasoning.

这些状态只描述审核状态，不暴露私有推理。

1. `REVIEW_PENDING`
   - material has entered independent review / 材料进入独立审核
2. `SOURCE_IDENTITY_VERIFIED`
   - source identity and exact cited version are verified where material / 来源身份与必要的准确版本已核验
3. `CLAIM_SURFACE_VERIFIED`
   - the strongest checked surface is bounded: abstract, full text, theorem, equation, assumptions / 已限定实际核验到的声明表面
4. `PRIMARY_SOURCE_CONFLICT`
   - primary surfaces disagree and the disagreement remains open / 一手来源表面存在未解决冲突
5. `INSUFFICIENT_EVIDENCE`
   - evidence cannot support the requested claim strength / 证据不足以支持目标声明强度
6. `MAPPING_SCOPED`
   - external result is explicitly classified as requirement, analogy, candidate mechanism, counterevidence, or out of scope / 外部结果的本地映射已明确限界
7. `IMPLEMENTATION_SEPARATED`
   - paper evidence and repository implementation/validation status are explicitly separated / 论文证据与仓库实现和验证状态已分离
8. `CALIBRATION_REQUIRED`
   - historical material remains useful but interpretation or provenance requires correction / 历史材料仍有价值但解释或溯源需纠正
9. `CALIBRATED`
   - an explicit erratum/reconciliation records the supported interpretation / 已通过显式勘误或校准记录支持解释
10. `ACCEPTED_FOR_VERIFIED_CORE`
   - the reviewed proposition fits the verified-core evidence contract / 审核命题满足可验证核心证据契约

Reviewer confidence or model agreement is never a transition condition.

评审者主观信心或模型一致意见从不构成状态迁移条件。

## Transition discipline / 状态迁移纪律

Normal supported path:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → CLAIM_SURFACE_VERIFIED → MAPPING_SCOPED → IMPLEMENTATION_SEPARATED → ACCEPTED_FOR_VERIFIED_CORE`

Correction path:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → CLAIM_SURFACE_VERIFIED → CALIBRATION_REQUIRED → CALIBRATED → MAPPING_SCOPED → IMPLEMENTATION_SEPARATED → ACCEPTED_FOR_VERIFIED_CORE`

Conflict path:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → PRIMARY_SOURCE_CONFLICT`

Evidence-limited path:

`REVIEW_PENDING → SOURCE_IDENTITY_VERIFIED → INSUFFICIENT_EVIDENCE`

Every transition requires public, reviewable evidence such as a primary source, exact source version, theorem/equation location, repository artifact, explicit command/result, or erratum record.

每次迁移都必须依赖公开、可复核证据，例如一手来源、准确来源版本、定理/公式位置、仓库产物、明确命令与结果或勘误记录。

## Agent Foundations review checks / 本仓审核检查

When applicable, independent review checks that:

- explicit arXiv `vN` citations are paired with the date belonging to that version
- source identity verification is not confused with theorem or formula verification
- abstract support is not promoted into theorem support
- a mechanism equation or probability factorization is not labelled a formal error/convergence bound without the theorem that provides that bound
- long formulas that were not independently checked remain limited to paper-level evidence
- primary-source disagreements remain `PRIMARY_SOURCE_CONFLICT` rather than being silently resolved
- mathematical results retain original assumptions, comparator, domain, quantifiers, and version
- external paper guarantees are never upgraded into repository guarantees without executable local evidence
- `CONCEPTUAL_MAPPING`, `DESIGN_CANDIDATE`, `REFERENCE_ONLY`, `NOT_IMPLEMENTED`, and `EVIDENCE_INSUFFICIENT` remain distinct
- bilingual weaving preserves the same evidence status and does not strengthen a claim in translation
- Weekly weaving preserves the original research period and does not make later material appear to belong to an older period

## Authority boundary / 权威边界

Independent review uses the existing verified-core topology but does not become an execution authority.

- `FOUNDATION/EVIDENCE.md` defines evidence and claim semantics
- `FOUNDATION/SOURCES.md` records verified source identities
- `FOUNDATION/PROVENANCE.md` defines reproducibility and source-version handling
- `FOUNDATION/ARCHITECTURE.md`, `MEMORY.md`, `TOOLS.md`, and `COLLABORATION.md` are bounded evidence/specification maps
- `docs/**` preserves the broader bilingual research stream
- executable repository artifacts and tests, where they exist, are the only basis for implementation claims

An audit finding may narrow or contest an interpretation. It must not invent implementation, reproduction, theorem support, source agreement, or test success to make the repository appear complete.

## Global-practice alignment / 全球实践对齐

This reviewer contract borrows selected public principles from international and industry guidance. It does **not** claim certification, formal conformity, or a NIST/ISO/OECD/SLSA/OWASP level.

本审核契约只吸收国际标准与行业公开实践中与本仓相关的原则，不声称认证、正式符合性或任何 NIST/ISO/OECD/SLSA/OWASP 等级。

- NIST AI RMF: independent review can improve measurement effectiveness and mitigate internal bias or conflicts of interest; limits, uncertainty, and unmeasured dimensions should remain documented. This supports independent theorem/claim review without turning the reviewer into an execution gate. Reference: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- ISO/IEC 42001: traceability, transparency, defined accountability, risk management, and continual improvement are useful governance patterns. Agent Foundations adopts these as documentary review principles only and claims no ISO certification or conformity. Reference: https://www.iso.org/standard/42001
- OECD AI Principles: accountability should be supported by lifecycle traceability and documentation sufficient for inquiry, while transparency and disclosure remain appropriate to context. This supports reproducibility without publishing unnecessary private operating context. References: https://oecd.ai/en/dashboards/ai-principles/P9 and https://oecd.ai/en/dashboards/ai-principles/P7
- SLSA v1.2: provenance becomes useful assurance only when a verifier checks it against explicit expectations. The verified core reuses this separation between provenance and verification for sources/revisions; it claims no SLSA level or attestation. References: https://slsa.dev/spec/v1.2/provenance and https://slsa.dev/spec/v1.2/verifying-source
- OpenAI third-party evaluation guidance: evaluation claims should identify the tested system, harness, budget, elicitation method, and validity hazards before results are generalized. This principle is used when Agent Foundations discusses agent/eval literature; it adds no automatic eval harness. Reference: https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- Anthropic agent-evaluation guidance: agent results depend on task design, environment isolation, trials, graders, and human calibration; multiple evidence layers are stronger than a single evaluator. This reinforces the distinction between paper result, local mapping, implementation, and validation. It is not a CI requirement. Reference: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- OWASP Agentic Top 10: tool misuse, identity/privilege abuse, memory/context poisoning, insecure inter-agent communication, cascading failures, and human-agent trust exploitation support preserving explicit boundaries between conceptual research and executable authority. Reference: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

Shared principle / 共同原则:

**Separate producer from reviewer; preserve exact provenance; verify against explicit expectations; retain assumptions, conflicts, and uncertainty; separate external results from local implementation; disclose only the minimum public context necessary for audit; never give the review layer unintended execution authority.**

**生产者与审核者分离；保留准确溯源；按显式预期核验；保留假设、冲突和不确定性；分离外部结果与本地实现；只公开审计所需的最小上下文；绝不让审核层获得非预期执行权。**

## Privacy and non-public reasoning boundary / 隐私与非公开推理边界

The public repository stores review outcomes and evidence, not private cognition or private operating context.

公开仓库保存审核结论与证据，不保存私有认知过程或私有运行上下文。

Do not commit, reconstruct, or expose:

- private task prompts or full private conversation prompts
- Jules repository-memory text or other private agent-memory content
- hidden reasoning traces, chain-of-thought, scratchpads, or internal deliberation
- personal context, private correspondence, private account metadata, or non-public relationship information
- credentials, tokens, session secrets, private URLs, or confidential third-party material
- internal strategy whose disclosure is unnecessary to reproduce the public evidence decision

不得提交、重建或公开：私有任务提示词、完整私聊提示、Jules 仓库记忆、其他私有 Agent 记忆、隐藏推理链、scratchpad、内部 deliberation、个人上下文、私信、私有账号信息、非公开关系信息、凭据、token、私有 URL、第三方机密材料，以及复核公开证据结论并不需要披露的内部策略。

A public rationale should contain only the minimum evidence explanation necessary to audit the disposition. It must not expose private reasoning traces.

公开理由只保留足以审计结论的最小证据说明，不公开私有推理轨迹。

## Minimal review record / 最小审核记录

A durable review may record:

- Claim ID or artifact under review
- current public review state
- public source identity and exact version where material
- strongest checked claim surface
- supported proposition, assumptions, and limits
- mapping status
- repository implementation and validation status
- missing or conflicting evidence
- erratum/reconciliation pointer when required
- safe validation commands and observed results when relevant
- final public disposition

No timestamp is required. No private prompt, private memory, hidden reasoning, workflow, or CI field exists in this public schema.

无需时间戳。本公开 schema 不包含私有提示、私有记忆、隐藏推理、workflow 或 CI 字段。

## Automation isolation / 自动化隔离

This contract is intentionally non-operative. It does not trigger, modify, gate, or replace Jules, GPT/cloud maintenance, GitHub Actions, CI, deployment, schedules, repository memory, or runtime behavior. No new CI or workflow is implied by this document.

本契约刻意不具备执行作用，不触发、不修改、不门控也不替代 Jules、GPT/云端维护、GitHub Actions、CI、部署、调度、仓库记忆或运行时行为。本文件不隐含新增任何 CI 或 workflow。

Generated material from those systems may be reviewed here later. That review never constitutes evidence that the producer consumed or enforced this contract.
