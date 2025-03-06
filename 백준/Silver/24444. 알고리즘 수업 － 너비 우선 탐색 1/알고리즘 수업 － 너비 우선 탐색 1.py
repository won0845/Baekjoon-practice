import sys
from collections import deque

input = sys.stdin.readline

n,m,v = map(int, input().split())
visited = [0 for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1,n+1):
    tree[i].sort()
    
cnt = [1]

def bfs(v):
    q = deque([v])
    visited[v] = cnt[0]
    while q:
        node = q.popleft()
        for i in tree[node]:
            if not visited[i]:
                visited[i] = cnt[0]+1
                cnt[0]= cnt[0] + 1
                q.append(i)
    for i in range(1, n+1):
        print(visited[i])
    
bfs(v)
