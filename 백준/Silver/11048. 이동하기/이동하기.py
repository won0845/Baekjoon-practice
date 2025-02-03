n, m = map(int, input().split())
candy = []
dp = [[0 for i in range(m+1)]for j in range(n+1)]

for i in range(n):
    candy.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i+1][j+1] = dp[i+1][j] + candy[i][j]    
        elif j == 0:
            dp[i+1][j+1] = dp[i][j+1] + candy[i][j]
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j],dp[i][j])+candy[i][j]

print(dp[-1][-1])

# +1 해놓고 다른 dp 에서는 +1을 안해준 문제떄문에 오류가 발생했었음 ,.., ㅇ