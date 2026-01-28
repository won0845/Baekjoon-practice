from itertools import cycle

def solution(answers):
    answer = []
    
    cnt = [0,0,0]
    
    gm1 = [1, 2, 3, 4, 5]
    gm2 = [2, 1, 2, 3, 2, 4, 2, 5]
    gm3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for a, g1, g2, g3 in zip(answers, cycle(gm1), cycle(gm2), cycle(gm3)):
        if a == g1:
            cnt[0] += 1
        if a == g2:
            cnt[1] += 1
        if a == g3:
            cnt[2] += 1

    maxv = max(cnt[0], cnt[1], cnt[2])
    
    for i in range(len(cnt)):
        if cnt[i] == maxv:
            answer.append(i+1)
    
    
    return answer