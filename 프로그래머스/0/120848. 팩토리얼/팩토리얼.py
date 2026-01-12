def solution(n):
    max_n = 0
    result = 0
    i = 1
    
    while True:
        result = factorial(i) 
        if  result <= n:
            max_n = i
            i += 1
            continue
        else:
            break    
    answer = max_n
    return answer

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac