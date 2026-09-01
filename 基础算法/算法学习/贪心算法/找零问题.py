#问题描述：假设只有1分、2分、5分、1角、2角、5角、1元的硬币，结账时，收银员希望将最少的硬币数找给顾客，如何确定
#算法分析：贪心算法，尽可能利用面值的大的硬币，从大面值开始遍历
def main():
    d = [ 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    d_num = []
    s = 0
    temp = input('请输入每种零钱的数量： ')
    d_num0 = temp.split(' ')
    for i in range(0, len(d_num0)):
         d_num.append(int(d_num0[i]))
         s += d[i] *d_num[i]#计算收银员拥有多少钱

    sum = float(input("请输入需要找的零钱： "))

    if sum>s:
        print("找零金额过大，无法找零")
        return 0

    s = s-sum
    i = 6
    while i>=0:
        if sum >= d[i]:
            n = int(sum / d[i])
            if n >= d_num[i]:
                n = d_num[i]
            sum -= n *d[i]
            print("用了%d个%f元硬币"%(n , d[i]))
        i -= 1
if __name__ == '__main__':
    main()