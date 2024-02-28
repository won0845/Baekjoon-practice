import sys

input = sys.stdin.readline

n = int(input())
nlist = sorted(list(map(int, input().split())))

m = int(input())
mlist = list(map(int, input().split()))

for i in mlist:
    low, high = 0, n - 1
    check = False
    while low <= high:
        mid = (low + high) // 2
        if nlist[mid] < i:
            low = mid + 1
        elif nlist[mid] > i:
            high = mid - 1
        elif nlist[mid] == i:
            check = True
            break
    print(1 if check else 0, end=" ")