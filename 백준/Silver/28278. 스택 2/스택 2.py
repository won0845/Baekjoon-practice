import sys
input= sys.stdin.readline

n = int(input())
stk = []
for _ in range(n):
    a = input().split()
    b = int(a[0])
    if b == 1:
        stk.append(int(a[1]))
    elif b == 2:
        if not stk:
            print(-1)
        else:
            print(stk.pop())
    elif b == 3:
        print(len(stk))
    elif b == 4:
        if not stk:
            print(1)
        else:
            print(0)
    elif b == 5:
        if not stk:
            print(-1)
        else:
            print(stk[-1])
