import sys

input = sys.stdin.readline

n = input().strip()

alpha = "abcdefghijklmnopqrstuvwxyz"
lst = [-1] * len(alpha)

for i in range(len(n)):
    lst[alpha.find(n[i])] = n.index(n[i])
print(' '.join(map(str, lst)))