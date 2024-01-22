import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

cNum = int(input())
eNum = int(input())
tree = []

for _ in range(eNum):
    tree.append(list(map(int, input().split())))

root = list(range(cNum + 1))


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        root[a] = b
    else:
        root[b] = a


count = 0

for a, b in tree:
    if find(a) != find(b):
        union(a, b)
        count += 1

count = sum(1 for i in range(2, cNum + 1) if find(i) == find(1))

print(count)