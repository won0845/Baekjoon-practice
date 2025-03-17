from collections import deque
import sys

input = sys.stdin.readline


n = int(input())
m = int(input())

friends = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

ans = [0]

def bfs(cnt, v):
    q = deque([(1, v)])    
    visited[v] = True
    while q:
        cnt, node = q.popleft()
        for friend in friends[node]:
            if not visited[friend]:  # 방문하지 않은 친구만 탐색
                visited[friend] = True  # 방문 체크
                q.append((cnt+1,friend))
                if cnt <= 2:
                    ans[0] += 1


bfs(1, 1)

print(ans[0])
