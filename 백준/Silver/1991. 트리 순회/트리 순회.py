import sys

input = sys.stdin.readline


def preorder(node):
    if node != ".":
        left_node, right_node = BT[node][0], BT[node][1]
        print(node, end="")
        preorder(left_node)
        preorder(right_node)


def inorder(node):
    if node != ".":
        left_node, right_node = BT[node][0], BT[node][1]

        inorder(left_node)
        print(node, end="")
        inorder(right_node)


def postorder(node):
    if node != ".":
        left_node, right_node = BT[node][0], BT[node][1]
        postorder(left_node)
        postorder(right_node)
        print(node, end="")


n = int(input())
BT = {}
for i in range(n):
    root, left, right = map(str, input().split())
    BT[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')