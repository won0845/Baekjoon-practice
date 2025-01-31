n = int(input())
dp = [0 for i in range(n+1)]

lst = list(map(int, input().split()))
dp[0] = float('-inf')
lst.insert(0,0)

for i in range(1, n+1):
    dp[i] = max(dp[i-1] + lst[i], lst[i])

print(max(dp))
    