def solution(balls, share):
    answer = factorial(balls) / (factorial(balls-share) * factorial(share))
    return answer

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans