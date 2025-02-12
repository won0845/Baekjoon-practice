n = int(input())

dp = [1 for i in range(n+1)]
dp[1] = 3
for i in range(2, n+1):
    dp[i] = (dp[i-2]+(dp[i-1]*2)) % 9901
    
print(dp[-1])
    