import sys
from collections import  deque
input = sys.stdin.readline

n = int(input())
deq = deque([])
for _ in range(n):
    inst = list(map(str, input().strip().split()))
    if inst[0] == "push_back":
        deq.append(inst[1])
    elif inst[0] == "push_front":
        deq.appendleft(inst[1])
    elif inst[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif inst[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
    elif inst[0] == "size":
        print(len(deq))
    elif inst[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif inst[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif inst[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())