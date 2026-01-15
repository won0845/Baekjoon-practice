def solution(num, k):
    num_list = list(str(num))
    cnt = 0
    for i, v in enumerate(num_list):
        print(i, v, k)
        if str(k) == v:
            return i+1
        
    answer = -1
    return answer