#EDA = Exploratory Data Analysis（探索性数据分析）

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
df = sns.load_dataset('titanic')

# ============================
# 1. 单变量分析
# ============================
fig, axes = plt.subplots(2, 3, figsize=(14, 8))

# 生存分布（目标变量）
df['survived'].value_counts().plot(kind='bar', ax=axes[0, 0], color=['#E74C3C', '#2ECC71'])
axes[0, 0].set_title('生存分布（0=死亡, 1=幸存）')
axes[0, 0].set_xticklabels(['死亡', '幸存'], rotation=0)

# 年龄分布
df['age'].hist(bins=30, ax=axes[0, 1], edgecolor='black')
axes[0, 1].set_title('年龄分布')

# 性别分布
df['sex'].value_counts().plot(kind='bar', ax=axes[0, 2], color=['#3498DB', '#E91E63'])
axes[0, 2].set_title('性别分布')
axes[0, 2].set_xticklabels(axes[0, 2].get_xticklabels(), rotation=0)

# 舱位等级分布
df['class'].value_counts().plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('舱位等级分布')
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=0)

# 票价分布
df['fare'].hist(bins=40, ax=axes[1, 1], edgecolor='black', color='orange')
axes[1, 1].set_title('票价分布')

# 登船港口分布
df['embarked'].value_counts().plot(kind='bar', ax=axes[1, 2], color='green')
axes[1, 2].set_title('登船港口分布')
axes[1, 2].set_xticklabels(axes[1, 2].get_xticklabels(), rotation=0)

plt.tight_layout()
plt.show()

# ============================
# 2. 双变量分析
# ============================
fig2, axes2 = plt.subplots(2, 2, figsize=(12, 10))

# 性别 vs 生存
sns.barplot(x='sex', y='survived', data=df, ax=axes2[0, 0])
axes2[0, 0].set_title('性别与生存率')
axes2[0, 0].set_ylabel('生存率')

# 舱位等级 vs 生存
sns.barplot(x='class', y='survived', data=df, ax=axes2[0, 1])
axes2[0, 1].set_title('舱位等级与生存率')
axes2[0, 1].set_ylabel('生存率')

# 年龄 vs 生存（箱线图）
df.boxplot(column='age', by='survived', ax=axes2[1, 0])
axes2[1, 0].set_title('年龄与生存')
axes2[1, 0].set_xlabel('生存（0=死亡, 1=幸存）')
axes2[1, 0].set_ylabel('年龄')

# 票价 vs 生存（箱线图）
df.boxplot(column='fare', by='survived', ax=axes2[1, 1])
axes2[1, 1].set_title('票价与生存')
axes2[1, 1].set_xlabel('生存（0=死亡, 1=幸存）')
axes2[1, 1].set_ylabel('票价')

plt.suptitle('')  # 去掉自动加的标题
plt.tight_layout()
plt.show()

# ============================
# 3. 相关性热力图（负相关也是相关）
#因果性：A 导致 B。比如"因为女性被优先安排上救生艇，所以女性生存率高"——这是因果关系。而相关性只是"同时发生"。热力图上看到的数字都是相关性，不代表谁导致了谁。
# ============================
plt.figure(figsize=(8, 6))
# 选出数值列
numeric_cols = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
corr = df[numeric_cols].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=1)
plt.title('数值变量相关矩阵')
plt.show()

# ============================
# 4. 多变量分析：舱位+性别+生存
# ============================
plt.figure(figsize=(8, 5))
sns.barplot(x='class', y='survived', hue='sex', data=df)
plt.title('按舱位和性别分组的生存率')
plt.ylabel('生存率')
plt.show()