def solution(my_string, n):
    lst = []
    for i in my_string:
        lst.append(i * n)
        
    answer = "".join(lst)
    return answer