import sys

input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))
maxNum = 0
count = 0

for _ in range(len(lst)):
    a = lst.pop()
    if a <= maxNum:
        continue
    else:
        maxNum = a
        count += 1
print(count)