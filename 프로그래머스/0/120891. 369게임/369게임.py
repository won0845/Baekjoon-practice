def solution(order):
    check = ["3", "6", "9"]
    cnt = 0
    for i in check:
        cnt += str(order).count(i)
        
    answer = cnt
    return answer