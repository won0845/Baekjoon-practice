import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())

seq = [i for i in range(1, n + 1)]

for i in permutations(seq):
    print(*i)