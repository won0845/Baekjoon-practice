def solution(box, n):
    
    a1 = box[0] // n
    a2 = box[1] // n
    a3 = box[2] // n
    answer = a1 * a2 * a3
    return answer