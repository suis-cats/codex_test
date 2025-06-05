from typing import List, Tuple

Item = Tuple[int, int]

def knapsack_bottomup(capacity: int, items: List[Item]) -> int:
    """Bottom-up dynamic programming solution."""
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

if __name__ == "__main__":
    sample_items = [(2, 3), (1, 2), (3, 4), (2, 2)]
    cap = 5
    print(knapsack_bottomup(cap, sample_items))
