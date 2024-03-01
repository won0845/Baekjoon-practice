import sys


def sosu(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


input = sys.stdin.readline
n = int(input())
so = 0

for _ in range(n):
    a = int(input())
    while not sosu(a):
        a += 1
    print(a)
