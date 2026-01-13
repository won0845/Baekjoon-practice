def solution(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 0
    
    print(len(dict),  (len(nums) // 2))
    max_value = len(dict)
    if max_value > (len(nums) // 2):
        max_value = (len(nums) // 2)
    
    answer = max_value
    return answer