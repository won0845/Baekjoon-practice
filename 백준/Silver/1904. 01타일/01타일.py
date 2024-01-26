import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())


def tile(n):
    t = {1: 1, 2: 2}
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n + 1):
        t[i] = (t[i - 1] + t[i - 2]) % 15746
    return t[n]


print(tile(N))
