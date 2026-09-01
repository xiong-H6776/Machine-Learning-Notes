import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
df = sns.load_dataset('titanic')
print('原始数据形状:', df.shape)

# --------------------------------
# 1. 检查缺失值
# --------------------------------
print('\n=== 缺失值统计 ===')
missing = df.isnull().sum()
print(missing[missing > 0])

# --------------------------------
# 2. 处理 Age 缺失——用中位数填充（数值类可用中位数、均值填充）
# --------------------------------
# 先看填充前的年龄分布
age_before = df['age']

# 用中位数填充
df['age'] = df['age'].fillna(df['age'].median())

print(f'\n年龄缺失填充完毕。填充值: {df["age"].median():.0f} 岁')
print(f'填充后年龄缺失数: {df["age"].isnull().sum()}')

# 填充前后对比
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
age_before.hist(bins=30, ax=axes[0], edgecolor='black')
axes[0].set_title('填充前（有缺失）')
df['age'].hist(bins=30, ax=axes[1], edgecolor='black', color='orange')
axes[1].set_title(f'填充后（中位数={df["age"].median():.0f}）')
plt.tight_layout()
plt.show()

# --------------------------------
# 3. 处理 Embarked 缺失——用众数填充（类别型属性可用众数填充）
# --------------------------------
print('\n=== Embarked 缺失处理 ===')
print('原始值分布:')
print(df['embarked'].value_counts())

mode_val = df['embarked'].mode()[0]
print(f'众数: {mode_val}')
df['embarked'] = df['embarked'].fillna(mode_val)
print(f'填充后 Embarked 缺失数: {df["embarked"].isnull().sum()}')

# --------------------------------
# 4. 异常值检测（IQR 方法）
# --------------------------------
print('\n=== Fare（票价）异常值检测 ===')
Q1 = df['fare'].quantile(0.25)
Q3 = df['fare'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['fare'] < lower) | (df['fare'] > upper)]
print(f'IQR 范围: [{lower:.2f}, {upper:.2f}]')
print(f'异常值数量: {len(outliers)}（占总数据 {len(outliers)/len(df)*100:.1f}%）')

# 箱线图可视化
plt.figure(figsize=(8, 4))
plt.boxplot(df['fare'])
plt.title('Fare 箱线图（圈起来的点是异常值）')
plt.ylabel('票价')
plt.grid(alpha=0.3)
plt.show()

# --------------------------------
# 5. 检查重复值
# --------------------------------
print(f'\n=== 重复值检查 ===')
print(f'完全重复的行数: {df.duplicated().sum()}')

# --------------------------------
print('\n=== 最终数据形状 ===')
print(f'清洗后: {df.shape[0]} 行, {df.shape[1]} 列')
print(f'剩余缺失值总数: {df.isnull().sum().sum()}')