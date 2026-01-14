def solution(array, commands):
    ans = []
    for command in commands:
        i = command[0] 
        j = command[1] 
        k = command[2] 
        answer = sorted(array[i-1:j])
        ans.append(answer[k-1])
        
    
    
    return ans