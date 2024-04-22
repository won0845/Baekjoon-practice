lst1 = input().rstrip()
lst2 = input().rstrip()
lst3 = input().rstrip()

dp = [[[0] * (len(lst3) + 1) for _ in range(len(lst2) + 1)] for _ in range(len(lst1) + 1)]
for i in range(1, len(lst1) + 1):
    for j in range(1, len(lst2) + 1):
        for l in range(1, len(lst3) + 1):
            if lst1[i - 1] == lst2[j - 1] == lst3[l - 1]:
                dp[i][j][l] = dp[i - 1][j - 1][l - 1] + 1
            else:
                dp[i][j][l] = max(dp[i - 1][j][l], dp[i][j - 1][l],dp[i][j][l-1])

print(dp[-1][-1][-1])
