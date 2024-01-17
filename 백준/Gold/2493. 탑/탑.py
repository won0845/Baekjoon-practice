import sys

input = sys.stdin.readline
n = int(input())

lst = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] > lst[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, lst[i]])
print(" ".join(map(str, answer)))