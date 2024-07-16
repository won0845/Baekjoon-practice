a, b, c = map(int, input().split())
m = a*b-c
if m <= 0:
    print(0)
else:
    print(m)