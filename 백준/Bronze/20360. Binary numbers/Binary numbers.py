n = int(input())
lst= []
while n >= 1:
    a = n % 2
    lst.append(a)
    n //= 2

for i in range(len(lst)):
    if lst[i] == 1:
        print(i, end=" ")
        