n = input()

lst = {"a":4, "e":3, "i":1, "o":0, "s":5}

for i in n:
    if i in lst:
        print(lst[i],end="")
    else:
        print(i,end="")