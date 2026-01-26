def solution(num, total):
    answer = []
    start = total // num - (num-1) //2
    
    for i in range(start, start + num):
        answer.append(i)
    
    return answer