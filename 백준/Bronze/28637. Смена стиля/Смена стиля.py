import re

def camel_to_snake(name):
    # 대문자 앞에 _ 추가 후 소문자로 변환
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

# n 입력받기
n = int(input())

# n번 반복하며 입력받기
for _ in range(n):
    value = input().strip()
    print(camel_to_snake(value))