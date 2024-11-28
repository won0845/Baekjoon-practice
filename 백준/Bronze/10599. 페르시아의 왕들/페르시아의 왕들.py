while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0 and lst[3] == 0 :
        break
    else:
        lst.sort()
        print(abs(lst[1]-lst[2]),abs(lst[0]-lst[3]))