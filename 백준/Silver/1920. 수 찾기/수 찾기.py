N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return print(0)
    mid = (start + end) // 2
    if array[mid] == target:
        return print(1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)


A.sort()
for i in B:
    binary_search(A, i, 0, len(A) - 1)