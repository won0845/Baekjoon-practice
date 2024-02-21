a =[]
for _ in range(3):
    a.append(int(input()))

if sum(a) == 180:
    if a[0] == a[1] == a[2]:
        print("Equilateral")
    elif (a[0] == a[1] and a[0] != a[2]) or (a[0] == a[2] and a[0] != a[1]) or (a[1] == a[2] and a[1] != a[0]): 
        print("Isosceles")
    if a[0] != a[1] and a[0] !=a[2] and a[1] != a[2]:
        print("Scalene")
else:
    print("Error")