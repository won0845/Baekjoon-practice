n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int,input().split())))
        
for i in lst:
    mack = 0
    zack = 0
    print(*i)
    if 17 in i and 18 in i:
        print("both")
    elif 18 in i:
        print("mack")
    elif 17 in i:
        print("zack")
    else:
        print("none")
    print()
