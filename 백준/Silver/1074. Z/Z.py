import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
ans = 0


def divide(x, y, n):
    global ans
    if x == r and y == c:
        print(ans)
        exit(0)
    if n == 1:
        ans += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        ans += n * n
        return

    divide(x, y, n // 2)
    divide(x, y + n // 2, n // 2)
    divide(x + n // 2, y, n // 2)
    divide(x + n // 2, y + n // 2, n // 2)


N, r, c = map(int, input().split())
n = 2 ** N

cnt = 0

divide(0, 0, n)
