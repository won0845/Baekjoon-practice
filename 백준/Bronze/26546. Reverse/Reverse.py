n = int(input())

for i in range(n):
    a, b, c = input().split()
    for i in range(len(a)):
        if i >= int(b) and i < int(c):
            continue
        else:
            print(a[i], end="")
    print()
    