import sys

input = sys.stdin.readline

check = [True for _ in range(1000001)]

check[0] = False
check[1] = False

for i in range(2, int(1000001 ** 0.5) + 1):
    if check[i]:
        for k in range(i * i, 1000001, i):
            check[k] = False

n = int(input())

# 문제 풀이
for i in range(n):
    count = 0
    N = int(input())
    for j in range(2, N // 2 + 1):
        if check[j] and check[N - j]:
            count += 1
    print(count)
