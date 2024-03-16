import sys

input = sys.stdin.readline

n = int(input())
stk = []
count = 1
op = []
tmp = True

for i in range(n):
    num = int(input())
    while count <= num:
        stk.append(count)
        op.append("+")
        count += 1
    if num == stk[-1]:
        stk.pop()
        op.append("-")
    else:
        tmp = False

if tmp:
    for i in op:
        print(i)
else:
    print("NO")