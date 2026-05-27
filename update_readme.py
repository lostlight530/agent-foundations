import sys

def replace_in_file(filepath, search_str, replace_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace(search_str, replace_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

# ZH table update
replace_in_file('README.md',
                'SimCLR + 无监督学习',
                'SimCLR + VICReg + 无监督学习')
replace_in_file('README.md',
                '梯度熵 (原创理论)',
                '梯度熵 (FIM/NTK 理论)')

# EN table update
replace_in_file('README.md',
                'SimCLR + Unsupervised Learning',
                'SimCLR + VICReg + Unsupervised Learning')
replace_in_file('README.md',
                'Gradient Entropy (Original Theory)',
                'Gradient Entropy (FIM/NTK Theory)')
