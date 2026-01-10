def solution(my_string, letter):
    string_a = []
    for i in my_string:
        if letter != i:
            string_a.append(i)
    
    answer = "".join(string_a)
    return answer