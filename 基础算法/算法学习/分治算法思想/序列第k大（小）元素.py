#问题描述：找出一组序列中的第k小的元素
#算法分析：随机找出一个元素作为枢纽元，将比该元素小的值放在左边，比该元素大的值放在右边，如果右半边的长度（包含枢纽元）正好等于k，则该枢纽元即第k小的元素
#如果右半边长度大于k，则继续细分右半边序列；如果右半边长度小于k，则继续细分左半边序列
def partition(seq):
    pi = seq[0] #选择第0个元素为枢纽元
    lo = [x for x in seq[1:] if x <= pi]
    hi = [x for x in seq[1:] if x > pi]
    return lo,pi,hi
def select(seq,k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi,k - m - 1)
    else:
        return select(lo,k)
if __name__ == "__main__":
    seq = [3,4,1,6,100,7,9,13,93]
    print(select(seq,3))#有第0位,所以这个答案应该为6
    print(select(seq,1))