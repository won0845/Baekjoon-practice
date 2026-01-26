def solution(common):
    arr = common
    
    if arr[1] - arr[0] == arr[2] - arr[1]:
        return arr[-1] + arr[1] - arr[0]
    elif arr[1] / arr[0] == arr[2] / arr[1]:
        return arr[-1] * (arr[1] / arr[0])

    return answer