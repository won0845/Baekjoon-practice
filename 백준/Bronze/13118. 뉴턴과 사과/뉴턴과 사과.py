h = list(map(int, input().split()))
a1, b1, c1 = map(int, input().split())

if a1 in h:
    print(h.index(a1)+1)
else:
    print(0)
