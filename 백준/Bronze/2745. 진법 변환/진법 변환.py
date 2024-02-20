import sys

input = sys.stdin.readline

N, B = map(str, input().split())
B = int(B)
N = ''.join(reversed(N))
numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0
sum = 0

for i in range(len(N)):

    sum += B ** i * numbers.index(N[i])

print(sum)
