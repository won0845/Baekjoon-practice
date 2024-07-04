lst = []
for i in range(5):
    lst.append(input())
lstset = set(lst)
for i in lstset:
    if lst.count(i)% 2 != 0:
        print(i)
    
    