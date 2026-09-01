#归并排序：将待排序数据分为两个部分，继续将两个子部分进行递归的归并排序，直到所有子部分仅有一个元素，然后将已经有序的子部分合并，最后完成排序
def mergesort(seq):
    mid = len(seq)//2
    if len(seq)<=1:
        return seq
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    res = []
    while left and right:
        if left[-1] >= right[-1]:#-1指最后一个元素
            res.append(left.pop())#pop()：按下标删除列表中指定的元素并原地修改原列表，返回值为被删除的元素
        else:
            res.append(right.pop())
    res.reverse()#reverse()：直接将原列表反转，[1，2，3]变为[3，2，1]，不返回新列表
    return left + right + res
print(mergesort([1,6,13,3,8]))