#只要求索引表是有序的，对块内节点没有排序要求，适合于节点动态变化的情况
#1.将列表分为若干块2.构造一个索引表：索引表记录每一块的起始位置于最大关键字（或最小关键字）
import random
Range = 20
Length = 9
flag = 0
pos = -1
tabNum = 3
tabPos = -1

list = random.sample(range(Range), Length)
goal = random.randint(0, Range)
print('开始查找数字', goal, ',在下面的列表中查找：')

list_index = []
for i in range(tabNum):
    list_index.append([])

for i in range(1, tabNum):
    list_index[i].append(list[i -1])
for i in range(1, tabNum - 1):
    for j in range(1, tabNum - 1):
        if list_index[j] < list_index[j + 1]:
            list_index[j], list_index[j + 1] = list_index[j + 1], list_index[j]

for i in range(tabNum -1, Length):
    for j in range(1, tabNum):
        if list[i] > list_index[j][0]:
            list_index[j - 1].append(list[i])
            break
    else:
        list_index[tabNum - 1].append(list[i])
if len(list_index[0]) > 1:
    for i in range(len(list_index[0]) -1, 0, -1):
        if list_index[0][i] > list_index[0][i - 1]:
            list_index[0][i], list_index[0][i - 1] = list_index[0][i - 1], list_index[0][i]
print(list_index)

for i in range(tabNum -1 , -1, -1):
    if len(list_index[i]) != 0 and goal <list_index[i][0]:
        for j in range(len(list_index[i])):
            if list_index[i][j] == goal:
                tabPos = i+1
                pos = j+1
                flag =1

if flag:
    print("查找结果：在第", tabPos, "个列表中，索引值是", pos)
else:
    print("未找到")