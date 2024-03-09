import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    sum1 = 1
    sum2 = 1
    n = 1

    for i in range(b, b - a, - 1):
        sum1 *= n
        n += 1
        sum2 *= i
    print(sum2 // sum1)
