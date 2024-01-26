import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
memo = []


def fibonaci(n):
    fibo = {0: 0, 1: 1, 2: 1}
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo[n]


print(fibonaci(n))
