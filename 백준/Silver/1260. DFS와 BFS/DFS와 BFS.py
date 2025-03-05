import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

visitedDFS = [False for _ in range(n+1)]
visitedBFS = [False for _ in range(n+1)]

tree = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
for i in range(1,n+1):
    tree[i].sort()

    
def dfs(v):
    visitedDFS[v] = True
    print(v, end=" ")
    for i in tree[v]:
        if not visitedDFS[i]:
            dfs(i)
    
def bfs(v):
    q = deque([v])
    visitedBFS[v] = True
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in tree[node]:
            if not visitedBFS[i]:
                q.append(i)
                visitedBFS[i] = True
dfs(v)
print()
bfs(v)
    
    
 