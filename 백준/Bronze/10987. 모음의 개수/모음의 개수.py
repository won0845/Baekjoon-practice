n = input()

mo = {"a":0, "e":0, "i":0, "o":0, "u":0} 
for i in n:
    if i in mo:
        mo[i] +=1
print(sum(list(mo.values())))