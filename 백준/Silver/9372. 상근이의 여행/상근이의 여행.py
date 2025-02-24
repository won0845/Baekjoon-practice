n = int(input())

for i in range(n):
    N, M = map(int, input().split())
    country = [[] for i in range(N+1)]
    visited = [False] * (N+1)
    for j in range(M):
        a, b = map(int, input().split())
        country[a].append(b)
        country[b].append(a)

    stk =[1]
    visited[1] =True
    cnt = 0
    
    while stk:
        a = stk.pop()
        for k in country[a]:        
            if not visited[k]:
                visited[k] = True
                cnt +=1
                stk.append(k)
                
    print(cnt)