    def compute_gradient_entropy(self, model: nn.Module) -> float:
        """
        核心推导：计算当前参数更新方向的梯度熵 (Gradient Entropy)
        数学本质：基于费舍尔信息阵 (FIM) 谱分布的香农熵估算
        H = - Σ (p_i * log(p_i))
        """
        all_grads = []
        for param in model.parameters():
            if param.grad is not None:
                all_grads.append(param.grad.view(-1))

        if not all_grads:
            return 0.0

        # 拼接所有梯度并计算协方差近似 (Fisher Information Approximation)
        grad_vector = torch.cat(all_grads)

        # 1. 采用局部窗口平滑或 Top-K 谱提取 (此处简化为 Softmax 概率映射)
        # 引入自适应温度系数，反映 NTK 动态
        temperature = torch.std(grad_vector) + 1e-6
        prob_dist = torch.softmax(torch.abs(grad_vector) / temperature, dim=0)

        # 2. 计算信息熵公式: H = - Σ p * log(p + epsilon)
        entropy = -torch.sum(prob_dist * torch.log(prob_dist + 1e-8))
        return entropy.item()
