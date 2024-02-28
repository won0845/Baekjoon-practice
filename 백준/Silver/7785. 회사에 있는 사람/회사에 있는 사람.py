import sys

input = sys.stdin.readline

n = int(input())
inComp = set()

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        inComp.add(name)
    elif state == "leave":
        inComp.discard(name)
remain = sorted(inComp, reverse=True)

for i in remain:
    print(i)