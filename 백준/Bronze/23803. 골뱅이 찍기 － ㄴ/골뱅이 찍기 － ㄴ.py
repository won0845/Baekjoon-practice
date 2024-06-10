import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n * 5 + 1):
    if i <= 4 * n:
        print("@" * n)
    else:
        print("@" * n * 5)
