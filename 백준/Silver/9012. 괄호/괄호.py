n = int(input())

for _ in range(n):
    parentheses = input()
    stack = []

    for p in parentheses:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:  # for-else 구문 사용
        if stack:
            print("NO")
        else:
            print("YES")