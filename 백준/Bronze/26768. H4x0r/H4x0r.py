n = input()
lst = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5'}

for i in lst:
    n = n.replace(i,lst[i])
print(n)