import sys

def update_code_block_v2(filepath, start_marker, end_marker, new_content):
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
        print(f"Updated {filepath}")
    else:
        print(f"Markers not found in {filepath}")

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

update_code_block_v2('docs/en/Memory_System.md', '# 1. Extract features and project', 'pass', new_memory_code_en)
