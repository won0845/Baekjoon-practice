string = input()

for i in string:
    hap = 0
    for j in str(ord(i)):
        hap += int(j)
    print(i*hap)
        