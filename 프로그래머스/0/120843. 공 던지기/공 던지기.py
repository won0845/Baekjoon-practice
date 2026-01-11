def solution(numbers, k):
    n = len(numbers)
    pos = 0  # 0번부터 시작

    for _ in range(k-1):
        pos = (pos + 2) % n

    return numbers[pos]
