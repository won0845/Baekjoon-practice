import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

for i in range(666, 10000000000):
    if "666" in str(i):
        cnt += 1
        if n == cnt:
            print(i)
            break