import sys

input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == b and a == 0:
        break
    print("{}".format(a + b))
