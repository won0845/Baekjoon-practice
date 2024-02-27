import sys

input = sys.stdin.readline

a = list(map(int, input().split()))

a.sort()
if a[0] + a[1] > a[2]:
    print(sum(a))
else:
    print(a[0] + a[1] + (a[0] + a[1] - 1))