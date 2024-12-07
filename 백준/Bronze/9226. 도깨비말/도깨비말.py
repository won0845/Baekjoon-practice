n = input()
mo = ["a","e","i","o","u"]

while n != "#":
    ans = []
    for i in range(len(n)):
        if n[i] in mo:
            print(n[i:],end="")
            break
        else:
            ans.append(n[i])
    print("".join(ans)+"ay")
    n = input()
            