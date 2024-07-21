sc = 0
so = 0
scli = []

for i in range(4):
    scli.append(int(input()))
scli.sort(reverse=True)
for i in range(3):
    sc += scli[i]
so = int(input())
so2 = int(input())
if so > so2:
    print(sc+so)
else:
    print(sc+so2)