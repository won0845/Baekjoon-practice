import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())


def fibo(n):
    memo = {0: 0, 1: 1, 2: 1}

    if n <= 2:
        return memo[n]
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


print(fibo(N))