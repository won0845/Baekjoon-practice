def solution(my_string):
    nums = []
    for i in my_string:
        if i.isdigit():
            nums.append(int(i))
            
    answer = sum(nums)
    return answer