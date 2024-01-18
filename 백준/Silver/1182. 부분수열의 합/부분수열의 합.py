N, S = map(int, input().split())
lst = list(map(int, input().split()))
combi = [[]]
count = 0

for num in lst:
    for j in range(len(combi)):
        combi.append(combi[j] + [num])

combi.pop(0)
for i in combi:
    if sum(i) == S:
        count += 1


print(count)