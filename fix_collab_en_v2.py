import sys

def update_code_block_v3(filepath, start_marker, end_marker, new_content):
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

new_collab_code_en = """            # 3. Byzantine Robust Filtering (Krum) & Differential Privacy
            local_grad = self._apply_krum_and_dp(local_grad)
"""

update_code_block_v3('docs/en/Collaboration_System.md', '# 3. Inject Differential Privacy noise', 'local_grad = self._apply_differential_privacy(local_grad)', new_collab_code_en)
