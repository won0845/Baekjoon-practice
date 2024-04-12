n = int(input())
for i in range(0, n):
    print(i * " " + ((2 * (n - i)) - 1) * "*")
for i in range(1, n):
    print((n - i - 1) * " " + (2 * i + 1) * "*")