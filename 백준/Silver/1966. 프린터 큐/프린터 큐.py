import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    docNum, target = map(int, input().split())
    docs = list(map(int, input().split()))
    docs = deque([(i, idx) for idx, i in enumerate(docs)])
    cnt = 0

    while docs:
        a, b = docs.popleft()
        if docs and max(docs)[0] > a:
            docs.append((a, b))
        else:
            cnt += 1
            if b == target:
                print(cnt)