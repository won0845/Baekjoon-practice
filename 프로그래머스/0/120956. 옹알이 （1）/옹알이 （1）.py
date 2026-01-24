def solution(babbling):
    answer = 0
    
    can = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        for j in can:
            babbling[i] = babbling[i].replace(j, " ")
            # print(babbling[i])
        
    answer = sum(1 for i in babbling if i.strip() == "")
    return answer