import sys
import math

input = sys.stdin.readline

n = int(input())
if n != 0:
    lst = []
    sum1 = 0

    for _ in range(n):
        lst.append(int(input()))

    mus = math.floor((n * 0.15 + 0.5))

    lst = sorted(lst)

    for i in range(mus, len(lst) - mus):
        sum1 += lst[i]

    print(math.floor((sum1 / (len(lst) - (mus * 2))) + 0.5))
else:
    print(0)