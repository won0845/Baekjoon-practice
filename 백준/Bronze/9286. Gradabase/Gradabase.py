import sys

input = sys.stdin.readline
for i in range(1, int(input()) + 1) :
    print(f"Case {i}:")
    for _ in range(int(input())) :
        g = int(input())
        if g + 1 > 0 and g + 1 < 7 : print(g + 1)