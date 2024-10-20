n = int(input())
hap = 0
for i in range(n):
    a = int(input().split("-")[1])
    if a <= 90:
        hap +=1
print(hap)