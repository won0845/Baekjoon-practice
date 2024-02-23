import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(input().split())
maxV = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            temp = int(lst[i]) + int(lst[j]) + int(lst[k])
            if temp <= m and temp > maxV:
                maxV = temp

print(maxV)