import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()
a = {}
sum = 0
alpha = "abcdefghijklmnopqrstuvwxyz"


for k in range(0, len(alpha)):
    a[alpha[k]] = k + 1

for i in range(len(s)):
    sum += a[s[i]]*(31**i)
print(sum%1234567891)