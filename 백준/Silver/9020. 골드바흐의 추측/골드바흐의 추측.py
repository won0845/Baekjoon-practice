import sys


def prime(num):
    if num <= 1:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


a = int(sys.stdin.readline())
lst = []
for i in range(a):
    lst.append(int(sys.stdin.readline()))

for l in lst:
    n = l // 2
    for k in range(n):
        if prime(n) and prime(l - n):
            print(n, l - n)
            break
        else:
            n = n - 1