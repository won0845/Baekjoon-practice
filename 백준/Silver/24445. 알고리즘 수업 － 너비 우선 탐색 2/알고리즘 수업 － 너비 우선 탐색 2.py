from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
zip = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    zip[a].append(b)
    zip[b].append(a)

for i in range(1,n+1):
    zip[i].sort(reverse = True)

def bfs(r):
    dep = 1
    visited[r] = 1
    q = deque([r])
    while q:
        node = q.popleft()
        for i in zip[node]:
            if visited[i] == 0:
                dep += 1
                visited[i] = dep
                q.append(i)


bfs(r)

for i in range(1, len(visited)):
    print(visited[i])