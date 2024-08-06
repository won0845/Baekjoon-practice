n = int(input())
big = 0
for _ in range(n):
    a, b = map(int, input().split())
    big = max(big, a*b)
    
print(big)
    