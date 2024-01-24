import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 설정
input = sys.stdin.readline

N = int(input())
parent = [0] * (N + 1)
visit = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    q = deque([v])

    visit[v] = True
    while q:
        v = q.popleft()
        for j in graph[v]:
            if not visit[j]:
                q.append(j)
                parent[j]=v
                visit[j] = True


bfs(1)
for i in range(2,len(parent)):
    print(parent[i])