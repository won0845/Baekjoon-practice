import sys

input = sys.stdin.readline

n = int(input())
dic = {1: 1, 2: 2, 3: 3, 4: 5}

for i in range(5, n + 1):
    dic[i] = dic[i - 1] + dic[i - 2]

print(dic[n] % 10007)
