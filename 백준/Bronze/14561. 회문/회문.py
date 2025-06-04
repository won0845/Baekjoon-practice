t = int(input())

for i in range(t):
    a, n = map(int, input().split())
    ans = []
    flag = True
    while True:
        if a == 0: break
        x = a % n
        ans.append(x)
        a //= n

    for j in range(len(ans)//2):
        if ans[j] != ans[-1-j]:
            flag = False

    if flag == True:
        print(1)
    else:
        print(0)
