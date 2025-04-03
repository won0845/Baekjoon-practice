N = int(input())

check = [False for _ in range(N+1)]
check2 =[False for _ in range(N+1)]
nodes = [[] for _ in range(N+1)]


#print(visited)

for _ in range(N-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

order = list(map(int, input().split()))
           
# 방문 순서에 따른 우선순위 매기기
priority = [0 for _ in range(N + 1)] 
for i in range(N):
    priority[order[i]] = i


# 각 노드의 자식들을 방문 순서 기준으로 정렬
for i in range(1, N + 1):
    nodes[i].sort(key=lambda x: priority[x])


result =[]
def dfs(x):
    if check[x]:
        return;
    check[x] = True;
    result.append(x)
    # x를 방문
    for i in nodes[x]:
        if not check[i]:
            dfs(i)
dfs(1)

if result == order:
    print(1)
else:
    print(0)
