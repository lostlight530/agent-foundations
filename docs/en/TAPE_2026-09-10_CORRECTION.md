# TAPE evidence correction — 2026-09-10

Status: `CURRENT_INTERPRETATION_CORRECTION`
Repository: `lostlight530/agent-foundations`
System container: `Collaboration System`
Canonical source: `S40`
Source identity: `arXiv:2312.15667v3`
Historical generated block affected: `AF-COLLAB-003` added by PR #155 on 2026-09-08
Related earlier weave: PR #151 on 2026-09-06

This file is a forward correction. It does not delete or rewrite the historical generated block or its PR history.

## Current source-supported interpretation

The checked TAPE paper supports the following bounded claims:

- TAPE introduces an agent-topology framework for cooperative multi-agent policy-gradient learning. The topology controls which other agents' utilities are considered and TAPE optimizes coalition utility rather than requiring an all-agent global utility for every update.
- The paper proposes stochastic and deterministic TAPE variants.
- For stochastic TAPE, the checked policy-improvement theorem assumes tabular policy expressions and a sufficiently small update condition, and establishes monotonic objective improvement under those conditions: the updated policy is no worse than the previous policy on the theorem's stated objective.
- The paper studies Barabási–Albert, Watts–Strogatz, and Erdős–Rényi graph models. Erdős–Rényi is used in most reported experiments because it produced more diverse topologies in the authors' study.
- The paper's second checked theoretical result relates stochastic-TAPE parameter-update variance relative to DOP to the Erdős–Rényi connection probability `p`; denser topology can increase update diversity while also reintroducing centralized-decentralized mismatch pressure.

## Claims from the 2026-09-08 generated block that are not current evidence

The following statements must not be reused as source-certified TAPE claims unless a later independent recertification establishes them:

- `Erdős–Rényi topology is a core or universal assumption of the policy-improvement theorem.` The checked paper describes agent topology as arbitrary and studies several graph families; Erdős–Rényi is one analyzed/experimental model.
- `The convergence rate is bounded by algebraic connectivity or other spectral properties of the communication graph.` This statement was not found in the checked source.
- `TAPE converges to a stationary point of the true objective.` That is not the theorem statement checked for the current correction; the checked theorem is a policy-improvement result under explicit conditions.
- `Each policy update is conditioned on neighbor messages m_N through the generated local-Q formula.` The checked paper formulates coalition utility/topology; the message-conditioned formula in the generated block is not certified as a paper equation.
- The beginner analogy's claim that sufficient connectivity mathematically guarantees an organization reaches an optimal global outcome. That extrapolation exceeds the source's theorem scope.

## Five-axis disposition

- Claim State: `SUPPORTED_WITH_SCOPE_CORRECTION`
- Evidence Level: `E4_PREPRINT / PEER-REVIEWED_PUBLICATION_IDENTITY_PRESENT`
- Mapping State: `DESIGN_ANALOGY`
- Implementation State: `REFERENCE_ONLY`
- Validation State: `NOT_TESTED`
- Formula/Theorem recertification in this correction: `PARTIAL — theorem/result surfaces above only`

The existence of an AAAI publication does not transfer the theorem into repository implementation or validation.

## Source surfaces checked

- arXiv: https://arxiv.org/abs/2312.15667
- AAAI publication: https://ojs.aaai.org/index.php/AAAI/article/view/29699

## Future cascade instruction

A future Weekly document cascade may weave this correction into the canonical Collaboration System document. When it does, it must preserve the historical source-revisit provenance and must not count the 2026-09-08 revisit as new independent support for S40.
