N = int(input())
X, Y, R = map(int, input().split())

left = X - R
right = X + R

A = 0
B = 0

for _ in range(N):
    v = int(input())
    if v == left or v == right:
        B += 1
    elif left < v < right:
        A += 1

print(A, B)
