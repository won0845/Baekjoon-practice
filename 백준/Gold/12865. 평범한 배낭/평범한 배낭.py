import sys

input = sys.stdin.readline

item = [[0, 0]]
N, K = map(int, input().split())
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    A, B = map(int, input().split())
    item.append([A, B])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j < item[i][0]:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(item[i][1] + knapsack[i - 1][j - item[i][0]], knapsack[i - 1][j])

print(knapsack[N][K])
