import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(r, depth):
    visited[r] = depth
    for node in graph[r]:
        if visited[node] == -1:
            dfs(node, depth + 1)

dfs(r, 0)

for i in range(1, n+1):
    print(visited[i])
