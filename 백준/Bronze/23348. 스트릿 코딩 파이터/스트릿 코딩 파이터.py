a, b, c = map(int, input().split())
n = int(input())
maxV = 0

for i in range(n):
    hap = 0
    for j in range(3):
        k, l, r = map(int, input().split())
        hap += k*a + l*b + r*c
    maxV = max(hap, maxV)
print(maxV)