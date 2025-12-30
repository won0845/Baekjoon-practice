def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer= numer1 * denom2 + numer2 * denom1

    g = gcd(numer, denom)    
    answer = [numer//g, denom//g]
    return answer


def gcd(a, b):
    a, b = (a, b) if a > b else (b, a)
    while b:
        a, b = b, a % b
    return a
