import sys

input = sys.stdin.readline
n = int(input())
tmp = []

def seq(depth):
    if depth == n:
        print(*tmp)
    for i in range(1,n+1):
        if i not in tmp:
            tmp.append(i)
            seq(depth+1)
            tmp.pop()

seq(0)