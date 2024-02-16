import sys

input = sys.stdin.readline

lst = [] * 10

for _ in range(10):
    a = int(input())
    lst.append(a % 42)
lst = set(lst)
print(len(lst))
