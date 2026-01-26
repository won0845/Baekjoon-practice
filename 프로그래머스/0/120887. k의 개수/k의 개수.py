def solution(i, j, k):
    answer = 0
    for t in range(i, j+1):
        answer += str(t).count(str(k))
    
    return answer