import sys
from itertools import permutations

input = sys.stdin.readline

case = list(map(int, input().split()))
indx = 1

while case[0] != 0:
    tmp = []

    def seq(depth, indx):
        if depth == 6:
            print(*tmp)
            return

        for i in range(indx, len(case)):
            indx = i
            if case[i] not in tmp:
                tmp.append(case[i])
                seq(depth+1, indx)
                tmp.pop()

    seq(0, indx)
    case = list(map(int, input().split()))
    print()