def solution(quiz):
    answer = []
    for i in quiz:
        opers = i.split(" ")
        p1 = int(opers[0])
        oper = opers[1]
        p2 = int(opers[2])
        ans = int(opers[4])
        if oper == "-":
            if p1 - p2 == ans:
                answer.append("O")
            else:
                answer.append("X")
        elif oper == "+":
            if p1 + p2 == ans:
                answer.append("O")
            else:
                answer.append("X")
            
                
    
    return answer