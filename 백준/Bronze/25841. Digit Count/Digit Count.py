a, b, c = map(int, input().split())
hap = 0
for i in range(a, b + 1):
    hap += str(i).count(str(c))
    
print(hap)

