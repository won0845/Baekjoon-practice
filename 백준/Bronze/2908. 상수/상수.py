A, B = input().split()
a = list(A)
b = list(B)
a.reverse()
b.reverse()
a = ''.join(a)
b = ''.join(b)

if int(a) > int(b):
    print(a)
else:
    print(b)