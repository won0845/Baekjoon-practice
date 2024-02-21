import sys

input = sys.stdin.readline

A, B = map(int, input().split())
div = []

for i in range(1, A + 1):
    if A % i == 0:
        div.append(i)

if len(div) < B:
    print(0)
else:
    print(div[B - 1])
