def solution(n, lost, reserve):
    answer = 0
    
    whole_student = {i : 1 for i in range(1, n+1)}
    
    for i in reserve:
        whole_student[i] += 1
    for i in lost:
        whole_student[i] -= 1
    
    for k in list(whole_student.keys()):
        if whole_student[k] == 0:
            if k > 1 and whole_student[k-1] == 2:
                whole_student[k-1] -= 1
                whole_student[k] += 1
            elif k < n and whole_student[k+1] == 2:
                whole_student[k+1] -= 1
                whole_student[k] += 1
            
    answer = sum(1 for i in whole_student.values() if i >= 1)
    
    return answer