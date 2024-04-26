import sys
import math

input = sys.stdin.readline
N, L = map(int, input().split())
pool = sorted(tuple(map(int, input().split()))for _ in range(N))
ans = 0
s = 0
for start, end in pool:
    s = max(start, s)
    diff = end - s
    cnt = math.ceil(diff/L)
    ans += cnt
    s += L * cnt
print(ans)