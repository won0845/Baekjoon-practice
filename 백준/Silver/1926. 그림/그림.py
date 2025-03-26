import sys
from collections import deque

n, m = map(int, input().split())

do = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[0 for _ in range(m)] for _ in range(n) ]

for _ in range(n):
    do.append(list(map(int, input().split())))
    
imgmax = 0
imgcnt = 0

def bfs(a,b):
    q = deque([(a,b)])
    visited[a][b] = 1
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            rx = dx[i] + x
            ry = dy[i] + y
            if rx >= 0 and rx < n and ry >= 0 and ry < m and visited[rx][ry] == 0 and do[rx][ry] == 1:
                visited[rx][ry] = size
                q.append((rx, ry))
                size +=1
    return size

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and do[i][j] == 1:
            imgcnt += 1
            imgmax = max(bfs(i,j),imgmax)
            
print(imgcnt)
print(imgmax)