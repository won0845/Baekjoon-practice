import sys

input = sys.stdin.readline

string_a = input().strip()
string_b = input().strip()

dp = [[0 for _ in range(1001)] for _ in range(1001)]
for i in range(1, len(string_a) + 1):
    for j in range(1, len(string_b) + 1):
        if string_a[i - 1] == string_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[len(string_a)][len(string_b)])
