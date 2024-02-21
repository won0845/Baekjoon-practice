import sys

input = sys.stdin.readline
div = []
N = int(input())

for i in range(1, N):
    while N % (i + 1) == 0:
        N = N // (i + 1)
        div.append(i + 1)

for j in div:
    print(j)
