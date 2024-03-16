import sys

input = sys.stdin.readline

cityNum = int(input())
requires = list(map(int, input().split()))
M = int(input())

start, end = 1, max(requires)

while start <= end:
    budget = 0
    mid = (start + end) // 2
    for i in requires:
        if i >= mid:
            budget += mid
        else:
            budget += i

    if budget <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)