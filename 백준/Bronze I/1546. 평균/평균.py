import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
maxV = max(lst)

for i in range(len(lst)):
    lst[i] = lst[i] / maxV * 100

print(sum(lst) / N)
