import sys

input = sys.stdin.readline

a, b = map(int, input().split())
check = [True for _ in range(b + 1)]
check[1] = False

for i in range(2, int(b ** 0.5) + 1):
    if check[i]:
        for j in range(i*i, b +1, i):
                check[j] = False
for k in range(a, b+1):
    if check[k]:
        print(k)
