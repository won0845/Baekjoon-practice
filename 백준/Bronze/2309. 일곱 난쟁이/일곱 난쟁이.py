import sys

input = sys.stdin.readline
lst = []

for i in range(9):
    lst.append(int(input()))

total = sum(lst)

for i in range(9):
    for j in range(i + 1, 9):
        if total - lst[i] - lst[j] == 100:
            a = lst[i]
            b = lst[j]

lst.remove(a)
lst.remove(b)
lst.sort()
for i in lst:
    print(i)
