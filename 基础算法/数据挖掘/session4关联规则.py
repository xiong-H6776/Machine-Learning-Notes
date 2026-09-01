import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

# ============================
# 1. 构造模拟超市交易数据
# ============================
# 每一行是一笔交易，每列是一个商品，1 表示买了，0 表示没买
transactions = pd.DataFrame({
    '牛奶': [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    '面包': [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    '黄油': [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    '鸡蛋': [0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    '啤酒': [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    '尿布': [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    '咖啡': [1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    '可乐': [0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
})

print('=== 原始交易数据（前 10 笔）===')
print(transactions)
print(f'\n交易总数: {len(transactions)}')

# ============================
# 2. 计算频繁项集
# ============================
print('\n=== 频繁项集（min_support=0.3）===')
frequent_itemsets = apriori(transactions, min_support=0.3, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(len)
print(frequent_itemsets.sort_values('support', ascending=False).to_string(index=False))

# ============================
# 3. 提取关联规则
# ============================
print('\n=== 关联规则 ===')
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1.0)

# 只看有用的列
rules_display = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].copy()
rules_display['antecedents'] = rules_display['antecedents'].apply(lambda x: ', '.join(list(x)))
rules_display['consequents'] = rules_display['consequents'].apply(lambda x: ', '.join(list(x)))
rules_display = rules_display.sort_values('lift', ascending=False)
print(rules_display.to_string(index=False))

# ============================
# 4. 解读最有趣的规则
# ============================
print('\n=== Top 3 规则解读 ===')
top3 = rules_display.head(3)
for i, (_, rule) in enumerate(top3.iterrows()):
    print(f'\n规则 {i+1}:')
    print(f'  买了 "{rule["antecedents"]}" 的人，也买了 "{rule["consequents"]}"')
    print(f'  支持度: {rule["support"]:.0%}（{rule["support"]*10:.0f}/10 的交易包含这个组合）')
    print(f'  置信度: {rule["confidence"]:.0%}（买了前者的顾客中，{rule["confidence"]:.0%} 也买了后者）')
    print(f'  提升度: {rule["lift"]:.2f}（>1 表示正相关，=1 无关联，<1 负相关）')