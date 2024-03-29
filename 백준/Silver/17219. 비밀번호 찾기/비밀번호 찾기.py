import sys
input = sys.stdin.readline
inf = {}
a, b = map(int, input().split())

for _ in range(a):
    i, p = map(str, input().split())
    inf[i] = p
for j in range(b):
    a = input().rstrip()
    print(inf[a])