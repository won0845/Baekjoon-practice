def solution(lines):
    
    horizon = [0] * 201
    
    for s,e in lines:
        for x in range(s,e):
            horizon[x + 100] += 1
            
    answer = sum(1 for v in horizon if v >= 2)
    return answer