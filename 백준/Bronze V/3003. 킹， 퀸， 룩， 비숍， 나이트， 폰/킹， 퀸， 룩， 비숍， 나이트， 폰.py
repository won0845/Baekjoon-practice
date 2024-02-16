c = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))
answer = [0] * 6
for i in range(len(c)):
    if c[i] == a[i]:
        continue
    else:
        answer[i] = c[i] - a[i]

print(' '.join(map(str, answer)))
