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
    i.sort()

def dfs(r, depth):
    visited[r] = depth * cnt[0]
    for i in v[r]:
        if visited[i] == -1:
            cnt[0] += 1
            dfs(i, depth+1)

cnt = [1]            
dfs(r, 0)

hap =0 
for i in range(1, len(visited)):
    if visited[i] != -1:
        hap += visited[i]
print(hap)
