N = int(input()) # 참여하는 사람
dice = 0

for _ in range(N):
    a, b, c = map(int, input().split()) # 주사위 세 개의 눈

    if a == b == c:
        dice = max(dice, 10000 + a * 1000)
    elif a == b:
        dice = max(dice, 1000 + a * 100)
    elif a == c:
        dice = max(dice, 1000 + a * 100)
    elif b == c:
        dice = max(dice, 1000 + b * 100)
    else:
        dice = max(dice, 100 * max(a, b, c))

print(dice)