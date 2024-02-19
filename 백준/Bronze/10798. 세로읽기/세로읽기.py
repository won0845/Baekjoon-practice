import sys
input = sys.stdin.readline
A = []

for _ in range(5):
    A.append(list(input().strip()))


for i in range(5):
    length = len(A[i])
    for j in range(15 - length):
        A[i].append("")

for i in range(15):
    for j in range(5):
        print(A[j][i], end="")