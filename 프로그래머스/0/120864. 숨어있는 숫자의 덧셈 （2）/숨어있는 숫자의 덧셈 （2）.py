def solution(my_string):
    answer = 0
    buf = ""
    
    for i in my_string:
        if i.isdigit():
            buf += i
        else:
            if buf:
                answer += int(buf)
                buf = ""
    if buf:
        answer += int(buf)
    return answer