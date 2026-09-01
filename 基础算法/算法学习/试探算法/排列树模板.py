n = 4
x = [1, 2, 3, 4]
X = []
#冲突检测：无
def conflict(k):
    global n, x, X
    return False
#冲突检测：元素奇偶相间的所有排列
def conflict2(k):
    global n, x, X
    if k == 0:#第一个元素，肯定无冲突
        return False
    if x[k -1] % 2 == x[k] % 2:
        return True
    return False

#排列树递归模板
def backkrak(k):#到达第k个位置
    global n, x, X
    if k >= n:#超出最尾的位置
        print(x)
    else:
        for i in range(k, n):#遍历后面第k到n-1的位置
            x[k], x[i] = x[i], x[k]
            if not conflict2(k):#剪枝
                backkrak(k + 1)
            x[i], x[k] = x[k], x[i]#回溯
backkrak(0)