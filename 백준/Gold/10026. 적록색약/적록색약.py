from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())

color = []

for i in range(n):
    color.append(list(input().strip()))



def dfs(i,j,col):
    if visited[i][j]:
        return 0
    currcolor = col
    q = deque([(i,j)])
    visited[i][j] = True
    while q:
        x, y = q.popleft()

        for k in range(4):
            a = dx[k] + x
            b = dy[k] + y
            if a >= 0 and a < n and b >= 0 and b < n:
                if not visited[a][b] and currcolor == color[a][b]:
                    q.append((a,b))
                    visited[a][b] = True
    return 1

hap = 0

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        hap += dfs(i,j,color[i][j])
print(hap, end=" ")
# replace 로 대체하기

for i in range(n):
    for j in range(n):
        if color[i][j] == 'G':
            color[i][j] = 'R'
hap = 0

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        hap += dfs(i,j,color[i][j])

print(hap)