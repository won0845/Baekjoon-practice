n = input()
cnt = 0
ansCnt = 0
check = []
hap = 0
while n != "-1":
    a, b, c = n.split()
    check.append(b)
    if c =="right":
        ansCnt += 1
        cnt = check.count(b) - 1
        hap += int(a) + (cnt*20)
    n = input()
            
print(ansCnt, hap)
            
