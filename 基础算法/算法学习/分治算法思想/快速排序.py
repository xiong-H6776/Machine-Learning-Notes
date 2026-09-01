#快速排序：将某个列表的元素，按照从小到大的顺序进行排列。
#算法分析：基于分治策略，设定一个基准线，将数据与基准线对比，分成大于和小于的两个部分，通过递归，实现数据的排序
def quick_sort(n):
    if len(n) < 2:
        return n
    else:
        pivot = n[0]
        left = [x for x in n[1:] if x < pivot]
        right = [x for x in n[1:] if x > pivot]
    return quick_sort(left) + [x for x in n if x == n[0]] + quick_sort(right)
print(quick_sort([3,4,9,1,7,6,5]))