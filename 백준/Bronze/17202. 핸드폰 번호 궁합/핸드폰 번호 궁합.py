a = list(map(int, input()))
b = list(map(int, input()))

case = []

for i in range(len(a)):
    case.append(a[i])
    case.append(b[i])

while len(case) > 2:
    j = 1
    hap = []
    while j < len(case):
        fir = (case[j-1]+case[j]) % 10
        hap.append(fir)
        j+=1
    case = hap

for i in case:
    print(i,end="")