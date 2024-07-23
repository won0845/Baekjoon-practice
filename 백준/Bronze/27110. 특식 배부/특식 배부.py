n = int(input())
nlist = list(map(int, input().split()))
csum = 0
for i in nlist:
    if i < n:
        csum += i
    else:
        csum += n
        
    
print(csum)
    

