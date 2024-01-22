import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

queue = deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)

result = []
while queue:
    node = queue.popleft()
    result.append(node)
    for adj in graph[node]:
        inDegree[adj] -= 1
        if inDegree[adj] == 0:
            queue.append(adj)

print(" ".join(map(str, result)))