import sys

input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))
sum = 0

for i in range(1, len(lst)):
    lst[i] = lst[i] + lst[i - 1]
    sum += lst[i]
print(sum + lst[0])