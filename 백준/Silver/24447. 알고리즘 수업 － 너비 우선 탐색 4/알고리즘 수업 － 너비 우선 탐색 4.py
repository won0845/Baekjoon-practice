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

for i in v:
    i.sort()

def bfs(r, depth, cnt):
    visited[r] = depth 
    q = deque([(r, depth)])
    while q:        
        node, d = q.popleft()
        d +=1
        for i in v[node]:
            if visited[i] == -1:
                cnt[0] += 1
                visited[i] = d * cnt[0]
                q.append((i, d))

cnt =[1]
bfs(r, 0, cnt)
hap = 0
for i in visited:
    if i != -1:
        hap += i

print(hap)
