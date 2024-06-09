import sys

input = sys.stdin.readline
birth = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

n = int(input())

for i in range(n):
    _, date = map(str, input().split())
    month = int(date.split("/")[1])
    birth[month] += 1

for i in range(1, 13):
    print(i, birth[i])