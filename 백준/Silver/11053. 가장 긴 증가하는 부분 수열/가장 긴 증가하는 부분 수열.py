import bisect

n = int(input())
arr = list(map(int, input().split()))
sub = []

for i in arr:
    pos = bisect.bisect_left(sub, i)
    if pos == len(sub):
        sub.append(i)
    else:
        sub[pos] = i
        
print(len(sub))