#斐波那契数列：1，1，2，3，5，8，13...后一项等于前俩项之和，也称“兔子数列”。

#1.输出第n项
"""
fib_table = {}

def fib_num(n):
   if (n <= 1):
      return n
   if n not in fib_table:
       fib_table[n] = fib_num(n - 1) + fib_num(n - 2)
   return fib_table[n]

n = int(input("请输入斐波那契数列的第n项 \n"))
print("斐波那契数列第",n,"项是", fib_num(n))
"""
#输入999报错，windows系统对递归深度的默认限制值为998

#2.输出前n项
"""
fib_table = {}

def fib_num(n):
   if (n <= 1):
      return n
   if n not in fib_table:
       fib_table[n] = fib_num(n - 1) + fib_num(n - 2)
   return fib_table[n]
   
n = int(input("请输入n \n"))
for i in range(1,n+1):
    print(fib_num(i),end=" ")
"""
#时间复杂度为O(1.618^n)

#3.利用记忆法缓存加速计算
#LRU缓存算法：利用缓存加速计算，将消耗较大的计算结果记录，当相同调用时无需重复计算
#函数lru_cache()是一个内置的函数缓存装饰器:
#@functools.lru_cache(maxsize = 128, typed =False)
#参数maxsize为最大缓存量，如果赋值为None，即表示无上限，且关闭lru功能；参数typed表示当控制函数参数类型不同是否单独缓存，设置为Ture后，f（3）与f（3.0）不等同
import functools

@functools.lru_cache(maxsize = 128, typed =False)
def fib_recur(n):
    assert n >= 0,"n > 0"
    if n <=1:
      return n
    return fib_recur(n-1) + fib_recur(n-2)
n = int(input("请输入n \n"))
for i in range(1,n+1):
    print(fib_recur(i),end=" ")
