import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())

mapList = []

for _ in range(N):
    mapList.append(list(map(int, input().strip())))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mapList[nx][ny] == 1:
                mapList[nx][ny] = mapList[x][y] + 1
                q.append((nx, ny))
    return mapList[N-1][M-1]

print(bfs(0, 0))
