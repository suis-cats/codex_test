from typing import List, Tuple

Item = Tuple[int, int]  # (weight, value)

def knapsack_bruteforce(capacity: int, items: List[Item]) -> int:
    """Brute force solution exploring all subsets."""
    n = len(items)
    best = 0
    for mask in range(1 << n):
        total_w = 0
        total_v = 0
        for i in range(n):
            if mask & (1 << i):
                w, v = items[i]
                total_w += w
                total_v += v
        if total_w <= capacity and total_v > best:
            best = total_v
    return best

if __name__ == "__main__":
    sample_items = [(2, 3), (1, 2), (3, 4), (2, 2)]
    cap = 5
    print(knapsack_bruteforce(cap, sample_items))
