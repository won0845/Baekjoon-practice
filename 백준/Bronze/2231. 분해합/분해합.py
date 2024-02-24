n = int(input())

start = max(n - (len(str(n)) * 9), 0)
minV = 0
for i in range(start, n):
    temp = list(map(int, str(i)))
    hap = i + sum(temp)
    if n == hap:
        minV = i
        break

print(minV)