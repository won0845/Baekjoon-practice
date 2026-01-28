def solution(citations):
    answer = 0
    
    citations = sorted(citations, reverse = True)
    
    for i, v in enumerate(citations, start = 1):
        if v >= i:
            answer = i
        else:
            break
        
    
    return answer