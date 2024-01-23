import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V, E = map(int, input().split())
tree = []

root = list(range(V + 1))

for _ in range(E):
    tree.append(list(map(int, input().split())))

root = list(range(V + 1))


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


tree.sort(key=lambda x: x[2])

ans = 0

for a, b, c in tree:
    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)