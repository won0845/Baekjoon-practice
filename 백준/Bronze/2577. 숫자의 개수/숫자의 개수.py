A = int(input())
B = int(input())
C = int(input())

value = A*B*C
strvalue = str(value)

for i in range(10):
    print(strvalue.count(str(i)))