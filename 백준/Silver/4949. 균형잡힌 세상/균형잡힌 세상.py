import sys

input = sys.stdin.readline

n = input().rstrip()
while n != ".":
    stk = []
    check = True
    for i in n:
        if i == "(" or i == "[":
            stk.append(i)
        elif i == ")" or i == "]":
            if not stk or (i == ")" and stk[-1] != "(") or (i == "]" and stk[-1] != "["):
                check = False
                break
            stk.pop()

    if stk or not check:
        print("no")
    else:
        print("yes")
    n = input().rstrip()