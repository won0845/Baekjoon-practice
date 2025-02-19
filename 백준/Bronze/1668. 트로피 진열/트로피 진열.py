n = int(input())
bp = []

count = 1
for i in range(n):
    bp.append(int(input()))

tmp = bp[0]

for i in range(1, n):
    if bp[i] > tmp:
        count+=1
        tmp = bp[i]

print(count)


tmp = bp[-1]
count = 1
for i in range(n-2,-1,-1):
    if bp[i] > tmp:
        count+=1
        tmp = bp[i]

print(count)