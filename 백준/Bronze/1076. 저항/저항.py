import sys

input = sys.stdin.readline

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = str(color.index(input().strip()))
b = str(color.index(input().strip()))
c = str(10**color.index(input().strip()))

print(int(a+b+c[1:]))
