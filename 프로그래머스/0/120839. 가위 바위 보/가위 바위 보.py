def solution(rsp):
    
    vic_dic = {"2":"0", "5":"2", "0":"5"}
    ans = []
    
    for i in rsp:
        ans.append(vic_dic[i])
    
    answer = "".join(ans)
    return answer