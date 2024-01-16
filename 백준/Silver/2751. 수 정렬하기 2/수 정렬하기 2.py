import sys

input = sys.stdin.readline

n = int(input())
lst = []
buff =[None] * n

for i in range(n):
    lst.append(int(input()))


def merge_sort(a, left, right):
    if left < right:
        center = (left + right) // 2

        merge_sort(a, left, center)
        merge_sort(a, center + 1, right)

        p = j = 0
        i = k = left

        while i <= center:
            buff[p] = a[i]
            p += 1
            i += 1

        while i <= right and j < p:
            if buff[j] <= a[i]:
                a[k] = buff[j]
                j += 1
            else:
                a[k] = a[i]
                i += 1
            k += 1

        while j < p:
            a[k] = buff[j]
            k += 1
            j += 1
    return a

lst = merge_sort(lst, 0, len(lst) - 1)
for i in lst:
    print(i)