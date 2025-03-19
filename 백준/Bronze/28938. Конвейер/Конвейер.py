n = int(input())
sum1 = sum(list(map(int, input().split())))


if sum1 < 0:
    print("Left")
elif sum1 == 0:
    print("Stay")
else:
    print("Right")