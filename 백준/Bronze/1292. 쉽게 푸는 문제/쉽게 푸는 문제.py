a, b = map(int, input().split())
hap = []
cnt = 0
for i in range(1, 1001):
    for _ in range(i):
        if cnt == 1000:
            break
        hap.append(i)
        cnt += 1

print(sum(hap[a-1:b]))