n = int(input())
for i in range(n):
    string = list(map(str, input()))
    buf = string[0]
    ans = [buf]
    for j in range(len(string)):
        if buf == string[j]:
            continue
        else:
            buf = string[j]
            ans.append(buf)
    for k in ans:
        print(k,end="")
    print()