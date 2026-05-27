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

new_collab_code_en = """        # 3. Byzantine Robust Filtering
        # Using Krum operator: identify the "honest" subset by calculating Euclidean distances
        filtered_updates = self._krum_filter(agent_updates)

        # 4. Apply Differential Privacy Noise
        for update in filtered_updates:
            local_grad = self._apply_differential_privacy(update['grad'])
"""

update_code_block_v2('docs/en/Collaboration_System.md', '# 3. Inject differential privacy noise', 'local_grad = self._apply_differential_privacy(local_grad)', new_collab_code_en)
