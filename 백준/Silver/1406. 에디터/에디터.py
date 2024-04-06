import sys

input = sys.stdin.readline

stk1 = list(map(str, input().rstrip()))
stk2 = []

n = int(input())

for i in range(n):
    a = list(map(str, input().split()))
    if a[0] == "P":
        stk1.append(a[1])
    elif a[0] == "L":
        if stk1:
            v = stk1.pop()
            stk2.append(v)
        else:
            continue
    elif a[0] == "D":
        if stk2:
            k = stk2.pop()
            stk1.append(k)
        else:
            continue
    elif a[0] == "B":
        if stk1:
            l = stk1.pop()
        else:
            continue
stk1.extend((reversed(stk2)))
for i in stk1:
    print(i, end="")