n, k = map(int, input().split())

lst = []
seq = []
idx = 0

for i in range(n):
    lst.append(i + 1)

while lst:
    idx += k - 1
    if idx >= len(lst):
        idx %= len(lst)
    seq.append(str(lst.pop(idx)))

print("<"+", ".join(seq)+">")