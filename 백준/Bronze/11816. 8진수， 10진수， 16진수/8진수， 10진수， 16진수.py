x =input()
if x[0] == '0' and x[1] =='x':
    print(int(x,16))
elif x[0] == '0' and (x[1] != 'x'):
    print(int(x,8))
else:
    print(int(x))