import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

prest = []

while True:
    try:
        prest.append(int(input()))
    except:
        break


def preorder(root_idx, end_idx):
    if root_idx > end_idx:
        return

    right_idx = end_idx + 1

    for i in range(root_idx + 1, end_idx + 1):
        if prest[root_idx] < prest[i]:
            right_idx = i
            break

    preorder(root_idx + 1, right_idx - 1)
    preorder(right_idx, end_idx)
    print(prest[root_idx])


preorder(0, len(prest) - 1)
