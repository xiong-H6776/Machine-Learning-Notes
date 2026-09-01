# 1. 导入库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 让 matplotlib 使用系统中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示异常
# 2. 加载 Titanic 数据集
df = sns.load_dataset('titanic')

# 3. 基础探索
print('=== 基本信息 ===')
print(f'数据集大小: {df.shape[0]} 行, {df.shape[1]} 列\n')

print('=== 前 8 行 ===')
print(df.head(8), '\n')

print('=== 列信息 ===')
print(df.info(), '\n')

print('=== 统计摘要 ===')
print(df.describe(), '\n')

print('=== 缺失值 ===')
print(df.isnull().sum(), '\n')

print('=== 生存分布 ===')
print(df['survived'].value_counts(), '\n')
#value_counts() 默认按值排序，所以 0（死亡）排前面，1（幸存）排后面

# 4. 画直方图
plt.figure(figsize=(10, 5))
df['age'].hist(bins=30, edgecolor='black', alpha=0.7)
plt.title('Titanic 乘客年龄分布')
plt.xlabel('年龄')
plt.ylabel('人数')
plt.grid(alpha=0.3)
plt.show()