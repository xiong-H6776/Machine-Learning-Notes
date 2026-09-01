#问题描述：输出n个数的全排列，n=1,数为1;n=2,数为1，2;n=3,数为1，2，3,...
import copy

def perm(n):
    data = []
    if n == 1:
        data.append([1])
    else:
        for m in perm(n - 1):
            for j in range(len(m) + 1):
                k = copy.copy(m) #递归，浅拷贝函数——copy函数，当b = copy.copy(a)时，b与a的元素相等，当修改b的独立元素赋值，a不改变；当修改b的内层嵌套的列表，a也会同步改变。如果要让内外层都随这b改变，可以直接赋值b = a；如果需要让内外层都不影响a，可以使用copy库中的深拷贝函数deepcopy（）。
                k.insert(j,n)
                data.append(k)
    return data

print(perm(4))
