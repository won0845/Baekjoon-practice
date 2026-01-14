def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    s3 = s1 & s2
    answer = len(s3)
    return answer