import sys

input = sys.stdin.readline

check = set()
answer =[]

a, b = map(int, input().split())
for _ in range(a):
    check.add(input().strip())

for _ in range(b):
    k = input().strip()

    if k in check:
        answer.append(k)
answer.sort()
print(len(answer))
print(*answer)