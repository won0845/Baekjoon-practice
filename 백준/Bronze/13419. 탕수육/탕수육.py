n = int(input())

for i in range(n):
    ans = input()
    a = []
    b = []
    if len(ans) % 2 == 0:
        for j in range(len(ans)):
            if j % 2 == 0:
                a.append(ans[j])
            else:
                b.append(ans[j])
        print("".join(a))
        print("".join(b))
    else:
        ans *= 2
        for j in range(len(ans)):
            if j % 2 == 0:
                if a[:-1] == ans[j]:
                    break
                a.append(ans[j])
            else:
                if b[:-1] == ans[j]:
                    break
                b.append(ans[j])
        print("".join(a))
        print("".join(b))
        