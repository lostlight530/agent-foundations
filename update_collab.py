import sys

def replace_in_file(filepath, search_str, replace_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace(search_str, replace_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

# ZH updates
replace_in_file('docs/zh/Collaboration_System.md',
                '采用经过严格数学约束改进的 FedAvg（联邦平均）算法',
                '采用具备 **拜占庭容错（Byzantine Robustness）** 能力的聚合协议（如 Krum 或 Bulyan 算法），改进了传统的 FedAvg')

replace_in_file('docs/zh/Collaboration_System.md',
                '防止恶意节点通过超大梯度毒化全局模型',
                '通过 Krum 算子识别并剔除离群的异常梯度，防止恶意或故障节点毒化全局模型')

# EN updates
replace_in_file('docs/en/Collaboration_System.md',
                'Utilizes mathematically constrained improvements to the FedAvg (Federated Averaging) algorithm',
                'Utilizes **Byzantine Robust** aggregation protocols (such as Krum or Bulyan) to improve upon the traditional FedAvg algorithm')

replace_in_file('docs/en/Collaboration_System.md',
                'prevent malicious nodes from poisoning the global model with massive gradients.',
                'identify and prune outlier gradients via the Krum operator, preventing malicious or faulty nodes from poisoning the global model.')

# Update pseudocode with Byzantine check
new_collab_code_zh = """        # 3. 拜占庭容错处理 (Byzantine Robustness)
        # 采用 Krum 算子：计算各梯度间的欧氏距离，选取距离最近的“诚实”子集
        filtered_updates = self._krum_filter(agent_updates)

        # 4. 注入差分隐私噪声
        for update in filtered_updates:
            local_grad = self._apply_differential_privacy(update['grad'])
"""

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
        print(f"Updated code in {filepath}")

update_code_block_v2('docs/zh/Collaboration_System.md', '# 3. 注入差分隐私噪声', 'local_grad = self._apply_differential_privacy(local_grad)', new_collab_code_zh)

new_collab_code_en = """        # 3. Byzantine Robust Filtering
        # Using Krum operator: identify the "honest" subset by calculating Euclidean distances
        filtered_updates = self._krum_filter(agent_updates)

        # 4. Apply Differential Privacy Noise
        for update in filtered_updates:
            local_grad = self._apply_differential_privacy(update['grad'])
"""
update_code_block_v2('docs/en/Collaboration_System.md', '# 3. Inject differential privacy noise', 'local_grad = self._apply_differential_privacy(local_grad)', new_collab_code_en)
