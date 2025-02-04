# dp[i] = arr[i]를 마지막 원소로 하는 가장 큰 증가 부분 수열의 합

n = int(input())
arr = list(map(int, input().split()))
# 1 100 2 50 60 3 5 6 7 8
dp = arr[:]
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))



