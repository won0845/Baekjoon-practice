def solution(n):
    answer = []

    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            answer.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        answer.append(n)
    return answer
