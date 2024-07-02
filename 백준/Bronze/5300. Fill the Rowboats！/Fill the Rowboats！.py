n = int(input())
for i in range(1, n + 1):
    print(i, end=" ")
    if i % 6 == 0:
        print("Go!", end=" ")
if n % 6 != 0:
    print("Go!")
