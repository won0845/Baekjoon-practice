import sys

input = sys.stdin.readline
diction = {}
N = int(input())
card = map(int, input().split())
M = int(input())
card1 = list(map(int, input().split()))
card1set = set(card1)

for i in card1:
    diction[i] = 0

for i in card:
    if i in card1set:
        diction[i] += 1

for i in card1:
    print(diction[i], end=" ")
