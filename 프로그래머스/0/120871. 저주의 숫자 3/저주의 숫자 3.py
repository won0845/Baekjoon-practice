def solution(n):
    answer = 0
    dp = {1:1, 2:2}
    for i in range(3, n+1):
        tmp = dp[i - 1] + 1
        while tmp % 3 == 0 or "3" in str(tmp):
            tmp +=1
        dp[i] = tmp
    return dp[n]


# 이전 3의 개수 + 3의 배수의 개수 