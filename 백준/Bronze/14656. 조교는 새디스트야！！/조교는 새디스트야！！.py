n = int(input())
lst = list(map(int, input().split()))
hap = 0

for i in range(n):
    if i+1 == lst[i]:
        continue
    else:
        hap+=1
print(hap)
    
    