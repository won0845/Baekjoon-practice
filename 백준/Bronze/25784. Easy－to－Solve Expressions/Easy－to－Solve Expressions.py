lst = list(map(int,input().split()))

lst.sort()
if lst[0] + lst[1] == lst[2]:
    print("1")
elif lst[0] * lst[1] == lst[2]:
    print("2")
else:
    print("3")