n = int(input())
card = list(map(int, input().split()))
card.insert(0,0)
dp = card.copy()

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i],dp[j]+dp[i-j])
        
print(dp[-1])

