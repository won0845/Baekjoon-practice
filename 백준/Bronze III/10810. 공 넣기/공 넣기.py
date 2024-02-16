import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
bucket = [0] * N
for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        bucket[i] = c
print(' '.join(map(str, bucket)))
