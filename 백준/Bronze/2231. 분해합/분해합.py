n = int(input())
minv = 0  

start = max(n - 9 * len(str(n)), 0)

for i in range(start, n):
    temp = list(map(int, str(i)))
    hap = i + sum(temp)
    if hap == n:
        minv = i  
        break
        
print(minv)