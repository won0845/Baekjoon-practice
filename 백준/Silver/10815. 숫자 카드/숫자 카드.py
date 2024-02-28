import sys

input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

ans = []

for num in nums:
    if num in cards:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)