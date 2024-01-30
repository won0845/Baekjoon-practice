import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

card = deque([])

for i in range(1, N + 1):
    card.append(i)

while len(card) !=1:
    card.popleft()
    back = card.popleft()
    card.append(back)

for i in card:
    print(i)