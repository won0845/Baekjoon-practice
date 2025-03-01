n, a, b = map(int, input().split())

ans = n // ( b - a)
if n % ( b - a) > 0:
    ans += 1
print(ans)
