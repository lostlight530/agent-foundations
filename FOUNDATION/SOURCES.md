# Primary Source Registry / 一手来源登记

Access boundary: 2026-08-05. Registry presence means “eligible to cite”, not “repository capability”.

访问边界：2026-08-05。进入登记表仅表示“可引用”，不表示“仓库已经具备该能力”。

## S01 — NIST AI 600-1

- Type: `E1_PRIMARY_STANDARD`
- Title: *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*
- Version: NIST AI 600-1; page updated 2026-04-08
- URL: https://doi.org/10.6028/NIST.AI.600-1
- Use: risk identification, measurement, governance, and lifecycle controls; not a certification of any repository.

## S02 — OWASP Agentic Top 10 2026

- Type: `E1_PRIMARY_STANDARD`
- Version: 2026, released 2025-12-09
- URL: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- Use: agent goal hijack, tool misuse, identity/privilege abuse, supply-chain risk, unexpected code execution, memory poisoning, and related mitigations.

## S03 — OpenAI trustworthy third-party evaluations

- Type: `E1_PRIMARY_STANDARD`
- Date: 2026-05-29
- URL: https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- Use: model, harness, tools, safeguards, retries, budgets, elicitation, and validity checks are part of an evaluation claim.

## S04 — OpenAI chain-of-thought monitorability evaluation

- Type: `E3_REPRODUCIBLE_PREPRINT`
- Date: 2025-12-18
- URL: https://openai.com/index/evaluating-chain-of-thought-monitorability/
- Use: monitoring can add evidence but remains system- and monitor-dependent and imperfect.

## S05 — OpenAI internal coding-agent monitoring

- Type: `E1_PRIMARY_STANDARD`
- Date: 2026-03-19
- URL: https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/
- Use: monitoring architecture, alerting, deployment feedback, and explicit limitations.

## S06 — Anthropic Constitution

- Type: `E1_PRIMARY_STANDARD`
- Version: January 2026
- URL: https://www.anthropic.com/constitution
- Use: natural-language constitutions shape intended behavior but are living documents and do not ensure adherence.

## S07 — Anthropic constitutional classifiers

- Type: `E3_REPRODUCIBLE_PREPRINT`
- Date: 2026-01-09
- URL: https://www.anthropic.com/research/next-generation-constitutional-classifiers
- Use: measured safeguard improvements and residual jailbreak risk; no perfect defense claim.

## S08 — PM-Bench

- Type: `E2_PEER_REVIEWED`
- Identifier: arXiv:2607.12385v1; COLM 2026
- URL: https://arxiv.org/abs/2607.12385
- Use: prospective-memory benchmark; the reported best configuration reached 65.1% F1 in that study.

## S09 — Agentic Context Management

- Type: `E3_REPRODUCIBLE_PREPRINT`
- Identifier: arXiv:2607.21503v1
- URL: https://arxiv.org/abs/2607.21503
- Use: context as a lifecycle spanning ingest, scope, anticipation, compaction, consolidation, and provenance; vendor-linked results remain source-specific.

## S10 — RAFA

- Type: `E2_PEER_REVIEWED`
- Identifier: arXiv:2309.17382v3; ICML 2024
- URL: https://arxiv.org/abs/2309.17382
- Use: regret result under the paper’s Bayesian adaptive MDP and planner assumptions; not a universal agent-convergence result.

## S11 — CHMAS

- Type: `E2_PEER_REVIEWED`
- Identifier: arXiv:2607.19555v1; ACC 2026
- URL: https://arxiv.org/abs/2607.19555
- Use: centralized strategic planning plus distributed tactical execution; counterexample to blanket rejection of all central coordination.

## S12 — HalluProp

- Type: `E4_PREPRINT`
- Identifier: arXiv:2607.26836v1
- URL: https://arxiv.org/abs/2607.26836
- Use: pre-hoc hallucination-risk inference and propagation modeling; not prevention proof.

## S13 — AgentLocate

- Type: `E2_PEER_REVIEWED`
- Identifier: arXiv:2607.07989v1; COLM 2026
- URL: https://arxiv.org/abs/2607.07989
- Use: multi-agent failure localization using multiple evaluators; attribution remains evaluator-dependent.

## S14 — AgentDebugX

- Type: `E4_PREPRINT`
- Identifier: arXiv:2607.18754v1
- URL: https://arxiv.org/abs/2607.18754
- Use: Detect–Attribute–Recover–Rerun debugging loop and reported benchmark results; external implementation only.

## S15 — Plover

- Type: `E4_PREPRINT`
- Identifier: arXiv:2607.15193v1
- URL: https://arxiv.org/abs/2607.15193
- Use: inspectable and revisable plans for supervised GUI-agent repair; GUI implementation is out of this repository’s scope.

## S16 — From Agent Failures to Text Policies

- Type: `E4_PREPRINT`
- Identifier: arXiv:2607.20668v1
- URL: https://arxiv.org/abs/2607.20668
- Use: human-written policies improved tested frozen agents while generated policies did not reliably beat fixed prompting in the reported setting.

## S17 — AlphaEvolve

- Type: `E1_PRIMARY_STANDARD`
- Date: 2025-05; impact update 2026-05-07
- URL: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- Use: LLM proposals paired with executable evaluators and evolutionary selection; applicable where objective scoring exists.

## S18 — SLSA 1.2

- Type: `E1_PRIMARY_STANDARD`
- Version: 1.2, approved
- URL: https://slsa.dev/spec/v1.2/
- Use: software supply-chain provenance and incremental assurance; not an AI-behavior standard.
