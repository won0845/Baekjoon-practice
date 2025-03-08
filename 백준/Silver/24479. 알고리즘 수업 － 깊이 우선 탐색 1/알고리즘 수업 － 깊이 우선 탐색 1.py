import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 방문을 위해
for i in range(1, n + 1):
    graph[i].sort()

cnt = [1]
def dfs(v):
    visited[v] = cnt[0]
    for i in graph[v]:
        if not visited[i]:
            cnt[0] += 1
            dfs(i)

dfs(v)
# print(cnt[0])
# 결과 출력
for i in range(1, n + 1):
    print(visited[i])
