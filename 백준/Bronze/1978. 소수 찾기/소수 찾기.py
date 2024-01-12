a = int(input())
num = 0
b = input()
c = b.split(" ")

for i in c:  # c = 1, 3,  5 , 7
    a = int(i)
    count = 0
    for k in range(1, a + 1):
        if a % k == 0:
            count += 1
    if count == 2:
        num += 1
print(num)
