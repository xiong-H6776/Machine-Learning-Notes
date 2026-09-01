# -*- coding: utf-8 -*-
"""
Prim 算法（普里姆算法）
用途：求无向带权图的最小生成树

核心思想：
1. 从任意一个顶点开始，将它加入 MST
2. 重复以下步骤，直到所有顶点都加入 MST：
   a. 找出连接"已在 MST 中的顶点"和"不在 MST 中的顶点"的边中权重最小的
   b. 把那个新顶点和这条边加入 MST

与 Kruskal 的区别：
  Kruskal 选全局最小边（用并查集判环）
  Prim   从已选顶点向外生长（用优先级队列找最小边）
"""

import heapq


def prim(n, edges):
    """
    Prim 算法主函数

    :param n:     顶点数量（顶点编号 0 ~ n-1）
    :param edges: 边列表，每个元素为 (权重, 顶点A, 顶点B)
    :return:      (选中的边列表, 总权重)
    """
    # 构建邻接表：adj[u] = [(w, v), ...] 表示 u -- v 权重为 w
    adj = [[] for _ in range(n)]
    for w, a, b in edges:
        adj[a].append((w, b))
        adj[b].append((w, a))

    visited = [False] * n      # 是否已加入 MST
    pq = []                    # 最小堆：(权重, 顶点, 来自哪个顶点)
    mst = []                   # 选中的边
    total_weight = 0

    # 从顶点 0 开始
    visited[0] = True
    for w, v in adj[0]:
        heapq.heappush(pq, (w, v, 0))

    print(f"从顶点 0 出发，将它的邻接边加入候选堆")
    print(f"{'当前边':>12}  {'操作':>8}")
    print("-" * 24)

    while pq and len(mst) < n - 1:
        w, v, u = heapq.heappop(pq)
        if visited[v]:
            # 这个顶点已经连通了，跳过
            continue

        # 选中这条边
        visited[v] = True
        mst.append((w, u, v))
        total_weight += w
        print(f"  ({u} -- {v}) w={w}   [+] 选中")

        # 将新顶点的邻接边加入候选堆
        for w2, v2 in adj[v]:
            if not visited[v2]:
                heapq.heappush(pq, (w2, v2, v))
                print(f"  ... → 候选 ({v} -- {v2}) w={w2}")

    return mst, total_weight


def main():
    print("=" * 50)
    print("Prim 算法 - 最小生成树")
    print("=" * 50)

    # 与 Kruskal 示例完全相同的图，方便对比结果
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

    mst, total = prim(n, edges)

    print()
    print("=" * 50)
    print("【Prim 最小生成树结果】")
    print("选中的边：")
    for w, a, b in mst:
        print(f"  ({a} -- {b})  权重={w}")
    print(f"总权重：{total}")
    print()

    print("=" * 50)


if __name__ == "__main__":
    main()
