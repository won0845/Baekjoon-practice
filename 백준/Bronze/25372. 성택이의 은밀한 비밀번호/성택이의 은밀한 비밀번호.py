import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    bibun = input().strip()
    if 6 <= len(bibun) <= 9:
        print("yes")
    else:
        print("no")

