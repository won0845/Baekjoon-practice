n = int(input())

# 숫자에 7이 포함되는지 확인
contains_seven = '7' in str(n)

# 7로 나누어 떨어지는지 확인
divisible_by_seven = (n % 7 == 0)

# 조건에 따라 출력
if not contains_seven and not divisible_by_seven:
    print(0)
elif not contains_seven and divisible_by_seven:
    print(1)
elif contains_seven and not divisible_by_seven:
    print(2)
else:
    print(3)
