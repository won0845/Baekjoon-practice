import math
def solution(price):
    discount = 0
    
    if price >= 50 * 10000:
        discount = 0.2
    elif price >= 30 * 10000:
        discount = 0.1
    elif price >= 10 * 10000:
        discount = 0.05
    
    
    answer = (1 - discount) * price
    return math.trunc(answer)