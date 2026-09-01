#问题描述：一个整数序列，如果两个相邻元素的差恰好正负（负正）交替出现，称之为摇摆序列。随即给出一个序列，求其中满足摇摆序列定义的最长子序列长度
#算法设计：设置最长的摇摆子序列长度为max_length,从头到尾扫描原始序列，设置三种状态：起始、上升、下降，根据当前数字和前一个数字的比较结果进行累加max_length的计算或状态切换
class Solution(object):
    def wiggleMMaxLength(self, nums):
        if len(nums) <2:
            return len(nums)
        self.state = 0
        self.max_length = 1

        for i in range(1, len(nums)):
            if self.state == 0:
               self.begin(i, nums)
            elif self.state == 1:
               self.up(i, nums)
            elif self.state == 2:
               self.down(i, nums)
        return self.max_length
    def begin(self, i, nums):
        if nums[i -1] >nums[i]:#下降
            self.state = 2
            self.max_length += 1
        elif nums[i -1] < nums[i]:#上升
            self.state = 1
            self.max_length += 1

    def up(self, i, nums):#下降
        if nums[i-1] > nums[i]:
            self.state = 2
            self.max_length += 1

    def down(self, i, nums):
        if nums[i-1] < nums[i]:#上升
            self.state = 1
            self.max_length += 1

if __name__ == '__main__':
    s = Solution()
    g = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    result = s.wiggleMMaxLength(g)
    print(result)#输出最长摇摆序列的长度