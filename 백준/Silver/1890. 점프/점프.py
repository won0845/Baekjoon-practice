import sys

input = sys.stdin.readline

N = int(input())

dp = [[0 for _ in range(N)]for _ in range(N)]
dp[0][0] = 1

board = []
count = 0
for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break

        if j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]

        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]



