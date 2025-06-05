from functools import lru_cache
from typing import List, Tuple

Item = Tuple[int, int]

def knapsack_memoization(capacity: int, items: List[Item]) -> int:
    """Top-down dynamic programming with memoization."""
    n = len(items)

    @lru_cache(maxsize=None)
    def dp(i: int, remaining: int) -> int:
        if i == n or remaining <= 0:
            return 0
        weight, value = items[i]
        skip = dp(i + 1, remaining)
        take = 0
        if weight <= remaining:
            take = value + dp(i + 1, remaining - weight)
        return max(take, skip)

    return dp(0, capacity)

if __name__ == "__main__":
    sample_items = [(2, 3), (1, 2), (3, 4), (2, 2)]
    cap = 5
    print(knapsack_memoization(cap, sample_items))
