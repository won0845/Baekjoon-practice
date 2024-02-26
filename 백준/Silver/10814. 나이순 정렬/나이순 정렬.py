import sys

input = sys.stdin.readline
n = int(input())
member = []

for _ in range(n):
    a, b = map(str, input().split())
    member.append([int(a), b])

member.sort(key=lambda x: x[0])

for i in range(len(member)):
    print(member[i][0], member[i][1])