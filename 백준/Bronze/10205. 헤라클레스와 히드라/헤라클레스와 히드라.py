n = int(input())

for i in range(1, n+1):
    s = int(input())
    string = input()
    for j in string:
        if j == "c":
            s += 1
        else:
            s -= 1
    print("Data Set "+ str(i)+":")
    print(s)
    print()