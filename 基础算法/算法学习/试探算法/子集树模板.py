#找出【1，2，3，4】奇偶性相同且和小于8的全部子集
n = 4#数据规模（可改）
a = [1, 2, 3, 4]#原始数据（可改）
x = []#一个解
X = []#一组解

#冲突检测1:空壳占位，可填入详细的约束条件
def conflict(k):
    global n, x, X, a
    return False
#冲突检测2（例子）：奇偶性相同且和小于8（可改）
def conflict2(k):
    global n, x, X, a
    if k == 0:#第0层不可能冲突
        return False

    s = [y[0] for y in filter(lambda s: s[1] != 0, zip(a[:k + 1], x[:k + 1]))]
    #zip(a[：k + 1],x[: k + 1]):将a和x序列的0到k的值一一配对，产生一组元组(a[0], x[0]), (a[1], x[1]), ..., (a[k], x[k])
    #lambda s: s[1] != 0:等价于def 匿名函数(s):return s[1] != 0
    #filter(条件函数, 可迭代对象):按条件筛选
    #本句作用：构造元组s，并从里面筛选出x值不得于0的元素保留
    #等同于s = [a[i] for i in range(k + 1) if x[i] != 0]
    if len(s) ==0:
        return False
    #约束条件：奇偶性相同且和小于8，True表示发生冲突
    if 0< sum(map(lambda y: y%2, s))< len(s) or sum(s) >=8:
        return True
    return False
def subset(k):
    global n, x, X
    if k>= n:#已处理的元素
        X.append(x[:])#保存当前完整解的副本
    else:
        for i in [1, 0]:#尝试俩种选择(1选；0不选)
            x.append(i)#选择
            if not conflict2(k):#如果不冲突
                subset(k + 1)#递归下一层
            x.pop()#否则回溯

def get_a_subset(x):
    global a
    return [y[0] for y in filter(lambda s: s[1] != 0,zip(a, x))]

def get_all_subsets(X):
    return [get_a_subset(x) for x in X]

subset(0)
print(get_all_subsets(X))