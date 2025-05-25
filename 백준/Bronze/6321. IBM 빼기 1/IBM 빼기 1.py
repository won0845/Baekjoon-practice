for i in range(1, int(input()) + 1) :
    print(f"String #{i}")
    s = input()
    for i in s :
        if i == "Z" : print("A", end = "")
        else : print(chr(ord(i) + 1), end = "")
    print()
    print()