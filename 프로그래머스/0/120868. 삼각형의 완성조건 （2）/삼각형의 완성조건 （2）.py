def solution(sides):
    answer = 0
    
    # 둘중에 한변이 가장 긴변인 경우
    cnt = 0
    
    for i in range(max(sides)-min(sides)+1, max(sides)+1, 1):
        cnt += 1
    
    # 나머지 한변이 가장 긴변인 경우
    for i in range(max(sides)+1, max(sides)+min(sides)):
        cnt += 1
    
    answer = cnt
    return answer