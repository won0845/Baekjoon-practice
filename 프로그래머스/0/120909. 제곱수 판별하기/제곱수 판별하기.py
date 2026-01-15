def solution(n):
    answer = 2
    
    if int(n ** 0.5) ** 2 == n:
        answer = 1
    return answer