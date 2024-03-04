import sys

input = sys.stdin.readline

check = [True for _ in range(246913)]

check[1] = False

for i in range(2, int(246913 ** 0.5) + 1):
    if check[i]:
        for j in range(i * i, 246913, i):
            check[j] = False

n = int(input())
while n != 0:
    cnt = 0
    for k in range(n + 1, (2 * n) + 1):
        if check[k]:
            cnt += 1
    print(cnt)
    n = int(input())