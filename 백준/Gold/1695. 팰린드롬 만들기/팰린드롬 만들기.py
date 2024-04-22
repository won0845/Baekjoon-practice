n = int(input())
lst = list(map(int, input().split()))
lst2 = list(reversed(lst))
dp = [[0 for _ in range(len(lst2)+1)] for _ in range(len(lst)+1)]

for i in range(1, len(lst)+1):
    for j in range(1, len(lst2)+1):
        if lst[i-1] == lst2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(len(lst)-dp[-1][-1])