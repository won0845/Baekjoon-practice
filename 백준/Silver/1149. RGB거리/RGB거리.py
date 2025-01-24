n = int(input())
dp = [[0,0,0] for _ in range(n)]
color = []
for _ in range(n):
    a, b, c = map(int, input().split())
    color.append([a,b,c])
dp[0] = color[0]

for i in range(n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+color[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+color[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0])+color[i][2]
    
print(min(dp[n-1]))


