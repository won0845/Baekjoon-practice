import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
visitDFS = [False] * (N + 1)  # DFS 방문기록

graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True


def dfs(v):
    visitDFS[v] = True
    for i in range(1, N + 1):
        if not visitDFS[i] and graph[v][i]:
            dfs(i)
count = 0
for i in range(1, N+1):
    if not visitDFS[i]:
        count +=1
        dfs(i)

print(count)