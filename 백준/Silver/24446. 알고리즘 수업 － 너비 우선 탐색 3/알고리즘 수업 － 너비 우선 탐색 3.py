import sys
from collections import deque

input = sys.stdin.readline

n, m , r = map(int, input().split())
v = [[]for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

def bfs(r, depth):
    visited[r] = depth
    q = deque([(r, depth)])
    while q:        
        node, d = q.popleft()
        d +=1
        for i in v[node]:
            if visited[i] == -1:   
                visited[i] = d
                q.append((i, d))

bfs(r, 0)

for i in range(1, len(visited)):
    print(visited[i])
