N, M = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 1, max(lst)

while start <= end:
    sum1 = 0
    mid = (start + end) // 2

    for i in lst:
        if i > mid:
            sum1 += i - mid

    if sum1 < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)