import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, K, X = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]
visitBFS = [False] * (N + 1)  # BFS 방문기록
distance = [0] * (N + 1)

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)


def bfs(v):
    answer = []
    q = deque([v])
    visitBFS[v] = True
    distance[v] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:  # 직접 연결된 노드들에만 접근
            if not visitBFS[i]:
                q.append(i)
                visitBFS[i] = True
                distance[i] = distance[v] + 1
                if distance[i] == K:
                    answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for j in answer:
            print(j)


bfs(X)
