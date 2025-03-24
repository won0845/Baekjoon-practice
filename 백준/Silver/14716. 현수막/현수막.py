import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())

hun = []
visited = [[False for _ in range(m)] for _ in range(n)] 
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

for _ in range(n):
    hun.append(list(map(int, input().split())))


cnt = 0
for i in range(n):
    for j in range(m):    
        if not visited[i][j] and hun[i][j] == 1:
            q = deque([(i,j)])
            while q:
                a, b = q.popleft()
                for k in range(8):
                    x = a + dx[k]
                    y = b + dy[k]
                    if x >= 0 and x < n and y >= 0 and y < m and not visited[x][y]:
                        visited[x][y] = True
                        if hun[x][y] != 0:
                            q.append((x,y))
            cnt +=1
                
print(cnt)