import bisect

def solution(array, height):
    array.sort()
    idx = bisect.bisect_right(array, height)
    
    answer = len(array) - idx
    return answer