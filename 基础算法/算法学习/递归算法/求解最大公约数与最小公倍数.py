#使用递归计算俩个数的最大公约数与最小公倍数
#算法分析：
#1.最大公约数：用大数除以小数取余，若余数不为0，则用小数除以余数得到新的余数，而前一步余数则为新的小数，逐一类推，直到余数为0，此时的小数则为最大公约数


"""
def gcd(a,b):
    if (a == b or b ==0):
        return a
    elif a > b:
        return gcd(b,a % b)
    else:
        return gcd(a,b % a)
test_cases = [(35, 14), (88, 66), (20, 10)]
for case in test_cases:
    print('GCD of {} & {} is {}'.format(*case, gcd(*case)))
"""


#2.最小公倍数：最小公倍数 = 俩整数的乘积➗最大公约数

def gcd(a,b):
    if (a == b or b ==0):
        return a
    elif a > b:
        return gcd(b,a % b)
    else:
        return gcd(a,b % a)

def lcm(a,b):
    return (a*b)//(gcd(a,b))
test_cases = [(4, 8), (35,42), (5,7)]
for case in test_cases:
    print('LCM of {} & {} is {}'.format(*case, lcm(*case)))
