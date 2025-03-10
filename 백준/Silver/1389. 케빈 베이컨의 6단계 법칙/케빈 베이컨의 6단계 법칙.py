from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tree = [[] for _ in range(n+1)]
bacon = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(v, t):
    visited = [False for _ in range(n+1)]
    if v == t:
        return 0
    q = deque([(v, 0)])
    visited[v] = True
    
    while q:
        node, cnt = q.popleft()
        if t == node:
            return cnt
            
        for i in tree[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt+1))
    return 0

for i in range(1,n+1):
    for j in range(1,n+1):
        bacon[i] += bfs(i,j)

print(bacon.index(min(bacon[1::])))