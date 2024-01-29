import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# dp 배열 초기화
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열 중 최대값을 찾아 출력
print(max(dp))