import sys

input = sys.stdin.readline

a, b = map(int, input().split())

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
c = setA - setB
d = setB - setA

print(len(c)+len(d))