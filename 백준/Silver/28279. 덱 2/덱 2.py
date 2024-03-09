import sys
from collections import  deque
input = sys.stdin.readline

n = int(input())
deq = deque([])
for _ in range(n):
    inst = list(map(str, input().strip().split()))
    if inst[0] == "1":
        deq.appendleft(inst[1])
    elif inst[0] == "2":
        deq.append(inst[1])
    elif inst[0] == "3":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif inst[0] == "4":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif inst[0] == "5":
        print(len(deq))
    elif inst[0] == "6":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif inst[0] == "7":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif inst[0] == "8":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
