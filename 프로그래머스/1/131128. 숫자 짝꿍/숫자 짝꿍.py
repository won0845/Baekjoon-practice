def solution(X, Y):
    answer = ''
    
    
    dicX = extra(X)
    dicY = extra(Y)
    dic = {i : 0 for i in range(0, 10)}
    lst = []
    
    for i in range(9, -1, -1):
        if dicX[i] != 0 and dicY[i] != 0:
            lst.append(str(i) * min(dicX[i], dicY[i]))
    
    if lst:
        answer = str(''.join(lst))
    else:
        answer = "-1"
        
    if lst and lst[0][0] == "0":
        return "0"
    
    return answer

def extra(num):
    dic = {i : 0 for i in range(0,10)}
    for i in num:
        dic[int(i)] += 1
    return dic