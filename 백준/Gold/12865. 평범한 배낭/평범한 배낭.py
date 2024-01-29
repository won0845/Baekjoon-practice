import sys

input = sys.stdin.readline

N, K = map(int, input().split())

item = []
for _ in range(N):
    item.append(list(map(int, input().split())))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if item[i-1][0] <= j:
            dp[i][j] = max(item[i-1][1] + dp[i - 1][j - item[i-1][0]], dp[i - 1][
                j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])