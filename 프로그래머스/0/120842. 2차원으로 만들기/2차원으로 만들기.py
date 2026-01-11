def solution(num_list, n):
    answer = []
    
    for i in range(len(num_list)//n):
        answer.append([])
        for j in range(n):
            answer[i].append(num_list[n*i+j])
        
    return answer



# 1 2  3 4  5 6
# 1~4 
# 1~2
#
#