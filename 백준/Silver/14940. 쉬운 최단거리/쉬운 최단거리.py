import sys
from collections import deque

input = sys.stdin.readline

maplist = []
sn, gm = map(int, input().split())
visited = [[0 for _ in range(gm)] for _ in range(sn)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0

queue = deque()

for _ in range(sn):
    maplist.append(list(map(int, input().split())))

for i in range(sn):
    for j in range(gm):
        if maplist[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = True
            maplist[i][j] = cnt

# BFS 실행
while queue:
    cnt += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < sn and 0 <= ny < gm and maplist[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                maplist[nx][ny] = cnt
                queue.append((nx, ny))

for i in range(sn):
    for j in range(gm):
        if maplist[i][j] != 0 and not visited[i][j]:
            print(-1, end=" ")
        else:
            print(maplist[i][j], end=" ")
    print()


