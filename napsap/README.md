# Napsap Coding Test

This directory contains a simple coding test around the **napsap** problem (a variant of the classic knapsack problem).

## Problem Statement

Given a list of items where each item has a weight and a value, and given a maximum capacity, determine the maximum total value of items that can be placed into the napsap without exceeding the capacity.

### Input
- `capacity`: positive integer specifying the maximum weight the napsap can hold.
- `items`: list of `(weight, value)` pairs.

### Output
- Maximum value achievable within the given capacity.

## Solutions
Three example solutions are provided:
1. **Brute force** (`solution_bruteforce.py`)
2. **Dynamic programming with memoization** (`solution_memoization.py`)
3. **Bottom-up dynamic programming** (`solution_bottomup.py`)

Run any script with Python 3 to see it in action.
