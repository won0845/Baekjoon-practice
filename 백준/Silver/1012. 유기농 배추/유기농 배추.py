import sys
from collections import deque

input = sys.stdin.readline

testNum = int(input())

for _ in range(testNum):
    g, s, n = map(int, input().split())
    bMap = [[0 for _ in range(g)] for _ in range(s)]
    visited = [[0 for _ in range(g)] for _ in range(s)]
    cnt = 0

    for _ in range(n):
        a, b = map(int, input().split())
        bMap[b][a] = 1

    for j in range(g):
        for i in range(s):
            if bMap[i][j] == 1 and visited[i][j] == 0:
                bfs = deque([[i, j]])
                visited[i][j] = 1
                while bfs:
                    x, y = bfs.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < s and 0 <= ny < g and bMap[nx][ny] == 1 and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            bfs.append([nx, ny])
                cnt += 1
    print(cnt)