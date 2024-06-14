import sys

input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    H, W, N = map(int, input().split())
    ho = N % H
    floor = N // H + 1
    if ho == 0:
        ho = H
        floor -= 1
    if floor < 10:
        print(f"{ho}0{floor}")
    else:
        print(f"{ho}{floor}")