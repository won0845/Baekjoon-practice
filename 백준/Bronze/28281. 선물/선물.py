n, a = map(int, input().split())
lst = list(map(int, input().split()))

# 초기 최소값을 충분히 큰 값으로 설정
min_sum = float('inf')

# 연속된 두 날의 양말 가격 합의 최소값 찾기
for i in range(n - 1):
    current_sum = lst[i] + lst[i + 1]
    if current_sum < min_sum:
        min_sum = current_sum

# 최소값에 양말 개수 곱하기
result = min_sum * a
print(result)
