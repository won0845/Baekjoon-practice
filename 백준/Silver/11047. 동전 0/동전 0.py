import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
count = 0


for i in range(N - 1, -1, -1):
    if coins[i] <= K:
        count += K // coins[i]
        K -= coins[i] * (K // coins[i])

print(count)
