import sys

input = sys.stdin.readline

N, M = map(int, input().split())
hap = {}
lst = list(map(int, input().split()))

hap[1] = 0
hap[2] = lst[0]
for i in range(2, N + 1):
    hap[i+1] = hap[i] + lst[i - 1]
for _ in range(M):
    a, b = map(int, input().split())
    print(hap[b+1] - hap[a])