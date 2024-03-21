import sys

input = sys.stdin.readline

n = int(input())
S = set()

for _ in range(n):
    args = input().split()
    if args[0] == "add":
        S.add(int(args[1]))
    if args[0] == "check":
        if int(args[1]) in S:
            print(1)
        else:
            print(0)
    if args[0] == "remove":
        if int(args[1]) in S:
            S.remove(int(args[1]))
    if args[0] == "toggle":
        if int(args[1]) in S:
            S.remove(int(args[1]))
        else:
            S.add(int(args[1]))
    if args[0] == "all":
        S = {i for i in range(1, 21)}
    if args[0] == "empty":
        S.clear()
