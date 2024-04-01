from collections import deque

M, N = map(int, input().split())  # M: 가로 길이, N: 세로 길이
mapT = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
queue = deque()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
days = -1

# 초기 익은 토마토 위치 찾기
for i in range(N):
    for j in range(M):
        if mapT[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = True

# BFS 실행
while queue:
    days += 1  # 각 사이클마다 날짜 증가
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and mapT[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                mapT[nx][ny] = 1
                queue.append((nx, ny))

# 모든 토마토가 익었는지 확인
for row in mapT:
    if 0 in row:
        print(-1)
        break
else:
    print(days)
