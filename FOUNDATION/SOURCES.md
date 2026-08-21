# Primary Source Registry / 一手来源登记

Access boundary: 2026-08-17. Registry presence means “eligible to cite”, not “repository capability”.

访问边界：2026-08-17。进入登记表仅表示“可引用”，不表示“仓库已经具备该能力”。

For an explicit arXiv `vN`, the version/date pair below is part of source identity. If a later audit finds a conflict, record the conflict rather than silently replacing history.

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

## S19 — On the Convergence of Bounded Agents

- Type: `E4_PREPRINT`
- Identifier: arXiv:2307.11044v1
- Version date: 2023-07-20
- URL: https://arxiv.org/abs/2307.11044
- Use: two bounded-agent convergence definitions centered on minimal future behavioral state size and performance change relative to internal-state change; not a proof of convergence for general LLM agents.
- Verification boundary: paper identity and abstract-level propositions are primary-source supported; formulas/theorems require separate full-text verification.

## S20 — Variational Policy Propagation for Multi-agent Reinforcement Learning

- Type: `E4_PREPRINT`
- Identifier: arXiv:2004.08883v4
- Version date: 2022-01-29
- v1 date: 2020-04-19
- URL: https://arxiv.org/abs/2004.08883
- Use: collaborative MARL, MRF-form joint policy under the paper’s conditions, and variational-inference-based policy layers; architecture mapping remains conceptual.
- Verification boundary: v4/date pairing is primary-source verified; exact formulas and assumptions require theorem/formula-level checks before strong transcription labels.

## S21 — No-regret learning in harmonic games

- Type: `E4_PREPRINT`
- Identifier: arXiv:2412.20203v1
- Version date: 2024-12-28
- URL: https://arxiv.org/abs/2412.20203
- Use: vanilla FTRL non-convergence/cycling phenomena in harmonic games and extrapolated FTRL convergence with at-most `O(1)` regret under the paper’s conditions.
- Verification boundary: these are harmonic-game results, not a general multi-agent or LLM-agent convergence guarantee.

## S22 — Compatibility of Fairness and Nash Welfare under Subadditive Valuations

- Type: `E4_PREPRINT`
- Identifier: arXiv:2407.12461v4
- Version date: 2025-11-07
- v1 date: 2024-07-17
- URL: https://arxiv.org/abs/2407.12461
- Use: existence of partial EFX and complete EF1 allocations with `1/2`-of-optimal NSW guarantees under subadditive valuations; the abstract also describes a polynomial transformation from an arbitrary input allocation.
- Conflict note: during the 2026-08-17 audit, the current arXiv abstract and rendered full-text theorem surface were not treated as automatically interchangeable for the exact polynomial-transformation coefficient. Preserve `PRIMARY_SOURCE_CONFLICT` until versioned TeX/PDF re-verification resolves any discrepancy.
- Verification boundary: do not state the transformation factor as directly relative to optimal unless the theorem used actually provides that relation.

## S23 — MAC-SQL

- Type: `E2_PEER_REVIEWED`
- Identifier: arXiv:2312.11242v6; COLING 2025 (Oral)
- Version date: 2025-03-18
- v1 date: 2023-12-18
- URL: https://arxiv.org/abs/2312.11242
- Use: multi-agent Text-to-SQL decomposition with Decomposer, Selector, and Refiner roles plus reported empirical execution accuracy.
- Verification boundary: the sequential-generation factorization is a paper mechanism; it is not by itself a formal convergence or numerical error-accumulation bound.

## S24 — Decentralized Blockchain-based Robust Multi-agent Multi-armed Bandit

- Type: `E4_PREPRINT`
- Identifier: arXiv:2402.04417v2
- Version date: 2024-07-25
- v1 date: 2024-02-06
- URL: https://arxiv.org/abs/2402.04417
- Use: decentralized MAMAB with malicious participants, validators, signatures, secure multiparty computation, UCB-style coordination, and paper-reported logarithmic regret under stated assumptions.
- Verification boundary: paper-level result is supported; long transcribed equations require separate `FORMULA_TRANSCRIPTION_VERIFIED` status before being treated as exact.

## S25 — Finite-Time Frequentist Regret Bounds of Multi-Agent Thompson Sampling on Sparse Hypergraphs

- Type: `E2_PEER_REVIEWED`
- Identifier: arXiv:2312.15549v1; AAAI 2024
- Version date: 2023-12-24
- URL: https://arxiv.org/abs/2312.15549
- Use: epsilon-exploring MATS, sublinear worst-case frequentist regret in the studied MAMAB hypergraph setting, and matching lower-bound interpretation up to constants/log terms when sufficiently sparse.
- Verification boundary: the regret guarantee remains tied to the paper’s hypergraph, reward-additivity, exploration, and sparsity assumptions; it does not transfer automatically to generic agent architectures.

## S26 — Multi-Agent Probabilistic Ensembles with Trajectory Sampling for Connected Autonomous Vehicles

- Type: `E4_PREPRINT`
- Identifier: arXiv:2312.13910v3
- Version date: 2023-12-21
- Authors: Ruoqi Wen, Jiahao Huang, Rongpeng Li, Guoru Ding, Zhifeng Zhao
- URL: https://arxiv.org/abs/2312.13910
- Use: group regret bounds for multi-agent model-based RL under limited communication range.

## S27 — Optimal Regret Bounds for Collaborative Learning

- Type: `E4_PREPRINT`
- Identifier: arXiv:2312.09674v1
- Version date: 2023-12-15
- Authors: Amitis Shidani, Sattar Vakili
- URL: https://arxiv.org/abs/2312.09674
- Use: CExp$^2$ algorithm, mixed reward collaborative bandit problem formulation, and optimal $\mathcal{O}(\log(T))$ regret bound under bounded expected communication rounds.
- Verification boundary: The bound is structurally tied to the static agent weight matrix $W$ and the assumption that an oracle $\mathcal{P}(\Delta)$ exists to solve the constrained optimization problem for arm allocation; it does not automatically scale to dynamic communication topologies or unpredictable environments.


## S28 — ADMM-Tracking Gradient for Distributed Optimization

- Type: `E4_PREPRINT`
- Identifier: arXiv:2309.14142v3
- Version date: 2023-09-25
- URL: https://arxiv.org/abs/2309.14142
- Use: Decentralized consensus optimization via an ADMM-based dynamic consensus protocol, maintaining linear convergence under asynchronous updates and unreliable network communications.
- Verification boundary: Guaranteed under strongly convex costs; requires ADMM dynamic consensus which may increase local computation relative to vanilla gradient tracking.

## S29 — Robust Multi-Agent Bandits with Heavy-Tailed Rewards and Information Asymmetry

- Type: `E4_PREPRINT`
- Identifier: arXiv:2608.10529v1
- Version date: 2026-08-11
- Authors: Daphne Feng, Ricardo Parada, Lily Jiang, Sophia Yi, William Chang
- URL: https://arxiv.org/abs/2608.10529
- Use: mRUCB-Intervals algorithm for decentralized action selection with observable actions but independent heavy-tailed rewards.
- Verification boundary: Bound holds under bounded $1+\varepsilon$ moment condition and heavily depends on horizon $T$ and exponential scaling in terms of number of agents and actions.

## S30 — Exploiting hidden structures in non-convex games for convergence to Nash equilibrium

- Type: `E4_PREPRINT`
- Identifier: arXiv:2312.16609v1
- Version date: 2023-12-27
- Authors: Iosif Sakos, Emmanouil-Vasileios Vlatakis-Gkaragkounis, Panayotis Mertikopoulos, Georgios Piliouras
- URL: https://arxiv.org/abs/2312.16609
- Use: Preconditioned Hidden Gradient Descent (PHGD) algorithm and theoretical convergence bounds in hidden non-convex multi-agent games under monotone assumptions bounded by representation maps.
- Verification boundary: Guarantees depend strictly on the game admitting a latent monotone structure, with representation maps lacking critical points and gradients meeting Lipschitz smoothness and bounded second moment requirements. It does not generalize unconditionally to all non-convex learning topologies.
