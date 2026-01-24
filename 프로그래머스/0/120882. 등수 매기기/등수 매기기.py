def solution(score):
    answer = []
    avg = [(x[0] + x[1]) / 2 for x in score]
    sorted_avg = sorted(avg, reverse=True)
    
    print(avg, sorted_avg)
    for i in avg:
        answer.append(sorted_avg.index(i)+1)
        
    print(answer)
    
    
    return answer