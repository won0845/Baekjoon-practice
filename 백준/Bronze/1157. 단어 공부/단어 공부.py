import sys

count_dict = {}
input = sys.stdin.readline
str = input().strip().upper()
count = 0

for i in str:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

maxV = max(count_dict.values())

for i in count_dict.values():
    if maxV == i:
        count += 1

if count > 1:
    print("?")
else:
    print(max(count_dict, key=count_dict.get))
