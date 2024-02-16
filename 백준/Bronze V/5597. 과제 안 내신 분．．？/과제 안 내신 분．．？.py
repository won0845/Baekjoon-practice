import sys

input = sys.stdin.readline

check = [0 for _ in range(30)]

for _ in range(28):
    a = int(input())
    check[a - 1] = a
for i in range(len(check)):
    if check[i] == 0:
        print(i+1)
