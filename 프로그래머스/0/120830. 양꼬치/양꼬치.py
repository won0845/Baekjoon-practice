def solution(n, k):
    
    service_beverage = n // 10
    
    answer = n * 12000 + (k - service_beverage) * 2000
    return answer