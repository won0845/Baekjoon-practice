C = int(input())
lst = []
for i in range(C):
    lst.append(input())

for i in lst:
    count = 0
    values = list(map(int, i.split()))
    avg = sum(values[1:]) / values[0]

    for k in values[1:]:
        if k > avg:
            count += 1
    per = count / values[0] * 100
    print("%.3f" % per + "%")