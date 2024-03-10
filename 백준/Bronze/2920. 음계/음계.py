import sys

input = sys.stdin.readline

lis = list(map(int, input().split()))
answer = ""

if lis[0] == 1:
    tmp = lis[0]
    cnt = 0
    for i in range(len(lis)):
        if tmp == lis[i]:
            cnt += 1
            tmp += 1
        else:
            tmp += 1
    if cnt == 8:
        answer = "ascending"
elif lis[0] == 8:
    tmp = lis[0]
    cnt = 0
    for i in range(len(lis)):
        if tmp == lis[i]:
            tmp -= 1
            cnt += 1
        else:
            tmp -= 1
    if cnt == 8:
        answer = "descending"
if answer != "ascending" and answer != "descending":
    print("mixed")
else:
    print(answer)