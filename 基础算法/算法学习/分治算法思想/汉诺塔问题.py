#利用分治思想解决汉诺塔问题：如果只有A柱上一个圆盘，则直接把其移动到C柱上，如果A柱圆盘大于等于2，均可视为两个圆盘，即最下面的盘和上面剩余的盘。则先把最上面的盘从A柱移动到B柱，再把下面的盘从A柱移动到C柱，最后把B柱上的盘移动到C柱
class HanoiTower(object):
    def hanoi_tower(self, num, a, b, c):
        if num == 1:#假设只有1个盘
            print('第1个盘从'+ a + '->' + c)
        else:
            self.hanoi_tower(num-1, a, c, b)
            print('第'+ str(num) + '个盘从' + a + '->' + c)
            self.hanoi_tower(num-1, b, a, c)

if __name__ == '__main__':
    t = HanoiTower()
    t.hanoi_tower(5, 'A', 'B', 'C')
