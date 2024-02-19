import sys
input = sys.stdin.readline

Big = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())
count = 0

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            Big[i+b][j+a] = 1

for i in range(100):
    for j in range(100):
        if Big[i][j] != 0:
            count +=1

print(count)