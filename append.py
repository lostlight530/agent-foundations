import re

en_chunk = """### Multi-Agent Flow Matching with Decoupled Generative Guidance (DeGG-Flow)

- **Technical Point:** Multi-Agent Flow Matching with Decoupled Generative Guidance (DeGG-Flow)
- **System Container:** Architecture Principles
- **Frontier Source:** Ruoyu Lin, Magnus Egerstedt, Fabio Pasqualetti. *Multi-Agent Flow Matching with Decoupled Generative Guidance*. arXiv:2609.38133v1.
- **Original Paper Problem:** Generating multi-agent behavior with hard, coupled constraints. Standard joint guidance couples all agents (creating a central point of failure), while decentralized settings need a way to ensure each agent computes its own guidance input to satisfy team-level constraints.
- **Core Assumptions:**
  - The shared requirement function $q_a^{\\mathrm{SE}}$ and bound function $\\beta_a^{\\mathrm{SE}}$ are $C^1$.
  - The probability distributions $\\mu_1$ and $\\nu_1$ have finite second moments.
  - The vector field $f^{\\theta}$ is Lipschitz continuous with respect to the generated state with integrable Lipschitz constant $L(\\tau)$.
  - The expected squared norm of the guidance correction $\\Gamma(s\\,|\\,\\xi)$ over the initial distribution is integrable over time.
- **Mathematical Mechanism:** DeGG-Flow represents the generative process as a control-affine dynamical system. It develops guidance conditions for shared requirements (dependent on multiple agents) and private requirements (dependent on an agent and its neighbors) by establishing feasibility conditions and finite-horizon convergence guarantees.
  - Convergence Bound:
    $$W_2(\\mu_1,\\nu_1) \\leq \\int_0^1 \\! \\exp\\!\\left( \\int_s^1 \\! L(r) \\,\\mathrm{d}r \\right) \\sqrt{ \\int_{\\mathcal{Z}^{N}}\\! \\left\\|\\Gamma(s\\,|\\,\\xi)\\right\\|^2 p_0(\\xi) \\,\\mathrm{d}\\xi } \\;\\mathrm{d}s$$
- **Convergence or behavior boundaries:** If the final boundary condition $\\beta_a^{\\mathrm{SE}}(1\\,|\\,\\chi,\\mathbf{z}(0))=0$ is met, then $q_a^{\\mathrm{SE}}(1,\\mathbf{z}_{\\mathcal{S}_a^{\\mathrm{SE}}}(1)\\,|\\,\\chi)\\leq 0$, meaning the final generated state strictly satisfies the shared hard requirement. The Wasserstein distance $W_2(\\mu_1,\\nu_1)$ between the nominal and guided distributions is bounded by the integrated guidance correction.
- **Applicable Scope:** Multi-agent generative environments requiring hard constraint satisfaction, such as multi-robot collaboration and scene generation with affordance requirements.
- **Limitations:** Theoretical bounds assume Lipschitz continuity of the underlying vector fields and finite second moments of the distributions. The framework requires the final bound condition to strictly reach zero to guarantee exact constraint satisfaction.
- **Agent Architecture Mapping:** CONCEPTUAL_MAPPING. Can conceptually support generative agent architectures by introducing decoupled guidance modules, ensuring that decentralized outputs from multiple autonomous agents satisfy shared system-level hard constraints without requiring synchronized internal state exchange during generation.
- **Repository Implementation Status:** NOT_IMPLEMENTED
- **Repository Test Status:** NOT_TESTED
- **Beginner Analogy:** Imagine multiple artists painting a large mural together. If they don't coordinate, the final picture will be chaotic. Instead of constantly stopping to discuss every brushstroke, each artist follows a set of decoupled "guardrails" (guidance) that ensures their individual work will perfectly align with the others at the edges, guaranteeing the final mural satisfies the overall design without needing real-time micromanagement.
- **Evidence Status:**
  - Paper Evidence Status: VERIFIED_FROM_LATEX_SOURCE
  - Architecture Mapping Status: CONCEPTUAL_MAPPING
  - Repository Implementation Status: NOT_IMPLEMENTED
  - Repository Test Status: NOT_TESTED
"""

zh_chunk = """### 具有解耦生成引导的多智能体流匹配 (DeGG-Flow)

- **技术点 (Technical Point):** 具有解耦生成引导的多智能体流匹配 (DeGG-Flow)
- **System Container:** Architecture Principles
- **Frontier Source:** Ruoyu Lin, Magnus Egerstedt, Fabio Pasqualetti. *Multi-Agent Flow Matching with Decoupled Generative Guidance*. arXiv:2609.38133v1.
- **论文原始问题 (Original Paper Problem):** 生成具有硬性、耦合约束的多智能体行为。标准的联合引导会将所有智能体耦合（产生单点故障），而去中心化设置需要一种方法来确保每个智能体计算自己的引导输入以满足团队级别的约束。
- **核心假设 (Core Assumptions):**
  - 共享需求函数 $q_a^{\\mathrm{SE}}$ 和边界函数 $\\beta_a^{\\mathrm{SE}}$ 是 $C^1$ 的。
  - 概率分布 $\\mu_1$ 和 $\\nu_1$ 具有有限的二阶矩。
  - 向量场 $f^{\\theta}$ 关于生成状态是李普希茨连续的，且李普希茨常数 $L(\\tau)$ 是可积的。
  - 引导校正 $\\Gamma(s\\,|\\,\\xi)$ 在初始分布上的期望范数平方随时间是可积的。
- **数学机制 (Mathematical Mechanism):** DeGG-Flow 将生成过程表示为控制仿射动力系统。通过建立可行性条件和有限视界收敛保证，它为共享需求（依赖于多个智能体）和私有需求（依赖于智能体及其邻居）开发了引导条件。
  - 收敛界 (Convergence bound):
    $$W_2(\\mu_1,\\nu_1) \\leq \\int_0^1 \\! \\exp\\!\\left( \\int_s^1 \\! L(r) \\,\\mathrm{d}r \\right) \\sqrt{ \\int_{\\mathcal{Z}^{N}}\\! \\left\\|\\Gamma(s\\,|\\,\\xi)\\right\\|^2 p_0(\\xi) \\,\\mathrm{d}\\xi } \\;\\mathrm{d}s$$
- **收敛或行为边界 (Convergence or behavior boundaries):** 如果满足最终边界条件 $\\beta_a^{\\mathrm{SE}}(1\\,|\\,\\chi,\\mathbf{z}(0))=0$，则 $q_a^{\\mathrm{SE}}(1,\\mathbf{z}_{\\mathcal{S}_a^{\\mathrm{SE}}}(1)\\,|\\,\\chi)\\leq 0$，这意味着最终生成的状态严格满足共享的硬需求。标称分布和引导分布之间的 Wasserstein 距离 $W_2(\\mu_1,\\nu_1)$ 由积分的引导校正界定。
- **适用范围 (Applicable Scope):** 需要满足硬约束的多智能体生成环境，例如多机器人协作和具有启示性要求的场景生成。
- **局限 (Limitations):** 理论边界假设底层向量场的李普希茨连续性和分布的有限二阶矩。该框架要求最终边界条件严格达到零，以保证精确的约束满足。
- **Agent 架构映射 (Agent Architecture Mapping):** CONCEPTUAL_MAPPING。通过引入解耦的引导模块，在概念上支持生成式智能体架构，确保来自多个自治智能体的去中心化输出满足共享的系统级硬约束，而无需在生成期间同步交换内部状态。
- **仓库实现状态 (Repository Implementation Status):** NOT_IMPLEMENTED
- **仓库测试状态 (Repository Test Status):** NOT_TESTED
- **初学者类比 (Beginner Analogy):** 想象多个艺术家一起绘制一幅大型壁画。如果他们不协调，最终的画面将是混乱的。每个艺术家不需要经常停下来讨论每一笔，而是遵循一套解耦的“护栏”（引导），这确保了他们个人的工作在边缘处与其他人的完美对齐，从而保证最终的壁画满足整体设计，而不需要实时的微观管理。
- **证据状态 (Evidence Status):**
  - Paper Evidence Status: VERIFIED_FROM_LATEX_SOURCE
  - Architecture Mapping Status: CONCEPTUAL_MAPPING
  - Repository Implementation Status: NOT_IMPLEMENTED
  - Repository Test Status: NOT_TESTED
"""

def append_to_file(filepath, chunk):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if the chunk title already exists
    if 'Multi-Agent Flow Matching with Decoupled Generative Guidance' in content:
        # replace the old incomplete chunk using string manipulation instead of regex sub to avoid backslash issues
        pattern = re.compile(r"### Multi-Agent Flow Matching with Decoupled Generative Guidance.*?(?=\n### |\Z)", re.DOTALL)
        match = pattern.search(content)
        if match:
            start, end = match.span()
            content = content[:start] + chunk + content[end:]
        else:
            # Just in case
            content = content + "\n\n" + chunk
    else:
        content = content + "\n\n" + chunk

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

append_to_file('docs/en/Architecture_Principles.md', en_chunk)
append_to_file('docs/zh/Architecture_Principles.md', zh_chunk)
