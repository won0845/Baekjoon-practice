import bisect

def solution(array, n):
    array.sort()
    
    idx = bisect.bisect_left(array, n)
    # n이 들어갈 위치 [3, 10, 28]
    # idx 후보 0 1 2 3
    
    if idx == 0:
        return array[0]
    elif idx == len(array):
        return array[-1]
    
    left = array[idx-1]
    right = array[idx]
    
    answer = right if abs(left-n) > abs(right-n) else left
    

    return answer