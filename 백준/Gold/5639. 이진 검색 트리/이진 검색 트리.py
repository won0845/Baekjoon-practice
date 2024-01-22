import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break


def postorder(root_idx, end_idx):
    if root_idx > end_idx:
        return

    global preorder

    right_start = end_idx + 1

    for i in range(root_idx + 1, end_idx + 1):
        if preorder[root_idx] < preorder[i]:
            right_start = i
            break
    postorder(root_idx + 1, right_start - 1)

    postorder(right_start, end_idx)

    print(preorder[root_idx])


postorder(0, len(preorder) - 1)