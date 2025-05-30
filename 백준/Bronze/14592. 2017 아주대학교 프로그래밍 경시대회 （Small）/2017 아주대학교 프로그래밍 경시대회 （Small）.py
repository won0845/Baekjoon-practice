import sys

N = int(sys.stdin.readline())

participant = dict()

for i in range(1, N + 1):
    S, C, L = map(int, sys.stdin.readline().split())

    participant[i] = [S, C, L]

print(sorted(participant.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2]))[0][0])