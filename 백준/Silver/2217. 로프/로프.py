n = int(input())
ropeList = []
maxV = 0
for _ in range(n):
    ropeList.append(int(input()))

ropeList.sort()
for i in range(n):
    if i == (n-1):
        maxV = max(ropeList[i],maxV)
    else:
        maxV = max(ropeList[i] * (n - i), maxV)

print(maxV)