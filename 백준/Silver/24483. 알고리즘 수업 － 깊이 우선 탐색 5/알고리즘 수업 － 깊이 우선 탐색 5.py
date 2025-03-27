import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m , r = map(int, input().split())
v = [[]for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
order = [0 for _ in range(n+1)]
cnt = [1]

for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

for i in v:
    i.sort()

def dfs(r, depth):
    visited[r] = depth
    order[r] = cnt[0]
    cnt[0] += 1
    for i in v[r]:
        if visited[i] == -1:
            dfs(i, depth+1)

        
dfs(r, 0)

print(sum(visited[i] * order[i] for i in range(1, n+1)))
