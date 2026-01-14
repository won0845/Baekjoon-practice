def solution(s):
    answer = []
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    
    for i, v in dic.items():
        if v == 1:
             answer.append(i)
    answer.sort()
    return "".join(answer)