import bisect
from collections import deque

def solution(numlist, n):
    answer = []
    
    numlist = sorted(numlist)
    idx = bisect.bisect_left(numlist, n)
    
    a = deque(numlist[:idx])
    b = deque(numlist[idx:])
    
    while a or b:
        if not a:                      # 왼쪽이 비었으면 오른쪽만
            answer.append(b.popleft())
            continue
        if not b:                      # 오른쪽이 비었으면 왼쪽만
            answer.append(a.pop())
            continue
        
        ca = a[-1]
        cb = b[0]
        
        if abs(ca - n) > abs(cb - n): # cb와 차이가 더 작다면
            answer.append(b.popleft())
        elif abs(ca - n) == abs(cb - n): # ca 와 cb의 차이가 같다면
            answer.append(b.popleft())
            answer.append(a.pop())
        else: # ca와 차이가 더 작다면
            answer.append(a.pop())
    
    return answer