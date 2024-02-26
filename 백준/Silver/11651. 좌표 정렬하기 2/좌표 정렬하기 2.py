import sys

input = sys.stdin.readline

num = int(input())
dot = []

for _ in range(num):
    a, b = map(int, input().split())
    dot.append([a, b])

dot.sort(key=lambda x: (x[1], x[0]))

for i in range(num):
    print(dot[i][0], dot[i][1])
