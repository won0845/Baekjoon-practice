def solution(sides):
    
    sides.sort()
    l = sides[2]
    a = sides[0]
    b = sides[1]
    
    answer = 2
    if l < a + b:
        answer = 1
    
    return answer