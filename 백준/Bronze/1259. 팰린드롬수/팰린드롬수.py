import sys

input = sys.stdin.readline
n = int(input())

while n != 0:
    nums = list(map(int, str(n)))
    revernum = list(reversed(nums))
    corcnt = 0
    for i in range(len(nums)):
        if nums[i] == revernum[i]:
            corcnt += 1
    if corcnt == len(nums):
        print("yes")
    else:
        print("no")
    n = int(input())
