n = input()

while n != "0":
    one = 0
    zero = 0
    one = n.count("1")
    zero = n.count("0")
    
    print((len(n)-1)+(one*2)+(zero*4)+((len(n)-(one+zero))*3)+1+1)
    n = input()