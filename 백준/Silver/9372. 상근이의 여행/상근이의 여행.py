n = int(input())

for i in range(n):
    N, M = map(int, input().split())
    country = [[] for i in range(N+1)]
    visited = [0 for i in range(N+1)]
    for j in range(M):
        a, b = map(int, input().split())
        country[a].append(b)
        country[b].append(a)

    stk =[]
    stk.append(country[1][0])
    cnt = 0
    while stk:
        a = stk.pop()
        if visited[a] == 0:
            visited[a] = 1
            cnt +=1
            for k in country[a]:
                stk.append(k)
    print(cnt- 1)
                
        

