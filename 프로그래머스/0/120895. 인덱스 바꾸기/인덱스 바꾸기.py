def solution(my_string, num1, num2):
    s = list(my_string)   # 문자열 → 리스트
    
    s[num1], s[num2] = s[num2], s[num1]   # swap
    
    return "".join(s)    # 리스트 → 문자열
