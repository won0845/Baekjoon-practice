import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

visited = [[False for _ in range(m)]for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


room = []
for _ in range(n):
    room.append(list(map(int, input().split())))


def bfs(x,y):
    if visited[x][y]:
        return 0
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        for i in range(4):
            xx = dx[i] + a
            yy = dy[i] + b
            if xx >= 0 and xx < n and yy >=0 and yy < m:
                if not visited[xx][yy] and abs(room[a][b]-room[xx][yy]) <= k:
                    visited[xx][yy] = True
                    q.append((xx,yy))
    return 1
cnt = 0
for i in range(n):
    for j in range(m):
        cnt += bfs(i,j)
print(cnt)
    
