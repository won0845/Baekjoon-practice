n = list(map(int, input().split()))
hap = 0
for i in n:
    if i == 1:
        hap+=500
    elif i == 2:
        hap+=800
    else:
        hap+=1000
print(5000-hap)