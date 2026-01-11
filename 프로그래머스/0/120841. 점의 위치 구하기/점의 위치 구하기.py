def solution(dot):
    x, y = dot[0], dot[1]
    answer = 0
    
    if x*y > 0 and x > 0:
        answer = 1
    elif x*y < 0 and x < 0:
        answer = 2
    elif x*y > 0 and x < 0:
        answer = 3
    elif x*y < 0 and x > 0:
        answer = 4
    
    
    return answer