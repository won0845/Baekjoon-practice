N, X = input().split()
lst = []
lstmin = []
lst = input().split()

for i in lst:
    if int(i) < int(X):
        lstmin.append(i)

for i in lstmin:
    print(i, end=" ")