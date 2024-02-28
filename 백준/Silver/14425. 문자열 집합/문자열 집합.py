import sys

input = sys.stdin.readline
S = []
check = []
cnt = 0

n, m = map(int, input().split())
for _ in range(n):
    S.append(input())
for _ in range(m):
    check.append(input())
S = set(S)

for i in check:
    if i in S:
        cnt += 1
print(cnt)