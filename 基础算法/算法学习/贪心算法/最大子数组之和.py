#问题描述：给定一个整数列表（元素有正有负），计算其连续子元素之和的最大值
def main():
    s= [12, -4, 32, -36, 12, 6, -6]
    print("定义的列表为： ",s)
    s_max, s_sum = 0, 0
    for i in range(len(s)):
        s_sum += s[i]
        if s_sum >= s_max:
            s_max = s_sum
        elif s_sum < 0:
            s_sum = 0#如果前面的和小于0，那其累加值会小于从新开始累加的累加值
    print("最大子列表之和为： ",s_max)

if __name__ == '__main__':
    main()