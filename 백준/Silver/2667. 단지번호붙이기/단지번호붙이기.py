import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

adj = [0 for _ in range(N)]

for i in range(N):
    adj[i] = str(input())

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


chk = [[False] * N for _ in range(N)]


def dfs(y, x):
    chk[y][x] = True
    count = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_valid_coord(ny, nx) and adj[ny][nx] == "1" and not chk[ny][nx]:
            count += dfs(ny, nx)
    return count

danji_counter = 0
house_per_danji = []

for i in range(N):
    for j in range(N):
        if adj[i][j] == "1" and not chk[i][j]:
            house_per_danji.append(dfs(i, j))
            danji_counter += 1

print(danji_counter)
house_per_danji.sort()
for danji in house_per_danji:
    print(danji)
