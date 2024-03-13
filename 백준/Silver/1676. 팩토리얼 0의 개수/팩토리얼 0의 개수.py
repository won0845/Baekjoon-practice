import sys

input = sys.stdin.readline

n = int(input())
sum = 1
cnt = 0
for i in range(1, n + 1):
    sum *= i
for j in str(sum)[::-1]:
    if j != '0':
        break
    cnt += 1

print(cnt)