dp = [1,2,4,7]

for _ in range(int(input())):#0,1,2,3
    n = int(input())
    for i in range(len(dp), n):
        dp.append((dp[i-3] + dp[i-2] + dp[i-1])%1000000009)
    print(dp[n-1])
    