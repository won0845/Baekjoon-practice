# 테스트 케이스의 수 입력
T = int(input().strip())

# 각 테스트 케이스를 처리
for _ in range(T):
    # 문자열 입력
    s = input().strip()
    # 첫 번째 'D'의 위치 찾기
    try:
        position = s.index('D')
    except ValueError:
        # 'D'가 없으면 문자열의 길이를 출력
        position = len(s)
    # 위치 출력
    print(position)
