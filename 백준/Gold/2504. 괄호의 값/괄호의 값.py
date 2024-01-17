import sys
input = sys.stdin.readline

n = input()
lst = []
total = 0
temp = 1

for i in range(len(n)):
    if n[i] == "(":
        lst.append(n[i])
        temp *= 2

    elif n[i] == "[":
        lst.append(n[i])
        temp *= 3

    elif n[i] == ")":
        if not lst or lst[-1] == "[":
            print(0)
            break
        if n[i-1] == "(":
            total += temp
        lst.pop()
        temp //= 2

    elif n[i] == "]":
        if not lst or lst[-1] == "(":
            print(0)
            break
        if n[i - 1] == "[":
            total += temp
        lst.pop()
        temp //= 3
else:
    if lst:
        print(0)
    else:
        print(total)
