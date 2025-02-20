from collections import deque
n = int(input())
a,b = map(int, input().split())
m = int(input())

visited = [0 for _ in range(n+1)]
family =[[] for _ in range(n+1)]
count = [-1 for _ in range(n+1)]


for i in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

q = deque([a])
count[a] = 0 #본인은 촌수가 0
visited[a] = 1 # 방문체크
depth = 0

while q:
    v = q.popleft()
    for i in family[v]:
        if visited[i] == 0:
            visited[i] = 1
            count[i] = count[v] + 1
            q.append(i)

print(count[b])
            
