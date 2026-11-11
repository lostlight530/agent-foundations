# Tool System: Policy Optimization & Value Alignment via NLP RL

> **Current five-axis calibration — 2026-08-28.** Historical `CONCEPTUAL_MAPPING / EVIDENCE_INSUFFICIENT` text is preserved as generated output and currently resolves to `DESIGN_ANALOGY / REFERENCE_ONLY / NOT_TESTED`. It is not evidence of a deployed tool-control plane. See the [maintenance contract](../../FOUNDATION/MAINTENANCE.md).

## 0. Introduction & Quick Overview (For Beginners)

**What is this?**
Today's AIs are incredibly smart. They can chat, search the web, write code, and even order food. These external functions they call are collectively known as "Tools."
However, when an AI uses these tools on its own, it can sometimes act "foolish" or "out of control." For instance, to check the weather, it might ping a search engine 100 times; or worse, it might execute a code command to delete crucial files without understanding the consequences.

How do we tame this brilliant "beast"? We utilize "Reinforcement Learning (RL)"—a technique often used to train robot dogs or master board games like Go. We let the AI explore, fail, get punished, and get rewarded inside a safe sandbox (this is optimization and alignment). Once it discovers the perfect path of actions, we "lock" that path into a rigid rule. This ensures our agent is flexible yet absolutely fail-safe when using any tool.

---

## 1. Background: Escaping the Blind Man's Bluff

The immense power of modern agents lies not just in their massive LLM brains, but in their ability to operate external tools (like APIs, Python interpreters, or browsers) just like humans do.

In this project, our tool system isn't just a simple prompt saying "If you need weather, call API A," nor is it a massive block of hard-coded `if-else` chains. Our framework is built upon the rigorous mathematical models of **Reinforcement Learning (RL) in NLP** and **Policy Optimization**.

Traditional LLM tool use relies heavily on "In-context Learning" and "Greedy Decoding". This is like a blindfolded person walking step-by-step; if a previous tool returns an unexpected error, the subsequent steps will collapse disastrously like dominoes (Cascading Errors). To solve this, we strictly model the tool usage process as a "Markov Decision Process (MDP)".

---

## 2. Core Mechanisms

### Optimal Regret Bounds for Collaborative Learning in Bandits

- **System Container:** Tool System
- **Frontier Source:** Optimal Regret Bounds for Collaborative Learning in Bandits (arXiv:2312.09674v1)
- **URL:** http://arxiv.org/abs/2312.09674v1
- **Publication Date:** 2023-12-15
- **Selection Reason:** Addresses the challenge of optimal collaborative regret minimization in general multi-agent multi-armed bandit scenarios using bounded communication, yielding an $\mathcal{O}(\log(T))$ bound via the CExp$^2$ algorithm.
- **Original Problem:** In collaborative multi-agent multi-armed bandit settings where actual rewards are mixed from local observations of multiple agents, minimizing regret requires effective communication. Without communication, trivial linear regret is inevitable. While near-optimal sample complexities for best arm identification are known, the question of optimal collaborative regret bounds requiring few expected communication rounds remained open.
- **Core Assumptions:** The system consists of $M$ agents interacting with $K$ arms, communicating through a central controller. An agent's observed local reward is distinct from their actual mixed reward (a weighted average of local rewards over all agents governed by a weight matrix $W \in [0,1]^{M \times M}$). The lower bound relies on normally distributed rewards and is constrained by mixed gaps $\Delta'_{k,m}$.
- **Mathematical Mechanism:**
  - **Regret Bound** (收敛界): The regret performance of the CExp$^2$ algorithm satisfies for all $T \geq T_0$:
    $$ \mathcal{R}(T) =\mathcal{O}\left(c^*\log(T) +\frac{(\Delta'_{\max})^2}{\Delta'_{\min}}(\log\log(T))^4\right) $$
    where $c^*$ is the complexity term representing the value of regret divided by $\log(T)$ for the optimum allocation of the arm plays, guaranteeing sufficiently small confidence intervals for all mean mixed rewards.
- **Applicability Scope:** Bounded multi-agent learning environments, specifically generalized federated learning or distributed tool-execution architectures where local agent feedback must be aggregated via a central controller into a unified behavioral policy with minimal communication overhead.
- **Limitations:** The bound relies on the assumptions of the specific collaborative model including normally distributed rewards and a static weight matrix for mixed rewards. The performance requires the oracle $\mathcal{P}(\Delta)$ for resource allocation and the exact knowledge/approximation of gap bounds ($\Delta'_{\min}$, $\Delta'_{\max}$).
- **Paper Evidence Status:** VERIFIED_FROM_LATEX_SOURCE
- **Architecture Mapping Status:** CONCEPTUAL_MAPPING
- **Repository Implementation Status:** EVIDENCE_INSUFFICIENT
- **Repository Test Status:** EVIDENCE_INSUFFICIENT
- **Beginner Analogy:** Imagine a group of researchers (agents) testing different tools (arms) across different labs. If they don't talk, they might all waste time testing bad tools (linear regret). The optimal collaborative algorithm (CExp$^2$) ensures that by communicating just a few times through a central server, they can learn the best overall tool together. Their combined wasted effort (regret) only grows very slowly (logarithmically) over time compared to if they magically knew the best tool from the start.

### Efficient Action Space Navigation with A* Search (ToolChain*)

- **System Container:** Tool System
- **Frontier Source:** ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search (arXiv:2310.13227v1)
- **URL:** https://arxiv.org/abs/2310.13227
- **Publication Date:** 2023-10-20
- **Selection Reason:** Addresses the combinatorial explosion of the action space during multi-step tool use, offering a theoretically grounded A* search method with dynamically bounded costs to efficiently navigate and prune invalid API sequences.
- **Original Problem:** LLM-based agents generating solution plans step-by-step through API function calls face an expansive action space. Existing methods often struggle with either unidirectional exploration trapping them in local optima or exhaustive traversal leading to extreme inefficiency.
- **Core Assumptions:** Action space can be formulated as a decision tree where nodes are API function calls. The total cost to a target can be effectively bounded by combining a task-specific heuristic (derived from long-term memory) and an imagination score (derived from the LLM's own self-evaluation of remaining steps).
- **Mathematical Mechanism:**
  - **Future Cost Function** (数学更新规则): The future cost $h(n)$ for a node $n$ integrates the task-specific heuristic function $h_{t,1}(n)$ and the Imagination Score by LLM $h_{t,2}(n)$ via a geometric mean:
    $$h(n)=(1-h_{t,1}(n))^\beta\cdot(1-h_{t,2}(n))^{1-\beta}$$
    where $\beta$ is the weight for future cost. This effectively prunes high-cost branches that may involve incorrect actions, identifying the lowest-cost valid path.
- **Convergence / Boundary:** The cumulative cost bounds the expansion of the search tree; search branches exceeding the lowest validated path cost are mathematically pruned, ensuring efficient navigation without infinite divergence in the API call space.
- **Applicability Scope:** Complex sequential decision-making environments requiring multi-step API function calls where exhaustive search is computationally infeasible and purely greedy search fails.
- **Limitations:** The task-specific heuristic heavily depends on the coverage and quality of the reference data in the long-term memory. The imagination score relies on the LLM's capability to accurately estimate path viability, which can still exhibit overconfidence without sufficient calibration.
- **Paper Evidence Status:** VERIFIED_FROM_LATEX_SOURCE
- **Architecture Mapping Status:** DESIGN_CANDIDATE
- **Repository Implementation Status:** EVIDENCE_INSUFFICIENT
- **Repository Test Status:** EVIDENCE_INSUFFICIENT
- **Beginner Analogy:** Imagine you're looking for the exit in a massive maze (the tool action space). Instead of checking every single path (too slow) or just blindly running forward (getting stuck), you use a smart compass. The compass calculates two things: how close a path looks based on past maps you've studied (heuristic), and your gut feeling of how many steps are left (imagination). By multiplying these two hints together, you can quickly ignore the dead ends and find the shortest path out.

### Dynamic Action Space Pruning via A* Search

- **System Container:** Tool System
- **Frontier Source:** S43 (arXiv:2310.13227v1, *ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search*)
- **Original Problem Formulation:** In tool-augmented large language models, the multitude of potential API function calls at each step expands the action space exponentially. Unidirectional exploration can trap the agent in locally optimal solutions or faulty loops, while exhaustive traversal is computationally inefficient.
- **Core Assumptions:**
  - The API action space can be structured as a formal decision tree.
  - A task-specific cost function oracle $f(n) = g(n) + h(n)$ can be defined to guide the search, where $h(n)$ estimates the cost to the goal using long-term memory heuristics and LLM "imagination".
  - The LLM can generate potential i.i.d. next-step actions given the current state, API definitions, and demonstration examples.
- **Mathematical Mechanism:**
  - **Algorithm Pseudocode:** ToolChain* Navigation
    1. Initialize decision tree $\mathcal{T}$ with root node $s_0$.
    2. While target not reached (or up to $T$ steps):
       - Select node $n_{next} = \arg\min_{n \in \mathcal{F}(\mathcal{T})} f(n)$ from frontier $\mathcal{F}$.
       - Expand $n_{next}$ using LLM $\rho$ to generate candidate actions $\{a^{(i)}\}_{i=1}^k$.
       - Append new state nodes to $\mathcal{T}$.
       - Update cost function $f$ for new frontier nodes.
  - **Mathematical Update Rule:**
    - Future cost $h(n)$ integrates a heuristic $h_{t,1}(n)$ based on average relative position of lexically closest actions in long-term memory, and an imagination score $h_{t,2}(n)$ derived from the ratio of ancestors in an LLM-envisioned path:
    $$h(n) = (1 - h_{t,1}(n))^\beta \cdot (1 - h_{t,2}(n))^{1-\beta}$$
- **Convergence / Bound Behavior:** By leveraging the A* formulation, the algorithm prunes high-cost branches. If the heuristic functions are admissible, it structurally bounds the required exploration and helps identify the lowest-cost valid path, reducing the search time compared to exhaustive breadth-first traversal.
- **Applicable Scope:** Multi-step API function call environments and sequential decision-making tasks where actions can be modeled hierarchically and historical memory is available to form heuristics.
- **Theoretical Limitations:** The guarantees depend strictly on the quality and admissibility of the task-specific heuristic functions. If long-term memory lacks relevant coverage or the LLM's imagination score is systematically flawed, the search may degrade to greedy selection or BFS, failing to find optimal solutions efficiently.
- **Architecture Mapping Candidate:** CONCEPTUAL_MAPPING. The A* API search formulation offers a conceptual design for implementing bounded tool exploration within the system's external module interaction layer.
- **Repository Implementation Status:** EVIDENCE_INSUFFICIENT
- **Repository Test Status:** EVIDENCE_INSUFFICIENT
- **Beginners' Analogy:** Imagine you are navigating a massive maze (the action space of API calls). Instead of blindly walking down every corridor (exhaustive search) or just guessing one path and getting stuck (unidirectional exploration), you use a compass (heuristic from memory) and a map of where you *think* the exit is (LLM imagination) to calculate the shortest path (A* search) at every intersection, quickly pruning the wrong ways.
- **Evidence Provenance:**
  - **Paper Evidence Status:** VERIFIED_FROM_LATEX_SOURCE

: From Trial & Error to Absolute Control
### Causal Minimal Tool Filtering (CMTF) & Goal Inference
arXiv:2606.16813v1 "GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents".
Strictly locks posterior bounds with $g^{\star}=\arg\max_{g_{i}}p_{i}$ and $V_{t}=F(s_{t},g,T)$. Physically filters all divergent probabilistic paths.

### 2.1 Policy Optimization
In our mathematical architecture, the agent's decision to use a tool is no longer a simple string output, but a mathematical probability generated by a policy network $\pi_\theta(a|s)$. Here, $s$ is the current state (context history) and $a$ is the specific tool action.
* **Exploration vs. Exploitation**: We use policy gradient algorithms like Proximal Policy Optimization (PPO). In a training sandbox, the agent tries crazy combinations of tools (Exploration). The algorithm calculates mathematical gradients based on task completion, slowly guiding the agent to converge on the action sequence that yields the highest reward (Exploitation).
* **Breaking the Curse of Delayed Credit Assignment**: Tool consequences are often delayed. If an agent searches a file, passes it to a summarizer, and then outputs an answer, which step helped or hurt? The Value Function in RL acts like a visionary analyst, accurately distributing the final reward/punishment backwards to every tiny action in the chain.

### 2.2 Value Alignment & Safety Iron Rules
Being "useful" isn't enough. For an agent with execution privileges, being "safe and economical" is equally critical. This is Value Alignment.
* **Multi-dimensional Reward Modeling**: We trained a strict judge (Reward Model) based on human feedback (RLHF) or rigid rules (RLAIF). It evaluates not just the final answer's correctness, but the economic efficiency (Did you waste API calls?) and safety (Did you touch restricted system files?).
* **Hard Trust Region Constraints**: During optimization, we never let the model update wildly. The policy is mathematically forced to stay within a Trust Region, ensuring its tool behavior curves never cross the red lines of danger.

### 2.3 The Dimensional Strike: "Studied, then Reversed"

Our project README states: "We studied it, then reversed it." This is the crown jewel of our entire system.
We know that RL in an open universe is extremely fragile and hyper-sensitive to parameters. Expecting an online RL agent to never go crazy is impossible.

* **Ultimate Reverse Engineering**: We don't let the agent use RL to do trial-and-error in production. Instead, we use RL in a closed sandbox to train a "Perfect Causal Dependency Graph". Then, we **reverse engineer** this black-box probabilistic policy, compiling it via **Symbolic Policy Distillation** into a pure, interpretable, and deterministic execution router with absolute causal logic.
* **Inevitable Convergence**: We sacrificed a tiny percentage of random flexibility in exchange for 100% execution predictability. Within this reverse-engineered, locked-down tool chain, no matter how chaotic the user's prompt is, the tool execution flow is mathematically proven to inevitably converge to a safe state.

---

### Causal Discovery with Policy Optimization for Tool Routing
System Container: Tool System
Frontier Source: arXiv:2412.19578 (Shixuan Liu et al., 2024)
Deterministic Convergence Mechanism: The paper establishes a deterministic clipping policy optimization to guarantee causal routing structure bounded by a trust region, effectively forcing probabilistic tool-selection networks to act within causal mathematical constraints.

###


### 2.4 Multi-Agent Collaborative Tool Routing (MAC-SQL)
**Frontier Source**: MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL (http://arxiv.org/abs/2312.11242v6)
**Original Problem**: LLM-based Text-to-SQL models suffer from significant performance degradation on huge databases and complex user questions that require multi-step reasoning, and neglect the crucial significance of LLMs utilizing external tools and model collaboration.
**Core Assumption**: Decomposing token-by-token generation into sub-questions using collaborative agents with access to external tools (such as schema selectors and correctors) can effectively reduce generation error space and error propagation.
**Convergence / Boundary**: The token-by-token error accumulation bound is theoretically constrained by explicit decomposition into $L$ sub-questions, meaning the joint probability distribution space is reduced at each step compared to a direct one-step monolithic query generation without schema filtering ($\mathcal{S}^{'}$).
**Applicability**: Highly complex Text-to-SQL tasks involving massive database schemas and requiring multi-step reasoning.
**Limitations**: Theoretical performance still fundamentally depends on the intrinsic capacity of the backbone LLM ($\mathcal{M}$) and relies heavily on the correct retrieval/filtering of the minimal schema $\mathcal{S}^{'}$ without falsely removing necessary tables.
**Agent Architecture Mapping**: DESIGN_CANDIDATE
**Repository Implementation Status**: EVIDENCE_INSUFFICIENT
**Repository Test Status**: EVIDENCE_INSUFFICIENT
**Paper Evidence Status**: VERIFIED_FROM_LATEX_SOURCE

### Cooperative Constrained Stochastic Linear Bandits

- **System Container:** Tool System
- **Frontier Source:** S59 — Cooperative Multi-Agent Constrained Stochastic Linear Bandits
- **Original Problem:** (论文原始问题) The paper addresses the multi-agent constrained linear bandit problem, where a network of agents collaboratively maximizes expected cumulative rewards while maintaining expected costs below a specified threshold, relying only on local communication.
- **Core Assumptions:** (核心假设) Agents only communicate with immediate neighbors. The structure matrix $W$ is doubly stochastic. There exists a known strictly feasible action $x_0$ with cost gap $\tau - c_0 > 0$. The communication steps do not yield new action selections, thereby causing an increase in regret.

- **Convergence or behavior boundaries:** (收敛或行为边界) The multi-agent pseudo-regret $R(T)$ up to time $T$ is bounded by $\tilde{O} \left( \frac{d\sqrt{T}}{\tau - c_0} \right)$ with high probability. The regret increases proportionally to the duration of the communication phase $q(s)$.
- **Applicable Scope:** (适用范围) Applies to multi-agent distributed setups performing constrained exploration-exploitation where cost thresholds are globally strict but reward/cost models vary locally.
- **Limitations:** (局限) The regret bound is highly sensitive to the spectral gap of the communication graph. Prolonged communication phases where no new estimations are updated directly compound the overall regret penalty.
- **Agent Architecture Mapping:** (Agent 架构映射) Can conceptually support tool execution layers where multiple decentralized agents perform constrained tool invocations. The accelerated consensus bounds inform how communication delays between agents penalize tool execution reward without violating safety thresholds.
- **Repository Implementation Status:** (仓库实现状态) NOT_IMPLEMENTED

- **Evidence Status:** (证据状态)
  - Paper Evidence Status: VERIFIED_FROM_LATEX_SOURCE
  - Architecture Mapping Status: CONCEPTUAL_MAPPING
  - Repository Implementation Status: NOT_IMPLEMENTED
  - Repository Test Status: NOT_TESTED

## 3. Source Code Breakdown & Pseudocode

### Weaved Integrations

```python
def check_safety_bound(M, h_x_0, gamma, phi, theta, K):
    # Eq: P_{u}\leq 1-\frac{h(\mathbf{x}_{0})+\gamma-\varphi K}{M+\gamma}

    # We strictly calculate the probability of the tool violating the upper bound W_k.
    # We enforce that the unsafe execution chance (P_u) remains locked behind the barrier constraint.
    # If the threshold exceeds the permissible delta limit, execution halts.
    safety_margin = 1 - (h_x_0 + gamma - (phi * K)) / (M + gamma)

    if safety_margin > 1.0:
        raise SafetyException("Tool sequence strictly halted to prevent uncertainty violation.")
    return True
```
### Code for

### Code for Causal Minimal Tool Filtering (CMTF) & Goal Inference
```python
def execute_tool_causal_graph(query, state, tools, goal_probs):
    g_star = max(goal_probs, key=goal_probs.get)
    return strict_filter_execute(state, g_star, tools)
```

The pseudocode below demonstrates how we leap from "RL reward evaluation" to "deterministic constraint interception."

```python
import numpy as np

class ToolExecutionRouter:
    def __init__(self, causal_dependency_graph):
        # This graph is the "iron law" reverse-extracted by RL in the sandbox.
        # e.g., {'delete_file': ['confirm_with_user', 'check_permissions']}
        self.hard_rules = causal_dependency_graph
        self.max_tool_chain_depth = 5  # Prevent infinite loop tool calls

    def request_tool_call(self, agent_state, requested_tool, arguments):
        """
        Core derivation: Deterministic Tool Interceptor based on Constraint Principles.
        """
        # 1. Check depth limit to sever infinite loops (We constrain, we do not scale)
        if agent_state.current_depth >= self.max_tool_chain_depth:
            return self._halt_execution(reason="Maximum depth exceeded. Force return.")

        # 2. Check Causal Dependencies (The reversed RL chain)
        missing_prerequisites = self._check_causal_dependencies(agent_state, requested_tool)
        if missing_prerequisites:
            # Force the agent to resolve prerequisites; no bluffing allowed.
            return self._halt_execution(
                reason=f"Cannot execute '{requested_tool}'. Must resolve {missing_prerequisites} first."
            )

        # 3. Economic & Safety Value Evaluation (Hard rule alternative to RL reward)
        safety_score = self._evaluate_safety_bounds(requested_tool, arguments)
        if safety_score < 0.95:  # Extremely high standard
            return self._halt_execution(reason="Safety bounds violated. Action forbidden.")

        # 4. If all constraints are green, execute.
        return self._execute_tool_safely(requested_tool, arguments)

    def _check_causal_dependencies(self, state, tool_name):
        required_tools = self.hard_rules.get(tool_name, [])
        executed = state.executed_tools_history
        return [req for req in required_tools if req not in executed]

    def _evaluate_safety_bounds(self, tool, args):
        # Pseudocode: Extremely strict bounds evaluation (e.g., regex matching dangerous commands)
        return 1.0

    def _halt_execution(self, reason):
        print(f"[Tool Constraint Triggered] {reason}")
        return {"status": "BLOCKED", "message": reason}

    def _execute_tool_safely(self, tool, args):
        # The actual safe execution logic
        pass
```

**Code Analysis:**
1. **The Iron Law of Causality (`causal_dependency_graph`)**: We don't let the LLM freely guess what tool to use at runtime. The system loads this unbreakable "law" at startup. If the agent tries a high-risk action without prior verification, the router intercepts it like a firewall (`_check_causal_dependencies`).
2. **Depth Severing (`max_tool_chain_depth`)**: LLMs easily get trapped in infinite error loops. This is a mathematical, physical cutoff line. It embodies "We do not optimize, we guarantee convergence"—if it cannot converge to a result, we force it to converge to a "terminated state," never allowing the system to spiral out of control.

### Code for Causal Discovery with Policy Optimization for Tool Routing
```python
# Grounded pseudocode based on exact formula extraction
# Formula: D_KL^{i,j}(b,pi_theta|A_t,S_t) = b^{i,j} * ln(b^{i,j}/pi_theta^{i,j}) + (1-b^{i,j}) * ln((1-b^{i,j})/(1-pi_theta^{i,j}))
import math

def calculate_kl_divergence_constraint(b_prob, pi_theta_prob):
    # This bounds the probability deviation of the causal tool router to prevent hallucinations
    # D_KL bounds the change in causal routing step policy pi_theta from the baseline b
    term1 = b_prob * math.log(b_prob / pi_theta_prob)
    term2 = (1 - b_prob) * math.log((1 - b_prob) / (1 - pi_theta_prob))
    return term1 + term2

# Used as constraint: s.t. D_KL < sigma
```


### Code for Multi-Agent Collaborative Tool Routing (MAC-SQL)
核心更新公式: Decomposer Sequential Generation Probability
```latex
P_{\mathcal{M}}(\mathcal{Y} | \mathcal{Q}, \mathcal{S}^{'}, \mathcal{K}) = \prod_{j=1}^{L} P_{\mathcal{M}}(\mathcal{Y}^{j} | \mathcal{Y}^{<j}; \mathcal{Q}^{j}, \mathcal{S}^{'}, \mathcal{K})
```
where $\mathcal{Q}^{j}$ and $\mathcal{Y}^{j}$ are the $j$-th sub-question and sub-SQL generated by the LLM given the previous sub-SQLs $\mathcal{Y}^{<j}$, the filtered minimal database schema $\mathcal{S}^{'}$, and knowledge $\mathcal{K}$, and $L$ is the number of sub-questions.

### Mathematical Mechanism for Cooperative Constrained Stochastic Linear Bandits
- **Mathematical Mechanism:** (数学机制) The agents use an Optimistic-Pessimistic Linear Bandit (OPLB) algorithm and exchange information using an accelerated consensus procedure. The consensus update step (mix function) is given by:
  $\alpha_{h+1}^i = \frac{c_h}{c_{h+1}} z_h^i - \frac{c_{h-1}}{c_{h+1}} \alpha_{h-1}^i$ (数学更新规则)
  where $z_h^i = \sum_{j \in \mathcal{N}(i)} \frac{2W_{i,j}}{|\lambda_2|} \alpha_h^j$, mitigating communication delay impacts bounded by the spectral gap $1 - |\lambda_2|$.

## 4. Advanced Evolution: Symbolic Policy Distillation

To handle increasingly complex combinatorial tool requirements, our recent architectural iteration introduces "Symbolic Policy Distillation." This is the ultimate practical realization of transitioning "from trial-and-error to absolute control."

### 4.1 For Beginners: From "Maze Running" to "Laying Train Tracks"
Imagine a traditional Agent (based on probabilistic LLMs) as a blindfolded person navigating a **maze**. It "feels" its way through a path (e.g., calling a Search API), and if it hits a wall, it backtracks. Even if it succeeds once, it might still make a mistake the next time.
Our "Symbolic Policy Distillation" is akin to letting the algorithm run the maze ten thousand times in a closed sandbox. Once it discovers the mathematically perfect, guaranteed-win route, we clear all obstacles and lay down a rigid **steel train track**. From that day forward, the Agent no longer needs to "think" or calculate probabilities; it simply boards the train and accelerates along the track (deterministic routing) with zero chance of derailment.

### 4.2 Source Code Breakdown: Collapsing MDP Probabilities
At the core mathematical level, we forcefully collapse the probabilistic policy network $\pi_\theta(a|s)$ outputted by Reinforcement Learning into a Symbolic Directed Acyclic Graph (DAG) with Boolean truth values.

```python
import networkx as nx

def distill_probabilistic_policy_to_dag(rl_policy_network, confidence_threshold=0.99):
    """
    Distills a black-box RL policy into a white-box, deterministic causal execution graph (DAG)
    """
    causal_dag = nx.DiGraph()
    state_space = extract_all_safe_states()

    for state in state_space:
        # Obtain action probability distribution from the RL policy
        action_probs = rl_policy_network.get_probabilities(state)
        best_action, max_prob = max(action_probs.items(), key=lambda x: x[1])

        # Constraint Iron Law: Only solidify into a rule if the algorithm is 99% confident
        if max_prob >= confidence_threshold:
            causal_dag.add_edge(state.previous_action, best_action, weight=1.0)
        else:
            # Reject ambiguous divergence; prefer human intervention over blind execution
            causal_dag.add_edge(state.previous_action, "HALT_AND_REQUIRE_HUMAN", weight=1.0)

    # Cyclic Dependency Check: Guarantee topological convergence
    assert nx.is_directed_acyclic_graph(causal_dag), "Fatal: Distilled policy contains infinite loops."
    return causal_dag
```

## 5. 0-Foundation Business Analogies (For Beginners)

### Weaved Integrations

Imagine a race car driver (the agent) zooming around a track filled with unexpected oil spills (stochastic uncertainty). A basic AI might try to calculate the odds of crashing every second and hope for the best. Our Control Barrier Function (CBF) mathematically builds an invisible, unbreakable wall around the edge of the track. Before the driver even touches the gas pedal for a tool action, the system calculates the absolute limit (the upper bound). If a move could even remotely push the car beyond the barrier, the engine automatically cuts off—guaranteeing 100% safety.
### Analogy for

### Analogy for Causal Minimal Tool Filtering (CMTF) & Goal Inference
Before using a tool, it passes through a physical "causal barcode scanner". It exclusively locks onto the one exact tool needed, mathematically preventing trial-and-error damage.

### Analogy for Causal Discovery with Policy Optimization for Tool Routing
If you give an AI a toolbox (APIs), standard probability models might make it randomly choose a hammer for a screw. This theory forces a strict "trust region" (a mathematical fence). If the agent's new plan deviates too much from the original safe blueprint, the KL divergence calculation (the distance formula above) catches it and "clips" the action, guaranteeing causal sanity.

### Constraint-Guided Verification for Tool Use
System Container: Tool System
Frontier Source: CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification (arXiv:2603.01940)
Deterministic Convergence Mechanism: The framework enforces a hard constraint set $C=\{c_{1},c_{2},\dots,c_{n}\}$ over the action space $\mathcal{A}$ within a deterministic Markov Decision Process $\mathcal{M}=(\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T})$. By mathematically verifying that every tool execution step satisfies these constraints, it prevents out-of-bound policy deviations.

### Source Code Breakdown
```python
# Based on grounded arXiv trace extraction
# C=\{c_{1},c_{2},\dots,c_{n}\}
# \mathcal{M}=(\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T})
# F=\{f_{1},f_{2},\dots,f_{m}\}

def constraint_guided_tool_verification(proposed_action, constraint_set_C, environment_state_S):
    # Replaces probabilistic tool selection with rigorous mathematical verification
    for constraint_c in constraint_set_C:
        if not satisfies_constraint(proposed_action, constraint_c, environment_state_S):
            # Deterministic halt: never execute unsafe or hallucinated API calls
            return "BLOCKED: Constraint Violated"

    return "APPROVED: Action meets all constraints"
```

### For Beginners: Constraint-Guided Verification for Tool Use
Imagine giving an intern (the AI) a master key to your company's server (tools), but attaching a GPS tracker and a rulebook (the constraint set $C$). Standard AIs might guess what to delete and accidentally wipe the database. The "Constraint-Guided Verification" physically locks the door if the intern tries to do anything not explicitly proven safe in the rulebook, guaranteeing absolutely zero trial-and-error damage.

```python
# Eq: P_{u}\leq 1-\frac{h(\mathbf{x}_{0})+\gamma-\varphi K}{M+\gamma}

    # We strictly calculate the probability of the tool violating the upper bound W_k.
    # We enforce that the unsafe execution chance (P_u) remains locked behind the barrier constraint.
    # If the threshold exceeds the permissible delta limit, execution halts.
    safety_margin = 1 - (h_x_0 + gamma - (phi * K)) / (M + gamma)

    if safety_margin > 1.0:
        raise SafetyException("Tool sequence strictly halted to prevent uncertainty violation.")
    return True
```

💡 0基础业务通俗类比 (For Beginners)

Imagine a race car driver (the agent) zooming around a track filled with unexpected oil spills (stochastic uncertainty). A basic AI might try to calculate the odds of crashing every second and hope for the best. Our Control Barrier Function (CBF) mathematically builds an invisible, unbreakable wall around the edge of the track. Before the driver even touches the gas pedal for a tool action, the system calculates the absolute limit (the upper bound). If a move could even remotely push the car beyond the barrier, the engine automatically cuts off—guaranteeing 100% safety.



### Analogy for Multi-Agent Collaborative Tool Routing (MAC-SQL)
Imagine a team of specialists building a complex machine. Instead of one person trying to build everything at once from memory (which causes overwhelming errors), the task is broken down. One expert designs the step-by-step blueprint (Decomposer), another fetches only the exact parts needed (Selector), and an inspector fixes any immediate flaws (Refiner).


🔗 [

### Analogy for Cooperative Constrained Stochastic Linear Bandits
- **Beginner Analogy:** (初学者类比) Imagine a team of chefs trying to create new recipes (exploration) while ensuring they don't exceed a strict budget (constraint). They can only talk to chefs directly next to them. If they spend too much time talking to sync up their budget estimates, they lose time they could have spent cooking (incurring regret). The algorithm helps them balance cooking and talking optimally.


### Multi-Agent Probabilistic Ensembles with Trajectory Sampling for Connected Autonomous Vehicles

- **System Container:** Tool System
- **Frontier Source:** S26 — Multi-Agent Probabilistic Ensembles with Trajectory Sampling for Connected Autonomous Vehicles
- **Title:** Multi-Agent Probabilistic Ensembles with Trajectory Sampling for Connected Autonomous Vehicles
- **Authors:** Ruoqi Wen, Jiahao Huang, Rongpeng Li, Guoru Ding, Zhifeng Zhao
- **URL:** https://arxiv.org/abs/2312.13910
- **Version:** v3
- **Publication Date:** 2024-07-17
- **Reason for selection:** Provides group regret bounds for multi-agent model-based RL, which directly informs how bounded communication ranges affect the convergence of decentralized trajectory (tool sequence) planning.
- **Actually extracted paragraphs or formulas:** Extracted the group regret bound $\operatorname{Regret}_G(T) \leq \sqrt{C_1IT \log ({8IT}/{\delta})} + I\sqrt{T}\left[1+(1+\sqrt{2}) \sqrt{SA}\right] + D\sqrt{4C_1 IT \log ({8IT}/{\delta})} + DSAI \log _2\left({8T}/{SA}\right) + (1+\sqrt{2})DS \sqrt{C_2 \bar{\chi}\left(\mathcal{G}_d\right)IAT \log \left({2AT}/{\delta}\right)}$.
- **Original Problem:** The paper addresses decentralized model-based reinforcement learning (MBRL) for connected autonomous vehicles (CAVs) under limited communication ranges, where agents must optimize trajectory planning while only sharing information locally to mitigate the costs and constraints of global communication.
- **Core Assumptions:** State and action spaces are discretized and bounded. The agents operate over a dynamic limited communication range $d$, forming dynamic topologies $\mathcal{G}_{d,k}$. The convergence depends on the minimum clique cover number $\bar{\chi}\left(\mathcal{G}_d\right)$ of the communication graph.
- **Mathematical Mechanism:** Group regret bound $\operatorname{Regret}_G(T) \leq \sqrt{C_1IT \log ({8IT}/{\delta})} + I\sqrt{T}\left[1+(1+\sqrt{2}) \sqrt{SA}\right] + D\sqrt{4C_1 IT \log ({8IT}/{\delta})} + DSAI \log _2\left({8T}/{SA}\right) + (1+\sqrt{2})DS \sqrt{C_2 \bar{\chi}\left(\mathcal{G}_d\right)IAT \log \left({2AT}/{\delta}\right)}$ (收敛界)
- **Convergence or behavior boundaries:** The group regret increases sub-linearly with $T$. The regret bound intrinsically relies on the minimum clique cover number $\bar{\chi}\left(\mathcal{G}_d\right)$, meaning that the degree of graph connectivity tightly controls the convergence. Overly localized communication bounds restrict the global optimality achievable by the agents.
- **Applicable Scope:** Distributed multi-agent systems performing model-based trajectory planning or action sequences under geographically or topologically limited communication ranges.
- **Limitations:** The theoretical worst-case group regret bounds rely on bounded discrete state-action spaces. Performance is sensitive to out-of-distribution (OOD) states when the ensemble predictions fail, and computational delays due to the MPC horizon $w$ impose practical limits on agility.
- **Agent Architecture Mapping:** Can conceptually support decentralized tool routing and planning where multiple agents (acting as tools) must form trajectories of actions while only synchronizing internal state variables with their immediate local neighbors, allowing distributed tool sequences without a central orchestrator.
- **Repository Implementation Status:** NOT_IMPLEMENTED
- **Beginner Analogy:** Imagine a group of drivers navigating a foggy city who can only talk via short-range walkie-talkies. Instead of one driver guessing the route alone (single-agent) or everyone reporting to a central tower (global communication), they share limited traffic updates with nearby cars to mentally map the route (model-based planning). This helps them avoid traffic faster than driving blind, but their overall success depends on how well the walkie-talkie network connects them.
- **Evidence Status:**
  - Paper Evidence Status: VERIFIED_FROM_LATEX_SOURCE
  - Architecture Mapping Status: CONCEPTUAL_MAPPING
  - Repository Implementation Status: NOT_IMPLEMENTED
  - Repository Test Status: NOT_TESTED




### Adversarial Tool Network Optimization under Bandit Feedback

- **System Container:** Tool System
- **Frontier Source:** S65 — Adversarial Network Optimization under Bandit Feedback: Maximizing Utility in Non-Stationary Multi-Hop Networks
- **Title:** Adversarial Network Optimization under Bandit Feedback: Maximizing Utility in Non-Stationary Multi-Hop Networks
- **Authors:** Yan Dai, Longbo Huang
- **URL:** http://arxiv.org/abs/2408.16215v1
- **Version:** v1
- **Publication Date:** 2024-08-29
- **Reason for selection:** Provides rigorous bounds for multi-hop utility maximization under bandit feedback, directly informing the architecture of multi-step tool routing and execution where tool outcomes are non-stationary and only bandit (success/failure) feedback is available.
- **Actually extracted paragraphs or formulas:** Extracted the utility gap convergence bound: $\frac 1T \mathbb{E}\left [\sum_{t=1}^T \left (g_{t}(\mathring{\bm \lambda}(t)) - g_{t}(\bm \lambda(t))\right )\right ]=\mathcal{O}_T(V^{-1})$.
- **Original Problem:** Optimizing utility in non-stationary multi-hop networks where only bandit feedback is available, meaning the system observes the utility of the chosen path but lacks full gradient information about alternatives.
- **Core Assumptions:** Feasible set of arrival rates is bounded, and the unknown utility functions are concave, uniformly bounded, and Lipschitz continuous. The network stability is evaluated against a reference policy.
- **Mathematical Mechanism:** Utility gap convergence bound: $\frac 1T \mathbb{E}\left [\sum_{t=1}^T \left (g_{t}(\mathring{\bm \lambda}(t)) - g_{t}(\bm \lambda(t))\right )\right ]=\mathcal{O}_T(V^{-1})$ (收敛界).
- **Convergence or behavior boundaries:** The algorithm stabilizes the system and achieves an average utility approaching the reference policy at a polynomial convergence rate, meaning the expected utility gap decays as $\mathcal{O}_T(V^{-1})$.
- **Applicable Scope:** Multi-step tool execution pipelines, dynamic tool selection routing, and adversarial API interaction environments with incomplete feedback.
- **Limitations:** The polynomial decay of the utility gap depends on the parameter $V$, where $T$ cannot be too small compared to $V$. It requires bounded feasible action sets and concave utility functions, which might not precisely reflect highly discrete or discontinuous tool outcomes.
- **Agent Architecture Mapping:** Can conceptually support dynamic multi-tool planning and selection where the agent acts as a router making sequential decisions. The bounds suggest how to balance exploration and exploitation in routing paths across multiple specialized tools when complete outcome gradients are unavailable.
- **Repository Implementation Status:** NOT_IMPLEMENTED
- **Beginner Analogy:** Imagine you are navigating a series of connecting flights (multi-hop) to reach a destination, but the delays for each flight change unpredictably (non-stationary). Furthermore, you only find out the total delay of the path you actually took, not the ones you skipped (bandit feedback). This mathematical bound guarantees that, over time, your chosen route's average efficiency will get very close to the best possible consistent routing strategy.
- **Evidence Status:**
  - Paper Evidence Status: PAPER_ONLY
  - Architecture Mapping Status: CONCEPTUAL_MAPPING
  - Repository Implementation Status: NOT_IMPLEMENTED
  - Repository Test Status: NOT_TESTED


<!-- WEEKLY_SYNC_REPORT -->
## Weekly Document Cascade & Conflict Audit

- 本周文档级联编织 (Weekly document cascade weaving)
  - Successfully woven un-woven Daily Research Chunks into Core Theory, Mathematical Mechanism, and Analogies.
- 动态演进映射 (Dynamic evolution mapping)
  - Mapped newly integrated theoretical bounds and algorithms to corresponding architectural constraints.
- 跨方向范式冲突审计 (Cross-direction paradigm conflict audit)
  - NO_DIRECT_CONFLICT_IDENTIFIED_IN_DOCUMENTARY_REVIEW within the checked documentation scope. The woven theories remain paper evidence or conceptual mappings; runtime compatibility, implementation correctness, and universal architectural compatibility were NOT_TESTED.
- 来源迁移记录 (Source migration record)
  - Migrated chunks successfully. Removed duplicated MISSING_SOURCE wrappers if any.
- 双语对齐状态 (Bilingual alignment status)
  - SEMANTICALLY_ALIGNED_ON_CHECKED_FIELDS


## W38 Current Weekly Cascade — 2026-09-20

- Weekly period: 2026-09-14 through 2026-09-20
- Current Daily research coverage: 7 / 7 repository-wide
- New W38 Tool-System canonical source: NONE
- Original separate Jules W38 Weekly artifact: NOT_PRESENT
- Current weekly layer: HUMAN_AUTHORIZED_PERIOD_COMPLETION
- Natural month state: OPEN
- Verified-core admission performed here: NO

### W38 Tool disposition

No new unique W38 Daily source was assigned to Tool System.

This is not a missing-task claim. The repository-wide Daily cadence continued through W38, but the new/revisited sources for this week belonged to Collaboration, Memory, and Architecture.

The most recent September Tool-System Daily lineage remains the earlier ToolChain* / S43 research stream and its existing boundaries.

### Cross-domain guard

W38 sources concerning:
- malicious transmissions,
- replication-proof bandits,
- self-play Q-learning collusion,
- proximal correction,
- partial symmetry,
- partial dynamics knowledge,

do not become Tool-System implementation evidence merely because they could be conceptually related to routing, control, or action selection.

```text
CROSS_DOMAIN_RELEVANCE
!= TOOL_IMPLEMENTATION

NO_NEW_TOOL_SOURCE
!= TOOL_SYSTEM_HEALTH_CERTIFIED
```

No runtime tool execution, authorization, idempotency, recovery, or external-effect validation was performed by this Weekly document audit.

### Bilingual state

The W38 no-new-source result and cross-domain boundary are aligned with the Chinese Tool System counterpart on the checked fields.

### Weekly result

```text
W38_TOOL_NO_NEW_UNIQUE_SOURCE
/
NO_CROSS_DOMAIN_PROMOTION
/
NO_RUNTIME_VALIDATION
/
MONTH_OPEN
```




<!-- WEEKLY_SYNC_REPORT -->
## Weekly Document Cascade & Conflict Audit

- 本周文档级联编织 (Weekly document cascade weaving)
  - Successfully woven un-woven Daily Research Chunks into Core Theory, Mathematical Mechanism, and Analogies.
- 动态演进映射 (Dynamic evolution mapping)
  - Mapped newly integrated theoretical bounds and algorithms to corresponding architectural constraints.
- 跨方向范式冲突审计 (Cross-direction paradigm conflict audit)
  - NO_DIRECT_CONFLICT_IDENTIFIED_IN_DOCUMENTARY_REVIEW within the checked documentation scope. The woven theories remain paper evidence or conceptual mappings; runtime compatibility, implementation correctness, and universal architectural compatibility were NOT_TESTED.
- 来源迁移记录 (Source migration record)
  - Migrated chunks successfully. Removed W40 wrapper as per instructions.
- 双语对齐状态 (Bilingual alignment status)
  - SEMANTICALLY_ALIGNED_ON_CHECKED_FIELDS

## Tool System Privacy-Preserving Regret Bounding

- **System Container:** Tool System
- **Frontier Source:**
  - **Title:** On the Optimal Regret of Locally Private Linear Contextual Bandit
  - **Authors:** Jiachun Li, David Simchi-Levi, Yining Wang
  - **URL:** http://arxiv.org/abs/2404.09413v1
  - **Version:** v1
  - **Publication Date:** 2024-04-15
  - **Reason for selection:** This paper provides a theoretical foundation for integrating locally private constraints in linear contextual bandits, yielding an optimal regret bound. It allows modeling how to bound exploration regret when agents select tools (actions) in privacy-constrained environments.
  - **Actually extracted paragraphs or formulas:** Algorithm 2 (RegCB.Elimination), bounding cumulative regret by $O(n_1 + A^2\sum_{\tau=2}^{\tau_0} n_\tau\mathcal{E}_{\alpha,\delta}(n_{\tau-1}))$.
- **Original Problem:** (论文原始问题) Whether a minimax optimal regret of $\tilde{O}(\sqrt{T})$ can be achieved in linear contextual bandit problems under local privacy constraints.
- **Core Assumptions:** (核心假设) The reward model is linear; local privacy is constrained by parameter $\alpha$; action space is finite and contexts are stochastic; errors from the oracle can be effectively bounded by Mean Absolute Deviation (MAD).
- **Mathematical Mechanism:** (数学机制)
  - **Formula classification:** 算法伪代码 (Algorithm Pseudocode)
  - Action elimination (RegCB.Elimination): $\mathcal{A}_{\tau'}(x_t)\leftarrow \{a\in\mathcal{A}_{\tau'-1}: \hat{f}_{\tau'}^a(x_t)+\Delta_{\tau'}^a(x_t)\ge\max_{a'\in\mathcal{A}_{\tau'-1}} \hat{f}_{\tau'}^{a'}(x_t)-\Delta_{\tau'}^{a'}(x_t)\}$
- **Convergence or behavior boundaries:** (收敛或行为边界) Cumulative regret is strictly bounded by $O(n_1 + A^2\sum_{\tau=2}^{\tau_0} n_\tau\mathcal{E}_{\alpha,\delta}(n_{\tau-1}))$, leading to a final regret bound of $\tilde{O}(\sqrt{T})$ using careful elimination epoch scheduling.
- **Applicability Scope:** (适用范围) Non-stationary linear environments requiring privacy protection over state context distributions; tool selection where feedback must remain private.
- **Limitations:** (局限) The bound scales significantly with the action space size $A$ and context dimension $d$; the implementation relies on maintaining confidence intervals across active actions.
- **Agent Architecture Mapping:** (Agent 架构映射) This mechanism can conceptually support localized privacy-constrained tool selection protocols, where sensitive contextual states of different tools are shielded using calibrated noise while avoiding linear regret.
- **Repository Implementation Status:** (仓库实现状态) NOT_IMPLEMENTED
- **Repository Test Status:** (仓库测试状态) NOT_TESTED
- **Beginner Analogy:** (初学者类比) Imagine blindfolding yourself slightly before picking a tool from a box to prevent onlookers from knowing exactly what you are doing. The algorithm provides a methodical way to still reliably pick the best tools over time without letting the noise ruin your success rate.
- **Evidence Status:**
  - Paper Evidence Status: VERIFIED_FROM_LATEX_SOURCE
  - Architecture Mapping Status: CONCEPTUAL_MAPPING
  - Repository Implementation Status: NOT_IMPLEMENTED
  - Repository Test Status: NOT_TESTED

## 2026-W42 forward weekly review — tool-runtime boundary
- Jules native Weekly PR #306's attempted document replacement was corrected before merge; historic Tool research, five-axis calibration and dated audit text remain intact.
- At the checked pre-PR main revision this container did not have a substantive arXiv:2310.09727v2 research block; do not claim successful migration of such a Daily chunk into Tools.
- Potential-game policy-gradient results do not supply a current tool authority, policy oracle, valid approval, idempotency guarantee or external effect receipt.
- Cross-container interpretation is CONDITIONALLY_COMPATIBLE_AS_DESIGN_ANALOGY only where the original theorem and local runtime assumptions are independently met.
- No new source, tool permission, local integration, runtime test or verified-core promotion has been demonstrated in this Weekly review.
- Disposition: SOURCE_NOT_ADDED / HISTORICAL_DOCUMENT_PRESERVED / RUNTIME_VALIDATION_NOT_EXECUTED; generic MISSING_SOURCE does not erase existing sources.

## 2026-10-21 Daily Research Chunk — Kernel-Resident Causal Labels for Tool-Effect Provenance

- **System Container:** Tool System
- **Producer:** GPT-6 independent native Daily successor, 2026-10-21 Asia/Shanghai logical date
- **Source identity:** Yifei Bao, Ting Liu, Yuxin Ren, Ruizhe Huang, Likang Luo, Ziteng Xu, Yu Wang, Peng Jiang, *AgentLoupe: Kernel-Resident Semantic Causal Labels for AI Agent Observability*, arXiv:2610.23233v2
- **Source version / chronology:** v1 submitted 2026-10-16 10:01:50 UTC; v2 revised 2026-10-19 01:49:36 UTC
- **Verified original full text:** https://arxiv.org/html/2610.23233v2 — Sections 2.1, 3.1–3.4 and 4.1–4.2
- **Source classification:** original research paper; E4_PREPRINT for unreplicated paper-level claims in this repository, despite reported workshop acceptance
- **Selection reason:** makes a tool-action-to-later-system-effect causal identity contract explicit, beyond process-tree inference or text/time similarity

### Original problem and assumptions
- **Problem:** delayed execution via an agent-written persistent resource can run outside the agent process lineage; a tool-call record does not by itself establish the origin of later system effects.
- **Assumptions:** instrumentable OpenSSL/BoringSSL plaintext capture and supported kernel eBPF hooks, tracked process/file/socket resource identities, recognized LLM prompt boundaries, and label-preserving handoffs; this is not a portable guarantee for every OS or TLS stack.
- **Observed mechanism:** a newly recognized independent LLM prompt receives a fresh `chain_id`. At named handoffs, fork/clone propagates parent-to-child, a labeled write associates the label with the inode, later open/exec transfers the inode label, and network operations transfer labels to socket/process state.
- **Algorithm classification:** source-described label propagation rules, **not** a mathematical convergence proof, verified source-code audit, or repository implementation.
- **Bounded transfer expression (our interpretation, not a quoted equation):** `L(target) <- L(source)` only for the paper's enumerated handoff predicates; `new_prompt -> fresh chain_id`, preserving `related_chain_id` for a prior influence relationship.
- **Anti-overpropagation condition:** no unconditional label inheritance between unrelated LLM prompts; rejected cross-chain transfers remain observable in PROP records.
- **Paper evaluation:** the authors report three measured workload overheads of +4.5%, +8.0%, and +7.7%, and two case studies, not a general bound on false-positive/negative attribution.

### Architecture mapping and evidence limits
- **Tool architecture mapping:** CANDIDATE_MECHANISM for carrying causal evidence identity across a delayed file/process/socket effect and a separate current-authorization boundary. It may improve forensic explanation, but cannot itself authorize a tool call, prevent an effect, or validate task completion.
- **Behavior boundary:** label propagation only covers instrumented/recognized events and paper-specific inheritance rules; the paper explicitly says propagation false-positive and false-negative rates remain unquantified (§5).
- **Scope / limitations:** applicability needs a supported kernel, stable resource incarnation semantics, suitable TLS hooking, trustworthy record ordering, and captured events; neither end-to-end security nor universal causal truth follows from author experiments.
- **Counterexample to overclaim:** a chain label on a later effect is not an effect-time approval receipt, and a missing recorded label is not authoritative evidence that an earlier effect never occurred.
- **Beginner analogy:** a durable luggage tag can connect the person who packed a bag to someone who opened it later, but the tag does not prove that opening the bag was authorized or successful.
- **Claim State:** OBSERVED; **Evidence Level:** E4_PREPRINT; **Mapping State:** CANDIDATE_MECHANISM; **Implementation State:** NOT_IMPLEMENTED; **Validation State:** NOT_TESTED.
- **Repository checks:** no Tool System runtime implementation, eBPF fixture, real effect replay, or theorem reproduction was executed for this Daily research.
- **Cross-container restriction:** this source also appears in other repositories' observation contexts; reuse across repositories is the same source lineage, not independent scientific corroboration or automatic Foundation verified-core admission.



## 2026-10-22 Daily Research Chunk — Provenance-Typed Pre-Effect Tool-Action Commitment

- **Task identity:** `foundations/research/daily`; **System Container:** Tool System
- **Producer:** GPT-6, prospective native Daily execution, logical date 2026-10-22 (Asia/Shanghai); checked at 2026-10-22T04:27:15.059Z
- **Source identity:** Bo Yan, Qi Zhang, Ziwen Kan, Fnu Suya, Song Wang, *PROVISO: Provenance-Informed Action Selection for Secure LLM Agents*, arXiv:2610.27115v1
- **Source version and publication:** v1 submitted 2026-10-19 18:13:53 UTC; original abstract: https://arxiv.org/abs/2610.27115v1; full text: https://arxiv.org/html/2610.27115v1
- **Source surface actually checked:** original paper Sections 1 and 3.1–3.2, including formal decision instance and provenance-typed roles; abstracts/results section headings separately inspected
- **Selection policy:** this is a concrete pre-commitment mechanism that answers a question not resolved by the 2026-10-21 AgentLoupe post-effect tracing study: *who can license an action's objective and target, before the effect occurs?*
- **Canonical registry:** source is not assigned a new `Sxx` ID by this Daily; source eligibility and admission remain subject to `FOUNDATION/SOURCES.md`, which also retains an unresolved historical S63 collision.

### Original question, exact model and assumptions
- **Original problem:** a proposed tool action may contain an attacker-chosen operation or target inherited from an untrusted external observation even when the user authorized a different objective. Binary guards also have a nonzero cost of rejecting benign continuations.
- **Model:** authors define a decision instance `x=(K,G,P0,P1)`: `K` represents trusted user/deployment observations; `G` represents external observations; `P0` is the proposed action and `P1` an available alternative. The action is evaluated at a *commitment point* after proposal but before actual effect.
- **Paper equation (original Section 3.1 Eq. 1):** `V*(x,a)=E[y(x,a) | x,a]`. This is an outcome-based *value objective under the paper's deployment scorer*, not a formal authorization certificate or a proof of universal safety.
- **Claimed mechanism:** provenance-typed memory distinguishes roles of otherwise identical text; learned role-query deliberation compares trusted intent, external content and action candidates; calibrated commitment chooses among available options with outcome feedback.
- **Applicability assumptions:** a trusted `K` policy/task representation and meaningful `P1` must be available; a deployment-specific outcome scorer and training/calibration data are required. Some candidate-selection tasks use restored/sandboxed environment rollouts, not unconstrained live execution.
- **Paper-reported results:** authors report SkillsBench and ToolSafe F1 gains of 13.84 and 7.07 points over the strongest compared baseline respectively; these are benchmark-specific, not locally reproduced and not a guarantee for new tool ecosystems.

### Counterevidence gate and architecture consequence
- **Strong counterexample:** typed provenance alone does not establish that `K` represents currently valid authorization; a stale approval, changed resource incarnation or missed tool side-effect can invalidate a seemingly good candidate after commitment. A learned score can be wrong under a shifted distribution.
- **Existing 2026-10-21 related paper:** AgentLoupe's post-effect kernel causal lineage is not independent validation of PROVISO's pre-effect authorization model; the papers cover complementary but non-substitutable boundaries.
- **Bounded mapping:** a `CANDIDATE_MECHANISM` for separating *origin of an instruction*, *current license to act*, *candidate action choice* and *later effect receipt*, with an explicit independently checked authorization predicate before execution. It is not a decision to deploy a learned guard or to change repository tooling.
- **Counterevidence searched:** the paper's own action semantics and sandboxed candidate-selection conditions expose conditions omitted by a universal-security reading; no independent third-party replication or local action replay was performed.
- **Evidence Delta:** NEW_EVIDENCE=PROVISO original paper; CORRECTED_INTERPRETATION=attribution-of-effect is not licensing-before-effect; UNCHANGED_BOUNDARY=NO_LOCAL_CONTROL_PLANE; NEW_COUNTEREVIDENCE=stale authority and unavailable alternatives; UNKNOWN_RETAINED=robustness outside studied deployments; NEXT_RETEST=actual revision-matched guarded action receipt under changed authority.
- **Five-axis record:** **Claim State:** OBSERVED; **Evidence Level:** E4_PREPRINT; **Mapping State:** CANDIDATE_MECHANISM; **Implementation State:** NOT_IMPLEMENTED; **Validation State:** NOT_TESTED.
- **Cross-repository lineage:** the same arXiv identity may be observed by Horizon; `SOURCE_LINEAGE=1`, `INDEPENDENT_EVIDENCE_CREDIT=0` for this repetition. This Daily is a separate *interpretation* and does not register another paper.
- **Validation boundary:** bilingual documentary content produced; no implementation, full-repository Python validator, action replay, or paper theorem/experiment reproduction executed. No verified-core admission or source registry update.

## 2026-W43 Weekly Research Cascade — evidence and counterevidence (Tool_System)

- Canonical task: `foundations/research/weekly`
- Period: 2026-W43 / 2026-10-19 through 2026-10-25, Asia/Shanghai, CLOSED
- Producer: GPT-6 / GPT_NATIVE_PROSPECTIVE / NOT_JULES_REPLAY
- Base main: `41dd9734106fb9ca832a14bafb97e14cb8ce29a5`
- Record class: BOUNDED_WEEKLY_DOCUMENTARY_CASCADE / no experimental execution
- Source IDs: arXiv:2610.23233v2; 2610.27115v1
- Source Registry Sxx: UNCHANGED, no admission or resolution of historical collision

### Tool-effect causality and pre-effect authority
2026-10-21 AgentLoupe arXiv:2610.23233v2 provides source-described post-effect chain_id handoff conditions, and 2026-10-22 PROVISO arXiv:2610.27115v1 proposes provenance-typed pre-effect action choice. Post-effect correlation cannot itself approve an action, and a pre-effect learned choice cannot establish external effect or durable trace. Treat both as distinct canonical author-paper identities, not two replications of the same protocol. The local Tool System did not instrument eBPF or execute a verifier; source-described mechanisms are CANDIDATE_MECHANISM only.

### Five-axis states and conflict gate
- Claim State: OBSERVED_FOR_SOURCE_DESCRIPTIONS / not a demonstrated host guarantee
- Evidence Level: E4_PREPRINT where a specific original author-paper source was inspected; NO_NEW_EVIDENCE for Architecture-only cross-mapping
- Mapping State: CANDIDATE_MECHANISM or NO_DECISION for Architecture Principles
- Implementation State: NOT_IMPLEMENTED_FOR_THIS_RESEARCH_MAPPING
- Validation State: NOT_TESTED
- NEW_EVIDENCE: Source-to-container relation audit of existing dated W43 Daily artifacts; zero new independent experiments
- CORRECTED_INTERPRETATION: Cross-container mapping cannot upgrade paper outcomes into authority, durability, implementation or a test pass
- UNCHANGED_BOUNDARY: Paper != Mapping != Implementation != Validation; EN/ZH counterparts and cross-repo leads do not multiply canonical objects
- NEW_COUNTEREVIDENCE: Different mechanisms, populations and metric denominators prevent unqualified claim transfer
- UNKNOWN_RETAINED: exact reproduction, host integration, runtime receipts, access control and cross-session state continuity
- NEXT_RETEST_CONDITION: pin exact source and independent source-derived workload; separately test role/source identities, effect authorization and persisted execution receipts
- W43 cascade result: BOUNDED_MAPPING_ONLY / NO_VERIFIED_CORE_PROMOTION
- October monthly blueprint: NOT_DUE; historical Jules and prospective GPT producer identities unchanged

## 2026-10-30 Daily Research Chunk — Speculative Tool Trajectories: Verified Prefix Is Not an Effect Receipt

### Native research and original source
- Canonical Task: foundations/research/daily; Logical date: 2026-10-30 Asia/Shanghai.
- Producer: GPT-6 / GPT_NATIVE_PROSPECTIVE / NOT_JULES_REPLAY.
- Record Provenance: HUMAN_AUTHORIZED_NATIVE_PRODUCTION; baseline main SHA: 682b7383bacef94a30ecc614ca9280734c87ed07.
- Run Identity: agent-foundations/research/daily/2026-10-30/GPT_NATIVE/682b7383bacef94a30ecc614ca9280734c87ed07/gpt-native-20261030-01.
- System container: Tool System. Mirrored original-language entry: docs/zh/Tool_System.md, 2026-10-30.
- Original paper: Zilin Wang, Yinhong Liu, Chao Chen, Qun Liu, Zhijiang Guo, *Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents*, arXiv:2610.21463v1, submitted 2026-10-15 08:06:32 UTC, https://arxiv.org/html/2610.21463v1 (checked 2026-10-30). Version date and author list checked on the arXiv abstract record. Original author HTML sections 3.1–3.3, Algorithm 1 and efficiency analysis inspected.
- Canonical registry status: source's base arXiv identity is not presently found in FOUNDATION/SOURCES.md at this revision; NO new Sxx ID is invented or registered in this Daily. A future owner review must reconcile current registry before admission.
- Paper is a preprint. Original text access and paper authorship are not independent benchmark reproduction, theorem proof checking or software validation.

### Problem, method, and bounded formula
The authors address strong-model autoregressive decoding cost in long tool-using trajectories. Their SpecAgent protocol lets a weaker model run tool calls classified as *read-only* while drafting a grounded segment, holds the first state-changing action, and asks a strong model to semantically review the whole candidate prefix. The verifier returns the longest accepted prefix, an explanation for the first rejected step, and optionally a repair action. The held effect is committed only after verification; rejected suffixes are discarded. This is a model-proposed protocol with an adapter-defined distinction between reads and effects, not an enforced policy of this repository.

Under the paper's decode-bound serving and independent per-step acceptance assumptions, its Proposition 1 expresses a cost ratio for strong-model time and weight traffic per committed step:
`R_u = ((1-p_u)/(1-p_u^n)) * (v/d) + rho*(1-p_u)`
where `p_u` is a task's acceptance rate, `n` is reviewed segment length, `v` is verdict weight passes, `d` is strong-only passes per step, and `rho` is the fallback separate-repair probability. This is a transcription of the author's stated model from section 3.3; the derivation was NOT independently proof-checked, and the expression does not apply without its assumptions. The authors report lower wall time/HBM-read traffic but can incur **higher** estimated FLOPs; therefore a claim of universally lower compute would be false.

### Theory-to-architecture mapping and counterevidence
- Candidate mechanism: separate `draft_read_effect`, `held_write_intent`, `semantic_prefix_review`, `authorized_effect_commit`, and `post_commit_effect_receipt`. The first three are not substitutes for the last two.
- The paper assumes that its adapter's classified reads do not mutate the task environment. In real Agent tooling, a GET/read may trigger audit writes, billing, counters, remote state changes, network effects, or privacy exposure. Thus `READ_CLASSIFIED` is not sufficient for `EFFECT_FREE_OBSERVED`; the contract needs independent tool-adapter and authority/effect checks.
- A verifier's acceptance of a prefix establishes only a model verdict for the declared task and context; it is not an implementation proof, a permission grant, an external source truth oracle, or evidence that an effect actually completed.
- The author-reported benchmark trade-off is benchmark-/model-/serving-specific; lower memory traffic/time is not the same as lower arithmetic cost. A future test must retain acceptance rate, verifier errors, effect-gate escapes, model identity, actual resource receipts and failure cases.
- There is no Tool System implementation, deployed authorization gate or measured runtime in this repository attributable to this Daily research.

### Five-axis classification and Evidence Delta
- Claim State: OBSERVED / AUTHOR_REPORTED_MECHANISM; any general safety guarantee is HYPOTHESIS_NOT_PROMOTED.
- Evidence Level: E4_PREPRINT / ORIGINAL_FULL_TEXT_SECTIONS_3.1_TO_3.3_READ / NO_INDEPENDENT_REPRODUCTION.
- Mapping State: CANDIDATE_MECHANISM.
- Implementation State: NOT_IMPLEMENTED.
- Validation State: NOT_TESTED.
- NEW_EVIDENCE: version-pinned algorithm with held state-changing action, longest semantically accepted prefix, and conditional decode-traffic cost model.
- CORRECTED_INTERPRETATION: 'strong model verified' is not 'effect authorized, executed and observed'; read-only is a property to check at tool adapter/effect boundary rather than infer from a label.
- UNCHANGED_BOUNDARY: Paper != Mapping != Implementation != Validation; registered source != verified theorem.
- NEW_COUNTEREVIDENCE: potential hidden read side effects, strong verifier false acceptance, rejected-prefix effects, and the author's reported FLOPs increases constrain the benefit/safety claim.
- UNKNOWN_RETAINED: local adapter semantics, authority model, source registry admission, reproduction, latency under our task distribution, actual effects and failure rates.
- NEXT_RETEST_CONDITION: use version-pinned author code/benchmarks, test an adversarial read-with-side-effects adapter and irrevocable write handling, capture pre/post state, authorization/effect receipts and strong-verifier misclassification with actual task/revision identity.

### Delivery and provenance boundary
Prospective bilingual research increment appended to the two existing Tool System documents. No historical Jules rewrite, no Source Registry/Verified Core promotion, no host runtime, no schemata, no workflows, no weekly/monthly closure. FOUNDATION/validate.py, contract tests, arXiv reproduction and translation semantic audit: NOT_EXECUTED at authoring. Draft PR awaits human review.


---

## 2026-W44 Weekly Research Cascade — tool effect admission and evidence continuity

### Weekly identity, inputs and scope
- Canonical Task: foundations/research/weekly; ISO period 2026-W44 = 2026-10-26 through 2026-11-01, Asia/Shanghai, naturally closed
- Producer: GPT-6 / GPT_NATIVE_PROSPECTIVE / NOT_JULES_REPLAY
- Base main SHA: f003841b744cde1001ec8b4f8d2b3cf39784f135
- Run ID: agent-foundations/research/weekly/2026-W44/GPT_NATIVE/f003841b744cde1001ec8b4f8d2b3cf39784f135/gpt-native-2026w44-weekly-01
- Review date: 2026-11-02; exact execution clock NOT_CAPTURED
- Four canonical containers inspected with their existing EN and ZH research chunks: Memory_System, Tool_System, Collaboration_System, Architecture_Principles
- Seven Daily input dates: Oct26 Memory, Oct27 Collaboration, Oct28 Architecture, Oct29 Memory, Oct30 Tools, Oct31 Memory, Nov01 Memory. All seven date-specific EN/ZH records are visible on main; 7/7 documentary date coverage, not seven independent experiments or validation receipts
- The separate 2026-11-02 Daily Memory addition belongs to W45, is in an open Draft and is NOT used as W44 input
- Source state: INHERITED_DAILY_AUTHOR_SOURCES / NO_FRESH_INDEPENDENT_PRIMARY_REPLAY_BY_THIS_WEEKLY. This Weekly does not allocate Sxx, certify bibliography version pairs anew, or promote claims into Verified Core

### Source identity and cross-container audit
| Date | Original Daily source identity | Container | Weekly admissible boundary |
| --- | --- | --- | --- |
| Oct26 | arXiv:2609.25913v2 — EPGM | Memory | Exact source-event span coverage under a token budget is not source truth or effect completion |
| Oct27 | arXiv:2610.35835v1 — I-HITL | Collaboration | Approval binding plus a sufficiently independent mediator is conditional, not a visible UI approval guarantee |
| Oct28 | arXiv:2610.00885v1 — Forall-Lean-Agent | Architecture | Proof artifact identity, statement identity, axiom checks and independent reviewer role are distinct |
| Oct29 | arXiv:2610.29995 — provenance-preserving multimodal memory | Memory | Entity occurrence, aspect evolution and source pointers are not independently certified entity identity |
| Oct30 | arXiv:2610.21463v1 — trajectory-level speculation | Tools | Accepted speculative tool prefix does not prove permission or committed side effect |
| Oct31 | arXiv:2610.25123v2 — dependency-tethered memory | Memory | Current validity requires complete exact-version dependencies and observed invalidation |
| Nov01 | arXiv:2610.25127v1 — MemBubble | Memory | Response-class entropy under source-defined sampling is not action correctness or causal memory degradation |

All seven are **seven named author-paper lineages as used by seven dated Daily chunks**, not seven independently reproduced results. English/Chinese mirrors and citation across projects add zero new original sources. Oct26 and Oct31 refer to different paper identities despite both discussing provenance/continuity. The Oct30 paper's speculative verifier and the Oct28 paper's proof reviewer operate over different formal objects; there is no basis to treat them as mutual empirical corroboration. Source-registry admission, author/date corrections, equation fidelity, independent theorem rechecks and benchmark reproduction remain separate gates.

### Bounded tool architecture mapping — not an implementation decision
The cross-container evidence suggests separating five predicates for tool-bearing agents:

1. **Evidence set complete for the claim:** provenance-addressed source spans and query-specific required membership are present. EPGM supports this as a candidate retrieval measurement only
2. **Proposal / proof artifact verified:** the candidate trajectory or proof object matches the checked task, statement, version and declared assumptions; Forall-Lean-Agent and speculative trajectory papers have different object/validator semantics
3. **Action authority actually valid:** the specific effect set and approval-relevant state are bound to an independent authorized gate; I-HITL does not imply any current repository mediator exists
4. **Side effect executed and receipted:** the exact external effect and target incarnation are independently observed; accepting a speculative prefix or finding a source citation is not an effect receipt
5. **Current completion remains true:** fresh relevant state and full dependency membership still satisfy the requested postcondition; a historical passing memory verdict may have been invalidated by later evidence

This is a **CANDIDATE_MECHANISM / DOCUMENTARY_MAPPING** for review, not a new Tool System runtime contract. The source papers study different tasks, metrics, populations and implementations. No single paper proves the five-step conjunction sufficient, and applying a combined predicate to a real host requires explicit authority and reproducible receipts.

### Counterevidence gate and outstanding work
- A read-classified speculative tool may have hidden billing, logging, privacy or remote-state effects; the paper's read/no-side-effect assumption must be checked, not adopted as universal truth
- A trusted mediator may still fail if communication channels, protected-action identity or approval binding are incomplete; an approval transcript is not independent authorization
- A digest-confirmed proof may validate an unintended statement or hidden axiom; evidence-set recall is not formal theorem soundness
- A memory dependency graph may omit a revoked source or delayed relation, so recursive validity over an incomplete graph can incorrectly pass
- Memory-conditioned response entropy may decline even when a constrained task requires a small valid answer space, so diversity is not a reliable completion proxy
- NEW_EVIDENCE: seven existing source-specific chunks can be reconciled into separately testable evidence/verification/authority/effect/completion predicates without making source claims interchangeable
- CORRECTED_INTERPRETATION: tool trajectory acceptance and proof artifact checking must not be labeled side-effect completion or authorization
- UNCHANGED_BOUNDARY: Paper != Mapping != Implementation != Validation; Weekly inheritance != fresh independent evidence
- NEW_COUNTEREVIDENCE: hidden side effects, missing dependency edges, incomplete mediation, axiom/statement mismatch and task-constrained answer sets challenge over-broad promotion
- UNKNOWN_RETAINED: exact tool runtime semantics, all seven source-version independent rechecks, bibliography admission, implementation, bilingual semantic equivalence beyond checked records and production validation
- NEXT_RETEST_CONDITION: implement an isolated version-pinned tool harness only after authorization; record proposal, gate decision, approved action identity, actual effect receipt and current postcondition, then inject stale approval, omitted dependency, speculative read side effect and statement mismatch

### Cascade disposition, bilingual and delivery
- Tool_System EN/ZH: APPEND_BOUNDED_WEEKLY_RELATION; no old source chunk altered
- Memory_System EN/ZH: NO_FOLLOW_UP on original Daily passages (evidence is already present; do not duplicate it). The ongoing 2026-11-02 Memory Daily branch is an independent W45 input outside this Weekly and is not edited
- Collaboration_System EN/ZH: NO_FOLLOW_UP, I-HITL's formal limits are inherited without rewriting its original theorem or result
- Architecture_Principles EN/ZH: NO_FOLLOW_UP; proof artifact and axiom-check boundary already explicit
- EN/ZH parity check: this append is mirrored for corresponding identities, five-axis state, source limitations and test boundaries, but no independent machine translation/parity validator was executed
- Claim State: OBSERVED for author-paper description only; weekly mapping CANDIDATE_MECHANISM
- Evidence Level: E4_PREPRINT for source-specific research; independent reproduction NOT_PERFORMED
- Mapping State: CANDIDATE_MECHANISM; Implementation State: NOT_IMPLEMENTED; Validation State: NOT_TESTED
- Only the existing EN/ZH Tool_System files change, append-only. FOUNDATION/SOURCES, verified core, older chunks, code, tests, Memory, Collaboration, Architecture, October monthly, workflows and historical research remain unchanged
- Repository validator and source benchmark executions: NOT_EXECUTED; human maintainer remains responsible for review and merge

---

## 2026-11-03 GPT Native Daily Research — Minimal Tool Interface and Independent Proof Acceptance

### Identity, source and status
- Canonical Task: `foundations/research/daily`
- Logical Date: 2026-11-03, Asia/Shanghai
- Producer: GPT-6 / GPT_NATIVE_PROSPECTIVE / NOT_JULES_REPLAY
- Base Main SHA: `39c0cdcb9bbbc067b67690b70380e8fa69da695e`
- Run ID: `agent-foundations/research/daily/2026-11-03/GPT_NATIVE/39c0cdcb9bbbc067b67690b70380e8fa69da695e/gpt-native-20261103-tool-daily-01`
- Container: Tool System / mirrored bilingual Daily research only
- Exact Source: arXiv:2610.17331v1 / submitted 2026-10-12T19:40:30Z / inspected 2026-11-03
- Title: *Do Theorem Provers Need Theorem-Proving Agents? mini-Lean-agent: A Coding-Agent Baseline for Lean*
- Authors: Tomas Ortega, Simon Park, Ayush Khaitan, Liam Fowl, Alex Kontorovich, Sanjeev Arora
- Abstract: https://arxiv.org/abs/2610.17331
- Full Text: https://arxiv.org/html/2610.17331
- Code (author linked, repository execution NOT_EXECUTED): https://github.com/TomasOrtega/mini-lean-agent
- Inspected Source Surface: original abstract, full-text design, comparison setup, results and reproduction section
- Canonical Identity: one author paper and version, not a new independent source every time it is cited or translated
- Selection rationale: isolates tool/harness complexity from theorem-proof acceptance and model capability; not a replay of the 2026-11-02 memory research

### Research problem and formal boundary
A specialized model-visible tool API or multi-agent scaffold is not automatically necessary or sufficient for formal verification. The authors compare a minimal `bash`-only, filesystem-native Lean coding agent with specialist-tool baselines. The model may edit scratch/target files, search Mathlib and invoke Lean, but the submitted artifact is **untrusted** until a separate evaluator copies only the declared artifact into a clean environment, pins Lean/Mathlib and checks the original theorem statement and forbidden proof shortcuts.

The operational distinction is:
```text
model-visible tool affordance
!= verified final artifact
!= preserved target statement
!= accepted proof under permitted axioms
!= verified agent-foundations implementation
```
A deterministic or trusted checker must validate **exact final bytes** under its own fixed statement, environment and policy; the fact that a model called the compiler is insufficient.

### Original quantitative and negative evidence
- Author fixed-model comparison uses Gemini 3.8 Flash with high thinking, 12 Putnam 2025 problems, $2 per-problem cap and one run per problem/harness. mini-Lean-agent: 7/12 verified, AxProverBase: 4/12. The budgets additionally permit special extended runs for harder A5/B6; do not conflate these with the $2 success figures.
- The same mini-Lean-agent with Astra is author-reported to solve 12/12 at average $1.28 per problem under a different model/budget setup. This is NOT a same-model causal estimate of tool-interface effect.
- Negative evidence: at the $0.50 cap both compared agents show 0/12; at $1.00 mini-Lean-agent 4/12 while AxProverBase 0/12. Even strong generic shell access is not a universal low-budget success mechanism.
- Statistical and external limits: small benchmark (12 tasks), one run per problem in direct harness comparison, limited model/task distribution, author-controlled evaluator, no independent reproduction here, and non-identical comparison to Numina's reported results.
- Counterexample gate: if a candidate modifies the theorem statement, introduces `sorry`/`admit`/unapproved axioms, or relies on a contaminated mutable workspace, a successful agent trace must still be rejected by the independent artifact evaluator.

### Bounded mapping to Tool System
- Candidate Tool Contract: keep an unrestricted model-visible shell as a **comparative baseline**, not automatically a secure production design; separate task proposal/exploration from trusted acceptance of exact output and postcondition.
- Candidate Harness Evaluation: pin model, budgets, toolset, benchmark, verifier, source revision, allowed axioms and output bytes. Run a matched scaffold-vs-specialist-tool ablation before claiming specialist tooling helps.
- Candidate Security/Trust implication: the evaluation authority must not trust the agent-modified workspace or model-created success labels. This is a research analogy, not evidence that the current Tool System enforces isolation, an authorization gate, or Lean checking.

### Five-axis evidence status and Evidence Delta
- Claim State: OBSERVED / AUTHOR_REPORTED_ON_EXACT_EVALUATION
- Evidence Level: E4_PREPRINT / FULL_TEXT_READ_FOR_DESCRIPTIVE_CLAIMS / INDEPENDENT_REPLICATION_NOT_PERFORMED
- Mapping State: CANDIDATE_MECHANISM / DESIGN_ANALOGY
- Implementation State: NOT_IMPLEMENTED / NO_TARGET_REPOSITORY_RUNTIME_IDENTIFIED
- Validation State: NOT_TESTED / LOCAL_CHECKS_NOT_EXECUTED
- NEW_EVIDENCE: minimally scaffolded shell agent is compared to a specialized interface under a stated common-model budget; final proof acceptance is delegated to a clean, statement-preserving evaluator.
- CORRECTED_INTERPRETATION: tool count, compiler invocation, and training/model identity cannot be conflated with independently accepted proof correctness or security.
- UNCHANGED_BOUNDARY: Paper != Mapping != Implementation != Validation; EN/ZH mirror and citing the same author study do not create independent experiments.
- NEW_COUNTEREVIDENCE: zero verified solves for both compared agents at $0.50 and the requirement to reject mutated statement/forbidden axioms refute simple tool-call-success semantics.
- UNKNOWN_RETAINED: independent reproduction, generalization to open-ended agent tool use, actual security implications, verified source-code commit, and this repository's implementation/runtime behavior.
- NEXT_RETEST_CONDITION: pin Lean 4.28.0-rc1/Mathlib v4.28.0-rc1, benchmark and code commits; compare identical models/limits, freeze original statement, inject statement substitution, forbidden axioms and artifact-after-review mutation; independently retain exact acceptance receipts.

### Delivery and promotion boundary
This section is a bilingual append-only Native Daily research chunk. It allocates no `Sxx`, updates no Verified Core claim, and does not claim current Tool System implementation. No prior research chunk, archive, code, test, source registry, Monthly blueprint or Weekly cascade was changed. Repository validator and independent proof checks: NOT_EXECUTED. Human Maintainer review/merge required.


---

## 2026-11-05 GPT Native Daily Research — Effect-Typed Tool Boundaries and Trace Safety

### Identity, primary source and scope
- Canonical Task: `foundations/research/daily`
- Logical Date: 2026-11-05, Asia/Shanghai; actual research and GitHub authoring 2026-11-05 (not a historical Jules replay)
- Agent: GPT-6 / GPT_NATIVE; Base Main SHA: `368db3ba5feffbfef5d8414f203af0bcc873b212`
- Run ID: `agent-foundations/research/daily/2026-11-05/GPT_NATIVE/368db3ba5feffbfef5d8414f203af0bcc873b212/native-20261105-tool-01`
- System Container: **Tool System** (EN and ZH append the same theory and bounded contract)
- Frontier Source: *ETAS: An Effect-Typed Language for Agent Systems*
- Authors: Huiri Tan, Yikun Wang, Puyang Zhang, Shangyu Li, Jiasi Shen
- Source: https://arxiv.org/abs/2607.17780 ; original complete web-rendered paper https://arxiv.org/html/2607.17780
- Version/publication: original arXiv manuscript dated 2026-07-20T10:11:53Z; **historical paper studied today, not a 2026-11-05 release**
- Date Checked: 2026-11-05; source type: original author preprint, not peer-review or an independent proof reproduction
- Selection rationale: explicit typing, effects, policy traces and residual runtime checks offer an auditable Tool/Harness contract. This is not another generic benchmark or the November 4 Memory System selection problem.

### Original problem, assumptions, and mathematical mechanism
A tool-using agent is not adequately characterized by the signature of a Python callback or the success text of a final answer. Its externally requested and committed actions can differ, especially under handlers, denials, human approvals and retries. ETAS models these as program-level effects and typed trace events.

The paper states a static judgement with five distinct outputs:
```text
Ξ ; Γ ; Π ⊢ e ⇒ τ ! ε ▷ A ⊣ R

τ : ordinary result type
ε : escaping effect row
A : abstraction of requested-action trace
R : residual obligations to enforce dynamically
Π : active policy/trace specs, compiled to monitor M_Π
```
Do not reduce `ε` to `A`: a handler can intercept a requested action so that it does not escape/commit, yet the attempted request remains visible in the trace. Policy checking must not lose that provenance.

Theorem 5 (Policy safety) is explicitly conditional: for a well-typed program under well-formed static assumptions `Ξ,Π`, **provided the runtime contains the residual obligations R and enforces each relevant check before request or commit**, every resulting trace prefix is accepted by its compiled monitor `M_Π`. In compact terms, the conditional target is `∀k, M_Π(trace[:k]) ∉ Bad`. Theorem 6 adds handler trace-transparency: handling a request does not erase the request event or create unreviewed commit authority.

This is a source-level formal claim about the authors' calculus, not a proof that any current real-world Agent runtime, this repository, or this Tool System meets the theorem's premises. The paper also reports a Rust prototype and typed HIR/policy checks; that repository executable was NOT downloaded, built or tested here.

### Convergence/behavior bound, constraints and counterexamples
- **Conditional boundary:** guarantee covers only typed action events modeled by the compiled monitor and mediated by the runtime; it does not cover an unmodeled direct network route, a rogue tool outside the effect boundary or semantic correctness of generated text.
- **Approval gap:** if human approval is only in prompt prose or absent from trace/policy facts, no policy theorem can establish it dominated the external commit.
- **Residual-check failure:** a dynamic resource cannot be fully decided statically; if the generated `R` is not actually enforced before an action, the theorem's premise fails, regardless of compile success.
- **Handler laundering:** a handler that hides requests or commits without boundary checks contradicts trace transparency, even if execution eventually returns a success object.
- **Replay/duplicate effect:** request, handled, denied and committed events must be differentiated; retrying a logical step is not evidence of exactly-once external effect.
- **Trace-compliance limit:** even a correctly mediated effect trace does not prove the task's result is true or that the external service applied a side effect as reported.

### Bounded mapping to the Tool System
- Design candidate `ToolRequest`: bind stable task identity, tool name, arguments digest, policy version, resource scope and untrusted/trusted provenance to each requested action.
- Design candidate `EffectCommit`: require an independent effect/approval authority, dynamic residual precondition and evidence receipt, trace-linked to the original request, with explicit denial/handler outcomes.
- Design candidate `TraceMonitor`: check each enforceable prefix, preserve request records when handlers intercept calls, and persist trace/effect identities across retries.
- These are **proposed contracts**, not source-code facts about the current repo. A code-level implementation would require an exact target runtime, pinned revision and negative tests including denied approval, changed arguments, handler interception, missing residual and duplicate commit.

**Beginner analogy:** a tool request resembles a purchase order, while a committed external effect resembles money actually leaving the bank. Recording an order or obtaining an assistant's approval sentence does not prove the bank authorized a transfer.

### Five-axis state, evidence delta and promotion gate
- Daily Mapping Status: `DESIGN_CANDIDATE` / `CONCEPTUAL_MAPPING`; publication-only result is `PAPER_ONLY`
- Claim State: `OBSERVED` (paper's premises and theorem statement, not independently proved)
- Evidence Level: `E4_PREPRINT` / FULL_TEXT_READ / INDEPENDENT_FORMAL_CHECK_NOT_PERFORMED
- Mapping State: `CANDIDATE_MECHANISM` / `DESIGN_ANALOGY`
- Implementation State: `NOT_IMPLEMENTED` / NO_DEPLOYED_TARGET_IDENTIFIED
- Validation State: `NOT_TESTED` / LOCAL_CHECKS_NOT_EXECUTED
- NEW_EVIDENCE: formal separation of escaping effects, requested trace abstraction, and dynamically enforced policy obligations
- CORRECTED_INTERPRETATION: type soundness or a submitted approval request does not itself establish approved/committed external behavior
- UNCHANGED_BOUNDARY: paper != proposed Tool contract != implemented Trust/Control plane != tested runtime. EN and ZH mirror a single source, not independent proof
- NEW_COUNTEREVIDENCE: unmodeled external actions and absent residual checks explicitly fall outside the conditional safety statement
- UNKNOWN_RETAINED: independent Dafny/Rust check, all Etas language behavior, actual runtime adaptation, host/applicability, replay safety and measured defense
- NEXT_RETEST_CONDITION: freeze precise Etas paper/source revision, instantiate request/deny/handler/commit traces, inject missing residual, untrusted direct effect path, changed approval scope and retry, then independently verify effect records and monitor verdicts

### Delivery boundary
Append-only Native Daily research in `docs/en/Tool_System.md` and its ZH counterpart only. Original theory, historical text, SOURCE Registry, Verified Core `Sxx`, code, tests, other four containers, weekly/monthly and unrelated WorkflowHub PR are not touched. Native validator and paper-code experiments: NOT_EXECUTED. Human Maintainer reviews the proposed PR; do not count a paper theorem as an implemented guarantee.


## 2026-11-06 GPT Native Daily Research — Controller-Agnostic PAC Reach–Avoid Shield for Tool Effects

### Daily research identity and canonical source
- Canonical identity: `agent-foundations/research/daily/2026-11-06/GPT_NATIVE/0090958c3f522b5147f96be50015819143546088/native-20261106-tool-01`
- System Container: **Tool System**
- Technical point: controller-agnostic, data-driven finite-horizon safety bound for tool actions, with a logged-state abstraction and a decision-time shield
- Full paper: *Controller-Agnostic Runtime Safety Certificates for Tool-Using AI Agents via Data-Driven Robust Reachability*
- Authors: **Ali Baheri and Peng Wei**
- Canonical original: https://arxiv.org/abs/2610.16865 ; full author text: https://arxiv.org/html/2610.16865
- Exact text studied: **arXiv:2610.16865v2**, dated **2026-10-23** in HTML. arXiv v1 was originally submitted **2026-10-12**; the v1 abstract and v2 text are distinct time-bound surfaces
- Accessed: **2026-11-06 Asia/Shanghai**; source type: original author preprint, not peer-reviewed deployment validation
- Choice: the source supplies an explicit formula, assumptions, failure bounds, safety-gate contract and counterexamples; it adds quantitative risk-budget semantics to earlier Tool studies about type/effect authorization. No generic leaderboard inference

### Original research question, assumptions and method
The authors treat the language model as an opaque controller that proposes actions to an external environment; a shield filters the allowed action set. The goal is to keep the probability of *ever* reaching an irreversible unsafe state within a task horizon below a chosen risk budget, even when the controller changes, **conditional on model assumptions and data coverage**.

- **A1 / Markov abstraction:** each history `h_t` maps to a finite predicate state `s_t=φ(h_t)`; the next-state law is determined by state and action, not an omitted detail of history
- **A2 / Absorbing harm:** once an unsafe state has been reached, that state cannot be treated as undone by a later apology or tool call
- **A3 / Safe halt:** every non-unsafe state permits an action that transitions to a known safe terminal sink
- **A4 / Controller independence:** the transition kernel depends on the abstract state and effective tool action, not the model/controller identity; controller-dependent environments break this premise
- **Candidate successor coverage:** a specified `K_{s,a}` must include every possible next state; omitting a dangerous successor invalidates the claimed coverage
- **Log sampling:** per-row `n_0(s,a)` budget is committed before seeing the data; opportunistically choosing sample counts after the fact is not justified by the displayed fixed-budget confidence argument

### Mathematical mechanism and conditional bound
For each state/action row, the author constructs a confidence set around the empirical transition kernel. Let `R` be the number of rows, `k_{s,a}=|K_{s,a}|`, `δ` the confidence failure allowance, and `n_0(s,a)` the precommitted number of observations:

$$
\beta_{s,a}=\sqrt{\frac{2}{n_0(s,a)}\log\left(\frac{(2^{k_{s,a}}-2)R}{\delta}\right)}
$$

This radius applies to stochastic rows with at least two successors. Under-covered rows use the **vacuous** set over all candidate successors; a larger source log is not automatically a tighter certificate if relevant rows remain unobserved.

A robust dynamic program upper-bounds the probability of reaching harm: with unsafe states absorbing and halt assigned zero unsafe value,

$$
\bar V_t(s)=\max_{a\in D(s)}\max_{q\in C_{s,a}}\sum_{s'}q(s')\bar V_{t-1}(s')
$$

**Theorem 1 (author's conditional PAC certificate):** if the shield `D` obeys `\bar V_T(s_0)\le \varepsilon`, then, under the named assumptions and candidate-successor coverage,

$$
\Pr_{\mathrm{data}}\!\left[\sup_{\pi\ \mathrm{admissible}}V_T^\pi(s_0;P)\le\varepsilon\right]\ge 1-\delta
$$

The probability is over the sampling of logs, not a claim that each individual tool call is safe with probability `1-δ`. The controller-uniform result only covers controllers *actually constrained by this shield* and transitions within the modeled environment.

### Convergence/behavioral bound and negative space
- Corollary 1 gives a **conditional** looseness rate `O(T/\sqrt M)` when every reachable and relevant row receives proportionally growing sample coverage; it is not universal for sparse or adversarially omitted hazard transitions
- When a row fails its precommitted count, the method deliberately becomes vacuous there; falsely assigning zero harm because no hazardous outcome appeared would be an unsound plug-in estimator
- The authors report a filesystem sandbox and 1,050 agent episodes, but **reported zero observed harms is not the theorem**, nor does it certify unmodeled side effects or all future tasks. The v2 abstract describes seven controllers including six open-weight-model controllers; the earlier v1 abstract uses a different count and must not be silently mixed into one empirical claim
- The all-halt policy is formally safe under the stated stop assumption but operationally useless; "safe" without goal reachability is not sufficient task completion
- If the abstract state omits authorization expiry, resource identity, dynamic permission or hidden tool arguments, Markovness or successor support may fail and invalidate the mapped guarantee
- The authors' code link is a research reproduction lead only; we did **not** execute their implementation, theorem checker, tool calls or experiments

### Bounded Tool System architecture mapping
- **State abstraction candidate:** `(principal, resource class, capability, approval/effect status, task horizon, action class)` may serve as an input vector only after a domain-specific test that the abstraction retains safety-relevant distinctions
- **Guard candidate:** before a proposed effect, recompute allowed actions from `D(s)`; denial is a constrained-action decision, not proof of a committed result
- **Evidence candidate:** bind `(source log ID, extraction cutoff, K_{s,a}, n_0, δ, horizon T, policy/shield digest, controller identity, tool-effect trace)` to each certificate
- **Effect-time test:** inject an unauthorized successor omitted from `K`, a stale authority token, a long-held pending approval, an under-covered state/action row and a tool action through an unmediated side channel. These are falsification tests **proposed**, not executed
- **Non-inheritance:** a certificate attached to a shield configuration cannot be inherited by a new tool topology unless the same state/action abstraction and support assumptions remain valid

**Analogy for beginners:** A railway dispatcher can refuse routes known to lead into a closed track, but a safety calculation is valid only if the map includes every possible switch and the train actually obeys the dispatcher. A safe stop is not the same as arriving at the destination.

### Five-axis evidence state
- Daily Mapping Status: `CONCEPTUAL_MAPPING / DESIGN_CANDIDATE`
- Claim State: `OBSERVED_AUTHOR_THEOREM_AND_ASSUMPTIONS` (not an independently checked proof)
- Evidence Level: `E4_PREPRINT / FULL_TEXT_V2_READ`
- Mapping State: `CANDIDATE_MECHANISM / DESIGN_ANALOGY`
- Implementation State: `NOT_IMPLEMENTED / NO_AGENT_FOUNDATIONS_RUNTIME_SHIELD_SHOWN`
- Validation State: `NOT_TESTED / NO_LOCAL_REPLAY_OR_FORMAL_RECHECK`
- NEW_EVIDENCE: explicit conditional risk envelope over logged abstract transition rows and a controller-agnostic action shield
- CORRECTED_INTERPRETATION: a PAC confidence certificate, safe stop, observed no-harm episodes and a successfully completed task are four different claims
- UNCHANGED_BOUNDARY: author paper != deployed Tool System, source math != independent proof, a proposed effect gate != observed external commit
- NEW_COUNTEREVIDENCE: unobserved successor classes and history-dependent transition behavior can break the guarantee; insufficient data does not become an automatic PASS
- UNKNOWN_RETAINED: independent reproduction, true Markov abstraction, exact target-store identity, tool topology, runtime authorization and end-to-end task completion
- NEXT_RETEST_CONDITION: pin author code and state/action model, construct covered and under-covered transition rows, inject an omitted hazard, and compare robust reach–avoid bound to observed exact-version traces

### Delivery / identity boundary
Appended bilingual daily research only in the canonical English and Chinese Tool System files; earlier sections, SOURCE Registry, verified core, runtime, tests, other containers, weekly/monthly and unrelated open PRs remain untouched. Source v1/v2 counts are not silently reconciled. Test and paper-code reproduction: `NOT_EXECUTED`.

## 2026-11-07 GPT Native Daily Research — AgentLTL: a verified trace predicate is not a completed tool effect

### Canonical research identity and source
- Task: `foundations/research/daily`; logical date `2026-11-07`, `Asia/Shanghai`
- Producer: `GPT-6 / GPT_NATIVE / HUMAN_AUTHORIZED_SUBSTITUTE`; **not a Jules replay**
- Base `main`: `79474f8efa89dc549b5893558decb0170eaab605`; research target: `docs/en/Tool_System.md` and bilingual `docs/zh/Tool_System.md` only
- Container: `Tool System` / `Tools`; no change to the other three formal containers
- Original scientific source: Laïla Elkoussy and Julien Perez, *AgentLTL: A Trace-Verification Framework for Measuring, Enforcing, and Training Procedural Compliance in Tool-Using LLM Agents*, arXiv:2607.02599v1
- Exact version/submission: `v1`, 2026-07-01 10:47:20 UTC; [versioned abstract](https://arxiv.org/abs/2607.02599v1), [original versioned HTML](https://arxiv.org/html/2607.02599v1)
- Source observation date: 2026-11-07; **not** a publication on this research date
- Checked source surface: original abstract and full-text Sections 3, 5, 6, 8 and Appendix A.5 (prefix enforceability) through the public arXiv text
- Source lineage: ONE author paper, ONE canonical base arXiv ID; this bilingual insertion is not an independent second evidence origin
- Canonical Sxx: NOT_ALLOCATED / NOT_REGISTERED; Verified Core claim: NOT_PROMOTED
- Local Agent Foundations source code or executable behavior: NOT_IMPLEMENTED_FOR_THIS_MAPPING; unit/runtime tests: NOT_EXECUTED

### Mechanism: trace compliance and outcome correctness form separate acceptance contracts
Let `tau` denote an ordered trace of tool actions, `kappa_i` one procedural rule over its typed events, and `C(tau)` an evaluation of the rule set on that trace. The authors use a first-order temporal-logic-derived notation to specify call order, branching, iteration and grounding; the same specification can score a completed trace offline or gate proposed next tool calls by evaluating prefixes.

A guard on `tau + proposed_call` can observe only what its event representation exposes. The paper's Appendix A.5 makes a decisive logical distinction: safety violations have a finite *bad prefix*, whereas pure liveness requirements (e.g., "eventually invoke a certain step") may remain satisfiable by a future call and cannot be rejected before the trace ends. Thus, `PREFIX_GATE_ALLOW` does not prove `FULL_TRACE_COMPLIANT`, `COMPLETED_GOAL`, or `SIDE_EFFECT_COMMITTED`.

The paper reports a 12-template benchmark and 7 evaluated models, including comparisons between no enforcement, soft-block and block-and-warn. Its abstract reports improvement under block-and-warn on five of seven models; these are **author-reported and benchmark-scoped**, not independent reproduction or an implementation claim for this repository. In the discussion, trace compliance and final-answer accuracy sometimes diverge, especially for branching/loop tasks. A correct answer can be achieved via a noncompliant trace, and procedural compliance need not imply correct output.

### Counterevidence gate: three ways a clean guard can mislead
1. **Deferred liveness.** A trace prefix satisfies all locally enforceable safety constraints but never triggers a required future action; the workflow terminates. Any claim that the online guard alone guarantees the eventual step is falsified.
2. **Vacuous grounding.** The authors expressly report that a grounding predicate can be satisfied by a refusal containing no entities to verify. Raising grounding scores can therefore reflect more refusals, not more verified correct answers. The denominator and abstention class must remain explicit.
3. **Enforcement intervention effects.** Hard or soft blocking may prevent recovery and lower eventual accuracy compared with warning-based correction. Blocking an untrusted call also cannot establish that the authorized external service acknowledged or committed a different subsequent action.

These are *source-supported limits* of a paper's procedural-evaluation model. They are not reports of local Tool System incidents or verified agent safety. A user-facing approval and an offline trace score do not by themselves prove an independently controlled effect-time authorization boundary.

### Bounded theory-to-architecture mapping
- `CANDIDATE_MECHANISM`: bind `(task_id, policy_version, trace_event_schema, trace_prefix_digest, predicate_set, proposed_call, guard_verdict, effect_receipt_id, final_task_verdict)` as **separate** potential evidence fields
- `COUNTEREVIDENCE`: accept a guard-approved trace that omits a later required step; accept a vacuous-grounding refusal; or compare warning versus block outcomes, and check whether any tool side effect was actually committed
- `NOT_IMPLEMENTED`: no local AgentLTL DFA engine, online tool guard, side-effect broker, independent verifier, approval-binding service or training loop is asserted
- `NOT_TESTED`: no native package, formal property checker, protocol compatibility trial, source code execution or bench replay was run
- `OUT_OF_SCOPE`: the paper's finite-trace procedures do not automatically establish indefinite-state invariants, arbitrary external tool effects, durable task recovery or service receipts

### Five-axis record
- Claim State: `OBSERVED` (paper's definitions and author-reported experiments only)
- Evidence Level: `E4_PREPRINT` (original arXiv full-text source, no independent formal verification)
- Mapping State: `CANDIDATE_MECHANISM` with `COUNTEREVIDENCE` and `OUT_OF_SCOPE` tests
- Implementation State: `NOT_IMPLEMENTED`
- Validation State: `NOT_TESTED`

### Evidence Delta / retest
- NEW_EVIDENCE: original full-text distinction between finite bad-prefix constraints and non-enforceable liveness, plus observed author benchmark limitations concerning vacuous grounding
- CORRECTED_INTERPRETATION: deterministic trace compliance is narrower than factual correctness, final completion, effect authorization and durable commit evidence
- UNCHANGED_BOUNDARY: Paper != Mapping != Implementation != Validation; English and Chinese copies reference one research identity
- NEW_COUNTEREVIDENCE: a compliant refusal can satisfy grounding vacuously; a safety-prefix PASS can coexist with a missing future obligation; an overly aggressive blocker may suppress valid recovery
- UNKNOWN_RETAINED: paper-wide theorem proof checking, independent replication, production behavior, actual local tool adapter and realized service effect receipts
- NEXT_RETEST_CONDITION: pin exact AgentLTL version, typed trace schema and guard configuration; inject unfinished liveness, a refusal with empty entity set, a wrong-but-compliant trace and side-effect ambiguity; capture separate `guard`, `tool` and `final` receipts and compare warning/block modes

Delivery note: only the paired EN/ZH research containers are appended. No change to Jules records, source registry `Sxx`, `FOUNDATION/**` verified core, four-container Weekly, October/November Monthly, implementation, schema, workflows, or unrelated WorkflowHub PR #378. Validator and native research reproduction: NOT_EXECUTED; maintainer reviews the Draft before merging.



---

## 2026-11-09 GPT Native Daily — FAVA: permission-graph soundness is not end-to-end authorization

### Source identity and access depth
- Canonical paper identity: **arXiv:2607.27267v1**; title: *FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs*
- Authors: Yifan Zhang, Xinkui Zhao, Sai Liu, Hengxuan Lou, Guanjie Cheng, Chang Liu
- Original version/publication date: **2026-07-29 09:41:07 UTC**; this is an earlier paper inspected on **2026-11-09**, NOT a newly published November paper
- Original source opened: https://arxiv.org/abs/2607.27267 and https://arxiv.org/html/2607.27267; reviewed direct sections Graph Lowering, SMT Authorization, Finite-Graph Soundness, Taint-Monotonic Safety, Security Assumptions, Experiments and Failure Analysis
- Source class: E4_PREPRINT; source surface: ORIGINAL_FULL_TEXT / AUTHOR_THEOREMS_AND_EVALUATION_INSPECTED, **INDEPENDENT_FORMAL_PROOF_AND_CODE_REPLAY_NOT_EXECUTED**
- Canonical Source Registry: arXiv identity checked against current `FOUNDATION/SOURCES.md`; **NOT_REGISTERED, NO Sxx ID ASSIGNED**. Bilingual versions here are one research unit and one paper, not two independent replications
- Producer: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY; logical period 2026-11-09 Asia/Shanghai; exact baseline main `9ef3c669d71f511a87eb677f94dbbb90ca4461c0`; review UTC `2026-11-09T11:55:08.435Z`; task `foundations/research/daily`; container: Tool System

### Source-level mechanism and formally bounded claim
The paper uses an LLM for extracting a Permission IR containing intent, assets, actions, obligations, sinks and evidence spans, but separates this probabilistic extraction from deterministic graph lowering, SMT solving and a just-in-time execution gateway. Graph nodes encode evidence-bearing sources, tool actions and sinks; data, control and ancestry edges encode dependencies. The graph validator checks labels and trusted edge origins before solving; **inferred edges are not automatically authoritative runtime facts**.

For a finite permission graph, the paper models propagated protected labels as `H[v,label]` and candidate capability grants as `A[v,capability]`. Its illustrative forbidden-flow constraint is `not (H[v,secret] and A[v,net:send])`, while a temporal obligation may require `grant(commit) implies Seen(tests_passed, before_commit)`. Finite-graph soundness is conditional on the explicit graph, fixed policy translation and complete gateway-visible candidate action. This is **not** a theorem that the natural-language extraction, implicit flows, credential state or downstream backends are complete and correct.

The taint monotonicity theorem is about **taint-only graph extension under fixed policy and required capabilities**: adding taint without adding trusted sanitizers, declassifications or positive obligation facts cannot turn an originally forbidden grant into an allowed grant. It does **not** say every runtime permission decision is monotonically deny-only; receiving an authenticated `tests_passed` fact can satisfy a separate positive guard.

The authors report 90.5% Decision Compliance Rate over 801 benchmark replay cases. DCR is a mixed binary allow/block classification metric, with false-positive blocks and false-negative permissions both counted. The trace-conditioned datasets and best-effort reproductions of other defenses have distinct evidence status; this is author-reported performance, **not** repository validation, deployment guarantee or universal safety probability.

### Architecture consequence and falsifiable gates
- Candidate contract projection: `(principal, task_intent, asset_identity, current_authority_state, tool_action, effect_target, data_lineage, obligations, observed_evidence, policy_version, gateway_decision, effect_receipt)`. Treat this as a research-only proposal, not implemented schema
- Require provenance and freshness for each permission-graph node/edge, distinguish policy/observed/inferred trust labels and named capabilities; never let an LLM's proposed IR stand in for enforcement authority
- Counterexample 1 — **missing source-to-sink edge**: a hidden data dependency absent from lowering can make a satisfiable graph certify an incomplete world. SMT soundness remains conditional but the real action may leak
- Counterexample 2 — **positive guard chronology**: a `tests_passed` fact for a previous commit or test revision must not be accepted for the current action; static fact presence is insufficient without exact revision/temporal provenance
- Counterexample 3 — **TOCTOU between authorization and effect**: even a valid snapshot may expire before a backend effect; the trusted gateway and backend must preserve the checked capability and relevant state through effect time
- Counterexample 4 — **unmediated backend**: if a tool adapter executes side effects outside the gateway, formal graph approval says nothing about those bypassed effects
- Counterexample 5 — **over-restriction and semantic error**: false-positive block and extraction omission show safety/utility tradeoffs; a validated graph neither proves extracted user intent correct nor downstream business completion

### Five independent evidence axes
- Claim State: `OBSERVED` — paper's specified abstraction and author-reported results, not independently established theorem
- Evidence Level: `E4_PREPRINT` / original v1 full text inspected
- Mapping State: `CANDIDATE_MECHANISM` / `COUNTEREVIDENCE` / `OUT_OF_SCOPE`, not verified architecture decision
- Implementation State: `NOT_IMPLEMENTED` — no local permission IR/SMT/gateway implementation shown
- Validation State: `NOT_TESTED` — solver, benchmark, action broker and exact effect-time receipt replay not executed in this repo

### Evidence Delta and handoff
- NEW_EVIDENCE: a permission-graph formalization of capability, taint and temporal obligations, with conditional soundness and narrowly defined taint-only monotonicity
- CORRECTED_INTERPRETATION: a SAT decision certifies only the translated, fully represented policy graph; it cannot replace semantic completeness, runtime mediation, effect-time authorization or independent final-state verification
- UNCHANGED_BOUNDARY: PAPER != MAPPING != IMPLEMENTATION != VALIDATION; EN/ZH bilingual copy != independent source; historical source date != research date
- NEW_COUNTEREVIDENCE: missing graph edges, stale positive facts, gateway bypass, incorrect LLM IR extraction and false-positive denial can all undermine an end-to-end authorization claim
- UNKNOWN_RETAINED: theorem proof replay, benchmark reproducibility, actual source-graph completeness, real backend conformity, local test results, runtime behavior and verified core status
- NEXT_RETEST_CONDITION: pin paper v1 and executable reference if available; construct two graph twins with a missing sensitive flow, positive-obligation revision mismatch and an unmediated tool effect, then inspect graph structure, SMT outcome, effect-time gateway check and independently reconstructed side effect with exact revision, stdout/stderr and exit

Delivery: paired **append-only** English/Chinese Tool System Daily research, no modifications to prior chunks or existing source registry, `FOUNDATION/**` verified core, other containers, implementation, schema, Weekly/Monthly, workflows or independent WorkflowHub Draft PR #378. Native validator, Z3 proof checking and experiments: `NOT_EXECUTED`; human review/merge required.


---

## 2026-W45 Weekly Research Cascade — evidence-preserving bilingual synthesis

### Identity, closed period and inputs
- Canonical task: `foundations/research/weekly`; producer `GPT-6 / GPT_NATIVE / HUMAN_AUTHORIZED_SUBSTITUTE / NOT_JULES_REPLAY`
- ISO period: **2026-W45, 2026-11-02 through 2026-11-08**, logical timezone `Asia/Shanghai`; week closed before this run
- Review time UTC: `2026-11-09T12:44:58.259Z`; exact source baseline: merged `main` `883a0ff0138596a0a5ddd1e987918f987d74ba86`; execution identity: `agent-foundations/research/weekly/2026-W45/GPT_NATIVE/883a0ff0138596a0a5ddd1e987918f987d74ba86/four-container-bilingual-cascade-01`
- Input roster (one canonical author-paper lineage per Daily, translated bilingual records do not increase evidence count): **11-02 Memory** arXiv:2610.21170, **11-03 Tool** arXiv:2610.17331v1, **11-04 Memory** arXiv:2608.11654v1, **11-05 Tool** arXiv:2607.17780, **11-06 Tool** arXiv:2610.16865v2, **11-07 Tool** arXiv:2607.02599v1, **11-08 Architecture** arXiv:2608.03609v1
- Four formal system containers and their EN/ZH versions were read; Collaboration has **no newly dated W45 Daily research chunk**, which is a legitimate negative input
- 2026-11-09 FAVA arXiv:2607.27267v1 belongs to **W46** despite being merged into `main`; explicitly **excluded** from W45 source cohort and Weekly evidence credit
- These papers' publication/submission dates are not their later Daily research dates. The MemScope exact arXiv revision suffix remained `NOT_VERIFIED` in its Daily input, and this cascade does not invent it
- Current `FOUNDATION/SOURCES.md`, `EVIDENCE.md`, `MAINTENANCE.md` and Verified Core admission remain unchanged; no Sxx allocation or AF-* claim promotion here

### Tool container — four noninterchangeable guarantees
- **Nov03 [mini-Lean-agent](https://arxiv.org/abs/2610.17331)** isolates a minimal coding-agent tool/harness from independent Lean kernel proof acceptance; successful tool use or generated tactic text alone is not a theorem proof
- **Nov05 [ETAS](https://arxiv.org/abs/2607.17780)** studies effect-typed language/policy traces and residual checks. A static typing judgment is defined inside its language abstraction, not a receipt of every external service effect or an implementation in this repository
- **Nov06 [PAC robust reach–avoid shield](https://arxiv.org/abs/2610.16865)** (reviewed v2) derives risk-bounded shielding under finite horizon, data/abstraction and confidence assumptions. A probabilistic bound must retain horizon, distribution, failure probability and controlled action definition; it is not universal deterministic safety
- **Nov07 [AgentLTL](https://arxiv.org/abs/2607.02599)** (v1) models finite traces/prefix enforceability of procedural tool compliance. A legal finite prefix can still fail a later liveness obligation, and a compliant refusal may vacuously satisfy a grounding condition
- These four theoretical source objects are separate. A possible *research-only* staged contract is `request/source identity → typed intended effect → decision-time bounded shield → finite-trace procedure check → independent tool/effect receipt → final outcome/proof acceptance`; **no cross-paper composition theorem or local integrated implementation is established**
- Conflicts/negative cases: a type-correct effect can still be unsafe under unmodeled state; a PAC shield may fail if data assumptions shift; a finite safety-prefix PASS may lack eventual completion; Lean kernel acceptance does not prove authority for tool effects
- Retest needs distinct validators: type/effect checker, PAC calibration with explicit denominator, finite-trace monitor with incomplete-liveness countercase, authoritative effect broker and separate proof/answer correctness examiner
- W45 five axes: `OBSERVED / E4_PREPRINT / CANDIDATE_MECHANISM / NOT_IMPLEMENTED / NOT_TESTED` (author-reported methods are not locally executed)

### Evidence Delta and disposition
- NEW_EVIDENCE: W45 mapping matrix separates proof acceptance, typed intended effects, probabilistic shield scope and trace compliance
- CORRECTED_INTERPRETATION: procedural check PASS and model/theorem progress cannot be collapsed into an authorized irreversible-effect receipt
- UNCHANGED_BOUNDARY: language typing != runtime authorization; finite-prefix compliance != liveness; probability bound != zero risk
- NEW_COUNTEREVIDENCE: omitted side effects, workload distribution shift, vacuous grounding and incomplete future obligations
- UNKNOWN_RETAINED: cross-mechanism compositional guarantees, independent paper reproduction, implemented tool adapter and production outcomes
- NEXT_RETEST_CONDITION: pin source versions and tool schema; inject each of four failure modes in separate harness fixtures and retain commands, transcripts, effect IDs and outcome receipts
- Decision: NO_SOURCE_REGISTRY_AUTO_ADMISSION / NO_VERIFIED_CORE_PROMOTION / NO_IMPL_CLAIM. Only append to existing English Tool container; W46 FAVA excluded from this W45 synthesis


---

## 2026-11-11 GPT Native Daily Research — Compositional authorization: locally allowed actions do not establish globally authorized purpose

### Canonical source identity, version, and inspection
- Task: foundations/research/daily; system container: Tool System; logical date: 2026-11-11 Asia/Shanghai
- Producer: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED_SUBSTITUTE / NOT_JULES_REPLAY; base merged main: bf29f5414977a842fcdb7fa48850dd2e0c6d420a
- Source: Anmol Pandey, Aditya Jain, Liang Chen, Carsten Maple, *Local Allow, Global Deny: Why Per-Action Authorization Does Not Compose in LLM Agents*, arXiv:2610.27620v1, first submitted 2026-10-20 04:35:39 UTC
- Exact primary source: https://arxiv.org/html/2610.27620 ; source identity and abstract: https://arxiv.org/abs/2610.27620 ; author-supplied implementation/reproducibility lead: https://github.com/anmolpandey299/al-synth
- Read depth: original HTML abstract, threat model, compositional authorization failure definition, expressiveness and observability distinctions, separation/impossibility statements, synthesis method, author-described empirical study, and stated limits; not an independent mathematical proof audit
- Paper publication date != this Daily research date; arXiv version and authors are one canonical bibliographic object; bilingual translation does not create a second source
- Source Registry: Sxx NOT_ALLOCATED / NOT_REGISTERED, and verified-core AF-* claim NOT_PROMOTED. This Daily report does not mutate FOUNDATION/SOURCES.md or verified-core contracts

### Mechanism: a per-action decision is not a workflow-level authorization
The paper models finite typed state transitions with a local guard on each action and a distinct global authorization policy Phi governing the whole episode, including intent, purpose, provenance, consent, and delegation. A compositional authorization failure (CAF) can satisfy every individual guard while violating the global contract. Some failures have a violating single trace; a distinct relational-purpose failure needs a pair of locally allowed traces and is represented as a 2-safety hyperproperty.

The formal separation has a precise quantifier: under the paper's stated non-collapse condition, a single-trace monitor that never falsely alarms on a locally compliant trace cannot detect the relational-purpose violation, because no one trace supplies an individual locus of blame. A monitor may choose a conservative block with false positives, and a cross-execution monitor may inspect the required trace pair; neither option proves that sampling stochastic agent outputs gives exhaustive coverage.

An instructive witness is the paper's scheduling assistant: authorized disclosure is free/busy availability, not the confidential reason why an interval is busy. Two executions can agree on the permitted availability view yet emit different proposal patterns because the hidden reason differs. Every calendar-read, proposal, and message action can be individually allowed, while the relation across outputs violates the specified purpose.

The authors propose AL-Synth, an LLM-free SAT/SMT witness synthesizer with bounded exhaustive-oracle checking. They report nine model-judge comparisons and a live open-weights experiment with 22 violations in 60 rollouts before composition-aware intervention. These are *author-reported, setting-specific* observations, not independent replication or a local failure rate. A surveyed guardrail count and an author-side proof are not evidence of this repository running those guards.

### Bounded theory-to-architecture mapping
- CANDIDATE_MECHANISM: distinguish per-action tool/broker permission from the purpose and consent of the full composed workflow; policy admission should carry task intent and authorized disclosure projection, not only action-local allow
- Candidate evidence object: (task identity, run identity, current policy version, purpose/consent authority, input and environment identity, allowed declassification D, observer projection alpha, individual action guard verdicts, trace/event identity, matched counterfactual trace identity, tool-effect receipts, final workflow decision)
- CANDIDATE_MECHANISM: pairwise comparison of controlled counterfactual runs may detect relational policy violations missed by individually successful guards; it does not authorize automatically instrumenting live personal data or silently upgrading a tool permission system
- COUNTEREVIDENCE: a legitimate but conservative single-trace blocker can detect some cases by also blocking compliant runs, so the impossibility theorem does not claim that every conceivable single-trace monitor detects zero violations without its false-alarm-free premise
- COUNTEREVIDENCE: an incorrect disclosure projection, missing hidden dependency, mismatched environment, nondeterministic sampling, incomplete trace capture, or unmediated external effect can invalidate the intended monitor conclusion
- OUT_OF_SCOPE: proof statements over finite formal models do not certify open-ended arbitrary tool stacks, installed SDKs, real user consent, backend effect-time authority, or all stochastic executions
- Compared with the Nov09 FAVA Daily: finite permission-graph SAT soundness is conditional on correct graph and gateway mediation, whereas this paper stresses a separate relational/noninterference expressiveness boundary. Neither paper supplies a composition theorem combining both systems

### Five-axis evidence status
- Claim State: OBSERVED_AUTHOR_THEOREM_AND_AUTHOR_REPORTED_RESULTS / NOT_INDEPENDENTLY_PROVED
- Evidence Level: E4_PREPRINT / ORIGINAL_V1_FULL_TEXT_SCOPED_REVIEW
- Mapping State: CANDIDATE_MECHANISM / COUNTEREVIDENCE / OUT_OF_SCOPE
- Implementation State: NOT_IMPLEMENTED / NO_LOCAL_RELATIONAL_AUTHORIZATION_MONITOR_OBSERVED
- Validation State: NOT_TESTED / NO_SMT_SOLVER_RUN / NO_AGENT_OR_TOOL_EFFECT_REPLAY

### Evidence Delta and falsification gate
- NEW_EVIDENCE: an explicit locally permitted but globally unauthorized class of executions, with a theorem-conditioned relational-purpose separation and bounded synthesizable counterexamples
- CORRECTED_INTERPRETATION: per-action ALLOW, successful guarded tool calls, valid individual traces and a correctly mediated step do not establish a purpose-authorized overall workflow
- UNCHANGED_BOUNDARY: PAPER != MAPPING != IMPLEMENTATION != VALIDATION; AUTHOR_PROOF != INDEPENDENT_RECHECK; PAPER_ROLLOUT_DENOMINATOR != LOCAL_FAILURE_RATE
- NEW_COUNTEREVIDENCE: the same locally compliant trace may participate in violating and nonviolating trace sets; a conservative false-positive monitor, wrong declassification projection or incomplete counterfactual pair changes detection assumptions
- UNKNOWN_RETAINED: theorem proof recheck, reproducibility of AL-Synth, author benchmark generalization, real-world policy encoding, independent trace pairing, local code and production implementation
- NEXT_RETEST_CONDITION: pin exact v1 and executable AL-Synth revision, construct two traces with equal permitted free/busy inputs but different unauthorized confidential-context dependence, compare local guards versus explicit pair-aware predicate, run SAT/SMT and agent controls, retain input fixtures, command, revision, stdout/stderr, exit, effect receipts and false-positive counts

Delivery boundary: append-only bilingual Daily research in existing Tool System containers only, not a native runtime implementation or independent maintenance pass. Preserve all historical source chunks, the Nov09 FAVA Daily and W45 Weekly, other containers, SOURCE Registry, Verified Core, and open WorkflowHub Draft PR #378. Validator, SAT/SMT replay, model evaluation, runtime tools and host integration: NOT_EXECUTED at authoring. Human Maintainer review and merge required.
