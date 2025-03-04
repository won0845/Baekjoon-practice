import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, V = map(int, input().split())

visitDFS = [False] * (N + 1)
visitBFS = [False] * (N + 1)

# ⚡ 인접 리스트로 변경 (메모리 최적화)
graph = [[] for _ in range(N + 1)]

# ⚡ 입력 처리 & 작은 번호부터 방문하도록 정렬
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    graph[i].sort()  # 작은 번호부터 방문하도록 정렬

# ✅ DFS (재귀)
def dfs(v):
    visitDFS[v] = True
    dfs_result.append(str(v))  # ⚡ 리스트에 저장하여 출력 최적화
    for i in graph[v]:  # ⚡ 1부터 N까지 검사하는 대신 리스트 순회
        if not visitDFS[i]:
            dfs(i)

# ✅ BFS (큐)
def bfs(v):
    q = deque([v])
    visitBFS[v] = True
    while q:
        node = q.popleft()
        bfs_result.append(str(node))  # ⚡ 리스트에 저장하여 출력 최적화
        for i in graph[node]:  # ⚡ 1부터 N까지 검사하는 대신 리스트 순회
            if not visitBFS[i]:
                q.append(i)
                visitBFS[i] = True  # ⚡ 큐에 넣을 때 방문 체크

# 결과 저장을 위한 리스트 (출력 최적화)
dfs_result = []
bfs_result = []

dfs(V)
bfs(V)

# ⚡ 한 번만 출력하여 성능 최적화
print(" ".join(dfs_result))
print(" ".join(bfs_result))
