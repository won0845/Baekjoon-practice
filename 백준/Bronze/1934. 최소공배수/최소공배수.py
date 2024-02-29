import math

# 두 수의 최소 공배수를 계산하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 입력 받기
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))