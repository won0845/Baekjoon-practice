import sys

input = sys.stdin.readline

N = int(input())
repeatCount = (N - 4) // 4

for _ in range(repeatCount):
    print("long", end=" ")

print("long int")
