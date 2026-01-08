from collections import Counter

def solution(array):
    cnt = Counter(array)
    
    max_value = max(cnt.values())
    modes = [num for num, cnt in cnt.items() if cnt == max_value]
    
    if len(modes) > 1:
        return -1
    
    return modes[0]