import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = []
que = deque([])
idx = 0

for i in range(n):
    lst.append(input())

for i in lst:
    mon = list(map(str, i.split()))

    if mon[0] == "push":
        que.append(mon[1])
    elif mon[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif mon[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
    elif mon[0] == "size":
        print(len(que))
    elif mon[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif mon[0] == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)