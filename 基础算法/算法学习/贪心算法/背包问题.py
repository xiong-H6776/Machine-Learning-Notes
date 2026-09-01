"""
背包问题 - 最小重量贪心策略

问题描述：
背包容量 W = 150
七件物品（不可分割），编号 1-7
重量 w = [35, 30, 60, 50, 40, 10, 25]
价值 p = [10, 40, 30, 50, 35, 40, 30]

目标：在总重量不超过 W 的前提下，使装入背包的总价值最高
策略：每次选择当前剩余物品中重量最小的物品尝试装入
"""


def knapsack_min_weight(capacity, weights, values):
    """
    使用最小重量贪心策略解决 0/1 背包问题

    :param capacity: 背包容量
    :param weights: 各物品重量列表
    :param values:  各物品价值列表
    :return: (选中物品索引列表, 总重量, 总价值)
    """
    n = len(weights)
    # 创建物品列表：每个元素为 (编号, 重量, 价值)
    items = [(i + 1, weights[i], values[i]) for i in range(n)]

    # 按重量从小到大排序（最小重量贪心策略）
    items.sort(key=lambda x: x[1])

    selected = []
    total_weight = 0
    total_value = 0

    print("物品按重量排序后的顺序：")
    print(f"{'编号':>4} {'重量':>6} {'价值':>6}")
    print("-" * 20)
    for idx, w, v in items:
        print(f"{idx:>4} {w:>6} {v:>6}")

    print()
    print("开始贪心选择（优先选最轻的）：")
    for idx, w, v in items:
        if total_weight + w <= capacity:
            selected.append(idx)
            total_weight += w
            total_value += v
            print(f"  选中物品 {idx}：重量={w}，价值={v}，当前总重量={total_weight}，当前总价值={total_value}")
        else:
            print(f"  跳过物品 {idx}：重量={w}，装入后总重量={total_weight + w} > 容量 {capacity}")

    return selected, total_weight, total_value


def brute_force_knapsack(capacity, weights, values):
    """
    穷举法求解 0/1 背包问题（用于对比验证最优解）
    """
    n = len(weights)
    best_value = 0
    best_selection = None
    best_weight = 0

    for mask in range(1 << n):
        total_w = 0
        total_v = 0
        for i in range(n):
            if mask & (1 << i):
                total_w += weights[i]
                total_v += values[i]
        if total_w <= capacity and total_v > best_value:
            best_value = total_v
            best_selection = mask
            best_weight = total_w

    selected = [i + 1 for i in range(n) if best_selection & (1 << i)]
    return selected, best_weight, best_value


def main():
    # 背包容量
    W = 150

    # 七件物品的重量和价值
    weights = [35, 30, 60, 50, 40, 10, 25]
    values = [10, 40, 30, 50, 35, 40, 30]

    print("=" * 50)
    print("背包问题 - 最小重量贪心策略")
    print("=" * 50)
    print(f"背包容量：W = {W}")
    print(f"物品数量：{len(weights)} 件")
    print()
    print("物品列表：")
    print(f"{'编号':>4} {'重量':>6} {'价值':>6}")
    print("-" * 20)
    for i in range(len(weights)):
        print(f"{i + 1:>4} {weights[i]:>6} {values[i]:>6}")
    print()

    # 贪心法求解
    selected, total_weight, total_value = knapsack_min_weight(W, weights, values)

    print()
    print("=" * 50)
    print("【最小重量贪心策略结果】")
    print(f"选中物品：{selected}")
    print(f"总重量：{total_weight}")
    print(f"总价值：{total_value}")
    print("=" * 50)

    # 穷举法求解最优解（用于对比）
    opt_selected, opt_weight, opt_value = brute_force_knapsack(W, weights, values)

    print()
    print("【穷举法最优解（用于对比）】")
    print(f"选中物品：{opt_selected}")
    print(f"总重量：{opt_weight}")
    print(f"总价值：{opt_value}")

    if total_value == opt_value:
        print("\n结论：最小重量贪心策略在此案例中得到了最优解 🎉")
    else:
        print(f"\n结论：最小重量贪心策略未得到最优解，差值为 {opt_value - total_value}")

    print("=" * 50)


if __name__ == "__main__":
    main()
