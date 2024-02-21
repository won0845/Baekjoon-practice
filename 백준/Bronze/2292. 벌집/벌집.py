
import sys

input = sys.stdin.readline

N = int(input())
cnt = 1
i = 1

while N > i:

     i += 6 * cnt
     cnt += 1
print(cnt)