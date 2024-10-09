n = int(input())

for i in range(n):
    a = int(input())
    m = a // 5
    r = a % 5
    print("++++ " * m + "|"* r)