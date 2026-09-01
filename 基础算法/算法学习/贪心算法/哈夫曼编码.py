#哈夫曼编码广泛用于数据压缩中，其根据文中不同字符出现的频率，对于出现频率高得字符采用较短的编码，对于出现频率低的字符，采用较长的编码，实现没有歧义的前提下，有效率的数据压缩
#比如112222233444455555，其中1和3出现2次，4出现4次，2和5出现5次，就可以采用00表示5，01表示2，110表示4，1010表示1，1011表示3（由于哈夫曼编码是不等长的，所以要求各个编码之间，不会吹西安某个编码是另一个编码前缀的情况）
#接下来给出一个算法，解决对于一个给出的字段，以哈夫曼树的形式给出用于编码参考的输出。
from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb , _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a,b]))
    return trees[0][-1]

seq = "abcdefghi"
frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
print(huffman(seq, frq))