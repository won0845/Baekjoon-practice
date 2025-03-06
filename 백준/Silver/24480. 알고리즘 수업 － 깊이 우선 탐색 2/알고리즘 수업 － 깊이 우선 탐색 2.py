import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, v = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 1

for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
for i in range(1,n+1):
    tree[i].sort(reverse = True)

def dfs(v):
    global cnt
    visited[v] = cnt
    for i in tree[v]:
        if not visited[i]:
            cnt+=1
            dfs(i)
            

visited[v] = 1
dfs(v)

for i in range(1, n+1):
    print(visited[i])
    
    
               