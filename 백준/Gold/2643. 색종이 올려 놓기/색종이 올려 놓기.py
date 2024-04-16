import sys

input = sys.stdin.readline
N = int(input())
lst = [[0,0]]
dp = [0] * (N+1)

for _ in range(N):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    lst.append([a, b])
# 내림차순
lst = sorted(lst, key=lambda x: (-x[0], -x[1]))
# 7

for i in range(1, N+1): # 1 ~ N
    for j in range(i): # 0 ~ i-1
        # dp[i]는 A[i] 보다 작은 A[j] 중 가장 큰 dp[j] 값에 1을 더한 값이다.
        if lst[i][1] <= lst[j][1]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))