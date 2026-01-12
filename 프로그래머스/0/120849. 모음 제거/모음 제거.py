def solution(my_string):
    moeum = ["a", "e", "i","o","u"]
    answer = []
    for i in my_string:
        if i not in moeum:
            answer.append(i)
    
    return "".join(answer)