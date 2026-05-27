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
| **Federated Learning + Spatiotemporal** | **Collaboration System** | Ensures distributed convergence across multi-agent networks. Utilizes privacy-preserving aggregation and spatiotemporal graphs for non-IID data harmony without a central server. |
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
| **联邦学习 + 时空建模** | **协作系统 (Collaboration System)** | 保证多智能体网络中的分布式收敛。无需中心服务器，通过隐私保护聚合和时空图卷积网络解决 Non-IID 数据协同问题。 |
| **梯度熵 (FIM/NTK 理论)** | **架构原则 (Architecture Principle)** | 一种量化信息耗散的新型指标。通过锁定梯度熵的上下界，我们在物理与数学层面彻底阻断了模型崩溃与结构发散。 |

### 文档结构与导读
- `docs/en/`：英文深度技术文档目录。
- `docs/zh/`：中文深度技术文档目录。包含架构原则、协作系统、记忆系统和工具系统的全面解析（每篇千字以上），涵盖学术推导、源码剖析（伪代码）以及面向 0 基础读者的通俗讲解。

想了解详细的技术索引和阅读指南，请查阅 `docs/zh/` 和 `docs/en/` 目录下的专属 `README.md`。

---
*lostLight*
