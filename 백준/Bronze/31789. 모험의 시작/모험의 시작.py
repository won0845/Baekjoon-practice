n = int(input())
a, b = map(int, input().split())

yes = 0

for i in range(n):
    c, d = map(int, input().split())
    if c <= a and d > b:
        yes = 1
        break
if yes == 1:
    print("YES")
else:
    print("NO")