#python内置函数可实现查找功能
aList = [1, 2, 3, 4, 5, 6, 3, 8, 9]
print(5 in aList)
print(5 not in aList)#查找数据5是否不在列表中
print(aList.index(5))#返回数据5的下标
print(aList.index(5, 4, 10))#从下标4到10（不包含）查找数据5
print(aList.count(5))#返回数据5的个数