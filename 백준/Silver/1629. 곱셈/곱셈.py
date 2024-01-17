import sys

A, B, C = map(int, sys.stdin.readline().split())


def cal(a, b, c):
    if b == 1:
        return a % c
    elif b == 0:
        return 1
    else:
        tmp = cal(a, b // 2, c)
        if b % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c


print(cal(A, B, C))