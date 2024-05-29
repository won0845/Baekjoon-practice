import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hap = 0

A.sort()
B.sort(reverse=True)

for i in range(N):
    hap += A[i] * B[i]

print(hap)