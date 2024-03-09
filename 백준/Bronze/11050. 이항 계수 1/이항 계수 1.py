import sys

input = sys.stdin.readline

a, b = map(int, input().split())
sum1 = 1
sum2 = 1
n = 1

for i in range(a, a - b, - 1):
    sum1 *= n
    n += 1

    sum2 *= i
print(sum2 // sum1)
