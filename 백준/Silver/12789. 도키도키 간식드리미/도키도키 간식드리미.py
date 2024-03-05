import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque(list(map(int, input().split())))
stk = []
current = 1

while q:
    if q[0] == current:
        q.popleft()
        current += 1
    elif stk and stk[-1] == current:
        stk.pop()
        current += 1
    else:
        stk.append(q.popleft())

while stk:
    k = stk.pop()
    if k == current:
        current += 1

if current - 1 == n:
    print("Nice")
else:
    print("Sad")