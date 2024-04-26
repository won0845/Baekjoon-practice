senN = int(input())
group = int(input())
lst = list(map(int, input().split()))
cha = []
lst.sort(reverse=True)
for i in range(1, len(lst)):
    cha.append((lst[i-1]) - lst[i])
cha.sort(reverse=True)
print(sum(cha[group-1:]))