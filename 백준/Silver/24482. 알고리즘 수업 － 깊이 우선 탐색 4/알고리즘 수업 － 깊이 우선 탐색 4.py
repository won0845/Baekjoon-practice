import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m , r = map(int, input().split())
v = [[]for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

for i in v:
    i.sort(reverse= True)

def dfs(r, depth):
    visited[r] = depth
    for i in v[r]:
        if visited[i] == -1:
            dfs(i, depth + 1)
dfs(r, 0)
for i in range(1, len(visited)):
    print(visited[i])
