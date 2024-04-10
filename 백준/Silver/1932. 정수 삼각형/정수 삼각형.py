import sys
input = sys.stdin.readline

n = int(input())
d = []

for _ in range(n):
    d.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            d[i][j] += d[i-1][0]
        elif i == j:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])
print(max(d[n-1]))