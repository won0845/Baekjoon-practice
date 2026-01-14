def solution(numbers):
    nums = list(map(str, numbers))

    nums.sort(key=lambda x: x*4, reverse=True)

    if nums[0] == "0":
        return "0"

    return "".join(nums)
