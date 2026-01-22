def solution(spell, dic):
    answer = 0
    s = sorted(spell)
    
    for i in dic:
        if sorted(i) == s:
            return 1
    
    return 2