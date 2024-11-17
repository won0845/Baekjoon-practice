a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

hap = 0

for i in range(3):
    cha = a2[i] - a1[i]
    if  cha > 0:
        hap += cha
        
print(hap)
        
        


