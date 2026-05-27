import sys

def replace_in_file(filepath, search_str, replace_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace(search_str, replace_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

# ZH updates
replace_in_file('docs/zh/Memory_System.md',
                'SimCLR（无监督对比学习）',
                'SimCLR 与 VICReg（方差-不变性-协方差正则化）')

replace_in_file('docs/zh/Memory_System.md',
                '（Invariant Features）',
                '（Invariant Features）。通过引入 VICReg 约束，我们不仅要求“认得准”，还要求隐空间的表征必须具备足够高的方差和低协方差，从数学层面彻底杜绝表征崩溃（Representation Collapse）。')

# EN updates
replace_in_file('docs/en/Memory_System.md',
                'SimCLR (Simple Framework for Contrastive Learning of Visual Representations)',
                'SimCLR and **VICReg (Variance-Invariance-Covariance Regularization)**')

replace_in_file('docs/en/Memory_System.md',
                '(Invariant Features).',
                '(Invariant Features). By introducing VICReg constraints, we ensure not only "recognition" but also that the latent space representations maintain high variance and low covariance, mathematically eliminating the risk of **Representation Collapse**.')

# Code update for Memory System
new_memory_code_zh = """        # 1. 提取特征并降维投影
        z1 = self.projector(self.encoder(x_t1))
        z2 = self.projector(self.encoder(x_t2))

        # 2. 核心：VICReg 损失计算 (防止崩溃)
        # Variance: 保证特征不缩减为单一常数
        std_z = torch.sqrt(z1.var(dim=0) + 1e-4)
        std_loss = torch.mean(F.relu(1 - std_z))

        # Covariance: 保证特征之间互不冗余 (解耦)
        cov_z = (z1.T @ z1) / (z1.shape[0] - 1)
        cov_loss = (cov_z.pow(2).sum() - cov_z.pow(2).diag().sum()) / z1.shape[1]

        # Invariance: 保证时序稳定性 (传统 SimCLR 核心)
        sim_loss = F.mse_loss(z1, z2)

        return sim_loss + std_loss + cov_loss
"""

def update_code_block(filepath, start_marker, end_marker, new_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if start_marker in line:
            start_idx = i
        if start_idx != -1 and end_marker in line:
            end_idx = i
            break
    if start_idx != -1 and end_idx != -1:
        new_lines = lines[:start_idx] + [new_content] + lines[end_idx+1:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated code in {filepath}")

update_code_block('docs/zh/Memory_System.md', '# 1. 提取特征并降维投影', 'pass', new_memory_code_zh)

new_memory_code_en = """        # 1. Feature extraction & Projection
        z1 = self.projector(self.encoder(x_t1))
        z2 = self.projector(self.encoder(x_t2))

        # 2. Core: VICReg Loss (Collapse Prevention)
        # Variance: Prevents all samples from collapsing to a single point
        std_z = torch.sqrt(z1.var(dim=0) + 1e-4)
        std_loss = torch.mean(F.relu(1 - std_z))

        # Covariance: Decouples features to ensure zero redundancy
        cov_z = (z1.T @ z1) / (z1.shape[0] - 1)
        cov_loss = (cov_z.pow(2).sum() - cov_z.pow(2).diag().sum()) / z1.shape[1]

        # Invariance: Traditional MSE/SimCLR objective
        sim_loss = F.mse_loss(z1, z2)

        return sim_loss + std_loss + cov_loss
"""
update_code_block('docs/en/Memory_System.md', '# 1. 提取特征并降维投影', 'pass', new_memory_code_en)
