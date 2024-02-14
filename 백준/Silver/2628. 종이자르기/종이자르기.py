import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

w, h = map(int, input().split())
wList = []
hList = []
sliceNum = int(input())

wList.append(w)
hList.append(h)

for _ in range(sliceNum):
    whSlice, cm = map(int, input().split())

    if whSlice == 0:
        hList.append(cm)
    elif whSlice == 1:
        wList.append(cm)

wList.sort()
hList.sort()

wMaxValue = wList[0]
for i in range(1, len(wList)):
    if wMaxValue< wList[i]-wList[i-1]:
        wMaxValue = wList[i]-wList[i-1]

hMaxValue = hList[0]
for i in range(1, len(hList)):
    if hMaxValue< hList[i]-hList[i-1]:
        hMaxValue = hList[i]-hList[i-1]

print(hMaxValue * wMaxValue)
