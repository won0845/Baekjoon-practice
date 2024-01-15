n = int(input())

lst = []

for i in range(n):
    lst.append(input())

for i in lst:
    count = 0
    sum1 = 0
    for value in i:
        if value == "O":
            count += 1
            sum1 += count
        else:
            count = 0

    print(sum1)
