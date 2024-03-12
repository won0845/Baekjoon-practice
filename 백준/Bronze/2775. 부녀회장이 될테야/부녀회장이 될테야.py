import sys
input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    k = int(input())
    n = int(input())
    dp = [[i for i in range(1, n + 1)]] + [[1 for _ in range(n)]for _ in range(k)]

    for z in range(1, k+1):
        for x in range(1, n):
            dp[z][x] = dp[z][x-1] + dp[z-1][x]
    print(dp[k][n-1])