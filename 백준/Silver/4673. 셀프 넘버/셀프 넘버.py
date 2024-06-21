natural_n = set(range(1,10001))
generated_n = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_n.add(i)
self_n = sorted(natural_n.difference(generated_n))
for i in self_n:
    print(i)