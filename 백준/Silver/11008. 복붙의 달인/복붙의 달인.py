n = int(input())

for i in range(n):
    a, b = map(str, input().split())
    a = a.replace(b, "a")
    print(len(a))