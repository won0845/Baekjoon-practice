n = int(input())
lst = list(map(int, input().split()))
hap = 0

tmp = lst[0]
hap += tmp

for i in range(1, n):
    if tmp + 1 == lst[i]:
        tmp = lst[i]
        continue
    else:
        tmp = lst[i]
        hap += tmp
print(hap)
        