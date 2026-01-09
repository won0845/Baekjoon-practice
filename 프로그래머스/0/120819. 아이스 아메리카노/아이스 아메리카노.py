def solution(money):
    
    cup = money // 5500
    remain = money % 5500
    
    answer = [cup, remain]
    return answer