import sys
input = sys.stdin.readline


n1, n2 = map(int, input().split())

while n1 != 0 or n2 != 0:
    if n1 > n2:
        if n1 % n2 == 0:
            print("multiple")
        else:
            print("neither")
    else:
        if n2 % n1 == 0:
            print("factor")
        else:
            print("neither")
    n1, n2 = map(int, input().split())

