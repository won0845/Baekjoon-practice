def solution(emergency):
    dic = {}
    
    sorted_list = sorted(emergency, reverse=True)
    
    for i, v in enumerate(sorted_list):
        dic[v] = i+1
        
    answer = []
    for e in emergency:
        answer.append(dic[e])
    
    return answer