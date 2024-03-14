import sys

input = sys.stdin.readline

n = input().rstrip()
while n != ".":
    stk = []
    balanced = True
    for i in n:
        if i == "(" or i == "[":
            stk.append(i)
        elif i == ")":
            if not stk or stk[-1] != "(":
                balanced = False
                break
            stk.pop()
        elif i == "]":
            if not stk or stk[-1] != "[":
                balanced = False
                break
            stk.pop()

    if stk or not balanced:
        print("no")
    else:
        print("yes")
    n = input().rstrip()