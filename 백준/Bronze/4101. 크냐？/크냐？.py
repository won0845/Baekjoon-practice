import sys
input = sys.stdin.readline
a, b = map(int, input().split())
while True:
    if a == 0 and b == 0:
        break
    if a > b:
        print("Yes")
    else:
        print("No")
    a, b = map(int, input().split())