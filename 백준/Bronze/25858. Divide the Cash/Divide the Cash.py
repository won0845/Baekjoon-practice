a, b = map(int,input().split())
lst = []
for i in range(a):
    lst.append(int(input()))
c = sum(lst)
d = b//c

for i in lst:
    print(i*d)