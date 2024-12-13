a, b = map(int,input().split())
cnt = 0
for i in range(a):
    p = "*"
    q = "."
    if i % 2 == 0:
        p = "*"
        q = "."
    else:
        p = "."
        q = "*"
    
    for j in range(b):
        if j % 2 == 0:
            print(p, end="")
        elif j % 2 != 0:
            print(q, end="")
    print()