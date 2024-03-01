import sys
import math

input = sys.stdin.readline

n = int(input())
cha = []
trees = []
count = 0

for _ in range(n):
    trees.append(int(input()))
first = trees[0]

for i in range(1, len(trees)):
    a = trees[i]
    cha.append(a - first)
    first = a

g = cha[0]
for i in range(1, len(cha)):
    g = math.gcd(g, cha[i])


totaltree = (trees[-1] - trees[0]) // g + 1
print(totaltree - n)