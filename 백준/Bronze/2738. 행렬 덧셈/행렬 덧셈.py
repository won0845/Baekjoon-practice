import sys

input = sys.stdin.readline
A = []
B = []
N, M = map(int, input().split())

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(N):
    a = list(map(int, input().split()))
    B.append(a)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()
