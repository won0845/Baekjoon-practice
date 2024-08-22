import sys
input = sys.stdin.readline

n = int(input())
hap = 0

for i in range(n):
    hap += int(input())-1
print(hap+1)