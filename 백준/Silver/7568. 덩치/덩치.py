import sys

input = sys.stdin.readline

n = int(input())
lst = []
rank = [1 for _ in range(n)]

for _ in range(n):
    w, h = map(int, input().split())
    lst.append([w, h])

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            rank[j] += 1
        elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank[i] += 1

for i in rank:
    print(i,end=" ")