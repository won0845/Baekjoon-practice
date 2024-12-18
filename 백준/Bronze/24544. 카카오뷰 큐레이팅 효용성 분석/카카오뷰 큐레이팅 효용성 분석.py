n = int(input())
hap = 0
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(n):
    if lst2[i] == 0:
        hap += lst1[i]

print(sum(lst1))
print(hap)
