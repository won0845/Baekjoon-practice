hap = 0
n = int(input())
for i in range(n):
    l = input()
    if "01" in l or "OI" in l:
        hap+=1
print(hap)