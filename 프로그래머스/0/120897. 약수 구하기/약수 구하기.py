def solution(n):
    answer = []
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                answer.append(i)
            else:
                answer.extend([i, n // i])
    answer.sort()
    
    return answer