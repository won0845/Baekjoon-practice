import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lst = []
answer = []

for _ in range(N):
    lst.append(list(map(int, input().strip())))


def bfs(x, y):
    q = deque([(x, y)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if lst[nx][ny] == 1:
                count += 1
                lst[nx][ny] = 0
                q.append((nx, ny))
    return count


for i in range(N):
    for j in range(N):
        if lst[i][j] == 0:
            continue
        answer.append(bfs(i, j))

answer.sort()

for i in range(answer.count(0)):
    answer[i] = 1

print(len(answer))
for i in answer:
    print(i)
