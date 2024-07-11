import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())
lst = []

for i in range(N):
    lst.append(input().split())
me = lst[a-1][b-1]
check = "HAPPY"
for i in range(N):
    if lst[a-1][i] > me or lst[i][b-1] > me:
        check = "ANGRY"
print(check)