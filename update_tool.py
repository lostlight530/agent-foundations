import sys

def replace_in_file(filepath, search_str, replace_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace(search_str, replace_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

# ZH updates
replace_in_file('docs/zh/Tool_System.md',
                '直接编译转化为了具有绝对因果逻辑关系的、纯纯的确定性执行路由流',
                '通过 **符号策略蒸馏（Symbolic Policy Distillation）** 技术，将复杂的策略网络直接编译转化为具有绝对因果逻辑关系的、具备可解释性的确定性执行路由流')

# EN updates
replace_in_file('docs/en/Tool_System.md',
                'compiling it directly into a pure, deterministic execution router with absolute causal logic.',
                'compiling it via **Symbolic Policy Distillation** into a pure, interpretable, and deterministic execution router with absolute causal logic.')

# Add a small section about Symbolic Policy Distillation in both
symbolic_zh = """
* **符号策略蒸馏 (Symbolic Policy Distillation)**：强化学习学到的是黑盒的概率分布，而我们的生产环境需要的是“看得见、摸得着”的逻辑。我们利用决策树或符号回归技术，从训练好的策略网络中提取出最核心的判定逻辑，并将其转化为确定性的代码路由。这使得每一笔工具调用的理由都可以在数学和逻辑上被事后追溯。
"""

symbolic_en = """
* **Symbolic Policy Distillation**: While RL learns a black-box probability distribution, our production environment demands "tangible" logic. We utilize decision trees or symbolic regression techniques to extract the core decision-making logic from the trained policy networks, transforming them into deterministic code routers. This ensures that the rationale behind every tool call is mathematically and logically traceable.
"""

def insert_after(filepath, marker, text):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if marker in line:
            new_lines.append(text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Inserted in {filepath}")

insert_after('docs/zh/Tool_System.md', '将发疯的概率降至 0。', symbolic_zh)
insert_after('docs/en/Tool_System.md', 'dropping the probability of agent madness to absolute zero.', symbolic_en)
