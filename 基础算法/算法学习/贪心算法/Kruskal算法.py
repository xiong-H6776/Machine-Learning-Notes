# -*- coding: utf-8 -*-
"""
Kruskal 算法（克鲁斯卡尔算法）
用途：求无向带权图的最小生成树

核心思想：
1. 将所有边按权重从小到大排序
2. 依次取出权重最小的边
3. 如果这条边连接的两个顶点尚未连通，则选中这条边
4. 重复直到选够 N-1 条边（N 为顶点数）

配套数据结构：并查集（Union-Find），用于快速判断是否形成环
"""


class UnionFind:
    """并查集：用于高效检测环"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # 按秩合并
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskal(n, edges):
    """
    Kruskal 算法主函数

    :param n:     顶点数量（顶点编号 0 ~ n-1）
    :param edges: 边列表，每个元素为 (权重, 顶点A, 顶点B)
    :return:      (选中的边列表, 总权重)
    """
    # 按权重从小到大排序
    edges_sorted = sorted(edges, key=lambda e: e[0])
    uf = UnionFind(n)
    mst = []          # 选中的边
    total_weight = 0  # 总权重

    print("按权重排序后的所有边：")
    print(f"{'权重':>6}  {'顶点A':>6}  {'顶点B':>6}")
    print("-" * 24)
    for w, a, b in edges_sorted:
        print(f"{w:>6}  {a:>6}  {b:>6}")

    print("\n开始贪心选择（优先选权重最小的边）：")
    for w, a, b in edges_sorted:
        if uf.union(a, b):
            mst.append((w, a, b))
            total_weight += w
            print(f"  [+] 选中边 ({a} -- {b})  权重={w}，当前总权重={total_weight}")
        else:
            print(f"  [-] 跳过边 ({a} -- {b})  权重={w}（会形成环）")

    return mst, total_weight


def main():
    print("=" * 50)
    print("Kruskal 算法 - 最小生成树")
    print("=" * 50)

    # 示例：6 个顶点（0~5），10 条边
    # 这是一个带权无向图
    n = 6
    edges = [
        (6, 0, 1),
        (1, 0, 2),
        (5, 0, 3),
        (3, 1, 2),
        (5, 1, 4),
        (6, 2, 3),
        (4, 2, 5),
        (2, 3, 5),
        (6, 4, 5),
        (3, 4, 2),
    ]

    print(f"顶点数量：{n}")
    print(f"边  数量：{len(edges)}")
    print()
    print("原始边列表：")
    print(f"{'权重':>6}  {'顶点A':>6}  {'顶点B':>6}")
    print("-" * 24)
    for w, a, b in edges:
        print(f"{w:>6}  {a:>6}  {b:>6}")

    print()
    mst, total = kruskal(n, edges)

    print()
    print("=" * 50)
    print("【最小生成树结果】")
    print("选中的边：")
    for w, a, b in mst:
        print(f"  ({a} -- {b})  权重={w}")
    print(f"总权重：{total}")
    print("=" * 50)


if __name__ == "__main__":
    main()
