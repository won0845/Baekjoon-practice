# BFS -
#
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

visitDFS = [False] * (N + 1)  # DFS 방문기록
visitBFS = [False] * (N + 1)  # BFS 방문기록


def bfs(v):
    q = deque([v])
    visitBFS[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if not visitBFS[i] and graph[v][i]:
                q.append(i)
                visitBFS[i] = True


def dfs(v):
    visitDFS[v] = True
    print(v, end=" ")
    for i in range(1, N + 1):
        if not visitDFS[i] and graph[v][i]:
            dfs(i)


dfs(V)
print()
bfs(V)
