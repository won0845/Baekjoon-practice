gimul = {"K":0, "k":0,"P":1,"p":1, "N":3,"n":3, "B":3,"b":3,"R":5, "r":5,"Q":9,"q":9}
black = 0
white = 0
lst =[]
for i in range(8):
    lst.append(list(map(str,input())))
    
for i in range(8):
    for j in range(8):
        if lst[i][j] == ".":
            continue
        elif lst[i][j].isupper():
            white += gimul[lst[i][j]]
        elif lst[i][j].islower():
            black += gimul[lst[i][j]]
            
print(white-black)