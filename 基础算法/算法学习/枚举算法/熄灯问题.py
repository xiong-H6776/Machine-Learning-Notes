import numpy as np
# 问题描述：
# 5*6大小的灯矩阵，部分灯亮，部分灯灭（随机初始状态），按下与灯同位置的按钮，
# 四周相邻的灯变换状态（自身和上下左右，不包含对角线上的灯），按哪些按钮能使得灯全灭。

# 1.按下第1行按钮（有2^6种按法，需一一枚举），对于第1行仍亮着的灯，用第2行按钮控制，以此类推
# 2.结束后判断最后一行是否全熄灭，全熄灭则方式正确，否则，改变第1行按钮的按法
# 3.灯的最后状态取决于自身初始状态与周围按钮是否按下（包括自身），且2次按钮作用会相互抵消，得到puzzle\[i][j]的最后状态公式为：
# puzzle\[i][j] = (press\[i][j-1] + press\[i][j] + press\[i][j+1] + press\[i-1][j] + puzzle\[i][j] )%2
# 4.press\[i+1][j]的取值完全由puzzle\[i][j]的值决定，puzzle\[i][j] = 1（灯亮），则press\[i+1][j] = 1（按下按钮），即puzzle\[i][j] = press\[i+1][j]
# 5.如果第5行灯全熄灭，则找到答案，否则换一种第一行按钮的按法（遍历）


line = [[0] * 6] * 5
for i in range(5):
    line[i] = input("请输入第" + str(i) + "行: ").split(',')
    #将line的元素转为整型
    line[i] = list(map(int, line[i]))

puzzle = np.array(line)
zero =np.zeros(6)
#为了让公式使用于边界位置，在puzzle矩阵上面，左边，右边都加入0
puzzle = np.insert(puzzle, 0, values=zero, axis=0)
puzzle = np.insert(puzzle, 6, values=zero, axis=1)
puzzle = np.insert(puzzle, 0, values=zero, axis=1)

b = [[0 for col in range(8)] for row in range(6)]
press = np.array(b)

#计算当前按法得到的最终状态是否符合要求，输出0即不符合，输出1即符合
def guess():
    for r in range(1,5):
        for c in range(1,7):
            press[r + 1][c] =(puzzle[r][c] + press[r][c] + press[r -1][c] + press[r][c - 1] + press[r][c + 1]) % 2
    for c in range(1,7):
        if (press[5][c - 1] + press[5][c] + press[5][c + 1] + press[4][c]) % 2 != puzzle[5][c]:
            return 0
    return 1

#调整第一行按法
def enumeration():
    #如果guess为0，则改变按法，继续循环
    while guess() == 0:
        press[1][1] += 1
        c = 1
        while press[1][c] >1:
            c += 1
            press[1][c] += 1
        continue

enumeration()
print("灯的初始状态：\n", puzzle[1:6,1:7])
print("按下结果为：\n", press[1:6,1:7])