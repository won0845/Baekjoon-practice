from collections import deque

def solution(A, B):
    cnt = 0
    que = deque(A)
    
    while "".join(que) != B and cnt <= len(A):
        que.rotate(1)
        cnt += 1
    
    if cnt >= len(A):
        return -1
    
    return cnt