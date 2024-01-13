n = int(input())
lst = []

for i in range(n):
    lst.append(input())

setlist = set(lst)
lst = list(setlist)

lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)