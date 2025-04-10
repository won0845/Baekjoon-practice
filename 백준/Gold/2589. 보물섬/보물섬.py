from collections import deque

g, s = map(int, input().split())
zido = [list(input().strip()) for _ in range(g)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    visited = [[-1 for _ in range(s)] for _ in range(g)]
    visited[i][j] = 0
    q = deque([(i, j)])
    max_dist = 0

    while q:
        a, b = q.popleft()
        for k in range(4):    
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < g and 0 <= y < s:
                if zido[x][y] == "L" and visited[x][y] == -1:
                    visited[x][y] = visited[a][b] + 1
                    max_dist = max(max_dist, visited[x][y])
                    q.append((x, y))
    return max_dist

# 전체 지도를 돌면서 가장 긴 거리 구하기
maxVal = 0
for i in range(g):
    for j in range(s):
        if zido[i][j] == 'L':
            maxVal = max(maxVal, bfs(i, j))

print(maxVal)
