n, a, b = map(int, input().split())

oa = 1
ob = 1

for i in range(n):
    oa += a
    ob += b
    if oa < ob:
        oa, ob = ob, oa
    elif oa == ob:
        ob -= 1
print(oa, ob)