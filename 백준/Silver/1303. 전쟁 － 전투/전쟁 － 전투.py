def bfs(i, j, color):
    cnt = 0
    que = deque()
    que.append((i, j))
    visited[i][j] = True

    while que:
        n, m = que.popleft()

        for l in range(4):
            x = n + dx[l]
            y = m + dy[l]

            if 0 <= x < b and 0 <= y < a and board[x][y] == color and not visited[x][y]:
                # visited 처리 뺴먹음
                visited[x][y] = True
                que.append([x, y])
                cnt += 1
    return (cnt + 1) ** 2


import sys
from collections import deque

a, b = map(int, input().split())  # 가로 a, 세로 b
input = sys.stdin.readline
board = []
my, eny = 0, 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0 for i in range(a)] for j in range(b)]

for i in range(b):
    board.append(list(map(str, input().rstrip())))

for i in range(b):
    for j in range(a):
        if board[i][j] == "W" and not visited[i][j]:
            my += bfs(i, j, "W")
        if board[i][j] == "B" and not visited[i][j]:
            eny += bfs(i, j, "B")

print(my, eny)