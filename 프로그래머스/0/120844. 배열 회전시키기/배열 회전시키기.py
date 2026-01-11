from collections import deque 

def solution(numbers, direction):
    
    que = deque(numbers)
    
    if direction == "right":
        pop = que.pop()
        que.insert(0,pop)
    else:
        pop = que.popleft()
        que.append(pop)
    answer = list(que)
    return answer