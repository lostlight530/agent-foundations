# Agent Foundations / 智能体理论基础

*(English version below | 中文版本见下)*

---

## 🇬🇧 English Version

> *The four repositories dictate what the system does. This repository explains why it works.*

### Introduction
Welcome to **Agent Foundations**, the theoretical skeleton and mathematical bedrock of a fully deterministic, self-converging Agent architecture. In an era where "Scale is All You Need" dominates AI, bringing stochastic black boxes and unpredictable hallucinations, we chose a fundamentally different path.

This repository compiles rigorous academic research across six major AI disciplines, dismantling the probabilistic nature of modern Large Language Models (LLMs) and rebuilding an Agent system from scratch. We do not rely on scale to probabilistically approximate intelligence; instead, we use mathematical proofs and rigid constraints to guarantee it.

### Core Philosophy

**We do not implement. We constrain.**
We eschew brittle, hard-coded `if-else` chains. Instead, we define continuous energy functions and mathematical boundary conditions. The agent explores freely within a constrained, safe manifold.

**We do not scale. We prove.**
We refuse to blindly stack parameters and hope for capabilities to emerge. Instead, we use convex optimization and Lyapunov stability theories to mathematically prove the behavioral lower bounds of the system.

**We do not optimize. We guarantee convergence.**
We model learning and decision-making as deterministic dynamical systems. Through meticulously designed algorithms, we ensure the agent inevitably stabilizes at a well-defined global or local minimum, immune to catastrophic forgetting.

### System Architecture & Research Matrix

Our research systematically surveyed the Agent capability matrix, resulting in four core systems backed by distinct theoretical pillars:

| Research Direction | Agent Component | Theoretical Role & Code Implication |
|-------------------|----------------|-------------------------------------|
| **SimCLR + VICReg + Unsupervised Learning** | **Memory System** | Replaces raw data storage with latent space representation learning. Enables true episodic memory via robust anomaly detection and contrastive feature extraction. |
| **RL (NLP) — Studied & Reversed** | **Tool System** | Transitions probabilistic tool use into a deterministic action space. We mapped RL value alignment, then reverse-engineered it into a hard-constrained causal execution graph. |
| **Distributed Direct Preference Optimization (DecDPO)** | **Collaboration System** | Ensures distributed convergence across multi-agent networks without a central server. Utilizes decentralized preference alignment and spectral connectivity to resolve Non-IID data harmony. |
| **Gradient Entropy (FIM/NTK Theory)** | **Architecture Principle** | A novel metric quantifying information dissipation. By clamping gradient entropy bounds, we physically prevent mode collapse and structural divergence. |

### Structure & Roadmap
- `docs/en/`: Deep-dive English documentation (1000+ words each) featuring academic derivations, source code/pseudocode analysis, and beginner-friendly analogies.
- `docs/zh/`: Equivalent deep-dive Chinese documentation.

For a detailed technical index and reading guide, please refer to the specific `README.md` within the `docs/en/` or `docs/zh/` directories.

---

## 🇨🇳 中文版本

> *其他四个仓库展示了系统在“做什么”，而本仓库揭示了系统“为什么有效”。*

### 简介
欢迎来到 **Agent Foundations（智能体理论基础）**。这里是构建一个完全确定性、自收敛智能体架构的理论骨架和数学基石。在“算力即一切（Scale is All You Need）”主导的时代，人工智能伴随着黑盒现象与不可预测的幻觉。我们选择了一条截然不同的道路。

本仓库汇集了横跨六大人工智能领域的严谨学术研究。我们解构了现代大语言模型（LLMs）的概率性质，从零开始重构了智能体系统。我们不依赖算力扩展来概率性地逼近智能，而是通过数学证明和严格约束来保障智能的必然性。

### 核心理念

**我们不实现，我们约束。**
我们摒弃脆弱的硬编码（if-else）规则。取而代之的是连续的能量函数与数学边界条件。智能体在一个被严格约束且安全的流形空间内自由探索。

**我们不扩展，我们证明。**
我们拒绝盲目堆叠参数以期盼能力的概率性涌现。我们运用凸优化和李雅普诺夫稳定性理论，从数学层面证明系统行为的下界与安全边界。

**我们不优化，我们保证收敛。**
我们将学习和决策建模为确定性的动力系统。通过精心设计的算法（如同质收敛的联邦网络），我们确保智能体最终必然稳定在定义明确的状态，绝不会发生灾难性遗忘。

### 系统架构与研究矩阵

我们历时半年的研究系统性地梳理了智能体能力矩阵，最终形成了由不同理论支柱支撑的四大核心系统：

| 学术研究方向 | 智能体核心组件 | 理论作用与源码启示 |
|-------------------|----------------|-------------------------------------|
| **SimCLR + VICReg + 无监督学习** | **记忆系统 (Memory System)** | 放弃原始数据存储，采用隐空间表征学习。通过对比特征提取和异常检测，实现真正的事件级和结构化记忆。 |
| **强化学习 (NLP) — 逆向工程** | **工具系统 (Tool System)** | 将概率性的工具使用转化为确定性的动作空间。我们学习了 RL 价值对齐，随后将其逆向推导为具有硬性约束的因果执行图。 |
| **Distributed Direct Preference Optimization (DecDPO)** | **协作系统 (Collaboration System)** | 保证多智能体网络中的分布式收敛。完全抛弃中心聚合服务器，利用去中心化偏好对齐和确定的谱连通性收敛来解决 Non-IID 数据协同问题。 |
| **梯度熵 (FIM/NTK 理论)** | **架构原则 (Architecture Principle)** | 一种量化信息耗散的新型指标。通过锁定梯度熵的上下界，我们在物理与数学层面彻底阻断了模型崩溃与结构发散。 |

### 文档结构与导读
- `docs/en/`：英文深度技术文档目录。
- `docs/zh/`：中文深度技术文档目录。包含架构原则、协作系统、记忆系统和工具系统的全面解析（每篇千字以上），涵盖学术推导、源码剖析（伪代码）以及面向 0 基础读者的通俗讲解。

想了解详细的技术索引和阅读指南，请查阅 `docs/zh/` 和 `docs/en/` 目录下的专属 `README.md`。


---

### 🗺️ [Monthly Strategic Blueprint] 月度理论防线加固与路线图大换血

#### ⚡ 外部黑盒翻车案例审计与免疫证明
- **故障扫描**：本月业内多智能体框架频繁暴露出“中心服务器单点故障（SPOF）”和“数据隐私泄漏”丑闻。当中心化调度节点宕机或遭遇恶意攻击时，整个由数万个 Agents 构成的集群瞬间瘫痪。
- **当前路线防御力评估**：我们本月在协作容器中正式部署的 DecDPO 理论对上述灾难完全免疫。因为在我们的数学设计中，根本不存在“总指挥”。每个节点仅依赖双随机混合矩阵 $\Lambda$ 与局部邻居通信，物理切断了单点故障的可能。

#### 🔄 核心研究方向修正与下月 Roadmap
- **方向废弃/替换评估（CRITICAL）**：基于本月的深度审计，我正式评估认为：原有的 **“联邦学习 (Federated Learning) + 时空图模型”** 范式中，联邦聚合过程虽然保护了隐私，但依旧残留了对中心参数服务器的路径依赖。**决定果断“切割”**！全面废弃中心化联邦学习，用纯粹的“去中心化分布式优化 (Decentralized Distributed Optimization)”彻底替换协作系统的底层骨架。
- **蓝图开辟**：继续维持四大系统容器，但 Collaboration 容器内部的理论血液已全部更新为“DecDPO”。
- **下月仓库演进路线图 (Roadmap)**：
  - [Collaboration]：全面编写基于网络谱间隙（Spectral Gap）验证去中心化收敛速度的 Python 分析模块，验证 $\mathcal{O}(1/\varepsilon^{2})$ 的时间复杂度下界。

***

### 🗺️ [Monthly Strategic Blueprint] Monthly Theoretical Defense Reinforcement & Roadmap Overhaul

#### ⚡ External Black-Box Failure Audit & Immunity Proof
- **Failure Scan**: This month, industry multi-agent frameworks frequently exposed scandals regarding "Single Point of Failure (SPOF) on central servers" and "data privacy leaks." When the centralized dispatch node crashed or was maliciously attacked, entire clusters consisting of tens of thousands of Agents paralyzed instantly.
- **Current Route Defense Assessment**: The DecDPO theory we officially deployed in the collaboration container this month is completely immune to the aforementioned disasters. In our mathematical design, there is fundamentally no "commander-in-chief." Each node relies solely on the doubly stochastic mixing matrix $\Lambda$ to communicate with local neighbors, physically severing the possibility of a single point of failure.

#### 🔄 Core Research Direction Correction & Next Month's Roadmap
- **Direction Deprecation/Replacement Assessment (CRITICAL)**: Based on this month's deep audit, I officially assess that: in the original **"Federated Learning + Spatiotemporal Graph Model"** paradigm, although the federated aggregation process protected privacy, it still retained a path dependence on a central parameter server. **Decided to decisively "change tracks"!** Completely deprecate centralized federated learning and thoroughly replace the underlying skeleton of the collaboration system with pure "Decentralized Distributed Optimization".
- **Blueprint Expansion**: Continue to maintain the four major system containers, but the theoretical blood inside the Collaboration container has been completely updated to "DecDPO".
- **Next Month's Repository Evolution Roadmap**:
  - [Collaboration]: Comprehensively write a Python analysis module based on the network's Spectral Gap to verify the decentralized convergence speed, validating the lower bound of time complexity at $\mathcal{O}(1/\varepsilon^{2})$.

---
*lostLight*
