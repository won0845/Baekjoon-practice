import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    string = map(str, input().strip().split())
    for j in string:
        print(j[::-1])