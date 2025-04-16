import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    parent =[0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a

    l, k = map(int, input().split())

    # 부모의 노드들을 싹다 방문처리한다!!
    while l != 0:
        visited[l] = True
        l = parent[l]

    #방문 한곳만을 찾는다.
    while not visited[k] :
        k = parent[k]
    print(k)