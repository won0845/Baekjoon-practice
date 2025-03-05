import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

movex = [1,2,2,1,-1,-2,-2,-1]
movey = [-2,-1,1,2,2,1,-1,-2]


    
def bfs(cx,cy,dx,dy):
    cnt = 0
    q = deque([(cx,cy,cnt)])
    visited[cx][cy] = True
    while q:
        a,b, cnt = q.popleft()
        if a == dx and b == dy:
            print(cnt)
            break
        for i in range(8):
            x = a + movex[i]
            y = b + movey[i]
            if x >= 0 and x < size and y >=0 and y < size and not visited[x][y]:
                q.append((x,y,cnt+1))
                visited[x][y] = True    


for _ in range(n):
    size = int(input())
    visited = [[False for _ in range(size)] for _ in range(size)]
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    bfs(cx,cy,dx,dy)