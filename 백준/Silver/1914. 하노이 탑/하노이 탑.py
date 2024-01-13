n = int(input())

def move(num, x, y):
    if num > 1:
        move(num - 1, x, 6 - x - y)
    if num <= 20:
        print(x, y)
    if num > 1:
        move(num - 1, 6 - x - y, y)

print(2 ** n - 1)

if n <= 20:
    move(n, 1, 3)