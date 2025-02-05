n = int(input())

# dp 최대값은 1^2의 개수 즉 자기자신 
dp = [x for x in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        if j*j > i:
            break
        elif dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[-1])
