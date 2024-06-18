import sys

input = sys.stdin.readline

for _ in range(3):
    a = list(map(str, input().split()))
    cnt = a.count("0")

    if cnt == 0:
        print("E")
    elif cnt == 1:
        print("A")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("C")
    elif cnt == 4:
        print("D")