a, b = map(int, input().split())
ans = 0
for i in range(1, a+1):
    v = str(i).count(str(b))
    ans += v
print(ans)