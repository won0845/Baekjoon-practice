def solution(a, b):
    answer = 0
    
    b //= gcd(a, b)
    
    for i in (2, 5):
        while b % i == 0:
            b //= i
    if b == 1:
        return 1
    else: 
        return 2


def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a