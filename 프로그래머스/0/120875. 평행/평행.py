def solution(dots):
    def parallel(a, b, c, d):
        x1, y1 = dots[a]
        x2, y2 = dots[b]
        x3, y3 = dots[c]
        x4, y4 = dots[d]
    
        return (y2 -y1) * (x4- x3) == (y4-y3) * (x2 - x1) 
    
    if parallel(0, 1, 2, 3):
        return 1
    if parallel(0, 2, 1, 3):
        return 1
    if parallel(0, 3, 2, 1):
        return 1
    return 0
    
    


