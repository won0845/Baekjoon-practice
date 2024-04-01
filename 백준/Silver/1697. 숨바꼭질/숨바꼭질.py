import sys
from collections import deque
input = sys.stdin.readline

MAX = 10 ** 5
visited = [0] * (MAX + 1)
time = 0

s, d = map(int, input().split())  # s: 수빈이 위치 , N: 동생 위치
q = deque([s])

while q:
    cur = q.popleft()
    if cur == d:
        print(visited[cur])
        break
    for i in (cur + 1, cur - 1, cur * 2):
        if 0 <= i <= MAX and not visited[i]:
            visited[i] = visited[cur] + 1
            q.append(i)