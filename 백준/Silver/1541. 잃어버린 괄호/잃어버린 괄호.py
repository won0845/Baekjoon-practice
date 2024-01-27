import sys

input = sys.stdin.readline

lst = input().split("-")
sum1 = 0
total = []
for i in lst:
    tmp = i.split("+")
    for i in tmp:
        sum1 += int(i)
    total.append(sum1)
    sum1 = 0

val = total[0]
for i in range(1, len(total)):
    val -= total[i]

print(val)
