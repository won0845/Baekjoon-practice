from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

friends = []

for _ in range(n):
    friends.append(list(map(str, input())))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]

cnt = [0]

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] =True
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if x >= 0 and x < n and y >= 0 and y < m and not visited[x][y] and friends[x][y] != "X":
                visited[x][y] = True
                q.append((x,y))
                if friends[x][y] == "P":
                    cnt[0] += 1
    return cnt[0]
for i in range(n):
    for j in range(m):
       if friends[i][j] == "I":
           result = bfs(i,j)
if result == 0:
    print("TT")
else:
    print(result)