import sys

input = sys.stdin.readline
coins = []

a, b = map(int, input().split())
dp = [1] + [0 for i in range(b)]

for _ in range(a):
    coins.append(int(input()))

for i in coins:
    for j in range(i,  b+1):
            dp[j] = dp[j - i] + dp[j]
print(dp[-1])