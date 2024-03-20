import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    str = input().strip()
    length = int(input())
    lst = deque(input().strip()[1:-1].split(","))
    isReversed = False
    isError = False

    if length == 0:
        lst = []

    for i in str:
        if i == "R":
            if isReversed:
                isReversed = False
            else:
                isReversed = True
        elif i == "D":
            if len(lst) != 0 and isReversed:
                lst.pop()
            elif len(lst) != 0 and not isReversed:
                lst.popleft()
            elif len(lst) == 0:
                isError = True
    if isError:
        print("error")
    else:
        if isReversed:
            print("["+",".join(reversed(lst))+"]")
        else:
            print("["+",".join(lst)+"]")