big = ""
value = 0
for i in range(7):
    a, b = input().split()
    if int(b) > int(value):
        value = int(b)
        big = a      

print(big)