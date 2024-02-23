n = int(input())
bag = 0

while n >= 0:
    if n % 5 == 0:  # 5로 나누어떨어지는 경우
        bag += (n // 5)  # 5kg 봉지로 나누어떨어지는 몫을 더함
        print(bag)
        break
    n -= 3  # 5kg 봉지로 정확히 나누어떨어지지 않으면 3kg을 빼고 시도
    bag += 1  # 3kg 봉지 하나 추가
else:  # 정확히 n kg을 만들 수 없는 경우
    print(-1)